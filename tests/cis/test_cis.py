import pytest
from ccdefundamentals.GRPCClient import GRPCClient
from rich import print
from ccdefundamentals.enums import NET
from ccdefundamentals.cis import (
    CIS,
    registerCredentialEvent,
    revokeCredentialEvent,
    transferEvent,
)


@pytest.fixture
def grpcclient():
    return GRPCClient()


def tx_at_index_from(
    tx_index: int, block_hash: str, grpcclient: GRPCClient, net: NET = NET.MAINNET
):
    block = grpcclient.get_block_transaction_events(block_hash, net)
    if tx_index == -1:
        return None
    else:
        return block.transaction_summaries[tx_index]


def test_CIS4_register(grpcclient: GRPCClient):
    block_hash = grpcclient.get_finalized_block_at_height(6983797, NET.MAINNET).hash
    tx = tx_at_index_from(11, block_hash, grpcclient, NET.MAINNET)
    # print(tx)
    ci = CIS(grpcclient, 0, 0, "", NET.MAINNET)

    for event in tx.account_transaction.effects.contract_update_issued.effects:
        tag, result = ci.process_log_events(event.updated.events[0])
        result: registerCredentialEvent
        assert tag == 249
        assert (
            result.credential_id
            == "53686beb67985cf532ab4ee7648c764585062417349b55877ebcbdaefae749dc"
        )
        assert (
            result.schema_ref.url
            == "https://telegram-web3id.mainnet.concordium.software/json-schemas/JsonSchema2023-telegram.json"
        )


def test_CIS4_revoke(grpcclient: GRPCClient):
    block_hash = grpcclient.get_finalized_block_at_height(7218597, NET.MAINNET).hash
    tx = tx_at_index_from(0, block_hash, grpcclient, NET.MAINNET)
    ci = CIS(grpcclient, 0, 0, "", NET.MAINNET)

    for event in tx.account_transaction.effects.contract_update_issued.effects:
        tag, result = ci.process_log_events(event.updated.events[0])
        result: revokeCredentialEvent
        assert tag == 248
        assert (
            result.credential_id
            == "534b3e99f0c546db4910bc4cf69f9844b9f9fffde160e74322ebd8496d25c54f"
        )
        assert result.revoker == "Holder"


def test_token_amount(grpcclient: GRPCClient):
    block_hash = grpcclient.get_finalized_block_at_height(13168540, NET.MAINNET).hash
    tx = tx_at_index_from(7, block_hash, grpcclient, NET.MAINNET)
    # print(tx)
    ci = CIS(grpcclient, 0, 0, "", NET.MAINNET)

    event = tx.account_transaction.effects.contract_update_issued.effects[0]
    tag, result = ci.process_log_events(event.interrupted.events[0])
    result: transferEvent
    assert tag == 255
    assert result.token_id == ""
    assert result.token_amount == 20162999394000755
    assert result.from_address == "4JafBcWeHt5K92EXyStUdzii5Jt32BSDiZ2EMAYcnYBtrAAePA"
    assert result.to_address == "<9363,0>"
