# CreateTokenInfo

Information needed to create a first-party API token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_label** | **str** | A human-readable label for the token. | 
**access_level** | [**ApiAccessLevelEnum**](ApiAccessLevelEnum.md) |  | 
**user_id** | **UUID** | The ID of the user the token should authenticate as. Omit or set to the caller&#39;s ID to create a personal token. Set to a service user&#39;s ID to mint a token for that service user.  | [optional] 
**expires_at** | **datetime** | Optional expiration time for the token. | [optional] 

## Example

```python
from opal_security.models.create_token_info import CreateTokenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTokenInfo from a JSON string
create_token_info_instance = CreateTokenInfo.from_json(json)
# print the JSON string representation of the object
print(CreateTokenInfo.to_json())

# convert the object into a dict
create_token_info_dict = create_token_info_instance.to_dict()
# create an instance of CreateTokenInfo from a dict
create_token_info_from_dict = CreateTokenInfo.from_dict(create_token_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


