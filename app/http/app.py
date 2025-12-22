"""
@author: Lzm
@date: 2025年12月01日
"""
from flask_sqlalchemy import SQLAlchemy
from injector import Injector, Module  # 获取依赖注入器，里面装着所有的依赖，你可以看成是IOC容器

from internal.router import Router
from internal.server import Http

injector = Injector()

# 将.env这个文件加载到环境变量中
import dotenv

dotenv.load_dotenv()

# 导入配置类
from config import Config

conf = Config()

# 导入数据库扩展，进行初始化，这里的db是SQLAlchemy的实例，这里这么写是因为作用就是将db绑定到依赖注入器中
from internal.extension import db
class DatabaseModule(Module):
    def configure(self, binder):
        binder.bind(SQLAlchemy, to=db)


# 创建HTTP应用实例，并注入路由管理器、配置类、数据库实例等依赖
app = Http(__name__, config=conf, router=injector.get(Router), db=injector.get(SQLAlchemy))

if __name__ == "__main__":
    app.run(debug=True)
