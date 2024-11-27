# GroupRemoteInfoLdapGroup

Remote info for LDAP group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the LDAP group. | 

## Example

```python
from opal_security.models.group_remote_info_ldap_group import GroupRemoteInfoLdapGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoLdapGroup from a JSON string
group_remote_info_ldap_group_instance = GroupRemoteInfoLdapGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoLdapGroup.to_json())

# convert the object into a dict
group_remote_info_ldap_group_dict = group_remote_info_ldap_group_instance.to_dict()
# create an instance of GroupRemoteInfoLdapGroup from a dict
group_remote_info_ldap_group_from_dict = GroupRemoteInfoLdapGroup.from_dict(group_remote_info_ldap_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


