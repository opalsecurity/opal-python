# ScopedRolePermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_ids** | **List[str]** | The IDs of the entities that this permission applies to. If empty of missing, the permission will have untargeted scope. | [optional] 
**target_type** | [**RolePermissionTargetTypeEnum**](RolePermissionTargetTypeEnum.md) |  | 
**permission_name** | [**RolePermissionNameEnum**](RolePermissionNameEnum.md) |  | 
**allow_all** | **bool** |  | 

## Example

```python
from opal_security.models.scoped_role_permission import ScopedRolePermission

# TODO update the JSON string below
json = "{}"
# create an instance of ScopedRolePermission from a JSON string
scoped_role_permission_instance = ScopedRolePermission.from_json(json)
# print the JSON string representation of the object
print(ScopedRolePermission.to_json())

# convert the object into a dict
scoped_role_permission_dict = scoped_role_permission_instance.to_dict()
# create an instance of ScopedRolePermission from a dict
scoped_role_permission_from_dict = ScopedRolePermission.from_dict(scoped_role_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


