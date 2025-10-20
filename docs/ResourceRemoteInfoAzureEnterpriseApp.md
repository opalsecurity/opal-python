# ResourceRemoteInfoAzureEnterpriseApp

Remote info for Azure Enterprise App.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The remote application identifier (service principal or application object ID). | 

## Example

```python
from opal_security.models.resource_remote_info_azure_enterprise_app import ResourceRemoteInfoAzureEnterpriseApp

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAzureEnterpriseApp from a JSON string
resource_remote_info_azure_enterprise_app_instance = ResourceRemoteInfoAzureEnterpriseApp.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAzureEnterpriseApp.to_json())

# convert the object into a dict
resource_remote_info_azure_enterprise_app_dict = resource_remote_info_azure_enterprise_app_instance.to_dict()
# create an instance of ResourceRemoteInfoAzureEnterpriseApp from a dict
resource_remote_info_azure_enterprise_app_from_dict = ResourceRemoteInfoAzureEnterpriseApp.from_dict(resource_remote_info_azure_enterprise_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


