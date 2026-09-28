# ViewerCampaignItem

A campaign review item assigned to the current viewer, matching GraphQL `ViewerCampaignItem`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_item_review_id** | **UUID** | The ID of the campaign item review. | 
**decision** | [**ViewerCampaignItemReviewDecisionEnum**](ViewerCampaignItemReviewDecisionEnum.md) | The reviewer&#39;s decision. Null when undecided. | [optional] 
**note** | **str** | Optional note from the reviewer. | [optional] 
**decided_at** | **datetime** | When the decision was finalized. | [optional] 
**pending_decision** | [**ViewerCampaignItemReviewDecisionEnum**](ViewerCampaignItemReviewDecisionEnum.md) | Pending decision staged by the viewer, if any. | [optional] 
**pending_note** | **str** | Pending note attached to the reviewer&#39;s pending decision. | [optional] 
**updated_access_level_remote_id** | **str** | Target access level remote ID when decision is CHANGE_ROLE. | [optional] 
**pending_updated_access_level_remote_id** | **str** | Pending target access level remote ID when decision is CHANGE_ROLE. | [optional] 
**reassigned_to_reviewer_ids** | **List[UUID]** | User IDs this review was reassigned to. | [optional] 
**principal_id** | **UUID** | Principal ID from the role assignment. | 
**principal_type** | [**EntityTypeEnum**](EntityTypeEnum.md) |  | 
**entity_id** | **UUID** | Entity ID from the role assignment. | 
**entity_type** | [**EntityTypeEnum**](EntityTypeEnum.md) |  | 
**access_level_name** | **str** | Denormalized access level name. | [optional] 
**access_level_remote_id** | **str** | Access level remote ID from the role assignment. | [optional] 
**granted_at** | **datetime** | When the access was originally granted. | 
**expires_at** | **datetime** | When the access expires, if set. | [optional] 
**role_assignment_id** | **UUID** | ID of the underlying role assignment. | 

## Example

```python
from opal_security.models.viewer_campaign_item import ViewerCampaignItem

# TODO update the JSON string below
json = "{}"
# create an instance of ViewerCampaignItem from a JSON string
viewer_campaign_item_instance = ViewerCampaignItem.from_json(json)
# print the JSON string representation of the object
print(ViewerCampaignItem.to_json())

# convert the object into a dict
viewer_campaign_item_dict = viewer_campaign_item_instance.to_dict()
# create an instance of ViewerCampaignItem from a dict
viewer_campaign_item_from_dict = ViewerCampaignItem.from_dict(viewer_campaign_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


