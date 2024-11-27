# UAR

A user access review.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uar_id** | **str** | The ID of the UAR. | 
**name** | **str** | The name of the UAR. | 
**reviewer_assignment_policy** | [**UARReviewerAssignmentPolicyEnum**](UARReviewerAssignmentPolicyEnum.md) |  | 
**send_reviewer_assignment_notification** | **bool** | A bool representing whether to send a notification to reviewers when they&#39;re assigned a new review. Default is False. | 
**deadline** | **datetime** | The last day for reviewers to complete their access reviews. | 
**time_zone** | **str** | The time zone name (as defined by the IANA Time Zone database) used in the access review deadline and exported audit report. Default is America/Los_Angeles. | 
**self_review_allowed** | **bool** | A bool representing whether to present a warning when a user is the only reviewer for themself. Default is False. | 
**uar_scope** | [**UARScope**](UARScope.md) |  | [optional] 

## Example

```python
from opal_security.models.uar import UAR

# TODO update the JSON string below
json = "{}"
# create an instance of UAR from a JSON string
uar_instance = UAR.from_json(json)
# print the JSON string representation of the object
print(UAR.to_json())

# convert the object into a dict
uar_dict = uar_instance.to_dict()
# create an instance of UAR from a dict
uar_from_dict = UAR.from_dict(uar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


