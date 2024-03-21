import pytest
import datetime as dt
import sys
import os

sys.path.append(os.path.dirname("ccdefundamentals"))
from ccdexplorer_fundamentals.GRPCClient import GRPCClient
from rich import print
from rich.progress import track


@pytest.fixture
def grpcclient():
    return GRPCClient()


@pytest.mark.skip(reason="Account list integration, slow (7 min).")
def test_tx_account_info_integration(grpcclient: GRPCClient):
    block_hash = "ee6f396d82bd3615fb74e53681dbacb1f409fba22eaa12fba60941bc3d387f2b"
    al = grpcclient.get_account_list(block_hash)

    accounts = []
    for account in track(al):
        ai = grpcclient.get_account_info(account, block_hash)
        accounts.append(ai)

    pass
    print(accounts[1000])
    pass


def test_tx_account_info_initica(grpcclient: GRPCClient):
    block_hash = "ee6f396d82bd3615fb74e53681dbacb1f409fba22eaa12fba60941bc3d387f2b"
    al = grpcclient.get_account_list(block_hash)

    accounts = []
    for account in track(al):
        ai = grpcclient.get_account_info(block_hash, account)
        accounts.append(ai)

    pass
    print(accounts[1000])
    pass
