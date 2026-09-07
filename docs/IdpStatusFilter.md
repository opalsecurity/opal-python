# IdpStatusFilter

Filters USER entities by their HR/IDP lifecycle status. Only applies to USER entities; GROUP and RESOURCE entities never match, in either polarity. `statuses` combine with OR. `not` inverts the match within the user domain (e.g. \"IDP status is NOT active\"), so it still returns only users rather than sweeping in groups/resources. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statuses** | [**List[UserHrIdpStatusEnum]**](UserHrIdpStatusEnum.md) | Match users whose HR/IDP status is one of these values. | [optional] 
**var_not** | **bool** | Invert the match within the user domain (e.g. \&quot;IDP status is NOT active\&quot;). | [optional] 

## Example

```python
from opal_security.models.idp_status_filter import IdpStatusFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IdpStatusFilter from a JSON string
idp_status_filter_instance = IdpStatusFilter.from_json(json)
# print the JSON string representation of the object
print(IdpStatusFilter.to_json())

# convert the object into a dict
idp_status_filter_dict = idp_status_filter_instance.to_dict()
# create an instance of IdpStatusFilter from a dict
idp_status_filter_from_dict = IdpStatusFilter.from_dict(idp_status_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


