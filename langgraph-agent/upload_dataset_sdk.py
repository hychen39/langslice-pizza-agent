

# 訂單資訊不足，需要追問的 examples
pizza_order_follow_up = [
  {
    "inputs": {
      "question": "我要自取一個小尺寸、手拋餅皮的原味起司 Pizza，就這些，請幫我下單。"
    },
    "outputs": {
      "answer": "請問訂單要登記什麼名字？",
      "requires_followup": True
    },
    "metadata": {
      "case_id": "PIZZA_FOLLOWUP_001",
      "missing_field": "customer_name"
    }
  },
  {
    "inputs": {
      "question": "我叫小陳，要一個小尺寸、手拋餅皮的原味起司 Pizza，就這些，請幫我下單。"
    },
    "outputs": {
      "answer": "請問您要自取還是外送？",
      "requires_followup": True
    },
    "metadata": {
      "case_id": "PIZZA_FOLLOWUP_002",
      "missing_field": "order_type"
    }
  },
  {
    "inputs": {
      "question": "我叫小陳，要自取一個手拋餅皮的原味起司 Pizza，就這些，請幫我下單。"
    },
    "outputs": {
      "answer": "請問 Pizza 要小、中還是大尺寸？",
      "requires_followup": True
    },
    "metadata": {
      "case_id": "PIZZA_FOLLOWUP_003",
      "missing_field": "size"
    }
  },
  {
    "inputs": {
      "question": "我叫小陳，要自取一個小尺寸的原味起司 Pizza，就這些，請幫我下單。"
    },
    "outputs": {
      "answer": "請問您想選哪一種餅皮？",
      "requires_followup": True
    },
    "metadata": {
      "case_id": "PIZZA_FOLLOWUP_004",
      "missing_field": "crust"
    }
  },
  {
    "inputs": {
      "question": "我叫小陳，要外送一個大尺寸、手拋餅皮的原味起司 Pizza，就這些，請幫我下單。"
    },
    "outputs": {
      "answer": "請問外送的街道地址是什麼？",
      "requires_followup": True
    },
    "metadata": {
      "case_id": "PIZZA_FOLLOWUP_005",
      "missing_field": "address"
    }
  }
]

pizza_order_normal = [
  {
    "inputs": {
      "question": "我叫小陳，要自取一個小尺寸、手拋餅皮的原味起司 Pizza，就這些，請幫我下單。"
    },
    "outputs": {
      "answer": "已確認您的訂單，小陳：一個小尺寸、手拋餅皮的原味起司 Pizza，自取，預計 15–20 分鐘後可取餐。",
      "requires_followup": False
    },
    "metadata": {
      "case_id": "PIZZA_NO_FOLLOWUP_001",
      "requires_followup": False
    }
  },
  {
    "inputs": {
      "question": "訂單登記小林，我要自取一個中尺寸、手拋餅皮的 Pizza，保留標準起司，不加其他配料。請直接下單。"
    },
    "outputs": {
      "answer": "已確認您的訂單，小林：一個中尺寸、手拋餅皮的原味起司 Pizza，自取，預計 15–20 分鐘後可取餐。",
      "requires_followup": False
    },
    "metadata": {
      "case_id": "PIZZA_NO_FOLLOWUP_002",
      "requires_followup": False
    }
  },
  {
    "inputs": {
      "question": "我是小王，要兩個大尺寸、手拋餅皮的原味起司 Pizza，我會到店自取。就這樣，確認下單。"
    },
    "outputs": {
      "answer": "已確認您的訂單，小王：兩個大尺寸、手拋餅皮的原味起司 Pizza，自取，預計 15–20 分鐘後可取餐。",
      "requires_followup": False
    },
    "metadata": {
      "case_id": "PIZZA_NO_FOLLOWUP_003",
      "requires_followup": False
    }
  },
  {
    "inputs": {
      "question": "我叫小李，要自取一個中尺寸、手拋餅皮的 Pizza，標準起司之外再加 extra cheese。沒有其他需求，請幫我下單。"
    },
    "outputs": {
      "answer": "已確認您的訂單，小李：一個中尺寸、手拋餅皮、加 extra cheese 的 Pizza，自取，預計 15–20 分鐘後可取餐。",
      "requires_followup": False
    },
    "metadata": {
      "case_id": "PIZZA_NO_FOLLOWUP_004",
      "requires_followup": False
    }
  },
  {
    "inputs": {
      "question": "請登記小張，我要自取一個大尺寸、手拋餅皮的原味起司 Pizza，請烤熟一點。就這些，請確認下單。"
    },
    "outputs": {
      "answer": "已確認您的訂單，小張：一個大尺寸、手拋餅皮的原味起司 Pizza，備註烤熟一點，自取，預計 15–20 分鐘後可取餐。",
      "requires_followup": False
    },
    "metadata": {
      "case_id": "PIZZA_NO_FOLLOWUP_005",
      "requires_followup": False
    }
  }
]

