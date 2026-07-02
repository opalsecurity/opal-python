# UserAttributeSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | 
**values** | **List[str]** |  | 

## Example

```python
from opal_security.models.user_attribute_selector import UserAttributeSelector

# TODO update the JSON string below
json = "{}"
# create an instance of UserAttributeSelector from a JSON string
user_attribute_selector_instance = UserAttributeSelector.from_json(json)
# print the JSON string representation of the object
print(UserAttributeSelector.to_json())

# convert the object into a dict
user_attribute_selector_dict = user_attribute_selector_instance.to_dict()
# create an instance of UserAttributeSelector from a dict
user_attribute_selector_from_dict = UserAttributeSelector.from_dict(user_attribute_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


