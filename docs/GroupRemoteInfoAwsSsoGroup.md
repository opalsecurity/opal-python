# GroupRemoteInfoAwsSsoGroup

Remote info for AWS SSO group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The id of the AWS SSO group. | 

## Example

```python
from opal_security.models.group_remote_info_aws_sso_group import GroupRemoteInfoAwsSsoGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoAwsSsoGroup from a JSON string
group_remote_info_aws_sso_group_instance = GroupRemoteInfoAwsSsoGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoAwsSsoGroup.to_json())

# convert the object into a dict
group_remote_info_aws_sso_group_dict = group_remote_info_aws_sso_group_instance.to_dict()
# create an instance of GroupRemoteInfoAwsSsoGroup from a dict
group_remote_info_aws_sso_group_from_dict = GroupRemoteInfoAwsSsoGroup.from_dict(group_remote_info_aws_sso_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


