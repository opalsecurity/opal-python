# UpdateCampaignConfigurationInfo

Configuration fields to update on a campaign. All fields are optional; omitted fields are left unchanged. `query` and `reviewer_assignment_policy` are set at create time and cannot be updated here; including either field returns 400. `cron_expression` and `recurring_duration_days` may only be set when the campaign is a template; setting them on a one-off campaign returns 400. `is_template` is immutable and not accepted on update. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_self_review** | **bool** | Whether reviewers can review their own access. | [optional] 
**send_reviewer_assignment_notification** | **bool** | Whether to notify reviewers upon assignment. | [optional] 
**allow_reviewer_reassignment** | **bool** | Whether reviewers may reassign their reviews to another user. | [optional] 
**start_date** | **datetime** | Scheduled start date of the campaign. May only be updated while the campaign has not started (started_at is null). When set, the date&#39;s calendar day in the campaign timezone must be at least tomorrow.  | [optional] 
**end_date** | **datetime** | Scheduled end date of the campaign. When set, the date&#39;s calendar day in the campaign timezone must be at least tomorrow.  | [optional] 
**timezone** | **str** | IANA timezone used to interpret campaign deadlines (e.g. America/Los_Angeles). | [optional] 
**revoke_on** | [**CampaignRevokeOnEnum**](CampaignRevokeOnEnum.md) |  | [optional] 
**reminder_schedule** | **List[int]** | Days before end date to send reminder notifications. | [optional] 
**reminder_include_manager** | **bool** | Whether to include the reviewer&#39;s manager in reminders. | [optional] 
**require_reason_on_denial** | **bool** | Whether reviewers must provide a reason when denying (revoking) access. | [optional] 
**hide_ai_suggestions** | **bool** | Whether AI suggestions are hidden from reviewers. | [optional] 
**custom_start_message** | **str** | Optional custom message included when notifying reviewers that the campaign started. | [optional] 
**group_asset_visibility_policy** | [**CampaignGroupAssetVisibilityPolicyEnum**](CampaignGroupAssetVisibilityPolicyEnum.md) |  | [optional] 
**cron_expression** | **str** | Cron expression driving the recurring schedule. Only valid on template campaigns. Pass an empty string to clear the active months (next_scheduled_run is cleared); the campaign remains a template. | [optional] 
**recurring_duration_days** | **int** | Deadline window in days applied to each draft generated from this template. Only valid on template campaigns. | [optional] 

## Example

```python
from opal_security.models.update_campaign_configuration_info import UpdateCampaignConfigurationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCampaignConfigurationInfo from a JSON string
update_campaign_configuration_info_instance = UpdateCampaignConfigurationInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateCampaignConfigurationInfo.to_json())

# convert the object into a dict
update_campaign_configuration_info_dict = update_campaign_configuration_info_instance.to_dict()
# create an instance of UpdateCampaignConfigurationInfo from a dict
update_campaign_configuration_info_from_dict = UpdateCampaignConfigurationInfo.from_dict(update_campaign_configuration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


