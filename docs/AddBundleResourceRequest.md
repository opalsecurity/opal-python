# AddBundleResourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ID of the resource to add. | 
**access_level_remote_id** | **str** | The remote ID of the access level to grant to this user. Required if the resource being added requires an access level. If omitted, the default access level remote ID value (empty string) is used. | [optional] 
**access_level_name** | **str** | The name of the access level to grant to this user. If omitted, the default access level name value (empty string) is used. | [optional] 

## Example

```python
from opal_security.models.add_bundle_resource_request import AddBundleResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddBundleResourceRequest from a JSON string
add_bundle_resource_request_instance = AddBundleResourceRequest.from_json(json)
# print the JSON string representation of the object
print(AddBundleResourceRequest.to_json())

# convert the object into a dict
add_bundle_resource_request_dict = add_bundle_resource_request_instance.to_dict()
# create an instance of AddBundleResourceRequest from a dict
add_bundle_resource_request_from_dict = AddBundleResourceRequest.from_dict(add_bundle_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


