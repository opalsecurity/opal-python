# CampaignItemReviewerAssignment

Pair of campaign item and reviewer to assign or unassign.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_item_id** | **UUID** | The ID of the campaign item. | 
**reviewer_id** | **UUID** | The ID of the reviewer. Required when &#x60;assignment_source&#x60; is &#x60;MANUAL&#x60; (or omitted), and required for every unassign entry.  | [optional] 
**assignment_source** | [**CampaignItemReviewerAssignmentSourceEnum**](CampaignItemReviewerAssignmentSourceEnum.md) | Defaults to &#x60;MANUAL&#x60;. When &#x60;PRINCIPAL_MANAGER&#x60; or &#x60;ASSET_ADMIN_OWNER&#x60;, the backend resolves reviewer ID(s) and &#x60;reviewer_id&#x60; may be omitted.  | [optional] 

## Example

```python
from opal_security.models.campaign_item_reviewer_assignment import CampaignItemReviewerAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignItemReviewerAssignment from a JSON string
campaign_item_reviewer_assignment_instance = CampaignItemReviewerAssignment.from_json(json)
# print the JSON string representation of the object
print(CampaignItemReviewerAssignment.to_json())

# convert the object into a dict
campaign_item_reviewer_assignment_dict = campaign_item_reviewer_assignment_instance.to_dict()
# create an instance of CampaignItemReviewerAssignment from a dict
campaign_item_reviewer_assignment_from_dict = CampaignItemReviewerAssignment.from_dict(campaign_item_reviewer_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


