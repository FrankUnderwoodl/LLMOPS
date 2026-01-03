"""
@author: Lzm
@date: 2025年12月25日
"""
from datetime import datetime

from langchain_core.prompts import PromptTemplate, MessagesPlaceholder, ChatPromptTemplate, HumanMessagePromptTemplate

# PromptTemplate和ChatPromptTemplate的使用区别是什么？
# PromptTemplate 像发送一条消息，ChatPromptTemplate 像进行一场对话


# 使用PromptTemplate组件创建提示模板(文本提示模板)
prompt = PromptTemplate.from_template("请讲一个关于{topic}的冷笑话")
print(prompt.format(topic="编程"))  # 请讲一个关于编程的冷笑话，这里使用了PromptTemplate组件，

prompt_value = prompt.invoke({"topic": "数学"})  # 提示值可以转成字符串或消息列表
print(prompt_value.to_string())  # 请讲一个关于数学的冷笑话
print(prompt_value.to_messages())  # [HumanMessage(content='请讲一个关于数学的冷笑话')]

print("-----分割线-----")

# 使用ChatPromptTemplate组件创建聊天提示模板(消息提示模板)
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个有趣的笑话生成器，现在的时间是{current_time}"),  # 在 ChatPromptTemplate.from_messages() 中，当使用元组形式 ("system", "...") 时，LangChain 会自动将其转换为 SystemMessagePromptTemplate 对象
    MessagesPlaceholder("chat_history"), # 有时候这里可能还有其他的消息，不确定
    HumanMessagePromptTemplate.from_template("请讲一个关于{topic}的冷笑话"),
]).partial(current_time=datetime.now())

chat_prompt = chat_prompt.invoke({
    # "current_time": datetime.now(),
    "chat_history": [
        {"role": "user", "content": "你好！"},
        {"role": "assistant", "content": "你好！很高兴见到你。"},
    ],
    "topic": "人工智能"
})
# print(chat_prompt)
print(chat_prompt.to_string())
