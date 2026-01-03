"""
@author: Lzm
@date: 2025年12月26日
"""
from datetime import datetime

# 导入系统环境变量
import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()  # 从 .env 文件加载环境变量

# 1.编排Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个有帮助的助手，现在的时间是 {now}"),
    ("user", "{query}"),
]).partial(now=datetime.now())

# 2.使用LLM和ChatModel
llm = ChatOpenAI(model="gpt-4o")
ai_msg = llm.invoke(prompt.invoke({"query": "介绍一下自己(具体是什么模型)，顺便说说今天的日期"}))
# print(ai_msg)

# 3.使用流式输出
response = llm.stream(prompt.invoke({"query": "你能简单介绍下LLM和LLMOps吗?"}))
for chunk in response:
    print(chunk.content, flush=True, end="")


