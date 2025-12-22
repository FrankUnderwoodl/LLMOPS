"""
@author: Lzm
@date: 2025年12月18日
"""
from dataclasses import field, dataclass
from typing import Any

from pkg.response import HTTPCode


@dataclass
class CustomException(Exception):
    """自定义异常类，用于处理应用中的特定错误情况"""

    # 默认的HTTP状态码为失败
    code: HTTPCode = HTTPCode.FAIL
    # 默认的错误信息
    message: str = "这是默认的错误信息"
    # 默认的data为空字典
    data: Any = field(default_factory=dict)


class FailException(CustomException):
    """通用失败异常"""
    pass

class NotFoundException(CustomException):
    """未找到数据异常(比如访问了不存在的资源)"""
    code = HTTPCode.NOT_FOUND

class UnauthorizedException(CustomException):
    """未授权异常(比如访问了需要登录才能访问的资源)"""
    code = HTTPCode.UNAUTHORIZED

class ForbiddenException(CustomException):
    """无权限异常(比如访问了没有权限访问的资源)"""
    code = HTTPCode.FORBIDDEN

class ValidateErrorException(CustomException):
    """数据验证异常(比如前端传入的数据格式不正确)"""
    code = HTTPCode.VALIDATE_ERROR



