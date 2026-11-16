# ResourceConfigurationTemplate

A reference, by ID only, to the configuration template a resource is linked to. This schema does not include any of the template's own fields (name, description, request configurations, visibility, etc.) — to read or modify those, use the `/configuration-templates` endpoints with the ID carried here. A `null` `configuration_template_id` indicates that the resource is not linked to a configuration template and uses its own private configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_template_id** | **UUID** | The ID of the configuration template that the resource is linked to, or &#x60;null&#x60; if the resource is not linked to a configuration template. Only the ID is exposed here; the template&#39;s own fields are managed through the &#x60;/configuration-templates&#x60; endpoints. | 

## Example

```python
from opal_security.models.resource_configuration_template import ResourceConfigurationTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceConfigurationTemplate from a JSON string
resource_configuration_template_instance = ResourceConfigurationTemplate.from_json(json)
# print the JSON string representation of the object
print(ResourceConfigurationTemplate.to_json())

# convert the object into a dict
resource_configuration_template_dict = resource_configuration_template_instance.to_dict()
# create an instance of ResourceConfigurationTemplate from a dict
resource_configuration_template_from_dict = ResourceConfigurationTemplate.from_dict(resource_configuration_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


