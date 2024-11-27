# ResourceRemoteInfoGcpServiceAccount

Remote info for a GCP service account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email of the service account. | 
**service_account_id** | **str** | The id of the service account. | 
**project_id** | **str** | The id of the project the service account is in. | 

## Example

```python
from opal_security.models.resource_remote_info_gcp_service_account import ResourceRemoteInfoGcpServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGcpServiceAccount from a JSON string
resource_remote_info_gcp_service_account_instance = ResourceRemoteInfoGcpServiceAccount.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGcpServiceAccount.to_json())

# convert the object into a dict
resource_remote_info_gcp_service_account_dict = resource_remote_info_gcp_service_account_instance.to_dict()
# create an instance of ResourceRemoteInfoGcpServiceAccount from a dict
resource_remote_info_gcp_service_account_from_dict = ResourceRemoteInfoGcpServiceAccount.from_dict(resource_remote_info_gcp_service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


