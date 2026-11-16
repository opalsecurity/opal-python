# PaladinList

# PaladinList Object ### Description A list of `Paladin` objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Paladin]**](Paladin.md) |  | 

## Example

```python
from opal_security.models.paladin_list import PaladinList

# TODO update the JSON string below
json = "{}"
# create an instance of PaladinList from a JSON string
paladin_list_instance = PaladinList.from_json(json)
# print the JSON string representation of the object
print(PaladinList.to_json())

# convert the object into a dict
paladin_list_dict = paladin_list_instance.to_dict()
# create an instance of PaladinList from a dict
paladin_list_from_dict = PaladinList.from_dict(paladin_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


