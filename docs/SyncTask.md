# SyncTask

Represents a sync task that has been completed, either successfully or with errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The ID of the sync task. | 
**completed_at** | **datetime** | The time when the sync task was completed. | 

## Example

```python
from opal_security.models.sync_task import SyncTask

# TODO update the JSON string below
json = "{}"
# create an instance of SyncTask from a JSON string
sync_task_instance = SyncTask.from_json(json)
# print the JSON string representation of the object
print(SyncTask.to_json())

# convert the object into a dict
sync_task_dict = sync_task_instance.to_dict()
# create an instance of SyncTask from a dict
sync_task_from_dict = SyncTask.from_dict(sync_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


