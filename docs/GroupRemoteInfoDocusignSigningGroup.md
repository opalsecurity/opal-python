# GroupRemoteInfoDocusignSigningGroup

Remote info for Docusign signing group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing_group_id** | **str** | The ID of the Docusign signing group. | 

## Example

```python
from opal_security.models.group_remote_info_docusign_signing_group import GroupRemoteInfoDocusignSigningGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoDocusignSigningGroup from a JSON string
group_remote_info_docusign_signing_group_instance = GroupRemoteInfoDocusignSigningGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoDocusignSigningGroup.to_json())

# convert the object into a dict
group_remote_info_docusign_signing_group_dict = group_remote_info_docusign_signing_group_instance.to_dict()
# create an instance of GroupRemoteInfoDocusignSigningGroup from a dict
group_remote_info_docusign_signing_group_from_dict = GroupRemoteInfoDocusignSigningGroup.from_dict(group_remote_info_docusign_signing_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


