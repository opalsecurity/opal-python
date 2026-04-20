# SyncError

# SyncError Object ### Description The `SyncError` object is used to represent a sync error.  ### Usage Example List from the `GET Sync Errors` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_seen** | **datetime** | The time when this error was first seen. | 
**last_seen** | **datetime** | The time when this error was most recently seen. | 
**error_message** | **str** | The error message associated with the sync error. | 
**app_id** | **str** | The ID of the app that the error occured for. | [optional] 

## Example

```python
from opal_security.models.sync_error import SyncError

# TODO update the JSON string below
json = "{}"
# create an instance of SyncError from a JSON string
sync_error_instance = SyncError.from_json(json)
# print the JSON string representation of the object
print(SyncError.to_json())

# convert the object into a dict
sync_error_dict = sync_error_instance.to_dict()
# create an instance of SyncError from a dict
sync_error_from_dict = SyncError.from_dict(sync_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


