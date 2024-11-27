# PaginatedGroupsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**results** | [**List[Group]**](Group.md) |  | 

## Example

```python
from opal_security.models.paginated_groups_list import PaginatedGroupsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGroupsList from a JSON string
paginated_groups_list_instance = PaginatedGroupsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGroupsList.to_json())

# convert the object into a dict
paginated_groups_list_dict = paginated_groups_list_instance.to_dict()
# create an instance of PaginatedGroupsList from a dict
paginated_groups_list_from_dict = PaginatedGroupsList.from_dict(paginated_groups_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


