# RequestedItem

# Requested Item Object ### Description The `RequestedItem` object is used to represent a request target item.  ### Usage Example Returned from the `GET Requests` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ID of the resource requested. | [optional] 
**group_id** | **str** | The ID of the group requested. | [optional] 
**access_level_name** | **str** | The name of the access level requested. | [optional] 
**access_level_remote_id** | **str** | The ID of the access level requested on the remote system. | [optional] 
**name** | **str** | The name of the target. | [optional] 

## Example

```python
from opal_security.models.requested_item import RequestedItem

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItem from a JSON string
requested_item_instance = RequestedItem.from_json(json)
# print the JSON string representation of the object
print(RequestedItem.to_json())

# convert the object into a dict
requested_item_dict = requested_item_instance.to_dict()
# create an instance of RequestedItem from a dict
requested_item_from_dict = RequestedItem.from_dict(requested_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


