# GRPCTypes

This Model is constructed only to generate documentation.

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| CCD_AccountInfo | `object` | ✅ | [CCD_AccountInfo](#ccd_accountinfo)|  |  |  | |
| CCD_BakerStakePendingChange | `object` | ✅ | [CCD_BakerStakePendingChange](#ccd_bakerstakependingchange)|  |  |  | |
| CCD_Block | `object` | ✅ | [CCD_Block](#ccd_block)|  |  |  | |
| CCD_BlockComplete | `object` | ✅ | [CCD_BlockComplete](#ccd_blockcomplete)|  |  |  | |
| CCD_BlocksAtHeightResponse | `object` | ✅ | [CCD_BlocksAtHeightResponse](#ccd_blocksatheightresponse)|  |  |  | |
| CCD_BlockSpecialEvent | `object` | ✅ | [CCD_BlockSpecialEvent](#ccd_blockspecialevent)|  |  |  | |
| CCD_ChainParameters | `object` | ✅ | [CCD_ChainParameters](#ccd_chainparameters)|  |  |  | |
| CCD_ConsensusInfo | `object` | ✅ | [CCD_ConsensusInfo](#ccd_consensusinfo)|  |  |  | |
| CCD_CurrentPaydayStatus | `object` | ✅ | [CCD_CurrentPaydayStatus](#ccd_currentpaydaystatus)|  |  |  | |
| CCD_DelegatorInfo | `object` | ✅ | [CCD_DelegatorInfo](#ccd_delegatorinfo)|  |  |  | |
| CCD_DelegatorRewardPeriodInfo | `object` | ✅ | [CCD_DelegatorRewardPeriodInfo](#ccd_delegatorrewardperiodinfo)|  |  |  | |
| CCD_ElectionInfo | `object` | ✅ | [CCD_ElectionInfo](#ccd_electioninfo)|  |  |  | |
| CCD_FinalizedBlockInfo | `object` | ✅ | [CCD_FinalizedBlockInfo](#ccd_finalizedblockinfo)|  |  |  | |
| CCD_InvokeInstanceResponse | `object` | ✅ | [CCD_InvokeInstanceResponse](#ccd_invokeinstanceresponse)|  |  |  | |
| CCD_InstanceInfo | `object` | ✅ | [CCD_InstanceInfo](#ccd_instanceinfo)|  |  |  | |
| CCD_PassiveDelegationInfo | `object` | ✅ | [CCD_PassiveDelegationInfo](#ccd_passivedelegationinfo)|  |  |  | |
| CCD_PendingUpdate | `object` | ✅ | [CCD_PendingUpdate](#ccd_pendingupdate)|  |  |  | |
| CCD_PoolInfo | `object` | ✅ | [CCD_PoolInfo](#ccd_poolinfo)|  |  |  | |
| CCD_TokenomicsInfo | `object` | ✅ | [CCD_TokenomicsInfo](#ccd_tokenomicsinfo)|  |  |  | |
| CCD_VersionedModuleSource | `object` | ✅ | [CCD_VersionedModuleSource](#ccd_versionedmodulesource)|  |  |  | |


---

# Definitions



## CCD_AccessStructure

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| access_public_keys | `array` | ✅ | integer|  |  |  | |
| access_threshold | `integer` | ✅ | integer|  |  |  | |


## CCD_AccountCreationDetails

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| credential_type | `integer` | ✅ | integer|  |  |  | |
| address | `string` | ✅ | string|  |  |  | |
| reg_id | `string` | ✅ | string|  |  |  | |


## CCD_AccountCredential

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| initial | `object` |  | [CCD_InitialCredentialValues](#ccd_initialcredentialvalues)|  |  |  | |
| normal | `object` |  | [CCD_NormalCredentialValues](#ccd_normalcredentialvalues)|  |  |  | |


## CCD_AccountInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| address | `string` | ✅ | string|  |  |  | |
| amount | `integer` | ✅ | integer|  |  |  | |
| credentials | `object` | ✅ | [CCD_AccountCredential](#ccd_accountcredential)|  |  |  | |
| encrypted_balance | `object` | ✅ | [CCD_EncryptedBalance](#ccd_encryptedbalance)|  |  |  | |
| encryption_key | `string` | ✅ | string|  |  |  | |
| index | `integer` | ✅ | integer|  |  |  | |
| threshold | `integer` | ✅ | integer|  |  |  | |
| sequence_number | `integer` | ✅ | integer|  |  |  | |
| stake | `object` |  | [CCD_AccountStakingInfo](#ccd_accountstakinginfo)|  |  |  | |
| schedule | `object` |  | [CCD_ReleaseSchedule](#ccd_releaseschedule)|  |  |  | |


## CCD_AccountStakingInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker | `object` |  | [CCD_AccountStakingInfo_Baker](#ccd_accountstakinginfo_baker)|  |  |  | |
| delegator | `object` |  | [CCD_AccountStakingInfo_Delegator](#ccd_accountstakinginfo_delegator)|  |  |  | |


## CCD_AccountStakingInfo_Baker

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_info | `object` | ✅ | [CCD_BakerInfo](#ccd_bakerinfo)|  |  |  | |
| pool_info | `object` | ✅ | [CCD_BakerPoolInfo](#ccd_bakerpoolinfo)|  |  |  | |
| pending_change | `object` | ✅ | [CCD_StakePendingChange](#ccd_stakependingchange)|  |  |  | |
| restake_earnings | `boolean` | ✅ | boolean|  |  |  | |
| staked_amount | `integer` | ✅ | integer|  |  |  | |


## CCD_AccountStakingInfo_Delegator

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| target | `object` | ✅ | [CCD_DelegationTarget](#ccd_delegationtarget)|  |  |  | |
| pending_change | `object` | ✅ | [CCD_StakePendingChange](#ccd_stakependingchange)|  |  |  | |
| restake_earnings | `boolean` | ✅ | boolean|  |  |  | |
| staked_amount | `integer` | ✅ | integer|  |  |  | |


## CCD_AccountTransactionDetails

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| cost | `integer` | ✅ | integer|  |  |  | |
| sender | `string` | ✅ | string|  |  |  | |
| outcome | `string` | ✅ | string|  |  |  | |
| effects | `object` | ✅ | [CCD_AccountTransactionEffects](#ccd_accounttransactioneffects)|  |  |  | |


## CCD_AccountTransactionEffects

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| none | `object` |  | [CCD_AccountTransactionEffects_None](#ccd_accounttransactioneffects_none)|  |  |  | |
| module_deployed | `string` |  | string|  |  |  | |
| contract_initialized | `object` |  | [CCD_ContractInitializedEvent](#ccd_contractinitializedevent)|  |  |  | |
| contract_update_issued | `object` |  | [CCD_ContractUpdateIssued](#ccd_contractupdateissued)|  |  |  | |
| account_transfer | `object` |  | [CCD_AccountTransfer](#ccd_accounttransfer)|  |  |  | |
| baker_added | `object` |  | [CCD_BakerAdded](#ccd_bakeradded)|  |  |  | |
| baker_removed | `integer` |  | integer|  |  |  | |
| baker_stake_updated | `object` |  | [CCD_BakerStakeUpdated](#ccd_bakerstakeupdated)|  |  |  | |
| baker_restake_earnings_updated | `object` |  | [CCD_BakerEvent_BakerRestakeEarningsUpdated](#ccd_bakerevent_bakerrestakeearningsupdated)|  |  |  | |
| baker_keys_updated | `object` |  | [CCD_BakerKeysEvent](#ccd_bakerkeysevent)|  |  |  | |
| encrypted_amount_transferred | `object` |  | [CCD_AccountTransactionEffects_EncryptedAmountTransferred](#ccd_accounttransactioneffects_encryptedamounttransferred)|  |  |  | |
| transferred_to_encrypted | `object` |  | [CCD_EncryptedSelfAmountAddedEvent](#ccd_encryptedselfamountaddedevent)|  |  |  | |
| transferred_to_public | `object` |  | [CCD_AccountTransactionEffects_TransferredToPublic](#ccd_accounttransactioneffects_transferredtopublic)|  |  |  | |
| transferred_with_schedule | `object` |  | [CCD_TransferredWithSchedule](#ccd_transferredwithschedule)|  |  |  | |
| credential_keys_updated | `string` |  | string|  |  |  | |
| credentials_updated | `object` |  | [CCD_AccountTransactionEffects_CredentialsUpdated](#ccd_accounttransactioneffects_credentialsupdated)|  |  |  | |
| data_registered | `string` |  | string|  |  |  | |
| baker_configured | `object` |  | [CCD_BakerConfigured](#ccd_bakerconfigured)|  |  |  | |
| delegation_configured | `object` |  | [CCD_DelegationConfigured](#ccd_delegationconfigured)|  |  |  | |


## CCD_AccountTransactionEffects_CredentialsUpdated

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| new_cred_ids | `array` | ✅ | string|  |  |  | |
| removed_cred_ids | `array` | ✅ | string|  |  |  | |
| new_threshold | `integer` | ✅ | integer|  |  |  | |


## CCD_AccountTransactionEffects_EncryptedAmountTransferred

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| removed | `object` |  | [CCD_EncryptedAmountRemovedEvent](#ccd_encryptedamountremovedevent)|  |  |  | |
| added | `object` |  | [CCD_NewEncryptedAmountEvent](#ccd_newencryptedamountevent)|  |  |  | |
| memo | `string` |  | string|  |  |  | |


## CCD_AccountTransactionEffects_None

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| reject_reason | `object` | ✅ | [CCD_RejectReason](#ccd_rejectreason)|  |  |  | |
| transaction_type | `integer` |  | integer|  |  |  | |


## CCD_AccountTransactionEffects_TransferredToPublic

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| removed | `object` | ✅ | [CCD_EncryptedAmountRemovedEvent](#ccd_encryptedamountremovedevent)|  |  |  | |
| amount | `integer` | ✅ | integer|  |  |  | |


## CCD_AccountTransfer

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| receiver | `string` | ✅ | string|  |  |  | |
| amount | `integer` |  | integer|  |  |  | |
| memo | `string` |  | string|  |  |  | |


## CCD_AccountVerifyKey

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| ed25519_key | `string` | ✅ | string|  |  |  | |


## CCD_Address

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| account | `string` |  | string|  |  |  | |
| contract | `object` |  | [CCD_ContractAddress](#ccd_contractaddress)|  |  |  | |


## CCD_ArInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| identity | `integer` | ✅ | integer|  |  |  | |
| description | `object` | ✅ | [CCD_Description](#ccd_description)|  |  |  | |
| public_key | `string` | ✅ | string|  |  |  | |


## CCD_AuthorizationsV0

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| keys | `array` | ✅ | string|  |  |  | |
| emergency | `object` | ✅ | [CCD_AccessStructure](#ccd_accessstructure)|  |  |  | |
| protocol | `object` | ✅ | [CCD_AccessStructure](#ccd_accessstructure)|  |  |  | |
| parameter_euro_per_energy | `object` | ✅ | [CCD_AccessStructure](#ccd_accessstructure)|  |  |  | |
| parameter_micro_CCD_per_euro | `object` | ✅ | [CCD_AccessStructure](#ccd_accessstructure)|  |  |  | |
| parameter_foundation_account | `object` | ✅ | [CCD_AccessStructure](#ccd_accessstructure)|  |  |  | |
| parameter_mint_distribution | `object` | ✅ | [CCD_AccessStructure](#ccd_accessstructure)|  |  |  | |
| parameter_transaction_fee_distribution | `object` | ✅ | [CCD_AccessStructure](#ccd_accessstructure)|  |  |  | |
| parameter_gas_rewards | `object` | ✅ | [CCD_AccessStructure](#ccd_accessstructure)|  |  |  | |
| pool_parameters | `object` | ✅ | [CCD_AccessStructure](#ccd_accessstructure)|  |  |  | |
| add_anonymity_revoker | `object` | ✅ | [CCD_AccessStructure](#ccd_accessstructure)|  |  |  | |
| add_identity_provider | `object` | ✅ | [CCD_AccessStructure](#ccd_accessstructure)|  |  |  | |
| parameter_election_difficulty | `object` |  | [CCD_AccessStructure](#ccd_accessstructure)|  |  |  | |


## CCD_AuthorizationsV1

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| v0 | `object` | ✅ | [CCD_AuthorizationsV0](#ccd_authorizationsv0)|  |  |  | |
| parameter_cooldown | `object` | ✅ | [CCD_AccessStructure](#ccd_accessstructure)|  |  |  | |
| parameter_time | `object` | ✅ | [CCD_AccessStructure](#ccd_accessstructure)|  |  |  | |


## CCD_BakerAdded

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| keys_event | `object` | ✅ | [CCD_BakerKeysEvent](#ccd_bakerkeysevent)|  |  |  | |
| stake | `integer` | ✅ | integer|  |  |  | |
| restake_earnings | `boolean` | ✅ | boolean|  |  |  | |


## CCD_BakerConfigured

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| events | `array` | ✅ | [CCD_BakerEvent](#ccd_bakerevent)|  |  |  | |


## CCD_BakerEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_added | `object` |  | [CCD_BakerAdded](#ccd_bakeradded)|  |  |  | |
| baker_removed | `integer` |  | integer|  |  |  | |
| baker_stake_increased | `object` |  | [CCD_BakerStakeIncreased](#ccd_bakerstakeincreased)|  |  |  | |
| baker_stake_decreased | `object` |  | [CCD_BakerStakeDecreased](#ccd_bakerstakedecreased)|  |  |  | |
| baker_restake_earnings_updated | `object` |  | [CCD_BakerRestakeEarningsUpdated](#ccd_bakerrestakeearningsupdated)|  |  |  | |
| baker_keys_updated | `object` |  | [CCD_BakerKeysEvent](#ccd_bakerkeysevent)|  |  |  | |
| baker_set_open_status | `object` |  | [CCD_BakerSetOpenStatus](#ccd_bakersetopenstatus)|  |  |  | |
| baker_set_metadata_url | `object` |  | [CCD_BakerSetMetadataUrl](#ccd_bakersetmetadataurl)|  |  |  | |
| baker_set_transaction_fee_commission | `object` |  | [CCD_BakerSetTransactionFeeCommission](#ccd_bakersettransactionfeecommission)|  |  |  | |
| baker_set_baking_reward_commission | `object` |  | [CCD_BakerSetBakingRewardCommission](#ccd_bakersetbakingrewardcommission)|  |  |  | |
| baker_set_finalization_reward_commission | `object` |  | [CCD_BakerSetFinalizationRewardCommission](#ccd_bakersetfinalizationrewardcommission)|  |  |  | |


## CCD_BakerEvent_BakerRestakeEarningsUpdated

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_id | `integer` | ✅ | integer|  |  |  | |
| restake_earnings | `boolean` | ✅ | boolean|  |  |  | |


## CCD_BakerInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| aggregation_key | `string` | ✅ | string|  |  |  | |
| election_key | `string` | ✅ | string|  |  |  | |
| baker_id | `integer` | ✅ | integer|  |  |  | |
| signature_key | `string` | ✅ | string|  |  |  | |


## CCD_BakerKeysEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_id | `integer` | ✅ | integer|  |  |  | |
| account | `string` | ✅ | string|  |  |  | |
| sign_key | `string` | ✅ | string|  |  |  | |
| election_key | `string` | ✅ | string|  |  |  | |
| aggregation_key | `string` | ✅ | string|  |  |  | |


## CCD_BakerPoolInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| commission_rates | `object` | ✅ | [CCD_CommissionRates](#ccd_commissionrates)|  |  |  | |
| url | `string` | ✅ | string|  |  |  | |
| open_status | `string` | ✅ | string|  |  |  | |


## CCD_BakerRestakeEarningsUpdated

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_id | `integer` | ✅ | integer|  |  |  | |
| restake_earnings | `boolean` | ✅ | boolean|  |  |  | |


## CCD_BakerSetBakingRewardCommission

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_id | `integer` | ✅ | integer|  |  |  | |
| baking_reward_commission | `number` | ✅ | number|  |  |  | |


## CCD_BakerSetFinalizationRewardCommission

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_id | `integer` | ✅ | integer|  |  |  | |
| finalization_reward_commission | `number` | ✅ | number|  |  |  | |


## CCD_BakerSetMetadataUrl

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_id | `integer` | ✅ | integer|  |  |  | |
| url | `string` | ✅ | string|  |  |  | |


## CCD_BakerSetOpenStatus

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_id | `integer` | ✅ | integer|  |  |  | |
| open_status | `integer` | ✅ | integer|  |  |  | |


## CCD_BakerSetTransactionFeeCommission

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_id | `integer` | ✅ | integer|  |  |  | |
| transaction_fee_commission | `number` | ✅ | number|  |  |  | |


## CCD_BakerStakeDecreased

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_id | `integer` | ✅ | integer|  |  |  | |
| new_stake | `integer` | ✅ | integer|  |  |  | |


## CCD_BakerStakeIncreased

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_id | `integer` | ✅ | integer|  |  |  | |
| new_stake | `integer` | ✅ | integer|  |  |  | |


## CCD_BakerStakePendingChange

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| reduce | `object` |  | [CCD_BakerStakePendingChange_Reduce](#ccd_bakerstakependingchange_reduce)|  |  |  | |
| remove | `object` |  | [CCD_BakerStakePendingChange_Remove](#ccd_bakerstakependingchange_remove)|  |  |  | |


## CCD_BakerStakePendingChange_Reduce

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| reduced_equity_capital | `integer` | ✅ | integer|  |  |  | |
| effective_time | `string` | ✅ | Format: `date-time`|  |  |  | |


## CCD_BakerStakePendingChange_Remove

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| effective_time | `string` | ✅ | Format: `date-time`|  |  |  | |


## CCD_BakerStakeThreshold

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_stake_threshold | `integer` | ✅ | integer|  |  |  | |


## CCD_BakerStakeUpdated

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| update | `object` | ✅ | [CCD_BakerStakeUpdatedData](#ccd_bakerstakeupdateddata)|  |  |  | |


## CCD_BakerStakeUpdatedData

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_id | `integer` | ✅ | integer|  |  |  | |
| new_stake | `integer` | ✅ | integer|  |  |  | |
| increased | `boolean` | ✅ | boolean|  |  |  | |


## CCD_Block

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| transaction_summaries | `array` | ✅ | [CCD_BlockItemSummary](#ccd_blockitemsummary)|  |  |  | |


## CCD_BlockComplete

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| block_info | `object` | ✅ | [CCD_BlockInfo](#ccd_blockinfo)|  |  |  | |
| transaction_summaries | `array` | ✅ | [CCD_BlockItemSummary](#ccd_blockitemsummary)|  |  |  | |
| special_events | `array` | ✅ | [CCD_BlockSpecialEvent](#ccd_blockspecialevent)|  |  |  | |
| logged_events | `array` |  | None|  |  |  | |
| net | `string` |  | string|  |  |  | |


## CCD_BlockInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| hash | `string` | ✅ | string|  |  |  | |
| height | `integer` | ✅ | integer|  |  |  | |
| last_finalized_block | `string` | ✅ | string|  |  |  | |
| parent_block | `string` | ✅ | string|  |  |  | |
| slot_time | `string` | ✅ | Format: `date-time`|  |  |  | |
| era_block_height | `integer` | ✅ | integer|  |  |  | |
| finalized | `boolean` | ✅ | boolean|  |  |  | |
| genesis_index | `integer` | ✅ | integer|  |  |  | |
| transaction_count | `integer` | ✅ | integer|  |  |  | |
| transactions_energy_cost | `integer` | ✅ | integer|  |  |  | |
| transactions_size | `integer` | ✅ | integer|  |  |  | |
| arrive_time | `string` |  | Format: `date-time`|  |  |  | |
| baker | `integer` |  | integer|  |  |  | |
| receive_time | `string` |  | Format: `date-time`|  |  |  | |
| slot_number | `integer` |  | integer|  |  |  | |
| transaction_hashes | `array` |  | string|  |  |  | |
| state_hash | `string` |  | string|  |  |  | |
| protocol_version | `string` |  | string|  |  |  | |
| round | `integer` |  | integer|  |  |  | |
| epoch | `integer` |  | integer|  |  |  | |


## CCD_BlockItemSummary

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| hash | `string` | ✅ | string|  |  |  | |
| index | `integer` |  | integer|  |  |  | |
| energy_cost | `integer` |  | integer|  |  |  | |
| type | `object` |  | [CCD_TransactionType](#ccd_transactiontype)|  |  |  | |
| account_transaction | `object` |  | [CCD_AccountTransactionDetails](#ccd_accounttransactiondetails)|  |  |  | |
| account_creation | `object` |  | [CCD_AccountCreationDetails](#ccd_accountcreationdetails)|  |  |  | |
| update | `object` |  | [CCD_UpdateDetails](#ccd_updatedetails)|  |  |  | |
| block_info | `object` |  | [CCD_ShortBlockInfo](#ccd_shortblockinfo)|  |  |  | |


## CCD_BlockSpecialEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baking_rewards | `object` |  | [CCD_BlockSpecialEvent_BakingRewards](#ccd_blockspecialevent_bakingrewards)|  |  |  | |
| mint | `object` |  | [CCD_BlockSpecialEvent_Mint](#ccd_blockspecialevent_mint)|  |  |  | |
| finalization_rewards | `object` |  | [CCD_BlockSpecialEvent_FinalizationRewards](#ccd_blockspecialevent_finalizationrewards)|  |  |  | |
| block_reward | `object` |  | [CCD_BlockSpecialEvent_BlockReward](#ccd_blockspecialevent_blockreward)|  |  |  | |
| payday_foundation_reward | `object` |  | [CCD_BlockSpecialEvent_PaydayFoundationReward](#ccd_blockspecialevent_paydayfoundationreward)|  |  |  | |
| payday_account_reward | `object` |  | [CCD_BlockSpecialEvent_PaydayAccountReward](#ccd_blockspecialevent_paydayaccountreward)|  |  |  | |
| block_accrue_reward | `object` |  | [CCD_BlockSpecialEvent_BlockAccrueReward](#ccd_blockspecialevent_blockaccruereward)|  |  |  | |
| payday_pool_reward | `object` |  | [CCD_BlockSpecialEvent_PaydayPoolReward](#ccd_blockspecialevent_paydaypoolreward)|  |  |  | |


## CCD_BlockSpecialEvent_AccountAmounts

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| entries | `array` | ✅ | [CCD_BlockSpecialEvent_AccountAmounts_Entry](#ccd_blockspecialevent_accountamounts_entry)|  |  |  | |


## CCD_BlockSpecialEvent_AccountAmounts_Entry

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| account | `string` | ✅ | string|  |  |  | |
| amount | `integer` | ✅ | integer|  |  |  | |


## CCD_BlockSpecialEvent_BakingRewards

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_rewards | `object` | ✅ | [CCD_BlockSpecialEvent_AccountAmounts](#ccd_blockspecialevent_accountamounts)|  |  |  | |
| remainder | `integer` | ✅ | integer|  |  |  | |


## CCD_BlockSpecialEvent_BlockAccrueReward

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| transaction_fees | `integer` | ✅ | integer|  |  |  | |
| old_gas_account | `integer` | ✅ | integer|  |  |  | |
| new_gas_account | `integer` | ✅ | integer|  |  |  | |
| baker_reward | `integer` | ✅ | integer|  |  |  | |
| passive_reward | `integer` | ✅ | integer|  |  |  | |
| foundation_charge | `integer` | ✅ | integer|  |  |  | |
| baker | `integer` | ✅ | integer|  |  |  | |


## CCD_BlockSpecialEvent_BlockReward

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| transaction_fees | `integer` | ✅ | integer|  |  |  | |
| old_gas_account | `integer` | ✅ | integer|  |  |  | |
| new_gas_account | `integer` | ✅ | integer|  |  |  | |
| baker_reward | `integer` | ✅ | integer|  |  |  | |
| foundation_charge | `integer` | ✅ | integer|  |  |  | |
| foundation_account | `string` | ✅ | string|  |  |  | |
| baker | `string` | ✅ | string|  |  |  | |


## CCD_BlockSpecialEvent_FinalizationRewards

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| finalization_rewards | `object` | ✅ | [CCD_BlockSpecialEvent_AccountAmounts](#ccd_blockspecialevent_accountamounts)|  |  |  | |
| remainder | `integer` | ✅ | integer|  |  |  | |


## CCD_BlockSpecialEvent_Mint

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| mint_baking_reward | `integer` | ✅ | integer|  |  |  | |
| mint_finalization_reward | `integer` | ✅ | integer|  |  |  | |
| mint_platform_development_charge | `integer` | ✅ | integer|  |  |  | |
| foundation_account | `string` | ✅ | string|  |  |  | |


## CCD_BlockSpecialEvent_PaydayAccountReward

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| account | `string` | ✅ | string|  |  |  | |
| transaction_fees | `integer` | ✅ | integer|  |  |  | |
| baker_reward | `integer` | ✅ | integer|  |  |  | |
| finalization_reward | `integer` | ✅ | integer|  |  |  | |


## CCD_BlockSpecialEvent_PaydayFoundationReward

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| foundation_account | `string` | ✅ | string|  |  |  | |
| development_charge | `integer` | ✅ | integer|  |  |  | |


## CCD_BlockSpecialEvent_PaydayPoolReward

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| transaction_fees | `integer` | ✅ | integer|  |  |  | |
| baker_reward | `integer` | ✅ | integer|  |  |  | |
| finalization_reward | `integer` | ✅ | integer|  |  |  | |
| pool_owner | `integer` |  | integer|  |  |  | |


## CCD_BlocksAtHeightResponse

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| blocks | `array` | ✅ | string|  |  |  | |


## CCD_CapitalBound

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| value | `number` | ✅ | number|  |  |  | |


## CCD_ChainArData

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| enc_id_cred_pub_share | `string` | ✅ | string|  |  |  | |


## CCD_ChainParameters

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| v0 | `object` |  | [CCD_ChainParametersV0](#ccd_chainparametersv0)|  |  |  | |
| v1 | `object` |  | [CCD_ChainParametersV1](#ccd_chainparametersv1)|  |  |  | |
| v2 | `object` |  | [CCD_ChainParametersV2](#ccd_chainparametersv2)|  |  |  | |


## CCD_ChainParametersV0

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| election_difficulty | `number` | ✅ | number|  |  |  | |
| euro_per_energy | `object` | ✅ | [CCD_ExchangeRate](#ccd_exchangerate)|  |  |  | |
| micro_ccd_per_euro | `object` | ✅ | [CCD_ExchangeRate](#ccd_exchangerate)|  |  |  | |
| baker_cooldown_epochs | `integer` | ✅ | integer|  |  |  | |
| account_creation_limit | `integer` | ✅ | integer|  |  |  | |
| mint_distribution | `object` | ✅ | [CCD_MintDistributionCpv0](#ccd_mintdistributioncpv0)|  |  |  | |
| transaction_fee_distribution | `object` | ✅ | [CCD_TransactionFeeDistribution](#ccd_transactionfeedistribution)|  |  |  | |
| gas_rewards | `object` | ✅ | [CCD_GasRewards](#ccd_gasrewards)|  |  |  | |
| foundation_account | `string` | ✅ | string|  |  |  | |
| minimum_threshold_for_baking | `integer` | ✅ | integer|  |  |  | |
| root_keys | `object` | ✅ | [CCD_HigherLevelKeys](#ccd_higherlevelkeys)|  |  |  | |
| level1_keys | `object` | ✅ | [CCD_HigherLevelKeys](#ccd_higherlevelkeys)|  |  |  | |
| level2_keys | `object` | ✅ | [CCD_AuthorizationsV0](#ccd_authorizationsv0)|  |  |  | |


## CCD_ChainParametersV1

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| election_difficulty | `number` | ✅ | number|  |  |  | |
| euro_per_energy | `object` | ✅ | [CCD_ExchangeRate](#ccd_exchangerate)|  |  |  | |
| micro_ccd_per_euro | `object` | ✅ | [CCD_ExchangeRate](#ccd_exchangerate)|  |  |  | |
| cooldown_parameters | `object` | ✅ | [CCD_CooldownParametersCpv1](#ccd_cooldownparameterscpv1)|  |  |  | |
| time_parameters | `object` | ✅ | [CCD_TimeParametersCpv1](#ccd_timeparameterscpv1)|  |  |  | |
| account_creation_limit | `integer` | ✅ | integer|  |  |  | |
| mint_distribution | `object` | ✅ | [CCD_MintDistributionCpv1](#ccd_mintdistributioncpv1)|  |  |  | |
| transaction_fee_distribution | `object` | ✅ | [CCD_TransactionFeeDistribution](#ccd_transactionfeedistribution)|  |  |  | |
| gas_rewards | `object` | ✅ | [CCD_GasRewards](#ccd_gasrewards)|  |  |  | |
| foundation_account | `string` | ✅ | string|  |  |  | |
| pool_parameters | `object` | ✅ | [CCD_PoolParametersCpv1](#ccd_poolparameterscpv1)|  |  |  | |
| root_keys | `object` | ✅ | [CCD_HigherLevelKeys](#ccd_higherlevelkeys)|  |  |  | |
| level1_keys | `object` | ✅ | [CCD_HigherLevelKeys](#ccd_higherlevelkeys)|  |  |  | |
| level2_keys | `object` | ✅ | [CCD_AuthorizationsV1](#ccd_authorizationsv1)|  |  |  | |


## CCD_ChainParametersV2

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| consensus_parameters | `object` | ✅ | [CCD_ConsensusParametersV1](#ccd_consensusparametersv1)|  |  |  | |
| euro_per_energy | `object` | ✅ | [CCD_ExchangeRate](#ccd_exchangerate)|  |  |  | |
| micro_ccd_per_euro | `object` | ✅ | [CCD_ExchangeRate](#ccd_exchangerate)|  |  |  | |
| cooldown_parameters | `object` | ✅ | [CCD_CooldownParametersCpv1](#ccd_cooldownparameterscpv1)|  |  |  | |
| time_parameters | `object` | ✅ | [CCD_TimeParametersCpv1](#ccd_timeparameterscpv1)|  |  |  | |
| account_creation_limit | `integer` | ✅ | integer|  |  |  | |
| mint_distribution | `object` | ✅ | [CCD_MintDistributionCpv1](#ccd_mintdistributioncpv1)|  |  |  | |
| transaction_fee_distribution | `object` | ✅ | [CCD_TransactionFeeDistribution](#ccd_transactionfeedistribution)|  |  |  | |
| gas_rewards | `object` | ✅ | [CCD_GasRewardsV2](#ccd_gasrewardsv2)|  |  |  | |
| foundation_account | `string` | ✅ | string|  |  |  | |
| pool_parameters | `object` | ✅ | [CCD_PoolParametersCpv1](#ccd_poolparameterscpv1)|  |  |  | |
| root_keys | `object` | ✅ | [CCD_HigherLevelKeys](#ccd_higherlevelkeys)|  |  |  | |
| level1_keys | `object` | ✅ | [CCD_HigherLevelKeys](#ccd_higherlevelkeys)|  |  |  | |
| level2_keys | `object` | ✅ | [CCD_AuthorizationsV1](#ccd_authorizationsv1)|  |  |  | |
| finalization_committee_parameters | `object` | ✅ | [CCD_FinalizationCommitteeParameters](#ccd_finalizationcommitteeparameters)|  |  |  | |


## CCD_CommissionRanges

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| finalization | `object` | ✅ | [CCD_InclusiveRangeAmountFraction](#ccd_inclusiverangeamountfraction)|  |  |  | |
| baking | `object` | ✅ | [CCD_InclusiveRangeAmountFraction](#ccd_inclusiverangeamountfraction)|  |  |  | |
| transaction | `object` | ✅ | [CCD_InclusiveRangeAmountFraction](#ccd_inclusiverangeamountfraction)|  |  |  | |


## CCD_CommissionRates

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baking | `number` | ✅ | number|  |  |  | |
| finalization | `number` | ✅ | number|  |  |  | |
| transaction | `number` | ✅ | number|  |  |  | |


## CCD_ConsensusInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| best_block | `string` | ✅ | string|  |  |  | |
| genesis_block | `string` | ✅ | string|  |  |  | |
| genesis_time | `string` | ✅ | Format: `date-time`|  |  |  | |
| epoch_duration | `integer` | ✅ | integer|  |  |  | |
| last_finalized_block | `string` | ✅ | string|  |  |  | |
| best_block_height | `integer` | ✅ | integer|  |  |  | |
| last_finalized_block_height | `integer` | ✅ | integer|  |  |  | |
| blocks_received_count | `integer` | ✅ | integer|  |  |  | |
| block_receive_latency_ema | `number` | ✅ | number|  |  |  | |
| block_receive_latency_emsd | `number` | ✅ | number|  |  |  | |
| blocks_verified_count | `integer` | ✅ | integer|  |  |  | |
| block_arrive_latency_ema | `number` | ✅ | number|  |  |  | |
| block_arrive_latency_emsd | `number` | ✅ | number|  |  |  | |
| transactions_per_block_ema | `number` | ✅ | number|  |  |  | |
| transactions_per_block_emsd | `number` | ✅ | number|  |  |  | |
| finalization_count | `integer` | ✅ | integer|  |  |  | |
| protocol_version | `string` | ✅ | string|  |  |  | |
| genesis_index | `integer` | ✅ | integer|  |  |  | |
| current_era_genesis_block | `string` | ✅ | string|  |  |  | |
| current_era_genesis_time | `string` | ✅ | Format: `date-time`|  |  |  | |
| slot_duration | `integer` |  | integer|  |  |  | |
| block_last_received_time | `string` |  | Format: `date-time`|  |  |  | |
| block_receive_period_ema | `number` |  | number|  |  |  | |
| block_receive_period_emsd | `number` |  | number|  |  |  | |
| block_last_arrived_time | `string` |  | Format: `date-time`|  |  |  | |
| block_arrive_period_ema | `number` |  | number|  |  |  | |
| block_arrive_period_emsd | `number` |  | number|  |  |  | |
| last_finalized_time | `string` |  | Format: `date-time`|  |  |  | |
| finalization_period_ema | `number` |  | number|  |  |  | |
| finalization_period_emsd | `number` |  | number|  |  |  | |
| current_timeout_duration | `integer` |  | integer|  |  |  | |
| current_round | `integer` |  | integer|  |  |  | |
| current_epoch | `integer` |  | integer|  |  |  | |
| trigger_block_time | `string` |  | Format: `date-time`|  |  |  | |


## CCD_ConsensusParametersV1

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| timeout_parameters | `object` | ✅ | [CCD_TimeOutParameters](#ccd_timeoutparameters)|  |  |  | |
| min_block_time | `integer` | ✅ | integer|  |  |  | |
| block_energy_limit | `integer` | ✅ | integer|  |  |  | |


## CCD_ContractAddress

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| index | `integer` | ✅ | integer|  |  |  | |
| subindex | `integer` | ✅ | integer|  |  |  | |


## CCD_ContractInitializedEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| contract_version | `integer` | ✅ | integer|  |  |  | |
| origin_ref | `string` | ✅ | string|  |  |  | |
| address | `object` | ✅ | [CCD_ContractAddress](#ccd_contractaddress)|  |  |  | |
| init_name | `string` | ✅ | string|  |  |  | |
| events | `array` | ✅ | string|  |  |  | |
| amount | `integer` |  | integer|  |  |  | |


## CCD_ContractTraceElement

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| updated | `object` |  | [CCD_InstanceUpdatedEvent](#ccd_instanceupdatedevent)|  |  |  | |
| transferred | `object` |  | [CCD_ContractTraceElement_Transferred](#ccd_contracttraceelement_transferred)|  |  |  | |
| interrupted | `object` |  | [CCD_ContractTraceElement_Interrupted](#ccd_contracttraceelement_interrupted)|  |  |  | |
| resumed | `object` |  | [CCD_ContractTraceElement_Resumed](#ccd_contracttraceelement_resumed)|  |  |  | |


## CCD_ContractTraceElement_Interrupted

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| address | `object` | ✅ | [CCD_ContractAddress](#ccd_contractaddress)|  |  |  | |
| events | `array` | ✅ | string|  |  |  | |


## CCD_ContractTraceElement_Resumed

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| address | `object` | ✅ | [CCD_ContractAddress](#ccd_contractaddress)|  |  |  | |
| success | `boolean` | ✅ | boolean|  |  |  | |


## CCD_ContractTraceElement_Transferred

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| sender | `object` | ✅ | [CCD_ContractAddress](#ccd_contractaddress)|  |  |  | |
| amount | `integer` | ✅ | integer|  |  |  | |
| receiver | `string` | ✅ | string|  |  |  | |


## CCD_ContractUpdateIssued

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| effects | `array` | ✅ | [CCD_ContractTraceElement](#ccd_contracttraceelement)|  |  |  | |


## CCD_CooldownParametersCpv1

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| pool_owner_cooldown | `integer` |  | integer|  |  |  | |
| delegator_cooldown | `integer` |  | integer|  |  |  | |


## CCD_CredentialCommitments

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| prf | `string` | ✅ | string|  |  |  | |
| cred_counter | `string` | ✅ | string|  |  |  | |
| max_accounts | `string` | ✅ | string|  |  |  | |
| attributes | `string` | ✅ | string|  |  |  | |
| id_cred_sec_sharing_coeff | `array` | ✅ | string|  |  |  | |


## CCD_CredentialPublicKeys

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| keys | `object` | ✅ | [CCD_AccountVerifyKey](#ccd_accountverifykey)|  |  |  | |
| threshold | `integer` | ✅ | integer|  |  |  | |


## CCD_CurrentPaydayStatus

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker_equity_capital | `integer` | ✅ | integer|  |  |  | |
| blocks_baked | `integer` | ✅ | integer|  |  |  | |
| delegated_capital | `integer` | ✅ | integer|  |  |  | |
| effective_stake | `integer` | ✅ | integer|  |  |  | |
| finalization_live | `boolean` | ✅ | boolean|  |  |  | |
| lottery_power | `number` | ✅ | number|  |  |  | |
| transaction_fees_earned | `integer` | ✅ | integer|  |  |  | |


## CCD_DelegationConfigured

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| events | `array` | ✅ | [CCD_DelegationEvent](#ccd_delegationevent)|  |  |  | |


## CCD_DelegationEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| delegation_added | `integer` |  | integer|  |  |  | |
| delegation_removed | `integer` |  | integer|  |  |  | |
| delegation_stake_increased | `object` |  | [CCD_DelegationStakeIncreased](#ccd_delegationstakeincreased)|  |  |  | |
| delegation_stake_decreased | `object` |  | [CCD_DelegationStakeDecreased](#ccd_delegationstakedecreased)|  |  |  | |
| delegation_set_restake_earnings | `object` |  | [CCD_DelegationSetRestakeEarnings](#ccd_delegationsetrestakeearnings)|  |  |  | |
| delegation_set_delegation_target | `object` |  | [CCD_DelegationSetDelegationTarget](#ccd_delegationsetdelegationtarget)|  |  |  | |


## CCD_DelegationSetDelegationTarget

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| delegator_id | `integer` | ✅ | integer|  |  |  | |
| delegation_target | `object` | ✅ | [CCD_DelegationTarget](#ccd_delegationtarget)|  |  |  | |


## CCD_DelegationSetRestakeEarnings

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| delegator_id | `integer` | ✅ | integer|  |  |  | |
| restake_earnings | `boolean` | ✅ | boolean|  |  |  | |


## CCD_DelegationStakeDecreased

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| delegator_id | `integer` | ✅ | integer|  |  |  | |
| new_stake | `integer` | ✅ | integer|  |  |  | |


## CCD_DelegationStakeIncreased

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| delegator_id | `integer` | ✅ | integer|  |  |  | |
| new_stake | `integer` | ✅ | integer|  |  |  | |


## CCD_DelegationTarget

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| passive_delegation | `boolean` |  | boolean|  |  |  | |
| baker | `integer` |  | integer|  |  |  | |


## CCD_DelegatorInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| account | `string` | ✅ | string|  |  |  | |
| stake | `integer` | ✅ | integer|  |  |  | |
| pending_change | `object` |  | [CCD_StakePendingChange](#ccd_stakependingchange)|  |  |  | |


## CCD_DelegatorRewardPeriodInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| account | `string` | ✅ | string|  |  |  | |
| stake | `integer` | ✅ | integer|  |  |  | |


## CCD_Description

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| name | `string` | ✅ | string|  |  |  | |
| url | `string` | ✅ | string|  |  |  | |
| description | `string` | ✅ | string|  |  |  | |


## CCD_ElectionInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| election_nonce | `string` | ✅ | string|  |  |  | |
| baker_election_info | `array` | ✅ | [CCD_ElectionInfo_Baker](#ccd_electioninfo_baker)|  |  |  | |
| election_difficulty | `number` |  | number|  |  |  | |


## CCD_ElectionInfo_Baker

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker | `integer` | ✅ | integer|  |  |  | |
| account | `string` | ✅ | string|  |  |  | |
| lottery_power | `number` | ✅ | number|  |  |  | |


## CCD_EncryptedAmountRemovedEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| account | `string` | ✅ | string|  |  |  | |
| new_amount | `string` | ✅ | string|  |  |  | |
| input_amount | `string` | ✅ | string|  |  |  | |
| up_to_index | `integer` | ✅ | integer|  |  |  | |


## CCD_EncryptedBalance

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| self_amount | `string` | ✅ | string|  |  |  | |
| start_index | `integer` | ✅ | integer|  |  |  | |
| incoming_amounts | `array` | ✅ | string|  |  |  | |
| aggregated_amount | `string` |  | string|  |  |  | |
| num_aggregated | `integer` |  | integer|  |  |  | |


## CCD_EncryptedSelfAmountAddedEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| account | `string` | ✅ | string|  |  |  | |
| new_amount | `string` | ✅ | string|  |  |  | |
| amount | `integer` | ✅ | integer|  |  |  | |


## CCD_ExchangeRate

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| numerator | `string` | ✅ | string|  |  |  | |
| denominator | `string` | ✅ | string|  |  |  | |


## CCD_FinalizationCommitteeParameters

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| minimum_finalizers | `integer` | ✅ | integer|  |  |  | |
| maximum_finalizers | `integer` | ✅ | integer|  |  |  | |
| finalizer_relative_stake_threshold | `number` | ✅ | number|  |  |  | |


## CCD_FinalizedBlockInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| hash | `string` | ✅ | string|  |  |  | |
| height | `integer` | ✅ | integer|  |  |  | |


## CCD_GasRewards

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker | `number` | ✅ | number|  |  |  | |
| finalization_proof | `number` | ✅ | number|  |  |  | |
| account_creation | `number` | ✅ | number|  |  |  | |
| chain_update | `number` | ✅ | number|  |  |  | |


## CCD_GasRewardsV2

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker | `number` | ✅ | number|  |  |  | |
| account_creation | `number` | ✅ | number|  |  |  | |
| chain_update | `number` | ✅ | number|  |  |  | |


## CCD_HigherLevelKeys

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| keys | `array` | ✅ | string|  |  |  | |
| threshold | `integer` | ✅ | integer|  |  |  | |


## CCD_InclusiveRangeAmountFraction

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| min | `number` | ✅ | number|  |  |  | |
| max_ | `number` | ✅ | number|  |  |  | |


## CCD_InitialCredentialValues

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| credential_public_keys | `object` | ✅ | [CCD_CredentialPublicKeys](#ccd_credentialpublickeys)|  |  |  | |
| cred_id | `string` | ✅ | string|  |  |  | |
| ip_id | `integer` | ✅ | integer|  |  |  | |
| policy | `object` | ✅ | [CCD_Policy](#ccd_policy)|  |  |  | |


## CCD_InstanceInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| v0 | `object` | ✅ | [CCD_InstanceInfo_V0](#ccd_instanceinfo_v0)|  |  |  | |
| v1 | `object` | ✅ | [CCD_InstanceInfo_V1](#ccd_instanceinfo_v1)|  |  |  | |


## CCD_InstanceInfo_V0

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| model | `string` | ✅ | string|  |  |  | |
| owner | `string` | ✅ | string|  |  |  | |
| amount | `integer` | ✅ | integer|  |  |  | |
| methods | `array` | ✅ | string|  |  |  | |
| name | `string` | ✅ | string|  |  |  | |
| source_module | `string` | ✅ | string|  |  |  | |


## CCD_InstanceInfo_V1

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| owner | `string` | ✅ | string|  |  |  | |
| amount | `integer` | ✅ | integer|  |  |  | |
| methods | `array` | ✅ | string|  |  |  | |
| name | `string` | ✅ | string|  |  |  | |
| source_module | `string` | ✅ | string|  |  |  | |


## CCD_InstanceUpdatedEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| contract_version | `integer` | ✅ | integer|  |  |  | |
| address | `object` | ✅ | [CCD_ContractAddress](#ccd_contractaddress)|  |  |  | |
| instigator | `object` | ✅ | [CCD_Address](#ccd_address)|  |  |  | |
| amount | `integer` | ✅ | integer|  |  |  | |
| parameter | `string` | ✅ | string|  |  |  | |
| receive_name | `string` | ✅ | string|  |  |  | |
| events | `array` |  | string|  |  |  | |


## CCD_InvokeInstanceResponse

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| success | `object` | ✅ | [CCD_InvokeInstanceResponse_Success](#ccd_invokeinstanceresponse_success)|  |  |  | |
| failure | `object` | ✅ | [CCD_InvokeInstanceResponse_Failure](#ccd_invokeinstanceresponse_failure)|  |  |  | |


## CCD_InvokeInstanceResponse_Failure

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| return_value | `string` | ✅ | Format: `binary`|  |  |  | |
| used_energy | `integer` | ✅ | integer|  |  |  | |
| reason | `object` | ✅ | [CCD_RejectReason](#ccd_rejectreason)|  |  |  | |


## CCD_InvokeInstanceResponse_Success

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| return_value | `string` | ✅ | Format: `binary`|  |  |  | |
| used_energy | `integer` | ✅ | integer|  |  |  | |
| effects | `array` | ✅ | [CCD_ContractTraceElement](#ccd_contracttraceelement)|  |  |  | |


## CCD_IpInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| identity | `integer` | ✅ | integer|  |  |  | |
| description | `object` | ✅ | [CCD_Description](#ccd_description)|  |  |  | |
| verify_key | `string` | ✅ | string|  |  |  | |
| cdi_verify_key | `string` | ✅ | string|  |  |  | |


## CCD_Level1Update

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| level_1_keys_update | `object` |  | [CCD_HigherLevelKeys](#ccd_higherlevelkeys)|  |  |  | |
| level_2_keys_update_v0 | `object` |  | [CCD_AuthorizationsV0](#ccd_authorizationsv0)|  |  |  | |
| level_2_keys_update_v1 | `object` |  | [CCD_AuthorizationsV1](#ccd_authorizationsv1)|  |  |  | |


## CCD_LeverageFactor

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| value | `object` | ✅ | [CCD_Ratio](#ccd_ratio)|  |  |  | |


## CCD_MintDistributionCpv0

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| mint_per_slot | `object` | ✅ | [CCD_MintRate](#ccd_mintrate)|  |  |  | |
| baking_reward | `number` | ✅ | number|  |  |  | |
| finalization_reward | `number` | ✅ | number|  |  |  | |


## CCD_MintDistributionCpv1

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baking_reward | `number` | ✅ | number|  |  |  | |
| finalization_reward | `number` | ✅ | number|  |  |  | |


## CCD_MintRate

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| mantissa | `integer` | ✅ | integer|  |  |  | |
| exponent | `integer` | ✅ | integer|  |  |  | |


## CCD_NewEncryptedAmountEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| receiver | `string` | ✅ | string|  |  |  | |
| new_index | `integer` | ✅ | integer|  |  |  | |
| encrypted_amount | `string` | ✅ | string|  |  |  | |


## CCD_NewRelease

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| timestamp | `string` | ✅ | Format: `date-time`|  |  |  | |
| amount | `integer` | ✅ | integer|  |  |  | |


## CCD_NormalCredentialValues

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| credential_public_keys | `object` | ✅ | [CCD_CredentialPublicKeys](#ccd_credentialpublickeys)|  |  |  | |
| cred_id | `string` | ✅ | string|  |  |  | |
| ip_id | `integer` | ✅ | integer|  |  |  | |
| policy | `object` | ✅ | [CCD_Policy](#ccd_policy)|  |  |  | |
| ar_threshold | `integer` | ✅ | integer|  |  |  | |
| ar_data | `object` | ✅ | [CCD_ChainArData](#ccd_chainardata)|  |  |  | |
| commitments | `object` | ✅ | [CCD_CredentialCommitments](#ccd_credentialcommitments)|  |  |  | |


## CCD_PassiveDelegationInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| all_pool_total_capital | `integer` | ✅ | integer|  |  |  | |
| delegated_capital | `integer` | ✅ | integer|  |  |  | |
| current_payday_transaction_fees_earned | `integer` | ✅ | integer|  |  |  | |
| current_payday_delegated_capital | `integer` | ✅ | integer|  |  |  | |
| commission_rates | `object` | ✅ | [CCD_CommissionRates](#ccd_commissionrates)|  |  |  | |


## CCD_PendingUpdate

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| effective_time | `integer` | ✅ | integer|  |  |  | |
| gas_rewards | `object` | ✅ | [CCD_GasRewards](#ccd_gasrewards)|  |  |  | |
| root_keys | `object` |  | [CCD_HigherLevelKeys](#ccd_higherlevelkeys)|  |  |  | |
| level1_keys | `object` |  | [CCD_HigherLevelKeys](#ccd_higherlevelkeys)|  |  |  | |
| level2_keys_cpc_0 | `object` |  | [CCD_AuthorizationsV0](#ccd_authorizationsv0)|  |  |  | |
| level2_keys_cpc_1 | `object` |  | [CCD_AuthorizationsV1](#ccd_authorizationsv1)|  |  |  | |
| protocol | `object` |  | [CCD_ProtocolUpdate](#ccd_protocolupdate)|  |  |  | |
| election_difficulty | `number` |  | number|  |  |  | |
| euro_per_energy | `object` |  | [CCD_ExchangeRate](#ccd_exchangerate)|  |  |  | |
| micro_ccd_per_euro | `object` |  | [CCD_ExchangeRate](#ccd_exchangerate)|  |  |  | |
| foundation_account | `string` |  | string|  |  |  | |
| mint_distribution_cpv_0 | `object` |  | [CCD_MintDistributionCpv0](#ccd_mintdistributioncpv0)|  |  |  | |
| mint_distribution_cpv_1 | `object` |  | [CCD_MintDistributionCpv1](#ccd_mintdistributioncpv1)|  |  |  | |
| transaction_fee_distribution | `object` |  | [CCD_TransactionFeeDistribution](#ccd_transactionfeedistribution)|  |  |  | |
| pool_parameters_cpv_0 | `object` |  | [CCD_PoolParametersCpv1](#ccd_poolparameterscpv1)|  |  |  | |
| add_anonymity_revoker | `object` |  | [CCD_ArInfo](#ccd_arinfo)|  |  |  | |
| add_identity_provider | `object` |  | [CCD_IpInfo](#ccd_ipinfo)|  |  |  | |
| cooldown_parameters | `object` |  | [CCD_CooldownParametersCpv1](#ccd_cooldownparameterscpv1)|  |  |  | |
| pool_parameters_cpv_1_update | `object` |  | [CCD_PoolParametersCpv1](#ccd_poolparameterscpv1)|  |  |  | |
| time_parameters | `object` |  | [CCD_TimeParametersCpv1](#ccd_timeparameterscpv1)|  |  |  | |


## CCD_Policy

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| created_at | `object` | ✅ | [CCD_YearMonth](#ccd_yearmonth)|  |  |  | |
| valid_to | `object` | ✅ | [CCD_YearMonth](#ccd_yearmonth)|  |  |  | |
| attributes | `string` | ✅ | string|  |  |  | |


## CCD_PoolInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| all_pool_total_capital | `integer` | ✅ | integer|  |  |  | |
| address | `string` | ✅ | string|  |  |  | |
| equity_capital | `integer` | ✅ | integer|  |  |  | |
| baker | `integer` | ✅ | integer|  |  |  | |
| delegated_capital | `integer` | ✅ | integer|  |  |  | |
| delegated_capital_cap | `integer` | ✅ | integer|  |  |  | |
| pool_info | `object` | ✅ | [CCD_BakerPoolInfo](#ccd_bakerpoolinfo)|  |  |  | |
| equity_pending_change | `object` |  | [CCD_BakerStakePendingChange](#ccd_bakerstakependingchange)|  |  |  | |
| current_payday_info | `object` |  | [CCD_CurrentPaydayStatus](#ccd_currentpaydaystatus)|  |  |  | |


## CCD_PoolParametersCpv1

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| passive_finalization_commission | `number` | ✅ | number|  |  |  | |
| passive_baking_commission | `number` | ✅ | number|  |  |  | |
| passive_transaction_commission | `number` | ✅ | number|  |  |  | |
| commission_bounds | `object` | ✅ | [CCD_CommissionRanges](#ccd_commissionranges)|  |  |  | |
| minimum_equity_capital | `integer` | ✅ | integer|  |  |  | |
| capital_bound | `object` | ✅ | [CCD_CapitalBound](#ccd_capitalbound)|  |  |  | |
| leverage_bound | `object` | ✅ | [CCD_LeverageFactor](#ccd_leveragefactor)|  |  |  | |


## CCD_ProtocolUpdate

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| message_ | `string` | ✅ | string|  |  |  | |
| specification_url | `string` | ✅ | string|  |  |  | |
| specificationHash | `string` | ✅ | string|  |  |  | |
| specification_auxiliary_data | `string` |  | Format: `binary`|  |  |  | |


## CCD_Ratio

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| numerator | `string` | ✅ | string|  |  |  | |
| denominator | `string` | ✅ | string|  |  |  | |


## CCD_RejectReason

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| module_not_wf | `null` |  | null|  |  |  | |
| module_hash_already_exists | `string` |  | string|  |  |  | |
| invalid_account_reference | `string` |  | string|  |  |  | |
| invalid_init_method | `object` |  | [CCD_RejectReason_InvalidInitMethod](#ccd_rejectreason_invalidinitmethod)|  |  |  | |
| invalid_receive_method | `object` |  | [CCD_RejectReason_InvalidReceiveMethod](#ccd_rejectreason_invalidreceivemethod)|  |  |  | |
| invalid_module_reference | `string` |  | string|  |  |  | |
| invalid_contract_address | `object` |  | [CCD_ContractAddress](#ccd_contractaddress)|  |  |  | |
| runtime_failure | `null` |  | null|  |  |  | |
| amount_too_large | `object` |  | [CCD_RejectReason_AmountTooLarge](#ccd_rejectreason_amounttoolarge)|  |  |  | |
| serialization_failure | `null` |  | null|  |  |  | |
| out_of_energy | `null` |  | null|  |  |  | |
| rejected_init | `object` |  | [CCD_RejectReason_RejectedInit](#ccd_rejectreason_rejectedinit)|  |  |  | |
| rejected_receive | `object` |  | [CCD_RejectReason_RejectedReceive](#ccd_rejectreason_rejectedreceive)|  |  |  | |
| invalid_proof | `null` |  | null|  |  |  | |
| already_a_baker | `integer` |  | integer|  |  |  | |
| not_a_baker | `string` |  | string|  |  |  | |
| insufficient_balance_for_baker_stake | `null` |  | null|  |  |  | |
| stake_under_minimum_threshold_for_baking | `null` |  | null|  |  |  | |
| baker_in_cooldown | `null` |  | null|  |  |  | |
| duplicate_aggregation_key | `string` |  | string|  |  |  | |
| non_existent_credential_id | `null` |  | null|  |  |  | |
| key_index_already_in_use | `null` |  | null|  |  |  | |
| invalid_account_threshold | `null` |  | null|  |  |  | |
| invalid_credential_key_sign_threshold | `null` |  | null|  |  |  | |
| invalid_encrypted_amount_transfer_proof | `null` |  | null|  |  |  | |
| invalid_transfer_to_public_proof | `null` |  | null|  |  |  | |
| encrypted_amount_self_transfer | `string` |  | string|  |  |  | |
| invalid_index_on_encrypted_transfer | `null` |  | null|  |  |  | |
| zero_scheduledAmount | `null` |  | null|  |  |  | |
| non_increasing_schedule | `null` |  | null|  |  |  | |
| first_scheduled_release_expired | `null` |  | null|  |  |  | |
| scheduled_self_transfer | `string` |  | string|  |  |  | |
| invalid_credentials | `null` |  | null|  |  |  | |
| duplicate_cred_ids | `object` |  | [CCD_RejectReason_DuplicateCredIds](#ccd_rejectreason_duplicatecredids)|  |  |  | |
| non_existent_cred_ids | `object` |  | [CCD_RejectReason_NonExistentCredIds](#ccd_rejectreason_nonexistentcredids)|  |  |  | |
| remove_first_credential | `null` |  | null|  |  |  | |
| credential_holder_did_not_sign | `null` |  | null|  |  |  | |
| not_allowed_multiple_credentials | `null` |  | null|  |  |  | |
| not_allowed_to_receive_encrypted | `null` |  | null|  |  |  | |
| not_allowed_to_handle_encrypted | `null` |  | null|  |  |  | |
| missing_baker_add_parameters | `null` |  | null|  |  |  | |
| finalization_reward_commission_not_in_range | `null` |  | null|  |  |  | |
| baking_reward_commission_not_in_range | `null` |  | null|  |  |  | |
| transaction_fee_commission_not_in_range | `null` |  | null|  |  |  | |
| already_a_delegator | `null` |  | null|  |  |  | |
| insufficient_balance_for_delegation_stake | `null` |  | null|  |  |  | |
| missing_delegation_add_parameters | `null` |  | null|  |  |  | |
| insufficient_delegation_stake | `null` |  | null|  |  |  | |
| delegator_in_cooldown | `null` |  | null|  |  |  | |
| not_a_delegator | `string` |  | string|  |  |  | |
| delegation_target_not_a_baker | `integer` |  | integer|  |  |  | |
| stake_over_maximum_threshold_for_pool | `null` |  | null|  |  |  | |
| pool_would_become_over_delegated | `null` |  | null|  |  |  | |
| pool_closed | `null` |  | null|  |  |  | |


## CCD_RejectReason_AmountTooLarge

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| address | `object` | ✅ | [CCD_Address](#ccd_address)|  |  |  | |
| amount | `integer` | ✅ | integer|  |  |  | |


## CCD_RejectReason_DuplicateCredIds

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| ids | `array` | ✅ | string|  |  |  | |


## CCD_RejectReason_InvalidInitMethod

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| module_ref | `string` | ✅ | string|  |  |  | |
| init_name | `string` | ✅ | string|  |  |  | |


## CCD_RejectReason_InvalidReceiveMethod

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| module_ref | `string` | ✅ | string|  |  |  | |
| receive_name | `string` | ✅ | string|  |  |  | |


## CCD_RejectReason_NonExistentCredIds

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| ids | `array` | ✅ | string|  |  |  | |


## CCD_RejectReason_RejectedInit

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| reject_reason | `integer` | ✅ | integer|  |  |  | |


## CCD_RejectReason_RejectedReceive

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| reject_reason | `integer` | ✅ | integer|  |  |  | |
| contract_address | `object` | ✅ | [CCD_ContractAddress](#ccd_contractaddress)|  |  |  | |
| receive_name | `string` | ✅ | string|  |  |  | |
| parameter | `string` | ✅ | string|  |  |  | |


## CCD_Release

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| timestamp | `string` | ✅ | Format: `date-time`|  |  |  | |
| amount | `integer` | ✅ | integer|  |  |  | |
| transactions | `array` | ✅ | string|  |  |  | |


## CCD_ReleaseSchedule

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| schedules | `array` | ✅ | [CCD_Release](#ccd_release)|  |  |  | |
| total | `integer` | ✅ | integer|  |  |  | |


## CCD_RootUpdate

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| root_keys_update | `object` | ✅ | [CCD_HigherLevelKeys](#ccd_higherlevelkeys)|  |  |  | |
| level_1_keys_update | `object` | ✅ | [CCD_HigherLevelKeys](#ccd_higherlevelkeys)|  |  |  | |
| level_2_keys_update_v0 | `object` | ✅ | [CCD_AuthorizationsV0](#ccd_authorizationsv0)|  |  |  | |
| level_2_keys_update_v1 | `object` | ✅ | [CCD_AuthorizationsV1](#ccd_authorizationsv1)|  |  |  | |


## CCD_ShortBlockInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| height | `integer` | ✅ | integer|  |  |  | |
| hash | `string` | ✅ | string|  |  |  | |
| slot_time | `string` | ✅ | Format: `date-time`|  |  |  | |


## CCD_StakePendingChange

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| reduce | `object` |  | [CCD_StakePendingChange_Reduce](#ccd_stakependingchange_reduce)|  |  |  | |
| remove | `string` |  | Format: `date-time`|  |  |  | |


## CCD_StakePendingChange_Reduce

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| new_stake | `integer` | ✅ | integer|  |  |  | |
| effective_time | `string` | ✅ | Format: `date-time`|  |  |  | |


## CCD_TimeOutParameters

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| timeout_base | `integer` | ✅ | integer|  |  |  | |
| timeout_increase | `object` | ✅ | [CCD_Ratio](#ccd_ratio)|  |  |  | |
| timeout_decrease | `object` | ✅ | [CCD_Ratio](#ccd_ratio)|  |  |  | |


## CCD_TimeParametersCpv1

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| reward_period_length | `integer` | ✅ | integer|  |  |  | |
| mint_per_payday | `object` | ✅ | [CCD_MintRate](#ccd_mintrate)|  |  |  | |


## CCD_TokenomicsInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| v0 | `object` |  | [CCD_TokenomicsInfo_V0](#ccd_tokenomicsinfo_v0)|  |  |  | |
| v1 | `object` |  | [CCD_TokenomicsInfo_V1](#ccd_tokenomicsinfo_v1)|  |  |  | |


## CCD_TokenomicsInfo_V0

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| total_amount | `integer` | ✅ | integer|  |  |  | |
| total_encrypted_amount | `integer` | ✅ | integer|  |  |  | |
| baking_reward_account | `integer` | ✅ | integer|  |  |  | |
| finalization_reward_account | `integer` | ✅ | integer|  |  |  | |
| gas_account | `integer` | ✅ | integer|  |  |  | |
| protocol_version | `integer` | ✅ | integer|  |  |  | |


## CCD_TokenomicsInfo_V1

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| total_amount | `integer` | ✅ | integer|  |  |  | |
| total_encrypted_amount | `integer` | ✅ | integer|  |  |  | |
| baking_reward_account | `integer` | ✅ | integer|  |  |  | |
| finalization_reward_account | `integer` | ✅ | integer|  |  |  | |
| gas_account | `integer` | ✅ | integer|  |  |  | |
| foundation_transaction_rewards | `integer` | ✅ | integer|  |  |  | |
| next_payday_time | `string` | ✅ | Format: `date-time`|  |  |  | |
| next_payday_mint_rate | `object` | ✅ | [CCD_MintRate](#ccd_mintrate)|  |  |  | |
| total_staked_capital | `integer` | ✅ | integer|  |  |  | |
| protocol_version | `integer` | ✅ | integer|  |  |  | |


## CCD_TransactionFeeDistribution

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baker | `number` |  | number|  |  |  | |
| gas_account | `number` |  | number|  |  |  | |


## CCD_TransactionType

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| type | `string` | ✅ | string|  |  |  | |
| contents | `string` | ✅ | string|  |  |  | |


## CCD_TransferredWithSchedule

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| receiver | `string` | ✅ | string|  |  |  | |
| amount | `array` | ✅ | [CCD_NewRelease](#ccd_newrelease)|  |  |  | |
| memo | `string` |  | string|  |  |  | |


## CCD_UpdateDetails

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| payload | `object` | ✅ | [CCD_UpdatePayload](#ccd_updatepayload)|  |  |  | |
| effective_time | `integer` |  | integer|  |  |  | |


## CCD_UpdatePayload

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| protocol_update | `object` |  | [CCD_ProtocolUpdate](#ccd_protocolupdate)|  |  |  | |
| election_difficulty_update | `number` |  | number|  |  |  | |
| euro_per_energy_update | `object` |  | [CCD_ExchangeRate](#ccd_exchangerate)|  |  |  | |
| micro_ccd_per_euro_update | `object` |  | [CCD_ExchangeRate](#ccd_exchangerate)|  |  |  | |
| foundation_account_update | `string` |  | string|  |  |  | |
| mint_distribution_update | `object` |  | [CCD_MintDistributionCpv0](#ccd_mintdistributioncpv0)|  |  |  | |
| transaction_fee_distribution_update | `object` |  | [CCD_TransactionFeeDistribution](#ccd_transactionfeedistribution)|  |  |  | |
| baker_stake_threshold_update | `object` |  | [CCD_BakerStakeThreshold](#ccd_bakerstakethreshold)|  |  |  | |
| root_update | `object` |  | [CCD_RootUpdate](#ccd_rootupdate)|  |  |  | |
| level_1_update | `object` |  | [CCD_Level1Update](#ccd_level1update)|  |  |  | |
| add_anonymity_revoker_update | `object` |  | [CCD_ArInfo](#ccd_arinfo)|  |  |  | |
| add_identity_provider_update | `object` |  | [CCD_IpInfo](#ccd_ipinfo)|  |  |  | |
| cooldown_parameters_cpv_1_update | `object` |  | [CCD_CooldownParametersCpv1](#ccd_cooldownparameterscpv1)|  |  |  | |
| pool_parameters_cpv_1_update | `object` |  | [CCD_PoolParametersCpv1](#ccd_poolparameterscpv1)|  |  |  | |
| time_parameters_cpv_1_update | `object` |  | [CCD_TimeParametersCpv1](#ccd_timeparameterscpv1)|  |  |  | |
| mint_distribution_cpv_1_update | `object` |  | [CCD_MintDistributionCpv1](#ccd_mintdistributioncpv1)|  |  |  | |
| finalization_committee_parameters_update | `object` |  | [CCD_FinalizationCommitteeParameters](#ccd_finalizationcommitteeparameters)|  |  |  | |


## CCD_VersionedModuleSource

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| v0 | `string` |  | string|  |  |  | |
| v1 | `string` |  | string|  |  |  | |


## CCD_YearMonth

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| year | `integer` | ✅ | integer|  |  |  | |
| month | `integer` | ✅ | integer|  |  |  | |


---

Markdown generated with [jsonschema-markdown](https://github.com/elisiariocouto/jsonschema-markdown).
