# SyncErrorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_errors** | [**List[SyncError]**](SyncError.md) |  | 

## Example

```python
from opal_security.models.sync_error_list import SyncErrorList

# TODO update the JSON string below
json = "{}"
# create an instance of SyncErrorList from a JSON string
sync_error_list_instance = SyncErrorList.from_json(json)
# print the JSON string representation of the object
print(SyncErrorList.to_json())

# convert the object into a dict
sync_error_list_dict = sync_error_list_instance.to_dict()
# create an instance of SyncErrorList from a dict
sync_error_list_from_dict = SyncErrorList.from_dict(sync_error_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


