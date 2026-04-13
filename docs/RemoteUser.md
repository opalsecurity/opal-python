# RemoteUser

# RemoteUser Object ### Description The `RemoteUser` object is used to represent a remote user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The ID of the user. | 
**remote_id** | **str** | The ID of the remote user. | 
**third_party_provider** | [**ThirdPartyProviderEnum**](ThirdPartyProviderEnum.md) | The third party provider of the remote user. | 

## Example

```python
from opal_security.models.remote_user import RemoteUser

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteUser from a JSON string
remote_user_instance = RemoteUser.from_json(json)
# print the JSON string representation of the object
print(RemoteUser.to_json())

# convert the object into a dict
remote_user_dict = remote_user_instance.to_dict()
# create an instance of RemoteUser from a dict
remote_user_from_dict = RemoteUser.from_dict(remote_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


