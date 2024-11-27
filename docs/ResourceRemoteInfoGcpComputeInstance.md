# ResourceRemoteInfoGcpComputeInstance

Remote info for GCP compute instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | The id of the instance. | 
**project_id** | **str** | The id of the project the instance is in. | 
**zone** | **str** | The zone the instance is in. | 

## Example

```python
from opal_security.models.resource_remote_info_gcp_compute_instance import ResourceRemoteInfoGcpComputeInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGcpComputeInstance from a JSON string
resource_remote_info_gcp_compute_instance_instance = ResourceRemoteInfoGcpComputeInstance.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGcpComputeInstance.to_json())

# convert the object into a dict
resource_remote_info_gcp_compute_instance_dict = resource_remote_info_gcp_compute_instance_instance.to_dict()
# create an instance of ResourceRemoteInfoGcpComputeInstance from a dict
resource_remote_info_gcp_compute_instance_from_dict = ResourceRemoteInfoGcpComputeInstance.from_dict(resource_remote_info_gcp_compute_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


