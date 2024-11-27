# AddResourceNhiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_minutes** | **int** | The duration for which the resource can be accessed (in minutes). Use 0 to set to indefinite. | 
**access_level_remote_id** | **str** | The remote ID of the access level to grant. If omitted, the default access level remote ID value (empty string) is used. | [optional] 

## Example

```python
from opal_security.models.add_resource_nhi_request import AddResourceNhiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddResourceNhiRequest from a JSON string
add_resource_nhi_request_instance = AddResourceNhiRequest.from_json(json)
# print the JSON string representation of the object
print(AddResourceNhiRequest.to_json())

# convert the object into a dict
add_resource_nhi_request_dict = add_resource_nhi_request_instance.to_dict()
# create an instance of AddResourceNhiRequest from a dict
add_resource_nhi_request_from_dict = AddResourceNhiRequest.from_dict(add_resource_nhi_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


