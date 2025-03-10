# RequestConfiguration

# Request Configuration Object ### Description The `RequestConfiguration` object is used to represent a request configuration.  ### Usage Example Returned from the `GET Request Configurations` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | [**Condition**](Condition.md) | The condition for the request configuration. | [optional] 
**allow_requests** | **bool** | A bool representing whether or not to allow requests for this resource. | 
**auto_approval** | **bool** | A bool representing whether or not to automatically approve requests for this resource. | 
**require_mfa_to_request** | **bool** | A bool representing whether or not to require MFA for requesting access to this resource. | 
**max_duration_minutes** | **int** | The maximum duration for which the resource can be requested (in minutes). | [optional] 
**recommended_duration_minutes** | **int** | The recommended duration for which the resource should be requested (in minutes). -1 represents an indefinite duration. | [optional] 
**require_support_ticket** | **bool** | A bool representing whether or not access requests to the resource require an access ticket. | 
**request_template_id** | **str** | The ID of the associated request template. | [optional] 
**reviewer_stages** | [**List[ReviewerStage]**](ReviewerStage.md) | The list of reviewer stages for the request configuration. | [optional] 
**priority** | **int** | The priority of the request configuration. | 

## Example

```python
from opal_security.models.request_configuration import RequestConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RequestConfiguration from a JSON string
request_configuration_instance = RequestConfiguration.from_json(json)
# print the JSON string representation of the object
print(RequestConfiguration.to_json())

# convert the object into a dict
request_configuration_dict = request_configuration_instance.to_dict()
# create an instance of RequestConfiguration from a dict
request_configuration_from_dict = RequestConfiguration.from_dict(request_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


