# UpdateConfigurationTemplateInfo

# UpdateConfigurationTemplateInfo Object ### Description The `ConfigurationTemplate` object is used to represent an update to a configuration template.  ### Usage Example Use in the `PUT Configuration Templates` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_template_id** | **str** | The ID of the configuration template. | 
**name** | **str** | The name of the configuration template. | [optional] 
**admin_owner_id** | **str** | The ID of the owner of the configuration template. | [optional] 
**visibility** | [**VisibilityInfo**](VisibilityInfo.md) | The visibility info of the configuration template. | [optional] 
**linked_audit_message_channel_ids** | **List[str]** | The IDs of the audit message channels linked to the configuration template. | [optional] 
**request_configurations** | [**List[RequestConfiguration]**](RequestConfiguration.md) | The request configuration list linked to the configuration template. | [optional] 
**request_configuration_list** | [**CreateRequestConfigurationInfoList**](CreateRequestConfigurationInfoList.md) | The request configuration list linked to the configuration template. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**member_oncall_schedule_ids** | **List[str]** | The IDs of the on-call schedules linked to the configuration template. | [optional] 
**break_glass_user_ids** | **List[str]** | The IDs of the break glass users linked to the configuration template. | [optional] 
**require_mfa_to_approve** | **bool** | A bool representing whether or not to require MFA for reviewers to approve requests for this configuration template. | [optional] 
**require_mfa_to_connect** | **bool** | A bool representing whether or not to require MFA to connect to resources associated with this configuration template. | [optional] 
**ticket_propagation** | [**TicketPropagationConfiguration**](TicketPropagationConfiguration.md) |  | [optional] 
**custom_request_notification** | **str** | Custom request notification sent upon request approval for this configuration template. | [optional] 

## Example

```python
from opal_security.models.update_configuration_template_info import UpdateConfigurationTemplateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConfigurationTemplateInfo from a JSON string
update_configuration_template_info_instance = UpdateConfigurationTemplateInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateConfigurationTemplateInfo.to_json())

# convert the object into a dict
update_configuration_template_info_dict = update_configuration_template_info_instance.to_dict()
# create an instance of UpdateConfigurationTemplateInfo from a dict
update_configuration_template_info_from_dict = UpdateConfigurationTemplateInfo.from_dict(update_configuration_template_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


