# GroupRemoteInfoDocusignGroup

Remote info for Docusign group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the Docusign group. | 

## Example

```python
from opal_security.models.group_remote_info_docusign_group import GroupRemoteInfoDocusignGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoDocusignGroup from a JSON string
group_remote_info_docusign_group_instance = GroupRemoteInfoDocusignGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoDocusignGroup.to_json())

# convert the object into a dict
group_remote_info_docusign_group_dict = group_remote_info_docusign_group_instance.to_dict()
# create an instance of GroupRemoteInfoDocusignGroup from a dict
group_remote_info_docusign_group_from_dict = GroupRemoteInfoDocusignGroup.from_dict(group_remote_info_docusign_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


