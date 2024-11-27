# ResourceAccessUserList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ResourceAccessUser]**](ResourceAccessUser.md) |  | [optional] 

## Example

```python
from opal_security.models.resource_access_user_list import ResourceAccessUserList

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAccessUserList from a JSON string
resource_access_user_list_instance = ResourceAccessUserList.from_json(json)
# print the JSON string representation of the object
print(ResourceAccessUserList.to_json())

# convert the object into a dict
resource_access_user_list_dict = resource_access_user_list_instance.to_dict()
# create an instance of ResourceAccessUserList from a dict
resource_access_user_list_from_dict = ResourceAccessUserList.from_dict(resource_access_user_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


