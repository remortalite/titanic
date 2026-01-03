import pytest
from titanic import exceptions
from titanic.models import Wallet
from titanic.services import wallet as wallet_service


def test_create_wallet():
    data = {
        'user_id': 123,
        'name': 'wallet_1',
        'bank': 'sber',
    }
    
    wallet: Wallet = wallet_service.create_wallet(
        user_id=data['user_id'],
        name=data['name'],
        bank=data['bank'],
    )

    wallet_created = wallet_service.get_wallet(id=wallet.id)

    assert wallet_created.user_id == wallet.user_id
    assert wallet_created.name == wallet.name
    assert wallet_created.bank == wallet.bank
    
    wallet_service.delete_wallet(id=wallet.id)


@pytest.fixture
def wallet_obj():
    data = {
        'user_id': 123,
        'name': 'wallet_1',
        'bank': 'sber',
    }
    
    wallet: Wallet = wallet_service.create_wallet(
        user_id=data['user_id'],
        name=data['name'],
        bank=data['bank'],
    )
    
    yield wallet
    
    try:
        wallet_service.delete_wallet(id=wallet.id)
    except Exception:
        pass


def test_get_wallet(wallet_obj):
    wallet: Wallet = wallet_service.get_wallet(id=wallet_obj.id)
    
    assert wallet is not None


def test_update_wallet(wallet_obj):
    new_data = {
        'name': 'Wallet With Changed Name',
        'bank': 'Tbank',
    }
    
    wallet_service.update_wallet(wallet_obj, name=new_data['name'])

    wallet_new = wallet_service.get_wallet(wallet_obj.id)
    assert wallet_new.name == new_data['name']
    assert not wallet_new.bank == new_data['bank']
    
    wallet_service.update_wallet(wallet_new, bank=new_data['bank'])
    
    wallet_new_new = wallet_service.get_wallet(wallet_obj.id)
    assert wallet_new.name == new_data['name']
    assert wallet_new_new.bank == new_data['bank']
    

def test_delete_wallet(wallet_obj):
    wallet_id = wallet_obj.id
    wallet_service.delete_wallet(id=wallet_id)
    
    with pytest.raises(exceptions.WalletNotExists):
        wallet_service.get_wallet(id=wallet_id)
