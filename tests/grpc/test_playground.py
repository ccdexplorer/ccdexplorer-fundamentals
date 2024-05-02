import pytest
import datetime as dt
import sys
import os

sys.path.append(os.path.dirname("ccdexplorer_fundamentals"))
from datetime import timezone
from ccdexplorer_fundamentals.GRPCClient import GRPCClient
from rich import print
from ccdexplorer_fundamentals.enums import NET
from ccdexplorer_fundamentals.cis import *


@pytest.fixture
def grpcclient():
    return GRPCClient()


def test_event(grpcclient: GRPCClient):
    account = "4QwfWAxNGVWHMTkDbDTZLy1dv6VkVgpQWEFN3BzgyPFpFbr4Rb"
    block_hash = "f58b0325ac9acb19c217700c08b27d724226b98082157b8ba006b5cedf36cdc1"
    net = NET.TESTNET
    ai = grpcclient.get_account_info(block_hash, account, net=net)
    print(ai)  # .dict(exclude_none=True))
    # assert ai.address == account
    # assert ai.schedule.schedules[0].amount == 16358781149999
    # assert ai.schedule.schedules[0].timestamp == dt.datetime(
    #     2023, 2, 5, 21, 0, tzinfo=dt.timezone.utc
    # )
    # assert (
    #     ai.schedule.schedules[0].transactions[0]
    #     == "f33050060051c6b738549b60e99498fc7f59fb0b6c915ed9e90a11a7584f2d30"
    # )


def test_7073_supports(grpcclient: GRPCClient):
    block_hash = "last_final"
    instance_index = 7073
    instance_subindex = 0
    entrypoint = "BictoryCnsNft.supports"

    ci = CIS(grpcclient, instance_index, instance_subindex, entrypoint, NET.MAINNET)

    supports_cis_1_2 = ci.supports_standards(
        [StandardIdentifiers.CIS_2]  # , StandardIdentifiers.CIS_2]
    )
    print(supports_cis_1_2)
