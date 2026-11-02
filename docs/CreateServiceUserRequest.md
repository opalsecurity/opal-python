# CreateServiceUserRequest

Request body for `POST /service-users`. Intentionally minimal: only the two fields that uniquely identify a new service user. Role grants are a separate resource managed through `/role-assignments`, which keeps each grant independently addressable and avoids silent drift when grants are added or revoked through another code path. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name of the service user. | 
**owner_id** | **UUID** | The ID of the owner (team of record) that owns the service user. Must reference an existing owner in the caller&#39;s organization. | 

## Example

```python
from opal_security.models.create_service_user_request import CreateServiceUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServiceUserRequest from a JSON string
create_service_user_request_instance = CreateServiceUserRequest.from_json(json)
# print the JSON string representation of the object
print(CreateServiceUserRequest.to_json())

# convert the object into a dict
create_service_user_request_dict = create_service_user_request_instance.to_dict()
# create an instance of CreateServiceUserRequest from a dict
create_service_user_request_from_dict = CreateServiceUserRequest.from_dict(create_service_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


