import pytest
import datetime as dt
import sys
import os

sys.path.append(os.path.dirname("ccdefundamentals"))
from ccdefundamentals.GRPCClient import GRPCClient
from ccdefundamentals.GRPCClient.CCD_Types import *
from rich import print


@pytest.fixture
def grpcclient():
    return GRPCClient()


def test_tokenomics_info_v0(grpcclient: GRPCClient):
    block_hash = "ee6f396d82bd3615fb74e53681dbacb1f409fba22eaa12fba60941bc3d387f2b"
    bi = grpcclient.get_block_info(block_hash)

    assert bi.baker == 8

    grpcclient.switch_to_net(net="testnet")
    block_hash = "cb13794e8180f06faaff4da2eb141c2ccdc33b9c40fbe56916ca1b9370496123"
    bi = grpcclient.get_block_info(block_hash)

    assert bi.height == 2548867

    grpcclient.switch_to_net(net="mainnet")
    block_hash = "ee6f396d82bd3615fb74e53681dbacb1f409fba22eaa12fba60941bc3d387f2b"
    bi = grpcclient.get_block_info(block_hash)

    assert bi.baker == 8
