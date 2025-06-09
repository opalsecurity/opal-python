# RequestStage

A stage in the request review process

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage** | **int** | The stage number | 
**operator** | [**ReviewStageOperator**](ReviewStageOperator.md) | The operator to apply to reviewers in this stage | 
**reviewers** | [**List[RequestReviewer]**](RequestReviewer.md) | The reviewers for this stage | 

## Example

```python
from opal_security.models.request_stage import RequestStage

# TODO update the JSON string below
json = "{}"
# create an instance of RequestStage from a JSON string
request_stage_instance = RequestStage.from_json(json)
# print the JSON string representation of the object
print(RequestStage.to_json())

# convert the object into a dict
request_stage_dict = request_stage_instance.to_dict()
# create an instance of RequestStage from a dict
request_stage_from_dict = RequestStage.from_dict(request_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


