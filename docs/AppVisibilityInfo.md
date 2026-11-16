# AppVisibilityInfo

Visibility information for an app. Mirrors `VisibilityInfo` but adds the App-specific `import_visibility`, which governs the default visibility of items imported from the app.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visibility** | [**VisibilityTypeEnum**](VisibilityTypeEnum.md) |  | 
**visibility_group_ids** | **List[UUID]** | The IDs of groups that can see this app when visibility is &#x60;LIMITED&#x60;. Must be empty when visibility is &#x60;GLOBAL&#x60;. | [optional] 
**import_visibility** | [**VisibilityTypeEnum**](VisibilityTypeEnum.md) | The visibility of items imported from this app. Defaults to &#x60;GLOBAL&#x60; when omitted on a write. | [optional] 

## Example

```python
from opal_security.models.app_visibility_info import AppVisibilityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppVisibilityInfo from a JSON string
app_visibility_info_instance = AppVisibilityInfo.from_json(json)
# print the JSON string representation of the object
print(AppVisibilityInfo.to_json())

# convert the object into a dict
app_visibility_info_dict = app_visibility_info_instance.to_dict()
# create an instance of AppVisibilityInfo from a dict
app_visibility_info_from_dict = AppVisibilityInfo.from_dict(app_visibility_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


