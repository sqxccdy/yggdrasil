from langchain_openai import ChatOpenAI
import os

os.environ["TENCENT_CLOUD_API_KEY"] = "sk-Pb23pgZpd95uM5wMZ8EcbILoJZiE6I8f0eKRZSaF9hInTp3L"

llm = ChatOpenAI(
    model="deepseek-v3",
    base_url="https://api.lkeap.cloud.tencent.com/v1",
    api_key=os.getenv("TENCENT_CLOUD_API_KEY")
)

response = llm.invoke("你好？")
print(response.content)