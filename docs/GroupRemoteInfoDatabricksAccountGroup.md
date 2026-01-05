# GroupRemoteInfoDatabricksAccountGroup

Remote info for Databricks account group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the Databricks account group. | 

## Example

```python
from opal_security.models.group_remote_info_databricks_account_group import GroupRemoteInfoDatabricksAccountGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoDatabricksAccountGroup from a JSON string
group_remote_info_databricks_account_group_instance = GroupRemoteInfoDatabricksAccountGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoDatabricksAccountGroup.to_json())

# convert the object into a dict
group_remote_info_databricks_account_group_dict = group_remote_info_databricks_account_group_instance.to_dict()
# create an instance of GroupRemoteInfoDatabricksAccountGroup from a dict
group_remote_info_databricks_account_group_from_dict = GroupRemoteInfoDatabricksAccountGroup.from_dict(group_remote_info_databricks_account_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


