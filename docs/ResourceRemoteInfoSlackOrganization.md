# ResourceRemoteInfoSlackOrganization

Remote info for Slack Enterprise Grid organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | The ID of the Slack Enterprise Grid organization (enterprise ID). | 

## Example

```python
from opal_security.models.resource_remote_info_slack_organization import ResourceRemoteInfoSlackOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoSlackOrganization from a JSON string
resource_remote_info_slack_organization_instance = ResourceRemoteInfoSlackOrganization.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoSlackOrganization.to_json())

# convert the object into a dict
resource_remote_info_slack_organization_dict = resource_remote_info_slack_organization_instance.to_dict()
# create an instance of ResourceRemoteInfoSlackOrganization from a dict
resource_remote_info_slack_organization_from_dict = ResourceRemoteInfoSlackOrganization.from_dict(resource_remote_info_slack_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


