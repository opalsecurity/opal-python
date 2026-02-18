# GroupRemoteInfoConnectorGroup

Remote info for Connector group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the Connector group. | 

## Example

```python
from opal_security.models.group_remote_info_connector_group import GroupRemoteInfoConnectorGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoConnectorGroup from a JSON string
group_remote_info_connector_group_instance = GroupRemoteInfoConnectorGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoConnectorGroup.to_json())

# convert the object into a dict
group_remote_info_connector_group_dict = group_remote_info_connector_group_instance.to_dict()
# create an instance of GroupRemoteInfoConnectorGroup from a dict
group_remote_info_connector_group_from_dict = GroupRemoteInfoConnectorGroup.from_dict(group_remote_info_connector_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


