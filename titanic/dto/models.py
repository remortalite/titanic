from datetime import datetime

from sqlalchemy import String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(32))
    password_hash: Mapped[str] = mapped_column(Text)


class Wallet(Base):
    __tablename__ = 'wallets'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[User] = mapped_column(ForeignKey('users.id'))
    name: Mapped[str] = mapped_column(String(30))
    bank_name: Mapped[str] = mapped_column(String(30), nullable=True)
    full_sum: Mapped[int] = mapped_column(Integer, default=0)


class Payout(Base):
    __tablename__ = 'payouts'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(32), default='Payout')
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    sum: Mapped[int] = mapped_column(Integer, default=0)
    wallet_id: Mapped[int] = mapped_column(ForeignKey('wallets.id'))


class Goal(Base):
    __tablename__ = 'goals'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    sum: Mapped[int] = mapped_column(Integer, default=0)


class Bite(Base):
    __tablename__ = 'bites'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    payout_id: Mapped[int] = mapped_column(ForeignKey('payouts.id'))
    sum: Mapped[int] = mapped_column(Integer, default=0)
    
    goal_id: Mapped[int] = mapped_column(ForeignKey('goals.id'))
