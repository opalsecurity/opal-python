# CreateTokenResponse

The created API token. `signed_token` is the secret credential and is only returned once at creation time. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | [**Token**](Token.md) |  | 
**signed_token** | **str** | The secret token string. Store this securely; it is only returned once at creation time.  | 

## Example

```python
from opal_security.models.create_token_response import CreateTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTokenResponse from a JSON string
create_token_response_instance = CreateTokenResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTokenResponse.to_json())

# convert the object into a dict
create_token_response_dict = create_token_response_instance.to_dict()
# create an instance of CreateTokenResponse from a dict
create_token_response_from_dict = CreateTokenResponse.from_dict(create_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


