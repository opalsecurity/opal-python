# CampaignItemReview

A single reviewer's assignment and decision for a campaign item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_item_review_id** | **UUID** | The ID of the campaign item review. | 
**campaign_item_id** | **UUID** | The ID of the campaign item. | 
**reviewer_user_id** | **UUID** | The ID of the assigned reviewer. | 
**assignment_source** | [**CampaignItemReviewerAssignmentSourceEnum**](CampaignItemReviewerAssignmentSourceEnum.md) |  | 
**decision** | [**CampaignItemReviewDecisionEnum**](CampaignItemReviewDecisionEnum.md) | The reviewer&#39;s decision. Null when the reviewer has not yet submitted.  | [optional] 
**note** | **str** | Optional note from the reviewer. | [optional] 
**updated_access_level_remote_id** | **str** | Target access level remote ID when decision is CHANGE_ROLE. | [optional] 
**decided_at** | **datetime** | When the decision was finalized. | [optional] 

## Example

```python
from opal_security.models.campaign_item_review import CampaignItemReview

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignItemReview from a JSON string
campaign_item_review_instance = CampaignItemReview.from_json(json)
# print the JSON string representation of the object
print(CampaignItemReview.to_json())

# convert the object into a dict
campaign_item_review_dict = campaign_item_review_instance.to_dict()
# create an instance of CampaignItemReview from a dict
campaign_item_review_from_dict = CampaignItemReview.from_dict(campaign_item_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


