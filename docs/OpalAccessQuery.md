# OpalAccessQuery

Use an Access query to retrieve access grants between principals (users or groups) and their entitlements (resources or groups), with one result per (principal, entitlement, access level). Every access path reaching that grant is returned as metadata on the result. Uses the same filters as an Access Path query; results are paginated. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**query** | [**OpalAccessPathQueryBody**](OpalAccessPathQueryBody.md) |  | [optional] 
**first** | **int** | Maximum number of results to return. Defaults to 200. | [optional] 
**after** | **str** | Opaque cursor from a previous ACCESS response to fetch the next page of results. | [optional] 

## Example

```python
from opal_security.models.opal_access_query import OpalAccessQuery

# TODO update the JSON string below
json = "{}"
# create an instance of OpalAccessQuery from a JSON string
opal_access_query_instance = OpalAccessQuery.from_json(json)
# print the JSON string representation of the object
print(OpalAccessQuery.to_json())

# convert the object into a dict
opal_access_query_dict = opal_access_query_instance.to_dict()
# create an instance of OpalAccessQuery from a dict
opal_access_query_from_dict = OpalAccessQuery.from_dict(opal_access_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


