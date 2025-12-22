"""
@author: Lzm
@date: 2025年12月18日
"""
from pkg.response import HTTPCode


class TestAppHandler:
    """app控制器的测试类"""

    # 给/app/completion这个接口发送POST请求，测试与ChatGPT对话的功能
    def test_completion(self, client):
        resp = client.post("/app/completion", json={"query": "你好，你是什么模型？"})
        assert resp.status_code == 200
        assert resp.json.get("code") == HTTPCode.SUCCESS
        print("响应内容：", resp.json)

