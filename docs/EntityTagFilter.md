# EntityTagFilter

Filters entities by a tag key/value pair, optionally scoped to a connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The tag key to filter by. | 
**value** | **str** | The tag value to filter by. If omitted, matches any value for the given key. | [optional] 
**connection_id** | **UUID** | If specified, filters by tags associated with this connection. | [optional] 

## Example

```python
from opal_security.models.entity_tag_filter import EntityTagFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EntityTagFilter from a JSON string
entity_tag_filter_instance = EntityTagFilter.from_json(json)
# print the JSON string representation of the object
print(EntityTagFilter.to_json())

# convert the object into a dict
entity_tag_filter_dict = entity_tag_filter_instance.to_dict()
# create an instance of EntityTagFilter from a dict
entity_tag_filter_from_dict = EntityTagFilter.from_dict(entity_tag_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


