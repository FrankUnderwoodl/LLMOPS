"""
@author: Lzm
@date: 2025年12月01日
"""
from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
from injector import Injector  # 获取依赖注入器，里面装着所有的依赖，你可以看成是IOC容器

# from internal.extension import db
from internal.router import Router
from internal.server import Http
from pkg.sqlalchemy import SQLAlchemy
from app.http.module import ExtensionModule

injector = Injector([ExtensionModule()])

# 将.env这个文件加载到环境变量中
import dotenv

dotenv.load_dotenv()

# 导入配置类
from config import Config

conf = Config()


# 创建HTTP应用实例，并注入路由管理器、配置类、数据库实例、迁移实例等依赖
app = Http(__name__,
           config=conf,
           router=injector.get(Router),
           db=injector.get(SQLAlchemy),
           migrate=injector.get(Migrate),
           )

if __name__ == "__main__":
    app.run(debug=True)
