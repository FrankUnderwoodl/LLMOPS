"""
@author: Lzm
@date: 2025年12月03日
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config
from internal.exception import CustomException
from internal.router import Router
from pkg.response import Response, json, HTTPCode


# 所有关于flask框架的配置，都在这个类中进行
class Http(Flask):
    """HTTP服务器类，继承自Flask"""

    def __init__(self, *args, config: Config, db:SQLAlchemy, router: Router, **kwargs):
        """Flask的初始化方法"""

        # 1.这里是调用父类的初始化方法，父类是Flask
        super().__init__(*args, **kwargs)
        
        # 2.加载路由配置
        router.register_routes(self)

        # 3.统一错误处理(第一个参数是错误码或者异常类，第二个参数是对应的处理函数)
        self.register_error_handler(Exception, self._request_exception_handler)

        # 4.加载config配置
        self.config.from_object(config)

        # 5.初始化数据库
        db.init_app(self)


    # 统一异常处理函数
    def _request_exception_handler(self, e: Exception):
        """异常两种情况，一种是自己定义的异常，一种是系统异常(比如系统异常、数据库异常等)"""

        # 如果是开发阶段的话，直接抛出异常，方便调试
        if self.debug or os.getenv("FLASK_ENV") == "development":
            raise e
        else:
            # 1.自己的异常
            if isinstance(e, CustomException):
                print("捕获到自定义异常：", e)
                return json(Response(
                    code=e.code,
                    message=e.message,
                    data=e.data
                ))
            # 2.系统异常
            else:
                print("捕获到系统异常：", e)
                return json(Response(
                    code=HTTPCode.FAIL,
                    message=str(e),
                    data={}
                ))

            # return e.message # 这是默认的错误信息
