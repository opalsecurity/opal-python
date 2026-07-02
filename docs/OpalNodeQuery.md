# OpalNodeQuery

Request body for a NODE-type OpalQuery. Returns entities (users, resources, groups) matching the given filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**query** | [**OpalNodeQueryBody**](OpalNodeQueryBody.md) |  | [optional] 
**first** | **int** | Maximum number of results to return. Defaults to 200. | [optional] 
**after** | **str** | Cursor from a previous response to fetch the next page of results. | [optional] 

## Example

```python
from opal_security.models.opal_node_query import OpalNodeQuery

# TODO update the JSON string below
json = "{}"
# create an instance of OpalNodeQuery from a JSON string
opal_node_query_instance = OpalNodeQuery.from_json(json)
# print the JSON string representation of the object
print(OpalNodeQuery.to_json())

# convert the object into a dict
opal_node_query_dict = opal_node_query_instance.to_dict()
# create an instance of OpalNodeQuery from a dict
opal_node_query_from_dict = OpalNodeQuery.from_dict(opal_node_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


