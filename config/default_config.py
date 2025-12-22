"""
@Time    : 2024/4/5 18:50
@Author  : thezehui@gmail.com
@File    : default_config.py
"""
# 应用默认配置项
DEFAULT_CONFIG = {
    # wft配置
    "WTF_CSRF_ENABLED": "False",
    
    # SQLAlchemy数据库配置
    "SQLALCHEMY_DATABASE_URI": "", # 默认数据库连接URI为空
    "SQLALCHEMY_POOL_SIZE": 30, # 默认数据库连接池大小为30
    "SQLALCHEMY_POOL_RECYCLE": 3600, # 默认一小时回收数据库连接
    "SQLALCHEMY_ECHO": "True",      # 默认开启SQLAlchemy的SQL日志输出
}
