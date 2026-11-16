# PaladinContextSourceList

# PaladinContextSourceList Object ### Description A list of `PaladinContextSource` objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PaladinContextSource]**](PaladinContextSource.md) |  | 

## Example

```python
from opal_security.models.paladin_context_source_list import PaladinContextSourceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaladinContextSourceList from a JSON string
paladin_context_source_list_instance = PaladinContextSourceList.from_json(json)
# print the JSON string representation of the object
print(PaladinContextSourceList.to_json())

# convert the object into a dict
paladin_context_source_list_dict = paladin_context_source_list_instance.to_dict()
# create an instance of PaladinContextSourceList from a dict
paladin_context_source_list_from_dict = PaladinContextSourceList.from_dict(paladin_context_source_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


