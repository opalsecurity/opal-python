# ResourceRemoteInfoRipplingDepartment

Remote info for Rippling department.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**department_id** | **str** | The ID of the Rippling department. | 

## Example

```python
from opal_security.models.resource_remote_info_rippling_department import ResourceRemoteInfoRipplingDepartment

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoRipplingDepartment from a JSON string
resource_remote_info_rippling_department_instance = ResourceRemoteInfoRipplingDepartment.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoRipplingDepartment.to_json())

# convert the object into a dict
resource_remote_info_rippling_department_dict = resource_remote_info_rippling_department_instance.to_dict()
# create an instance of ResourceRemoteInfoRipplingDepartment from a dict
resource_remote_info_rippling_department_from_dict = ResourceRemoteInfoRipplingDepartment.from_dict(resource_remote_info_rippling_department_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


