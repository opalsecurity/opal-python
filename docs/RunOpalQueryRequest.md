# RunOpalQueryRequest

Request body for running an ad-hoc OpalQuery. The `type` field determines which query schema applies.

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
from opal_security.models.run_opal_query_request import RunOpalQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunOpalQueryRequest from a JSON string
run_opal_query_request_instance = RunOpalQueryRequest.from_json(json)
# print the JSON string representation of the object
print(RunOpalQueryRequest.to_json())

# convert the object into a dict
run_opal_query_request_dict = run_opal_query_request_instance.to_dict()
# create an instance of RunOpalQueryRequest from a dict
run_opal_query_request_from_dict = RunOpalQueryRequest.from_dict(run_opal_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


