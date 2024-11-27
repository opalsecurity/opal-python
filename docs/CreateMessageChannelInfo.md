# CreateMessageChannelInfo

# CreateMessageChannelInfo Object ### Description The `CreateMessageChannelInfo` object is used to describe the message channel object to be created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**third_party_provider** | [**MessageChannelProviderEnum**](MessageChannelProviderEnum.md) |  | 
**remote_id** | **str** | The remote ID of the message channel | 

## Example

```python
from opal_security.models.create_message_channel_info import CreateMessageChannelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMessageChannelInfo from a JSON string
create_message_channel_info_instance = CreateMessageChannelInfo.from_json(json)
# print the JSON string representation of the object
print(CreateMessageChannelInfo.to_json())

# convert the object into a dict
create_message_channel_info_dict = create_message_channel_info_instance.to_dict()
# create an instance of CreateMessageChannelInfo from a dict
create_message_channel_info_from_dict = CreateMessageChannelInfo.from_dict(create_message_channel_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


