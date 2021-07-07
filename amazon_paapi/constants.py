"""Module containing all the constants."""

from .sdk.models.search_items_resource import SearchItemsResource
from .sdk.models.get_variations_resource import GetVariationsResource
from .sdk.models.get_browse_nodes_resource import GetBrowseNodesResource


class Country(object):
    AU = 'AU'
    BR = 'BR'
    CA = 'CA'
    FR = 'FR'
    DE = 'DE'
    IN = 'IN'
    IT = 'IT'
    JP = 'JP'
    MX = 'MX'
    NL = 'NL'
    PL = 'PL'
    SG = 'SG'
    SA = 'SA'
    ES = 'ES'
    SE = 'SE'
    TR = 'TR'
    AE = 'AE'
    UK = 'UK'
    US = 'US'


"""Available regions for the Amazon API."""
_REGIONS = {
    'AU': 'us-west-2',
    'BR': 'us-east-1',
    'CA': 'us-east-1',
    'FR': 'eu-west-1',
    'DE': 'eu-west-1',
    'IN': 'eu-west-1',
    'IT': 'eu-west-1',
    'JP': 'us-west-2',
    'MX': 'us-east-1',
    'NL': 'eu-west-1',
    'PL': 'eu-west-1',
    'SG': 'us-west-2',
    'SA': 'eu-west-1',
    'ES': 'eu-west-1',
    'SE': 'eu-west-1',
    'TR': 'eu-west-1',
    'AE': 'eu-west-1',
    'UK': 'eu-west-1',
    'US': 'us-east-1'
}

"""Domains for each region on the Amazon API."""
_DOMAINS = {
    'AU': 'com.au',
    'BR': 'com.br',
    'CA': 'ca',
    'FR': 'fr',
    'DE': 'de',
    'IN': 'in',
    'IT': 'it',
    'JP': 'co.jp',
    'MX': 'com.mx',
    'NL': 'nl',
    'PL': 'pl',
    'SG': 'sg',
    'SA': 'sa',
    'ES': 'es',
    'SE': 'se',
    'TR': 'com.tr',
    'AE': 'ae',
    'UK': 'co.uk',
    'US': 'com',
}

