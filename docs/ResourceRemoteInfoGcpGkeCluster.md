# ResourceRemoteInfoGcpGkeCluster

Remote info for GCP GKE cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The name of the GKE cluster. | 

## Example

```python
from opal_security.models.resource_remote_info_gcp_gke_cluster import ResourceRemoteInfoGcpGkeCluster

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGcpGkeCluster from a JSON string
resource_remote_info_gcp_gke_cluster_instance = ResourceRemoteInfoGcpGkeCluster.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGcpGkeCluster.to_json())

# convert the object into a dict
resource_remote_info_gcp_gke_cluster_dict = resource_remote_info_gcp_gke_cluster_instance.to_dict()
# create an instance of ResourceRemoteInfoGcpGkeCluster from a dict
resource_remote_info_gcp_gke_cluster_from_dict = ResourceRemoteInfoGcpGkeCluster.from_dict(resource_remote_info_gcp_gke_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


