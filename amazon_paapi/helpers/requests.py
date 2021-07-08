"""Module with helper functions for creating requests."""


from .. import models
from ..sdk.models.get_items_resource import GetItemsResource
from ..sdk.rest import ApiException
from ..sdk.models.partner_type import PartnerType
from ..sdk.models.get_items_request import GetItemsRequest
from ..errors import ApiRequestException, ItemsNotFoudException, MalformedRequestException
import inspect


def get_items_request(self, asin_chunk: list[str], **kwargs) -> models.GetItemsRequest:
    try:
        return GetItemsRequest(resources=_get_items_request_resources(),
                               partner_type=PartnerType.ASSOCIATES,
                               marketplace=self._marketplace,
                               partner_tag=self._tag,
                               item_ids=asin_chunk,
                               **kwargs)
    except TypeError:
        raise MalformedRequestException('Parameters for get_items request are not correct')


def _get_items_request_resources() -> list[models.GetItemsResource]:
    resources = inspect.getmembers(GetItemsResource, lambda a:not(inspect.isroutine(a)))
    resources = [x[-1] for x in resources if isinstance(x[-1], str) and x[0][0:2] != '__']
    return resources


def get_items_response(self, request: models.GetItemsRequest) -> list[models.ApiItem]:
    try:
        response = self._api.get_items(request)
    except ApiException as e:
        raise ApiRequestException('Error getting a response from Amazon API: ' + str(e))

    if response.items_result == None:
        raise ItemsNotFoudException('No items have been found')

    return response.items_result.items
