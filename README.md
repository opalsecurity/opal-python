# opal
Your Home For Developer Resources.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.opal.dev/](https://www.opal.dev/)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/opalsecurity/opal-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/opalsecurity/opal-pythong.git`)

Then import the package:
```python
import opal
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import opal
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import opal
from pprint import pprint
from opal.api import events_api
from opal.model.paginated_event_list import PaginatedEventList
# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = opal.Configuration(
    host = "https://api.opal.dev/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with opal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    start_date_filter = "2021/11/01" # str | A start date filter for the events. (optional)
end_date_filter = "2021-11-12" # str | An end date filter for the events. (optional)
actor_filter = "29827fb8-f2dd-4e80-9576-28e31e9934ac" # str | An actor filter for the events. Supply the ID of the actor. (optional)
object_filter = "29827fb8-f2dd-4e80-9576-28e31e9934ac" # str | An object filter for the events. Supply the ID of the object. (optional)
event_type_filter = "29827fb8-f2dd-4e80-9576-28e31e9934ac" # str | An event type filter for the events. (optional)
cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
page_size = 200 # int | Number of results to return per page. Default is 200. (optional)

    try:
        api_response = api_instance.events(start_date_filter=start_date_filter, end_date_filter=end_date_filter, actor_filter=actor_filter, object_filter=object_filter, event_type_filter=event_type_filter, cursor=cursor, page_size=page_size)
        pprint(api_response)
    except opal.ApiException as e:
        print("Exception when calling EventsApi->events: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.opal.dev/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EventsApi* | [**events**](docs/EventsApi.md#events) | **GET** /events | 
*GroupsApi* | [**convert_group**](docs/GroupsApi.md#convert_group) | **PUT** /groups/{group_id}/convert | 
*GroupsApi* | [**delete_group**](docs/GroupsApi.md#delete_group) | **DELETE** /groups/{group_id} | 
*GroupsApi* | [**get_group_message_channels**](docs/GroupsApi.md#get_group_message_channels) | **GET** /groups/{group_id}/message-channels | 
*GroupsApi* | [**get_group_reviewers**](docs/GroupsApi.md#get_group_reviewers) | **GET** /groups/{group_id}/reviewers | 
*GroupsApi* | [**get_group_tags**](docs/GroupsApi.md#get_group_tags) | **GET** /groups/{group_id}/tags | 
*GroupsApi* | [**get_groups**](docs/GroupsApi.md#get_groups) | **GET** /groups | 
*GroupsApi* | [**set_group_message_channels**](docs/GroupsApi.md#set_group_message_channels) | **PUT** /groups/{group_id}/message-channels | 
*GroupsApi* | [**set_group_reviewers**](docs/GroupsApi.md#set_group_reviewers) | **PUT** /groups/{group_id}/reviewers | 
*GroupsApi* | [**update_groups**](docs/GroupsApi.md#update_groups) | **PUT** /groups | 
*ResourcesApi* | [**delete_resource**](docs/ResourcesApi.md#delete_resource) | **DELETE** /resources/{resource_id} | 
*ResourcesApi* | [**get_resource_message_channels**](docs/ResourcesApi.md#get_resource_message_channels) | **GET** /resources/{resource_id}/message-channels | 
*ResourcesApi* | [**get_resource_reviewers**](docs/ResourcesApi.md#get_resource_reviewers) | **GET** /resources/{resource_id}/reviewers | 
*ResourcesApi* | [**get_resource_tags**](docs/ResourcesApi.md#get_resource_tags) | **GET** /resources/{resource_id}/tags | 
*ResourcesApi* | [**get_resources**](docs/ResourcesApi.md#get_resources) | **GET** /resources | 
*ResourcesApi* | [**resource_user_access_status_retrieve**](docs/ResourcesApi.md#resource_user_access_status_retrieve) | **GET** /resource-user-access-status/{resource_id}/{user_id} | 
*ResourcesApi* | [**resource_users**](docs/ResourcesApi.md#resource_users) | **GET** /resource-users | 
*ResourcesApi* | [**set_resource_message_channels**](docs/ResourcesApi.md#set_resource_message_channels) | **PUT** /resources/{resource_id}/message-channels | 
*ResourcesApi* | [**set_resource_reviewers**](docs/ResourcesApi.md#set_resource_reviewers) | **PUT** /resources/{resource_id}/reviewers | 
*ResourcesApi* | [**update_resources**](docs/ResourcesApi.md#update_resources) | **PUT** /resources | 
*SessionsApi* | [**sessions**](docs/SessionsApi.md#sessions) | **GET** /sessions | 
*TagsApi* | [**add_group_tag**](docs/TagsApi.md#add_group_tag) | **POST** /tags/{tag_id}/groups/{group_id} | 
*TagsApi* | [**add_resource_tag**](docs/TagsApi.md#add_resource_tag) | **POST** /tags/{tag_id}/resources/{resource_id} | 
*TagsApi* | [**add_user_tag**](docs/TagsApi.md#add_user_tag) | **POST** /tags/{tag_id}/users/{user_id} | 
*TagsApi* | [**create_tag**](docs/TagsApi.md#create_tag) | **POST** /tag | 
*TagsApi* | [**get_tag**](docs/TagsApi.md#get_tag) | **GET** /tag | 
*TagsApi* | [**remove_group_tag**](docs/TagsApi.md#remove_group_tag) | **DELETE** /tags/{tag_id}/groups/{group_id} | 
*TagsApi* | [**remove_resource_tag**](docs/TagsApi.md#remove_resource_tag) | **DELETE** /tags/{tag_id}/resources/{resource_id} | 
*TagsApi* | [**remove_user_tag**](docs/TagsApi.md#remove_user_tag) | **DELETE** /tags/{tag_id}/users/{user_id} | 
*UsersApi* | [**get_user_tags**](docs/UsersApi.md#get_user_tags) | **GET** /users/{user_id}/tags | 
*UsersApi* | [**user**](docs/UsersApi.md#user) | **GET** /user | 


## Documentation For Models

 - [EntityTypeEnum](docs/EntityTypeEnum.md)
 - [Event](docs/Event.md)
 - [Group](docs/Group.md)
 - [GroupFunctionEnum](docs/GroupFunctionEnum.md)
 - [GroupTypeEnum](docs/GroupTypeEnum.md)
 - [MessageChannel](docs/MessageChannel.md)
 - [MessageChannelIDList](docs/MessageChannelIDList.md)
 - [MessageChannelList](docs/MessageChannelList.md)
 - [MessageChannelProviderEnum](docs/MessageChannelProviderEnum.md)
 - [MessageChannelTypeEnum](docs/MessageChannelTypeEnum.md)
 - [NewAdminIDList](docs/NewAdminIDList.md)
 - [PaginatedEventList](docs/PaginatedEventList.md)
 - [PaginatedGroupsList](docs/PaginatedGroupsList.md)
 - [PaginatedResourceUserList](docs/PaginatedResourceUserList.md)
 - [PaginatedResourcesList](docs/PaginatedResourcesList.md)
 - [Resource](docs/Resource.md)
 - [ResourceAccessLevel](docs/ResourceAccessLevel.md)
 - [ResourceTypeEnum](docs/ResourceTypeEnum.md)
 - [ResourceUser](docs/ResourceUser.md)
 - [ResourceUserAccessStatus](docs/ResourceUserAccessStatus.md)
 - [ResourceUserAccessStatusEnum](docs/ResourceUserAccessStatusEnum.md)
 - [ReviewerIDList](docs/ReviewerIDList.md)
 - [Session](docs/Session.md)
 - [SessionsList](docs/SessionsList.md)
 - [Tag](docs/Tag.md)
 - [TagsList](docs/TagsList.md)
 - [UpdateGroupInfo](docs/UpdateGroupInfo.md)
 - [UpdateGroupInfoList](docs/UpdateGroupInfoList.md)
 - [UpdateResourceInfo](docs/UpdateResourceInfo.md)
 - [UpdateResourceInfoList](docs/UpdateResourceInfoList.md)
 - [User](docs/User.md)
 - [UsersList](docs/UsersList.md)
 - [VisibilityEnum](docs/VisibilityEnum.md)


## Documentation For Authorization


## BearerAuth

- **Type**: Bearer authentication


## Author

hello@opal.dev


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in opal.apis and opal.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from opal.api.default_api import DefaultApi`
- `from opal.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import opal
from opal.apis import *
from opal.models import *
```

