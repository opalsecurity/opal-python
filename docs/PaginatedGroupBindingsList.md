# PaginatedGroupBindingsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**results** | [**List[GroupBinding]**](GroupBinding.md) |  | 

## Example

```python
from opal_security.models.paginated_group_bindings_list import PaginatedGroupBindingsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGroupBindingsList from a JSON string
paginated_group_bindings_list_instance = PaginatedGroupBindingsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGroupBindingsList.to_json())

# convert the object into a dict
paginated_group_bindings_list_dict = paginated_group_bindings_list_instance.to_dict()
# create an instance of PaginatedGroupBindingsList from a dict
paginated_group_bindings_list_from_dict = PaginatedGroupBindingsList.from_dict(paginated_group_bindings_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


