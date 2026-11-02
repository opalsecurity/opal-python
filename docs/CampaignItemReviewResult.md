# CampaignItemReviewResult

A campaign item review after a successful submit. Flat fields only — does not expand principal/entity relationships. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_item_review_id** | **UUID** | The ID of the campaign item review. | 
**decision** | [**CampaignItemReviewDecisionEnum**](CampaignItemReviewDecisionEnum.md) |  | [optional] 
**note** | **str** | Note recorded with the decision, if any. | [optional] 
**decided_at** | **datetime** | When the decision was submitted. | [optional] 
**updated_access_level_remote_id** | **str** | When &#x60;decision&#x60; is &#x60;CHANGE_ROLE&#x60;, the remote ID of the access level the reviewer selected.  | [optional] 
**reassigned_to_reviewer_ids** | **List[UUID]** | When &#x60;decision&#x60; is &#x60;REASSIGNED&#x60;, the user IDs the review was reassigned to.  | [optional] 

## Example

```python
from opal_security.models.campaign_item_review_result import CampaignItemReviewResult

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignItemReviewResult from a JSON string
campaign_item_review_result_instance = CampaignItemReviewResult.from_json(json)
# print the JSON string representation of the object
print(CampaignItemReviewResult.to_json())

# convert the object into a dict
campaign_item_review_result_dict = campaign_item_review_result_instance.to_dict()
# create an instance of CampaignItemReviewResult from a dict
campaign_item_review_result_from_dict = CampaignItemReviewResult.from_dict(campaign_item_review_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


