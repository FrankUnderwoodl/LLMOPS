"""
@author: Lzm
@date: 2025年12月01日
"""

from internal.exception.exception import ValidateErrorException, CustomException, FailException, NotFoundException, \
    UnauthorizedException, ForbiddenException

# 导出所有的异常类
__all__ = [
    "CustomException",
    "FailException",
    "NotFoundException",
    "UnauthorizedException",
    "ForbiddenException",
    "ValidateErrorException",
]


