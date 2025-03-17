# PaginatedBundleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**total_count** | **int** | The total number of items in the result set. | [optional] 
**bundles** | [**List[Bundle]**](Bundle.md) |  | 

## Example

```python
from opal_security.models.paginated_bundle_list import PaginatedBundleList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBundleList from a JSON string
paginated_bundle_list_instance = PaginatedBundleList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBundleList.to_json())

# convert the object into a dict
paginated_bundle_list_dict = paginated_bundle_list_instance.to_dict()
# create an instance of PaginatedBundleList from a dict
paginated_bundle_list_from_dict = PaginatedBundleList.from_dict(paginated_bundle_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


