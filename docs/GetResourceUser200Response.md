# GetResourceUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceUser]**](ResourceUser.md) |  | 
**cursor** | **str** | Pagination cursor for the next page of results | [optional] 
**total_count** | **int** | Total number of results | [optional] 

## Example

```python
from opal_security.models.get_resource_user200_response import GetResourceUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceUser200Response from a JSON string
get_resource_user200_response_instance = GetResourceUser200Response.from_json(json)
# print the JSON string representation of the object
print(GetResourceUser200Response.to_json())

# convert the object into a dict
get_resource_user200_response_dict = get_resource_user200_response_instance.to_dict()
# create an instance of GetResourceUser200Response from a dict
get_resource_user200_response_from_dict = GetResourceUser200Response.from_dict(get_resource_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


