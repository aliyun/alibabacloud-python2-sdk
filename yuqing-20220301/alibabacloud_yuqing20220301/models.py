# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ProductInstance(TeaModel):
    def __init__(self, app_code=None, buyer_name=None, buyer_uid=None, channel=None, config=None, end=None,
                 instance_id=None, order_no=None, product_code=None, product_spec_code=None, start=None, tenant_name=None,
                 tenant_uid=None):
        # 应用码
        self.app_code = app_code  # type: str
        # 购买者名称
        self.buyer_name = buyer_name  # type: str
        # 购买者账号uid
        self.buyer_uid = buyer_uid  # type: str
        # 商业化渠道码
        self.channel = channel  # type: str
        # 购买配置信息
        self.config = config  # type: str
        # 生效结束时间
        self.end = end  # type: long
        # 实例id
        self.instance_id = instance_id  # type: str
        # 订单号，幂等使用
        self.order_no = order_no  # type: str
        # 产品码
        self.product_code = product_code  # type: str
        # 规格码
        self.product_spec_code = product_spec_code  # type: str
        # 生效开始时间
        self.start = start  # type: long
        # 租户名称
        self.tenant_name = tenant_name  # type: str
        # 租户uid
        self.tenant_uid = tenant_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProductInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['appCode'] = self.app_code
        if self.buyer_name is not None:
            result['buyerName'] = self.buyer_name
        if self.buyer_uid is not None:
            result['buyerUid'] = self.buyer_uid
        if self.channel is not None:
            result['channel'] = self.channel
        if self.config is not None:
            result['config'] = self.config
        if self.end is not None:
            result['end'] = self.end
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.order_no is not None:
            result['orderNo'] = self.order_no
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.product_spec_code is not None:
            result['productSpecCode'] = self.product_spec_code
        if self.start is not None:
            result['start'] = self.start
        if self.tenant_name is not None:
            result['tenantName'] = self.tenant_name
        if self.tenant_uid is not None:
            result['tenantUid'] = self.tenant_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appCode') is not None:
            self.app_code = m.get('appCode')
        if m.get('buyerName') is not None:
            self.buyer_name = m.get('buyerName')
        if m.get('buyerUid') is not None:
            self.buyer_uid = m.get('buyerUid')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('orderNo') is not None:
            self.order_no = m.get('orderNo')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('productSpecCode') is not None:
            self.product_spec_code = m.get('productSpecCode')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('tenantName') is not None:
            self.tenant_name = m.get('tenantName')
        if m.get('tenantUid') is not None:
            self.tenant_uid = m.get('tenantUid')
        return self


