"""
@author: Lzm
@date: 2025年12月22日
"""
import uuid
from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy
from injector import inject

from internal.model.app import App


@inject
@dataclass
class AppService:
    """应用服务逻辑"""

    db: SQLAlchemy

    def create_app(self) -> App:
        with self.db.auto_commit(): # 这里会自动提交事务
            # 1.创建模型的实体类
            app = App(name="测试机器人", account_id=uuid.uuid4(), icon="", description="这是一个简单的聊天机器人")
            # 2.将实体类添加到session会话中，并提交事务(这里是增加操作)
            self.db.session.add(app)
        return app
