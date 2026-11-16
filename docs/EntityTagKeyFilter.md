# EntityTagKeyFilter

Filters entities that have a tag whose key is one of `keys`, whatever its value (including no value). Keys match exactly and case-sensitively. An empty list matches nothing. AGENT entities carry no tags, so they never match; under `not`, every agent matches, as with entityTag. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** | The tag keys to match. | 

## Example

```python
from opal_security.models.entity_tag_key_filter import EntityTagKeyFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EntityTagKeyFilter from a JSON string
entity_tag_key_filter_instance = EntityTagKeyFilter.from_json(json)
# print the JSON string representation of the object
print(EntityTagKeyFilter.to_json())

# convert the object into a dict
entity_tag_key_filter_dict = entity_tag_key_filter_instance.to_dict()
# create an instance of EntityTagKeyFilter from a dict
entity_tag_key_filter_from_dict = EntityTagKeyFilter.from_dict(entity_tag_key_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


