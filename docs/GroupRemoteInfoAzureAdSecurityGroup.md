# GroupRemoteInfoAzureAdSecurityGroup

Remote info for Microsoft Entra ID Security group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the Microsoft Entra ID Security group. | 

## Example

```python
from opal_security.models.group_remote_info_azure_ad_security_group import GroupRemoteInfoAzureAdSecurityGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoAzureAdSecurityGroup from a JSON string
group_remote_info_azure_ad_security_group_instance = GroupRemoteInfoAzureAdSecurityGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoAzureAdSecurityGroup.to_json())

# convert the object into a dict
group_remote_info_azure_ad_security_group_dict = group_remote_info_azure_ad_security_group_instance.to_dict()
# create an instance of GroupRemoteInfoAzureAdSecurityGroup from a dict
group_remote_info_azure_ad_security_group_from_dict = GroupRemoteInfoAzureAdSecurityGroup.from_dict(group_remote_info_azure_ad_security_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


