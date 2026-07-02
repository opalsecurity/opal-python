# WebhookApiKeyCredential

An API key credential for webhook authentication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The unique identifier for the credential. | 
**name** | **str** | The name of the API key. | 
**value** | **str** | The value of the API key. | 
**location** | [**WebhookApiKeyLocationEnum**](WebhookApiKeyLocationEnum.md) |  | 

## Example

```python
from opal_security.models.webhook_api_key_credential import WebhookApiKeyCredential

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookApiKeyCredential from a JSON string
webhook_api_key_credential_instance = WebhookApiKeyCredential.from_json(json)
# print the JSON string representation of the object
print(WebhookApiKeyCredential.to_json())

# convert the object into a dict
webhook_api_key_credential_dict = webhook_api_key_credential_instance.to_dict()
# create an instance of WebhookApiKeyCredential from a dict
webhook_api_key_credential_from_dict = WebhookApiKeyCredential.from_dict(webhook_api_key_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


