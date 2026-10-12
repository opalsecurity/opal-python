# PaginatedRequestTemplateList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**results** | [**List[RequestTemplate]**](RequestTemplate.md) |  | [optional] 

## Example

```python
from opal_security.models.paginated_request_template_list import PaginatedRequestTemplateList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRequestTemplateList from a JSON string
paginated_request_template_list_instance = PaginatedRequestTemplateList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRequestTemplateList.to_json())

# convert the object into a dict
paginated_request_template_list_dict = paginated_request_template_list_instance.to_dict()
# create an instance of PaginatedRequestTemplateList from a dict
paginated_request_template_list_from_dict = PaginatedRequestTemplateList.from_dict(paginated_request_template_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


