# CampaignItem

A campaign review item — one direct access edge under review, matching a row on the admin Reviews tab. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_item_id** | **UUID** | The ID of the campaign item. | 
**campaign_id** | **UUID** | The ID of the parent campaign. | 
**target_type** | [**CampaignItemTargetTypeEnum**](CampaignItemTargetTypeEnum.md) |  | 
**role_assignment_id** | **UUID** | The role assignment ID this item reviews (&#x60;target_id&#x60; when &#x60;target_type&#x60; is ROLE_ASSIGNMENT).  | 
**status** | [**CampaignItemStatusEnum**](CampaignItemStatusEnum.md) |  | 
**created_at** | **datetime** | When the item was created (snapshotted into the campaign). | 
**is_target_deleted** | **bool** | True when the underlying role assignment is soft-deleted. | 
**principal_id** | **UUID** | Principal ID from the role assignment. Null if the RA is missing. | [optional] 
**principal_type** | [**EntityTypeEnum**](EntityTypeEnum.md) | Principal entity type. Null if the RA is missing. | [optional] 
**entity_id** | **UUID** | Entitlement entity ID. Null if the RA is missing. | [optional] 
**entity_type** | [**EntityTypeEnum**](EntityTypeEnum.md) | Entitlement entity type. Null if the RA is missing. | [optional] 
**access_level** | [**ResourceAccessLevel**](ResourceAccessLevel.md) | Access level on the role assignment, if any. | [optional] 
**access_level_name** | **str** | Denormalized access level name stored on the campaign item. | [optional] 
**reviews** | [**List[CampaignItemReview]**](CampaignItemReview.md) | Reviewer assignments and decisions for this item. | 
**admin_override** | [**CampaignItemAdminOverride**](CampaignItemAdminOverride.md) | Admin override, if any. | [optional] 

## Example

```python
from opal_security.models.campaign_item import CampaignItem

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignItem from a JSON string
campaign_item_instance = CampaignItem.from_json(json)
# print the JSON string representation of the object
print(CampaignItem.to_json())

# convert the object into a dict
campaign_item_dict = campaign_item_instance.to_dict()
# create an instance of CampaignItem from a dict
campaign_item_from_dict = CampaignItem.from_dict(campaign_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


