# CreateConfigurationTemplateInfo

# CreateConfigurationTemplateInfo Object ### Description The `CreateConfigurationTemplateInfo` object is used to store creation info for a configuration template.  ### Usage Example Use in the `POST Configuration Templates` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_owner_id** | **str** | The ID of the owner of the configuration template. | 
**visibility** | [**VisibilityInfo**](VisibilityInfo.md) | The visibility info of the configuration template. | 
**linked_audit_message_channel_ids** | **List[str]** | The IDs of the audit message channels linked to the configuration template. | [optional] 
**member_oncall_schedule_ids** | **List[str]** | The IDs of the on-call schedules linked to the configuration template. | [optional] 
**break_glass_user_ids** | **List[str]** | The IDs of the break glass users linked to the configuration template. | [optional] 
**require_mfa_to_approve** | **bool** | A bool representing whether or not to require MFA for reviewers to approve requests for this configuration template. | 
**require_mfa_to_connect** | **bool** | A bool representing whether or not to require MFA to connect to resources associated with this configuration template. | 
**name** | **str** | The name of the configuration template. | 
**request_configurations** | [**List[RequestConfiguration]**](RequestConfiguration.md) | The request configuration list of the configuration template. If not provided, the default request configuration will be used. | [optional] 
**request_configuration_list** | [**CreateRequestConfigurationInfoList**](CreateRequestConfigurationInfoList.md) | The request configuration list of the configuration template. If not provided, the default request configuration will be used. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**ticket_propagation** | [**TicketPropagationConfiguration**](TicketPropagationConfiguration.md) |  | [optional] 
**custom_request_notification** | **str** | Custom request notification sent upon request approval for this configuration template. | [optional] 

## Example

```python
from opal_security.models.create_configuration_template_info import CreateConfigurationTemplateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConfigurationTemplateInfo from a JSON string
create_configuration_template_info_instance = CreateConfigurationTemplateInfo.from_json(json)
# print the JSON string representation of the object
print(CreateConfigurationTemplateInfo.to_json())

# convert the object into a dict
create_configuration_template_info_dict = create_configuration_template_info_instance.to_dict()
# create an instance of CreateConfigurationTemplateInfo from a dict
create_configuration_template_info_from_dict = CreateConfigurationTemplateInfo.from_dict(create_configuration_template_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


