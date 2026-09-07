# CampaignConfiguration

Configuration for an access review campaign.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_id** | **UUID** | The ID of the campaign configuration. | 
**created_at** | **datetime** | The creation time of the configuration. | 
**updated_at** | **datetime** | The last updated time of the configuration. | 
**query** | [**OpalAccessPathQueryBody**](OpalAccessPathQueryBody.md) | Access-path query defining the scope of access to review. Uses the same principalFilter / entitlementFilter shape as ACCESS_PATH OpalQuery. | [optional] 
**reviewer_assignment_policy** | [**UARReviewerAssignmentPolicyEnum**](UARReviewerAssignmentPolicyEnum.md) |  | 
**allow_self_review** | **bool** | Whether reviewers can review their own access. | 
**send_reviewer_assignment_notification** | **bool** | Whether to notify reviewers upon assignment. | 
**allow_reviewer_reassignment** | **bool** | Whether reviewers may reassign their reviews to another user. | 
**start_date** | **datetime** | Scheduled start date of the campaign. | [optional] 
**end_date** | **datetime** | Scheduled end date of the campaign. | [optional] 
**timezone** | **str** | IANA timezone used to interpret campaign deadlines (e.g. America/Los_Angeles). | 
**revoke_on** | [**CampaignRevokeOnEnum**](CampaignRevokeOnEnum.md) |  | 
**reminder_schedule** | **List[int]** | Days before end date to send reminder notifications. | [optional] 
**reminder_include_manager** | **bool** | Whether to include the reviewer&#39;s manager in reminders. | 
**require_reason_on_denial** | **bool** | Whether reviewers must provide a reason when denying (revoking) access. | 
**hide_ai_suggestions** | **bool** | Whether AI suggestions are hidden from reviewers. | 
**custom_start_message** | **str** | Optional custom message included when notifying reviewers that the campaign started. | [optional] 
**group_asset_visibility_policy** | [**CampaignGroupAssetVisibilityPolicyEnum**](CampaignGroupAssetVisibilityPolicyEnum.md) |  | 
**is_template** | **bool** | Whether this configuration is a recurring schedule template. | 
**cron_expression** | **str** | Cron expression driving the recurring schedule. Null for one-off campaigns. | [optional] 
**next_scheduled_run** | **datetime** | Next time a draft will be generated from this template. | [optional] 
**last_scheduled_run** | **datetime** | Most recent time a draft was generated from this template. | [optional] 
**recurring_duration_days** | **int** | Deadline window in days applied to each draft generated from this template. | [optional] 

## Example

```python
from opal_security.models.campaign_configuration import CampaignConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignConfiguration from a JSON string
campaign_configuration_instance = CampaignConfiguration.from_json(json)
# print the JSON string representation of the object
print(CampaignConfiguration.to_json())

# convert the object into a dict
campaign_configuration_dict = campaign_configuration_instance.to_dict()
# create an instance of CampaignConfiguration from a dict
campaign_configuration_from_dict = CampaignConfiguration.from_dict(campaign_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


