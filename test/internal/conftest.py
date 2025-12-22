"""
@author: Lzm
@date: 2025年12月19日
"""
import pytest

from app.http.app import app


@pytest.fixture
def client():
    """获取测试客户端"""
    app.config["TESTING"] = True  # 获取Flask这个应用的测试配置
    with app.test_client() as client:   # with 是用来自动管理资源的，保证资源用完后一定会被清理、 as 就是把 with 管理的东西赋值给一个变量
        yield client   # 这里用 yield 是因为我们可能需要在测试后做一些清理工作，比如关闭数据库连接等