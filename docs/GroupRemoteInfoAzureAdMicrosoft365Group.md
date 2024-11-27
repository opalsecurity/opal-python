# GroupRemoteInfoAzureAdMicrosoft365Group

Remote info for Microsoft Entra ID Microsoft 365 group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the Microsoft Entra ID Microsoft 365 group. | 

## Example

```python
from opal_security.models.group_remote_info_azure_ad_microsoft365_group import GroupRemoteInfoAzureAdMicrosoft365Group

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoAzureAdMicrosoft365Group from a JSON string
group_remote_info_azure_ad_microsoft365_group_instance = GroupRemoteInfoAzureAdMicrosoft365Group.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoAzureAdMicrosoft365Group.to_json())

# convert the object into a dict
group_remote_info_azure_ad_microsoft365_group_dict = group_remote_info_azure_ad_microsoft365_group_instance.to_dict()
# create an instance of GroupRemoteInfoAzureAdMicrosoft365Group from a dict
group_remote_info_azure_ad_microsoft365_group_from_dict = GroupRemoteInfoAzureAdMicrosoft365Group.from_dict(group_remote_info_azure_ad_microsoft365_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


