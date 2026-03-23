# UserIDList

A list of user IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** |  | 

## Example

```python
from opal_security.models.user_id_list import UserIDList

# TODO update the JSON string below
json = "{}"
# create an instance of UserIDList from a JSON string
user_id_list_instance = UserIDList.from_json(json)
# print the JSON string representation of the object
print(UserIDList.to_json())

# convert the object into a dict
user_id_list_dict = user_id_list_instance.to_dict()
# create an instance of UserIDList from a dict
user_id_list_from_dict = UserIDList.from_dict(user_id_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


