# PaginatedTagsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**results** | [**List[Tag]**](Tag.md) |  | 

## Example

```python
from opal_security.models.paginated_tags_list import PaginatedTagsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTagsList from a JSON string
paginated_tags_list_instance = PaginatedTagsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTagsList.to_json())

# convert the object into a dict
paginated_tags_list_dict = paginated_tags_list_instance.to_dict()
# create an instance of PaginatedTagsList from a dict
paginated_tags_list_from_dict = PaginatedTagsList.from_dict(paginated_tags_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


