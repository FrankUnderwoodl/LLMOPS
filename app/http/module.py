"""
@author: Lzm
@date: 2025年12月21日
"""
from flask_migrate import Migrate
from injector import Module, Binder

from internal.extension import db, migrate
from pkg.sqlalchemy import SQLAlchemy


# 这里是已经实例好的扩展模块，然后进行依赖注入
class ExtensionModule(Module):
    """扩展模块的依赖注入"""

    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)  # 导入数据库扩展，进行初始化，这里的db是SQLAlchemy的实例，这里这么写是因为作用就是将db绑定到依赖注入器中
        binder.bind(Migrate, to=migrate)