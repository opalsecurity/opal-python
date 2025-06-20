# ResourceRemoteInfoCustomConnector

Remote info for a custom connector resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_resource_id** | **str** | The id of the resource in the end system | 
**can_have_usage_events** | **bool** | A bool representing whether or not the resource can have usage data. | 

## Example

```python
from opal_security.models.resource_remote_info_custom_connector import ResourceRemoteInfoCustomConnector

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoCustomConnector from a JSON string
resource_remote_info_custom_connector_instance = ResourceRemoteInfoCustomConnector.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoCustomConnector.to_json())

# convert the object into a dict
resource_remote_info_custom_connector_dict = resource_remote_info_custom_connector_instance.to_dict()
# create an instance of ResourceRemoteInfoCustomConnector from a dict
resource_remote_info_custom_connector_from_dict = ResourceRemoteInfoCustomConnector.from_dict(resource_remote_info_custom_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


