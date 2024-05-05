# CISTypes

This Model is constructed only to generate documentation.

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| TokenMetaData | `object` | ✅ | [TokenMetaData](#tokenmetadata)|  |  |  | |
| StandardIdentifiers | `string` | ✅ | [StandardIdentifiers](#standardidentifiers)|  |  |  | |
| LoggedEvents | `integer` | ✅ | [LoggedEvents](#loggedevents)|  |  |  | |
| transferEvent | `object` | ✅ | [transferEvent](#transferevent)|  |  |  | |
| mintEvent | `object` | ✅ | [mintEvent](#mintevent)|  |  |  | |
| burnEvent | `object` | ✅ | [burnEvent](#burnevent)|  |  |  | |
| updateOperatorEvent | `object` | ✅ | [updateOperatorEvent](#updateoperatorevent)|  |  |  | |
| registerCredentialEvent | `object` | ✅ | [registerCredentialEvent](#registercredentialevent)|  |  |  | |
| revokeCredentialEvent | `object` | ✅ | [revokeCredentialEvent](#revokecredentialevent)|  |  |  | |
| issuerMetadataEvent | `object` | ✅ | [issuerMetadataEvent](#issuermetadataevent)|  |  |  | |
| credentialMetadataEvent | `object` | ✅ | [credentialMetadataEvent](#credentialmetadataevent)|  |  |  | |
| credentialSchemaRefEvent | `object` | ✅ | [credentialSchemaRefEvent](#credentialschemarefevent)|  |  |  | |
| revocationKeyEvent | `object` | ✅ | [revocationKeyEvent](#revocationkeyevent)|  |  |  | |
| tokenMetadataEvent | `object` | ✅ | [tokenMetadataEvent](#tokenmetadataevent)|  |  |  | |
| nonceEvent | `object` | ✅ | [nonceEvent](#nonceevent)|  |  |  | |


---

# Definitions



## LoggedEvents

No description provided for this model.

### Type: `integer`

**Possible Values:** `255` or `254` or `253` or `252` or `251` or `250` or `249` or `248` or `247` or `246` or `245` or `244` or `237` or `236`



## MetadataUrl

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| url | `string` | ✅ | string|  |  |  | |
| checksum | `string` |  | string|  |  |  | |


## SchemaRef

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| url | `string` | ✅ | string|  |  |  | |
| checksum | `string` |  | string|  |  |  | |


## StandardIdentifiers

No description provided for this model.

### Type: `string`

**Possible Values:** `CIS-0` or `CIS-1` or `CIS-2` or `CIS-3` or `CIS-4` or `CIS-5` or `CIS-6`



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


## burnEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| tag | `integer` | ✅ | integer|  |  |  | |
| token_id | `string` |  | string|  |  |  | |
| token_amount | `integer` |  | integer|  |  |  | |
| from_address | `string` |  | string|  |  |  | |


## credentialMetadataEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| tag | `integer` | ✅ | integer|  |  |  | |
| id | `string` | ✅ | string|  |  |  | |
| metadata | `object` | ✅ | [MetadataUrl](#metadataurl)|  |  |  | |


## credentialSchemaRefEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| tag | `integer` | ✅ | integer|  |  |  | |
| type | `string` |  | string|  |  |  | |
| schema_ref | `string` |  | string|  |  |  | |


## issuerMetadataEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| tag | `integer` | ✅ | integer|  |  |  | |
| metadata | `object` | ✅ | [MetadataUrl](#metadataurl)|  |  |  | |


## mintEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| tag | `integer` | ✅ | integer|  |  |  | |
| token_id | `string` |  | string|  |  |  | |
| token_amount | `integer` |  | integer|  |  |  | |
| to_address | `string` |  | string|  |  |  | |


## nonceEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| tag | `integer` | ✅ | integer|  |  |  | |
| nonce | `integer` |  | integer|  |  |  | |
| sponsoree | `string` |  | string|  |  |  | |


## registerCredentialEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| tag | `integer` | ✅ | integer|  |  |  | |
| credential_id | `string` |  | string|  |  |  | |
| schema_ref | `object` |  | [SchemaRef](#schemaref)|  |  |  | |
| credential_type | `string` |  | string|  |  |  | |


## revocationKeyEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| tag | `integer` | ✅ | integer|  |  |  | |
| action | `string` |  | string|  |  |  | |


## revokeCredentialEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| tag | `integer` | ✅ | integer|  |  |  | |
| credential_id | `string` |  | string|  |  |  | |
| revoker | `string` |  | string|  |  |  | |
| reason | `string` |  | string|  |  |  | |


## tokenMetadataEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| tag | `integer` | ✅ | integer|  |  |  | |
| token_id | `string` | ✅ | string|  |  |  | |
| metadata | `object` | ✅ | [MetadataUrl](#metadataurl)|  |  |  | |


## transferEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| tag | `integer` | ✅ | integer|  |  |  | |
| token_id | `string` |  | string|  |  |  | |
| token_amount | `integer` |  | integer|  |  |  | |
| from_address | `string` |  | string|  |  |  | |
| to_address | `string` |  | string|  |  |  | |


## updateOperatorEvent

No description provided for this model.

### Type: `object`

| Property | Type | Required | Possible Values | Deprecated | Default | Description | Examples
| -------- | ---- | -------- | --------------- | ---------- | ------- | ----------- | --------
| tag | `integer` | ✅ | integer|  |  |  | |
| operator_update | `string` |  | string|  |  |  | |
| owner | `string` |  | string|  |  |  | |
| operator | `string` |  | string|  |  |  | |


---

Markdown generated with [jsonschema-markdown](https://github.com/elisiariocouto/jsonschema-markdown).
