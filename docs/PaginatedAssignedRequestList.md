# PaginatedAssignedRequestList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[Request]**](Request.md) |  | 
**cursor** | **str** | The cursor to continue pagination | 

## Example

```python
from opal_security.models.paginated_assigned_request_list import PaginatedAssignedRequestList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAssignedRequestList from a JSON string
paginated_assigned_request_list_instance = PaginatedAssignedRequestList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAssignedRequestList.to_json())

# convert the object into a dict
paginated_assigned_request_list_dict = paginated_assigned_request_list_instance.to_dict()
# create an instance of PaginatedAssignedRequestList from a dict
paginated_assigned_request_list_from_dict = PaginatedAssignedRequestList.from_dict(paginated_assigned_request_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


