import pytest
import datetime as dt
from ccdefundamentals.GRPCClient import GRPCClient
from ccdefundamentals.enums import NET
from rich import print


@pytest.fixture
def grpcclient():
    return GRPCClient()


@pytest.mark.skip(reason="Finalized blocks is a stream that never ends...")
def test_finalized_block_info(grpcclient: GRPCClient):
    # while True:
    #     bi = grpcclient.get_finalized_blocks()
    #     print (bi)

    grpcclient.get_finalized_blocks()


def test_get_finalized_block_at_height(grpcclient: GRPCClient):
    block = grpcclient.get_finalized_block_at_height(1_000_000_000)
    assert block is None


def test_get_finalized_block_at_height_testnet(grpcclient: GRPCClient):
    block = grpcclient.get_finalized_block_at_height(2708607, NET("testnet"))
    assert block is not None
