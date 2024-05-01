import pytest
import sys
import os


sys.path.append(os.path.dirname("ccdexplorer_fundamentals"))
from ccdexplorer_fundamentals.GRPCClient import GRPCClient
from rich import print
from ccdexplorer_fundamentals.enums import NET
from ccdexplorer_fundamentals.mongodb import MongoDB, Collections
from ccdexplorer_schema_parser.Schema import Schema
from ccdexplorer_fundamentals.cis import (
    CIS,
    registerCredentialEvent,
    revokeCredentialEvent,
    transferEvent,
    tokenMetadataEvent,
    itemCreatedEvent,
    itemStatusChangedEvent,
)
from ccdexplorer_fundamentals.GRPCClient.CCD_Types import CCD_ContractAddress


@pytest.fixture
def grpcclient():
    return GRPCClient()


@pytest.fixture
def mongodb():
    return MongoDB(tooter=None)


def tx_at_index_from(
    tx_index: int,
    block_hash: str,
    grpcclient: GRPCClient,
    net: NET = NET.MAINNET,
    show_all: bool = False,
):
    block = grpcclient.get_block_transaction_events(block_hash, net)
    if show_all:
        return block.transaction_summaries
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


def test_checksum_provenance(grpcclient: GRPCClient):
    block_hash = grpcclient.get_finalized_block_at_height(14189078, NET.MAINNET).hash
    tx = tx_at_index_from(13, block_hash, grpcclient, NET.MAINNET, show_all=False)
    # print(tx)
    ci = CIS(grpcclient, 9403, 0, "", NET.MAINNET)

    event = tx.account_transaction.effects.contract_update_issued.effects[0]
    tag, result = ci.process_log_events(event.updated.events[1])
    result: tokenMetadataEvent
    assert tag == 251
    assert (
        result.token_id
        == "01288764e78695027bd972e9b654cde28df2563e56b3ed66a4c8f4dcb3c08cec"
    )
    assert result.metadata.checksum is None


def test_checksum_aesirx(grpcclient: GRPCClient):
    block_hash = grpcclient.get_finalized_block_at_height(14178624, NET.MAINNET).hash
    tx = tx_at_index_from(0, block_hash, grpcclient, NET.MAINNET, show_all=False)
    # print(tx)
    ci = CIS(grpcclient, 8602, 0, "", NET.MAINNET)

    event = tx.account_transaction.effects.contract_update_issued.effects[0]
    tag, result = ci.process_log_events(event.updated.events[1])
    result: tokenMetadataEvent
    assert tag == 251
    assert (
        result.token_id
        == "01288764e78695027bd972e9b654cde28df2563e56b3ed66a4c8f4dcb3c08cec"
    )
    assert result.metadata.checksum is None


def test_checksum_other(grpcclient: GRPCClient):
    block_hash = grpcclient.get_finalized_block_at_height(11788918, NET.TESTNET).hash
    tx = tx_at_index_from(0, block_hash, grpcclient, NET.TESTNET, show_all=False)
    # print(tx)
    ci = CIS(grpcclient, 8364, 0, "", NET.MAINNET)

    event = tx.account_transaction.effects.contract_update_issued.effects[0]
    tag, result = ci.process_log_events(event.updated.events[1])
    result: tokenMetadataEvent
    assert tag == 251
    assert (
        result.token_id
        == "01288764e78695027bd972e9b654cde28df2563e56b3ed66a4c8f4dcb3c08cec"
    )
    assert result.metadata.checksum is None


def test_checksum_other2(grpcclient: GRPCClient):
    block_hash = grpcclient.get_finalized_block_at_height(11950993, NET.TESTNET).hash
    tx = tx_at_index_from(0, block_hash, grpcclient, NET.TESTNET, show_all=False)
    # print(tx)
    ci = CIS(grpcclient, 8416, 0, "", NET.MAINNET)

    event = tx.account_transaction.effects.contract_update_issued.effects[0]
    tag, result = ci.process_log_events(event.updated.events[1])
    result: tokenMetadataEvent
    assert tag == 251
    assert result.token_id == "25"
    assert result.metadata.checksum is None


def get_schema_from_source(
    contract_address: CCD_ContractAddress,
    mongodb: MongoDB,
    grpcclient: GRPCClient,
    net: NET,
):
    result = mongodb.testnet[Collections.instances].find_one(
        {"_id": contract_address.to_str()}
    )
    module_ref = (
        result["v1"]["source_module"]
        if result.get("v1")
        else result["v0"]["source_module"]
    )
    source_module_name = (
        result["v1"]["name"][5:] if result.get("v1") else result["v0"]["name"][5:]
    )
    ms = grpcclient.get_module_source_original_classes(
        module_ref, "last_final", net=net
    )
    schema = Schema(ms.v1.value, 1) if ms.v1 else Schema(ms.v0.value, 0)

    return schema, source_module_name


def test_cis_6_create_item(
    grpcclient: GRPCClient,
    mongodb: MongoDB,
):
    net = NET.TESTNET
    block_hash = grpcclient.get_finalized_block_at_height(13753259, net).hash
    tx = tx_at_index_from(0, block_hash, grpcclient, net)
    # print(tx)
    contract_address = CCD_ContractAddress(index=8901, subindex=0)
    schema, source_module_name = get_schema_from_source(
        contract_address, mongodb, grpcclient, net
    )
    ci = CIS(grpcclient, contract_address.index, contract_address.subindex, "", net)

    event = tx.account_transaction.effects.contract_update_issued.effects[0]
    tag, result = ci.process_tnt_log_event(event.updated.events[0])

    if tag == 237:
        event_json = schema.event_to_json(
            source_module_name,
            bytes.fromhex(event.updated.events[0]),
        )

        result: itemCreatedEvent
        result.initial_status = list(
            event_json["ItemCreated"][0]["initial_status"].keys()
        )[0]
    print(result)


def test_cis_6_status_changed_item(grpcclient: GRPCClient, mongodb: MongoDB):
    net = NET.TESTNET
    block_hash = grpcclient.get_finalized_block_at_height(13757068, net).hash
    tx = tx_at_index_from(0, block_hash, grpcclient, net)
    # print(tx)
    contract_address = CCD_ContractAddress(index=8901, subindex=0)
    schema, source_module_name = get_schema_from_source(
        contract_address, mongodb, grpcclient, net
    )
    ci = CIS(grpcclient, contract_address.index, contract_address.subindex, "", net)

    event = tx.account_transaction.effects.contract_update_issued.effects[0]
    tag, result = ci.process_tnt_log_event(event.updated.events[0])

    if tag == 236:
        event_json = schema.event_to_json(
            source_module_name,
            bytes.fromhex(event.updated.events[0]),
        )

        result: itemStatusChangedEvent
        result.new_status = list(
            event_json["ItemStatusChanged"][0]["new_status"].keys()
        )[0]
    print(result)
