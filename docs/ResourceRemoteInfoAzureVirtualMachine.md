# ResourceRemoteInfoAzureVirtualMachine

Remote info for Azure virtual machine.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ARM resource ID of the virtual machine. | 

## Example

```python
from opal_security.models.resource_remote_info_azure_virtual_machine import ResourceRemoteInfoAzureVirtualMachine

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAzureVirtualMachine from a JSON string
resource_remote_info_azure_virtual_machine_instance = ResourceRemoteInfoAzureVirtualMachine.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAzureVirtualMachine.to_json())

# convert the object into a dict
resource_remote_info_azure_virtual_machine_dict = resource_remote_info_azure_virtual_machine_instance.to_dict()
# create an instance of ResourceRemoteInfoAzureVirtualMachine from a dict
resource_remote_info_azure_virtual_machine_from_dict = ResourceRemoteInfoAzureVirtualMachine.from_dict(resource_remote_info_azure_virtual_machine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


