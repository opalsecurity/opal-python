# PaginatedUARsList

A list of UARs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**results** | [**List[UAR]**](UAR.md) |  | 

## Example

```python
from opal_security.models.paginated_uars_list import PaginatedUARsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUARsList from a JSON string
paginated_uars_list_instance = PaginatedUARsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUARsList.to_json())

# convert the object into a dict
paginated_uars_list_dict = paginated_uars_list_instance.to_dict()
# create an instance of PaginatedUARsList from a dict
paginated_uars_list_from_dict = PaginatedUARsList.from_dict(paginated_uars_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


