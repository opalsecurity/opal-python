# PaginatedTokensList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**results** | [**List[Token]**](Token.md) |  | 

## Example

```python
from opal_security.models.paginated_tokens_list import PaginatedTokensList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTokensList from a JSON string
paginated_tokens_list_instance = PaginatedTokensList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTokensList.to_json())

# convert the object into a dict
paginated_tokens_list_dict = paginated_tokens_list_instance.to_dict()
# create an instance of PaginatedTokensList from a dict
paginated_tokens_list_from_dict = PaginatedTokensList.from_dict(paginated_tokens_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


