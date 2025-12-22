"""
@author: Lzm
@date: 2025年12月04日
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """聊天接口的参数验证"""

    # 必填、长度最大为2000
    # StringField表示字符串类型的参数，validators表示验证器列表，这里使用了DataRequired和Length两个验证器
    query = StringField("query", validators=[DataRequired(message="你的提问，是必填的哦！"),
                                             Length(max=2000, message="你的提问，不能超过2000个字符哦！")])
