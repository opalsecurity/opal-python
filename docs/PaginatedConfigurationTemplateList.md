# PaginatedConfigurationTemplateList

# PaginatedConfigurationTemplateList Object ### Description The `PaginatedConfigurationTemplateList` object is used to store a list of configuration templates.  ### Usage Example Returned from the `GET Configuration Templates` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ConfigurationTemplate]**](ConfigurationTemplate.md) |  | [optional] 

## Example

```python
from opal_security.models.paginated_configuration_template_list import PaginatedConfigurationTemplateList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedConfigurationTemplateList from a JSON string
paginated_configuration_template_list_instance = PaginatedConfigurationTemplateList.from_json(json)
# print the JSON string representation of the object
print(PaginatedConfigurationTemplateList.to_json())

# convert the object into a dict
paginated_configuration_template_list_dict = paginated_configuration_template_list_instance.to_dict()
# create an instance of PaginatedConfigurationTemplateList from a dict
paginated_configuration_template_list_from_dict = PaginatedConfigurationTemplateList.from_dict(paginated_configuration_template_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


