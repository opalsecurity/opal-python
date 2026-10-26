# CustomConnectorAppConfig

Configuration for a Custom Connector app. Does not include the signing secret; secrets are write-only and never returned by the API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | The identifier of the Custom Connector. | 
**base_url** | **str** | The base URL of the Custom Connector. | 
**tls_mode** | **bool** | Whether TLS verification is enabled for the Custom Connector. | 
**tls_ca_cert_content** | **str** | Optional PEM-encoded CA certificate content for TLS. | [optional] 
**supports_groups** | **bool** | Whether the Custom Connector supports groups. | 
**supports_nested_resources** | **bool** | Whether the Custom Connector supports nested resources. | 
**supports_nested_groups** | **bool** | Whether the Custom Connector supports nested groups. | 
**supports_event_ingestion** | **bool** | Whether the Custom Connector supports event ingestion. | 

## Example

```python
from opal_security.models.custom_connector_app_config import CustomConnectorAppConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CustomConnectorAppConfig from a JSON string
custom_connector_app_config_instance = CustomConnectorAppConfig.from_json(json)
# print the JSON string representation of the object
print(CustomConnectorAppConfig.to_json())

# convert the object into a dict
custom_connector_app_config_dict = custom_connector_app_config_instance.to_dict()
# create an instance of CustomConnectorAppConfig from a dict
custom_connector_app_config_from_dict = CustomConnectorAppConfig.from_dict(custom_connector_app_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


