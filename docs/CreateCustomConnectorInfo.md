# CreateCustomConnectorInfo

Information needed to create a Custom Connector app.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | The identifier of the Custom Connector. | 
**base_url** | **str** | The base URL of the Custom Connector. | 
**signing_secret** | **str** | The signing secret used to authenticate requests to the Custom Connector. Write-only; never returned by the API. | 
**tls_mode** | **bool** | Whether TLS verification is enabled. Defaults to &#x60;true&#x60; when omitted. | [optional] 
**tls_ca_cert_content** | **str** | Optional PEM-encoded CA certificate content for TLS. | [optional] 
**supports_groups** | **bool** | Whether the Custom Connector supports groups. Defaults to &#x60;false&#x60;. | [optional] 
**supports_nested_resources** | **bool** | Whether the Custom Connector supports nested resources. Defaults to &#x60;false&#x60;. | [optional] 
**supports_nested_groups** | **bool** | Whether the Custom Connector supports nested groups. Defaults to &#x60;false&#x60;. | [optional] 
**supports_event_ingestion** | **bool** | Whether the Custom Connector supports event ingestion. Defaults to &#x60;false&#x60;. | [optional] 

## Example

```python
from opal_security.models.create_custom_connector_info import CreateCustomConnectorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomConnectorInfo from a JSON string
create_custom_connector_info_instance = CreateCustomConnectorInfo.from_json(json)
# print the JSON string representation of the object
print(CreateCustomConnectorInfo.to_json())

# convert the object into a dict
create_custom_connector_info_dict = create_custom_connector_info_instance.to_dict()
# create an instance of CreateCustomConnectorInfo from a dict
create_custom_connector_info_from_dict = CreateCustomConnectorInfo.from_dict(create_custom_connector_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


