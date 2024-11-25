# coding: utf-8

"""
    Opal API

    Your Home For Developer Resources.

    The version of the OpenAPI document: 1.0
    Contact: hello@opal.dev
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from opal.models.paginated_event_list import PaginatedEventList

from opal.api_client import ApiClient, RequestSerialized
from opal.api_response import ApiResponse
from opal.rest import RESTResponseType


class EventsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def events(
        self,
        start_date_filter: Annotated[Optional[StrictStr], Field(description="A start date filter for the events.")] = None,
        end_date_filter: Annotated[Optional[StrictStr], Field(description="An end date filter for the events.")] = None,
        actor_filter: Annotated[Optional[StrictStr], Field(description="An actor filter for the events. Supply the ID of the actor.")] = None,
        object_filter: Annotated[Optional[StrictStr], Field(description="An object filter for the events. Supply the ID of the object.")] = None,
        event_type_filter: Annotated[Optional[StrictStr], Field(description="An event type filter for the events.")] = None,
        api_token_filter: Annotated[Optional[StrictStr], Field(description="An API filter for the events. Supply the name and preview of the API token.")] = None,
        cursor: Annotated[Optional[StrictStr], Field(description="The pagination cursor value.")] = None,
        page_size: Annotated[Optional[Annotated[int, Field(le=1000, strict=True)]], Field(description="Number of results to return per page. Default is 200.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PaginatedEventList:
        """events

        Returns a list of `Event` objects.

        :param start_date_filter: A start date filter for the events.
        :type start_date_filter: str
        :param end_date_filter: An end date filter for the events.
        :type end_date_filter: str
        :param actor_filter: An actor filter for the events. Supply the ID of the actor.
        :type actor_filter: str
        :param object_filter: An object filter for the events. Supply the ID of the object.
        :type object_filter: str
        :param event_type_filter: An event type filter for the events.
        :type event_type_filter: str
        :param api_token_filter: An API filter for the events. Supply the name and preview of the API token.
        :type api_token_filter: str
        :param cursor: The pagination cursor value.
        :type cursor: str
        :param page_size: Number of results to return per page. Default is 200.
        :type page_size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._events_serialize(
            start_date_filter=start_date_filter,
            end_date_filter=end_date_filter,
            actor_filter=actor_filter,
            object_filter=object_filter,
            event_type_filter=event_type_filter,
            api_token_filter=api_token_filter,
            cursor=cursor,
            page_size=page_size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedEventList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def events_with_http_info(
        self,
        start_date_filter: Annotated[Optional[StrictStr], Field(description="A start date filter for the events.")] = None,
        end_date_filter: Annotated[Optional[StrictStr], Field(description="An end date filter for the events.")] = None,
        actor_filter: Annotated[Optional[StrictStr], Field(description="An actor filter for the events. Supply the ID of the actor.")] = None,
        object_filter: Annotated[Optional[StrictStr], Field(description="An object filter for the events. Supply the ID of the object.")] = None,
        event_type_filter: Annotated[Optional[StrictStr], Field(description="An event type filter for the events.")] = None,
        api_token_filter: Annotated[Optional[StrictStr], Field(description="An API filter for the events. Supply the name and preview of the API token.")] = None,
        cursor: Annotated[Optional[StrictStr], Field(description="The pagination cursor value.")] = None,
        page_size: Annotated[Optional[Annotated[int, Field(le=1000, strict=True)]], Field(description="Number of results to return per page. Default is 200.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PaginatedEventList]:
        """events

        Returns a list of `Event` objects.

        :param start_date_filter: A start date filter for the events.
        :type start_date_filter: str
        :param end_date_filter: An end date filter for the events.
        :type end_date_filter: str
        :param actor_filter: An actor filter for the events. Supply the ID of the actor.
        :type actor_filter: str
        :param object_filter: An object filter for the events. Supply the ID of the object.
        :type object_filter: str
        :param event_type_filter: An event type filter for the events.
        :type event_type_filter: str
        :param api_token_filter: An API filter for the events. Supply the name and preview of the API token.
        :type api_token_filter: str
        :param cursor: The pagination cursor value.
        :type cursor: str
        :param page_size: Number of results to return per page. Default is 200.
        :type page_size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._events_serialize(
            start_date_filter=start_date_filter,
            end_date_filter=end_date_filter,
            actor_filter=actor_filter,
            object_filter=object_filter,
            event_type_filter=event_type_filter,
            api_token_filter=api_token_filter,
            cursor=cursor,
            page_size=page_size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedEventList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def events_without_preload_content(
        self,
        start_date_filter: Annotated[Optional[StrictStr], Field(description="A start date filter for the events.")] = None,
        end_date_filter: Annotated[Optional[StrictStr], Field(description="An end date filter for the events.")] = None,
        actor_filter: Annotated[Optional[StrictStr], Field(description="An actor filter for the events. Supply the ID of the actor.")] = None,
        object_filter: Annotated[Optional[StrictStr], Field(description="An object filter for the events. Supply the ID of the object.")] = None,
        event_type_filter: Annotated[Optional[StrictStr], Field(description="An event type filter for the events.")] = None,
        api_token_filter: Annotated[Optional[StrictStr], Field(description="An API filter for the events. Supply the name and preview of the API token.")] = None,
        cursor: Annotated[Optional[StrictStr], Field(description="The pagination cursor value.")] = None,
        page_size: Annotated[Optional[Annotated[int, Field(le=1000, strict=True)]], Field(description="Number of results to return per page. Default is 200.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """events

        Returns a list of `Event` objects.

        :param start_date_filter: A start date filter for the events.
        :type start_date_filter: str
        :param end_date_filter: An end date filter for the events.
        :type end_date_filter: str
        :param actor_filter: An actor filter for the events. Supply the ID of the actor.
        :type actor_filter: str
        :param object_filter: An object filter for the events. Supply the ID of the object.
        :type object_filter: str
        :param event_type_filter: An event type filter for the events.
        :type event_type_filter: str
        :param api_token_filter: An API filter for the events. Supply the name and preview of the API token.
        :type api_token_filter: str
        :param cursor: The pagination cursor value.
        :type cursor: str
        :param page_size: Number of results to return per page. Default is 200.
        :type page_size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._events_serialize(
            start_date_filter=start_date_filter,
            end_date_filter=end_date_filter,
            actor_filter=actor_filter,
            object_filter=object_filter,
            event_type_filter=event_type_filter,
            api_token_filter=api_token_filter,
            cursor=cursor,
            page_size=page_size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedEventList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _events_serialize(
        self,
        start_date_filter,
        end_date_filter,
        actor_filter,
        object_filter,
        event_type_filter,
        api_token_filter,
        cursor,
        page_size,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if start_date_filter is not None:
            
            _query_params.append(('start_date_filter', start_date_filter))
            
        if end_date_filter is not None:
            
            _query_params.append(('end_date_filter', end_date_filter))
            
        if actor_filter is not None:
            
            _query_params.append(('actor_filter', actor_filter))
            
        if object_filter is not None:
            
            _query_params.append(('object_filter', object_filter))
            
        if event_type_filter is not None:
            
            _query_params.append(('event_type_filter', event_type_filter))
            
        if api_token_filter is not None:
            
            _query_params.append(('api_token_filter', api_token_filter))
            
        if cursor is not None:
            
            _query_params.append(('cursor', cursor))
            
        if page_size is not None:
            
            _query_params.append(('page_size', page_size))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/events',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


