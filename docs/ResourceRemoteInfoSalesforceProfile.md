# ResourceRemoteInfoSalesforceProfile

Remote info for Salesforce profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** | The id of the permission set. | 
**user_license_id** | **str** | The id of the user license. | 

## Example

```python
from opal_security.models.resource_remote_info_salesforce_profile import ResourceRemoteInfoSalesforceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoSalesforceProfile from a JSON string
resource_remote_info_salesforce_profile_instance = ResourceRemoteInfoSalesforceProfile.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoSalesforceProfile.to_json())

# convert the object into a dict
resource_remote_info_salesforce_profile_dict = resource_remote_info_salesforce_profile_instance.to_dict()
# create an instance of ResourceRemoteInfoSalesforceProfile from a dict
resource_remote_info_salesforce_profile_from_dict = ResourceRemoteInfoSalesforceProfile.from_dict(resource_remote_info_salesforce_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


