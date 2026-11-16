# ResourceRemoteInfoWrikeUserType

Remote info for Wrike user type (license type).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_type_id** | **str** | The Wrike user type ID (16-char UID from GET /user_types). | 

## Example

```python
from opal_security.models.resource_remote_info_wrike_user_type import ResourceRemoteInfoWrikeUserType

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoWrikeUserType from a JSON string
resource_remote_info_wrike_user_type_instance = ResourceRemoteInfoWrikeUserType.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoWrikeUserType.to_json())

# convert the object into a dict
resource_remote_info_wrike_user_type_dict = resource_remote_info_wrike_user_type_instance.to_dict()
# create an instance of ResourceRemoteInfoWrikeUserType from a dict
resource_remote_info_wrike_user_type_from_dict = ResourceRemoteInfoWrikeUserType.from_dict(resource_remote_info_wrike_user_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


