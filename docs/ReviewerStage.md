# ReviewerStage

A reviewer stage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**require_manager_approval** | **bool** | Whether this reviewer stage should require manager approval. | 
**require_admin_approval** | **bool** | Whether this reviewer stage should require admin approval. | [optional] 
**operator** | **str** | The operator of the reviewer stage. Admin and manager approval are also treated as reviewers. A stage that sets &#x60;escalation&#x60; must use &#x60;OR&#x60;; &#x60;AND&#x60; is rejected there, because the escalation timer joins the stage as an additional reviewer and would otherwise become a required approver that stalls every request until the timeout. | 
**owner_ids** | **List[UUID]** | The IDs of owners assigned as reviewers for this stage. | 
**service_user_ids** | **List[UUID]** | The IDs of service users assigned as reviewers for this stage. | [optional] 
**escalation** | [**ReviewerStageEscalation**](ReviewerStageEscalation.md) |  | [optional] 

## Example

```python
from opal_security.models.reviewer_stage import ReviewerStage

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewerStage from a JSON string
reviewer_stage_instance = ReviewerStage.from_json(json)
# print the JSON string representation of the object
print(ReviewerStage.to_json())

# convert the object into a dict
reviewer_stage_dict = reviewer_stage_instance.to_dict()
# create an instance of ReviewerStage from a dict
reviewer_stage_from_dict = ReviewerStage.from_dict(reviewer_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


