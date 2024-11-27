# ResourceRemoteInfoAwsEc2Instance

Remote info for AWS EC2 instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | The instanceId of the EC2 instance. | 
**region** | **str** | The region of the EC2 instance. | 
**account_id** | **str** | The id of the AWS account. Required for AWS Organizations. | [optional] 

## Example

```python
from opal_security.models.resource_remote_info_aws_ec2_instance import ResourceRemoteInfoAwsEc2Instance

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoAwsEc2Instance from a JSON string
resource_remote_info_aws_ec2_instance_instance = ResourceRemoteInfoAwsEc2Instance.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoAwsEc2Instance.to_json())

# convert the object into a dict
resource_remote_info_aws_ec2_instance_dict = resource_remote_info_aws_ec2_instance_instance.to_dict()
# create an instance of ResourceRemoteInfoAwsEc2Instance from a dict
resource_remote_info_aws_ec2_instance_from_dict = ResourceRemoteInfoAwsEc2Instance.from_dict(resource_remote_info_aws_ec2_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


