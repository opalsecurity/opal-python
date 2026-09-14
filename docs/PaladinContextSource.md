# PaladinContextSource

# PaladinContextSource Object ### Description A context source (a Slack channel or a document) that a Paladin is configured to read during access-request review.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The ID of the context source. | 
**paladin_id** | **UUID** | The ID of the Paladin this source belongs to. | 
**source_kind** | [**PaladinContextSourceKind**](PaladinContextSourceKind.md) |  | 
**third_party_provider** | [**PaladinContextSourceProvider**](PaladinContextSourceProvider.md) |  | 
**remote_id** | **str** | The provider&#39;s identifier for the source. The Slack channel ID for a channel, or the Notion/Confluence page ID for a document. | 
**name** | **str** | A human-readable name for the source. | 
**url** | **str** | A link to the source. | 

## Example

```python
from opal_security.models.paladin_context_source import PaladinContextSource

# TODO update the JSON string below
json = "{}"
# create an instance of PaladinContextSource from a JSON string
paladin_context_source_instance = PaladinContextSource.from_json(json)
# print the JSON string representation of the object
print(PaladinContextSource.to_json())

# convert the object into a dict
paladin_context_source_dict = paladin_context_source_instance.to_dict()
# create an instance of PaladinContextSource from a dict
paladin_context_source_from_dict = PaladinContextSource.from_dict(paladin_context_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


