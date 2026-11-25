from datetime import datetime

from sqlalchemy import (
    BigInteger, CheckConstraint, DateTime, ForeignKey, Index, Text,
    UniqueConstraint, func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    customer_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("customers.id"), nullable=False
    )
    order_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("orders.id"))
    channel: Mapped[str] = mapped_column(Text, nullable=False)
    external_message_id: Mapped[str] = mapped_column(Text, nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    intent: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(Text, nullable=False, server_default="RECEIVED")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    __table_args__ = (
        UniqueConstraint("channel", "external_message_id", name="uq_tickets_channel_message"),
        CheckConstraint("channel IN ('telegram','email')", name="ck_tickets_channel"),
        CheckConstraint(
            "status IN ('RECEIVED','CLASSIFIED','AWAITING_APPROVAL','REPLIED','FAILED')",
            name="ck_tickets_status",
        ),
        Index("ix_tickets_customer_id", "customer_id"),
        Index("ix_tickets_status", "status"),
    )