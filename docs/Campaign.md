# Campaign

An access review campaign.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **UUID** | The ID of the campaign. | 
**name** | **str** | The name of the campaign. | 
**status** | [**CampaignStatusEnum**](CampaignStatusEnum.md) |  | 
**is_template** | **bool** | Whether this campaign is a recurring schedule template. Templates spawn draft campaigns on schedule rather than being reviewed directly. | 
**created_at** | **datetime** | The creation time of the campaign. | 
**updated_at** | **datetime** | The last updated time of the campaign. | 
**created_by_user_id** | **UUID** | The ID of the user who created the campaign. | 
**configuration** | [**CampaignConfiguration**](CampaignConfiguration.md) | The campaign&#39;s configuration, if set. | [optional] 
**started_at** | **datetime** | The time the campaign was started, if started. | [optional] 
**started_by_user_id** | **UUID** | The ID of the user who started the campaign, if started. | [optional] 
**stopped_at** | **datetime** | The time the campaign was manually stopped, if stopped. | [optional] 
**stopped_by_user_id** | **UUID** | The ID of the user who stopped the campaign, if stopped. | [optional] 
**ended_at** | **datetime** | The time the campaign reached its scheduled end, if ended. | [optional] 
**ended_by_user_id** | **UUID** | The ID of the user who ended the campaign, if ended. | [optional] 

## Example

```python
from opal_security.models.campaign import Campaign

# TODO update the JSON string below
json = "{}"
# create an instance of Campaign from a JSON string
campaign_instance = Campaign.from_json(json)
# print the JSON string representation of the object
print(Campaign.to_json())

# convert the object into a dict
campaign_dict = campaign_instance.to_dict()
# create an instance of Campaign from a dict
campaign_from_dict = Campaign.from_dict(campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


