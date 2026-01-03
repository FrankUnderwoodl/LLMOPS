# """
# @author: Lzm
# @date: 2025年12月27日
# """
# from langchain_core.pydantic_v1 import BaseModel, Field
#
# # 1.创建一个json数据结构，用于告诉大语言模型这个json长什么样子
# class Joke(BaseModel):
#     # 冷笑话
#     joke: str = Field(description="回答用户的冷笑话")
#     # 冷笑话的笑点
#     punchline: str = Field(description="这个冷笑话的笑点")
#
# # 输出解析器，其实就是用来定义模型输出的格式的啦
# parser = JsonOutputParser(pydantic_object=Joke)
#
# # 2.构建一个提示模板
# prompt = ChatPromptTemplate.from_template("请根据用户的提问进行回答。\n{format_instructions}\n{query}").partial(
#     format_instructions=parser.get_format_instructions())
#
# print(prompt.format(query="请讲一个关于程序员的冷笑话"))
