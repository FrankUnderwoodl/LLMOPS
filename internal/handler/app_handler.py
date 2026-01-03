"""
@author: Lzm
@date: 2025年12月01日
"""
import uuid
from dataclasses import dataclass

from injector import inject
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from internal.service.app_service import AppService
from pkg.response import success_json, validate_error_json, success_message


@inject
@dataclass
class AppHandler:
    """应用控制器"""

    app_service: AppService

    def create_app(self):
        """调用service层创建一个应用(其实就是往数据库插入一条记录)"""
        app = self.app_service.create_app()
        return success_message({"app_id": str(app.id), "app_name": app.name})

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用已经成功获取，名字是{app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功修改，修改的名字是:{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，id为:{app.id}")

    def chatToChatGPT(self):
        """与ChatGPT进行对话的接口"""

        # 1. fuck the front
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 2.编写提示词
        prompt = ChatPromptTemplate.from_template("{query}")
        llm = ChatOpenAI(model="gpt-3.5-turbo")
        parser = StrOutputParser()

        # 3.创建链
        chain = prompt | llm | parser
        content = chain.invoke({"query": req.query})

        return success_json({"content": content})

    def ping(self):
        """返回pong字符串，表示应用存活"""
        raise FailException()
