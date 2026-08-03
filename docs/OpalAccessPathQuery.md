# OpalAccessPathQuery

Request body for an ACCESS_PATH-type OpalQuery. Returns principal-to- entitlement access paths matching the given edge filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**query** | [**OpalAccessPathQueryBody**](OpalAccessPathQueryBody.md) |  | [optional] 
**first** | **int** | Maximum number of results to return. Defaults to 200. | [optional] 
**after** | **str** | Opaque cursor from a previous ACCESS_PATH response to fetch the next page of results. | [optional] 
**include_count** | **bool** | When true, populate totalCount in the response. Defaults to false. | [optional] 

## Example

```python
from opal_security.models.opal_access_path_query import OpalAccessPathQuery

# TODO update the JSON string below
json = "{}"
# create an instance of OpalAccessPathQuery from a JSON string
opal_access_path_query_instance = OpalAccessPathQuery.from_json(json)
# print the JSON string representation of the object
print(OpalAccessPathQuery.to_json())

# convert the object into a dict
opal_access_path_query_dict = opal_access_path_query_instance.to_dict()
# create an instance of OpalAccessPathQuery from a dict
opal_access_path_query_from_dict = OpalAccessPathQuery.from_dict(opal_access_path_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


