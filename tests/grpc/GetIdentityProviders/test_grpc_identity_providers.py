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


def test_identity_providers(grpcclient: GRPCClient):
    block_hash = "ee6f396d82bd3615fb74e53681dbacb1f409fba22eaa12fba60941bc3d387f2b"
    ip = grpcclient.get_identity_providers(block_hash)

    assert ip[0].description.name == "Identity Provider 0"
    assert (
        ip[1].cdi_verify_key
        == "e0f2040fc103db1fb5429780b1c9d654ac6818c1d8ba847106dcae53e749fd40"
    )
    assert ip[2].identity == 2
