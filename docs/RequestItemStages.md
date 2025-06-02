# RequestItemStages

The stages configuration for a request item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_role_name** | **str** | The name of the requested role | [optional] 
**requested_item_name** | **str** | The name of the requested item | 
**stages** | [**List[RequestStage]**](RequestStage.md) | The stages of review for this request | 

## Example

```python
from opal_security.models.request_item_stages import RequestItemStages

# TODO update the JSON string below
json = "{}"
# create an instance of RequestItemStages from a JSON string
request_item_stages_instance = RequestItemStages.from_json(json)
# print the JSON string representation of the object
print(RequestItemStages.to_json())

# convert the object into a dict
request_item_stages_dict = request_item_stages_instance.to_dict()
# create an instance of RequestItemStages from a dict
request_item_stages_from_dict = RequestItemStages.from_dict(request_item_stages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


