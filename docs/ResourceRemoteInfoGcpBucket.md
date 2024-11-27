# ResourceRemoteInfoGcpBucket

Remote info for GCP bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | The id of the bucket. | 

## Example

```python
from opal_security.models.resource_remote_info_gcp_bucket import ResourceRemoteInfoGcpBucket

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGcpBucket from a JSON string
resource_remote_info_gcp_bucket_instance = ResourceRemoteInfoGcpBucket.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGcpBucket.to_json())

# convert the object into a dict
resource_remote_info_gcp_bucket_dict = resource_remote_info_gcp_bucket_instance.to_dict()
# create an instance of ResourceRemoteInfoGcpBucket from a dict
resource_remote_info_gcp_bucket_from_dict = ResourceRemoteInfoGcpBucket.from_dict(resource_remote_info_gcp_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


