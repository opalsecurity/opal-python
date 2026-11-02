# ReviewCampaignItemDecisionInfo

A single reviewer decision to submit for a campaign item review. Mirrors GraphQL `CampaignItemReviewDecisionInput`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_item_review_id** | **UUID** | The ID of the campaign item review to update. | 
**decision** | [**CampaignItemReviewDecisionEnum**](CampaignItemReviewDecisionEnum.md) |  | 
**note** | **str** | Optional note from the reviewer for this decision. | [optional] 
**access_level_remote_id** | **str** | Required when &#x60;decision&#x60; is &#x60;CHANGE_ROLE&#x60;. The remote ID of the access level to change to. Ignored for other decisions.  | [optional] 
**new_reviewer_user_ids** | **List[UUID]** | When &#x60;decision&#x60; is &#x60;REASSIGNED&#x60; and &#x60;assignment_source&#x60; is &#x60;MANUAL&#x60; or omitted, the user IDs to reassign this review to.  | [optional] 
**assignment_source** | [**CampaignItemReviewerAssignmentSourceEnum**](CampaignItemReviewerAssignmentSourceEnum.md) |  | [optional] 

## Example

```python
from opal_security.models.review_campaign_item_decision_info import ReviewCampaignItemDecisionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewCampaignItemDecisionInfo from a JSON string
review_campaign_item_decision_info_instance = ReviewCampaignItemDecisionInfo.from_json(json)
# print the JSON string representation of the object
print(ReviewCampaignItemDecisionInfo.to_json())

# convert the object into a dict
review_campaign_item_decision_info_dict = review_campaign_item_decision_info_instance.to_dict()
# create an instance of ReviewCampaignItemDecisionInfo from a dict
review_campaign_item_decision_info_from_dict = ReviewCampaignItemDecisionInfo.from_dict(review_campaign_item_decision_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


