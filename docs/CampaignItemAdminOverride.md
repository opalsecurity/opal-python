# CampaignItemAdminOverride

Admin override applied to a campaign item. When set, it takes precedence over reviewer decisions for status and end-campaign remediations. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_user_id** | **UUID** | The admin who applied the override. | 
**decision** | [**CampaignItemReviewDecisionEnum**](CampaignItemReviewDecisionEnum.md) |  | 
**decided_at** | **datetime** | When the override was applied. | 

## Example

```python
from opal_security.models.campaign_item_admin_override import CampaignItemAdminOverride

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignItemAdminOverride from a JSON string
campaign_item_admin_override_instance = CampaignItemAdminOverride.from_json(json)
# print the JSON string representation of the object
print(CampaignItemAdminOverride.to_json())

# convert the object into a dict
campaign_item_admin_override_dict = campaign_item_admin_override_instance.to_dict()
# create an instance of CampaignItemAdminOverride from a dict
campaign_item_admin_override_from_dict = CampaignItemAdminOverride.from_dict(campaign_item_admin_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


