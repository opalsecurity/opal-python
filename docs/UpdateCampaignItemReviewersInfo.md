# UpdateCampaignItemReviewersInfo

Input for updating campaign item reviewers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_assign** | [**List[CampaignItemReviewerAssignment]**](CampaignItemReviewerAssignment.md) | Pairs to assign. Existing pairs are ignored. | [optional] 
**to_unassign** | [**List[CampaignItemReviewerAssignment]**](CampaignItemReviewerAssignment.md) | Pairs to unassign. Only pending &#x60;MANUAL&#x60; pairs are removed; missing pairs are skipped. &#x60;reviewer_id&#x60; is required on each entry.  | [optional] 
**to_remove_sources** | [**List[CampaignItemReviewerSourceRemoval]**](CampaignItemReviewerSourceRemoval.md) | Remove all pending rows for the given assignment sources. | [optional] 

## Example

```python
from opal_security.models.update_campaign_item_reviewers_info import UpdateCampaignItemReviewersInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCampaignItemReviewersInfo from a JSON string
update_campaign_item_reviewers_info_instance = UpdateCampaignItemReviewersInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateCampaignItemReviewersInfo.to_json())

# convert the object into a dict
update_campaign_item_reviewers_info_dict = update_campaign_item_reviewers_info_instance.to_dict()
# create an instance of UpdateCampaignItemReviewersInfo from a dict
update_campaign_item_reviewers_info_from_dict = UpdateCampaignItemReviewersInfo.from_dict(update_campaign_item_reviewers_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


