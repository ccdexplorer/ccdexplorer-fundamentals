# ruff: noqa: F403, F405, E402
from __future__ import annotations
from ccdefundamentals.GRPCClient.types_pb2 import *
from ccdefundamentals.enums import NET
from ccdefundamentals.GRPCClient.queries._SharedConverters import (
    Mixin as _SharedConverters,
)
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from ccdefundamentals.GRPCClient import GRPCClient
from ccdefundamentals.GRPCClient.CCD_Types import *


class Mixin(_SharedConverters):
    def get_consensus_info(
        self: GRPCClient,
        net: Enum = NET.MAINNET,
    ) -> CCD_ConsensusInfo:
        grpc_return_value: ConsensusInfo = self.stub_on_net(
            net, "GetConsensusInfo", Empty()
        )

        result = {}

        for descriptor in grpc_return_value.DESCRIPTOR.fields:
            key, value = self.get_key_value_from_descriptor(
                descriptor, grpc_return_value
            )

            if key == "protocol_version":
                result[key] = ProtocolVersions(value).name

            elif type(value) in self.simple_types:
                result[key] = self.convertType(value)

        return CCD_ConsensusInfo(**result)
