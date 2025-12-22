"""
@author: Lzm
@date: 2025年12月03日
@describe: 所谓的路由管理器，就是将handler中的函数进行url绑定，然后注册到flask应用中
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject  # 这个装饰器表示这个类是可以被依赖注入框架进行管理的，你可以把它看成是一个单例然后被注入到其他类中
@dataclass # 使用dataclass简化类的定义
class Router:
    """路由管理器"""

    # 这里是实例属性，底层通过依赖注入框架进行赋值,注意这里是实例属性，因为使用了@dataclass，底层会自动生成__init__方法
    app_handler: AppHandler

    def register_routes(self, app: Flask):
        """给后端程序开始注册路由"""

        # 1.创建蓝图(目的是给app程序注册路由)
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 2.将url和视图函数进行绑定给蓝图
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)
        bp.add_url_rule("/app/completion", methods = ["POST"], view_func=self.app_handler.chatToChatGPT)
        bp.add_url_rule("/app/create", methods = ["POST"], view_func=self.app_handler.create_app)

        # 3.将蓝图注册到app程序中
        app.register_blueprint(bp)
