from datetime import datetime

from sqlalchemy import (
    BigInteger, CheckConstraint, DateTime, ForeignKey, Index, Text, func, text,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Refund(Base):
    __tablename__ = "refunds"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    order_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("orders.id"), nullable=False)
    ticket_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("tickets.id"), nullable=False)
    amount_paise: Mapped[int] = mapped_column(BigInteger, nullable=False)
    status: Mapped[str] = mapped_column(Text, nullable=False, server_default="REQUESTED")
    reason: Mapped[str | None] = mapped_column(Text)
    decided_by: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    __table_args__ = (
        CheckConstraint("amount_paise > 0", name="ck_refunds_amount_positive"),
        CheckConstraint(
            "status IN ('REQUESTED','AUTO_APPROVED','PENDING_APPROVAL','APPROVED',"
            "'REJECTED','PROCESSED','FAILED')",
            name="ck_refunds_status",
        ),
        # At most one ACTIVE refund per order. Rejected/failed ones don't block a retry.
        Index(
            "uq_refunds_one_active_per_order",
            "order_id",
            unique=True,
            postgresql_where=text("status NOT IN ('REJECTED','FAILED')"),
        ),
    )