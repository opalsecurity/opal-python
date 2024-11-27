# UARScope

If set, the access review will only contain resources and groups that match at least one of the filters in scope.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_visibility** | **str** | Specifies what users can see during an Access Review | [optional] 
**users** | **List[str]** | The access review will only include the following users. If any users are selected, any entity filters will be applied to only the entities that the selected users have access to. | [optional] 
**filter_operator** | **str** | Specifies whether entities must match all (AND) or any (OR) of the filters. | [optional] 
**entities** | **List[str]** | This access review will include resources and groups with ids in the given strings. | [optional] 
**apps** | **List[str]** | This access review will include items in the specified applications | [optional] 
**admins** | **List[str]** | This access review will include resources and groups who are owned by one of the owners corresponding to the given IDs. | [optional] 
**group_types** | [**List[GroupTypeEnum]**](GroupTypeEnum.md) | This access review will include items of the specified group types | [optional] 
**resource_types** | [**List[ResourceTypeEnum]**](ResourceTypeEnum.md) | This access review will include items of the specified resource types | [optional] 
**include_group_bindings** | **bool** |  | [optional] 
**tags** | [**List[TagFilter]**](TagFilter.md) | This access review will include resources and groups who are tagged with one of the given tags. | [optional] 
**names** | **List[str]** | This access review will include resources and groups whose name contains one of the given strings. | [optional] 

## Example

```python
from opal_security.models.uar_scope import UARScope

# TODO update the JSON string below
json = "{}"
# create an instance of UARScope from a JSON string
uar_scope_instance = UARScope.from_json(json)
# print the JSON string representation of the object
print(UARScope.to_json())

# convert the object into a dict
uar_scope_dict = uar_scope_instance.to_dict()
# create an instance of UARScope from a dict
uar_scope_from_dict = UARScope.from_dict(uar_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


