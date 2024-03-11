# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class QueryUsageResponseBodyDataArticleInfos(TeaModel):
    def __init__(self, article_type=None, title=None, url=None):
        self.article_type = article_type  # type: str
        self.title = title  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUsageResponseBodyDataArticleInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.article_type is not None:
            result['articleType'] = self.article_type
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('articleType') is not None:
            self.article_type = m.get('articleType')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class QueryUsageResponseBodyDataCommoditySpecUsageInfosCommodityConfig(TeaModel):
    def __init__(self, beta_deadline_ms=None, commodity_code=None, commodity_name=None,
                 expired_to_released_hour=None, in_beta=None, independent=None, paid_type=None, product_code=None, quota_items=None,
                 spec_codes=None):
        self.beta_deadline_ms = beta_deadline_ms  # type: long
        self.commodity_code = commodity_code  # type: str
        self.commodity_name = commodity_name  # type: str
        self.expired_to_released_hour = expired_to_released_hour  # type: long
        self.in_beta = in_beta  # type: bool
        self.independent = independent  # type: bool
        self.paid_type = paid_type  # type: str
        self.product_code = product_code  # type: str
        self.quota_items = quota_items  # type: list[str]
        self.spec_codes = spec_codes  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUsageResponseBodyDataCommoditySpecUsageInfosCommodityConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.beta_deadline_ms is not None:
            result['betaDeadlineMs'] = self.beta_deadline_ms
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.commodity_name is not None:
            result['commodityName'] = self.commodity_name
        if self.expired_to_released_hour is not None:
            result['expiredToReleasedHour'] = self.expired_to_released_hour
        if self.in_beta is not None:
            result['inBeta'] = self.in_beta
        if self.independent is not None:
            result['independent'] = self.independent
        if self.paid_type is not None:
            result['paidType'] = self.paid_type
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.quota_items is not None:
            result['quotaItems'] = self.quota_items
        if self.spec_codes is not None:
            result['specCodes'] = self.spec_codes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('betaDeadlineMs') is not None:
            self.beta_deadline_ms = m.get('betaDeadlineMs')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('commodityName') is not None:
            self.commodity_name = m.get('commodityName')
        if m.get('expiredToReleasedHour') is not None:
            self.expired_to_released_hour = m.get('expiredToReleasedHour')
        if m.get('inBeta') is not None:
            self.in_beta = m.get('inBeta')
        if m.get('independent') is not None:
            self.independent = m.get('independent')
        if m.get('paidType') is not None:
            self.paid_type = m.get('paidType')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('quotaItems') is not None:
            self.quota_items = m.get('quotaItems')
        if m.get('specCodes') is not None:
            self.spec_codes = m.get('specCodes')
        return self


class QueryUsageResponseBodyDataCommoditySpecUsageInfosPurchasedCommoditySpecUsagesCommoditySpec(TeaModel):
    def __init__(self, application_num=None, commercialize_status=None, commodity_code=None, commodity_name=None,
                 cpu_num=None, expire_date=None, mem_num=None, next_buy_actions=None, ntm_commodity_instance_id=None,
                 open_date=None, related_sub_products=None, remaining_time=None, spec_code=None):
        self.application_num = application_num  # type: str
        self.commercialize_status = commercialize_status  # type: str
        self.commodity_code = commodity_code  # type: str
        self.commodity_name = commodity_name  # type: str
        self.cpu_num = cpu_num  # type: long
        self.expire_date = expire_date  # type: long
        self.mem_num = mem_num  # type: long
        self.next_buy_actions = next_buy_actions  # type: list[str]
        self.ntm_commodity_instance_id = ntm_commodity_instance_id  # type: str
        self.open_date = open_date  # type: long
        self.related_sub_products = related_sub_products  # type: list[str]
        self.remaining_time = remaining_time  # type: str
        self.spec_code = spec_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUsageResponseBodyDataCommoditySpecUsageInfosPurchasedCommoditySpecUsagesCommoditySpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_num is not None:
            result['applicationNum'] = self.application_num
        if self.commercialize_status is not None:
            result['commercializeStatus'] = self.commercialize_status
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.commodity_name is not None:
            result['commodityName'] = self.commodity_name
        if self.cpu_num is not None:
            result['cpuNum'] = self.cpu_num
        if self.expire_date is not None:
            result['expireDate'] = self.expire_date
        if self.mem_num is not None:
            result['memNum'] = self.mem_num
        if self.next_buy_actions is not None:
            result['nextBuyActions'] = self.next_buy_actions
        if self.ntm_commodity_instance_id is not None:
            result['ntmCommodityInstanceId'] = self.ntm_commodity_instance_id
        if self.open_date is not None:
            result['openDate'] = self.open_date
        if self.related_sub_products is not None:
            result['relatedSubProducts'] = self.related_sub_products
        if self.remaining_time is not None:
            result['remainingTime'] = self.remaining_time
        if self.spec_code is not None:
            result['specCode'] = self.spec_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applicationNum') is not None:
            self.application_num = m.get('applicationNum')
        if m.get('commercializeStatus') is not None:
            self.commercialize_status = m.get('commercializeStatus')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('commodityName') is not None:
            self.commodity_name = m.get('commodityName')
        if m.get('cpuNum') is not None:
            self.cpu_num = m.get('cpuNum')
        if m.get('expireDate') is not None:
            self.expire_date = m.get('expireDate')
        if m.get('memNum') is not None:
            self.mem_num = m.get('memNum')
        if m.get('nextBuyActions') is not None:
            self.next_buy_actions = m.get('nextBuyActions')
        if m.get('ntmCommodityInstanceId') is not None:
            self.ntm_commodity_instance_id = m.get('ntmCommodityInstanceId')
        if m.get('openDate') is not None:
            self.open_date = m.get('openDate')
        if m.get('relatedSubProducts') is not None:
            self.related_sub_products = m.get('relatedSubProducts')
        if m.get('remainingTime') is not None:
            self.remaining_time = m.get('remainingTime')
        if m.get('specCode') is not None:
            self.spec_code = m.get('specCode')
        return self


