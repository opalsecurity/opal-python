# PaginatedBundleResourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**total_count** | **int** | The total number of items in the result set. | [optional] 
**bundle_resources** | [**List[BundleResource]**](BundleResource.md) |  | 

## Example

```python
from opal_security.models.paginated_bundle_resource_list import PaginatedBundleResourceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBundleResourceList from a JSON string
paginated_bundle_resource_list_instance = PaginatedBundleResourceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBundleResourceList.to_json())

# convert the object into a dict
paginated_bundle_resource_list_dict = paginated_bundle_resource_list_instance.to_dict()
# create an instance of PaginatedBundleResourceList from a dict
paginated_bundle_resource_list_from_dict = PaginatedBundleResourceList.from_dict(paginated_bundle_resource_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


