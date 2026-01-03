"""
@Time    : 2024/4/6 15:08
@Author  : thezehui@gmail.com
@File    : app.py
"""
import uuid
from datetime import datetime

from sqlalchemy import (
    Column,
    UUID,
    String,
    Text,
    DateTime,
    PrimaryKeyConstraint,
    Index,
)

from internal.extension.database_extension import db


class App(db.Model):
    """AI应用基础模型类"""

    # 设置表名
    __tablename__ = "app"
    # 设置表的约束和索引
    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_app_id"), # 给ID字段创建主键约束
        Index("idx_app_account_id", "account_id"), # 给account_id字段创建索引
    )

    id = Column(UUID, default=uuid.uuid4, nullable=False)
    account_id = Column(UUID, nullable=False)
    name = Column(String(255), default="", nullable=False)
    icon = Column(String(255), default="", nullable=False)
    description = Column(Text, default="", nullable=False)
    # status = Column(String(255), default="", nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
