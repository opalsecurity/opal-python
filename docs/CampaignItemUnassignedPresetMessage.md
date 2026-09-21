# CampaignItemUnassignedPresetMessage

Preset assignment feedback when no review row was created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_item_id** | **UUID** | The ID of the campaign item. | 
**assignment_source** | [**CampaignItemReviewerAssignmentSourceEnum**](CampaignItemReviewerAssignmentSourceEnum.md) |  | 
**message** | **str** | Human-readable explanation of why no reviewer was assigned. | 

## Example

```python
from opal_security.models.campaign_item_unassigned_preset_message import CampaignItemUnassignedPresetMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignItemUnassignedPresetMessage from a JSON string
campaign_item_unassigned_preset_message_instance = CampaignItemUnassignedPresetMessage.from_json(json)
# print the JSON string representation of the object
print(CampaignItemUnassignedPresetMessage.to_json())

# convert the object into a dict
campaign_item_unassigned_preset_message_dict = campaign_item_unassigned_preset_message_instance.to_dict()
# create an instance of CampaignItemUnassignedPresetMessage from a dict
campaign_item_unassigned_preset_message_from_dict = CampaignItemUnassignedPresetMessage.from_dict(campaign_item_unassigned_preset_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


