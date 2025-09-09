# RequestReviewerStages

The stages configuration for a request item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level_name** | **str** | The name of the access level requested. | [optional] 
**access_level_remote_id** | **str** | The ID of the access level requested on the remote system. | [optional] 
**item_name** | **str** | The name of the requested item | 
**item_id** | **str** | The ID of the resource requested. | 
**stages** | [**List[RequestStage]**](RequestStage.md) | The stages of review for this request | 

## Example

```python
from opal_security.models.request_reviewer_stages import RequestReviewerStages

# TODO update the JSON string below
json = "{}"
# create an instance of RequestReviewerStages from a JSON string
request_reviewer_stages_instance = RequestReviewerStages.from_json(json)
# print the JSON string representation of the object
print(RequestReviewerStages.to_json())

# convert the object into a dict
request_reviewer_stages_dict = request_reviewer_stages_instance.to_dict()
# create an instance of RequestReviewerStages from a dict
request_reviewer_stages_from_dict = RequestReviewerStages.from_dict(request_reviewer_stages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


