# MessageChannelIDList

A list of message channel IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_channel_ids** | **List[str]** |  | 

## Example

```python
from opal_security.models.message_channel_id_list import MessageChannelIDList

# TODO update the JSON string below
json = "{}"
# create an instance of MessageChannelIDList from a JSON string
message_channel_id_list_instance = MessageChannelIDList.from_json(json)
# print the JSON string representation of the object
print(MessageChannelIDList.to_json())

# convert the object into a dict
message_channel_id_list_dict = message_channel_id_list_instance.to_dict()
# create an instance of MessageChannelIDList from a dict
message_channel_id_list_from_dict = MessageChannelIDList.from_dict(message_channel_id_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


