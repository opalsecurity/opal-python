# ResourceRemoteInfoGrafanaRole

Remote info for Grafana role(fixed or custom).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_uid** | **str** | The UID of the Grafana role. | 

## Example

```python
from opal_security.models.resource_remote_info_grafana_role import ResourceRemoteInfoGrafanaRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGrafanaRole from a JSON string
resource_remote_info_grafana_role_instance = ResourceRemoteInfoGrafanaRole.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGrafanaRole.to_json())

# convert the object into a dict
resource_remote_info_grafana_role_dict = resource_remote_info_grafana_role_instance.to_dict()
# create an instance of ResourceRemoteInfoGrafanaRole from a dict
resource_remote_info_grafana_role_from_dict = ResourceRemoteInfoGrafanaRole.from_dict(resource_remote_info_grafana_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


