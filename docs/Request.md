# Request

# Request Object ### Description The `Request` object is used to represent a request.  ### Usage Example Returned from the `GET Requests` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the request. | 
**created_at** | **datetime** | The date and time the request was created. | 
**updated_at** | **datetime** | The date and time the request was last updated. | 
**requester_id** | **str** | The unique identifier of the user who created the request. | 
**target_user_id** | **str** | The unique identifier of the user who is the target of the request. | [optional] 
**target_group_id** | **str** | The unique identifier of the group who is the target of the request. | [optional] 
**status** | [**RequestStatusEnum**](RequestStatusEnum.md) | The status of the request. | 
**reason** | **str** | The reason for the request. | 
**duration_minutes** | **int** | The duration of the request in minutes. | [optional] 
**requested_items_list** | [**List[RequestedItem]**](RequestedItem.md) | The list of targets for the request. | [optional] 
**custom_fields_responses** | [**List[RequestCustomFieldResponse]**](RequestCustomFieldResponse.md) | The responses given to the custom fields associated to the request | [optional] 

## Example

```python
from opal_security.models.request import Request

# TODO update the JSON string below
json = "{}"
# create an instance of Request from a JSON string
request_instance = Request.from_json(json)
# print the JSON string representation of the object
print(Request.to_json())

# convert the object into a dict
request_dict = request_instance.to_dict()
# create an instance of Request from a dict
request_from_dict = Request.from_dict(request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


