import pytest
from titanic import exceptions
from titanic.models import Wallet
from titanic.services.wallet import get_wallet, create_wallet, update_wallet, delete_wallet


def test_get_wallet():
    wallet: Wallet = get_wallet(id=0)
    
    assert wallet is not None


def test_create_wallet():
    data = {
        'user': 'rem',
        'name': 'wallet_1',
        'bank': 'sber',
    }
    
    wallet: Wallet = create_wallet(
        user=data['user'],
        name=data['name'],
        bank=data['bank'],
    )

    wallet_created = get_wallet(id=wallet.id)

    assert wallet_created.user == wallet.user
    assert wallet_created.name == wallet.name
    assert wallet_created.bank == wallet.bank


@pytest.fixture
def wallet_obj():
    data = {
        'user': 'rem',
        'name': 'wallet_1',
        'bank': 'sber',
    }
    
    wallet: Wallet = create_wallet(
        user=data['user'],
        name=data['name'],
        bank=data['bank'],
    )
    
    return wallet


def test_update_wallet(wallet_obj):
    new_data = {
        'name': 'Wallet With Changed Name',
        'bank': 'Tbank',
    }
    
    update_wallet(wallet_obj, name=new_data['name'])

    wallet_new = get_wallet(wallet_obj.id)
    assert wallet_new.name == new_data['name']
    assert not wallet_new.bank == new_data['bank']
    
    update_wallet(wallet_new, bank=new_data['bank'])
    
    wallet_new_new = get_wallet(wallet_obj.id)
    assert wallet_new.name == new_data['name']
    assert wallet_new_new.bank == new_data['bank']
    

def test_delete_wallet(wallet_obj):
    wallet_id = wallet_obj.id
    delete_wallet(wallet_obj)
    
    with pytest.raises(exceptions.WalletNotExists):
        assert get_wallet(id=wallet_id)