side_drink_order_followup = [
  {
    "inputs": {
      "question": "我要自取一份 garlic knots (6)，只訂配餐，就這些，請幫我下單。"
    },
    "outputs": {
      "answer": "請問訂單要登記什麼名字？",
      "requires_followup": True
    },
    "metadata": {
      "case_id": "SIDE_DRINK_FOLLOWUP_001",
      "missing_field": "customer_name",
      "requires_followup": True
    }
  },
  {
    "inputs": {
      "question": "我叫小林，只要兩杯 fountain drink，就這些，請幫我下單。"
    },
    "outputs": {
      "answer": "請問您要自取還是外送？",
      "requires_followup": True
    },
    "metadata": {
      "case_id": "SIDE_DRINK_FOLLOWUP_002",
      "missing_field": "order_type",
      "requires_followup": True
    }
  },
  {
    "inputs": {
      "question": "我叫小王，要自取，今天只想訂一份配餐，不要 Pizza，請幫我下單。"
    },
    "outputs": {
      "answer": "請問您想訂哪一種配餐？",
      "requires_followup": True
    },
    "metadata": {
      "case_id": "SIDE_DRINK_FOLLOWUP_003",
      "missing_field": "item",
      "requires_followup": True
    }
  },
  {
    "inputs": {
      "question": "我叫小李，要外送四份 garlic knots (6)，不要 Pizza，就這些，請確認下單。"
    },
    "outputs": {
      "answer": "請問外送的街道地址是什麼？",
      "requires_followup": True
    },
    "metadata": {
      "case_id": "SIDE_DRINK_FOLLOWUP_004",
      "missing_field": "address",
      "requires_followup": True
    }
  },
  {
    "inputs": {
      "question": "我要到店自取三杯 fountain drink，不需要其他餐點，請直接下單。"
    },
    "outputs": {
      "answer": "請問訂單要登記什麼名字？",
      "requires_followup": True
    },
    "metadata": {
      "case_id": "SIDE_DRINK_FOLLOWUP_005",
      "missing_field": "customer_name",
      "requires_followup": True
    }
  }
]


# 訂單資訊 OK, 不需要追問
side_drink_order_normal = [
  {
    "inputs": {
      "question": "我叫小陳，要自取一份 garlic knots (6)，只訂這個，請幫我下單。"
    },
    "outputs": {
      "answer": "已確認您的訂單，小陳：一份 garlic knots (6)，自取，預計 15–20 分鐘後可取餐。",
      "requires_followup": False
    },
    "metadata": {
      "case_id": "SIDE_DRINK_NO_FOLLOWUP_001",
      "requires_followup": False
    }
  },
  {
    "inputs": {
      "question": "訂單登記小林，我要自取兩杯 fountain drink，就這些，確認下單。"
    },
    "outputs": {
      "answer": "已確認您的訂單，小林：兩杯 fountain drink，自取，預計 15–20 分鐘後可取餐。",
      "requires_followup": False
    },
    "metadata": {
      "case_id": "SIDE_DRINK_NO_FOLLOWUP_002",
      "requires_followup": False
    }
  },
  {
    "inputs": {
      "question": "我是小王，要一份 caesar salad 和一份 mozzarella sticks (6)，我會到店自取。不要 Pizza，請直接下單。"
    },
    "outputs": {
      "answer": "已確認您的訂單，小王：一份 caesar salad 和一份 mozzarella sticks (6)，自取，預計 15–20 分鐘後可取餐。",
      "requires_followup": False
    },
    "metadata": {
      "case_id": "SIDE_DRINK_NO_FOLLOWUP_003",
      "requires_followup": False
    }
  },
  {
    "inputs": {
      "question": "我叫小李，要自取一份 cannoli 和一杯 fountain drink，沒有其他需求，請幫我下單。"
    },
    "outputs": {
      "answer": "已確認您的訂單，小李：一份 cannoli 和一杯 fountain drink，自取，預計 15–20 分鐘後可取餐。",
      "requires_followup": False
    },
    "metadata": {
      "case_id": "SIDE_DRINK_NO_FOLLOWUP_004",
      "requires_followup": False
    }
  },
  {
    "inputs": {
      "question": "請登記小張，我要一杯 fountain drink，到店自取。只要飲料，請確認下單。"
    },
    "outputs": {
      "answer": "已確認您的訂單，小張：一杯 fountain drink，自取，預計 15–20 分鐘後可取餐。",
      "requires_followup": False
    },
    "metadata": {
      "case_id": "SIDE_DRINK_NO_FOLLOWUP_005",
      "requires_followup": False
    }
  }
]

from langsmith import Client
from dotenv import load_dotenv

def upload_dataset():

    # Note: 相同的 dataset name 不能重覆上傳，否則會產生例外:
    # langsmith.utils.LangSmithConflictError:
    # Conflict for /datasets. HTTPError('409 Client Error: Conflict for url: https://api.smith.langchain.com/datasets',
    # '{"detail":"Dataset with this name already exists."}')

    # Combine multiple examples
    examples = pizza_order_follow_up[0:2] + pizza_order_normal[0:2]
    dataset_name = "pizza_order_followup"
    client = Client()

    dataset = client.create_dataset(dataset_name,
                                    description="測試 Pizza follow up 功能 ")
    # Create examples
    response = client.create_examples(dataset_id=dataset.id,
                           examples=examples)

    print(f"成功上傳：{response['count']} 筆")
    print(f"Example IDs：{response['example_ids']}")
    print(f"資料版本時間：{response.get('as_of')}")


if __name__ == "__main__":
    load_dotenv(verbose=True)
    upload_dataset()
