# ResourceRemoteInfoAwsOrganizationalUnit

Remote info for AWS organizational unit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **str** | The id of the parent organizational unit. | [optional] 
**organizational_unit_id** | **str** | The id of the AWS organizational unit that is being created. | 

## Example

```python
from opal_security.models.resource_remote_info_aws_organizational_unit import ResourceRemoteInfoAwsOrganizationalUnit

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAwsOrganizationalUnit from a JSON string
resource_remote_info_aws_organizational_unit_instance = ResourceRemoteInfoAwsOrganizationalUnit.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAwsOrganizationalUnit.to_json())

# convert the object into a dict
resource_remote_info_aws_organizational_unit_dict = resource_remote_info_aws_organizational_unit_instance.to_dict()
# create an instance of ResourceRemoteInfoAwsOrganizationalUnit from a dict
resource_remote_info_aws_organizational_unit_from_dict = ResourceRemoteInfoAwsOrganizationalUnit.from_dict(resource_remote_info_aws_organizational_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


