from sqlalchemy.orm import Session

from titanic import exceptions
from titanic.dto import engine
from titanic.dto.models import Wallet
from titanic.models import Wallet as WalletModel


def get_wallet(id: int) -> WalletModel:
    with Session(engine) as session:
        wallet_obj = session.get(Wallet, id)
    
    if wallet_obj is None:
        raise exceptions.WalletNotExists(f'Wallet with id={id} does not exist')

    wallet_model: WalletModel = WalletModel(
        id=wallet_obj.id,
        user_id=wallet_obj.user_id,
        name=wallet_obj.name,
        bank=wallet_obj.bank_name,
        full_sum=wallet_obj.full_sum,
    )
    return wallet_model


def create_wallet(user_id: int, name: str, bank: str, full_sum: int = 0) ->  WalletModel:
    with Session(engine) as session:
        wallet_obj = Wallet(user_id=user_id, name=name, bank_name=bank, full_sum=full_sum)
        session.add(wallet_obj)
        session.flush()
        wallet_id = wallet_obj.id
        session.commit()
        
    wallet_model = WalletModel(
        id=wallet_id,
        user_id=user_id,
        name=name,
        bank=bank,
        full_sum=full_sum,
    )
    return wallet_model


def delete_wallet(id: int):
    with Session(engine) as session:
        wallet_obj = session.get(Wallet, id)
        if not wallet_obj:
            raise exceptions.WalletNotExists(f'Wallet with id={id} does not exist')
        session.delete(wallet_obj)
        session.commit()
