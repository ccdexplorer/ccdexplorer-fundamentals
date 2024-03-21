# ruff:noqa: F403, F405
import sys
import os
from pydantic import BaseModel

import jsonschema_markdown


sys.path.append(os.path.dirname("ccdefundamentals"))
from ccdexplorer_fundamentals.GRPCClient.CCD_Types import *
from ccdexplorer_fundamentals.cis import *
from ccdexplorer_fundamentals.mongodb import *


class GRPCTypes(BaseModel):
    """
    This Model is constructed only to generate documentation.
    """

    CCD_AccountInfo: CCD_AccountInfo
    CCD_BakerStakePendingChange: CCD_BakerStakePendingChange
    CCD_Block: CCD_Block
    CCD_BlockComplete: CCD_BlockComplete
    CCD_BlocksAtHeightResponse: CCD_BlocksAtHeightResponse
    CCD_BlockSpecialEvent: CCD_BlockSpecialEvent
    CCD_ChainParameters: CCD_ChainParameters
    CCD_ConsensusInfo: CCD_ConsensusInfo
    CCD_CurrentPaydayStatus: CCD_CurrentPaydayStatus
    CCD_DelegatorInfo: CCD_DelegatorInfo
    CCD_DelegatorRewardPeriodInfo: CCD_DelegatorRewardPeriodInfo
    CCD_ElectionInfo: CCD_ElectionInfo
    CCD_FinalizedBlockInfo: CCD_FinalizedBlockInfo
    CCD_InvokeInstanceResponse: CCD_InvokeInstanceResponse
    CCD_InstanceInfo: CCD_InstanceInfo
    CCD_PassiveDelegationInfo: CCD_PassiveDelegationInfo
    CCD_PendingUpdate: CCD_PendingUpdate
    CCD_PoolInfo: CCD_PoolInfo
    CCD_TokenomicsInfo: CCD_TokenomicsInfo
    CCD_VersionedModuleSource: CCD_VersionedModuleSource


class MongoTypes(BaseModel):
    """
    This Model is constructed only to generate documentation.
    """

    Collections: Collections
    CollectionsUtilities: CollectionsUtilities
    MongoImpactedAddress: MongoImpactedAddress
    MongoLabeledAccount: MongoLabeledAccount
    MongoTypeAccountReward: MongoTypeAccountReward
    MongoTypeBlockPerDay: MongoTypeBlockPerDay
    MongoTypeInvolvedAccount: MongoTypeInvolvedAccount
    MongoTypeInvolvedContract: MongoTypeInvolvedContract
    MongoTypeInstance: MongoTypeInstance
    MongoTypeLoggedEvent: MongoTypeLoggedEvent
    MongoTypeModule: MongoTypeModule
    MongoTypeReward: MongoTypeReward
    MongoTypePayday: MongoTypePayday
    MongoTypePaydayAPYIntermediate: MongoTypePaydayAPYIntermediate
    MongoTypePaydaysPerformance: MongoTypePaydaysPerformance
    MongoTypePoolReward: MongoTypePoolReward
    MongoTypeTokenAddress: MongoTypeTokenAddress
    MongoTypeTokenHolderAddress: MongoTypeTokenHolderAddress
    MongoTypeTokenLink: MongoTypeTokenLink
    MongoTypeTokensTag: MongoTypeTokensTag


class CISTypes(BaseModel):
    """
    This Model is constructed only to generate documentation.
    """

    TokenMetaData: TokenMetaData

    StandardIdentifiers: StandardIdentifiers
    LoggedEvents: LoggedEvents
    transferEvent: transferEvent
    mintEvent: mintEvent
    burnEvent: burnEvent
    updateOperatorEvent: updateOperatorEvent
    registerCredentialEvent: registerCredentialEvent
    revokeCredentialEvent: revokeCredentialEvent
    issuerMetadataEvent: issuerMetadataEvent
    credentialMetadataEvent: credentialMetadataEvent
    credentialSchemaRefEvent: credentialSchemaRefEvent
    revocationKeyEvent: revocationKeyEvent
    tokenMetadataEvent: tokenMetadataEvent
    nonceEvent: nonceEvent


grpc_model_schema = GRPCTypes.model_json_schema()  # (1)!
markdown = jsonschema_markdown.generate(grpc_model_schema)

with open("docs/grpc_types_docs.md", "w") as f:
    f.write(markdown)

mongo_model_schema = MongoTypes.model_json_schema()  # (1)!
markdown = jsonschema_markdown.generate(mongo_model_schema)

with open("docs/mongo_types_docs.md", "w") as f:
    f.write(markdown)

cis_model_schema = CISTypes.model_json_schema()  # (1)!
markdown = jsonschema_markdown.generate(cis_model_schema)

with open("docs/cis_types_docs.md", "w") as f:
    f.write(markdown)
