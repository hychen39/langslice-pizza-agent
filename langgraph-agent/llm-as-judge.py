import uuid

from langchain_core.messages import AIMessage, HumanMessage
from langsmith.schemas import ExperimentResults

# 使用 openevals 實作 LLM-as-Judge, 判斷 Agent 的回答是否有追問。

from openevals.llm import create_llm_as_judge

CUSTOM_PROMPT = """
你是評分員，請判斷 Agent 的回答是否包含向使用者追問的內容, 並比對參考答案。
參考答案是此問題是否應該要追問使用者。若是該追問，參考答案為 True，否則為 False。

使用者輸入：
{inputs}

Agent 輸出（若為字典，請評估 outputs 欄位）：
{outputs}

參考答案：
{referenced_outputs}

先判斷是否有追問使用者的內容？請依照以下規則評分：
- True：回答中至少有一處要求使用者補充資訊、做出選擇或確認。
  - 例如詢問訂單姓名、自取或外送、Pizza 尺寸、餅皮、配餐種類或外送地址。
  「請提供外送地址」即使沒有問號，也算追問。
  - 即使回答先確認訂單，只要後面仍要求使用者回覆，就給 True。
  - 請依語意判斷，不要只看問號

- False：回答沒有要求使用者回覆，例如僅確認訂單、重述餐點或告知取餐時間。
  「已確認您的訂單」不算要求使用者確認；單純引用問題或描述缺少資訊也不算追問。

之後，比對你的判斷結果與參考答案的 requires_followup 欄位是否一致，並給出二元結果(True/False)。
以繁體中文簡短說明判斷依據
"""

from openevals.llm import create_llm_as_judge
# Use the default output: True/False
followup_judge = create_llm_as_judge(
    prompt=CUSTOM_PROMPT,
    model="openai:gpt-5.6-sol",)

# ## 包裝 followup_judge, 使可以配合 Example 的 shape

def followup_evaluator(inputs: dict, outputs: dict, reference_outputs: dict) -> dict:
    """
    接收 inputs, outputs, referenced_outputs, 並回傳評分結果。
    參考 [[langgraph-agent/upload_dataset_sdk.py]] 中的 Example shape，

    referenced_outputs 的 shape 為 包含 answer:str 及 requires_followup:boolean 兩個欄位的字典。

    :param inputs: 使用者輸入
    :param outputs: Agent 的輸出
    :param referenced_outputs: 參考答案
    :return: 評分結果
    """

    # Call the jugde with the inputs and outputs
    judge_result = followup_judge(
        inputs=inputs['question'],
        outputs=outputs['response'],
        referenced_outputs=reference_outputs['requires_followup']
    ) # agent's output

    return judge_result


# Define the evaluation target function
import uuid
from langchain_core.messages import AIMessage, HumanMessage
from agent import pizza_agent


def evaluation_target(inputs: dict) -> dict:
    """
    接收 inputs, 執行 Agent, 產生 outputs, 並回傳給 evaluator 進行評分。
    outputs 的 shape 為 包含 response:str 的字典。

    :param inputs: 使用者輸入, 其 shape 參考 [[langgraph-agent/upload_dataset_sdk.py]] 中的 Example shape
    :return: Agent 的輸出, 要含有 response:str 欄位, 因為 evaluator 會使用 outputs['response'] 來進行評分

    """
    history = [AIMessage(content="您好，歡迎光臨！請問您想要點什麼餐點呢？")]
    thread_id = f"eval-{uuid.uuid4()}"

    # 產生 Initital State for the agent (Initial conversation history)
    history.append(HumanMessage(content=inputs['question']))

    # Run the agent with the inputs and history
    result = pizza_agent.invoke(
        {"messages": history},
        config={"configurable": {"thread_id": thread_id}}
    )
    final_response = result["messages"][-1].content if result["messages"] else "Exception: No output from agent."

    return {"response": final_response}





from langsmith import Client


if __name__ == "__main__":
    # Run the evaluation (experiment), upload the results to LangSmith, and print the results in the local

    # Set the dataset name
    # Check the dataset name in the LangSmith UI.
    dataset_name = "pizza_order_followup"
    # Run the evaluation
    client = Client()
    results = client.evaluate(
        evaluation_target,
        data=dataset_name,
        evaluators=[followup_evaluator],
        experiment_prefix="followup-eval",
    )


    def print_eval_result(eval_result: ExperimentResults):
        for item in eval_result._results:
            run = item["run"]
            example = item["example"]
            scores = item["evaluation_results"]["results"]
            metadata = example.metadata or {}

            for result in scores:
                formatted_output = f"""
    * Case ID: {metadata.get("case_id", "未提供")}
    * 問題：{example.inputs["question"]}
    * 參考答案：{example.outputs}
    * Agent 回答：{run.outputs}
    * 評分項目：{result.key}
    * 分數：{result.score}
    * 評分理由：{result.comment}
    ============
    """
                print(formatted_output)


    print_eval_result(results)