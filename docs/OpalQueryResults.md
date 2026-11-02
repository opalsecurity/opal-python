# OpalQueryResults

Paginated results of an OpalQuery. The `type` field discriminates which result schema applies and mirrors the `type` field on the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**edges** | [**List[OpalAccessResultEdge]**](OpalAccessResultEdge.md) | List of matched access grants. | 
**page_info** | [**PageInfo**](PageInfo.md) |  | 

## Example

```python
from opal_security.models.opal_query_results import OpalQueryResults

# TODO update the JSON string below
json = "{}"
# create an instance of OpalQueryResults from a JSON string
opal_query_results_instance = OpalQueryResults.from_json(json)
# print the JSON string representation of the object
print(OpalQueryResults.to_json())

# convert the object into a dict
opal_query_results_dict = opal_query_results_instance.to_dict()
# create an instance of OpalQueryResults from a dict
opal_query_results_from_dict = OpalQueryResults.from_dict(opal_query_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


