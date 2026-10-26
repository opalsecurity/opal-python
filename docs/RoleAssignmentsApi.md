# opal_security.RoleAssignmentsApi

All URIs are relative to *https://api.opal.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_role_assignments**](RoleAssignmentsApi.md#add_role_assignments) | **POST** /role-assignments | Add role assignments
[**list_role_assignments**](RoleAssignmentsApi.md#list_role_assignments) | **GET** /role-assignments | List role assignments


# **add_role_assignments**
> AddRoleAssignmentsResponse add_role_assignments(add_role_assignments_request)

Add role assignments

Grants one or more principals (user, group, or resource) access to one or more
entities (resource or group). The request body is batched to match the GraphQL
`addRoleAssignments` mutation, which this endpoint thin-wraps. The caller must
hold the `EDIT_ASSIGNMENTS` role permission on every entity in the batch.

Omit `access_level_remote_id` for entities that have a single default access
level. Omit `duration_minutes` (or send `0`) for an indefinite grant.

**Atomicity:** the batch is applied as a single transaction. If any entry
fails input validation, authorization, lookup, or creation, **no entries
are created** and the response identifies the first failing entry's
`entity_id` and `principal_id` (and the request-array index for input
validation errors). Clients should retry with the offending entry
removed; partial-success is intentionally not supported, matching the
semantics of the GraphQL `addRoleAssignments` mutation that this
endpoint wraps.

Prefer this endpoint for batch or programmatic use (e.g. Terraform). For a
single grant on a specific entity/principal pair, the per-pair endpoints —
`/resources/{id}/users/{id}`, `/groups/{id}/users/{id}`,
`/groups/{id}/resources/{id}`, `/groups/{id}/containing-groups`,
`/resources/{id}/non-human-identities/{id}` — are often simpler.


### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.add_role_assignments_request import AddRoleAssignmentsRequest
from opal_security.models.add_role_assignments_response import AddRoleAssignmentsResponse
from opal_security.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
import opal_security as opal

configuration = opal.Configuration(
    host = "https://api.opal.dev/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with opal_security.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opal_security.RoleAssignmentsApi(api_client)
    add_role_assignments_request = opal_security.AddRoleAssignmentsRequest() # AddRoleAssignmentsRequest | 

    try:
        # Add role assignments
        api_response = api_instance.add_role_assignments(add_role_assignments_request)
        print("The response of RoleAssignmentsApi->add_role_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentsApi->add_role_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_role_assignments_request** | [**AddRoleAssignmentsRequest**](AddRoleAssignmentsRequest.md)|  | 

### Return type

[**AddRoleAssignmentsResponse**](AddRoleAssignmentsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested role assignments were created. |  -  |
**400** | Invalid request body: unknown field, missing required field, malformed JSON, invalid enum (entity_type must be RESOURCE or GROUP; principal_type must be RESOURCE, GROUP, or USER), negative duration_minutes, or role_assignments batch size outside the allowed range.  |  -  |
**403** | Caller is not authorized to edit role assignments on one or more of the entities. |  -  |
**404** | One or more referenced entities or principals does not exist in the organization. |  -  |
**409** | One of the requested role assignments already exists. The error message identifies the offending entity_id and principal_id so a batch client can locate the colliding entry. Matches the convention of the per-pair endpoints (&#x60;/resources/{id}/users/{id}&#x60;, &#x60;/groups/{id}/users/{id}&#x60;), which also return 409 for the same condition.  |  -  |
**422** | Request was syntactically valid but could not be fulfilled. Includes group nesting cycles, self-grants, invalid durations, access-level mismatches, assignments on computed groups or non-requestable resources, and unsupported entity/principal type combinations.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_assignments**
> PaginatedRoleAssignmentsList list_role_assignments(entity_ids=entity_ids, principal_ids=principal_ids, entity_type=entity_type, principal_type=principal_type, cursor=cursor, page_size=page_size)

List role assignments

Returns a paginated list of role assignments. This endpoint is
**admin-only**: the caller's bearer token must belong to a user with the
admin or read-only admin role. Non-admin callers receive 403.

Mirrors the GraphQL `directRoleAssignments` query and shares the same
underlying code path, so pagination order, sort default
(`first_granted_at` DESC), and the set of grants returned are identical
across the two surfaces.

The REST filter surface is intentionally narrower on first ship — sort,
risk-factor filters, text search, access-scope filters, the
agents/humans toggle, and access-level filtering are deferred to a
future revision. For a single entity/principal pair, the per-pair
endpoints — `/resources/{resource_id}/users`,
`/resources/{resource_id}/groups`,
`/resources/{resource_id}/non-human-identities`,
`/groups/{group_id}/users`, `/groups/{group_id}/containing-groups` —
are often simpler.


### Example

* Bearer Authentication (BearerAuth):

```python
import opal_security
from opal_security.models.entity_type_enum import EntityTypeEnum
from opal_security.models.paginated_role_assignments_list import PaginatedRoleAssignmentsList
from opal_security.models.role_assignment_entity_type_enum import RoleAssignmentEntityTypeEnum
from opal_security.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
import opal_security as opal

configuration = opal.Configuration(
    host = "https://api.opal.dev/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with opal_security.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opal_security.RoleAssignmentsApi(api_client)
    entity_ids = None # List[UUID] | Filter to grants on these entity (resource or group) IDs. Any-match. (optional)
    principal_ids = None # List[UUID] | Filter to grants with these principal (user, group, or resource) IDs. Any-match. (optional)
    entity_type = opal_security.RoleAssignmentEntityTypeEnum() # RoleAssignmentEntityTypeEnum | Filter by entity type. Omit to include both RESOURCE and GROUP entities. (optional)
    principal_type = opal_security.EntityTypeEnum() # EntityTypeEnum | Filter by principal type. Omit to include USER, GROUP, and RESOURCE principals. (optional)
    cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)

    try:
        # List role assignments
        api_response = api_instance.list_role_assignments(entity_ids=entity_ids, principal_ids=principal_ids, entity_type=entity_type, principal_type=principal_type, cursor=cursor, page_size=page_size)
        print("The response of RoleAssignmentsApi->list_role_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentsApi->list_role_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_ids** | [**List[UUID]**](UUID.md)| Filter to grants on these entity (resource or group) IDs. Any-match. | [optional] 
 **principal_ids** | [**List[UUID]**](UUID.md)| Filter to grants with these principal (user, group, or resource) IDs. Any-match. | [optional] 
 **entity_type** | [**RoleAssignmentEntityTypeEnum**](.md)| Filter by entity type. Omit to include both RESOURCE and GROUP entities. | [optional] 
 **principal_type** | [**EntityTypeEnum**](.md)| Filter by principal type. Omit to include USER, GROUP, and RESOURCE principals. | [optional] 
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. Default is 200. | [optional] 

### Return type

[**PaginatedRoleAssignmentsList**](PaginatedRoleAssignmentsList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of role assignments. |  -  |
**400** | Invalid query parameter: unknown entity_type / principal_type enum value, malformed UUID, malformed cursor, or page_size outside the allowed range.  |  -  |
**403** | Caller is not an admin or read-only admin. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

