# CreateBundleInfo

# CreateBundleInfo Object ### Description The `CreateBundleInfo` object is used to store creation info for a bundle.  ### Usage Example Use in the `POST Bundles` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the bundle. | 
**description** | **str** | A brief description of the bundle. | [optional] 
**admin_owner_id** | **str** | The ID of the bundle&#39;s admin owner. | 

## Example

```python
from opal_security.models.create_bundle_info import CreateBundleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBundleInfo from a JSON string
create_bundle_info_instance = CreateBundleInfo.from_json(json)
# print the JSON string representation of the object
print(CreateBundleInfo.to_json())

# convert the object into a dict
create_bundle_info_dict = create_bundle_info_instance.to_dict()
# create an instance of CreateBundleInfo from a dict
create_bundle_info_from_dict = CreateBundleInfo.from_dict(create_bundle_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


