"""
@author: Lzm
@date: 2025年12月10日
"""
from enum import Enum


# 这里先继承自str是因为可以str的__str__方法可以在Enum中覆盖，从而实现更好的字符串表现形式，比如:
class HTTPCode(str, Enum):
    """HTTP状态码枚举类"""

    SUCCESS = "success"  # 成功状态
    FAIL = "fail"  # 失败状态
    NOT_FOUND = "not_found"  # 未找到
    UNAUTHORIZED = "unauthorized"  # 未授权
    FORBIDDEN = "forbidden"  # 无权限
    VALIDATE_ERROR = "validate_error"  # 数据验证错误
