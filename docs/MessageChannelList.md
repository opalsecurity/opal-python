# MessageChannelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | [**List[MessageChannel]**](MessageChannel.md) |  | 

## Example

```python
from opal_security.models.message_channel_list import MessageChannelList

# TODO update the JSON string below
json = "{}"
# create an instance of MessageChannelList from a JSON string
message_channel_list_instance = MessageChannelList.from_json(json)
# print the JSON string representation of the object
print(MessageChannelList.to_json())

# convert the object into a dict
message_channel_list_dict = message_channel_list_instance.to_dict()
# create an instance of MessageChannelList from a dict
message_channel_list_from_dict = MessageChannelList.from_dict(message_channel_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


