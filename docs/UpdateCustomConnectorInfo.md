# UpdateCustomConnectorInfo

Information needed to update a Custom Connector app. Omitted fields are left unchanged. Provide `signing_secret` only when rotating the secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | The identifier of the Custom Connector. | [optional] 
**base_url** | **str** | The base URL of the Custom Connector. | [optional] 
**signing_secret** | **str** | New signing secret. Write-only; never returned by the API. Omit to leave the existing secret unchanged. | [optional] 
**tls_mode** | **bool** | Whether TLS verification is enabled for the Custom Connector. | [optional] 
**tls_ca_cert_content** | **str** | Optional PEM-encoded CA certificate content for TLS. | [optional] 
**supports_groups** | **bool** | Whether the Custom Connector supports groups. | [optional] 
**supports_nested_resources** | **bool** | Whether the Custom Connector supports nested resources. | [optional] 
**supports_nested_groups** | **bool** | Whether the Custom Connector supports nested groups. | [optional] 
**supports_event_ingestion** | **bool** | Whether the Custom Connector supports event ingestion. | [optional] 

## Example

```python
from opal_security.models.update_custom_connector_info import UpdateCustomConnectorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomConnectorInfo from a JSON string
update_custom_connector_info_instance = UpdateCustomConnectorInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomConnectorInfo.to_json())

# convert the object into a dict
update_custom_connector_info_dict = update_custom_connector_info_instance.to_dict()
# create an instance of UpdateCustomConnectorInfo from a dict
update_custom_connector_info_from_dict = UpdateCustomConnectorInfo.from_dict(update_custom_connector_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


