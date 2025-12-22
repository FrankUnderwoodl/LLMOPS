"""
@author: Lzm
@date: 2025年12月10日
"""
import os
from typing import Any

from config.default_config import DEFAULT_CONFIG


# 需求：定义一个函数，可以从环境变量获取配置项(字符串、值)，如果没有则使用默认值
def _get_env_or_default(key: str) -> Any:
    """从环境变量中获取配置项，如果找不到则返回默认值"""
    return os.getenv(key, DEFAULT_CONFIG.get(key))

# 获取环境变量中的布尔值配置项
def _get_bool_env_or_default(key: str) -> bool:
    """从环境变量中获取布尔值型的配置项，如果找不到则返回默认值"""
    value: str = _get_env_or_default(key)
    return value.lower() == "true" if value is not None else False  # 如果value是个空值的话，直接返回False



class Config:
    """配置类，存放全局配置"""

    def __init__(self):
        # 关闭Flask的CSRF保护机制
        self.WTF_CSRF_ENABLED = _get_bool_env_or_default("WTF_CSRF_ENABLED")

        # 配置数据库配置
        self.SQLALCHEMY_DATABASE_URI = _get_env_or_default("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": int(_get_env_or_default("SQLALCHEMY_POOL_SIZE")),
            "pool_recycle": int(_get_env_or_default("SQLALCHEMY_POOL_RECYCLE")),
        }
        self.SQLALCHEMY_ECHO = _get_bool_env_or_default("SQLALCHEMY_ECHO")

