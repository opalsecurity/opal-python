# WebhookHmacCredential

An HMAC credential for webhook authentication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The unique identifier for the credential. | 
**secret** | **str** | The HMAC secret value. | 
**created_at** | **datetime** | When the credential was created. | 

## Example

```python
from opal_security.models.webhook_hmac_credential import WebhookHmacCredential

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookHmacCredential from a JSON string
webhook_hmac_credential_instance = WebhookHmacCredential.from_json(json)
# print the JSON string representation of the object
print(WebhookHmacCredential.to_json())

# convert the object into a dict
webhook_hmac_credential_dict = webhook_hmac_credential_instance.to_dict()
# create an instance of WebhookHmacCredential from a dict
webhook_hmac_credential_from_dict = WebhookHmacCredential.from_dict(webhook_hmac_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


