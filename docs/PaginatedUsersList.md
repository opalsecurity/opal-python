# PaginatedUsersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**results** | [**List[User]**](User.md) |  | 

## Example

```python
from opal_security.models.paginated_users_list import PaginatedUsersList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUsersList from a JSON string
paginated_users_list_instance = PaginatedUsersList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUsersList.to_json())

# convert the object into a dict
paginated_users_list_dict = paginated_users_list_instance.to_dict()
# create an instance of PaginatedUsersList from a dict
paginated_users_list_from_dict = PaginatedUsersList.from_dict(paginated_users_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


