# CreateGroupInfo

# CreateGroupInfo Object ### Description The `CreateGroupInfo` object is used to store creation info for a group.  ### Usage Example Use in the `POST Groups` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the remote group. | 
**description** | **str** | A description of the remote group. | [optional] 
**group_type** | [**GroupTypeEnum**](GroupTypeEnum.md) |  | 
**app_id** | **str** | The ID of the app for the group. | 
**remote_info** | [**GroupRemoteInfo**](GroupRemoteInfo.md) |  | [optional] 
**remote_group_id** | **str** | Deprecated - use remote_info instead. The ID of the group on the remote system. Include only for items linked to remote systems. See [this guide](https://docs.opal.dev/reference/end-system-objects) for details on how to specify this field. | [optional] 
**metadata** | **str** | Deprecated - use remote_info instead.  JSON metadata about the remote group. Include only for items linked to remote systems. See [this guide](https://docs.opal.dev/reference/end-system-objects) for details on how to specify this field. The required format is dependent on group_type and should have the following schema: &lt;style type&#x3D;\&quot;text/css\&quot;&gt; code {max-height:300px !important} &lt;/style&gt; &#x60;&#x60;&#x60;json {   \&quot;$schema\&quot;: \&quot;http://json-schema.org/draft-04/schema#\&quot;,   \&quot;title\&quot;: \&quot;Group Metadata\&quot;,   \&quot;properties\&quot;: {     \&quot;ad_group\&quot;: {       \&quot;properties\&quot;: {         \&quot;object_guid\&quot;: {           \&quot;type\&quot;: \&quot;string\&quot;         }       },       \&quot;required\&quot;: [\&quot;object_guid\&quot;],       \&quot;additionalProperties\&quot;: false,       \&quot;type\&quot;: \&quot;object\&quot;,       \&quot;title\&quot;: \&quot;Active Directory Group\&quot;     },     \&quot;duo_group\&quot;: {       \&quot;properties\&quot;: {         \&quot;group_id\&quot;: {           \&quot;type\&quot;: \&quot;string\&quot;         }       },       \&quot;required\&quot;: [\&quot;group_id\&quot;],       \&quot;additionalProperties\&quot;: false,       \&quot;type\&quot;: \&quot;object\&quot;,       \&quot;title\&quot;: \&quot;Duo Group\&quot;     },     \&quot;git_hub_team\&quot;: {       \&quot;properties\&quot;: {         \&quot;org_name\&quot;: {           \&quot;type\&quot;: \&quot;string\&quot;         },         \&quot;team_slug\&quot;: {           \&quot;type\&quot;: \&quot;string\&quot;         }       },       \&quot;required\&quot;: [\&quot;org_name\&quot;, \&quot;team_slug\&quot;],       \&quot;additionalProperties\&quot;: false,       \&quot;type\&quot;: \&quot;object\&quot;,       \&quot;title\&quot;: \&quot;GitHub Team\&quot;     },     \&quot;google_groups_group\&quot;: {       \&quot;properties\&quot;: {         \&quot;group_id\&quot;: {           \&quot;type\&quot;: \&quot;string\&quot;         }       },       \&quot;required\&quot;: [\&quot;group_id\&quot;],       \&quot;additionalProperties\&quot;: false,       \&quot;type\&quot;: \&quot;object\&quot;,       \&quot;title\&quot;: \&quot;Google Groups Group\&quot;     },     \&quot;ldap_group\&quot;: {       \&quot;properties\&quot;: {         \&quot;group_uid\&quot;: {           \&quot;type\&quot;: \&quot;string\&quot;         }       },       \&quot;required\&quot;: [\&quot;group_uid\&quot;],       \&quot;additionalProperties\&quot;: false,       \&quot;type\&quot;: \&quot;object\&quot;,       \&quot;title\&quot;: \&quot;LDAP Group\&quot;     },     \&quot;okta_directory_group\&quot;: {       \&quot;properties\&quot;: {         \&quot;group_id\&quot;: {           \&quot;type\&quot;: \&quot;string\&quot;         }       },       \&quot;required\&quot;: [\&quot;group_id\&quot;],       \&quot;additionalProperties\&quot;: false,       \&quot;type\&quot;: \&quot;object\&quot;,       \&quot;title\&quot;: \&quot;Okta Directory Group\&quot;     }   },   \&quot;additionalProperties\&quot;: false,   \&quot;minProperties\&quot;: 1,   \&quot;maxProperties\&quot;: 1,   \&quot;type\&quot;: \&quot;object\&quot; } &#x60;&#x60;&#x60; | [optional] 
**custom_request_notification** | **str** | Custom request notification sent upon request approval. | [optional] 
**risk_sensitivity_override** | [**RiskSensitivityEnum**](RiskSensitivityEnum.md) |  | [optional] 

## Example

```python
from opal_security.models.create_group_info import CreateGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupInfo from a JSON string
create_group_info_instance = CreateGroupInfo.from_json(json)
# print the JSON string representation of the object
print(CreateGroupInfo.to_json())

# convert the object into a dict
create_group_info_dict = create_group_info_instance.to_dict()
# create an instance of CreateGroupInfo from a dict
create_group_info_from_dict = CreateGroupInfo.from_dict(create_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


