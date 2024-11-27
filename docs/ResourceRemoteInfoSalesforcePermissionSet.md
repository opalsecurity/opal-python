# ResourceRemoteInfoSalesforcePermissionSet

Remote info for Salesforce permission set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_set_id** | **str** | The id of the permission set. | 

## Example

```python
from opal_security.models.resource_remote_info_salesforce_permission_set import ResourceRemoteInfoSalesforcePermissionSet

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoSalesforcePermissionSet from a JSON string
resource_remote_info_salesforce_permission_set_instance = ResourceRemoteInfoSalesforcePermissionSet.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoSalesforcePermissionSet.to_json())

# convert the object into a dict
resource_remote_info_salesforce_permission_set_dict = resource_remote_info_salesforce_permission_set_instance.to_dict()
# create an instance of ResourceRemoteInfoSalesforcePermissionSet from a dict
resource_remote_info_salesforce_permission_set_from_dict = ResourceRemoteInfoSalesforcePermissionSet.from_dict(resource_remote_info_salesforce_permission_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


