# UpdateAppInfo

Information needed to update an app. Currently supports only Push-only apps (`CUSTOM`) and Custom Connector apps (`CUSTOM_CONNECTOR`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The updated name of the app. | [optional] 
**description** | **str** | The updated description of the app. | [optional] 
**admin_owner_id** | **UUID** | The updated ID of the owner of the app. | [optional] 
**visibility** | [**VisibilityTypeEnum**](VisibilityTypeEnum.md) |  | [optional] 
**visibility_group_ids** | **List[UUID]** | The IDs of groups that can see this app when visibility is &#x60;LIMITED&#x60;. | [optional] 
**import_visibility** | [**VisibilityTypeEnum**](VisibilityTypeEnum.md) |  | [optional] 
**custom_connector** | [**UpdateCustomConnectorInfo**](UpdateCustomConnectorInfo.md) | Updates Custom Connector configuration. Only valid for &#x60;CUSTOM_CONNECTOR&#x60; apps. | [optional] 

## Example

```python
from opal_security.models.update_app_info import UpdateAppInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAppInfo from a JSON string
update_app_info_instance = UpdateAppInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateAppInfo.to_json())

# convert the object into a dict
update_app_info_dict = update_app_info_instance.to_dict()
# create an instance of UpdateAppInfo from a dict
update_app_info_from_dict = UpdateAppInfo.from_dict(update_app_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


