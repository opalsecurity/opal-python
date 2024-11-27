# CreateOnCallScheduleInfo

# CreateOnCallScheduleInfo Object ### Description The `CreateOnCallScheduleInfo` object is used to describe the on call schedule object to be created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**third_party_provider** | [**OnCallScheduleProviderEnum**](OnCallScheduleProviderEnum.md) |  | 
**remote_id** | **str** | The remote ID of the on call schedule | 

## Example

```python
from opal_security.models.create_on_call_schedule_info import CreateOnCallScheduleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOnCallScheduleInfo from a JSON string
create_on_call_schedule_info_instance = CreateOnCallScheduleInfo.from_json(json)
# print the JSON string representation of the object
print(CreateOnCallScheduleInfo.to_json())

# convert the object into a dict
create_on_call_schedule_info_dict = create_on_call_schedule_info_instance.to_dict()
# create an instance of CreateOnCallScheduleInfo from a dict
create_on_call_schedule_info_from_dict = CreateOnCallScheduleInfo.from_dict(create_on_call_schedule_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


