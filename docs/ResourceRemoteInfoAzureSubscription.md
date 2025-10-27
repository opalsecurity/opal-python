# ResourceRemoteInfoAzureSubscription

Remote info for Azure subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ARM resource ID of the subscription. | 

## Example

```python
from opal_security.models.resource_remote_info_azure_subscription import ResourceRemoteInfoAzureSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAzureSubscription from a JSON string
resource_remote_info_azure_subscription_instance = ResourceRemoteInfoAzureSubscription.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAzureSubscription.to_json())

# convert the object into a dict
resource_remote_info_azure_subscription_dict = resource_remote_info_azure_subscription_instance.to_dict()
# create an instance of ResourceRemoteInfoAzureSubscription from a dict
resource_remote_info_azure_subscription_from_dict = ResourceRemoteInfoAzureSubscription.from_dict(resource_remote_info_azure_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


