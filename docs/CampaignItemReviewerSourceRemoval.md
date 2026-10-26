# CampaignItemReviewerSourceRemoval

Remove all pending reviewer rows for a given assignment source on a campaign item. Completed reviews are preserved. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_item_id** | **UUID** | The ID of the campaign item. | 
**assignment_source** | [**CampaignItemReviewerAssignmentSourceEnum**](CampaignItemReviewerAssignmentSourceEnum.md) |  | 

## Example

```python
from opal_security.models.campaign_item_reviewer_source_removal import CampaignItemReviewerSourceRemoval

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignItemReviewerSourceRemoval from a JSON string
campaign_item_reviewer_source_removal_instance = CampaignItemReviewerSourceRemoval.from_json(json)
# print the JSON string representation of the object
print(CampaignItemReviewerSourceRemoval.to_json())

# convert the object into a dict
campaign_item_reviewer_source_removal_dict = campaign_item_reviewer_source_removal_instance.to_dict()
# create an instance of CampaignItemReviewerSourceRemoval from a dict
campaign_item_reviewer_source_removal_from_dict = CampaignItemReviewerSourceRemoval.from_dict(campaign_item_reviewer_source_removal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


