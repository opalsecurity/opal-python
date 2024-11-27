# SessionsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**results** | [**List[Session]**](Session.md) |  | [optional] 

## Example

```python
from opal_security.models.sessions_list import SessionsList

# TODO update the JSON string below
json = "{}"
# create an instance of SessionsList from a JSON string
sessions_list_instance = SessionsList.from_json(json)
# print the JSON string representation of the object
print(SessionsList.to_json())

# convert the object into a dict
sessions_list_dict = sessions_list_instance.to_dict()
# create an instance of SessionsList from a dict
sessions_list_from_dict = SessionsList.from_dict(sessions_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


