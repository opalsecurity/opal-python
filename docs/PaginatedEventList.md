# PaginatedEventList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**results** | [**List[Event]**](Event.md) |  | [optional] 

## Example

```python
from opal_security.models.paginated_event_list import PaginatedEventList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEventList from a JSON string
paginated_event_list_instance = PaginatedEventList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEventList.to_json())

# convert the object into a dict
paginated_event_list_dict = paginated_event_list_instance.to_dict()
# create an instance of PaginatedEventList from a dict
paginated_event_list_from_dict = PaginatedEventList.from_dict(paginated_event_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


