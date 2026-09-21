# OpalAccessQueryResults

Paginated results of an ACCESS-type OpalQuery — one edge per matched (principal, entitlement, access level) grant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**edges** | [**List[OpalAccessResultEdge]**](OpalAccessResultEdge.md) | List of matched access grants. | 
**page_info** | [**PageInfo**](PageInfo.md) |  | 

## Example

```python
from opal_security.models.opal_access_query_results import OpalAccessQueryResults

# TODO update the JSON string below
json = "{}"
# create an instance of OpalAccessQueryResults from a JSON string
opal_access_query_results_instance = OpalAccessQueryResults.from_json(json)
# print the JSON string representation of the object
print(OpalAccessQueryResults.to_json())

# convert the object into a dict
opal_access_query_results_dict = opal_access_query_results_instance.to_dict()
# create an instance of OpalAccessQueryResults from a dict
opal_access_query_results_from_dict = OpalAccessQueryResults.from_dict(opal_access_query_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