class QueryUsageResponseBodyDataCommoditySpecUsageInfosPurchasedCommoditySpecUsagesCommodityUsage(TeaModel):
    def __init__(self, application_num=None, cpu_num=None, mem_num=None):
        self.application_num = application_num  # type: long
        self.cpu_num = cpu_num  # type: long
        self.mem_num = mem_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUsageResponseBodyDataCommoditySpecUsageInfosPurchasedCommoditySpecUsagesCommodityUsage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_num is not None:
            result['applicationNum'] = self.application_num
        if self.cpu_num is not None:
            result['cpuNum'] = self.cpu_num
        if self.mem_num is not None:
            result['memNum'] = self.mem_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applicationNum') is not None:
            self.application_num = m.get('applicationNum')
        if m.get('cpuNum') is not None:
            self.cpu_num = m.get('cpuNum')
        if m.get('memNum') is not None:
            self.mem_num = m.get('memNum')
        return self


class QueryUsageResponseBodyDataCommoditySpecUsageInfosPurchasedCommoditySpecUsages(TeaModel):
    def __init__(self, commodity_spec=None, commodity_usage=None):
        self.commodity_spec = commodity_spec  # type: QueryUsageResponseBodyDataCommoditySpecUsageInfosPurchasedCommoditySpecUsagesCommoditySpec
        self.commodity_usage = commodity_usage  # type: QueryUsageResponseBodyDataCommoditySpecUsageInfosPurchasedCommoditySpecUsagesCommodityUsage

    def validate(self):
        if self.commodity_spec:
            self.commodity_spec.validate()
        if self.commodity_usage:
            self.commodity_usage.validate()

    def to_map(self):
        _map = super(QueryUsageResponseBodyDataCommoditySpecUsageInfosPurchasedCommoditySpecUsages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_spec is not None:
            result['commoditySpec'] = self.commodity_spec.to_map()
        if self.commodity_usage is not None:
            result['commodityUsage'] = self.commodity_usage.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commoditySpec') is not None:
            temp_model = QueryUsageResponseBodyDataCommoditySpecUsageInfosPurchasedCommoditySpecUsagesCommoditySpec()
            self.commodity_spec = temp_model.from_map(m['commoditySpec'])
        if m.get('commodityUsage') is not None:
            temp_model = QueryUsageResponseBodyDataCommoditySpecUsageInfosPurchasedCommoditySpecUsagesCommodityUsage()
            self.commodity_usage = temp_model.from_map(m['commodityUsage'])
        return self


class QueryUsageResponseBodyDataCommoditySpecUsageInfos(TeaModel):
    def __init__(self, commodity_config=None, purchased_commodity_spec_usages=None):
        self.commodity_config = commodity_config  # type: QueryUsageResponseBodyDataCommoditySpecUsageInfosCommodityConfig
        self.purchased_commodity_spec_usages = purchased_commodity_spec_usages  # type: list[QueryUsageResponseBodyDataCommoditySpecUsageInfosPurchasedCommoditySpecUsages]

    def validate(self):
        if self.commodity_config:
            self.commodity_config.validate()
        if self.purchased_commodity_spec_usages:
            for k in self.purchased_commodity_spec_usages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryUsageResponseBodyDataCommoditySpecUsageInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_config is not None:
            result['commodityConfig'] = self.commodity_config.to_map()
        result['purchasedCommoditySpecUsages'] = []
        if self.purchased_commodity_spec_usages is not None:
            for k in self.purchased_commodity_spec_usages:
                result['purchasedCommoditySpecUsages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commodityConfig') is not None:
            temp_model = QueryUsageResponseBodyDataCommoditySpecUsageInfosCommodityConfig()
            self.commodity_config = temp_model.from_map(m['commodityConfig'])
        self.purchased_commodity_spec_usages = []
        if m.get('purchasedCommoditySpecUsages') is not None:
            for k in m.get('purchasedCommoditySpecUsages'):
                temp_model = QueryUsageResponseBodyDataCommoditySpecUsageInfosPurchasedCommoditySpecUsages()
                self.purchased_commodity_spec_usages.append(temp_model.from_map(k))
        return self


class QueryUsageResponseBodyDataSubProductInfosSubProduct(TeaModel):
    def __init__(self, display=None, extend_properties=None, sub_product_code=None, sub_product_name=None,
                 sub_product_state=None):
        self.display = display  # type: bool
        self.extend_properties = extend_properties  # type: dict[str, any]
        self.sub_product_code = sub_product_code  # type: str
        self.sub_product_name = sub_product_name  # type: str
        self.sub_product_state = sub_product_state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUsageResponseBodyDataSubProductInfosSubProduct, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['display'] = self.display
        if self.extend_properties is not None:
            result['extendProperties'] = self.extend_properties
        if self.sub_product_code is not None:
            result['subProductCode'] = self.sub_product_code
        if self.sub_product_name is not None:
            result['subProductName'] = self.sub_product_name
        if self.sub_product_state is not None:
            result['subProductState'] = self.sub_product_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('extendProperties') is not None:
            self.extend_properties = m.get('extendProperties')
        if m.get('subProductCode') is not None:
            self.sub_product_code = m.get('subProductCode')
        if m.get('subProductName') is not None:
            self.sub_product_name = m.get('subProductName')
        if m.get('subProductState') is not None:
            self.sub_product_state = m.get('subProductState')
        return self


class QueryUsageResponseBodyDataSubProductInfosSubProductCommoditySpecsForGuideToBuyCommodityConfig(TeaModel):
    def __init__(self, beta_deadline_ms=None, commodity_code=None, commodity_name=None,
                 expired_to_released_hour=None, in_beta=None, independent=None, paid_type=None, product_code=None, quota_items=None,
                 spec_codes=None):
        self.beta_deadline_ms = beta_deadline_ms  # type: long
        self.commodity_code = commodity_code  # type: str
        self.commodity_name = commodity_name  # type: str
        self.expired_to_released_hour = expired_to_released_hour  # type: long
        self.in_beta = in_beta  # type: bool
        self.independent = independent  # type: bool
        self.paid_type = paid_type  # type: str
        self.product_code = product_code  # type: str
        self.quota_items = quota_items  # type: list[str]
        self.spec_codes = spec_codes  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUsageResponseBodyDataSubProductInfosSubProductCommoditySpecsForGuideToBuyCommodityConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.beta_deadline_ms is not None:
            result['betaDeadlineMs'] = self.beta_deadline_ms
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.commodity_name is not None:
            result['commodityName'] = self.commodity_name
        if self.expired_to_released_hour is not None:
            result['expiredToReleasedHour'] = self.expired_to_released_hour
        if self.in_beta is not None:
            result['inBeta'] = self.in_beta
        if self.independent is not None:
            result['independent'] = self.independent
        if self.paid_type is not None:
            result['paidType'] = self.paid_type
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.quota_items is not None:
            result['quotaItems'] = self.quota_items
        if self.spec_codes is not None:
            result['specCodes'] = self.spec_codes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('betaDeadlineMs') is not None:
            self.beta_deadline_ms = m.get('betaDeadlineMs')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('commodityName') is not None:
            self.commodity_name = m.get('commodityName')
        if m.get('expiredToReleasedHour') is not None:
            self.expired_to_released_hour = m.get('expiredToReleasedHour')
        if m.get('inBeta') is not None:
            self.in_beta = m.get('inBeta')
        if m.get('independent') is not None:
            self.independent = m.get('independent')
        if m.get('paidType') is not None:
            self.paid_type = m.get('paidType')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('quotaItems') is not None:
            self.quota_items = m.get('quotaItems')
        if m.get('specCodes') is not None:
            self.spec_codes = m.get('specCodes')
        return self


class QueryUsageResponseBodyDataSubProductInfosSubProductCommoditySpecsForGuideToBuyCommoditySpec(TeaModel):
    def __init__(self, application_num=None, commercialize_status=None, commodity_code=None, commodity_name=None,
                 cpu_num=None, expire_date=None, mem_num=None, next_buy_actions=None, ntm_commodity_instance_id=None,
                 open_date=None, related_sub_products=None, spec_code=None, spec_name=None):
        self.application_num = application_num  # type: long
        self.commercialize_status = commercialize_status  # type: str
        self.commodity_code = commodity_code  # type: str
        self.commodity_name = commodity_name  # type: str
        self.cpu_num = cpu_num  # type: long
        self.expire_date = expire_date  # type: long
        self.mem_num = mem_num  # type: long
        self.next_buy_actions = next_buy_actions  # type: str
        self.ntm_commodity_instance_id = ntm_commodity_instance_id  # type: str
        self.open_date = open_date  # type: long
        self.related_sub_products = related_sub_products  # type: list[str]
        self.spec_code = spec_code  # type: str
        self.spec_name = spec_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUsageResponseBodyDataSubProductInfosSubProductCommoditySpecsForGuideToBuyCommoditySpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_num is not None:
            result['applicationNum'] = self.application_num
        if self.commercialize_status is not None:
            result['commercializeStatus'] = self.commercialize_status
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.commodity_name is not None:
            result['commodityName'] = self.commodity_name
        if self.cpu_num is not None:
            result['cpuNum'] = self.cpu_num
        if self.expire_date is not None:
            result['expireDate'] = self.expire_date
        if self.mem_num is not None:
            result['memNum'] = self.mem_num
        if self.next_buy_actions is not None:
            result['nextBuyActions'] = self.next_buy_actions
        if self.ntm_commodity_instance_id is not None:
            result['ntmCommodityInstanceId'] = self.ntm_commodity_instance_id
        if self.open_date is not None:
            result['openDate'] = self.open_date
        if self.related_sub_products is not None:
            result['relatedSubProducts'] = self.related_sub_products
        if self.spec_code is not None:
            result['specCode'] = self.spec_code
        if self.spec_name is not None:
            result['specName'] = self.spec_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applicationNum') is not None:
            self.application_num = m.get('applicationNum')
        if m.get('commercializeStatus') is not None:
            self.commercialize_status = m.get('commercializeStatus')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('commodityName') is not None:
            self.commodity_name = m.get('commodityName')
        if m.get('cpuNum') is not None:
            self.cpu_num = m.get('cpuNum')
        if m.get('expireDate') is not None:
            self.expire_date = m.get('expireDate')
        if m.get('memNum') is not None:
            self.mem_num = m.get('memNum')
        if m.get('nextBuyActions') is not None:
            self.next_buy_actions = m.get('nextBuyActions')
        if m.get('ntmCommodityInstanceId') is not None:
            self.ntm_commodity_instance_id = m.get('ntmCommodityInstanceId')
        if m.get('openDate') is not None:
            self.open_date = m.get('openDate')
        if m.get('relatedSubProducts') is not None:
            self.related_sub_products = m.get('relatedSubProducts')
        if m.get('specCode') is not None:
            self.spec_code = m.get('specCode')
        if m.get('specName') is not None:
            self.spec_name = m.get('specName')
        return self


class QueryUsageResponseBodyDataSubProductInfosSubProductCommoditySpecsForGuideToBuy(TeaModel):
    def __init__(self, commodity_config=None, commodity_spec=None, release_time=None):
        self.commodity_config = commodity_config  # type: QueryUsageResponseBodyDataSubProductInfosSubProductCommoditySpecsForGuideToBuyCommodityConfig
        self.commodity_spec = commodity_spec  # type: QueryUsageResponseBodyDataSubProductInfosSubProductCommoditySpecsForGuideToBuyCommoditySpec
        self.release_time = release_time  # type: long

    def validate(self):
        if self.commodity_config:
            self.commodity_config.validate()
        if self.commodity_spec:
            self.commodity_spec.validate()

    def to_map(self):
        _map = super(QueryUsageResponseBodyDataSubProductInfosSubProductCommoditySpecsForGuideToBuy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_config is not None:
            result['commodityConfig'] = self.commodity_config.to_map()
        if self.commodity_spec is not None:
            result['commoditySpec'] = self.commodity_spec.to_map()
        if self.release_time is not None:
            result['releaseTime'] = self.release_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commodityConfig') is not None:
            temp_model = QueryUsageResponseBodyDataSubProductInfosSubProductCommoditySpecsForGuideToBuyCommodityConfig()
            self.commodity_config = temp_model.from_map(m['commodityConfig'])
        if m.get('commoditySpec') is not None:
            temp_model = QueryUsageResponseBodyDataSubProductInfosSubProductCommoditySpecsForGuideToBuyCommoditySpec()
            self.commodity_spec = temp_model.from_map(m['commoditySpec'])
        if m.get('releaseTime') is not None:
            self.release_time = m.get('releaseTime')
        return self


class QueryUsageResponseBodyDataSubProductInfos(TeaModel):
    def __init__(self, sub_product=None, sub_product_commodity_specs_for_guide_to_buy=None):
        self.sub_product = sub_product  # type: QueryUsageResponseBodyDataSubProductInfosSubProduct
        self.sub_product_commodity_specs_for_guide_to_buy = sub_product_commodity_specs_for_guide_to_buy  # type: list[QueryUsageResponseBodyDataSubProductInfosSubProductCommoditySpecsForGuideToBuy]

    def validate(self):
        if self.sub_product:
            self.sub_product.validate()
        if self.sub_product_commodity_specs_for_guide_to_buy:
            for k in self.sub_product_commodity_specs_for_guide_to_buy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryUsageResponseBodyDataSubProductInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_product is not None:
            result['subProduct'] = self.sub_product.to_map()
        result['subProductCommoditySpecsForGuideToBuy'] = []
        if self.sub_product_commodity_specs_for_guide_to_buy is not None:
            for k in self.sub_product_commodity_specs_for_guide_to_buy:
                result['subProductCommoditySpecsForGuideToBuy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('subProduct') is not None:
            temp_model = QueryUsageResponseBodyDataSubProductInfosSubProduct()
            self.sub_product = temp_model.from_map(m['subProduct'])
        self.sub_product_commodity_specs_for_guide_to_buy = []
        if m.get('subProductCommoditySpecsForGuideToBuy') is not None:
            for k in m.get('subProductCommoditySpecsForGuideToBuy'):
                temp_model = QueryUsageResponseBodyDataSubProductInfosSubProductCommoditySpecsForGuideToBuy()
                self.sub_product_commodity_specs_for_guide_to_buy.append(temp_model.from_map(k))
        return self


class QueryUsageResponseBodyData(TeaModel):
    def __init__(self, article_infos=None, commodity_spec_usage_infos=None, sub_product_infos=None):
        self.article_infos = article_infos  # type: list[QueryUsageResponseBodyDataArticleInfos]
        self.commodity_spec_usage_infos = commodity_spec_usage_infos  # type: list[QueryUsageResponseBodyDataCommoditySpecUsageInfos]
        self.sub_product_infos = sub_product_infos  # type: list[QueryUsageResponseBodyDataSubProductInfos]

    def validate(self):
        if self.article_infos:
            for k in self.article_infos:
                if k:
                    k.validate()
        if self.commodity_spec_usage_infos:
            for k in self.commodity_spec_usage_infos:
                if k:
                    k.validate()
        if self.sub_product_infos:
            for k in self.sub_product_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryUsageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['articleInfos'] = []
        if self.article_infos is not None:
            for k in self.article_infos:
                result['articleInfos'].append(k.to_map() if k else None)
        result['commoditySpecUsageInfos'] = []
        if self.commodity_spec_usage_infos is not None:
            for k in self.commodity_spec_usage_infos:
                result['commoditySpecUsageInfos'].append(k.to_map() if k else None)
        result['subProductInfos'] = []
        if self.sub_product_infos is not None:
            for k in self.sub_product_infos:
                result['subProductInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.article_infos = []
        if m.get('articleInfos') is not None:
            for k in m.get('articleInfos'):
                temp_model = QueryUsageResponseBodyDataArticleInfos()
                self.article_infos.append(temp_model.from_map(k))
        self.commodity_spec_usage_infos = []
        if m.get('commoditySpecUsageInfos') is not None:
            for k in m.get('commoditySpecUsageInfos'):
                temp_model = QueryUsageResponseBodyDataCommoditySpecUsageInfos()
                self.commodity_spec_usage_infos.append(temp_model.from_map(k))
        self.sub_product_infos = []
        if m.get('subProductInfos') is not None:
            for k in m.get('subProductInfos'):
                temp_model = QueryUsageResponseBodyDataSubProductInfos()
                self.sub_product_infos.append(temp_model.from_map(k))
        return self


class QueryUsageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: QueryUsageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryUsageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryUsageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryUsageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUsageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


