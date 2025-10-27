# ResourceRemoteInfoOpenaiPlatformServiceAccount

Remote info for OpenAI Platform service account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The id of the project for the service account. | 
**service_account_id** | **str** | The id of the service account. | 

## Example

```python
from opal_security.models.resource_remote_info_openai_platform_service_account import ResourceRemoteInfoOpenaiPlatformServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoOpenaiPlatformServiceAccount from a JSON string
resource_remote_info_openai_platform_service_account_instance = ResourceRemoteInfoOpenaiPlatformServiceAccount.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoOpenaiPlatformServiceAccount.to_json())

# convert the object into a dict
resource_remote_info_openai_platform_service_account_dict = resource_remote_info_openai_platform_service_account_instance.to_dict()
# create an instance of ResourceRemoteInfoOpenaiPlatformServiceAccount from a dict
resource_remote_info_openai_platform_service_account_from_dict = ResourceRemoteInfoOpenaiPlatformServiceAccount.from_dict(resource_remote_info_openai_platform_service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