"""Search resources to get from Amazon API."""
SEARCH_RESOURCES = [
    SearchItemsResource.BROWSENODEINFO_BROWSENODES,
    SearchItemsResource.BROWSENODEINFO_BROWSENODES_ANCESTOR,
    SearchItemsResource.BROWSENODEINFO_BROWSENODES_SALESRANK,
    SearchItemsResource.BROWSENODEINFO_WEBSITESALESRANK,
    SearchItemsResource.IMAGES_PRIMARY_SMALL,
    SearchItemsResource.IMAGES_PRIMARY_MEDIUM,
    SearchItemsResource.IMAGES_PRIMARY_LARGE,
    SearchItemsResource.IMAGES_VARIANTS_SMALL,
    SearchItemsResource.IMAGES_VARIANTS_MEDIUM,
    SearchItemsResource.IMAGES_VARIANTS_LARGE,
    SearchItemsResource.ITEMINFO_BYLINEINFO,
    SearchItemsResource.ITEMINFO_CONTENTINFO,
    SearchItemsResource.ITEMINFO_CONTENTRATING,
    SearchItemsResource.ITEMINFO_CLASSIFICATIONS,
    SearchItemsResource.ITEMINFO_EXTERNALIDS,
    SearchItemsResource.ITEMINFO_FEATURES,
    SearchItemsResource.ITEMINFO_MANUFACTUREINFO,
    SearchItemsResource.ITEMINFO_PRODUCTINFO,
    SearchItemsResource.ITEMINFO_TECHNICALINFO,
    SearchItemsResource.ITEMINFO_TITLE,
    SearchItemsResource.ITEMINFO_TRADEININFO,
    SearchItemsResource.OFFERS_LISTINGS_AVAILABILITY_MAXORDERQUANTITY,
    SearchItemsResource.OFFERS_LISTINGS_AVAILABILITY_MESSAGE,
    SearchItemsResource.OFFERS_LISTINGS_AVAILABILITY_MINORDERQUANTITY,
    SearchItemsResource.OFFERS_LISTINGS_AVAILABILITY_TYPE,
    SearchItemsResource.OFFERS_LISTINGS_CONDITION,
    SearchItemsResource.OFFERS_LISTINGS_CONDITION_SUBCONDITION,
    SearchItemsResource.OFFERS_LISTINGS_DELIVERYINFO_ISAMAZONFULFILLED,
    SearchItemsResource.OFFERS_LISTINGS_DELIVERYINFO_ISFREESHIPPINGELIGIBLE,
    SearchItemsResource.OFFERS_LISTINGS_DELIVERYINFO_ISPRIMEELIGIBLE,
    SearchItemsResource.OFFERS_LISTINGS_DELIVERYINFO_SHIPPINGCHARGES,
    SearchItemsResource.OFFERS_LISTINGS_ISBUYBOXWINNER,
    SearchItemsResource.OFFERS_LISTINGS_LOYALTYPOINTS_POINTS,
    SearchItemsResource.OFFERS_LISTINGS_MERCHANTINFO,
    SearchItemsResource.OFFERS_LISTINGS_PRICE,
    SearchItemsResource.OFFERS_LISTINGS_PROGRAMELIGIBILITY_ISPRIMEEXCLUSIVE,
    SearchItemsResource.OFFERS_LISTINGS_PROGRAMELIGIBILITY_ISPRIMEPANTRY,
    SearchItemsResource.OFFERS_LISTINGS_PROMOTIONS,
    SearchItemsResource.OFFERS_LISTINGS_SAVINGBASIS,
    SearchItemsResource.OFFERS_SUMMARIES_HIGHESTPRICE,
    SearchItemsResource.OFFERS_SUMMARIES_LOWESTPRICE,
    SearchItemsResource.OFFERS_SUMMARIES_OFFERCOUNT,
    SearchItemsResource.PARENTASIN,
    SearchItemsResource.RENTALOFFERS_LISTINGS_AVAILABILITY_MAXORDERQUANTITY,
    SearchItemsResource.RENTALOFFERS_LISTINGS_AVAILABILITY_MESSAGE,
    SearchItemsResource.RENTALOFFERS_LISTINGS_AVAILABILITY_MINORDERQUANTITY,
    SearchItemsResource.RENTALOFFERS_LISTINGS_AVAILABILITY_TYPE,
    SearchItemsResource.RENTALOFFERS_LISTINGS_BASEPRICE,
    SearchItemsResource.RENTALOFFERS_LISTINGS_CONDITION,
    SearchItemsResource.RENTALOFFERS_LISTINGS_CONDITION_SUBCONDITION,
    SearchItemsResource.RENTALOFFERS_LISTINGS_DELIVERYINFO_ISAMAZONFULFILLED,
    SearchItemsResource.RENTALOFFERS_LISTINGS_DELIVERYINFO_ISFREESHIPPINGELIGIBLE,
    SearchItemsResource.RENTALOFFERS_LISTINGS_DELIVERYINFO_ISPRIMEELIGIBLE,
    SearchItemsResource.RENTALOFFERS_LISTINGS_DELIVERYINFO_SHIPPINGCHARGES,
    SearchItemsResource.RENTALOFFERS_LISTINGS_MERCHANTINFO,
    SearchItemsResource.SEARCHREFINEMENTS]

