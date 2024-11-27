# AccessList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Access]**](Access.md) |  | [optional] 

## Example

```python
from opal_security.models.access_list import AccessList

# TODO update the JSON string below
json = "{}"
# create an instance of AccessList from a JSON string
access_list_instance = AccessList.from_json(json)
# print the JSON string representation of the object
print(AccessList.to_json())

# convert the object into a dict
access_list_dict = access_list_instance.to_dict()
# create an instance of AccessList from a dict
access_list_from_dict = AccessList.from_dict(access_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


