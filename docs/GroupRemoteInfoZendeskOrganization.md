# GroupRemoteInfoZendeskOrganization

Remote info for Zendesk organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | The ID of the Zendesk organization. | 

## Example

```python
from opal_security.models.group_remote_info_zendesk_organization import GroupRemoteInfoZendeskOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoZendeskOrganization from a JSON string
group_remote_info_zendesk_organization_instance = GroupRemoteInfoZendeskOrganization.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoZendeskOrganization.to_json())

# convert the object into a dict
group_remote_info_zendesk_organization_dict = group_remote_info_zendesk_organization_instance.to_dict()
# create an instance of GroupRemoteInfoZendeskOrganization from a dict
group_remote_info_zendesk_organization_from_dict = GroupRemoteInfoZendeskOrganization.from_dict(group_remote_info_zendesk_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


