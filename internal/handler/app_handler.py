"""
@author: Lzm
@date: 2025年12月01日
"""
from dataclasses import dataclass

from injector import inject
from openai import OpenAI

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from internal.service.app_service import AppService
from pkg.response import success_json, validate_error_json


@dataclass
@inject
class AppHandler:
    """应用控制器"""

    app_service: AppService

    def create_app(self):
        """调用service层创建一个应用(其实就是往数据库插入一条记录)"""
        app = self.app_service.create_app()
        return success_json({"app_id": str(app.id), "app_name": app.name})

    def chatToChatGPT(self):
        """与ChatGPT进行对话的接口"""

        # 1. fuck the front
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # extract the query value from the req object
        user_query = req.query.data

        # 2. 调用ChatGPT API获取响应
        client = OpenAI()
        # 3. 返回响应给用户
        # noinspection PyTypeChecker
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content": "你是OpenAI开发的聊天机器人，请根据用户的输入回复对应的信息，请你在结果最后面加上‘——Lzm’"},
                {"role": "user", "content": user_query},
            ])
        content = completion.choices[0].message.content

        # 封装进固定格式返回
        # resp = Response(code=HTTPCode.SUCCESS, message="请求成功", data={"content": content})

        return success_json({"content": content})

    def ping(self):
        """返回pong字符串，表示应用存活"""
        raise FailException()
