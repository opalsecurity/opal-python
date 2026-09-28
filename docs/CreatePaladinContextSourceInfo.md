# CreatePaladinContextSourceInfo

Information for adding a context source to a Paladin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_kind** | [**PaladinContextSourceKind**](PaladinContextSourceKind.md) |  | 
**third_party_provider** | [**PaladinContextSourceProvider**](PaladinContextSourceProvider.md) |  | 
**remote_id** | **str** | The provider&#39;s identifier for the source. The Slack channel ID for a channel, or the Notion/Confluence page ID for a document. | 
**name** | **str** | An optional human-readable name for the source. | [optional] 
**url** | **str** | An optional link to the source. | [optional] 

## Example

```python
from opal_security.models.create_paladin_context_source_info import CreatePaladinContextSourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaladinContextSourceInfo from a JSON string
create_paladin_context_source_info_instance = CreatePaladinContextSourceInfo.from_json(json)
# print the JSON string representation of the object
print(CreatePaladinContextSourceInfo.to_json())

# convert the object into a dict
create_paladin_context_source_info_dict = create_paladin_context_source_info_instance.to_dict()
# create an instance of CreatePaladinContextSourceInfo from a dict
create_paladin_context_source_info_from_dict = CreatePaladinContextSourceInfo.from_dict(create_paladin_context_source_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


