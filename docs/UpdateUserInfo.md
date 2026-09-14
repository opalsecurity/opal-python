# UpdateUserInfo

The user fields to update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manager_id** | **UUID** | The user&#39;s manager ID. Set to null to remove the manager. | [optional] 
**position** | **str** | The user&#39;s position. | [optional] 

## Example

```python
from opal_security.models.update_user_info import UpdateUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserInfo from a JSON string
update_user_info_instance = UpdateUserInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateUserInfo.to_json())

# convert the object into a dict
update_user_info_dict = update_user_info_instance.to_dict()
# create an instance of UpdateUserInfo from a dict
update_user_info_from_dict = UpdateUserInfo.from_dict(update_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


