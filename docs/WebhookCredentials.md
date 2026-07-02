# WebhookCredentials

Authentication credentials for a webhook connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | [**WebhookAuthTypeEnum**](WebhookAuthTypeEnum.md) |  | 
**api_key_credentials** | [**List[WebhookApiKeyCredential]**](WebhookApiKeyCredential.md) | API key credentials, present when auth_type is API_KEY. | [optional] 
**hmac_credential_1** | [**WebhookHmacCredential**](WebhookHmacCredential.md) | Primary HMAC credential, present when auth_type is HMAC. | [optional] 
**hmac_credential_2** | [**WebhookHmacCredential**](WebhookHmacCredential.md) | Secondary HMAC credential for rotation, present when auth_type is HMAC. | [optional] 

## Example

```python
from opal_security.models.webhook_credentials import WebhookCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCredentials from a JSON string
webhook_credentials_instance = WebhookCredentials.from_json(json)
# print the JSON string representation of the object
print(WebhookCredentials.to_json())

# convert the object into a dict
webhook_credentials_dict = webhook_credentials_instance.to_dict()
# create an instance of WebhookCredentials from a dict
webhook_credentials_from_dict = WebhookCredentials.from_dict(webhook_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


