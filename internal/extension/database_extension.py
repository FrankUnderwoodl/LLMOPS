"""
@author: Lzm
@date: 2025年12月21日
"""
from pkg.sqlalchemy import SQLAlchemy

# from flask_sqlalchemy import SQLAlchemy

# 这个类的作用是封装数据库操作，比如增删改查等，
# 注意这里不能依赖注入，因为@injector装饰器只能作用在类上，不能作用在模块变量上
db = SQLAlchemy()

