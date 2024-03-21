# MongoTypes

This Model is constructed only to generate documentation.

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| Collections | `string` | ✅ | [Collections](#collections)|  |  |  | |
| CollectionsUtilities | `string` | ✅ | [CollectionsUtilities](#collectionsutilities)|  |  |  | |
| MongoImpactedAddress | `object` | ✅ | [MongoImpactedAddress](#mongoimpactedaddress)|  |  |  | |
| MongoLabeledAccount | `object` | ✅ | [MongoLabeledAccount](#mongolabeledaccount)|  |  |  | |
| MongoTypeAccountReward | `object` | ✅ | [MongoTypeAccountReward](#mongotypeaccountreward)|  |  |  | |
| MongoTypeBlockPerDay | `object` | ✅ | [MongoTypeBlockPerDay](#mongotypeblockperday)|  |  |  | |
| MongoTypeInvolvedAccount | `object` | ✅ | [MongoTypeInvolvedAccount](#mongotypeinvolvedaccount)|  |  |  | |
| MongoTypeInvolvedContract | `object` | ✅ | [MongoTypeInvolvedContract](#mongotypeinvolvedcontract)|  |  |  | |
| MongoTypeInstance | `object` | ✅ | [MongoTypeInstance](#mongotypeinstance)|  |  |  | |
| MongoTypeLoggedEvent | `object` | ✅ | [MongoTypeLoggedEvent](#mongotypeloggedevent)|  |  |  | |
| MongoTypeModule | `object` | ✅ | [MongoTypeModule](#mongotypemodule)|  |  |  | |
| MongoTypeReward | `object` | ✅ | [MongoTypeReward](#mongotypereward)|  |  |  | |
| MongoTypePayday | `object` | ✅ | [MongoTypePayday](#mongotypepayday)|  |  |  | |
| MongoTypePaydayAPYIntermediate | `object` | ✅ | [MongoTypePaydayAPYIntermediate](#mongotypepaydayapyintermediate)|  |  |  | |
| MongoTypePaydaysPerformance | `object` | ✅ | [MongoTypePaydaysPerformance](#mongotypepaydaysperformance)|  |  |  | |
| MongoTypePoolReward | `object` | ✅ | [MongoTypePoolReward](#mongotypepoolreward)|  |  |  | |
| MongoTypeTokenAddress | `object` | ✅ | [MongoTypeTokenAddress](#mongotypetokenaddress)|  |  |  | |
| MongoTypeTokenHolderAddress | `object` | ✅ | [MongoTypeTokenHolderAddress](#mongotypetokenholderaddress)|  |  |  | |
| MongoTypeTokenLink | `object` | ✅ | [MongoTypeTokenLink](#mongotypetokenlink)|  |  |  | |
| MongoTypeTokensTag | `object` | ✅ | [MongoTypeTokensTag](#mongotypetokenstag)|  |  |  | |


---

# Definitions



## AccountStatementEntryType

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| amount_decrypted | `integer` |  | integer|  |  |  | |
| amount_encrypted | `integer` |  | integer|  |  |  | |
| baker_reward | `integer` |  | integer|  |  |  | |
| finalization_reward | `integer` |  | integer|  |  |  | |
| foundation_reward | `integer` |  | integer|  |  |  | |
| transaction_fee | `integer` |  | integer|  |  |  | |
| transaction_fee_reward | `integer` |  | integer|  |  |  | |
| transfer_in | `array` |  | [AccountStatementTransferType](#accountstatementtransfertype)|  |  |  | |
| transfer_out | `array` |  | [AccountStatementTransferType](#accountstatementtransfertype)|  |  |  | |


## AccountStatementTransferType

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| amount | `integer` | ✅ | integer|  |  |  | |
| counterparty | `string` | ✅ | string|  |  |  | |


## CCD_BakerPoolInfo

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| commission_rates | `object` | ✅ | [CCD_CommissionRates](#ccd_commissionrates)|  |  |  | |
| url | `string` | ✅ | string|  |  |  | |
| open_status | `string` | ✅ | string|  |  |  | |


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


## CCD_CommissionRates

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| baking | `number` | ✅ | number|  |  |  | |
| finalization | `number` | ✅ | number|  |  |  | |
| transaction | `number` | ✅ | number|  |  |  | |


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


## Collections

No description provided for this model.

### Type: `string`

**Possible Values:** `blocks` or `transactions` or `special_events` or `instances` or `modules` or `messages` or `paydays` or `paydays_performance` or `paydays_rewards` or `paydays_apy_intermediate` or `paydays_current_payday` or `paydays_helpers` or `involved_accounts_all` or `involved_accounts_all_top_list` or `involved_accounts_transfer` or `involved_contracts` or `nightly_accounts` or `blocks_at_end_of_day` or `blocks_per_day` or `helpers` or `memo_transaction_hashes` or `cns_domains` or `bot_messages` or `dashboard_nodes` or `tokens_accounts` or `tokens_links_v2` or `tokens_token_addresses_v2` or `tokens_tags` or `tokens_logged_events` or `tokens_token_addresses` or `memos_to_hashes` or `credentials_issuers` or `impacted_addresses` or `impacted_addresses_pre_payday` or `impacted_addresses_all_top_list` or `pre_tokens_overview` or `pre_addresses_by_contract_count` or `pre_tokens_by_address` or `statistics` or `pre_render` or `usecases`



## CollectionsUtilities

No description provided for this model.

### Type: `string`

**Possible Values:** `labeled_accounts` or `labeled_accounts_metadata` or `users_prod` or `users_dev` or `exchange_rates` or `exchange_rates_historical` or `users_v2_prod` or `users_v2_dev` or `message_log` or `preferences_explanations` or `release_notes` or `token_api_translations` or `usecases` or `helpers`



## Delegator

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| account | `string` | ✅ | string|  |  |  | |
| stake | `integer` | ✅ | integer|  |  |  | |


## FailedAttempt

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| attempts | `integer` | ✅ | integer|  |  |  | |
| do_not_try_before | `string` | ✅ | Format: `date-time`|  |  |  | |
| last_error | `string` | ✅ | string|  |  |  | |


## MongoImpactedAddress

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| impacted_address | `string` | ✅ | string|  |  |  | |
| impacted_address_canonical | `string` | ✅ | string|  |  |  | |
| effect_type | `string` | ✅ | string|  |  |  | |
| block_height | `integer` | ✅ | integer|  |  |  | |
| tx_hash | `string` |  | string|  |  |  | |
| balance_movement | `object` |  | [AccountStatementEntryType](#accountstatemententrytype)|  |  |  | |
| included_in_flow | `boolean` |  | boolean|  |  |  | |
| date | `string` |  | string|  |  |  | |


## MongoLabeledAccount

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| label | `string` | ✅ | string|  |  |  | |
| label_group | `string` | ✅ | string|  |  |  | |
| account_index | `integer` |  | integer|  |  |  | |


## MongoTypeAccountReward

Module. This type is stored in the collection `payday_rewards`.

:Parameters:
- `_id`: the hex string
- `module_name`: the name from the module
- `methods`: list of method names
- `contracts`: list of contract instances from this module

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| account_id | `string` | ✅ | string|  |  |  | |
| staked_amount | `integer` | ✅ | integer|  |  |  | |
| reward | `object` | ✅ | [MongoTypeReward](#mongotypereward)|  |  |  | |
| date | `string` | ✅ | string|  |  |  | |
| slot_time | `string` | ✅ | Format: `date-time`|  |  |  | |
| account_is_baker | `boolean` |  | boolean|  |  |  | |
| baker_id | `integer` |  | integer|  |  |  | |


## MongoTypeBlockPerDay

Block Per Day. This type is stored in the collection `blocks_per_day`.

:Parameters:
- `_id`: the date of the day that ended
- `date`: the date of the day that ended
- `height_for_first_block`: height of the first block in the day
- `height_for_last_block`: height of the last block in the day
- `slot_time_for_first_block`: time of the first block in the day
- `slot_time_for_last_block`: time of the last block in the day
- `hash_for_first_block`: hash of the first block in the day
- `hash_for_last_block`: hash of the last block in the day

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| date | `string` | ✅ | string|  |  |  | |
| height_for_first_block | `integer` | ✅ | integer|  |  |  | |
| height_for_last_block | `integer` | ✅ | integer|  |  |  | |
| slot_time_for_first_block | `string` | ✅ | Format: `date-time`|  |  |  | |
| slot_time_for_last_block | `string` | ✅ | Format: `date-time`|  |  |  | |
| hash_for_first_block | `string` | ✅ | string|  |  |  | |
| hash_for_last_block | `string` | ✅ | string|  |  |  | |


## MongoTypeInstance

Instance. This type is stored in the collection `instances`.

:Parameters:
- `_id`: the hex string
- `module_name`: the name from the module
- `methods`: list of method names
- `contracts`: list of contract instances from this module

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| v0 | `object` |  | [CCD_InstanceInfo_V0](#ccd_instanceinfo_v0)|  |  |  | |
| v1 | `object` |  | [CCD_InstanceInfo_V1](#ccd_instanceinfo_v1)|  |  |  | |


## MongoTypeInvolvedAccount

Involved Account. This type is stored in the collections `involved_accounts_all` and
`involved_accounts_transfer`.

:Parameters:
- `_id`: the hash of the transaction
- `sender`: the sender account address
- `receiver`: the receiver account address, might be null
- `sender_canonical`: the canonical sender account address
- `receiver_canonical`: the  canonical receiver account address, might be null
- `amount`: amount of the transaction, might be null
- `type`: dict with transaction `type` and `contents`
- `block_height`: height of the block in which the transaction is executed

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| sender | `string` | ✅ | string|  |  |  | |
| sender_canonical | `string` | ✅ | string|  |  |  | |
| type | `string` | ✅ | string|  |  |  | |
| block_height | `integer` | ✅ | integer|  |  |  | |
| receiver | `string` |  | string|  |  |  | |
| receiver_canonical | `string` |  | string|  |  |  | |
| amount | `integer` |  | integer|  |  |  | |
| memo | `string` |  | string|  |  |  | |


## MongoTypeInvolvedContract

Involved Contract. This type is stored in the collection `involved_contracts`.

:Parameters:
- `_id`: the hash of the transaction - the `str` representation of the contract.
- `index`: contract index
- `subindex`: contract subindex
- `contract`: the `str` representation of the contract
- `type`: dict with transaction `type` and `contents`
- `block_height`: height of the block in which the transaction is executed
- `source_module`: hash of the source module from which this contract is instanciated.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| index | `integer` | ✅ | integer|  |  |  | |
| subindex | `integer` | ✅ | integer|  |  |  | |
| contract | `string` | ✅ | string|  |  |  | |
| type | `string` | ✅ | string|  |  |  | |
| block_height | `integer` | ✅ | integer|  |  |  | |
| source_module | `string` | ✅ | string|  |  |  | |


## MongoTypeLoggedEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| logged_event | `string` | ✅ | string|  |  |  | |
| result | `object` | ✅ | object|  |  |  | |
| tag | `integer` | ✅ | integer|  |  |  | |
| event_type | `string` | ✅ | string|  |  |  | |
| block_height | `integer` | ✅ | integer|  |  |  | |
| tx_index | `integer` | ✅ | integer|  |  |  | |
| ordering | `integer` | ✅ | integer|  |  |  | |
| tx_hash | `string` | ✅ | string|  |  |  | |
| token_address | `string` | ✅ | string|  |  |  | |
| contract | `string` | ✅ | string|  |  |  | |
| slot_time | `string` |  | Format: `date-time`|  |  |  | |
| date | `string` |  | string|  |  |  | |


## MongoTypeModule

Module. This type is stored in the collection `modules`.

:Parameters:
- `_id`: the hex string
- `module_name`: the name from the module
- `methods`: list of method names
- `contracts`: list of contract instances from this module

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| module_name | `string` | ✅ | string|  |  |  | |
| methods | `array` |  | string|  |  |  | |
| contracts | `array` |  | string|  |  |  | |
| init_date | `string` |  | Format: `date-time`|  |  |  | |


## MongoTypePayday

Payday. This type is stored in collection `paydays`.

:Parameters:
- `_id`: hash of the block that contains payday information for
this payday.
- `date`: the payday date
- `height_for_first_block`: height of the first block in the payday
- `height_for_last_block`: height of the last block in the payday
- `hash_for_first_block`: hash of the first block in the payday
- `hash_for_last_block`: hash of the last block in the payday
- `payday_duration_in_seconds`: duration of the payday in seconds (used for
APY calculation)
- `payday_block_slot_time`: time of payday reward block
- `bakers_with_delegation_information`: bakers with delegators for reward period, retrieved
from `get_delegators_for_pool_in_reward_period`, using the hash of the last block
- `baker_account_ids`: mapping from baker_id to account_address
- `pool_status_for_bakers`: dictionary, keyed on pool_status, value
is a list of bakers, retrieved using the hash of the first block

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| date | `string` | ✅ | string|  |  |  | |
| height_for_first_block | `integer` | ✅ | integer|  |  |  | |
| height_for_last_block | `integer` | ✅ | integer|  |  |  | |
| hash_for_first_block | `string` | ✅ | string|  |  |  | |
| hash_for_last_block | `string` | ✅ | string|  |  |  | |
| payday_duration_in_seconds | `number` | ✅ | number|  |  |  | |
| payday_block_slot_time | `string` | ✅ | Format: `date-time`|  |  |  | |
| bakers_with_delegation_information | `array` | ✅ | array|  |  |  | |
| baker_account_ids | `string` | ✅ | string|  |  |  | |
| pool_status_for_bakers | `array` |  | array|  |  |  | |


## MongoTypePaydayAPYIntermediate

Payday APY Intermediate. This type is stored in collection `paydays_apy_intermediate`.

:Parameters:
- `_id`: baker_is or account address

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| daily_apy_dict | `object` | ✅ | object|  |  |  | |
| d30_apy_dict | `object` |  | object|  |  |  | |
| d90_apy_dict | `object` |  | object|  |  |  | |
| d180_apy_dict | `object` |  | object|  |  |  | |


## MongoTypePaydaysPerformance

Payday Performance. This is a collection that stores daily performance characteristics
for bakers.


:Parameters:
- `_id`: unique id in the form of `date`-`baker_id`
- `expectation`: the daily expected number of blocks for this baker in this payday.
Calculated as the lottery power * 8640 (the expected number of blocks in a day)
- `payday_block_slot_time`: Slot time of the payday block
- `baker_id`: the baker_id
- `pool_status`:

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| pool_status | `object` | ✅ | [CCD_PoolInfo](#ccd_poolinfo)|  |  |  | |
| expectation | `number` | ✅ | number|  |  |  | |
| date | `string` | ✅ | string|  |  |  | |
| payday_block_slot_time | `string` | ✅ | Format: `date-time`|  |  |  | |
| baker_id | `string` | ✅ | string|  |  |  | |


## MongoTypePoolReward

Module. This type is stored in the collection `payday_rewards`.

:Parameters:
- `_id`: the hex string

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| pool_owner | `integer` | ✅ | integer and/or string|  |  |  | |
| pool_status | `object` | ✅ | object|  |  |  | |
| reward | `object` | ✅ | [MongoTypeReward](#mongotypereward)|  |  |  | |
| date | `string` | ✅ | string|  |  |  | |
| slot_time | `string` | ✅ | Format: `date-time`|  |  |  | |


## MongoTypeReward

Module. This type is stored in the collection `payday_rewards`, property `reward`.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| transaction_fees | `integer` | ✅ | integer|  |  |  | |
| baker_reward | `integer` | ✅ | integer|  |  |  | |
| finalization_reward | `integer` | ✅ | integer|  |  |  | |
| pool_owner | `integer` |  | integer and/or string|  |  |  | |
| account_id | `string` |  | string|  |  |  | |


## MongoTypeTokenAddress

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| contract | `string` | ✅ | string|  |  |  | |
| token_id | `string` | ✅ | string|  |  |  | |
| last_height_processed | `integer` | ✅ | integer|  |  |  | |
| token_amount | `string` |  | string|  |  |  | |
| metadata_url | `string` |  | string|  |  |  | |
| token_holders | `string` |  | string|  |  |  | |
| tag_information | `object` |  | [MongoTypeTokensTag](#mongotypetokenstag)|  |  |  | |
| exchange_rate | `number` |  | number|  |  |  | |
| domain_name | `string` |  | string|  |  |  | |
| token_metadata | `object` |  | [TokenMetaData](#tokenmetadata)|  |  |  | |
| failed_attempt | `object` |  | [FailedAttempt](#failedattempt)|  |  |  | |
| hidden | `boolean` |  | boolean|  |  |  | |


## MongoTypeTokenForAddress

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| token_address | `string` | ✅ | string|  |  |  | |
| contract | `string` | ✅ | string|  |  |  | |
| token_id | `string` | ✅ | string|  |  |  | |
| token_amount | `string` | ✅ | string|  |  |  | |


## MongoTypeTokenHolderAddress

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| tokens | `object` | ✅ | [MongoTypeTokenForAddress](#mongotypetokenforaddress)|  |  |  | |
| account_address_canonical | `string` |  | string|  |  |  | |


## MongoTypeTokenLink

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| account_address | `string` |  | string|  |  |  | |
| account_address_canonical | `string` |  | string|  |  |  | |
| token_holding | `object` |  | [MongoTypeTokenForAddress](#mongotypetokenforaddress)|  |  |  | |


## MongoTypeTokensTag

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| _id | `string` | ✅ | string|  |  |  | |
| contracts | `array` | ✅ | string|  |  |  | |
| tag_template | `boolean` |  | boolean|  |  |  | |
| single_use_contract | `boolean` |  | boolean|  |  |  | |
| logo_url | `string` |  | string|  |  |  | |
| decimals | `integer` |  | integer|  |  |  | |
| exchange_rate | `number` |  | number|  |  |  | |
| logged_events_count | `integer` |  | integer|  |  |  | |
| owner | `string` |  | string|  |  |  | |
| module_name | `string` |  | string|  |  |  | |
| token_type | `string` |  | string|  |  |  | |
| display_name | `string` |  | string|  |  |  | |
| tvl_for_token_in_usd | `number` |  | number|  |  |  | |


## TokenAttribute

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| type | `string` |  | string|  |  |  | |
| name | `string` |  | string|  |  |  | |
| value | `string` |  | string|  |  |  | |


## TokenMetaData

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| name | `string` |  | string|  |  |  | |
| symbol | `string` |  | string|  |  |  | |
| unique | `boolean` |  | boolean|  |  |  | |
| decimals | `integer` |  | integer|  |  |  | |
| description | `string` |  | string|  |  |  | |
| thumbnail | `object` |  | [TokenURLJSON](#tokenurljson)|  |  |  | |
| display | `object` |  | [TokenURLJSON](#tokenurljson)|  |  |  | |
| artifact | `object` |  | [TokenURLJSON](#tokenurljson)|  |  |  | |
| assets | `array` |  | [TokenMetaData](#tokenmetadata)|  |  |  | |
| attributes | `array` |  | [TokenAttribute](#tokenattribute)|  |  |  | |
| localization | `object` |  | [TokenURLJSON](#tokenurljson)|  |  |  | |


## TokenURLJSON

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| url | `string` |  | string|  |  |  | |
| hash | `string` |  | string|  |  |  | |


---

Markdown generated with [jsonschema-markdown](https://github.com/elisiariocouto/jsonschema-markdown).
