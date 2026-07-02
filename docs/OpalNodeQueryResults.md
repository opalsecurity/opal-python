# OpalNodeQueryResults

Paginated results of a NODE-type OpalQuery — one edge per matched entity (user, resource, or group).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**edges** | [**List[OpalQueryResultEdge]**](OpalQueryResultEdge.md) | List of matched entities. | 
**page_info** | [**PageInfo**](PageInfo.md) |  | 

## Example

```python
from opal_security.models.opal_node_query_results import OpalNodeQueryResults

# TODO update the JSON string below
json = "{}"
# create an instance of OpalNodeQueryResults from a JSON string
opal_node_query_results_instance = OpalNodeQueryResults.from_json(json)
# print the JSON string representation of the object
print(OpalNodeQueryResults.to_json())

# convert the object into a dict
opal_node_query_results_dict = opal_node_query_results_instance.to_dict()
# create an instance of OpalNodeQueryResults from a dict
opal_node_query_results_from_dict = OpalNodeQueryResults.from_dict(opal_node_query_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


