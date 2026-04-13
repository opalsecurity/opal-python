# MessageChannel

# MessageChannel Object ### Description The `MessageChannel` object is used to represent a message channel.  ### Usage Example Update a groups message channel from the `UPDATE Groups` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_channel_id** | **str** | The ID of the message channel. | 
**third_party_provider** | [**MessageChannelProviderEnum**](MessageChannelProviderEnum.md) |  | [optional] 
**remote_id** | **str** | The remote ID of the message channel | [optional] 
**name** | **str** | The name of the message channel. | [optional] 
**is_private** | **bool** | A bool representing whether or not the message channel is private. | [optional] 

## Example

```python
from opal_security.models.message_channel import MessageChannel

# TODO update the JSON string below
json = "{}"
# create an instance of MessageChannel from a JSON string
message_channel_instance = MessageChannel.from_json(json)
# print the JSON string representation of the object
print(MessageChannel.to_json())

# convert the object into a dict
message_channel_dict = message_channel_instance.to_dict()
# create an instance of MessageChannel from a dict
message_channel_from_dict = MessageChannel.from_dict(message_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


