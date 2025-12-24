from datetime import datetime
from typing import List

from sqlalchemy import Column, String, Integer, Table, Text, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(32))
    password_hash: Mapped[str] = mapped_column(Text)


class Wallet(Base):
    __tablename__ = 'wallet'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[User] = mapped_column(ForeignKey('user.id'))
    name: Mapped[str] = mapped_column(String(30))
    bank_name: Mapped[str] = mapped_column(String(30), nullable=True)
    full_sum: Mapped[int] = mapped_column(Integer, default=0)


class Payout(Base):
    __tablename__ = 'payout'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(32), default='Payout')
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    sum: Mapped[int] = mapped_column(Integer, default=0)
    wallet_id: Mapped[int] = mapped_column(ForeignKey('wallet.id'))


goal_bite_table = Table(
    "association_table",
    Base.metadata,
    Column("goal_id", ForeignKey("goal.id"), primary_key=True),
    Column("bite_id", ForeignKey("bite.id"), primary_key=True),
)


class Bite(Base):
    __tablename__ = 'bite'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    payout_id: Mapped[int] = mapped_column(ForeignKey('payout.id'))
    sum: Mapped[int] = mapped_column(Integer, default=0)
    
    goals: Mapped[List['Goal']] = relationship(secondary=goal_bite_table, back_populates='bites')
    

class Goal(Base):
    __tablename__ = 'goal'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    sum: Mapped[int] = mapped_column(Integer, default=0)

    bites: Mapped[List[Bite]] = relationship(secondary=goal_bite_table, back_populates='goals')
