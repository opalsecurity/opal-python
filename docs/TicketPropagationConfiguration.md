# TicketPropagationConfiguration

Configuration for ticket propagation, when enabled, a ticket will be created for access changes related to the users in this resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_on_grant** | **bool** |  | 
**enabled_on_revocation** | **bool** |  | 
**ticket_provider** | [**TicketingProviderEnum**](TicketingProviderEnum.md) |  | [optional] 
**ticket_project_id** | **str** |  | [optional] 

## Example

```python
from opal_security.models.ticket_propagation_configuration import TicketPropagationConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of TicketPropagationConfiguration from a JSON string
ticket_propagation_configuration_instance = TicketPropagationConfiguration.from_json(json)
# print the JSON string representation of the object
print(TicketPropagationConfiguration.to_json())

# convert the object into a dict
ticket_propagation_configuration_dict = ticket_propagation_configuration_instance.to_dict()
# create an instance of TicketPropagationConfiguration from a dict
ticket_propagation_configuration_from_dict = TicketPropagationConfiguration.from_dict(ticket_propagation_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


