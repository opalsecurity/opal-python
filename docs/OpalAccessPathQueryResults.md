# OpalAccessPathQueryResults

Paginated results of an ACCESS_PATH-type OpalQuery — one edge per matched principal-to-entitlement access path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**edges** | [**List[OpalAccessPathResultEdge]**](OpalAccessPathResultEdge.md) | List of matched access paths. | 
**page_info** | [**PageInfo**](PageInfo.md) |  | 
**total_count** | **int** | Exact total number of matching paths when includeCount was true on the request; otherwise null. | [optional] 

## Example

```python
from opal_security.models.opal_access_path_query_results import OpalAccessPathQueryResults

# TODO update the JSON string below
json = "{}"
# create an instance of OpalAccessPathQueryResults from a JSON string
opal_access_path_query_results_instance = OpalAccessPathQueryResults.from_json(json)
# print the JSON string representation of the object
print(OpalAccessPathQueryResults.to_json())

# convert the object into a dict
opal_access_path_query_results_dict = opal_access_path_query_results_instance.to_dict()
# create an instance of OpalAccessPathQueryResults from a dict
opal_access_path_query_results_from_dict = OpalAccessPathQueryResults.from_dict(opal_access_path_query_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


