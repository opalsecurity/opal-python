# AccessEntityFilters

Filters for matching entities by type, name, tag, IDs, connections, or access levels. Supports recursive logical composition via allOf/anyOf.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_types** | **List[str]** | Filter by entity type. Only RESOURCE, GROUP, and USER are queryable via OpalQuery. | [optional] 
**entity_item_types** | [**List[EntityItemTypeEnum]**](EntityItemTypeEnum.md) | Filter by entity item types. | [optional] 
**entity_name** | [**EntityNameFilter**](EntityNameFilter.md) |  | [optional] 
**entity_tag** | [**EntityTagFilter**](EntityTagFilter.md) |  | [optional] 
**hr_idp_status** | [**IdpStatusFilter**](IdpStatusFilter.md) |  | [optional] 
**entity_admin_owner** | [**EntityAdminFilter**](EntityAdminFilter.md) |  | [optional] 
**entity_ids** | **List[UUID]** | Filter by specific entity UUIDs. | [optional] 
**imported_from_app** | **List[UUID]** | Filter by app IDs from which returned nodes will be imported from. | [optional] 
**role_remote_ids** | **List[str]** | Filter by role remote IDs. Can only be applied within a hasAccessTo clause. | [optional] 
**role_names** | **List[str]** | Filter by role display names (e.g. \&quot;Admin\&quot;, \&quot;Read\&quot;). Can only be applied within a hasAccessTo clause. | [optional] 
**all_of** | [**List[AccessEntityFilters]**](AccessEntityFilters.md) | A list of nested filters that must all match (logical AND). Each  item has the same shape as this object — scalar fields like  &#x60;entityTypes&#x60; or &#x60;entityTag&#x60;, and can further nest &#x60;allOf&#x60;,  &#x60;anyOf&#x60;, or &#x60;not&#x60;.  | [optional] 
**any_of** | [**List[AccessEntityFilters]**](AccessEntityFilters.md) | A list of nested filters where at least one must match (logical  OR). Each item has the same shape as this object.  | [optional] 
**var_not** | **object** | Excludes entities matching the embedded filter (logical NOT). Pass a filter object with the same shape as this one — typically a single scalar field, like &#x60;{not: {entityTypes: [\&quot;RESOURCE\&quot;]}}&#x60; to exclude resources.  | [optional] 

## Example

```python
from opal_security.models.access_entity_filters import AccessEntityFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AccessEntityFilters from a JSON string
access_entity_filters_instance = AccessEntityFilters.from_json(json)
# print the JSON string representation of the object
print(AccessEntityFilters.to_json())

# convert the object into a dict
access_entity_filters_dict = access_entity_filters_instance.to_dict()
# create an instance of AccessEntityFilters from a dict
access_entity_filters_from_dict = AccessEntityFilters.from_dict(access_entity_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


