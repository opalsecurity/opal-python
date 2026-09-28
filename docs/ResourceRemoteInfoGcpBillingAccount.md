# ResourceRemoteInfoGcpBillingAccount

Remote info for a GCP billing account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_account_id** | **str** | The resource name of the billing account. | 

## Example

```python
from opal_security.models.resource_remote_info_gcp_billing_account import ResourceRemoteInfoGcpBillingAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGcpBillingAccount from a JSON string
resource_remote_info_gcp_billing_account_instance = ResourceRemoteInfoGcpBillingAccount.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGcpBillingAccount.to_json())

# convert the object into a dict
resource_remote_info_gcp_billing_account_dict = resource_remote_info_gcp_billing_account_instance.to_dict()
# create an instance of ResourceRemoteInfoGcpBillingAccount from a dict
resource_remote_info_gcp_billing_account_from_dict = ResourceRemoteInfoGcpBillingAccount.from_dict(resource_remote_info_gcp_billing_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


