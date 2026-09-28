# ReviewerStageEscalation

Escalation for a reviewer stage. When set, the request advances to the reviewers named here if nobody responds within delay_minutes. Timely approval by any of the stage's own reviewers resolves the stage without escalating.  owner_ids and user_ids name only who to escalate to; the stage's own reviewers are added automatically and must not be repeated here. A stage with owner_ids [X] escalating to Y sets escalation.owner_ids to [Y], and reviewing after escalation is then open to both X and Y.  Because the stage's reviewers are unioned in rather than copied, removing someone from the stage also removes them from the escalation. At least one owner or user named here must not already be a reviewer of the stage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delay_minutes** | **int** | How long to wait for a response before escalating, in minutes. Between 1 and 1440 (24 hours). | 
**owner_ids** | **List[UUID]** | The owners to escalate to. The stage&#39;s own owner_ids are added automatically and must not be repeated here. | [optional] 
**user_ids** | **List[UUID]** | The users to escalate to. The stage&#39;s own service_user_ids are added automatically and must not be repeated here. | [optional] 

## Example

```python
from opal_security.models.reviewer_stage_escalation import ReviewerStageEscalation

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewerStageEscalation from a JSON string
reviewer_stage_escalation_instance = ReviewerStageEscalation.from_json(json)
# print the JSON string representation of the object
print(ReviewerStageEscalation.to_json())

# convert the object into a dict
reviewer_stage_escalation_dict = reviewer_stage_escalation_instance.to_dict()
# create an instance of ReviewerStageEscalation from a dict
reviewer_stage_escalation_from_dict = ReviewerStageEscalation.from_dict(reviewer_stage_escalation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


