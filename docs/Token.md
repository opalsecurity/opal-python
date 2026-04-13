# Token

A first-party API token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The ID of the API token. | 
**created_at** | **datetime** | The date and time the token was created. | 
**token_label** | **str** | A human-readable label for the token. | 
**creator_user_id** | **str** | The ID of the user who created the token. | 
**user_id** | **str** | The ID of the user the token authenticates as. | 
**last_used_at** | **datetime** | The date and time the token was last used. | [optional] 
**access_level** | [**ApiAccessLevelEnum**](ApiAccessLevelEnum.md) |  | 
**expires_at** | **datetime** | The date and time the token expires. | [optional] 

## Example

```python
from opal_security.models.token import Token

# TODO update the JSON string below
json = "{}"
# create an instance of Token from a JSON string
token_instance = Token.from_json(json)
# print the JSON string representation of the object
print(Token.to_json())

# convert the object into a dict
token_dict = token_instance.to_dict()
# create an instance of Token from a dict
token_from_dict = Token.from_dict(token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


