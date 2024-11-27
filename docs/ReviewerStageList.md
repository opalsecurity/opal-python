# ReviewerStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stages** | [**List[ReviewerStage]**](ReviewerStage.md) | A list of reviewer stages. | 

## Example

```python
from opal_security.models.reviewer_stage_list import ReviewerStageList

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewerStageList from a JSON string
reviewer_stage_list_instance = ReviewerStageList.from_json(json)
# print the JSON string representation of the object
print(ReviewerStageList.to_json())

# convert the object into a dict
reviewer_stage_list_dict = reviewer_stage_list_instance.to_dict()
# create an instance of ReviewerStageList from a dict
reviewer_stage_list_from_dict = ReviewerStageList.from_dict(reviewer_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


