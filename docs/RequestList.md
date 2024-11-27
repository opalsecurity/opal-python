# RequestList

# Request List ### Description The `RequestList` object is used to represent a list of requests.  ### Usage Example Returned from the `GET Requests` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[Request]**](Request.md) | The list of requests. | [optional] 
**cursor** | **str** | The cursor to use in the next request to get the next page of results. | [optional] 

## Example

```python
from opal_security.models.request_list import RequestList

# TODO update the JSON string below
json = "{}"
# create an instance of RequestList from a JSON string
request_list_instance = RequestList.from_json(json)
# print the JSON string representation of the object
print(RequestList.to_json())

# convert the object into a dict
request_list_dict = request_list_instance.to_dict()
# create an instance of RequestList from a dict
request_list_from_dict = RequestList.from_dict(request_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


