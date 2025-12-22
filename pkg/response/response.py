"""
@author: Lzm
@date: 2025年12月17日
"""
from dataclasses import field, dataclass
from typing import Any

from flask import jsonify

from .http_code import HTTPCode


@dataclass  # 自动生成初始化方法等
class Response:
    """默认的接口响应格式"""
    code: HTTPCode = HTTPCode.SUCCESS  # 响应状态码，默认成功
    message: str = "请求成功"  # 响应消息，默认请求成功
    data: Any = field(default_factory=dict)  # 这里千万别用 data: Any = {}，因为默认值是可变对象，会导致所有实例共享同一个对象

    # def __init__(self, code: HTTPCode = HTTPCode.SUCCESS, message: str = "请求成功", data: Any = None):
    #     self.code = code
    #     self.message = message
    #     if data is None:
    #         self.data = {}
    #     else:
    #         self.data = data


# 返回数据的基础响应接口们
def json(data: Response = None):
    """基础的响应接口"""
    return jsonify(data), 200

# 成功响应接口
def success_json(data: Any = None):
    return json(Response(code=HTTPCode.SUCCESS, message="", data=data))

# 失败响应接口
def fail_json(data: Any = None):
    return json(Response(code=HTTPCode.FAIL, message="", data=data))

# 前端传入参数校验失败的响应接口
def validate_error_json(errors: dict = None):
    """数据验证错误响应"""
    first_key = next(iter(errors))
    if first_key is not None:
        msg = errors.get(first_key)[0]
    else:
        msg = ""
    return json(Response(code=HTTPCode.VALIDATE_ERROR, message=msg, data=errors))




# 只有消息，不返回数据的响应接口们
def message(code: HTTPCode = None, msg: str = ""):
    """基础的消息响应，固定返回消息提示，数据固定为空字典"""
    return json(Response(code=code, message=msg, data={}))


def success_message(msg: str = ""):
    """成功的消息响应"""
    return message(code=HTTPCode.SUCCESS, msg=msg)


def fail_message(msg: str = ""):
    """失败的消息响应"""
    return message(code=HTTPCode.FAIL, msg=msg)


def not_found_message(msg: str = ""):
    """未找到消息响应"""
    return message(code=HTTPCode.NOT_FOUND, msg=msg)


def unauthorized_message(msg: str = ""):
    """未授权消息响应"""
    return message(code=HTTPCode.UNAUTHORIZED, msg=msg)


def forbidden_message(msg: str = ""):
    """无权限消息响应"""
    return message(code=HTTPCode.FORBIDDEN, msg=msg)
