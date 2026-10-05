# GroupRemoteInfoConfluenceGroup

Remote info for Confluence group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the Confluence group. | 

## Example

```python
from opal_security.models.group_remote_info_confluence_group import GroupRemoteInfoConfluenceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoConfluenceGroup from a JSON string
group_remote_info_confluence_group_instance = GroupRemoteInfoConfluenceGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoConfluenceGroup.to_json())

# convert the object into a dict
group_remote_info_confluence_group_dict = group_remote_info_confluence_group_instance.to_dict()
# create an instance of GroupRemoteInfoConfluenceGroup from a dict
group_remote_info_confluence_group_from_dict = GroupRemoteInfoConfluenceGroup.from_dict(group_remote_info_confluence_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


