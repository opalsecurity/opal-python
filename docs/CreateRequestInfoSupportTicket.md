# CreateRequestInfoSupportTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticketing_provider** | [**TicketingProviderEnum**](TicketingProviderEnum.md) |  | 
**remote_id** | **str** |  | 
**identifier** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from opal_security.models.create_request_info_support_ticket import CreateRequestInfoSupportTicket

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRequestInfoSupportTicket from a JSON string
create_request_info_support_ticket_instance = CreateRequestInfoSupportTicket.from_json(json)
# print the JSON string representation of the object
print(CreateRequestInfoSupportTicket.to_json())

# convert the object into a dict
create_request_info_support_ticket_dict = create_request_info_support_ticket_instance.to_dict()
# create an instance of CreateRequestInfoSupportTicket from a dict
create_request_info_support_ticket_from_dict = CreateRequestInfoSupportTicket.from_dict(create_request_info_support_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


