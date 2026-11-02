# AnthropicInferenceHookVerdict

# AnthropicInferenceHookVerdict Object ### Description An Anthropic Inference hooks verdict. `deny_reason` is shown to the end user on a deny.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**deny_reason** | **str** |  | [optional] 
**reference_id** | **str** |  | [optional] 

## Example

```python
from opal_security.models.anthropic_inference_hook_verdict import AnthropicInferenceHookVerdict

# TODO update the JSON string below
json = "{}"
# create an instance of AnthropicInferenceHookVerdict from a JSON string
anthropic_inference_hook_verdict_instance = AnthropicInferenceHookVerdict.from_json(json)
# print the JSON string representation of the object
print(AnthropicInferenceHookVerdict.to_json())

# convert the object into a dict
anthropic_inference_hook_verdict_dict = anthropic_inference_hook_verdict_instance.to_dict()
# create an instance of AnthropicInferenceHookVerdict from a dict
anthropic_inference_hook_verdict_from_dict = AnthropicInferenceHookVerdict.from_dict(anthropic_inference_hook_verdict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