"""Variation resources to get from Amazon API."""
VARIATION_RESOURCES = [
    GetVariationsResource.BROWSENODEINFO_BROWSENODES,
    GetVariationsResource.BROWSENODEINFO_BROWSENODES_ANCESTOR,
    GetVariationsResource.BROWSENODEINFO_BROWSENODES_SALESRANK,
    GetVariationsResource.BROWSENODEINFO_WEBSITESALESRANK,
    GetVariationsResource.IMAGES_PRIMARY_SMALL,
    GetVariationsResource.IMAGES_PRIMARY_MEDIUM,
    GetVariationsResource.IMAGES_PRIMARY_LARGE,
    GetVariationsResource.IMAGES_VARIANTS_SMALL,
    GetVariationsResource.IMAGES_VARIANTS_MEDIUM,
    GetVariationsResource.IMAGES_VARIANTS_LARGE,
    GetVariationsResource.ITEMINFO_BYLINEINFO,
    GetVariationsResource.ITEMINFO_CONTENTINFO,
    GetVariationsResource.ITEMINFO_CONTENTRATING,
    GetVariationsResource.ITEMINFO_CLASSIFICATIONS,
    GetVariationsResource.ITEMINFO_EXTERNALIDS,
    GetVariationsResource.ITEMINFO_FEATURES,
    GetVariationsResource.ITEMINFO_MANUFACTUREINFO,
    GetVariationsResource.ITEMINFO_PRODUCTINFO,
    GetVariationsResource.ITEMINFO_TECHNICALINFO,
    GetVariationsResource.ITEMINFO_TITLE,
    GetVariationsResource.ITEMINFO_TRADEININFO,
    GetVariationsResource.OFFERS_LISTINGS_AVAILABILITY_MAXORDERQUANTITY,
    GetVariationsResource.OFFERS_LISTINGS_AVAILABILITY_MESSAGE,
    GetVariationsResource.OFFERS_LISTINGS_AVAILABILITY_MINORDERQUANTITY,
    GetVariationsResource.OFFERS_LISTINGS_AVAILABILITY_TYPE,
    GetVariationsResource.OFFERS_LISTINGS_CONDITION,
    GetVariationsResource.OFFERS_LISTINGS_CONDITION_SUBCONDITION,
    GetVariationsResource.OFFERS_LISTINGS_DELIVERYINFO_ISAMAZONFULFILLED,
    GetVariationsResource.OFFERS_LISTINGS_DELIVERYINFO_ISFREESHIPPINGELIGIBLE,
    GetVariationsResource.OFFERS_LISTINGS_DELIVERYINFO_ISPRIMEELIGIBLE,
    GetVariationsResource.OFFERS_LISTINGS_DELIVERYINFO_SHIPPINGCHARGES,
    GetVariationsResource.OFFERS_LISTINGS_ISBUYBOXWINNER,
    GetVariationsResource.OFFERS_LISTINGS_LOYALTYPOINTS_POINTS,
    GetVariationsResource.OFFERS_LISTINGS_MERCHANTINFO,
    GetVariationsResource.OFFERS_LISTINGS_PRICE,
    GetVariationsResource.OFFERS_LISTINGS_PROGRAMELIGIBILITY_ISPRIMEEXCLUSIVE,
    GetVariationsResource.OFFERS_LISTINGS_PROGRAMELIGIBILITY_ISPRIMEPANTRY,
    GetVariationsResource.OFFERS_LISTINGS_PROMOTIONS,
    GetVariationsResource.OFFERS_LISTINGS_SAVINGBASIS,
    GetVariationsResource.OFFERS_SUMMARIES_HIGHESTPRICE,
    GetVariationsResource.OFFERS_SUMMARIES_LOWESTPRICE,
    GetVariationsResource.OFFERS_SUMMARIES_OFFERCOUNT,
    GetVariationsResource.PARENTASIN,
    GetVariationsResource.RENTALOFFERS_LISTINGS_AVAILABILITY_MAXORDERQUANTITY,
    GetVariationsResource.RENTALOFFERS_LISTINGS_AVAILABILITY_MESSAGE,
    GetVariationsResource.RENTALOFFERS_LISTINGS_AVAILABILITY_MINORDERQUANTITY,
    GetVariationsResource.RENTALOFFERS_LISTINGS_AVAILABILITY_TYPE,
    GetVariationsResource.RENTALOFFERS_LISTINGS_BASEPRICE,
    GetVariationsResource.RENTALOFFERS_LISTINGS_CONDITION,
    GetVariationsResource.RENTALOFFERS_LISTINGS_CONDITION_SUBCONDITION,
    GetVariationsResource.RENTALOFFERS_LISTINGS_DELIVERYINFO_ISAMAZONFULFILLED,
    GetVariationsResource.RENTALOFFERS_LISTINGS_DELIVERYINFO_ISFREESHIPPINGELIGIBLE,
    GetVariationsResource.RENTALOFFERS_LISTINGS_DELIVERYINFO_ISPRIMEELIGIBLE,
    GetVariationsResource.RENTALOFFERS_LISTINGS_DELIVERYINFO_SHIPPINGCHARGES,
    GetVariationsResource.RENTALOFFERS_LISTINGS_MERCHANTINFO,
    GetVariationsResource.VARIATIONSUMMARY_PRICE_HIGHESTPRICE,
    GetVariationsResource.VARIATIONSUMMARY_PRICE_LOWESTPRICE,
    GetVariationsResource.VARIATIONSUMMARY_VARIATIONDIMENSION
]

"""Browse Node resources to get from Amazon API."""
BROWSE_RESOURCES = [
    GetBrowseNodesResource.ANCESTOR,
    GetBrowseNodesResource.CHILDREN
]
