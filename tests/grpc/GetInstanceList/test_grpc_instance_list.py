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


def test_instance_list(grpcclient: GRPCClient):
    block_hash = "ee6f396d82bd3615fb74e53681dbacb1f409fba22eaa12fba60941bc3d387f2b"
    # block_hash = "last_final"
    il = grpcclient.get_instance_list(block_hash)
    # print(il)
    assert il[0].index == 0
    assert il[-1].index == 8584
