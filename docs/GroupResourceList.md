# GroupResourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_resources** | [**List[GroupResource]**](GroupResource.md) |  | 

## Example

```python
from opal_security.models.group_resource_list import GroupResourceList

# TODO update the JSON string below
json = "{}"
# create an instance of GroupResourceList from a JSON string
group_resource_list_instance = GroupResourceList.from_json(json)
# print the JSON string representation of the object
print(GroupResourceList.to_json())

# convert the object into a dict
group_resource_list_dict = group_resource_list_instance.to_dict()
# create an instance of GroupResourceList from a dict
group_resource_list_from_dict = GroupResourceList.from_dict(group_resource_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


