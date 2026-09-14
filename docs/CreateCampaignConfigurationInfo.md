# CreateCampaignConfigurationInfo

Configuration to apply when creating a campaign. `query` is required; other omitted fields use defaults.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**OpalAccessPathQueryBody**](OpalAccessPathQueryBody.md) | Access-path query defining the scope of access to review. Required. Uses the same principalFilter / entitlementFilter shape as ACCESS_PATH OpalQuery. Must include at least one of principalFilter or entitlementFilter.  Campaign scope only supports direct access edges: &#x60;edgeFilter.directOnly&#x60; defaults to &#x60;true&#x60;, is always stored as &#x60;true&#x60;, and passing &#x60;false&#x60; returns 400.  | 
**reviewer_assignment_policy** | [**UARReviewerAssignmentPolicyEnum**](UARReviewerAssignmentPolicyEnum.md) |  | [optional] 
**allow_self_review** | **bool** | Whether reviewers can review their own access. | [optional] 
**send_reviewer_assignment_notification** | **bool** | Whether to notify reviewers upon assignment. | [optional] 
**allow_reviewer_reassignment** | **bool** | Whether reviewers may reassign their reviews to another user. | [optional] 
**start_date** | **datetime** | Scheduled start date of the campaign. | [optional] 
**end_date** | **datetime** | Scheduled end date of the campaign. | [optional] 
**timezone** | **str** | IANA timezone used to interpret campaign deadlines (e.g. America/Los_Angeles). | [optional] 
**revoke_on** | [**CampaignRevokeOnEnum**](CampaignRevokeOnEnum.md) |  | [optional] 
**reminder_schedule** | **List[int]** | Days before end date to send reminder notifications. | [optional] 
**reminder_include_manager** | **bool** | Whether to include the reviewer&#39;s manager in reminders. | [optional] 
**require_reason_on_denial** | **bool** | Whether reviewers must provide a reason when denying (revoking) access. | [optional] 
**hide_ai_suggestions** | **bool** | Whether AI suggestions are hidden from reviewers. | [optional] 
**custom_start_message** | **str** | Optional custom message included when notifying reviewers that the campaign started. | [optional] 
**group_asset_visibility_policy** | [**CampaignGroupAssetVisibilityPolicyEnum**](CampaignGroupAssetVisibilityPolicyEnum.md) |  | [optional] 
**is_template** | **bool** | Whether this configuration is a recurring schedule template. | [optional] 
**cron_expression** | **str** | Cron expression driving the recurring schedule. Null for one-off campaigns. | [optional] 
**recurring_duration_days** | **int** | Deadline window in days applied to each draft generated from this template. | [optional] 
**excluded_role_assignment_ids** | **List[UUID]** | Role assignment IDs to exclude from the campaign scope during population. | [optional] 

## Example

```python
from opal_security.models.create_campaign_configuration_info import CreateCampaignConfigurationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCampaignConfigurationInfo from a JSON string
create_campaign_configuration_info_instance = CreateCampaignConfigurationInfo.from_json(json)
# print the JSON string representation of the object
print(CreateCampaignConfigurationInfo.to_json())

# convert the object into a dict
create_campaign_configuration_info_dict = create_campaign_configuration_info_instance.to_dict()
# create an instance of CreateCampaignConfigurationInfo from a dict
create_campaign_configuration_info_from_dict = CreateCampaignConfigurationInfo.from_dict(create_campaign_configuration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


