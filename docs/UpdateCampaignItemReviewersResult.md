# UpdateCampaignItemReviewersResult

Result of updating campaign item reviewers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviews** | [**List[CampaignItemReview]**](CampaignItemReview.md) | Full review set for every referenced item after the update. | 
**unassigned_preset_messages** | [**List[CampaignItemUnassignedPresetMessage]**](CampaignItemUnassignedPresetMessage.md) | Preset assignment messages for items that did not produce a review row. | 

## Example

```python
from opal_security.models.update_campaign_item_reviewers_result import UpdateCampaignItemReviewersResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCampaignItemReviewersResult from a JSON string
update_campaign_item_reviewers_result_instance = UpdateCampaignItemReviewersResult.from_json(json)
# print the JSON string representation of the object
print(UpdateCampaignItemReviewersResult.to_json())

# convert the object into a dict
update_campaign_item_reviewers_result_dict = update_campaign_item_reviewers_result_instance.to_dict()
# create an instance of UpdateCampaignItemReviewersResult from a dict
update_campaign_item_reviewers_result_from_dict = UpdateCampaignItemReviewersResult.from_dict(update_campaign_item_reviewers_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


