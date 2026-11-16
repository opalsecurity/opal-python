# AgentActivityImages

# AgentActivityImages Object ### Description The images attached to a prompt or returned by a tool. Only their number and size are sent; the images themselves are not.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**bytes** | **int** |  | [optional] 

## Example

```python
from opal_security.models.agent_activity_images import AgentActivityImages

# TODO update the JSON string below
json = "{}"
# create an instance of AgentActivityImages from a JSON string
agent_activity_images_instance = AgentActivityImages.from_json(json)
# print the JSON string representation of the object
print(AgentActivityImages.to_json())

# convert the object into a dict
agent_activity_images_dict = agent_activity_images_instance.to_dict()
# create an instance of AgentActivityImages from a dict
agent_activity_images_from_dict = AgentActivityImages.from_dict(agent_activity_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


