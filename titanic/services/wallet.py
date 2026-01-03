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
