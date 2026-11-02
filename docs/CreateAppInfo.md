# CreateAppInfo

Information needed to create an app. Currently supports only Push-only apps (`CUSTOM`) and Custom Connector apps (`CUSTOM_CONNECTOR`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the app. | 
**description** | **str** | A description of the app. | 
**admin_owner_id** | **UUID** | The ID of the owner of the app. | 
**app_type** | [**AppTypeEnum**](AppTypeEnum.md) | The type of the app. Must be &#x60;CUSTOM&#x60; (Push-only App) or &#x60;CUSTOM_CONNECTOR&#x60;. | 
**visibility** | [**VisibilityTypeEnum**](VisibilityTypeEnum.md) | The visibility of the app. Defaults to &#x60;GLOBAL&#x60; when omitted. | [optional] 
**visibility_group_ids** | **List[UUID]** | The IDs of groups that can see this app when visibility is &#x60;LIMITED&#x60;. Must be empty when visibility is &#x60;GLOBAL&#x60;; the server returns &#x60;400&#x60; otherwise. | [optional] 
**import_visibility** | [**VisibilityTypeEnum**](VisibilityTypeEnum.md) | The visibility of imported items. Defaults to &#x60;GLOBAL&#x60; when omitted. | [optional] 
**custom_connector** | [**CreateCustomConnectorInfo**](CreateCustomConnectorInfo.md) | Required when &#x60;app_type&#x60; is &#x60;CUSTOM_CONNECTOR&#x60;. Must not be set when &#x60;app_type&#x60; is &#x60;CUSTOM&#x60;. | [optional] 

## Example

```python
from opal_security.models.create_app_info import CreateAppInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppInfo from a JSON string
create_app_info_instance = CreateAppInfo.from_json(json)
# print the JSON string representation of the object
print(CreateAppInfo.to_json())

# convert the object into a dict
create_app_info_dict = create_app_info_instance.to_dict()
# create an instance of CreateAppInfo from a dict
create_app_info_from_dict = CreateAppInfo.from_dict(create_app_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


