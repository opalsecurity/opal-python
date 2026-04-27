# ResourceRemoteInfoGrafanaDashboard

Remote info for Grafana dashboard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_uid** | **str** | The UID of the Grafana dashboard. | 

## Example

```python
from opal_security.models.resource_remote_info_grafana_dashboard import ResourceRemoteInfoGrafanaDashboard

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGrafanaDashboard from a JSON string
resource_remote_info_grafana_dashboard_instance = ResourceRemoteInfoGrafanaDashboard.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGrafanaDashboard.to_json())

# convert the object into a dict
resource_remote_info_grafana_dashboard_dict = resource_remote_info_grafana_dashboard_instance.to_dict()
# create an instance of ResourceRemoteInfoGrafanaDashboard from a dict
resource_remote_info_grafana_dashboard_from_dict = ResourceRemoteInfoGrafanaDashboard.from_dict(resource_remote_info_grafana_dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


