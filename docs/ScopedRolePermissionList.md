# ScopedRolePermissionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[ScopedRolePermission]**](ScopedRolePermission.md) |  | 

## Example

```python
from opal_security.models.scoped_role_permission_list import ScopedRolePermissionList

# TODO update the JSON string below
json = "{}"
# create an instance of ScopedRolePermissionList from a JSON string
scoped_role_permission_list_instance = ScopedRolePermissionList.from_json(json)
# print the JSON string representation of the object
print(ScopedRolePermissionList.to_json())

# convert the object into a dict
scoped_role_permission_list_dict = scoped_role_permission_list_instance.to_dict()
# create an instance of ScopedRolePermissionList from a dict
scoped_role_permission_list_from_dict = ScopedRolePermissionList.from_dict(scoped_role_permission_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


