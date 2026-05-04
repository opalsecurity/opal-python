# ResourceRemoteInfoGrafanaFolder

Remote info for Grafana folder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_uid** | **str** | The UID of the Grafana folder. | 

## Example

```python
from opal_security.models.resource_remote_info_grafana_folder import ResourceRemoteInfoGrafanaFolder

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGrafanaFolder from a JSON string
resource_remote_info_grafana_folder_instance = ResourceRemoteInfoGrafanaFolder.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGrafanaFolder.to_json())

# convert the object into a dict
resource_remote_info_grafana_folder_dict = resource_remote_info_grafana_folder_instance.to_dict()
# create an instance of ResourceRemoteInfoGrafanaFolder from a dict
resource_remote_info_grafana_folder_from_dict = ResourceRemoteInfoGrafanaFolder.from_dict(resource_remote_info_grafana_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


