import pytest
import datetime as dt
import sys
import os

sys.path.append(os.path.dirname("ccdefundamentals"))
from ccdexplorer_fundamentals.GRPCClient import GRPCClient
from ccdexplorer_fundamentals.GRPCClient.CCD_Types import *
from rich import print


@pytest.fixture
def grpcclient():
    return GRPCClient()


def test_baker_list(grpcclient: GRPCClient):
    block_hash = "ee6f396d82bd3615fb74e53681dbacb1f409fba22eaa12fba60941bc3d387f2b"
    bl = grpcclient.get_baker_list(block_hash)

    assert bl[0] == 0
    assert bl[10] == 452


def test_baker_list_first_payday(grpcclient: GRPCClient):
    block_hash = "ee6f396d82bd3615fb74e53681dbacb1f409fba22eaa12fba60941bc3d387f2b"
    bl = grpcclient.get_baker_list(block_hash)

    assert bl[0] == 0
    assert bl[10] == 452
