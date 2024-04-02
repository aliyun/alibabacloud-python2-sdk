# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AuditItemSubmitRequestData(TeaModel):
    def __init__(self, custom_result=None, custom_risk_type=None, id=None):
        self.custom_result = custom_result  # type: str
        self.custom_risk_type = custom_risk_type  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuditItemSubmitRequestData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_result is not None:
            result['CustomResult'] = self.custom_result
        if self.custom_risk_type is not None:
            result['CustomRiskType'] = self.custom_risk_type
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomResult') is not None:
            self.custom_result = m.get('CustomResult')
        if m.get('CustomRiskType') is not None:
            self.custom_risk_type = m.get('CustomRiskType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class AuditItemSubmitRequest(TeaModel):
    def __init__(self, data=None):
        self.data = data  # type: list[AuditItemSubmitRequestData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AuditItemSubmitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AuditItemSubmitRequestData()
                self.data.append(temp_model.from_map(k))
        return self


class AuditItemSubmitResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuditItemSubmitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuditItemSubmitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AuditItemSubmitResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AuditItemSubmitResponse, self).to_map()
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
            temp_model = AuditItemSubmitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatCustomOcrTemplateRequest(TeaModel):
    def __init__(self, img_url=None, name=None, recognize_area=None, refer_area=None):
        self.img_url = img_url  # type: str
        self.name = name  # type: str
        self.recognize_area = recognize_area  # type: str
        self.refer_area = refer_area  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatCustomOcrTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.img_url is not None:
            result['ImgUrl'] = self.img_url
        if self.name is not None:
            result['Name'] = self.name
        if self.recognize_area is not None:
            result['RecognizeArea'] = self.recognize_area
        if self.refer_area is not None:
            result['ReferArea'] = self.refer_area
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImgUrl') is not None:
            self.img_url = m.get('ImgUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RecognizeArea') is not None:
            self.recognize_area = m.get('RecognizeArea')
        if m.get('ReferArea') is not None:
            self.refer_area = m.get('ReferArea')
        return self


class CreatCustomOcrTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatCustomOcrTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatCustomOcrTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatCustomOcrTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatCustomOcrTemplateResponse, self).to_map()
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
            temp_model = CreatCustomOcrTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuditCallbackRequest(TeaModel):
    def __init__(self, callback_suggestions=None, callback_types=None, crypt_type=None, name=None, url=None):
        self.callback_suggestions = callback_suggestions  # type: str
        self.callback_types = callback_types  # type: str
        self.crypt_type = crypt_type  # type: str
        self.name = name  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuditCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_suggestions is not None:
            result['CallbackSuggestions'] = self.callback_suggestions
        if self.callback_types is not None:
            result['CallbackTypes'] = self.callback_types
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.name is not None:
            result['Name'] = self.name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackSuggestions') is not None:
            self.callback_suggestions = m.get('CallbackSuggestions')
        if m.get('CallbackTypes') is not None:
            self.callback_types = m.get('CallbackTypes')
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateAuditCallbackResponseBody(TeaModel):
    def __init__(self, callback_suggestions=None, callback_types=None, create_time=None, crypt_type=None, id=None,
                 modified_time=None, name=None, request_id=None, seed=None, url=None):
        self.callback_suggestions = callback_suggestions  # type: list[str]
        self.callback_types = callback_types  # type: list[str]
        self.create_time = create_time  # type: str
        self.crypt_type = crypt_type  # type: str
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.seed = seed  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuditCallbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_suggestions is not None:
            result['CallbackSuggestions'] = self.callback_suggestions
        if self.callback_types is not None:
            result['CallbackTypes'] = self.callback_types
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.seed is not None:
            result['Seed'] = self.seed
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackSuggestions') is not None:
            self.callback_suggestions = m.get('CallbackSuggestions')
        if m.get('CallbackTypes') is not None:
            self.callback_types = m.get('CallbackTypes')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateAuditCallbackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAuditCallbackResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAuditCallbackResponse, self).to_map()
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
            temp_model = CreateAuditCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBizTypeRequest(TeaModel):
    def __init__(self, biz_type_import=None, biz_type_name=None, cite_template=None, description=None,
                 industry_info=None):
        self.biz_type_import = biz_type_import  # type: str
        self.biz_type_name = biz_type_name  # type: str
        self.cite_template = cite_template  # type: bool
        self.description = description  # type: str
        self.industry_info = industry_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBizTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_import is not None:
            result['BizTypeImport'] = self.biz_type_import
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.cite_template is not None:
            result['CiteTemplate'] = self.cite_template
        if self.description is not None:
            result['Description'] = self.description
        if self.industry_info is not None:
            result['IndustryInfo'] = self.industry_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeImport') is not None:
            self.biz_type_import = m.get('BizTypeImport')
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('CiteTemplate') is not None:
            self.cite_template = m.get('CiteTemplate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IndustryInfo') is not None:
            self.industry_info = m.get('IndustryInfo')
        return self


class CreateBizTypeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBizTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBizTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBizTypeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBizTypeResponse, self).to_map()
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
            temp_model = CreateBizTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCdiBagRequest(TeaModel):
    def __init__(self, client_token=None, commodity_code=None, flow_out_spec=None, order_num=None, order_type=None,
                 owner_id=None):
        self.client_token = client_token  # type: str
        self.commodity_code = commodity_code  # type: str
        self.flow_out_spec = flow_out_spec  # type: int
        self.order_num = order_num  # type: int
        self.order_type = order_type  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCdiBagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.flow_out_spec is not None:
            result['FlowOutSpec'] = self.flow_out_spec
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('FlowOutSpec') is not None:
            self.flow_out_spec = m.get('FlowOutSpec')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CreateCdiBagResponseBodyInstanceIds(TeaModel):
    def __init__(self, string=None):
        self.string = string  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCdiBagResponseBodyInstanceIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.string is not None:
            result['String'] = self.string
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')
        return self


class CreateCdiBagResponseBody(TeaModel):
    def __init__(self, code=None, instance_ids=None, message=None, order_id=None, request_id=None):
        self.code = code  # type: str
        self.instance_ids = instance_ids  # type: CreateCdiBagResponseBodyInstanceIds
        self.message = message  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super(CreateCdiBagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceIds') is not None:
            temp_model = CreateCdiBagResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCdiBagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCdiBagResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCdiBagResponse, self).to_map()
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
            temp_model = CreateCdiBagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCdiBaseBagRequest(TeaModel):
    def __init__(self, client_token=None, commodity_code=None, duration=None, flow_out_spec=None, order_type=None,
                 owner_id=None):
        self.client_token = client_token  # type: str
        self.commodity_code = commodity_code  # type: str
        self.duration = duration  # type: int
        self.flow_out_spec = flow_out_spec  # type: int
        self.order_type = order_type  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCdiBaseBagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.flow_out_spec is not None:
            result['FlowOutSpec'] = self.flow_out_spec
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FlowOutSpec') is not None:
            self.flow_out_spec = m.get('FlowOutSpec')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CreateCdiBaseBagResponseBody(TeaModel):
    def __init__(self, code=None, instance_id=None, message=None, order_id=None, request_id=None):
        self.code = code  # type: str
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCdiBaseBagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCdiBaseBagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCdiBaseBagResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCdiBaseBagResponse, self).to_map()
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
            temp_model = CreateCdiBaseBagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageLibRequest(TeaModel):
    def __init__(self, biz_types=None, category=None, enable=None, name=None, scene=None, service_module=None,
                 source_ip=None):
        self.biz_types = biz_types  # type: str
        self.category = category  # type: str
        self.enable = enable  # type: bool
        self.name = name  # type: str
        self.scene = scene  # type: str
        self.service_module = service_module  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageLibRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.category is not None:
            result['Category'] = self.category
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.name is not None:
            result['Name'] = self.name
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.service_module is not None:
            result['ServiceModule'] = self.service_module
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('ServiceModule') is not None:
            self.service_module = m.get('ServiceModule')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CreateImageLibResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageLibResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageLibResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateImageLibResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateImageLibResponse, self).to_map()
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
            temp_model = CreateImageLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeywordRequest(TeaModel):
    def __init__(self, keyword_lib_id=None, keywords=None, lang=None, source_ip=None):
        self.keyword_lib_id = keyword_lib_id  # type: long
        self.keywords = keywords  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKeywordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword_lib_id is not None:
            result['KeywordLibId'] = self.keyword_lib_id
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeywordLibId') is not None:
            self.keyword_lib_id = m.get('KeywordLibId')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CreateKeywordResponseBodyValidKeywordList(TeaModel):
    def __init__(self, id=None, keyword=None):
        self.id = id  # type: int
        self.keyword = keyword  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKeywordResponseBodyValidKeywordList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        return self


class CreateKeywordResponseBody(TeaModel):
    def __init__(self, invalid_keyword_list=None, request_id=None, success_count=None, valid_keyword_list=None):
        self.invalid_keyword_list = invalid_keyword_list  # type: list[str]
        self.request_id = request_id  # type: str
        self.success_count = success_count  # type: int
        self.valid_keyword_list = valid_keyword_list  # type: list[CreateKeywordResponseBodyValidKeywordList]

    def validate(self):
        if self.valid_keyword_list:
            for k in self.valid_keyword_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateKeywordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invalid_keyword_list is not None:
            result['InvalidKeywordList'] = self.invalid_keyword_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        result['validKeywordList'] = []
        if self.valid_keyword_list is not None:
            for k in self.valid_keyword_list:
                result['validKeywordList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InvalidKeywordList') is not None:
            self.invalid_keyword_list = m.get('InvalidKeywordList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        self.valid_keyword_list = []
        if m.get('validKeywordList') is not None:
            for k in m.get('validKeywordList'):
                temp_model = CreateKeywordResponseBodyValidKeywordList()
                self.valid_keyword_list.append(temp_model.from_map(k))
        return self


class CreateKeywordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateKeywordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateKeywordResponse, self).to_map()
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
            temp_model = CreateKeywordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeywordLibRequest(TeaModel):
    def __init__(self, biz_types=None, category=None, enable=None, lang=None, language=None, lib_type=None,
                 match_mode=None, name=None, resource_type=None, service_module=None, source_ip=None):
        self.biz_types = biz_types  # type: str
        self.category = category  # type: str
        self.enable = enable  # type: bool
        self.lang = lang  # type: str
        self.language = language  # type: str
        self.lib_type = lib_type  # type: str
        self.match_mode = match_mode  # type: str
        self.name = name  # type: str
        self.resource_type = resource_type  # type: str
        self.service_module = service_module  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKeywordLibRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.category is not None:
            result['Category'] = self.category
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.language is not None:
            result['Language'] = self.language
        if self.lib_type is not None:
            result['LibType'] = self.lib_type
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_module is not None:
            result['ServiceModule'] = self.service_module
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LibType') is not None:
            self.lib_type = m.get('LibType')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceModule') is not None:
            self.service_module = m.get('ServiceModule')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CreateKeywordLibResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateKeywordLibResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateKeywordLibResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateKeywordLibResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateKeywordLibResponse, self).to_map()
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
            temp_model = CreateKeywordLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWebSiteInstanceRequest(TeaModel):
    def __init__(self, client_token=None, duration=None, order_num=None, order_type=None, owner_id=None,
                 pricing_cycle=None):
        self.client_token = client_token  # type: str
        self.duration = duration  # type: int
        self.order_num = order_num  # type: int
        self.order_type = order_type  # type: str
        self.owner_id = owner_id  # type: long
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWebSiteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class CreateWebSiteInstanceResponseBodyInstanceIds(TeaModel):
    def __init__(self, string=None):
        self.string = string  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWebSiteInstanceResponseBodyInstanceIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.string is not None:
            result['String'] = self.string
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')
        return self


class CreateWebSiteInstanceResponseBody(TeaModel):
    def __init__(self, code=None, instance_ids=None, message=None, order_id=None, request_id=None):
        self.code = code  # type: str
        self.instance_ids = instance_ids  # type: CreateWebSiteInstanceResponseBodyInstanceIds
        self.message = message  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super(CreateWebSiteInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceIds') is not None:
            temp_model = CreateWebSiteInstanceResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWebSiteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateWebSiteInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWebSiteInstanceResponse, self).to_map()
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
            temp_model = CreateWebSiteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWebsiteIndexPageBaselineRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, source_ip=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWebsiteIndexPageBaselineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CreateWebsiteIndexPageBaselineResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWebsiteIndexPageBaselineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWebsiteIndexPageBaselineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateWebsiteIndexPageBaselineResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWebsiteIndexPageBaselineResponse, self).to_map()
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
            temp_model = CreateWebsiteIndexPageBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBizTypeRequest(TeaModel):
    def __init__(self, biz_type_name=None):
        self.biz_type_name = biz_type_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBizTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        return self


class DeleteBizTypeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBizTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBizTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBizTypeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBizTypeResponse, self).to_map()
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
            temp_model = DeleteBizTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomOcrTemplateRequest(TeaModel):
    def __init__(self, ids=None):
        self.ids = ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomOcrTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DeleteCustomOcrTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomOcrTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCustomOcrTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCustomOcrTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCustomOcrTemplateResponse, self).to_map()
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
            temp_model = DeleteCustomOcrTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageFromLibRequest(TeaModel):
    def __init__(self, ids=None, source_ip=None):
        self.ids = ids  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageFromLibRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteImageFromLibResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageFromLibResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImageFromLibResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteImageFromLibResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteImageFromLibResponse, self).to_map()
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
            temp_model = DeleteImageFromLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageLibRequest(TeaModel):
    def __init__(self, id=None, source_ip=None):
        self.id = id  # type: int
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageLibRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteImageLibResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageLibResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImageLibResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteImageLibResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteImageLibResponse, self).to_map()
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
            temp_model = DeleteImageLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeywordRequest(TeaModel):
    def __init__(self, ids=None, keyword_lib_id=None, keywords=None, lang=None, source_ip=None):
        self.ids = ids  # type: str
        self.keyword_lib_id = keyword_lib_id  # type: str
        self.keywords = keywords  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteKeywordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.keyword_lib_id is not None:
            result['KeywordLibId'] = self.keyword_lib_id
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('KeywordLibId') is not None:
            self.keyword_lib_id = m.get('KeywordLibId')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteKeywordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteKeywordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteKeywordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteKeywordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteKeywordResponse, self).to_map()
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
            temp_model = DeleteKeywordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeywordLibRequest(TeaModel):
    def __init__(self, id=None, lang=None, source_ip=None):
        self.id = id  # type: int
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteKeywordLibRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteKeywordLibResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteKeywordLibResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteKeywordLibResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteKeywordLibResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteKeywordLibResponse, self).to_map()
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
            temp_model = DeleteKeywordLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNotificationContactsRequest(TeaModel):
    def __init__(self, contact_types=None, lang=None, source_ip=None):
        self.contact_types = contact_types  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNotificationContactsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_types is not None:
            result['ContactTypes'] = self.contact_types
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactTypes') is not None:
            self.contact_types = m.get('ContactTypes')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteNotificationContactsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNotificationContactsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNotificationContactsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteNotificationContactsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNotificationContactsResponse, self).to_map()
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
            temp_model = DeleteNotificationContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppInfoRequest(TeaModel):
    def __init__(self, current_page=None, lang=None, page_size=None, platform=None, source_ip=None, total_count=None):
        self.current_page = current_page  # type: int
        self.lang = lang  # type: str
        self.page_size = page_size  # type: int
        self.platform = platform  # type: str
        self.source_ip = source_ip  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppInfoResponseBodyAppInfoListDebugPackageInfo(TeaModel):
    def __init__(self, version=None):
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppInfoResponseBodyAppInfoListDebugPackageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAppInfoResponseBodyAppInfoListPackageInfo(TeaModel):
    def __init__(self, version=None):
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppInfoResponseBodyAppInfoListPackageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAppInfoResponseBodyAppInfoList(TeaModel):
    def __init__(self, debug_package_info=None, end_date=None, icon=None, id=None, name=None, package_info=None,
                 package_name=None, start_date=None, type=None):
        self.debug_package_info = debug_package_info  # type: DescribeAppInfoResponseBodyAppInfoListDebugPackageInfo
        self.end_date = end_date  # type: str
        self.icon = icon  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.package_info = package_info  # type: DescribeAppInfoResponseBodyAppInfoListPackageInfo
        self.package_name = package_name  # type: str
        self.start_date = start_date  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.debug_package_info:
            self.debug_package_info.validate()
        if self.package_info:
            self.package_info.validate()

    def to_map(self):
        _map = super(DescribeAppInfoResponseBodyAppInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug_package_info is not None:
            result['DebugPackageInfo'] = self.debug_package_info.to_map()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.package_info is not None:
            result['PackageInfo'] = self.package_info.to_map()
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DebugPackageInfo') is not None:
            temp_model = DescribeAppInfoResponseBodyAppInfoListDebugPackageInfo()
            self.debug_package_info = temp_model.from_map(m['DebugPackageInfo'])
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageInfo') is not None:
            temp_model = DescribeAppInfoResponseBodyAppInfoListPackageInfo()
            self.package_info = temp_model.from_map(m['PackageInfo'])
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAppInfoResponseBody(TeaModel):
    def __init__(self, app_info_list=None, current_page=None, page_size=None, request_id=None, total_count=None):
        self.app_info_list = app_info_list  # type: list[DescribeAppInfoResponseBodyAppInfoList]
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.app_info_list:
            for k in self.app_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAppInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k in m.get('AppInfoList'):
                temp_model = DescribeAppInfoResponseBodyAppInfoList()
                self.app_info_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppInfoResponse, self).to_map()
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
            temp_model = DescribeAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditCallbackResponseBody(TeaModel):
    def __init__(self, callback=None, crypt_type=None, request_id=None, seed=None):
        self.callback = callback  # type: str
        self.crypt_type = crypt_type  # type: int
        self.request_id = request_id  # type: str
        self.seed = seed  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditCallbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.seed is not None:
            result['Seed'] = self.seed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        return self


class DescribeAuditCallbackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAuditCallbackResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAuditCallbackResponse, self).to_map()
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
            temp_model = DescribeAuditCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditCallbackListResponseBodyCallbackList(TeaModel):
    def __init__(self, callback_suggestions=None, callback_types=None, create_time=None, crypt_type=None, id=None,
                 modified_time=None, name=None, seed=None, url=None):
        self.callback_suggestions = callback_suggestions  # type: list[str]
        self.callback_types = callback_types  # type: list[str]
        self.create_time = create_time  # type: str
        self.crypt_type = crypt_type  # type: str
        self.id = id  # type: long
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.seed = seed  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditCallbackListResponseBodyCallbackList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_suggestions is not None:
            result['CallbackSuggestions'] = self.callback_suggestions
        if self.callback_types is not None:
            result['CallbackTypes'] = self.callback_types
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.seed is not None:
            result['Seed'] = self.seed
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackSuggestions') is not None:
            self.callback_suggestions = m.get('CallbackSuggestions')
        if m.get('CallbackTypes') is not None:
            self.callback_types = m.get('CallbackTypes')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeAuditCallbackListResponseBody(TeaModel):
    def __init__(self, callback_list=None, request_id=None, total_count=None):
        self.callback_list = callback_list  # type: list[DescribeAuditCallbackListResponseBodyCallbackList]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.callback_list:
            for k in self.callback_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAuditCallbackListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CallbackList'] = []
        if self.callback_list is not None:
            for k in self.callback_list:
                result['CallbackList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.callback_list = []
        if m.get('CallbackList') is not None:
            for k in m.get('CallbackList'):
                temp_model = DescribeAuditCallbackListResponseBodyCallbackList()
                self.callback_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAuditCallbackListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAuditCallbackListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAuditCallbackListResponse, self).to_map()
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
            temp_model = DescribeAuditCallbackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditContentRequest(TeaModel):
    def __init__(self, audit_result=None, biz_type=None, current_page=None, data_id=None, end_date=None,
                 image_id=None, keyword_id=None, label=None, lang=None, lib_type=None, page_size=None, resource_type=None,
                 scene=None, source_ip=None, start_date=None, suggestion=None, task_id=None, total_count=None):
        self.audit_result = audit_result  # type: str
        self.biz_type = biz_type  # type: str
        self.current_page = current_page  # type: int
        self.data_id = data_id  # type: str
        self.end_date = end_date  # type: str
        self.image_id = image_id  # type: str
        self.keyword_id = keyword_id  # type: str
        self.label = label  # type: str
        self.lang = lang  # type: str
        self.lib_type = lib_type  # type: str
        self.page_size = page_size  # type: int
        self.resource_type = resource_type  # type: str
        self.scene = scene  # type: str
        self.source_ip = source_ip  # type: str
        self.start_date = start_date  # type: str
        self.suggestion = suggestion  # type: str
        self.task_id = task_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.keyword_id is not None:
            result['KeywordId'] = self.keyword_id
        if self.label is not None:
            result['Label'] = self.label
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.lib_type is not None:
            result['LibType'] = self.lib_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('KeywordId') is not None:
            self.keyword_id = m.get('KeywordId')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LibType') is not None:
            self.lib_type = m.get('LibType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAuditContentResponseBodyAuditContentListFrameResults(TeaModel):
    def __init__(self, label=None, offset=None, url=None):
        self.label = label  # type: str
        self.offset = offset  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditContentResponseBodyAuditContentListFrameResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeAuditContentResponseBodyAuditContentListResults(TeaModel):
    def __init__(self, label=None, scene=None, suggestion=None):
        self.label = label  # type: str
        self.scene = scene  # type: str
        self.suggestion = suggestion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditContentResponseBodyAuditContentListResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class DescribeAuditContentResponseBodyAuditContentList(TeaModel):
    def __init__(self, audit=None, audit_illegal_reasons=None, audit_result=None, biz_type=None, content=None,
                 data_id=None, frame_results=None, id=None, new_url=None, request_time=None, results=None,
                 scan_finished_time=None, suggestion=None, task_id=None, thumbnail=None, url=None):
        self.audit = audit  # type: int
        self.audit_illegal_reasons = audit_illegal_reasons  # type: list[str]
        self.audit_result = audit_result  # type: str
        self.biz_type = biz_type  # type: str
        self.content = content  # type: str
        self.data_id = data_id  # type: str
        self.frame_results = frame_results  # type: list[DescribeAuditContentResponseBodyAuditContentListFrameResults]
        self.id = id  # type: long
        self.new_url = new_url  # type: str
        self.request_time = request_time  # type: str
        self.results = results  # type: list[DescribeAuditContentResponseBodyAuditContentListResults]
        self.scan_finished_time = scan_finished_time  # type: str
        self.suggestion = suggestion  # type: str
        self.task_id = task_id  # type: str
        self.thumbnail = thumbnail  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.frame_results:
            for k in self.frame_results:
                if k:
                    k.validate()
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAuditContentResponseBodyAuditContentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit is not None:
            result['Audit'] = self.audit
        if self.audit_illegal_reasons is not None:
            result['AuditIllegalReasons'] = self.audit_illegal_reasons
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.content is not None:
            result['Content'] = self.content
        if self.data_id is not None:
            result['DataId'] = self.data_id
        result['FrameResults'] = []
        if self.frame_results is not None:
            for k in self.frame_results:
                result['FrameResults'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.new_url is not None:
            result['NewUrl'] = self.new_url
        if self.request_time is not None:
            result['RequestTime'] = self.request_time
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.scan_finished_time is not None:
            result['ScanFinishedTime'] = self.scan_finished_time
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Audit') is not None:
            self.audit = m.get('Audit')
        if m.get('AuditIllegalReasons') is not None:
            self.audit_illegal_reasons = m.get('AuditIllegalReasons')
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        self.frame_results = []
        if m.get('FrameResults') is not None:
            for k in m.get('FrameResults'):
                temp_model = DescribeAuditContentResponseBodyAuditContentListFrameResults()
                self.frame_results.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NewUrl') is not None:
            self.new_url = m.get('NewUrl')
        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DescribeAuditContentResponseBodyAuditContentListResults()
                self.results.append(temp_model.from_map(k))
        if m.get('ScanFinishedTime') is not None:
            self.scan_finished_time = m.get('ScanFinishedTime')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeAuditContentResponseBody(TeaModel):
    def __init__(self, audit_content_list=None, current_page=None, page_size=None, request_id=None,
                 total_count=None):
        self.audit_content_list = audit_content_list  # type: list[DescribeAuditContentResponseBodyAuditContentList]
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.audit_content_list:
            for k in self.audit_content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAuditContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuditContentList'] = []
        if self.audit_content_list is not None:
            for k in self.audit_content_list:
                result['AuditContentList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.audit_content_list = []
        if m.get('AuditContentList') is not None:
            for k in m.get('AuditContentList'):
                temp_model = DescribeAuditContentResponseBodyAuditContentList()
                self.audit_content_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAuditContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAuditContentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAuditContentResponse, self).to_map()
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
            temp_model = DescribeAuditContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditContentItemRequest(TeaModel):
    def __init__(self, current_page=None, lang=None, page_size=None, resource_type=None, source_ip=None,
                 task_id=None, total_count=None):
        self.current_page = current_page  # type: int
        self.lang = lang  # type: str
        self.page_size = page_size  # type: int
        self.resource_type = resource_type  # type: str
        self.source_ip = source_ip  # type: str
        self.task_id = task_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditContentItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAuditContentItemResponseBodyAuditContentItemList(TeaModel):
    def __init__(self, audit=None, audit_illegal_reasons=None, audit_result=None, content=None, end_time=None,
                 id=None, parent_task_id=None, sn=None, start_time=None, suggestion=None):
        self.audit = audit  # type: int
        self.audit_illegal_reasons = audit_illegal_reasons  # type: list[str]
        self.audit_result = audit_result  # type: str
        self.content = content  # type: str
        self.end_time = end_time  # type: str
        self.id = id  # type: long
        self.parent_task_id = parent_task_id  # type: str
        self.sn = sn  # type: int
        self.start_time = start_time  # type: str
        self.suggestion = suggestion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditContentItemResponseBodyAuditContentItemList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit is not None:
            result['Audit'] = self.audit
        if self.audit_illegal_reasons is not None:
            result['AuditIllegalReasons'] = self.audit_illegal_reasons
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.content is not None:
            result['Content'] = self.content
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Audit') is not None:
            self.audit = m.get('Audit')
        if m.get('AuditIllegalReasons') is not None:
            self.audit_illegal_reasons = m.get('AuditIllegalReasons')
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class DescribeAuditContentItemResponseBody(TeaModel):
    def __init__(self, audit_content_item_list=None, current_page=None, page_size=None, request_id=None,
                 total_count=None):
        self.audit_content_item_list = audit_content_item_list  # type: list[DescribeAuditContentItemResponseBodyAuditContentItemList]
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.audit_content_item_list:
            for k in self.audit_content_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAuditContentItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuditContentItemList'] = []
        if self.audit_content_item_list is not None:
            for k in self.audit_content_item_list:
                result['AuditContentItemList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.audit_content_item_list = []
        if m.get('AuditContentItemList') is not None:
            for k in m.get('AuditContentItemList'):
                temp_model = DescribeAuditContentItemResponseBodyAuditContentItemList()
                self.audit_content_item_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAuditContentItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAuditContentItemResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAuditContentItemResponse, self).to_map()
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
            temp_model = DescribeAuditContentItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditRangeResponseBodyAuditRange(TeaModel):
    def __init__(self, block=None, pass_=None, review=None):
        self.block = block  # type: bool
        self.pass_ = pass_  # type: bool
        self.review = review  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditRangeResponseBodyAuditRange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['block'] = self.block
        if self.pass_ is not None:
            result['pass'] = self.pass_
        if self.review is not None:
            result['review'] = self.review
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('block') is not None:
            self.block = m.get('block')
        if m.get('pass') is not None:
            self.pass_ = m.get('pass')
        if m.get('review') is not None:
            self.review = m.get('review')
        return self


class DescribeAuditRangeResponseBody(TeaModel):
    def __init__(self, audit_range=None, request_id=None):
        self.audit_range = audit_range  # type: DescribeAuditRangeResponseBodyAuditRange
        self.request_id = request_id  # type: str

    def validate(self):
        if self.audit_range:
            self.audit_range.validate()

    def to_map(self):
        _map = super(DescribeAuditRangeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_range is not None:
            result['AuditRange'] = self.audit_range.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditRange') is not None:
            temp_model = DescribeAuditRangeResponseBodyAuditRange()
            self.audit_range = temp_model.from_map(m['AuditRange'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAuditRangeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAuditRangeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAuditRangeResponse, self).to_map()
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
            temp_model = DescribeAuditRangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditSettingRequest(TeaModel):
    def __init__(self, lang=None, source_ip=None):
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeAuditSettingResponseBodyAuditRange(TeaModel):
    def __init__(self, block=None, pass_=None, review=None):
        self.block = block  # type: bool
        self.pass_ = pass_  # type: bool
        self.review = review  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditSettingResponseBodyAuditRange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['block'] = self.block
        if self.pass_ is not None:
            result['pass'] = self.pass_
        if self.review is not None:
            result['review'] = self.review
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('block') is not None:
            self.block = m.get('block')
        if m.get('pass') is not None:
            self.pass_ = m.get('pass')
        if m.get('review') is not None:
            self.review = m.get('review')
        return self


class DescribeAuditSettingResponseBody(TeaModel):
    def __init__(self, audit_range=None, callback=None, request_id=None, seed=None):
        self.audit_range = audit_range  # type: DescribeAuditSettingResponseBodyAuditRange
        self.callback = callback  # type: str
        self.request_id = request_id  # type: str
        self.seed = seed  # type: str

    def validate(self):
        if self.audit_range:
            self.audit_range.validate()

    def to_map(self):
        _map = super(DescribeAuditSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_range is not None:
            result['AuditRange'] = self.audit_range.to_map()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.seed is not None:
            result['Seed'] = self.seed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditRange') is not None:
            temp_model = DescribeAuditSettingResponseBodyAuditRange()
            self.audit_range = temp_model.from_map(m['AuditRange'])
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        return self


class DescribeAuditSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAuditSettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAuditSettingResponse, self).to_map()
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
            temp_model = DescribeAuditSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBizTypeImageLibRequest(TeaModel):
    def __init__(self, biz_type_name=None, resource_type=None, scene=None):
        self.biz_type_name = biz_type_name  # type: str
        self.resource_type = resource_type  # type: str
        self.scene = scene  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeImageLibRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class DescribeBizTypeImageLibResponseBodyBlackAll(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeImageLibResponseBodyBlackAll, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeImageLibResponseBodyBlackSelected(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeImageLibResponseBodyBlackSelected, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeImageLibResponseBodyBlack(TeaModel):
    def __init__(self, all=None, selected=None):
        self.all = all  # type: list[DescribeBizTypeImageLibResponseBodyBlackAll]
        self.selected = selected  # type: list[DescribeBizTypeImageLibResponseBodyBlackSelected]

    def validate(self):
        if self.all:
            for k in self.all:
                if k:
                    k.validate()
        if self.selected:
            for k in self.selected:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBizTypeImageLibResponseBodyBlack, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['All'] = []
        if self.all is not None:
            for k in self.all:
                result['All'].append(k.to_map() if k else None)
        result['Selected'] = []
        if self.selected is not None:
            for k in self.selected:
                result['Selected'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.all = []
        if m.get('All') is not None:
            for k in m.get('All'):
                temp_model = DescribeBizTypeImageLibResponseBodyBlackAll()
                self.all.append(temp_model.from_map(k))
        self.selected = []
        if m.get('Selected') is not None:
            for k in m.get('Selected'):
                temp_model = DescribeBizTypeImageLibResponseBodyBlackSelected()
                self.selected.append(temp_model.from_map(k))
        return self


class DescribeBizTypeImageLibResponseBodyReviewAll(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeImageLibResponseBodyReviewAll, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeImageLibResponseBodyReviewSelected(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeImageLibResponseBodyReviewSelected, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeImageLibResponseBodyReview(TeaModel):
    def __init__(self, all=None, selected=None):
        self.all = all  # type: list[DescribeBizTypeImageLibResponseBodyReviewAll]
        self.selected = selected  # type: list[DescribeBizTypeImageLibResponseBodyReviewSelected]

    def validate(self):
        if self.all:
            for k in self.all:
                if k:
                    k.validate()
        if self.selected:
            for k in self.selected:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBizTypeImageLibResponseBodyReview, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['All'] = []
        if self.all is not None:
            for k in self.all:
                result['All'].append(k.to_map() if k else None)
        result['Selected'] = []
        if self.selected is not None:
            for k in self.selected:
                result['Selected'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.all = []
        if m.get('All') is not None:
            for k in m.get('All'):
                temp_model = DescribeBizTypeImageLibResponseBodyReviewAll()
                self.all.append(temp_model.from_map(k))
        self.selected = []
        if m.get('Selected') is not None:
            for k in m.get('Selected'):
                temp_model = DescribeBizTypeImageLibResponseBodyReviewSelected()
                self.selected.append(temp_model.from_map(k))
        return self


class DescribeBizTypeImageLibResponseBodyWhiteAll(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeImageLibResponseBodyWhiteAll, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeImageLibResponseBodyWhiteSelected(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeImageLibResponseBodyWhiteSelected, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeImageLibResponseBodyWhite(TeaModel):
    def __init__(self, all=None, selected=None):
        self.all = all  # type: list[DescribeBizTypeImageLibResponseBodyWhiteAll]
        self.selected = selected  # type: list[DescribeBizTypeImageLibResponseBodyWhiteSelected]

    def validate(self):
        if self.all:
            for k in self.all:
                if k:
                    k.validate()
        if self.selected:
            for k in self.selected:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBizTypeImageLibResponseBodyWhite, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['All'] = []
        if self.all is not None:
            for k in self.all:
                result['All'].append(k.to_map() if k else None)
        result['Selected'] = []
        if self.selected is not None:
            for k in self.selected:
                result['Selected'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.all = []
        if m.get('All') is not None:
            for k in m.get('All'):
                temp_model = DescribeBizTypeImageLibResponseBodyWhiteAll()
                self.all.append(temp_model.from_map(k))
        self.selected = []
        if m.get('Selected') is not None:
            for k in m.get('Selected'):
                temp_model = DescribeBizTypeImageLibResponseBodyWhiteSelected()
                self.selected.append(temp_model.from_map(k))
        return self


class DescribeBizTypeImageLibResponseBody(TeaModel):
    def __init__(self, black=None, request_id=None, review=None, white=None):
        self.black = black  # type: DescribeBizTypeImageLibResponseBodyBlack
        self.request_id = request_id  # type: str
        self.review = review  # type: DescribeBizTypeImageLibResponseBodyReview
        self.white = white  # type: DescribeBizTypeImageLibResponseBodyWhite

    def validate(self):
        if self.black:
            self.black.validate()
        if self.review:
            self.review.validate()
        if self.white:
            self.white.validate()

    def to_map(self):
        _map = super(DescribeBizTypeImageLibResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black is not None:
            result['Black'] = self.black.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.review is not None:
            result['Review'] = self.review.to_map()
        if self.white is not None:
            result['White'] = self.white.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Black') is not None:
            temp_model = DescribeBizTypeImageLibResponseBodyBlack()
            self.black = temp_model.from_map(m['Black'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Review') is not None:
            temp_model = DescribeBizTypeImageLibResponseBodyReview()
            self.review = temp_model.from_map(m['Review'])
        if m.get('White') is not None:
            temp_model = DescribeBizTypeImageLibResponseBodyWhite()
            self.white = temp_model.from_map(m['White'])
        return self


class DescribeBizTypeImageLibResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBizTypeImageLibResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBizTypeImageLibResponse, self).to_map()
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
            temp_model = DescribeBizTypeImageLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBizTypeSettingRequest(TeaModel):
    def __init__(self, biz_type_name=None, resource_type=None):
        self.biz_type_name = biz_type_name  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeBizTypeSettingResponseBodyAd(TeaModel):
    def __init__(self, categories=None):
        self.categories = categories  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeSettingResponseBodyAd, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeBizTypeSettingResponseBodyAntispam(TeaModel):
    def __init__(self, categories=None):
        self.categories = categories  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeSettingResponseBodyAntispam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeBizTypeSettingResponseBodyLive(TeaModel):
    def __init__(self, categories=None):
        self.categories = categories  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeSettingResponseBodyLive, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeBizTypeSettingResponseBodyPorn(TeaModel):
    def __init__(self, categories=None):
        self.categories = categories  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeSettingResponseBodyPorn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeBizTypeSettingResponseBodyTerrorism(TeaModel):
    def __init__(self, categories=None):
        self.categories = categories  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeSettingResponseBodyTerrorism, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeBizTypeSettingResponseBody(TeaModel):
    def __init__(self, ad=None, antispam=None, live=None, porn=None, request_id=None, terrorism=None):
        self.ad = ad  # type: DescribeBizTypeSettingResponseBodyAd
        self.antispam = antispam  # type: DescribeBizTypeSettingResponseBodyAntispam
        self.live = live  # type: DescribeBizTypeSettingResponseBodyLive
        self.porn = porn  # type: DescribeBizTypeSettingResponseBodyPorn
        self.request_id = request_id  # type: str
        self.terrorism = terrorism  # type: DescribeBizTypeSettingResponseBodyTerrorism

    def validate(self):
        if self.ad:
            self.ad.validate()
        if self.antispam:
            self.antispam.validate()
        if self.live:
            self.live.validate()
        if self.porn:
            self.porn.validate()
        if self.terrorism:
            self.terrorism.validate()

    def to_map(self):
        _map = super(DescribeBizTypeSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad is not None:
            result['Ad'] = self.ad.to_map()
        if self.antispam is not None:
            result['Antispam'] = self.antispam.to_map()
        if self.live is not None:
            result['Live'] = self.live.to_map()
        if self.porn is not None:
            result['Porn'] = self.porn.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.terrorism is not None:
            result['Terrorism'] = self.terrorism.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ad') is not None:
            temp_model = DescribeBizTypeSettingResponseBodyAd()
            self.ad = temp_model.from_map(m['Ad'])
        if m.get('Antispam') is not None:
            temp_model = DescribeBizTypeSettingResponseBodyAntispam()
            self.antispam = temp_model.from_map(m['Antispam'])
        if m.get('Live') is not None:
            temp_model = DescribeBizTypeSettingResponseBodyLive()
            self.live = temp_model.from_map(m['Live'])
        if m.get('Porn') is not None:
            temp_model = DescribeBizTypeSettingResponseBodyPorn()
            self.porn = temp_model.from_map(m['Porn'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Terrorism') is not None:
            temp_model = DescribeBizTypeSettingResponseBodyTerrorism()
            self.terrorism = temp_model.from_map(m['Terrorism'])
        return self


class DescribeBizTypeSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBizTypeSettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBizTypeSettingResponse, self).to_map()
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
            temp_model = DescribeBizTypeSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBizTypeTextLibRequest(TeaModel):
    def __init__(self, biz_type_name=None, resource_type=None, scene=None):
        self.biz_type_name = biz_type_name  # type: str
        self.resource_type = resource_type  # type: str
        self.scene = scene  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeTextLibRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class DescribeBizTypeTextLibResponseBodyBlackAll(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeTextLibResponseBodyBlackAll, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyBlackSelected(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeTextLibResponseBodyBlackSelected, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyBlack(TeaModel):
    def __init__(self, all=None, selected=None):
        self.all = all  # type: list[DescribeBizTypeTextLibResponseBodyBlackAll]
        self.selected = selected  # type: list[DescribeBizTypeTextLibResponseBodyBlackSelected]

    def validate(self):
        if self.all:
            for k in self.all:
                if k:
                    k.validate()
        if self.selected:
            for k in self.selected:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBizTypeTextLibResponseBodyBlack, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['All'] = []
        if self.all is not None:
            for k in self.all:
                result['All'].append(k.to_map() if k else None)
        result['Selected'] = []
        if self.selected is not None:
            for k in self.selected:
                result['Selected'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.all = []
        if m.get('All') is not None:
            for k in m.get('All'):
                temp_model = DescribeBizTypeTextLibResponseBodyBlackAll()
                self.all.append(temp_model.from_map(k))
        self.selected = []
        if m.get('Selected') is not None:
            for k in m.get('Selected'):
                temp_model = DescribeBizTypeTextLibResponseBodyBlackSelected()
                self.selected.append(temp_model.from_map(k))
        return self


class DescribeBizTypeTextLibResponseBodyIgnoreAll(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeTextLibResponseBodyIgnoreAll, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyIgnoreSelected(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeTextLibResponseBodyIgnoreSelected, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyIgnore(TeaModel):
    def __init__(self, all=None, selected=None):
        self.all = all  # type: list[DescribeBizTypeTextLibResponseBodyIgnoreAll]
        self.selected = selected  # type: list[DescribeBizTypeTextLibResponseBodyIgnoreSelected]

    def validate(self):
        if self.all:
            for k in self.all:
                if k:
                    k.validate()
        if self.selected:
            for k in self.selected:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBizTypeTextLibResponseBodyIgnore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['All'] = []
        if self.all is not None:
            for k in self.all:
                result['All'].append(k.to_map() if k else None)
        result['Selected'] = []
        if self.selected is not None:
            for k in self.selected:
                result['Selected'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.all = []
        if m.get('All') is not None:
            for k in m.get('All'):
                temp_model = DescribeBizTypeTextLibResponseBodyIgnoreAll()
                self.all.append(temp_model.from_map(k))
        self.selected = []
        if m.get('Selected') is not None:
            for k in m.get('Selected'):
                temp_model = DescribeBizTypeTextLibResponseBodyIgnoreSelected()
                self.selected.append(temp_model.from_map(k))
        return self


class DescribeBizTypeTextLibResponseBodyReviewAll(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeTextLibResponseBodyReviewAll, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyReviewSelected(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeTextLibResponseBodyReviewSelected, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyReview(TeaModel):
    def __init__(self, all=None, selected=None):
        self.all = all  # type: list[DescribeBizTypeTextLibResponseBodyReviewAll]
        self.selected = selected  # type: list[DescribeBizTypeTextLibResponseBodyReviewSelected]

    def validate(self):
        if self.all:
            for k in self.all:
                if k:
                    k.validate()
        if self.selected:
            for k in self.selected:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBizTypeTextLibResponseBodyReview, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['All'] = []
        if self.all is not None:
            for k in self.all:
                result['All'].append(k.to_map() if k else None)
        result['Selected'] = []
        if self.selected is not None:
            for k in self.selected:
                result['Selected'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.all = []
        if m.get('All') is not None:
            for k in m.get('All'):
                temp_model = DescribeBizTypeTextLibResponseBodyReviewAll()
                self.all.append(temp_model.from_map(k))
        self.selected = []
        if m.get('Selected') is not None:
            for k in m.get('Selected'):
                temp_model = DescribeBizTypeTextLibResponseBodyReviewSelected()
                self.selected.append(temp_model.from_map(k))
        return self


class DescribeBizTypeTextLibResponseBodyWhiteAll(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeTextLibResponseBodyWhiteAll, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyWhiteSelected(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypeTextLibResponseBodyWhiteSelected, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyWhite(TeaModel):
    def __init__(self, all=None, selected=None):
        self.all = all  # type: list[DescribeBizTypeTextLibResponseBodyWhiteAll]
        self.selected = selected  # type: list[DescribeBizTypeTextLibResponseBodyWhiteSelected]

    def validate(self):
        if self.all:
            for k in self.all:
                if k:
                    k.validate()
        if self.selected:
            for k in self.selected:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBizTypeTextLibResponseBodyWhite, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['All'] = []
        if self.all is not None:
            for k in self.all:
                result['All'].append(k.to_map() if k else None)
        result['Selected'] = []
        if self.selected is not None:
            for k in self.selected:
                result['Selected'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.all = []
        if m.get('All') is not None:
            for k in m.get('All'):
                temp_model = DescribeBizTypeTextLibResponseBodyWhiteAll()
                self.all.append(temp_model.from_map(k))
        self.selected = []
        if m.get('Selected') is not None:
            for k in m.get('Selected'):
                temp_model = DescribeBizTypeTextLibResponseBodyWhiteSelected()
                self.selected.append(temp_model.from_map(k))
        return self


class DescribeBizTypeTextLibResponseBody(TeaModel):
    def __init__(self, black=None, ignore=None, request_id=None, review=None, white=None):
        self.black = black  # type: DescribeBizTypeTextLibResponseBodyBlack
        self.ignore = ignore  # type: DescribeBizTypeTextLibResponseBodyIgnore
        self.request_id = request_id  # type: str
        self.review = review  # type: DescribeBizTypeTextLibResponseBodyReview
        self.white = white  # type: DescribeBizTypeTextLibResponseBodyWhite

    def validate(self):
        if self.black:
            self.black.validate()
        if self.ignore:
            self.ignore.validate()
        if self.review:
            self.review.validate()
        if self.white:
            self.white.validate()

    def to_map(self):
        _map = super(DescribeBizTypeTextLibResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black is not None:
            result['Black'] = self.black.to_map()
        if self.ignore is not None:
            result['Ignore'] = self.ignore.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.review is not None:
            result['Review'] = self.review.to_map()
        if self.white is not None:
            result['White'] = self.white.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Black') is not None:
            temp_model = DescribeBizTypeTextLibResponseBodyBlack()
            self.black = temp_model.from_map(m['Black'])
        if m.get('Ignore') is not None:
            temp_model = DescribeBizTypeTextLibResponseBodyIgnore()
            self.ignore = temp_model.from_map(m['Ignore'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Review') is not None:
            temp_model = DescribeBizTypeTextLibResponseBodyReview()
            self.review = temp_model.from_map(m['Review'])
        if m.get('White') is not None:
            temp_model = DescribeBizTypeTextLibResponseBodyWhite()
            self.white = temp_model.from_map(m['White'])
        return self


class DescribeBizTypeTextLibResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBizTypeTextLibResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBizTypeTextLibResponse, self).to_map()
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
            temp_model = DescribeBizTypeTextLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBizTypesRequest(TeaModel):
    def __init__(self, import_flag=None):
        self.import_flag = import_flag  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_flag is not None:
            result['ImportFlag'] = self.import_flag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImportFlag') is not None:
            self.import_flag = m.get('ImportFlag')
        return self


class DescribeBizTypesResponseBody(TeaModel):
    def __init__(self, biz_type_list=None, request_id=None, total_count=None):
        self.biz_type_list = biz_type_list  # type: list[str]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBizTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBizTypesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBizTypesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBizTypesResponse, self).to_map()
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
            temp_model = DescribeBizTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudMonitorServicesRequest(TeaModel):
    def __init__(self, page=None, page_size=None, source_ip=None):
        self.page = page  # type: str
        self.page_size = page_size  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudMonitorServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeCloudMonitorServicesResponseBody(TeaModel):
    def __init__(self, items=None, request_id=None, total_count=None):
        self.items = items  # type: list[str]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudMonitorServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCloudMonitorServicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCloudMonitorServicesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCloudMonitorServicesResponse, self).to_map()
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
            temp_model = DescribeCloudMonitorServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomOcrTemplateRequest(TeaModel):
    def __init__(self, ids=None):
        self.ids = ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomOcrTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DescribeCustomOcrTemplateResponseBodyOcrTemplateListRecognizeArea(TeaModel):
    def __init__(self, height=None, name=None, width=None, x=None, y=None):
        self.height = height  # type: int
        self.name = name  # type: str
        self.width = width  # type: int
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomOcrTemplateResponseBodyOcrTemplateListRecognizeArea, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.name is not None:
            result['Name'] = self.name
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeCustomOcrTemplateResponseBodyOcrTemplateListReferArea(TeaModel):
    def __init__(self, height=None, name=None, width=None, x=None, y=None):
        self.height = height  # type: int
        self.name = name  # type: str
        self.width = width  # type: int
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomOcrTemplateResponseBodyOcrTemplateListReferArea, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.name is not None:
            result['Name'] = self.name
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeCustomOcrTemplateResponseBodyOcrTemplateList(TeaModel):
    def __init__(self, id=None, img_url=None, name=None, recognize_area=None, refer_area=None, status=None):
        self.id = id  # type: long
        self.img_url = img_url  # type: str
        self.name = name  # type: str
        self.recognize_area = recognize_area  # type: list[DescribeCustomOcrTemplateResponseBodyOcrTemplateListRecognizeArea]
        self.refer_area = refer_area  # type: list[DescribeCustomOcrTemplateResponseBodyOcrTemplateListReferArea]
        self.status = status  # type: int

    def validate(self):
        if self.recognize_area:
            for k in self.recognize_area:
                if k:
                    k.validate()
        if self.refer_area:
            for k in self.refer_area:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCustomOcrTemplateResponseBodyOcrTemplateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.img_url is not None:
            result['ImgUrl'] = self.img_url
        if self.name is not None:
            result['Name'] = self.name
        result['RecognizeArea'] = []
        if self.recognize_area is not None:
            for k in self.recognize_area:
                result['RecognizeArea'].append(k.to_map() if k else None)
        result['ReferArea'] = []
        if self.refer_area is not None:
            for k in self.refer_area:
                result['ReferArea'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImgUrl') is not None:
            self.img_url = m.get('ImgUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.recognize_area = []
        if m.get('RecognizeArea') is not None:
            for k in m.get('RecognizeArea'):
                temp_model = DescribeCustomOcrTemplateResponseBodyOcrTemplateListRecognizeArea()
                self.recognize_area.append(temp_model.from_map(k))
        self.refer_area = []
        if m.get('ReferArea') is not None:
            for k in m.get('ReferArea'):
                temp_model = DescribeCustomOcrTemplateResponseBodyOcrTemplateListReferArea()
                self.refer_area.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCustomOcrTemplateResponseBody(TeaModel):
    def __init__(self, ocr_template_list=None, request_id=None, total_count=None):
        self.ocr_template_list = ocr_template_list  # type: list[DescribeCustomOcrTemplateResponseBodyOcrTemplateList]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.ocr_template_list:
            for k in self.ocr_template_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCustomOcrTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OcrTemplateList'] = []
        if self.ocr_template_list is not None:
            for k in self.ocr_template_list:
                result['OcrTemplateList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ocr_template_list = []
        if m.get('OcrTemplateList') is not None:
            for k in m.get('OcrTemplateList'):
                temp_model = DescribeCustomOcrTemplateResponseBodyOcrTemplateList()
                self.ocr_template_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCustomOcrTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCustomOcrTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCustomOcrTemplateResponse, self).to_map()
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
            temp_model = DescribeCustomOcrTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageFromLibRequest(TeaModel):
    def __init__(self, current_page=None, end_date=None, id=None, image_lib_id=None, model_id=None, page_size=None,
                 source_ip=None, start_date=None, total_count=None):
        self.current_page = current_page  # type: int
        self.end_date = end_date  # type: str
        self.id = id  # type: long
        self.image_lib_id = image_lib_id  # type: int
        self.model_id = model_id  # type: long
        self.page_size = page_size  # type: int
        self.source_ip = source_ip  # type: str
        self.start_date = start_date  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageFromLibRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.id is not None:
            result['Id'] = self.id
        if self.image_lib_id is not None:
            result['ImageLibId'] = self.image_lib_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageLibId') is not None:
            self.image_lib_id = m.get('ImageLibId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeImageFromLibResponseBodyImageFromLibList(TeaModel):
    def __init__(self, create_time=None, id=None, image=None, image_hit_count=None, thumbnail=None,
                 video_hit_count=None):
        self.create_time = create_time  # type: str
        self.id = id  # type: long
        self.image = image  # type: str
        self.image_hit_count = image_hit_count  # type: long
        self.thumbnail = thumbnail  # type: str
        self.video_hit_count = video_hit_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageFromLibResponseBodyImageFromLibList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.image is not None:
            result['Image'] = self.image
        if self.image_hit_count is not None:
            result['ImageHitCount'] = self.image_hit_count
        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail
        if self.video_hit_count is not None:
            result['VideoHitCount'] = self.video_hit_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImageHitCount') is not None:
            self.image_hit_count = m.get('ImageHitCount')
        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')
        if m.get('VideoHitCount') is not None:
            self.video_hit_count = m.get('VideoHitCount')
        return self


class DescribeImageFromLibResponseBody(TeaModel):
    def __init__(self, current_page=None, image_from_lib_list=None, page_size=None, request_id=None,
                 total_count=None):
        self.current_page = current_page  # type: int
        self.image_from_lib_list = image_from_lib_list  # type: list[DescribeImageFromLibResponseBodyImageFromLibList]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.image_from_lib_list:
            for k in self.image_from_lib_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeImageFromLibResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['ImageFromLibList'] = []
        if self.image_from_lib_list is not None:
            for k in self.image_from_lib_list:
                result['ImageFromLibList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.image_from_lib_list = []
        if m.get('ImageFromLibList') is not None:
            for k in m.get('ImageFromLibList'):
                temp_model = DescribeImageFromLibResponseBodyImageFromLibList()
                self.image_from_lib_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeImageFromLibResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeImageFromLibResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeImageFromLibResponse, self).to_map()
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
            temp_model = DescribeImageFromLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageLibRequest(TeaModel):
    def __init__(self, service_module=None, source_ip=None):
        self.service_module = service_module  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageLibRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_module is not None:
            result['ServiceModule'] = self.service_module
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceModule') is not None:
            self.service_module = m.get('ServiceModule')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeImageLibResponseBodyImageLibList(TeaModel):
    def __init__(self, biz_types=None, category=None, code=None, enable=None, id=None, image_count=None,
                 modified_time=None, name=None, scene=None, service_module=None, source=None):
        self.biz_types = biz_types  # type: list[str]
        self.category = category  # type: str
        self.code = code  # type: str
        self.enable = enable  # type: str
        self.id = id  # type: int
        self.image_count = image_count  # type: int
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.scene = scene  # type: str
        self.service_module = service_module  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageLibResponseBodyImageLibList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.category is not None:
            result['Category'] = self.category
        if self.code is not None:
            result['Code'] = self.code
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.id is not None:
            result['Id'] = self.id
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.service_module is not None:
            result['ServiceModule'] = self.service_module
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('ServiceModule') is not None:
            self.service_module = m.get('ServiceModule')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeImageLibResponseBody(TeaModel):
    def __init__(self, image_lib_list=None, request_id=None, total_count=None):
        self.image_lib_list = image_lib_list  # type: list[DescribeImageLibResponseBodyImageLibList]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.image_lib_list:
            for k in self.image_lib_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeImageLibResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageLibList'] = []
        if self.image_lib_list is not None:
            for k in self.image_lib_list:
                result['ImageLibList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.image_lib_list = []
        if m.get('ImageLibList') is not None:
            for k in m.get('ImageLibList'):
                temp_model = DescribeImageLibResponseBodyImageLibList()
                self.image_lib_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeImageLibResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeImageLibResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeImageLibResponse, self).to_map()
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
            temp_model = DescribeImageLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageUploadInfoRequest(TeaModel):
    def __init__(self, source_ip=None):
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageUploadInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeImageUploadInfoResponseBody(TeaModel):
    def __init__(self, accessid=None, expire=None, folder=None, host=None, policy=None, request_id=None,
                 signature=None):
        self.accessid = accessid  # type: str
        self.expire = expire  # type: int
        self.folder = folder  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.request_id = request_id  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageUploadInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessid is not None:
            result['Accessid'] = self.accessid
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.folder is not None:
            result['Folder'] = self.folder
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Folder') is not None:
            self.folder = m.get('Folder')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class DescribeImageUploadInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeImageUploadInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeImageUploadInfoResponse, self).to_map()
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
            temp_model = DescribeImageUploadInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKeywordRequest(TeaModel):
    def __init__(self, current_page=None, keyword=None, keyword_lib_id=None, lang=None, page_size=None,
                 source_ip=None, total_count=None):
        self.current_page = current_page  # type: int
        self.keyword = keyword  # type: str
        self.keyword_lib_id = keyword_lib_id  # type: int
        self.lang = lang  # type: str
        self.page_size = page_size  # type: int
        self.source_ip = source_ip  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKeywordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.keyword_lib_id is not None:
            result['KeywordLibId'] = self.keyword_lib_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('KeywordLibId') is not None:
            self.keyword_lib_id = m.get('KeywordLibId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeKeywordResponseBodyKeywordList(TeaModel):
    def __init__(self, create_time=None, hit_count=None, id=None, keyword=None):
        self.create_time = create_time  # type: str
        self.hit_count = hit_count  # type: int
        self.id = id  # type: int
        self.keyword = keyword  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKeywordResponseBodyKeywordList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.hit_count is not None:
            result['HitCount'] = self.hit_count
        if self.id is not None:
            result['Id'] = self.id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('HitCount') is not None:
            self.hit_count = m.get('HitCount')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class DescribeKeywordResponseBody(TeaModel):
    def __init__(self, current_page=None, keyword_list=None, page_size=None, request_id=None, total_count=None):
        self.current_page = current_page  # type: int
        self.keyword_list = keyword_list  # type: list[DescribeKeywordResponseBodyKeywordList]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.keyword_list:
            for k in self.keyword_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeKeywordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['KeywordList'] = []
        if self.keyword_list is not None:
            for k in self.keyword_list:
                result['KeywordList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.keyword_list = []
        if m.get('KeywordList') is not None:
            for k in m.get('KeywordList'):
                temp_model = DescribeKeywordResponseBodyKeywordList()
                self.keyword_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeKeywordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeKeywordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeKeywordResponse, self).to_map()
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
            temp_model = DescribeKeywordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKeywordLibRequest(TeaModel):
    def __init__(self, lang=None, service_module=None, source_ip=None):
        self.lang = lang  # type: str
        self.service_module = service_module  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKeywordLibRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.service_module is not None:
            result['ServiceModule'] = self.service_module
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ServiceModule') is not None:
            self.service_module = m.get('ServiceModule')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeKeywordLibResponseBodyKeywordLibList(TeaModel):
    def __init__(self, biz_types=None, category=None, code=None, count=None, enable=None, id=None, language=None,
                 lib_type=None, match_mode=None, modified_time=None, name=None, resource_type=None, service_module=None,
                 source=None):
        self.biz_types = biz_types  # type: list[str]
        self.category = category  # type: str
        self.code = code  # type: str
        self.count = count  # type: int
        self.enable = enable  # type: bool
        self.id = id  # type: int
        self.language = language  # type: str
        self.lib_type = lib_type  # type: str
        self.match_mode = match_mode  # type: str
        self.modified_time = modified_time  # type: str
        self.name = name  # type: str
        self.resource_type = resource_type  # type: str
        self.service_module = service_module  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeKeywordLibResponseBodyKeywordLibList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.category is not None:
            result['Category'] = self.category
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.id is not None:
            result['Id'] = self.id
        if self.language is not None:
            result['Language'] = self.language
        if self.lib_type is not None:
            result['LibType'] = self.lib_type
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_module is not None:
            result['ServiceModule'] = self.service_module
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LibType') is not None:
            self.lib_type = m.get('LibType')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceModule') is not None:
            self.service_module = m.get('ServiceModule')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeKeywordLibResponseBody(TeaModel):
    def __init__(self, keyword_lib_list=None, request_id=None, total_count=None):
        self.keyword_lib_list = keyword_lib_list  # type: list[DescribeKeywordLibResponseBodyKeywordLibList]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.keyword_lib_list:
            for k in self.keyword_lib_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeKeywordLibResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeywordLibList'] = []
        if self.keyword_lib_list is not None:
            for k in self.keyword_lib_list:
                result['KeywordLibList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.keyword_lib_list = []
        if m.get('KeywordLibList') is not None:
            for k in m.get('KeywordLibList'):
                temp_model = DescribeKeywordLibResponseBodyKeywordLibList()
                self.keyword_lib_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeKeywordLibResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeKeywordLibResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeKeywordLibResponse, self).to_map()
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
            temp_model = DescribeKeywordLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNotificationSettingRequest(TeaModel):
    def __init__(self, lang=None, source_ip=None):
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNotificationSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeNotificationSettingResponseBody(TeaModel):
    def __init__(self, email=None, phone=None, realtime_message_list=None, reminder_mode_list=None, request_id=None,
                 schedule_message_time=None, schedule_message_time_zone=None):
        self.email = email  # type: str
        self.phone = phone  # type: str
        self.realtime_message_list = realtime_message_list  # type: list[str]
        self.reminder_mode_list = reminder_mode_list  # type: list[str]
        self.request_id = request_id  # type: str
        self.schedule_message_time = schedule_message_time  # type: int
        self.schedule_message_time_zone = schedule_message_time_zone  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNotificationSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.realtime_message_list is not None:
            result['RealtimeMessageList'] = self.realtime_message_list
        if self.reminder_mode_list is not None:
            result['ReminderModeList'] = self.reminder_mode_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_message_time is not None:
            result['ScheduleMessageTime'] = self.schedule_message_time
        if self.schedule_message_time_zone is not None:
            result['ScheduleMessageTimeZone'] = self.schedule_message_time_zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RealtimeMessageList') is not None:
            self.realtime_message_list = m.get('RealtimeMessageList')
        if m.get('ReminderModeList') is not None:
            self.reminder_mode_list = m.get('ReminderModeList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleMessageTime') is not None:
            self.schedule_message_time = m.get('ScheduleMessageTime')
        if m.get('ScheduleMessageTimeZone') is not None:
            self.schedule_message_time_zone = m.get('ScheduleMessageTimeZone')
        return self


class DescribeNotificationSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNotificationSettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNotificationSettingResponse, self).to_map()
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
            temp_model = DescribeNotificationSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOpenApiRcpStatsRequest(TeaModel):
    def __init__(self, biz_type=None, end_date=None, resource_type=None, start_date=None):
        self.biz_type = biz_type  # type: str
        self.end_date = end_date  # type: str
        self.resource_type = resource_type  # type: str
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOpenApiRcpStatsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeOpenApiRcpStatsResponseBodyStatList(TeaModel):
    def __init__(self, block_count=None, date=None, pass_count=None, resource_type=None, review_count=None,
                 total_count=None, total_duration=None):
        self.block_count = block_count  # type: int
        self.date = date  # type: str
        self.pass_count = pass_count  # type: int
        self.resource_type = resource_type  # type: str
        self.review_count = review_count  # type: int
        self.total_count = total_count  # type: int
        self.total_duration = total_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOpenApiRcpStatsResponseBodyStatList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        if self.date is not None:
            result['Date'] = self.date
        if self.pass_count is not None:
            result['PassCount'] = self.pass_count
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.review_count is not None:
            result['ReviewCount'] = self.review_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ReviewCount') is not None:
            self.review_count = m.get('ReviewCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')
        return self


class DescribeOpenApiRcpStatsResponseBody(TeaModel):
    def __init__(self, request_id=None, stat_list=None, total_count=None):
        self.request_id = request_id  # type: str
        self.stat_list = stat_list  # type: list[DescribeOpenApiRcpStatsResponseBodyStatList]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.stat_list:
            for k in self.stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOpenApiRcpStatsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatList'] = []
        if self.stat_list is not None:
            for k in self.stat_list:
                result['StatList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stat_list = []
        if m.get('StatList') is not None:
            for k in m.get('StatList'):
                temp_model = DescribeOpenApiRcpStatsResponseBodyStatList()
                self.stat_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOpenApiRcpStatsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOpenApiRcpStatsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOpenApiRcpStatsResponse, self).to_map()
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
            temp_model = DescribeOpenApiRcpStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOpenApiUsageRequest(TeaModel):
    def __init__(self, end_date=None, resource_type=None, source_ip=None, start_date=None):
        self.end_date = end_date  # type: str
        self.resource_type = resource_type  # type: str
        self.source_ip = source_ip  # type: str
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOpenApiUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeOpenApiUsageResponseBodyOpenApiUsageList(TeaModel):
    def __init__(self, block_count=None, block_duration=None, date=None, inner_total_count=None,
                 outer_total_count=None, pass_count=None, pass_duration=None, resource_type=None, review_count=None,
                 review_duration=None, scene=None, total_count=None, total_duration=None):
        self.block_count = block_count  # type: int
        self.block_duration = block_duration  # type: int
        self.date = date  # type: str
        self.inner_total_count = inner_total_count  # type: int
        self.outer_total_count = outer_total_count  # type: int
        self.pass_count = pass_count  # type: int
        self.pass_duration = pass_duration  # type: int
        self.resource_type = resource_type  # type: str
        self.review_count = review_count  # type: int
        self.review_duration = review_duration  # type: int
        self.scene = scene  # type: str
        self.total_count = total_count  # type: int
        self.total_duration = total_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOpenApiUsageResponseBodyOpenApiUsageList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        if self.block_duration is not None:
            result['BlockDuration'] = self.block_duration
        if self.date is not None:
            result['Date'] = self.date
        if self.inner_total_count is not None:
            result['InnerTotalCount'] = self.inner_total_count
        if self.outer_total_count is not None:
            result['OuterTotalCount'] = self.outer_total_count
        if self.pass_count is not None:
            result['PassCount'] = self.pass_count
        if self.pass_duration is not None:
            result['PassDuration'] = self.pass_duration
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.review_count is not None:
            result['ReviewCount'] = self.review_count
        if self.review_duration is not None:
            result['ReviewDuration'] = self.review_duration
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        if m.get('BlockDuration') is not None:
            self.block_duration = m.get('BlockDuration')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('InnerTotalCount') is not None:
            self.inner_total_count = m.get('InnerTotalCount')
        if m.get('OuterTotalCount') is not None:
            self.outer_total_count = m.get('OuterTotalCount')
        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')
        if m.get('PassDuration') is not None:
            self.pass_duration = m.get('PassDuration')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ReviewCount') is not None:
            self.review_count = m.get('ReviewCount')
        if m.get('ReviewDuration') is not None:
            self.review_duration = m.get('ReviewDuration')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')
        return self


class DescribeOpenApiUsageResponseBody(TeaModel):
    def __init__(self, open_api_usage_list=None, request_id=None, total_count=None):
        self.open_api_usage_list = open_api_usage_list  # type: list[DescribeOpenApiUsageResponseBodyOpenApiUsageList]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.open_api_usage_list:
            for k in self.open_api_usage_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOpenApiUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OpenApiUsageList'] = []
        if self.open_api_usage_list is not None:
            for k in self.open_api_usage_list:
                result['OpenApiUsageList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.open_api_usage_list = []
        if m.get('OpenApiUsageList') is not None:
            for k in m.get('OpenApiUsageList'):
                temp_model = DescribeOpenApiUsageResponseBodyOpenApiUsageList()
                self.open_api_usage_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOpenApiUsageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOpenApiUsageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOpenApiUsageResponse, self).to_map()
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
            temp_model = DescribeOpenApiUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssCallbackSettingResponseBody(TeaModel):
    def __init__(self, audit_callback=None, callback_seed=None, callback_url=None, request_id=None,
                 scan_callback=None, scan_callback_suggestions=None, service_modules=None):
        self.audit_callback = audit_callback  # type: bool
        self.callback_seed = callback_seed  # type: str
        self.callback_url = callback_url  # type: str
        self.request_id = request_id  # type: str
        self.scan_callback = scan_callback  # type: bool
        self.scan_callback_suggestions = scan_callback_suggestions  # type: list[str]
        self.service_modules = service_modules  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssCallbackSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_callback is not None:
            result['AuditCallback'] = self.audit_callback
        if self.callback_seed is not None:
            result['CallbackSeed'] = self.callback_seed
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scan_callback is not None:
            result['ScanCallback'] = self.scan_callback
        if self.scan_callback_suggestions is not None:
            result['ScanCallbackSuggestions'] = self.scan_callback_suggestions
        if self.service_modules is not None:
            result['ServiceModules'] = self.service_modules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditCallback') is not None:
            self.audit_callback = m.get('AuditCallback')
        if m.get('CallbackSeed') is not None:
            self.callback_seed = m.get('CallbackSeed')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScanCallback') is not None:
            self.scan_callback = m.get('ScanCallback')
        if m.get('ScanCallbackSuggestions') is not None:
            self.scan_callback_suggestions = m.get('ScanCallbackSuggestions')
        if m.get('ServiceModules') is not None:
            self.service_modules = m.get('ServiceModules')
        return self


class DescribeOssCallbackSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOssCallbackSettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOssCallbackSettingResponse, self).to_map()
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
            temp_model = DescribeOssCallbackSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssIncrementCheckSettingRequest(TeaModel):
    def __init__(self, lang=None, source_ip=None):
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeOssIncrementCheckSettingResponseBodyAudioAntispamFreezeConfig(TeaModel):
    def __init__(self, type=None, value=None):
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyAudioAntispamFreezeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigAd(TeaModel):
    def __init__(self, categories=None):
        self.categories = categories  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigAd, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigLive(TeaModel):
    def __init__(self, categories=None):
        self.categories = categories  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigLive, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigPorn(TeaModel):
    def __init__(self, categories=None):
        self.categories = categories  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigPorn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigTerrorism(TeaModel):
    def __init__(self, categories=None):
        self.categories = categories  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigTerrorism, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfig(TeaModel):
    def __init__(self, ad=None, live=None, porn=None, terrorism=None):
        self.ad = ad  # type: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigAd
        self.live = live  # type: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigLive
        self.porn = porn  # type: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigPorn
        self.terrorism = terrorism  # type: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigTerrorism

    def validate(self):
        if self.ad:
            self.ad.validate()
        if self.live:
            self.live.validate()
        if self.porn:
            self.porn.validate()
        if self.terrorism:
            self.terrorism.validate()

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad is not None:
            result['Ad'] = self.ad.to_map()
        if self.live is not None:
            result['Live'] = self.live.to_map()
        if self.porn is not None:
            result['Porn'] = self.porn.to_map()
        if self.terrorism is not None:
            result['Terrorism'] = self.terrorism.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ad') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigAd()
            self.ad = temp_model.from_map(m['Ad'])
        if m.get('Live') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigLive()
            self.live = temp_model.from_map(m['Live'])
        if m.get('Porn') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigPorn()
            self.porn = temp_model.from_map(m['Porn'])
        if m.get('Terrorism') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigTerrorism()
            self.terrorism = temp_model.from_map(m['Terrorism'])
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigAd(TeaModel):
    def __init__(self, categories=None):
        self.categories = categories  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigAd, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigLive(TeaModel):
    def __init__(self, categories=None):
        self.categories = categories  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigLive, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigPorn(TeaModel):
    def __init__(self, categories=None):
        self.categories = categories  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigPorn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigTerrorism(TeaModel):
    def __init__(self, categories=None):
        self.categories = categories  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigTerrorism, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfig(TeaModel):
    def __init__(self, ad=None, live=None, porn=None, terrorism=None):
        self.ad = ad  # type: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigAd
        self.live = live  # type: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigLive
        self.porn = porn  # type: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigPorn
        self.terrorism = terrorism  # type: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigTerrorism

    def validate(self):
        if self.ad:
            self.ad.validate()
        if self.live:
            self.live.validate()
        if self.porn:
            self.porn.validate()
        if self.terrorism:
            self.terrorism.validate()

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad is not None:
            result['Ad'] = self.ad.to_map()
        if self.live is not None:
            result['Live'] = self.live.to_map()
        if self.porn is not None:
            result['Porn'] = self.porn.to_map()
        if self.terrorism is not None:
            result['Terrorism'] = self.terrorism.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ad') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigAd()
            self.ad = temp_model.from_map(m['Ad'])
        if m.get('Live') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigLive()
            self.live = temp_model.from_map(m['Live'])
        if m.get('Porn') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigPorn()
            self.porn = temp_model.from_map(m['Porn'])
        if m.get('Terrorism') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigTerrorism()
            self.terrorism = temp_model.from_map(m['Terrorism'])
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVoiceConfigAntispam(TeaModel):
    def __init__(self, categories=None):
        self.categories = categories  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVoiceConfigAntispam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVoiceConfig(TeaModel):
    def __init__(self, antispam=None):
        self.antispam = antispam  # type: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVoiceConfigAntispam

    def validate(self):
        if self.antispam:
            self.antispam.validate()

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVoiceConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.antispam is not None:
            result['Antispam'] = self.antispam.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Antispam') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVoiceConfigAntispam()
            self.antispam = temp_model.from_map(m['Antispam'])
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplate(TeaModel):
    def __init__(self, biz_type=None, description=None, image_config=None, include_channel=None, name=None,
                 video_config=None, voice_config=None):
        self.biz_type = biz_type  # type: str
        self.description = description  # type: str
        self.image_config = image_config  # type: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfig
        self.include_channel = include_channel  # type: int
        self.name = name  # type: str
        self.video_config = video_config  # type: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfig
        self.voice_config = voice_config  # type: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVoiceConfig

    def validate(self):
        if self.image_config:
            self.image_config.validate()
        if self.video_config:
            self.video_config.validate()
        if self.voice_config:
            self.voice_config.validate()

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.description is not None:
            result['Description'] = self.description
        if self.image_config is not None:
            result['ImageConfig'] = self.image_config.to_map()
        if self.include_channel is not None:
            result['IncludeChannel'] = self.include_channel
        if self.name is not None:
            result['Name'] = self.name
        if self.video_config is not None:
            result['VideoConfig'] = self.video_config.to_map()
        if self.voice_config is not None:
            result['VoiceConfig'] = self.voice_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfig()
            self.image_config = temp_model.from_map(m['ImageConfig'])
        if m.get('IncludeChannel') is not None:
            self.include_channel = m.get('IncludeChannel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VideoConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfig()
            self.video_config = temp_model.from_map(m['VideoConfig'])
        if m.get('VoiceConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVoiceConfig()
            self.voice_config = temp_model.from_map(m['VoiceConfig'])
        return self


class DescribeOssIncrementCheckSettingResponseBodyBucketConfigList(TeaModel):
    def __init__(self, bucket=None, prefixes=None, selected=None, type=None):
        self.bucket = bucket  # type: str
        self.prefixes = prefixes  # type: list[str]
        self.selected = selected  # type: bool
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyBucketConfigList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.prefixes is not None:
            result['Prefixes'] = self.prefixes
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Prefixes') is not None:
            self.prefixes = m.get('Prefixes')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeOssIncrementCheckSettingResponseBodyImageAdFreezeConfig(TeaModel):
    def __init__(self, type=None, value=None):
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyImageAdFreezeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeOssIncrementCheckSettingResponseBodyImageAutoFreeze(TeaModel):
    def __init__(self, ad=None, enabled=None, live=None, porn=None, terrorism=None):
        self.ad = ad  # type: str
        self.enabled = enabled  # type: bool
        self.live = live  # type: str
        self.porn = porn  # type: str
        self.terrorism = terrorism  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyImageAutoFreeze, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad is not None:
            result['Ad'] = self.ad
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.live is not None:
            result['Live'] = self.live
        if self.porn is not None:
            result['Porn'] = self.porn
        if self.terrorism is not None:
            result['Terrorism'] = self.terrorism
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ad') is not None:
            self.ad = m.get('Ad')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Live') is not None:
            self.live = m.get('Live')
        if m.get('Porn') is not None:
            self.porn = m.get('Porn')
        if m.get('Terrorism') is not None:
            self.terrorism = m.get('Terrorism')
        return self


class DescribeOssIncrementCheckSettingResponseBodyImageLiveFreezeConfig(TeaModel):
    def __init__(self, type=None, value=None):
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyImageLiveFreezeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeOssIncrementCheckSettingResponseBodyImagePornFreezeConfig(TeaModel):
    def __init__(self, type=None, value=None):
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyImagePornFreezeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeOssIncrementCheckSettingResponseBodyImageTerrorismFreezeConfig(TeaModel):
    def __init__(self, type=None, value=None):
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyImageTerrorismFreezeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeOssIncrementCheckSettingResponseBodyVideoAdFreezeConfig(TeaModel):
    def __init__(self, type=None, value=None):
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyVideoAdFreezeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeOssIncrementCheckSettingResponseBodyVideoLiveFreezeConfig(TeaModel):
    def __init__(self, type=None, value=None):
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyVideoLiveFreezeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeOssIncrementCheckSettingResponseBodyVideoPornFreezeConfig(TeaModel):
    def __init__(self, type=None, value=None):
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyVideoPornFreezeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeOssIncrementCheckSettingResponseBodyVideoTerrorismFreezeConfig(TeaModel):
    def __init__(self, type=None, value=None):
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyVideoTerrorismFreezeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeOssIncrementCheckSettingResponseBodyVideoVoiceAntispamFreezeConfig(TeaModel):
    def __init__(self, type=None, value=None):
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBodyVideoVoiceAntispamFreezeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeOssIncrementCheckSettingResponseBody(TeaModel):
    def __init__(self, audio_antispam_freeze_config=None, audio_auto_freeze_opened=None, audio_max_size=None,
                 audio_scan_limit=None, audio_scene_list=None, auto_freeze_type=None, biz_type=None, biz_type_template=None,
                 bucket_config_list=None, callback_id=None, callback_name=None, end_time=None, image_ad_freeze_config=None,
                 image_auto_freeze=None, image_auto_freeze_opened=None, image_enable_limit=None, image_live_freeze_config=None,
                 image_porn_freeze_config=None, image_scan_limit=None, image_scene_list=None, image_terrorism_freeze_config=None,
                 request_id=None, scan_image_no_file_type=None, start_time=None, video_ad_freeze_config=None,
                 video_auto_freeze_opened=None, video_auto_freeze_scene_list=None, video_frame_interval=None,
                 video_live_freeze_config=None, video_max_frames=None, video_max_size=None, video_porn_freeze_config=None,
                 video_scan_limit=None, video_scene_list=None, video_terrorism_freeze_config=None,
                 video_voice_antispam_freeze_config=None):
        self.audio_antispam_freeze_config = audio_antispam_freeze_config  # type: DescribeOssIncrementCheckSettingResponseBodyAudioAntispamFreezeConfig
        self.audio_auto_freeze_opened = audio_auto_freeze_opened  # type: bool
        self.audio_max_size = audio_max_size  # type: int
        self.audio_scan_limit = audio_scan_limit  # type: long
        self.audio_scene_list = audio_scene_list  # type: list[str]
        self.auto_freeze_type = auto_freeze_type  # type: str
        self.biz_type = biz_type  # type: str
        self.biz_type_template = biz_type_template  # type: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplate
        self.bucket_config_list = bucket_config_list  # type: list[DescribeOssIncrementCheckSettingResponseBodyBucketConfigList]
        self.callback_id = callback_id  # type: str
        self.callback_name = callback_name  # type: str
        self.end_time = end_time  # type: str
        self.image_ad_freeze_config = image_ad_freeze_config  # type: DescribeOssIncrementCheckSettingResponseBodyImageAdFreezeConfig
        self.image_auto_freeze = image_auto_freeze  # type: DescribeOssIncrementCheckSettingResponseBodyImageAutoFreeze
        self.image_auto_freeze_opened = image_auto_freeze_opened  # type: bool
        self.image_enable_limit = image_enable_limit  # type: bool
        self.image_live_freeze_config = image_live_freeze_config  # type: DescribeOssIncrementCheckSettingResponseBodyImageLiveFreezeConfig
        self.image_porn_freeze_config = image_porn_freeze_config  # type: DescribeOssIncrementCheckSettingResponseBodyImagePornFreezeConfig
        self.image_scan_limit = image_scan_limit  # type: long
        self.image_scene_list = image_scene_list  # type: list[str]
        self.image_terrorism_freeze_config = image_terrorism_freeze_config  # type: DescribeOssIncrementCheckSettingResponseBodyImageTerrorismFreezeConfig
        self.request_id = request_id  # type: str
        self.scan_image_no_file_type = scan_image_no_file_type  # type: bool
        self.start_time = start_time  # type: str
        self.video_ad_freeze_config = video_ad_freeze_config  # type: DescribeOssIncrementCheckSettingResponseBodyVideoAdFreezeConfig
        self.video_auto_freeze_opened = video_auto_freeze_opened  # type: bool
        self.video_auto_freeze_scene_list = video_auto_freeze_scene_list  # type: list[str]
        self.video_frame_interval = video_frame_interval  # type: int
        self.video_live_freeze_config = video_live_freeze_config  # type: DescribeOssIncrementCheckSettingResponseBodyVideoLiveFreezeConfig
        self.video_max_frames = video_max_frames  # type: int
        self.video_max_size = video_max_size  # type: int
        self.video_porn_freeze_config = video_porn_freeze_config  # type: DescribeOssIncrementCheckSettingResponseBodyVideoPornFreezeConfig
        self.video_scan_limit = video_scan_limit  # type: long
        self.video_scene_list = video_scene_list  # type: list[str]
        self.video_terrorism_freeze_config = video_terrorism_freeze_config  # type: DescribeOssIncrementCheckSettingResponseBodyVideoTerrorismFreezeConfig
        self.video_voice_antispam_freeze_config = video_voice_antispam_freeze_config  # type: DescribeOssIncrementCheckSettingResponseBodyVideoVoiceAntispamFreezeConfig

    def validate(self):
        if self.audio_antispam_freeze_config:
            self.audio_antispam_freeze_config.validate()
        if self.biz_type_template:
            self.biz_type_template.validate()
        if self.bucket_config_list:
            for k in self.bucket_config_list:
                if k:
                    k.validate()
        if self.image_ad_freeze_config:
            self.image_ad_freeze_config.validate()
        if self.image_auto_freeze:
            self.image_auto_freeze.validate()
        if self.image_live_freeze_config:
            self.image_live_freeze_config.validate()
        if self.image_porn_freeze_config:
            self.image_porn_freeze_config.validate()
        if self.image_terrorism_freeze_config:
            self.image_terrorism_freeze_config.validate()
        if self.video_ad_freeze_config:
            self.video_ad_freeze_config.validate()
        if self.video_live_freeze_config:
            self.video_live_freeze_config.validate()
        if self.video_porn_freeze_config:
            self.video_porn_freeze_config.validate()
        if self.video_terrorism_freeze_config:
            self.video_terrorism_freeze_config.validate()
        if self.video_voice_antispam_freeze_config:
            self.video_voice_antispam_freeze_config.validate()

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_antispam_freeze_config is not None:
            result['AudioAntispamFreezeConfig'] = self.audio_antispam_freeze_config.to_map()
        if self.audio_auto_freeze_opened is not None:
            result['AudioAutoFreezeOpened'] = self.audio_auto_freeze_opened
        if self.audio_max_size is not None:
            result['AudioMaxSize'] = self.audio_max_size
        if self.audio_scan_limit is not None:
            result['AudioScanLimit'] = self.audio_scan_limit
        if self.audio_scene_list is not None:
            result['AudioSceneList'] = self.audio_scene_list
        if self.auto_freeze_type is not None:
            result['AutoFreezeType'] = self.auto_freeze_type
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_type_template is not None:
            result['BizTypeTemplate'] = self.biz_type_template.to_map()
        result['BucketConfigList'] = []
        if self.bucket_config_list is not None:
            for k in self.bucket_config_list:
                result['BucketConfigList'].append(k.to_map() if k else None)
        if self.callback_id is not None:
            result['CallbackId'] = self.callback_id
        if self.callback_name is not None:
            result['CallbackName'] = self.callback_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.image_ad_freeze_config is not None:
            result['ImageAdFreezeConfig'] = self.image_ad_freeze_config.to_map()
        if self.image_auto_freeze is not None:
            result['ImageAutoFreeze'] = self.image_auto_freeze.to_map()
        if self.image_auto_freeze_opened is not None:
            result['ImageAutoFreezeOpened'] = self.image_auto_freeze_opened
        if self.image_enable_limit is not None:
            result['ImageEnableLimit'] = self.image_enable_limit
        if self.image_live_freeze_config is not None:
            result['ImageLiveFreezeConfig'] = self.image_live_freeze_config.to_map()
        if self.image_porn_freeze_config is not None:
            result['ImagePornFreezeConfig'] = self.image_porn_freeze_config.to_map()
        if self.image_scan_limit is not None:
            result['ImageScanLimit'] = self.image_scan_limit
        if self.image_scene_list is not None:
            result['ImageSceneList'] = self.image_scene_list
        if self.image_terrorism_freeze_config is not None:
            result['ImageTerrorismFreezeConfig'] = self.image_terrorism_freeze_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scan_image_no_file_type is not None:
            result['ScanImageNoFileType'] = self.scan_image_no_file_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.video_ad_freeze_config is not None:
            result['VideoAdFreezeConfig'] = self.video_ad_freeze_config.to_map()
        if self.video_auto_freeze_opened is not None:
            result['VideoAutoFreezeOpened'] = self.video_auto_freeze_opened
        if self.video_auto_freeze_scene_list is not None:
            result['VideoAutoFreezeSceneList'] = self.video_auto_freeze_scene_list
        if self.video_frame_interval is not None:
            result['VideoFrameInterval'] = self.video_frame_interval
        if self.video_live_freeze_config is not None:
            result['VideoLiveFreezeConfig'] = self.video_live_freeze_config.to_map()
        if self.video_max_frames is not None:
            result['VideoMaxFrames'] = self.video_max_frames
        if self.video_max_size is not None:
            result['VideoMaxSize'] = self.video_max_size
        if self.video_porn_freeze_config is not None:
            result['VideoPornFreezeConfig'] = self.video_porn_freeze_config.to_map()
        if self.video_scan_limit is not None:
            result['VideoScanLimit'] = self.video_scan_limit
        if self.video_scene_list is not None:
            result['VideoSceneList'] = self.video_scene_list
        if self.video_terrorism_freeze_config is not None:
            result['VideoTerrorismFreezeConfig'] = self.video_terrorism_freeze_config.to_map()
        if self.video_voice_antispam_freeze_config is not None:
            result['VideoVoiceAntispamFreezeConfig'] = self.video_voice_antispam_freeze_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioAntispamFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyAudioAntispamFreezeConfig()
            self.audio_antispam_freeze_config = temp_model.from_map(m['AudioAntispamFreezeConfig'])
        if m.get('AudioAutoFreezeOpened') is not None:
            self.audio_auto_freeze_opened = m.get('AudioAutoFreezeOpened')
        if m.get('AudioMaxSize') is not None:
            self.audio_max_size = m.get('AudioMaxSize')
        if m.get('AudioScanLimit') is not None:
            self.audio_scan_limit = m.get('AudioScanLimit')
        if m.get('AudioSceneList') is not None:
            self.audio_scene_list = m.get('AudioSceneList')
        if m.get('AutoFreezeType') is not None:
            self.auto_freeze_type = m.get('AutoFreezeType')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizTypeTemplate') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplate()
            self.biz_type_template = temp_model.from_map(m['BizTypeTemplate'])
        self.bucket_config_list = []
        if m.get('BucketConfigList') is not None:
            for k in m.get('BucketConfigList'):
                temp_model = DescribeOssIncrementCheckSettingResponseBodyBucketConfigList()
                self.bucket_config_list.append(temp_model.from_map(k))
        if m.get('CallbackId') is not None:
            self.callback_id = m.get('CallbackId')
        if m.get('CallbackName') is not None:
            self.callback_name = m.get('CallbackName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ImageAdFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyImageAdFreezeConfig()
            self.image_ad_freeze_config = temp_model.from_map(m['ImageAdFreezeConfig'])
        if m.get('ImageAutoFreeze') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyImageAutoFreeze()
            self.image_auto_freeze = temp_model.from_map(m['ImageAutoFreeze'])
        if m.get('ImageAutoFreezeOpened') is not None:
            self.image_auto_freeze_opened = m.get('ImageAutoFreezeOpened')
        if m.get('ImageEnableLimit') is not None:
            self.image_enable_limit = m.get('ImageEnableLimit')
        if m.get('ImageLiveFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyImageLiveFreezeConfig()
            self.image_live_freeze_config = temp_model.from_map(m['ImageLiveFreezeConfig'])
        if m.get('ImagePornFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyImagePornFreezeConfig()
            self.image_porn_freeze_config = temp_model.from_map(m['ImagePornFreezeConfig'])
        if m.get('ImageScanLimit') is not None:
            self.image_scan_limit = m.get('ImageScanLimit')
        if m.get('ImageSceneList') is not None:
            self.image_scene_list = m.get('ImageSceneList')
        if m.get('ImageTerrorismFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyImageTerrorismFreezeConfig()
            self.image_terrorism_freeze_config = temp_model.from_map(m['ImageTerrorismFreezeConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScanImageNoFileType') is not None:
            self.scan_image_no_file_type = m.get('ScanImageNoFileType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VideoAdFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyVideoAdFreezeConfig()
            self.video_ad_freeze_config = temp_model.from_map(m['VideoAdFreezeConfig'])
        if m.get('VideoAutoFreezeOpened') is not None:
            self.video_auto_freeze_opened = m.get('VideoAutoFreezeOpened')
        if m.get('VideoAutoFreezeSceneList') is not None:
            self.video_auto_freeze_scene_list = m.get('VideoAutoFreezeSceneList')
        if m.get('VideoFrameInterval') is not None:
            self.video_frame_interval = m.get('VideoFrameInterval')
        if m.get('VideoLiveFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyVideoLiveFreezeConfig()
            self.video_live_freeze_config = temp_model.from_map(m['VideoLiveFreezeConfig'])
        if m.get('VideoMaxFrames') is not None:
            self.video_max_frames = m.get('VideoMaxFrames')
        if m.get('VideoMaxSize') is not None:
            self.video_max_size = m.get('VideoMaxSize')
        if m.get('VideoPornFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyVideoPornFreezeConfig()
            self.video_porn_freeze_config = temp_model.from_map(m['VideoPornFreezeConfig'])
        if m.get('VideoScanLimit') is not None:
            self.video_scan_limit = m.get('VideoScanLimit')
        if m.get('VideoSceneList') is not None:
            self.video_scene_list = m.get('VideoSceneList')
        if m.get('VideoTerrorismFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyVideoTerrorismFreezeConfig()
            self.video_terrorism_freeze_config = temp_model.from_map(m['VideoTerrorismFreezeConfig'])
        if m.get('VideoVoiceAntispamFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyVideoVoiceAntispamFreezeConfig()
            self.video_voice_antispam_freeze_config = temp_model.from_map(m['VideoVoiceAntispamFreezeConfig'])
        return self


class DescribeOssIncrementCheckSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOssIncrementCheckSettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOssIncrementCheckSettingResponse, self).to_map()
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
            temp_model = DescribeOssIncrementCheckSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssIncrementOverviewRequest(TeaModel):
    def __init__(self, lang=None, source_ip=None):
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementOverviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeOssIncrementOverviewResponseBody(TeaModel):
    def __init__(self, ad_unhandle_count=None, audio_count=None, image_count=None, live_unhandle_count=None,
                 porn_unhandle_count=None, request_id=None, terrorism_unhandle_count=None, video_count=None, video_frame_count=None,
                 voice_antispam_unhandle_count=None):
        self.ad_unhandle_count = ad_unhandle_count  # type: int
        self.audio_count = audio_count  # type: int
        self.image_count = image_count  # type: int
        self.live_unhandle_count = live_unhandle_count  # type: int
        self.porn_unhandle_count = porn_unhandle_count  # type: int
        self.request_id = request_id  # type: str
        self.terrorism_unhandle_count = terrorism_unhandle_count  # type: int
        self.video_count = video_count  # type: int
        self.video_frame_count = video_frame_count  # type: int
        self.voice_antispam_unhandle_count = voice_antispam_unhandle_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementOverviewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_unhandle_count is not None:
            result['AdUnhandleCount'] = self.ad_unhandle_count
        if self.audio_count is not None:
            result['AudioCount'] = self.audio_count
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.live_unhandle_count is not None:
            result['LiveUnhandleCount'] = self.live_unhandle_count
        if self.porn_unhandle_count is not None:
            result['PornUnhandleCount'] = self.porn_unhandle_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.terrorism_unhandle_count is not None:
            result['TerrorismUnhandleCount'] = self.terrorism_unhandle_count
        if self.video_count is not None:
            result['VideoCount'] = self.video_count
        if self.video_frame_count is not None:
            result['VideoFrameCount'] = self.video_frame_count
        if self.voice_antispam_unhandle_count is not None:
            result['VoiceAntispamUnhandleCount'] = self.voice_antispam_unhandle_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdUnhandleCount') is not None:
            self.ad_unhandle_count = m.get('AdUnhandleCount')
        if m.get('AudioCount') is not None:
            self.audio_count = m.get('AudioCount')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('LiveUnhandleCount') is not None:
            self.live_unhandle_count = m.get('LiveUnhandleCount')
        if m.get('PornUnhandleCount') is not None:
            self.porn_unhandle_count = m.get('PornUnhandleCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TerrorismUnhandleCount') is not None:
            self.terrorism_unhandle_count = m.get('TerrorismUnhandleCount')
        if m.get('VideoCount') is not None:
            self.video_count = m.get('VideoCount')
        if m.get('VideoFrameCount') is not None:
            self.video_frame_count = m.get('VideoFrameCount')
        if m.get('VoiceAntispamUnhandleCount') is not None:
            self.voice_antispam_unhandle_count = m.get('VoiceAntispamUnhandleCount')
        return self


class DescribeOssIncrementOverviewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOssIncrementOverviewResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOssIncrementOverviewResponse, self).to_map()
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
            temp_model = DescribeOssIncrementOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssIncrementStatsRequest(TeaModel):
    def __init__(self, end_date=None, lang=None, resource_type=None, scene=None, source_ip=None, start_date=None):
        self.end_date = end_date  # type: str
        self.lang = lang  # type: str
        self.resource_type = resource_type  # type: str
        self.scene = scene  # type: str
        self.source_ip = source_ip  # type: str
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementStatsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeOssIncrementStatsResponseBodyStatList(TeaModel):
    def __init__(self, block_count=None, date=None, pass_count=None, resource_type=None, review_count=None,
                 scene=None, total_count=None):
        self.block_count = block_count  # type: int
        self.date = date  # type: str
        self.pass_count = pass_count  # type: int
        self.resource_type = resource_type  # type: str
        self.review_count = review_count  # type: int
        self.scene = scene  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssIncrementStatsResponseBodyStatList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        if self.date is not None:
            result['Date'] = self.date
        if self.pass_count is not None:
            result['PassCount'] = self.pass_count
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.review_count is not None:
            result['ReviewCount'] = self.review_count
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ReviewCount') is not None:
            self.review_count = m.get('ReviewCount')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOssIncrementStatsResponseBody(TeaModel):
    def __init__(self, request_id=None, stat_list=None, total_count=None):
        self.request_id = request_id  # type: str
        self.stat_list = stat_list  # type: list[DescribeOssIncrementStatsResponseBodyStatList]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.stat_list:
            for k in self.stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOssIncrementStatsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatList'] = []
        if self.stat_list is not None:
            for k in self.stat_list:
                result['StatList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stat_list = []
        if m.get('StatList') is not None:
            for k in m.get('StatList'):
                temp_model = DescribeOssIncrementStatsResponseBodyStatList()
                self.stat_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOssIncrementStatsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOssIncrementStatsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOssIncrementStatsResponse, self).to_map()
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
            temp_model = DescribeOssIncrementStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssResultItemsRequest(TeaModel):
    def __init__(self, bucket=None, current_page=None, end_date=None, lang=None, max_score=None, min_score=None,
                 object=None, page_size=None, query_id=None, resource_type=None, scene=None, source_ip=None,
                 start_date=None, stock=None, stock_task_id=None, suggestion=None, total_count=None):
        self.bucket = bucket  # type: str
        self.current_page = current_page  # type: int
        self.end_date = end_date  # type: str
        self.lang = lang  # type: str
        self.max_score = max_score  # type: float
        self.min_score = min_score  # type: float
        self.object = object  # type: str
        self.page_size = page_size  # type: int
        self.query_id = query_id  # type: str
        self.resource_type = resource_type  # type: str
        self.scene = scene  # type: str
        self.source_ip = source_ip  # type: str
        self.start_date = start_date  # type: str
        self.stock = stock  # type: bool
        self.stock_task_id = stock_task_id  # type: long
        self.suggestion = suggestion  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssResultItemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_score is not None:
            result['MaxScore'] = self.max_score
        if self.min_score is not None:
            result['MinScore'] = self.min_score
        if self.object is not None:
            result['Object'] = self.object
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.stock is not None:
            result['Stock'] = self.stock
        if self.stock_task_id is not None:
            result['StockTaskId'] = self.stock_task_id
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')
        if m.get('MinScore') is not None:
            self.min_score = m.get('MinScore')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Stock') is not None:
            self.stock = m.get('Stock')
        if m.get('StockTaskId') is not None:
            self.stock_task_id = m.get('StockTaskId')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOssResultItemsResponseBodyScanResultListFrameResults(TeaModel):
    def __init__(self, offset=None, thumbnail=None, url=None):
        self.offset = offset  # type: int
        self.thumbnail = thumbnail  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssResultItemsResponseBodyScanResultListFrameResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeOssResultItemsResponseBodyScanResultListVoiceSegmentAntispamResults(TeaModel):
    def __init__(self, end_time=None, label=None, start_time=None, text=None):
        self.end_time = end_time  # type: int
        self.label = label  # type: str
        self.start_time = start_time  # type: int
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssResultItemsResponseBodyScanResultListVoiceSegmentAntispamResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.label is not None:
            result['Label'] = self.label
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class DescribeOssResultItemsResponseBodyScanResultList(TeaModel):
    def __init__(self, bucket=None, content=None, create_time=None, data_id=None, frame_results=None,
                 handle_status=None, id=None, new_url=None, object=None, request_time=None, resource_status=None,
                 scan_finished_time=None, score=None, suggestion=None, task_id=None, thumbnail=None,
                 voice_segment_antispam_results=None):
        self.bucket = bucket  # type: str
        self.content = content  # type: str
        self.create_time = create_time  # type: str
        self.data_id = data_id  # type: str
        self.frame_results = frame_results  # type: list[DescribeOssResultItemsResponseBodyScanResultListFrameResults]
        self.handle_status = handle_status  # type: int
        self.id = id  # type: long
        self.new_url = new_url  # type: str
        self.object = object  # type: str
        self.request_time = request_time  # type: str
        self.resource_status = resource_status  # type: int
        self.scan_finished_time = scan_finished_time  # type: str
        self.score = score  # type: str
        self.suggestion = suggestion  # type: str
        self.task_id = task_id  # type: str
        self.thumbnail = thumbnail  # type: str
        self.voice_segment_antispam_results = voice_segment_antispam_results  # type: list[DescribeOssResultItemsResponseBodyScanResultListVoiceSegmentAntispamResults]

    def validate(self):
        if self.frame_results:
            for k in self.frame_results:
                if k:
                    k.validate()
        if self.voice_segment_antispam_results:
            for k in self.voice_segment_antispam_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOssResultItemsResponseBodyScanResultList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_id is not None:
            result['DataId'] = self.data_id
        result['FrameResults'] = []
        if self.frame_results is not None:
            for k in self.frame_results:
                result['FrameResults'].append(k.to_map() if k else None)
        if self.handle_status is not None:
            result['HandleStatus'] = self.handle_status
        if self.id is not None:
            result['Id'] = self.id
        if self.new_url is not None:
            result['NewUrl'] = self.new_url
        if self.object is not None:
            result['Object'] = self.object
        if self.request_time is not None:
            result['RequestTime'] = self.request_time
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.scan_finished_time is not None:
            result['ScanFinishedTime'] = self.scan_finished_time
        if self.score is not None:
            result['Score'] = self.score
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail
        result['VoiceSegmentAntispamResults'] = []
        if self.voice_segment_antispam_results is not None:
            for k in self.voice_segment_antispam_results:
                result['VoiceSegmentAntispamResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        self.frame_results = []
        if m.get('FrameResults') is not None:
            for k in m.get('FrameResults'):
                temp_model = DescribeOssResultItemsResponseBodyScanResultListFrameResults()
                self.frame_results.append(temp_model.from_map(k))
        if m.get('HandleStatus') is not None:
            self.handle_status = m.get('HandleStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NewUrl') is not None:
            self.new_url = m.get('NewUrl')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ScanFinishedTime') is not None:
            self.scan_finished_time = m.get('ScanFinishedTime')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')
        self.voice_segment_antispam_results = []
        if m.get('VoiceSegmentAntispamResults') is not None:
            for k in m.get('VoiceSegmentAntispamResults'):
                temp_model = DescribeOssResultItemsResponseBodyScanResultListVoiceSegmentAntispamResults()
                self.voice_segment_antispam_results.append(temp_model.from_map(k))
        return self


class DescribeOssResultItemsResponseBody(TeaModel):
    def __init__(self, current_page=None, page_size=None, query_id=None, request_id=None, scan_result_list=None,
                 total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.query_id = query_id  # type: str
        self.request_id = request_id  # type: str
        self.scan_result_list = scan_result_list  # type: list[DescribeOssResultItemsResponseBodyScanResultList]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.scan_result_list:
            for k in self.scan_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOssResultItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ScanResultList'] = []
        if self.scan_result_list is not None:
            for k in self.scan_result_list:
                result['ScanResultList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scan_result_list = []
        if m.get('ScanResultList') is not None:
            for k in m.get('ScanResultList'):
                temp_model = DescribeOssResultItemsResponseBodyScanResultList()
                self.scan_result_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOssResultItemsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOssResultItemsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOssResultItemsResponse, self).to_map()
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
            temp_model = DescribeOssResultItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssStockStatusRequest(TeaModel):
    def __init__(self, lang=None, source_ip=None, stock_task_id=None):
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str
        self.stock_task_id = stock_task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssStockStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.stock_task_id is not None:
            result['StockTaskId'] = self.stock_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StockTaskId') is not None:
            self.stock_task_id = m.get('StockTaskId')
        return self


class DescribeOssStockStatusResponseBodyBucketList(TeaModel):
    def __init__(self, bucket=None, prefixes=None, selected=None):
        self.bucket = bucket  # type: str
        self.prefixes = prefixes  # type: list[str]
        self.selected = selected  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssStockStatusResponseBodyBucketList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.prefixes is not None:
            result['Prefixes'] = self.prefixes
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Prefixes') is not None:
            self.prefixes = m.get('Prefixes')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class DescribeOssStockStatusResponseBody(TeaModel):
    def __init__(self, audio_antispam_count=None, audio_total_count=None, bucket_list=None, finished_time=None,
                 image_ad_count=None, image_live_count=None, image_porn_count=None, image_terrorism_count=None,
                 image_total_count=None, request_id=None, resouce_type_list=None, scene_list=None, stock_status=None,
                 video_ad_count=None, video_live_count=None, video_porn_count=None, video_terrorism_count=None,
                 video_total_count=None, video_voice_antispam_count=None):
        self.audio_antispam_count = audio_antispam_count  # type: int
        self.audio_total_count = audio_total_count  # type: int
        self.bucket_list = bucket_list  # type: list[DescribeOssStockStatusResponseBodyBucketList]
        self.finished_time = finished_time  # type: str
        self.image_ad_count = image_ad_count  # type: int
        self.image_live_count = image_live_count  # type: int
        self.image_porn_count = image_porn_count  # type: int
        self.image_terrorism_count = image_terrorism_count  # type: int
        self.image_total_count = image_total_count  # type: int
        self.request_id = request_id  # type: str
        self.resouce_type_list = resouce_type_list  # type: list[str]
        self.scene_list = scene_list  # type: list[str]
        self.stock_status = stock_status  # type: int
        self.video_ad_count = video_ad_count  # type: int
        self.video_live_count = video_live_count  # type: int
        self.video_porn_count = video_porn_count  # type: int
        self.video_terrorism_count = video_terrorism_count  # type: int
        self.video_total_count = video_total_count  # type: int
        self.video_voice_antispam_count = video_voice_antispam_count  # type: int

    def validate(self):
        if self.bucket_list:
            for k in self.bucket_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOssStockStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_antispam_count is not None:
            result['AudioAntispamCount'] = self.audio_antispam_count
        if self.audio_total_count is not None:
            result['AudioTotalCount'] = self.audio_total_count
        result['BucketList'] = []
        if self.bucket_list is not None:
            for k in self.bucket_list:
                result['BucketList'].append(k.to_map() if k else None)
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.image_ad_count is not None:
            result['ImageAdCount'] = self.image_ad_count
        if self.image_live_count is not None:
            result['ImageLiveCount'] = self.image_live_count
        if self.image_porn_count is not None:
            result['ImagePornCount'] = self.image_porn_count
        if self.image_terrorism_count is not None:
            result['ImageTerrorismCount'] = self.image_terrorism_count
        if self.image_total_count is not None:
            result['ImageTotalCount'] = self.image_total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resouce_type_list is not None:
            result['ResouceTypeList'] = self.resouce_type_list
        if self.scene_list is not None:
            result['SceneList'] = self.scene_list
        if self.stock_status is not None:
            result['StockStatus'] = self.stock_status
        if self.video_ad_count is not None:
            result['VideoAdCount'] = self.video_ad_count
        if self.video_live_count is not None:
            result['VideoLiveCount'] = self.video_live_count
        if self.video_porn_count is not None:
            result['VideoPornCount'] = self.video_porn_count
        if self.video_terrorism_count is not None:
            result['VideoTerrorismCount'] = self.video_terrorism_count
        if self.video_total_count is not None:
            result['VideoTotalCount'] = self.video_total_count
        if self.video_voice_antispam_count is not None:
            result['VideoVoiceAntispamCount'] = self.video_voice_antispam_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioAntispamCount') is not None:
            self.audio_antispam_count = m.get('AudioAntispamCount')
        if m.get('AudioTotalCount') is not None:
            self.audio_total_count = m.get('AudioTotalCount')
        self.bucket_list = []
        if m.get('BucketList') is not None:
            for k in m.get('BucketList'):
                temp_model = DescribeOssStockStatusResponseBodyBucketList()
                self.bucket_list.append(temp_model.from_map(k))
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('ImageAdCount') is not None:
            self.image_ad_count = m.get('ImageAdCount')
        if m.get('ImageLiveCount') is not None:
            self.image_live_count = m.get('ImageLiveCount')
        if m.get('ImagePornCount') is not None:
            self.image_porn_count = m.get('ImagePornCount')
        if m.get('ImageTerrorismCount') is not None:
            self.image_terrorism_count = m.get('ImageTerrorismCount')
        if m.get('ImageTotalCount') is not None:
            self.image_total_count = m.get('ImageTotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResouceTypeList') is not None:
            self.resouce_type_list = m.get('ResouceTypeList')
        if m.get('SceneList') is not None:
            self.scene_list = m.get('SceneList')
        if m.get('StockStatus') is not None:
            self.stock_status = m.get('StockStatus')
        if m.get('VideoAdCount') is not None:
            self.video_ad_count = m.get('VideoAdCount')
        if m.get('VideoLiveCount') is not None:
            self.video_live_count = m.get('VideoLiveCount')
        if m.get('VideoPornCount') is not None:
            self.video_porn_count = m.get('VideoPornCount')
        if m.get('VideoTerrorismCount') is not None:
            self.video_terrorism_count = m.get('VideoTerrorismCount')
        if m.get('VideoTotalCount') is not None:
            self.video_total_count = m.get('VideoTotalCount')
        if m.get('VideoVoiceAntispamCount') is not None:
            self.video_voice_antispam_count = m.get('VideoVoiceAntispamCount')
        return self


class DescribeOssStockStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOssStockStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOssStockStatusResponse, self).to_map()
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
            temp_model = DescribeOssStockStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSdkUrlRequest(TeaModel):
    def __init__(self, debug=None, id=None, lang=None, source_ip=None):
        self.debug = debug  # type: bool
        self.id = id  # type: long
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSdkUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeSdkUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, sdk_url=None):
        self.request_id = request_id  # type: str
        self.sdk_url = sdk_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSdkUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        return self


class DescribeSdkUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSdkUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSdkUrlResponse, self).to_map()
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
            temp_model = DescribeSdkUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUpdatePackageResultRequest(TeaModel):
    def __init__(self, lang=None, source_ip=None, task_id=None):
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUpdatePackageResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeUpdatePackageResultResponseBodyAppInfoDebugPackageInfo(TeaModel):
    def __init__(self, version=None):
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUpdatePackageResultResponseBodyAppInfoDebugPackageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeUpdatePackageResultResponseBodyAppInfoPackageInfo(TeaModel):
    def __init__(self, version=None):
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUpdatePackageResultResponseBodyAppInfoPackageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeUpdatePackageResultResponseBodyAppInfo(TeaModel):
    def __init__(self, debug_package_info=None, end_date=None, icon=None, id=None, name=None, package_info=None,
                 package_name=None, start_date=None, type=None):
        self.debug_package_info = debug_package_info  # type: DescribeUpdatePackageResultResponseBodyAppInfoDebugPackageInfo
        self.end_date = end_date  # type: str
        self.icon = icon  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.package_info = package_info  # type: DescribeUpdatePackageResultResponseBodyAppInfoPackageInfo
        self.package_name = package_name  # type: str
        self.start_date = start_date  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.debug_package_info:
            self.debug_package_info.validate()
        if self.package_info:
            self.package_info.validate()

    def to_map(self):
        _map = super(DescribeUpdatePackageResultResponseBodyAppInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug_package_info is not None:
            result['DebugPackageInfo'] = self.debug_package_info.to_map()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.package_info is not None:
            result['PackageInfo'] = self.package_info.to_map()
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DebugPackageInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseBodyAppInfoDebugPackageInfo()
            self.debug_package_info = temp_model.from_map(m['DebugPackageInfo'])
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseBodyAppInfoPackageInfo()
            self.package_info = temp_model.from_map(m['PackageInfo'])
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeUpdatePackageResultResponseBody(TeaModel):
    def __init__(self, app_info=None, request_id=None):
        self.app_info = app_info  # type: DescribeUpdatePackageResultResponseBodyAppInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.app_info:
            self.app_info.validate()

    def to_map(self):
        _map = super(DescribeUpdatePackageResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_info is not None:
            result['AppInfo'] = self.app_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseBodyAppInfo()
            self.app_info = temp_model.from_map(m['AppInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUpdatePackageResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUpdatePackageResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUpdatePackageResultResponse, self).to_map()
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
            temp_model = DescribeUpdatePackageResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUploadInfoRequest(TeaModel):
    def __init__(self, biz=None, lang=None, source_ip=None):
        self.biz = biz  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUploadInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz is not None:
            result['Biz'] = self.biz
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeUploadInfoResponseBody(TeaModel):
    def __init__(self, accessid=None, expire=None, folder=None, host=None, policy=None, request_id=None,
                 signature=None):
        self.accessid = accessid  # type: str
        self.expire = expire  # type: int
        self.folder = folder  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.request_id = request_id  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUploadInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessid is not None:
            result['Accessid'] = self.accessid
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.folder is not None:
            result['Folder'] = self.folder
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Folder') is not None:
            self.folder = m.get('Folder')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class DescribeUploadInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUploadInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUploadInfoResponse, self).to_map()
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
            temp_model = DescribeUploadInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsageBillRequest(TeaModel):
    def __init__(self, current_page=None, day=None, page_size=None, total_count=None, type=None):
        self.current_page = current_page  # type: int
        self.day = day  # type: str
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsageBillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.day is not None:
            result['Day'] = self.day
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeUsageBillResponseBodyBillList(TeaModel):
    def __init__(self, biz_type=None, confirm_count=None, day=None, free_count=None, region=None, review_count=None,
                 scene=None, sub_uid=None, total_count=None):
        self.biz_type = biz_type  # type: str
        self.confirm_count = confirm_count  # type: long
        self.day = day  # type: str
        self.free_count = free_count  # type: long
        self.region = region  # type: str
        self.review_count = review_count  # type: long
        self.scene = scene  # type: str
        self.sub_uid = sub_uid  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsageBillResponseBodyBillList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.confirm_count is not None:
            result['ConfirmCount'] = self.confirm_count
        if self.day is not None:
            result['Day'] = self.day
        if self.free_count is not None:
            result['FreeCount'] = self.free_count
        if self.region is not None:
            result['Region'] = self.region
        if self.review_count is not None:
            result['ReviewCount'] = self.review_count
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.sub_uid is not None:
            result['SubUid'] = self.sub_uid
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ConfirmCount') is not None:
            self.confirm_count = m.get('ConfirmCount')
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('FreeCount') is not None:
            self.free_count = m.get('FreeCount')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReviewCount') is not None:
            self.review_count = m.get('ReviewCount')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SubUid') is not None:
            self.sub_uid = m.get('SubUid')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUsageBillResponseBody(TeaModel):
    def __init__(self, bill_list=None, current_page=None, page_size=None, request_id=None, total_count=None):
        self.bill_list = bill_list  # type: list[DescribeUsageBillResponseBodyBillList]
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.bill_list:
            for k in self.bill_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUsageBillResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BillList'] = []
        if self.bill_list is not None:
            for k in self.bill_list:
                result['BillList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bill_list = []
        if m.get('BillList') is not None:
            for k in m.get('BillList'):
                temp_model = DescribeUsageBillResponseBodyBillList()
                self.bill_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUsageBillResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUsageBillResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUsageBillResponse, self).to_map()
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
            temp_model = DescribeUsageBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserBizTypesRequest(TeaModel):
    def __init__(self, customized=None):
        self.customized = customized  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserBizTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customized is not None:
            result['Customized'] = self.customized
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Customized') is not None:
            self.customized = m.get('Customized')
        return self


class DescribeUserBizTypesResponseBodyBizTypeList(TeaModel):
    def __init__(self, biz_type=None, cite_template=None, description=None, gray=None, industry_info=None,
                 source=None, source_biz_type=None):
        self.biz_type = biz_type  # type: str
        self.cite_template = cite_template  # type: bool
        self.description = description  # type: str
        self.gray = gray  # type: bool
        self.industry_info = industry_info  # type: str
        self.source = source  # type: str
        self.source_biz_type = source_biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserBizTypesResponseBodyBizTypeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.cite_template is not None:
            result['CiteTemplate'] = self.cite_template
        if self.description is not None:
            result['Description'] = self.description
        if self.gray is not None:
            result['Gray'] = self.gray
        if self.industry_info is not None:
            result['IndustryInfo'] = self.industry_info
        if self.source is not None:
            result['Source'] = self.source
        if self.source_biz_type is not None:
            result['SourceBizType'] = self.source_biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CiteTemplate') is not None:
            self.cite_template = m.get('CiteTemplate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Gray') is not None:
            self.gray = m.get('Gray')
        if m.get('IndustryInfo') is not None:
            self.industry_info = m.get('IndustryInfo')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceBizType') is not None:
            self.source_biz_type = m.get('SourceBizType')
        return self


class DescribeUserBizTypesResponseBodyBizTypeListImport(TeaModel):
    def __init__(self, biz_type=None, cite_template=None, description=None, gray=None, industry_info=None,
                 source=None, source_biz_type=None):
        self.biz_type = biz_type  # type: str
        self.cite_template = cite_template  # type: bool
        self.description = description  # type: str
        self.gray = gray  # type: bool
        self.industry_info = industry_info  # type: str
        self.source = source  # type: str
        self.source_biz_type = source_biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserBizTypesResponseBodyBizTypeListImport, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.cite_template is not None:
            result['CiteTemplate'] = self.cite_template
        if self.description is not None:
            result['Description'] = self.description
        if self.gray is not None:
            result['Gray'] = self.gray
        if self.industry_info is not None:
            result['IndustryInfo'] = self.industry_info
        if self.source is not None:
            result['Source'] = self.source
        if self.source_biz_type is not None:
            result['SourceBizType'] = self.source_biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CiteTemplate') is not None:
            self.cite_template = m.get('CiteTemplate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Gray') is not None:
            self.gray = m.get('Gray')
        if m.get('IndustryInfo') is not None:
            self.industry_info = m.get('IndustryInfo')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceBizType') is not None:
            self.source_biz_type = m.get('SourceBizType')
        return self


class DescribeUserBizTypesResponseBody(TeaModel):
    def __init__(self, biz_type_list=None, biz_type_list_import=None, request_id=None):
        self.biz_type_list = biz_type_list  # type: list[DescribeUserBizTypesResponseBodyBizTypeList]
        self.biz_type_list_import = biz_type_list_import  # type: list[DescribeUserBizTypesResponseBodyBizTypeListImport]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.biz_type_list:
            for k in self.biz_type_list:
                if k:
                    k.validate()
        if self.biz_type_list_import:
            for k in self.biz_type_list_import:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUserBizTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BizTypeList'] = []
        if self.biz_type_list is not None:
            for k in self.biz_type_list:
                result['BizTypeList'].append(k.to_map() if k else None)
        result['BizTypeListImport'] = []
        if self.biz_type_list_import is not None:
            for k in self.biz_type_list_import:
                result['BizTypeListImport'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.biz_type_list = []
        if m.get('BizTypeList') is not None:
            for k in m.get('BizTypeList'):
                temp_model = DescribeUserBizTypesResponseBodyBizTypeList()
                self.biz_type_list.append(temp_model.from_map(k))
        self.biz_type_list_import = []
        if m.get('BizTypeListImport') is not None:
            for k in m.get('BizTypeListImport'):
                temp_model = DescribeUserBizTypesResponseBodyBizTypeListImport()
                self.biz_type_list_import.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserBizTypesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUserBizTypesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserBizTypesResponse, self).to_map()
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
            temp_model = DescribeUserBizTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserStatusRequest(TeaModel):
    def __init__(self, lang=None, source_ip=None):
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeUserStatusResponseBody(TeaModel):
    def __init__(self, agree_channel=None, buyed=None, in_dept=None, open_api_begin_time=None, open_api_used=None,
                 oss_check_status=None, oss_video_size_limit=None, request_id=None, uid=None):
        self.agree_channel = agree_channel  # type: int
        self.buyed = buyed  # type: bool
        self.in_dept = in_dept  # type: bool
        self.open_api_begin_time = open_api_begin_time  # type: str
        self.open_api_used = open_api_used  # type: bool
        self.oss_check_status = oss_check_status  # type: str
        self.oss_video_size_limit = oss_video_size_limit  # type: int
        self.request_id = request_id  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agree_channel is not None:
            result['AgreeChannel'] = self.agree_channel
        if self.buyed is not None:
            result['Buyed'] = self.buyed
        if self.in_dept is not None:
            result['InDept'] = self.in_dept
        if self.open_api_begin_time is not None:
            result['OpenApiBeginTime'] = self.open_api_begin_time
        if self.open_api_used is not None:
            result['OpenApiUsed'] = self.open_api_used
        if self.oss_check_status is not None:
            result['OssCheckStatus'] = self.oss_check_status
        if self.oss_video_size_limit is not None:
            result['OssVideoSizeLimit'] = self.oss_video_size_limit
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgreeChannel') is not None:
            self.agree_channel = m.get('AgreeChannel')
        if m.get('Buyed') is not None:
            self.buyed = m.get('Buyed')
        if m.get('InDept') is not None:
            self.in_dept = m.get('InDept')
        if m.get('OpenApiBeginTime') is not None:
            self.open_api_begin_time = m.get('OpenApiBeginTime')
        if m.get('OpenApiUsed') is not None:
            self.open_api_used = m.get('OpenApiUsed')
        if m.get('OssCheckStatus') is not None:
            self.oss_check_status = m.get('OssCheckStatus')
        if m.get('OssVideoSizeLimit') is not None:
            self.oss_video_size_limit = m.get('OssVideoSizeLimit')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeUserStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUserStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserStatusResponse, self).to_map()
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
            temp_model = DescribeUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeViewContentRequest(TeaModel):
    def __init__(self, audit_result=None, biz_type=None, current_page=None, data_id=None, end_date=None,
                 image_id=None, keyword=None, keyword_id=None, label=None, lib_type=None, page_size=None, resource_type=None,
                 scene=None, start_date=None, suggestion=None, task_id=None, total_count=None):
        self.audit_result = audit_result  # type: str
        self.biz_type = biz_type  # type: str
        self.current_page = current_page  # type: int
        self.data_id = data_id  # type: str
        self.end_date = end_date  # type: str
        self.image_id = image_id  # type: str
        self.keyword = keyword  # type: str
        self.keyword_id = keyword_id  # type: str
        self.label = label  # type: str
        self.lib_type = lib_type  # type: str
        self.page_size = page_size  # type: int
        self.resource_type = resource_type  # type: str
        self.scene = scene  # type: str
        self.start_date = start_date  # type: str
        self.suggestion = suggestion  # type: str
        self.task_id = task_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.keyword_id is not None:
            result['KeywordId'] = self.keyword_id
        if self.label is not None:
            result['Label'] = self.label
        if self.lib_type is not None:
            result['LibType'] = self.lib_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('KeywordId') is not None:
            self.keyword_id = m.get('KeywordId')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LibType') is not None:
            self.lib_type = m.get('LibType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsAge(TeaModel):
    def __init__(self, rate=None, value=None):
        self.rate = rate  # type: float
        self.value = value  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListFaceResultsAge, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsBang(TeaModel):
    def __init__(self, rate=None, value=None):
        self.rate = rate  # type: float
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListFaceResultsBang, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsGender(TeaModel):
    def __init__(self, rate=None, value=None):
        self.rate = rate  # type: float
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListFaceResultsGender, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsGlasses(TeaModel):
    def __init__(self, rate=None, value=None):
        self.rate = rate  # type: float
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListFaceResultsGlasses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsHairstyle(TeaModel):
    def __init__(self, rate=None, value=None):
        self.rate = rate  # type: float
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListFaceResultsHairstyle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsHat(TeaModel):
    def __init__(self, rate=None, value=None):
        self.rate = rate  # type: float
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListFaceResultsHat, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsImage(TeaModel):
    def __init__(self, height=None, width=None):
        self.height = height  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListFaceResultsImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsLocation(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        self.h = h  # type: int
        self.w = w  # type: int
        self.x = x  # type: int
        self.y = y  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListFaceResultsLocation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['H'] = self.h
        if self.w is not None:
            result['W'] = self.w
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsMustache(TeaModel):
    def __init__(self, rate=None, value=None):
        self.rate = rate  # type: float
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListFaceResultsMustache, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsQuality(TeaModel):
    def __init__(self, blur=None, pitch=None, roll=None, yaw=None):
        self.blur = blur  # type: float
        self.pitch = pitch  # type: float
        self.roll = roll  # type: float
        self.yaw = yaw  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListFaceResultsQuality, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blur is not None:
            result['Blur'] = self.blur
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Blur') is not None:
            self.blur = m.get('Blur')
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsRespirator(TeaModel):
    def __init__(self, rate=None, value=None):
        self.rate = rate  # type: float
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListFaceResultsRespirator, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsSmile(TeaModel):
    def __init__(self, rate=None, value=None):
        self.rate = rate  # type: float
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListFaceResultsSmile, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResults(TeaModel):
    def __init__(self, age=None, bang=None, bualified=None, gender=None, glasses=None, hairstyle=None, hat=None,
                 image=None, location=None, mustache=None, quality=None, respirator=None, smile=None):
        self.age = age  # type: DescribeViewContentResponseBodyViewContentListFaceResultsAge
        self.bang = bang  # type: DescribeViewContentResponseBodyViewContentListFaceResultsBang
        self.bualified = bualified  # type: bool
        self.gender = gender  # type: DescribeViewContentResponseBodyViewContentListFaceResultsGender
        self.glasses = glasses  # type: DescribeViewContentResponseBodyViewContentListFaceResultsGlasses
        self.hairstyle = hairstyle  # type: DescribeViewContentResponseBodyViewContentListFaceResultsHairstyle
        self.hat = hat  # type: DescribeViewContentResponseBodyViewContentListFaceResultsHat
        self.image = image  # type: DescribeViewContentResponseBodyViewContentListFaceResultsImage
        self.location = location  # type: DescribeViewContentResponseBodyViewContentListFaceResultsLocation
        self.mustache = mustache  # type: DescribeViewContentResponseBodyViewContentListFaceResultsMustache
        self.quality = quality  # type: DescribeViewContentResponseBodyViewContentListFaceResultsQuality
        self.respirator = respirator  # type: DescribeViewContentResponseBodyViewContentListFaceResultsRespirator
        self.smile = smile  # type: DescribeViewContentResponseBodyViewContentListFaceResultsSmile

    def validate(self):
        if self.age:
            self.age.validate()
        if self.bang:
            self.bang.validate()
        if self.gender:
            self.gender.validate()
        if self.glasses:
            self.glasses.validate()
        if self.hairstyle:
            self.hairstyle.validate()
        if self.hat:
            self.hat.validate()
        if self.image:
            self.image.validate()
        if self.location:
            self.location.validate()
        if self.mustache:
            self.mustache.validate()
        if self.quality:
            self.quality.validate()
        if self.respirator:
            self.respirator.validate()
        if self.smile:
            self.smile.validate()

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListFaceResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age is not None:
            result['Age'] = self.age.to_map()
        if self.bang is not None:
            result['Bang'] = self.bang.to_map()
        if self.bualified is not None:
            result['Bualified'] = self.bualified
        if self.gender is not None:
            result['Gender'] = self.gender.to_map()
        if self.glasses is not None:
            result['Glasses'] = self.glasses.to_map()
        if self.hairstyle is not None:
            result['Hairstyle'] = self.hairstyle.to_map()
        if self.hat is not None:
            result['Hat'] = self.hat.to_map()
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.mustache is not None:
            result['Mustache'] = self.mustache.to_map()
        if self.quality is not None:
            result['Quality'] = self.quality.to_map()
        if self.respirator is not None:
            result['Respirator'] = self.respirator.to_map()
        if self.smile is not None:
            result['Smile'] = self.smile.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Age') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsAge()
            self.age = temp_model.from_map(m['Age'])
        if m.get('Bang') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsBang()
            self.bang = temp_model.from_map(m['Bang'])
        if m.get('Bualified') is not None:
            self.bualified = m.get('Bualified')
        if m.get('Gender') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsGender()
            self.gender = temp_model.from_map(m['Gender'])
        if m.get('Glasses') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsGlasses()
            self.glasses = temp_model.from_map(m['Glasses'])
        if m.get('Hairstyle') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsHairstyle()
            self.hairstyle = temp_model.from_map(m['Hairstyle'])
        if m.get('Hat') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsHat()
            self.hat = temp_model.from_map(m['Hat'])
        if m.get('Image') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('Location') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Mustache') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsMustache()
            self.mustache = temp_model.from_map(m['Mustache'])
        if m.get('Quality') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsQuality()
            self.quality = temp_model.from_map(m['Quality'])
        if m.get('Respirator') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsRespirator()
            self.respirator = temp_model.from_map(m['Respirator'])
        if m.get('Smile') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsSmile()
            self.smile = temp_model.from_map(m['Smile'])
        return self


class DescribeViewContentResponseBodyViewContentListFrameResults(TeaModel):
    def __init__(self, label=None, offset=None, url=None):
        self.label = label  # type: str
        self.offset = offset  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListFrameResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeViewContentResponseBodyViewContentListResults(TeaModel):
    def __init__(self, label=None, scene=None, suggestion=None):
        self.label = label  # type: str
        self.scene = scene  # type: str
        self.suggestion = suggestion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentListResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class DescribeViewContentResponseBodyViewContentList(TeaModel):
    def __init__(self, biz_type=None, content=None, data_id=None, face_results=None, frame_results=None, id=None,
                 new_url=None, request_time=None, results=None, scan_finished_time=None, scan_result=None, suggestion=None,
                 task_id=None, thumbnail=None, url=None):
        self.biz_type = biz_type  # type: str
        self.content = content  # type: str
        self.data_id = data_id  # type: str
        self.face_results = face_results  # type: list[DescribeViewContentResponseBodyViewContentListFaceResults]
        self.frame_results = frame_results  # type: list[DescribeViewContentResponseBodyViewContentListFrameResults]
        self.id = id  # type: long
        self.new_url = new_url  # type: str
        self.request_time = request_time  # type: str
        self.results = results  # type: list[DescribeViewContentResponseBodyViewContentListResults]
        self.scan_finished_time = scan_finished_time  # type: str
        self.scan_result = scan_result  # type: str
        self.suggestion = suggestion  # type: str
        self.task_id = task_id  # type: str
        self.thumbnail = thumbnail  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.face_results:
            for k in self.face_results:
                if k:
                    k.validate()
        if self.frame_results:
            for k in self.frame_results:
                if k:
                    k.validate()
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeViewContentResponseBodyViewContentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.content is not None:
            result['Content'] = self.content
        if self.data_id is not None:
            result['DataId'] = self.data_id
        result['FaceResults'] = []
        if self.face_results is not None:
            for k in self.face_results:
                result['FaceResults'].append(k.to_map() if k else None)
        result['FrameResults'] = []
        if self.frame_results is not None:
            for k in self.frame_results:
                result['FrameResults'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.new_url is not None:
            result['NewUrl'] = self.new_url
        if self.request_time is not None:
            result['RequestTime'] = self.request_time
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.scan_finished_time is not None:
            result['ScanFinishedTime'] = self.scan_finished_time
        if self.scan_result is not None:
            result['ScanResult'] = self.scan_result
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        self.face_results = []
        if m.get('FaceResults') is not None:
            for k in m.get('FaceResults'):
                temp_model = DescribeViewContentResponseBodyViewContentListFaceResults()
                self.face_results.append(temp_model.from_map(k))
        self.frame_results = []
        if m.get('FrameResults') is not None:
            for k in m.get('FrameResults'):
                temp_model = DescribeViewContentResponseBodyViewContentListFrameResults()
                self.frame_results.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NewUrl') is not None:
            self.new_url = m.get('NewUrl')
        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DescribeViewContentResponseBodyViewContentListResults()
                self.results.append(temp_model.from_map(k))
        if m.get('ScanFinishedTime') is not None:
            self.scan_finished_time = m.get('ScanFinishedTime')
        if m.get('ScanResult') is not None:
            self.scan_result = m.get('ScanResult')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeViewContentResponseBody(TeaModel):
    def __init__(self, current_page=None, page_size=None, request_id=None, total_count=None, view_content_list=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.view_content_list = view_content_list  # type: list[DescribeViewContentResponseBodyViewContentList]

    def validate(self):
        if self.view_content_list:
            for k in self.view_content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeViewContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['ViewContentList'] = []
        if self.view_content_list is not None:
            for k in self.view_content_list:
                result['ViewContentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.view_content_list = []
        if m.get('ViewContentList') is not None:
            for k in m.get('ViewContentList'):
                temp_model = DescribeViewContentResponseBodyViewContentList()
                self.view_content_list.append(temp_model.from_map(k))
        return self


class DescribeViewContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeViewContentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeViewContentResponse, self).to_map()
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
            temp_model = DescribeViewContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteIndexPageBaselineRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, source_ip=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteIndexPageBaselineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeWebsiteIndexPageBaselineResponseBody(TeaModel):
    def __init__(self, base_line_status=None, create_time=None, request_id=None, snapshot=None):
        self.base_line_status = base_line_status  # type: str
        self.create_time = create_time  # type: str
        self.request_id = request_id  # type: str
        self.snapshot = snapshot  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteIndexPageBaselineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_line_status is not None:
            result['BaseLineStatus'] = self.base_line_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BaseLineStatus') is not None:
            self.base_line_status = m.get('BaseLineStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')
        return self


class DescribeWebsiteIndexPageBaselineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebsiteIndexPageBaselineResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebsiteIndexPageBaselineResponse, self).to_map()
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
            temp_model = DescribeWebsiteIndexPageBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteInstanceRequest(TeaModel):
    def __init__(self, current_page=None, instance_id=None, lang=None, page_size=None, source_ip=None,
                 total_count=None):
        self.current_page = current_page  # type: int
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.page_size = page_size  # type: int
        self.source_ip = source_ip  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeWebsiteInstanceResponseBodyWebsiteInstanceList(TeaModel):
    def __init__(self, buy_time=None, domain=None, expired_time=None, index_page=None,
                 index_page_scan_interval=None, instance_id=None, protocol=None, status=None, website_scan_interval=None):
        self.buy_time = buy_time  # type: str
        self.domain = domain  # type: str
        self.expired_time = expired_time  # type: str
        self.index_page = index_page  # type: str
        self.index_page_scan_interval = index_page_scan_interval  # type: int
        self.instance_id = instance_id  # type: str
        self.protocol = protocol  # type: str
        self.status = status  # type: str
        self.website_scan_interval = website_scan_interval  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteInstanceResponseBodyWebsiteInstanceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_time is not None:
            result['BuyTime'] = self.buy_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.index_page is not None:
            result['IndexPage'] = self.index_page
        if self.index_page_scan_interval is not None:
            result['IndexPageScanInterval'] = self.index_page_scan_interval
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.website_scan_interval is not None:
            result['WebsiteScanInterval'] = self.website_scan_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuyTime') is not None:
            self.buy_time = m.get('BuyTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('IndexPage') is not None:
            self.index_page = m.get('IndexPage')
        if m.get('IndexPageScanInterval') is not None:
            self.index_page_scan_interval = m.get('IndexPageScanInterval')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WebsiteScanInterval') is not None:
            self.website_scan_interval = m.get('WebsiteScanInterval')
        return self


class DescribeWebsiteInstanceResponseBody(TeaModel):
    def __init__(self, current_page=None, page_size=None, request_id=None, total_count=None,
                 website_instance_list=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.website_instance_list = website_instance_list  # type: list[DescribeWebsiteInstanceResponseBodyWebsiteInstanceList]

    def validate(self):
        if self.website_instance_list:
            for k in self.website_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebsiteInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WebsiteInstanceList'] = []
        if self.website_instance_list is not None:
            for k in self.website_instance_list:
                result['WebsiteInstanceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.website_instance_list = []
        if m.get('WebsiteInstanceList') is not None:
            for k in m.get('WebsiteInstanceList'):
                temp_model = DescribeWebsiteInstanceResponseBodyWebsiteInstanceList()
                self.website_instance_list.append(temp_model.from_map(k))
        return self


class DescribeWebsiteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebsiteInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebsiteInstanceResponse, self).to_map()
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
            temp_model = DescribeWebsiteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteInstanceIdRequest(TeaModel):
    def __init__(self, lang=None, source_ip=None):
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteInstanceIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeWebsiteInstanceIdResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, website_instance_id_list=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.website_instance_id_list = website_instance_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteInstanceIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.website_instance_id_list is not None:
            result['WebsiteInstanceIdList'] = self.website_instance_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('WebsiteInstanceIdList') is not None:
            self.website_instance_id_list = m.get('WebsiteInstanceIdList')
        return self


class DescribeWebsiteInstanceIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebsiteInstanceIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebsiteInstanceIdResponse, self).to_map()
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
            temp_model = DescribeWebsiteInstanceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteInstanceKeyUrlRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, source_ip=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteInstanceKeyUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeWebsiteInstanceKeyUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, website_instance_key_url_list=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.website_instance_key_url_list = website_instance_key_url_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteInstanceKeyUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.website_instance_key_url_list is not None:
            result['WebsiteInstanceKeyUrlList'] = self.website_instance_key_url_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('WebsiteInstanceKeyUrlList') is not None:
            self.website_instance_key_url_list = m.get('WebsiteInstanceKeyUrlList')
        return self


class DescribeWebsiteInstanceKeyUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebsiteInstanceKeyUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebsiteInstanceKeyUrlResponse, self).to_map()
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
            temp_model = DescribeWebsiteInstanceKeyUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteScanResultRequest(TeaModel):
    def __init__(self, current_page=None, domain=None, handle_status=None, label=None, lang=None, page_size=None,
                 site_url=None, source_ip=None, sub_service_module=None, total_count=None):
        self.current_page = current_page  # type: int
        self.domain = domain  # type: str
        self.handle_status = handle_status  # type: str
        self.label = label  # type: str
        self.lang = lang  # type: str
        self.page_size = page_size  # type: int
        self.site_url = site_url  # type: str
        self.source_ip = source_ip  # type: str
        self.sub_service_module = sub_service_module  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteScanResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.handle_status is not None:
            result['HandleStatus'] = self.handle_status
        if self.label is not None:
            result['Label'] = self.label
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.site_url is not None:
            result['SiteUrl'] = self.site_url
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.sub_service_module is not None:
            result['SubServiceModule'] = self.sub_service_module
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('HandleStatus') is not None:
            self.handle_status = m.get('HandleStatus')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SiteUrl') is not None:
            self.site_url = m.get('SiteUrl')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SubServiceModule') is not None:
            self.sub_service_module = m.get('SubServiceModule')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeWebsiteScanResultResponseBodyWebsiteScanResultList(TeaModel):
    def __init__(self, domain=None, handle_status=None, id=None, image_risk_count=None, instance_id=None,
                 labels=None, scan_time=None, source_risk_count=None, task_id=None, text_risk_count=None, url=None):
        self.domain = domain  # type: str
        self.handle_status = handle_status  # type: int
        self.id = id  # type: int
        self.image_risk_count = image_risk_count  # type: int
        self.instance_id = instance_id  # type: str
        self.labels = labels  # type: list[str]
        self.scan_time = scan_time  # type: str
        self.source_risk_count = source_risk_count  # type: int
        self.task_id = task_id  # type: str
        self.text_risk_count = text_risk_count  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteScanResultResponseBodyWebsiteScanResultList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.handle_status is not None:
            result['HandleStatus'] = self.handle_status
        if self.id is not None:
            result['Id'] = self.id
        if self.image_risk_count is not None:
            result['ImageRiskCount'] = self.image_risk_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.scan_time is not None:
            result['ScanTime'] = self.scan_time
        if self.source_risk_count is not None:
            result['SourceRiskCount'] = self.source_risk_count
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.text_risk_count is not None:
            result['TextRiskCount'] = self.text_risk_count
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('HandleStatus') is not None:
            self.handle_status = m.get('HandleStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageRiskCount') is not None:
            self.image_risk_count = m.get('ImageRiskCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ScanTime') is not None:
            self.scan_time = m.get('ScanTime')
        if m.get('SourceRiskCount') is not None:
            self.source_risk_count = m.get('SourceRiskCount')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TextRiskCount') is not None:
            self.text_risk_count = m.get('TextRiskCount')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeWebsiteScanResultResponseBody(TeaModel):
    def __init__(self, current_page=None, page_size=None, request_id=None, total_count=None,
                 website_scan_result_list=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.website_scan_result_list = website_scan_result_list  # type: list[DescribeWebsiteScanResultResponseBodyWebsiteScanResultList]

    def validate(self):
        if self.website_scan_result_list:
            for k in self.website_scan_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebsiteScanResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WebsiteScanResultList'] = []
        if self.website_scan_result_list is not None:
            for k in self.website_scan_result_list:
                result['WebsiteScanResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.website_scan_result_list = []
        if m.get('WebsiteScanResultList') is not None:
            for k in m.get('WebsiteScanResultList'):
                temp_model = DescribeWebsiteScanResultResponseBodyWebsiteScanResultList()
                self.website_scan_result_list.append(temp_model.from_map(k))
        return self


class DescribeWebsiteScanResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebsiteScanResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebsiteScanResultResponse, self).to_map()
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
            temp_model = DescribeWebsiteScanResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteScanResultDetailRequest(TeaModel):
    def __init__(self, id=None, lang=None, resource_type=None, source_ip=None):
        self.id = id  # type: int
        self.lang = lang  # type: str
        self.resource_type = resource_type  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteScanResultDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeWebsiteScanResultDetailResponseBodyImageScanResults(TeaModel):
    def __init__(self, labels=None, url=None):
        self.labels = labels  # type: list[str]
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteScanResultDetailResponseBodyImageScanResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeWebsiteScanResultDetailResponseBody(TeaModel):
    def __init__(self, baseline=None, content=None, hit_keywords=None, image_scan_results=None, request_id=None,
                 resource_type=None, tampered_source=None):
        self.baseline = baseline  # type: str
        self.content = content  # type: str
        self.hit_keywords = hit_keywords  # type: list[str]
        self.image_scan_results = image_scan_results  # type: list[DescribeWebsiteScanResultDetailResponseBodyImageScanResults]
        self.request_id = request_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tampered_source = tampered_source  # type: str

    def validate(self):
        if self.image_scan_results:
            for k in self.image_scan_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebsiteScanResultDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline is not None:
            result['Baseline'] = self.baseline
        if self.content is not None:
            result['Content'] = self.content
        if self.hit_keywords is not None:
            result['HitKeywords'] = self.hit_keywords
        result['ImageScanResults'] = []
        if self.image_scan_results is not None:
            for k in self.image_scan_results:
                result['ImageScanResults'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tampered_source is not None:
            result['TamperedSource'] = self.tampered_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Baseline') is not None:
            self.baseline = m.get('Baseline')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('HitKeywords') is not None:
            self.hit_keywords = m.get('HitKeywords')
        self.image_scan_results = []
        if m.get('ImageScanResults') is not None:
            for k in m.get('ImageScanResults'):
                temp_model = DescribeWebsiteScanResultDetailResponseBodyImageScanResults()
                self.image_scan_results.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TamperedSource') is not None:
            self.tampered_source = m.get('TamperedSource')
        return self


class DescribeWebsiteScanResultDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebsiteScanResultDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebsiteScanResultDetailResponse, self).to_map()
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
            temp_model = DescribeWebsiteScanResultDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteStatRequest(TeaModel):
    def __init__(self, lang=None, source_ip=None):
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteStatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeWebsiteStatResponseBodyWebsiteStatList(TeaModel):
    def __init__(self, instance_count=None, risk_count=None, scan_count=None, sub_service_module=None):
        self.instance_count = instance_count  # type: int
        self.risk_count = risk_count  # type: int
        self.scan_count = scan_count  # type: int
        self.sub_service_module = sub_service_module  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteStatResponseBodyWebsiteStatList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.scan_count is not None:
            result['ScanCount'] = self.scan_count
        if self.sub_service_module is not None:
            result['SubServiceModule'] = self.sub_service_module
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('ScanCount') is not None:
            self.scan_count = m.get('ScanCount')
        if m.get('SubServiceModule') is not None:
            self.sub_service_module = m.get('SubServiceModule')
        return self


class DescribeWebsiteStatResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, website_stat_list=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.website_stat_list = website_stat_list  # type: list[DescribeWebsiteStatResponseBodyWebsiteStatList]

    def validate(self):
        if self.website_stat_list:
            for k in self.website_stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebsiteStatResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WebsiteStatList'] = []
        if self.website_stat_list is not None:
            for k in self.website_stat_list:
                result['WebsiteStatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.website_stat_list = []
        if m.get('WebsiteStatList') is not None:
            for k in m.get('WebsiteStatList'):
                temp_model = DescribeWebsiteStatResponseBodyWebsiteStatList()
                self.website_stat_list.append(temp_model.from_map(k))
        return self


class DescribeWebsiteStatResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebsiteStatResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebsiteStatResponse, self).to_map()
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
            temp_model = DescribeWebsiteStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteVerifyInfoRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, source_ip=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteVerifyInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeWebsiteVerifyInfoResponseBody(TeaModel):
    def __init__(self, cname=None, domain=None, host_file=None, index_page=None, protocol=None, request_id=None,
                 verify_method=None):
        self.cname = cname  # type: str
        self.domain = domain  # type: str
        self.host_file = host_file  # type: str
        self.index_page = index_page  # type: str
        self.protocol = protocol  # type: str
        self.request_id = request_id  # type: str
        self.verify_method = verify_method  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebsiteVerifyInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.host_file is not None:
            result['HostFile'] = self.host_file
        if self.index_page is not None:
            result['IndexPage'] = self.index_page
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_method is not None:
            result['VerifyMethod'] = self.verify_method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('HostFile') is not None:
            self.host_file = m.get('HostFile')
        if m.get('IndexPage') is not None:
            self.index_page = m.get('IndexPage')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyMethod') is not None:
            self.verify_method = m.get('VerifyMethod')
        return self


class DescribeWebsiteVerifyInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebsiteVerifyInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebsiteVerifyInfoResponse, self).to_map()
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
            temp_model = DescribeWebsiteVerifyInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportKeywordsRequest(TeaModel):
    def __init__(self, keyword_lib_id=None):
        self.keyword_lib_id = keyword_lib_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportKeywordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword_lib_id is not None:
            result['KeywordLibId'] = self.keyword_lib_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeywordLibId') is not None:
            self.keyword_lib_id = m.get('KeywordLibId')
        return self


class ExportKeywordsResponseBody(TeaModel):
    def __init__(self, download_url=None, request_id=None):
        self.download_url = download_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportKeywordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportKeywordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExportKeywordsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportKeywordsResponse, self).to_map()
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
            temp_model = ExportKeywordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportOpenApiRcpStatsRequest(TeaModel):
    def __init__(self, biz_type=None, end_date=None, resource_type=None, start_date=None):
        self.biz_type = biz_type  # type: str
        self.end_date = end_date  # type: str
        self.resource_type = resource_type  # type: str
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportOpenApiRcpStatsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ExportOpenApiRcpStatsResponseBody(TeaModel):
    def __init__(self, download_url=None, request_id=None):
        self.download_url = download_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportOpenApiRcpStatsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportOpenApiRcpStatsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExportOpenApiRcpStatsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportOpenApiRcpStatsResponse, self).to_map()
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
            temp_model = ExportOpenApiRcpStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportOssResultRequest(TeaModel):
    def __init__(self, bucket=None, current_page=None, end_date=None, lang=None, max_score=None, min_score=None,
                 page_size=None, resource_type=None, scene=None, source_ip=None, start_date=None, stock=None,
                 stock_task_id=None, suggestion=None, total_count=None):
        self.bucket = bucket  # type: str
        self.current_page = current_page  # type: int
        self.end_date = end_date  # type: str
        self.lang = lang  # type: str
        self.max_score = max_score  # type: float
        self.min_score = min_score  # type: float
        self.page_size = page_size  # type: int
        self.resource_type = resource_type  # type: str
        self.scene = scene  # type: str
        self.source_ip = source_ip  # type: str
        self.start_date = start_date  # type: str
        self.stock = stock  # type: bool
        self.stock_task_id = stock_task_id  # type: long
        self.suggestion = suggestion  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportOssResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_score is not None:
            result['MaxScore'] = self.max_score
        if self.min_score is not None:
            result['MinScore'] = self.min_score
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.stock is not None:
            result['Stock'] = self.stock
        if self.stock_task_id is not None:
            result['StockTaskId'] = self.stock_task_id
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')
        if m.get('MinScore') is not None:
            self.min_score = m.get('MinScore')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Stock') is not None:
            self.stock = m.get('Stock')
        if m.get('StockTaskId') is not None:
            self.stock_task_id = m.get('StockTaskId')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ExportOssResultResponseBody(TeaModel):
    def __init__(self, file_url=None, request_id=None):
        self.file_url = file_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportOssResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportOssResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExportOssResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportOssResultResponse, self).to_map()
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
            temp_model = ExportOssResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuditItemDetailRequest(TeaModel):
    def __init__(self, task_id=None, type=None):
        self.task_id = task_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuditItemDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAuditItemDetailResponseBody(TeaModel):
    def __init__(self, api_result=None, api_risk_type=None, api_ts=None, new_url=None, request_id=None):
        self.api_result = api_result  # type: str
        self.api_risk_type = api_risk_type  # type: str
        self.api_ts = api_ts  # type: str
        self.new_url = new_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuditItemDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_result is not None:
            result['ApiResult'] = self.api_result
        if self.api_risk_type is not None:
            result['ApiRiskType'] = self.api_risk_type
        if self.api_ts is not None:
            result['ApiTs'] = self.api_ts
        if self.new_url is not None:
            result['NewUrl'] = self.new_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiResult') is not None:
            self.api_result = m.get('ApiResult')
        if m.get('ApiRiskType') is not None:
            self.api_risk_type = m.get('ApiRiskType')
        if m.get('ApiTs') is not None:
            self.api_ts = m.get('ApiTs')
        if m.get('NewUrl') is not None:
            self.new_url = m.get('NewUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAuditItemDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAuditItemDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAuditItemDetailResponse, self).to_map()
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
            temp_model = GetAuditItemDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuditItemListRequest(TeaModel):
    def __init__(self, biz_type=None, current_page=None, custom_result=None, custom_risk_type=None, data_id=None,
                 end_date=None, page_size=None, rcp_result=None, rcp_risk_type=None, start_date=None, task_id=None, type=None):
        self.biz_type = biz_type  # type: str
        self.current_page = current_page  # type: long
        self.custom_result = custom_result  # type: str
        self.custom_risk_type = custom_risk_type  # type: str
        self.data_id = data_id  # type: str
        self.end_date = end_date  # type: str
        self.page_size = page_size  # type: long
        self.rcp_result = rcp_result  # type: str
        self.rcp_risk_type = rcp_risk_type  # type: str
        self.start_date = start_date  # type: str
        self.task_id = task_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuditItemListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.custom_result is not None:
            result['CustomResult'] = self.custom_result
        if self.custom_risk_type is not None:
            result['CustomRiskType'] = self.custom_risk_type
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rcp_result is not None:
            result['RcpResult'] = self.rcp_result
        if self.rcp_risk_type is not None:
            result['RcpRiskType'] = self.rcp_risk_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('CustomResult') is not None:
            self.custom_result = m.get('CustomResult')
        if m.get('CustomRiskType') is not None:
            self.custom_risk_type = m.get('CustomRiskType')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RcpResult') is not None:
            self.rcp_result = m.get('RcpResult')
        if m.get('RcpRiskType') is not None:
            self.rcp_risk_type = m.get('RcpRiskType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAuditItemListResponseBodyItems(TeaModel):
    def __init__(self, biz_type=None, content=None, create=None, custom_result=None, custom_risk_type=None,
                 custom_ts=None, data_id=None, id=None, operator=None, rcp_result=None, rcp_risk_type=None, rcp_ts=None,
                 sub_uid=None, task_id=None, thumbnail=None, type=None, uid=None, url=None):
        self.biz_type = biz_type  # type: str
        self.content = content  # type: str
        self.create = create  # type: str
        self.custom_result = custom_result  # type: str
        self.custom_risk_type = custom_risk_type  # type: str
        self.custom_ts = custom_ts  # type: str
        self.data_id = data_id  # type: str
        self.id = id  # type: long
        self.operator = operator  # type: str
        self.rcp_result = rcp_result  # type: str
        self.rcp_risk_type = rcp_risk_type  # type: str
        self.rcp_ts = rcp_ts  # type: str
        self.sub_uid = sub_uid  # type: str
        self.task_id = task_id  # type: str
        self.thumbnail = thumbnail  # type: str
        self.type = type  # type: str
        self.uid = uid  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuditItemListResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.content is not None:
            result['Content'] = self.content
        if self.create is not None:
            result['Create'] = self.create
        if self.custom_result is not None:
            result['CustomResult'] = self.custom_result
        if self.custom_risk_type is not None:
            result['CustomRiskType'] = self.custom_risk_type
        if self.custom_ts is not None:
            result['CustomTs'] = self.custom_ts
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.id is not None:
            result['Id'] = self.id
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.rcp_result is not None:
            result['RcpResult'] = self.rcp_result
        if self.rcp_risk_type is not None:
            result['RcpRiskType'] = self.rcp_risk_type
        if self.rcp_ts is not None:
            result['RcpTs'] = self.rcp_ts
        if self.sub_uid is not None:
            result['SubUid'] = self.sub_uid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Create') is not None:
            self.create = m.get('Create')
        if m.get('CustomResult') is not None:
            self.custom_result = m.get('CustomResult')
        if m.get('CustomRiskType') is not None:
            self.custom_risk_type = m.get('CustomRiskType')
        if m.get('CustomTs') is not None:
            self.custom_ts = m.get('CustomTs')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('RcpResult') is not None:
            self.rcp_result = m.get('RcpResult')
        if m.get('RcpRiskType') is not None:
            self.rcp_risk_type = m.get('RcpRiskType')
        if m.get('RcpTs') is not None:
            self.rcp_ts = m.get('RcpTs')
        if m.get('SubUid') is not None:
            self.sub_uid = m.get('SubUid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetAuditItemListResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None):
        self.current_page = current_page  # type: long
        self.items = items  # type: list[GetAuditItemListResponseBodyItems]
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAuditItemListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = GetAuditItemListResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetAuditItemListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAuditItemListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAuditItemListResponse, self).to_map()
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
            temp_model = GetAuditItemListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuditUserConfResponseBody(TeaModel):
    def __init__(self, custom_audit=None, rcp_labels=None, request_id=None, user_labels=None):
        self.custom_audit = custom_audit  # type: bool
        self.rcp_labels = rcp_labels  # type: dict[str, list[str]]
        self.request_id = request_id  # type: str
        self.user_labels = user_labels  # type: dict[str, list[str]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuditUserConfResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_audit is not None:
            result['CustomAudit'] = self.custom_audit
        if self.rcp_labels is not None:
            result['RcpLabels'] = self.rcp_labels
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_labels is not None:
            result['UserLabels'] = self.user_labels
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomAudit') is not None:
            self.custom_audit = m.get('CustomAudit')
        if m.get('RcpLabels') is not None:
            self.rcp_labels = m.get('RcpLabels')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserLabels') is not None:
            self.user_labels = m.get('UserLabels')
        return self


class GetAuditUserConfResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAuditUserConfResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAuditUserConfResponse, self).to_map()
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
            temp_model = GetAuditUserConfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportKeywordsRequest(TeaModel):
    def __init__(self, keyword_lib_id=None, keywords_object=None):
        self.keyword_lib_id = keyword_lib_id  # type: int
        self.keywords_object = keywords_object  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportKeywordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword_lib_id is not None:
            result['KeywordLibId'] = self.keyword_lib_id
        if self.keywords_object is not None:
            result['KeywordsObject'] = self.keywords_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeywordLibId') is not None:
            self.keyword_lib_id = m.get('KeywordLibId')
        if m.get('KeywordsObject') is not None:
            self.keywords_object = m.get('KeywordsObject')
        return self


class ImportKeywordsResponseBody(TeaModel):
    def __init__(self, invalid_keyword_list=None, request_id=None, success_count=None, valid_keyword_list=None):
        self.invalid_keyword_list = invalid_keyword_list  # type: list[str]
        self.request_id = request_id  # type: str
        self.success_count = success_count  # type: int
        self.valid_keyword_list = valid_keyword_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportKeywordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invalid_keyword_list is not None:
            result['InvalidKeywordList'] = self.invalid_keyword_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.valid_keyword_list is not None:
            result['validKeywordList'] = self.valid_keyword_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InvalidKeywordList') is not None:
            self.invalid_keyword_list = m.get('InvalidKeywordList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('validKeywordList') is not None:
            self.valid_keyword_list = m.get('validKeywordList')
        return self


class ImportKeywordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportKeywordsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportKeywordsResponse, self).to_map()
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
            temp_model = ImportKeywordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MarkAuditContentRequest(TeaModel):
    def __init__(self, audit_illegal_reasons=None, audit_result=None, biz_types=None, ids=None, source_ip=None):
        self.audit_illegal_reasons = audit_illegal_reasons  # type: str
        self.audit_result = audit_result  # type: str
        self.biz_types = biz_types  # type: str
        self.ids = ids  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MarkAuditContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_illegal_reasons is not None:
            result['AuditIllegalReasons'] = self.audit_illegal_reasons
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditIllegalReasons') is not None:
            self.audit_illegal_reasons = m.get('AuditIllegalReasons')
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class MarkAuditContentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MarkAuditContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MarkAuditContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MarkAuditContentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MarkAuditContentResponse, self).to_map()
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
            temp_model = MarkAuditContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MarkAuditContentItemRequest(TeaModel):
    def __init__(self, audit_illegal_reasons=None, audit_result=None, biz_types=None, ids=None, lang=None,
                 source_ip=None):
        self.audit_illegal_reasons = audit_illegal_reasons  # type: str
        self.audit_result = audit_result  # type: str
        self.biz_types = biz_types  # type: str
        self.ids = ids  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MarkAuditContentItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_illegal_reasons is not None:
            result['AuditIllegalReasons'] = self.audit_illegal_reasons
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditIllegalReasons') is not None:
            self.audit_illegal_reasons = m.get('AuditIllegalReasons')
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class MarkAuditContentItemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MarkAuditContentItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MarkAuditContentItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MarkAuditContentItemResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MarkAuditContentItemResponse, self).to_map()
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
            temp_model = MarkAuditContentItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MarkOssResultRequest(TeaModel):
    def __init__(self, ids=None, lang=None, operation=None, resource_type=None, scene=None, source_ip=None,
                 stock=None):
        self.ids = ids  # type: str
        self.lang = lang  # type: str
        self.operation = operation  # type: str
        self.resource_type = resource_type  # type: str
        self.scene = scene  # type: str
        self.source_ip = source_ip  # type: str
        self.stock = stock  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(MarkOssResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.stock is not None:
            result['Stock'] = self.stock
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Stock') is not None:
            self.stock = m.get('Stock')
        return self


class MarkOssResultResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MarkOssResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MarkOssResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MarkOssResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MarkOssResultResponse, self).to_map()
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
            temp_model = MarkOssResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MarkWebsiteScanResultRequest(TeaModel):
    def __init__(self, ids=None, lang=None, source_ip=None):
        self.ids = ids  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MarkWebsiteScanResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class MarkWebsiteScanResultResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MarkWebsiteScanResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MarkWebsiteScanResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MarkWebsiteScanResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MarkWebsiteScanResultResponse, self).to_map()
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
            temp_model = MarkWebsiteScanResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundCdiBagRequest(TeaModel):
    def __init__(self, instance_id=None, resource_owner_id=None):
        self.instance_id = instance_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundCdiBagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RefundCdiBagResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundCdiBagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefundCdiBagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefundCdiBagResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefundCdiBagResponse, self).to_map()
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
            temp_model = RefundCdiBagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundCdiBaseBagRequest(TeaModel):
    def __init__(self, instance_id=None, resource_owner_id=None):
        self.instance_id = instance_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundCdiBaseBagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RefundCdiBaseBagResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundCdiBaseBagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefundCdiBaseBagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefundCdiBaseBagResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefundCdiBaseBagResponse, self).to_map()
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
            temp_model = RefundCdiBaseBagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundWebSiteInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, resource_owner_id=None):
        self.instance_id = instance_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundWebSiteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RefundWebSiteInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundWebSiteInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefundWebSiteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefundWebSiteInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefundWebSiteInstanceResponse, self).to_map()
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
            temp_model = RefundWebSiteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewWebSiteInstanceRequest(TeaModel):
    def __init__(self, client_token=None, commodity_code=None, duration=None, instance_id=None, order_num=None,
                 order_type=None, owner_id=None, pricing_cycle=None):
        self.client_token = client_token  # type: str
        self.commodity_code = commodity_code  # type: str
        self.duration = duration  # type: int
        self.instance_id = instance_id  # type: str
        self.order_num = order_num  # type: int
        self.order_type = order_type  # type: str
        self.owner_id = owner_id  # type: long
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewWebSiteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class RenewWebSiteInstanceResponseBodyInstanceIds(TeaModel):
    def __init__(self, string=None):
        self.string = string  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewWebSiteInstanceResponseBodyInstanceIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.string is not None:
            result['String'] = self.string
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')
        return self


class RenewWebSiteInstanceResponseBody(TeaModel):
    def __init__(self, code=None, instance_id=None, instance_ids=None, message=None, order_id=None, request_id=None):
        self.code = code  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_ids = instance_ids  # type: RenewWebSiteInstanceResponseBodyInstanceIds
        self.message = message  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super(RenewWebSiteInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIds') is not None:
            temp_model = RenewWebSiteInstanceResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewWebSiteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenewWebSiteInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewWebSiteInstanceResponse, self).to_map()
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
            temp_model = RenewWebSiteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerifyCodeToEmailRequest(TeaModel):
    def __init__(self, email=None, lang=None, source_ip=None):
        self.email = email  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendVerifyCodeToEmailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class SendVerifyCodeToEmailResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendVerifyCodeToEmailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendVerifyCodeToEmailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendVerifyCodeToEmailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendVerifyCodeToEmailResponse, self).to_map()
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
            temp_model = SendVerifyCodeToEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerifyCodeToPhoneRequest(TeaModel):
    def __init__(self, lang=None, phone=None, source_ip=None):
        self.lang = lang  # type: str
        self.phone = phone  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendVerifyCodeToPhoneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class SendVerifyCodeToPhoneResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendVerifyCodeToPhoneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendVerifyCodeToPhoneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendVerifyCodeToPhoneResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendVerifyCodeToPhoneResponse, self).to_map()
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
            temp_model = SendVerifyCodeToPhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendWebsiteFeedbackRequest(TeaModel):
    def __init__(self, feedback=None, lang=None, source_ip=None, urls=None):
        self.feedback = feedback  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str
        self.urls = urls  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendWebsiteFeedbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.urls is not None:
            result['Urls'] = self.urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Urls') is not None:
            self.urls = m.get('Urls')
        return self


class SendWebsiteFeedbackResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendWebsiteFeedbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendWebsiteFeedbackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendWebsiteFeedbackResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendWebsiteFeedbackResponse, self).to_map()
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
            temp_model = SendWebsiteFeedbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppPackageRequest(TeaModel):
    def __init__(self, debug=None, id=None, lang=None, package_url=None, platform=None, source_ip=None):
        self.debug = debug  # type: bool
        self.id = id  # type: long
        self.lang = lang  # type: str
        self.package_url = package_url  # type: str
        self.platform = platform  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class UpdateAppPackageResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateAppPackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAppPackageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppPackageResponse, self).to_map()
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
            temp_model = UpdateAppPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuditCallbackRequest(TeaModel):
    def __init__(self, callback=None, crypt_type=None, seed=None):
        self.callback = callback  # type: str
        self.crypt_type = crypt_type  # type: int
        self.seed = seed  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuditCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.seed is not None:
            result['Seed'] = self.seed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        return self


class UpdateAuditCallbackResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuditCallbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAuditCallbackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAuditCallbackResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAuditCallbackResponse, self).to_map()
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
            temp_model = UpdateAuditCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuditRangeRequest(TeaModel):
    def __init__(self, audit_range=None):
        self.audit_range = audit_range  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuditRangeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_range is not None:
            result['AuditRange'] = self.audit_range
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditRange') is not None:
            self.audit_range = m.get('AuditRange')
        return self


class UpdateAuditRangeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuditRangeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAuditRangeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAuditRangeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAuditRangeResponse, self).to_map()
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
            temp_model = UpdateAuditRangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuditSettingRequest(TeaModel):
    def __init__(self, audit_range=None, callback=None, seed=None, source_ip=None):
        self.audit_range = audit_range  # type: str
        self.callback = callback  # type: str
        self.seed = seed  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuditSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_range is not None:
            result['AuditRange'] = self.audit_range
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.seed is not None:
            result['Seed'] = self.seed
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditRange') is not None:
            self.audit_range = m.get('AuditRange')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class UpdateAuditSettingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAuditSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAuditSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAuditSettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAuditSettingResponse, self).to_map()
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
            temp_model = UpdateAuditSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBizTypeRequest(TeaModel):
    def __init__(self, biz_type_name=None, description=None):
        self.biz_type_name = biz_type_name  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBizTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateBizTypeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBizTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBizTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateBizTypeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBizTypeResponse, self).to_map()
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
            temp_model = UpdateBizTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBizTypeImageLibRequest(TeaModel):
    def __init__(self, biz_type_name=None, black=None, resource_type=None, review=None, scene=None, white=None):
        self.biz_type_name = biz_type_name  # type: str
        self.black = black  # type: str
        self.resource_type = resource_type  # type: str
        self.review = review  # type: str
        self.scene = scene  # type: str
        self.white = white  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBizTypeImageLibRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.black is not None:
            result['Black'] = self.black
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.review is not None:
            result['Review'] = self.review
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.white is not None:
            result['White'] = self.white
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('Black') is not None:
            self.black = m.get('Black')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Review') is not None:
            self.review = m.get('Review')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('White') is not None:
            self.white = m.get('White')
        return self


class UpdateBizTypeImageLibResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBizTypeImageLibResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBizTypeImageLibResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateBizTypeImageLibResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBizTypeImageLibResponse, self).to_map()
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
            temp_model = UpdateBizTypeImageLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBizTypeSettingRequest(TeaModel):
    def __init__(self, ad=None, antispam=None, biz_type_name=None, live=None, porn=None, resource_type=None,
                 terrorism=None):
        self.ad = ad  # type: str
        self.antispam = antispam  # type: str
        self.biz_type_name = biz_type_name  # type: str
        self.live = live  # type: str
        self.porn = porn  # type: str
        self.resource_type = resource_type  # type: str
        self.terrorism = terrorism  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBizTypeSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad is not None:
            result['Ad'] = self.ad
        if self.antispam is not None:
            result['Antispam'] = self.antispam
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.live is not None:
            result['Live'] = self.live
        if self.porn is not None:
            result['Porn'] = self.porn
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.terrorism is not None:
            result['Terrorism'] = self.terrorism
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ad') is not None:
            self.ad = m.get('Ad')
        if m.get('Antispam') is not None:
            self.antispam = m.get('Antispam')
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('Live') is not None:
            self.live = m.get('Live')
        if m.get('Porn') is not None:
            self.porn = m.get('Porn')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Terrorism') is not None:
            self.terrorism = m.get('Terrorism')
        return self


class UpdateBizTypeSettingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBizTypeSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBizTypeSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateBizTypeSettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBizTypeSettingResponse, self).to_map()
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
            temp_model = UpdateBizTypeSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBizTypeTextLibRequest(TeaModel):
    def __init__(self, biz_type_name=None, black=None, ignore=None, resource_type=None, review=None, scene=None,
                 white=None):
        self.biz_type_name = biz_type_name  # type: str
        self.black = black  # type: str
        self.ignore = ignore  # type: str
        self.resource_type = resource_type  # type: str
        self.review = review  # type: str
        self.scene = scene  # type: str
        self.white = white  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBizTypeTextLibRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.black is not None:
            result['Black'] = self.black
        if self.ignore is not None:
            result['Ignore'] = self.ignore
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.review is not None:
            result['Review'] = self.review
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.white is not None:
            result['White'] = self.white
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('Black') is not None:
            self.black = m.get('Black')
        if m.get('Ignore') is not None:
            self.ignore = m.get('Ignore')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Review') is not None:
            self.review = m.get('Review')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('White') is not None:
            self.white = m.get('White')
        return self


class UpdateBizTypeTextLibResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBizTypeTextLibResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBizTypeTextLibResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateBizTypeTextLibResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBizTypeTextLibResponse, self).to_map()
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
            temp_model = UpdateBizTypeTextLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomOcrTemplateRequest(TeaModel):
    def __init__(self, id=None, name=None, recognize_area=None, refer_area=None):
        self.id = id  # type: long
        self.name = name  # type: str
        self.recognize_area = recognize_area  # type: str
        self.refer_area = refer_area  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomOcrTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.recognize_area is not None:
            result['RecognizeArea'] = self.recognize_area
        if self.refer_area is not None:
            result['ReferArea'] = self.refer_area
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RecognizeArea') is not None:
            self.recognize_area = m.get('RecognizeArea')
        if m.get('ReferArea') is not None:
            self.refer_area = m.get('ReferArea')
        return self


class UpdateCustomOcrTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomOcrTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCustomOcrTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCustomOcrTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCustomOcrTemplateResponse, self).to_map()
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
            temp_model = UpdateCustomOcrTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKeywordLibRequest(TeaModel):
    def __init__(self, biz_types=None, enable=None, id=None, lang=None, match_mode=None, name=None, source_ip=None):
        self.biz_types = biz_types  # type: str
        self.enable = enable  # type: bool
        self.id = id  # type: int
        self.lang = lang  # type: str
        self.match_mode = match_mode  # type: str
        self.name = name  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKeywordLibRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class UpdateKeywordLibResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateKeywordLibResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateKeywordLibResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateKeywordLibResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateKeywordLibResponse, self).to_map()
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
            temp_model = UpdateKeywordLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNotificationSettingRequest(TeaModel):
    def __init__(self, lang=None, realtime_message_list=None, reminder_mode_list=None, schedule_message_time=None,
                 schedule_message_time_zone=None, source_ip=None):
        self.lang = lang  # type: str
        self.realtime_message_list = realtime_message_list  # type: str
        self.reminder_mode_list = reminder_mode_list  # type: str
        self.schedule_message_time = schedule_message_time  # type: int
        self.schedule_message_time_zone = schedule_message_time_zone  # type: int
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNotificationSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.realtime_message_list is not None:
            result['RealtimeMessageList'] = self.realtime_message_list
        if self.reminder_mode_list is not None:
            result['ReminderModeList'] = self.reminder_mode_list
        if self.schedule_message_time is not None:
            result['ScheduleMessageTime'] = self.schedule_message_time
        if self.schedule_message_time_zone is not None:
            result['ScheduleMessageTimeZone'] = self.schedule_message_time_zone
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RealtimeMessageList') is not None:
            self.realtime_message_list = m.get('RealtimeMessageList')
        if m.get('ReminderModeList') is not None:
            self.reminder_mode_list = m.get('ReminderModeList')
        if m.get('ScheduleMessageTime') is not None:
            self.schedule_message_time = m.get('ScheduleMessageTime')
        if m.get('ScheduleMessageTimeZone') is not None:
            self.schedule_message_time_zone = m.get('ScheduleMessageTimeZone')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class UpdateNotificationSettingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNotificationSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateNotificationSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateNotificationSettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNotificationSettingResponse, self).to_map()
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
            temp_model = UpdateNotificationSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOssCallbackSettingRequest(TeaModel):
    def __init__(self, audit_callback=None, callback_seed=None, callback_url=None, scan_callback=None,
                 scan_callback_suggestions=None, service_modules=None):
        self.audit_callback = audit_callback  # type: bool
        self.callback_seed = callback_seed  # type: str
        self.callback_url = callback_url  # type: str
        self.scan_callback = scan_callback  # type: bool
        self.scan_callback_suggestions = scan_callback_suggestions  # type: str
        self.service_modules = service_modules  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOssCallbackSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_callback is not None:
            result['AuditCallback'] = self.audit_callback
        if self.callback_seed is not None:
            result['CallbackSeed'] = self.callback_seed
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.scan_callback is not None:
            result['ScanCallback'] = self.scan_callback
        if self.scan_callback_suggestions is not None:
            result['ScanCallbackSuggestions'] = self.scan_callback_suggestions
        if self.service_modules is not None:
            result['ServiceModules'] = self.service_modules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditCallback') is not None:
            self.audit_callback = m.get('AuditCallback')
        if m.get('CallbackSeed') is not None:
            self.callback_seed = m.get('CallbackSeed')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ScanCallback') is not None:
            self.scan_callback = m.get('ScanCallback')
        if m.get('ScanCallbackSuggestions') is not None:
            self.scan_callback_suggestions = m.get('ScanCallbackSuggestions')
        if m.get('ServiceModules') is not None:
            self.service_modules = m.get('ServiceModules')
        return self


class UpdateOssCallbackSettingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOssCallbackSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateOssCallbackSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateOssCallbackSettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateOssCallbackSettingResponse, self).to_map()
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
            temp_model = UpdateOssCallbackSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOssIncrementCheckSettingRequest(TeaModel):
    def __init__(self, audio_antispam_freeze_config=None, audio_auto_freeze_opened=None, audio_max_size=None,
                 audio_scan_limit=None, audio_scene_list=None, auto_freeze_type=None, biz_type=None, bucket_config_list=None,
                 callback_id=None, image_ad_freeze_config=None, image_auto_freeze=None, image_auto_freeze_opened=None,
                 image_live_freeze_config=None, image_porn_freeze_config=None, image_scan_limit=None, image_scene_list=None,
                 image_terrorism_freeze_config=None, lang=None, scan_image_no_file_type=None, source_ip=None, video_ad_freeze_config=None,
                 video_auto_freeze_opened=None, video_auto_freeze_scene_list=None, video_frame_interval=None,
                 video_live_freeze_config=None, video_max_frames=None, video_max_size=None, video_porn_freeze_config=None,
                 video_scan_limit=None, video_scene_list=None, video_terrorism_freeze_config=None,
                 video_voice_antispam_freeze_config=None):
        self.audio_antispam_freeze_config = audio_antispam_freeze_config  # type: str
        self.audio_auto_freeze_opened = audio_auto_freeze_opened  # type: bool
        self.audio_max_size = audio_max_size  # type: int
        self.audio_scan_limit = audio_scan_limit  # type: long
        self.audio_scene_list = audio_scene_list  # type: str
        self.auto_freeze_type = auto_freeze_type  # type: str
        self.biz_type = biz_type  # type: str
        self.bucket_config_list = bucket_config_list  # type: str
        self.callback_id = callback_id  # type: str
        self.image_ad_freeze_config = image_ad_freeze_config  # type: str
        self.image_auto_freeze = image_auto_freeze  # type: str
        self.image_auto_freeze_opened = image_auto_freeze_opened  # type: bool
        self.image_live_freeze_config = image_live_freeze_config  # type: str
        self.image_porn_freeze_config = image_porn_freeze_config  # type: str
        self.image_scan_limit = image_scan_limit  # type: str
        self.image_scene_list = image_scene_list  # type: str
        self.image_terrorism_freeze_config = image_terrorism_freeze_config  # type: str
        self.lang = lang  # type: str
        self.scan_image_no_file_type = scan_image_no_file_type  # type: bool
        self.source_ip = source_ip  # type: str
        self.video_ad_freeze_config = video_ad_freeze_config  # type: str
        self.video_auto_freeze_opened = video_auto_freeze_opened  # type: bool
        self.video_auto_freeze_scene_list = video_auto_freeze_scene_list  # type: str
        self.video_frame_interval = video_frame_interval  # type: int
        self.video_live_freeze_config = video_live_freeze_config  # type: str
        self.video_max_frames = video_max_frames  # type: int
        self.video_max_size = video_max_size  # type: int
        self.video_porn_freeze_config = video_porn_freeze_config  # type: str
        self.video_scan_limit = video_scan_limit  # type: long
        self.video_scene_list = video_scene_list  # type: str
        self.video_terrorism_freeze_config = video_terrorism_freeze_config  # type: str
        self.video_voice_antispam_freeze_config = video_voice_antispam_freeze_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOssIncrementCheckSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_antispam_freeze_config is not None:
            result['AudioAntispamFreezeConfig'] = self.audio_antispam_freeze_config
        if self.audio_auto_freeze_opened is not None:
            result['AudioAutoFreezeOpened'] = self.audio_auto_freeze_opened
        if self.audio_max_size is not None:
            result['AudioMaxSize'] = self.audio_max_size
        if self.audio_scan_limit is not None:
            result['AudioScanLimit'] = self.audio_scan_limit
        if self.audio_scene_list is not None:
            result['AudioSceneList'] = self.audio_scene_list
        if self.auto_freeze_type is not None:
            result['AutoFreezeType'] = self.auto_freeze_type
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.bucket_config_list is not None:
            result['BucketConfigList'] = self.bucket_config_list
        if self.callback_id is not None:
            result['CallbackId'] = self.callback_id
        if self.image_ad_freeze_config is not None:
            result['ImageAdFreezeConfig'] = self.image_ad_freeze_config
        if self.image_auto_freeze is not None:
            result['ImageAutoFreeze'] = self.image_auto_freeze
        if self.image_auto_freeze_opened is not None:
            result['ImageAutoFreezeOpened'] = self.image_auto_freeze_opened
        if self.image_live_freeze_config is not None:
            result['ImageLiveFreezeConfig'] = self.image_live_freeze_config
        if self.image_porn_freeze_config is not None:
            result['ImagePornFreezeConfig'] = self.image_porn_freeze_config
        if self.image_scan_limit is not None:
            result['ImageScanLimit'] = self.image_scan_limit
        if self.image_scene_list is not None:
            result['ImageSceneList'] = self.image_scene_list
        if self.image_terrorism_freeze_config is not None:
            result['ImageTerrorismFreezeConfig'] = self.image_terrorism_freeze_config
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.scan_image_no_file_type is not None:
            result['ScanImageNoFileType'] = self.scan_image_no_file_type
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.video_ad_freeze_config is not None:
            result['VideoAdFreezeConfig'] = self.video_ad_freeze_config
        if self.video_auto_freeze_opened is not None:
            result['VideoAutoFreezeOpened'] = self.video_auto_freeze_opened
        if self.video_auto_freeze_scene_list is not None:
            result['VideoAutoFreezeSceneList'] = self.video_auto_freeze_scene_list
        if self.video_frame_interval is not None:
            result['VideoFrameInterval'] = self.video_frame_interval
        if self.video_live_freeze_config is not None:
            result['VideoLiveFreezeConfig'] = self.video_live_freeze_config
        if self.video_max_frames is not None:
            result['VideoMaxFrames'] = self.video_max_frames
        if self.video_max_size is not None:
            result['VideoMaxSize'] = self.video_max_size
        if self.video_porn_freeze_config is not None:
            result['VideoPornFreezeConfig'] = self.video_porn_freeze_config
        if self.video_scan_limit is not None:
            result['VideoScanLimit'] = self.video_scan_limit
        if self.video_scene_list is not None:
            result['VideoSceneList'] = self.video_scene_list
        if self.video_terrorism_freeze_config is not None:
            result['VideoTerrorismFreezeConfig'] = self.video_terrorism_freeze_config
        if self.video_voice_antispam_freeze_config is not None:
            result['VideoVoiceAntispamFreezeConfig'] = self.video_voice_antispam_freeze_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioAntispamFreezeConfig') is not None:
            self.audio_antispam_freeze_config = m.get('AudioAntispamFreezeConfig')
        if m.get('AudioAutoFreezeOpened') is not None:
            self.audio_auto_freeze_opened = m.get('AudioAutoFreezeOpened')
        if m.get('AudioMaxSize') is not None:
            self.audio_max_size = m.get('AudioMaxSize')
        if m.get('AudioScanLimit') is not None:
            self.audio_scan_limit = m.get('AudioScanLimit')
        if m.get('AudioSceneList') is not None:
            self.audio_scene_list = m.get('AudioSceneList')
        if m.get('AutoFreezeType') is not None:
            self.auto_freeze_type = m.get('AutoFreezeType')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BucketConfigList') is not None:
            self.bucket_config_list = m.get('BucketConfigList')
        if m.get('CallbackId') is not None:
            self.callback_id = m.get('CallbackId')
        if m.get('ImageAdFreezeConfig') is not None:
            self.image_ad_freeze_config = m.get('ImageAdFreezeConfig')
        if m.get('ImageAutoFreeze') is not None:
            self.image_auto_freeze = m.get('ImageAutoFreeze')
        if m.get('ImageAutoFreezeOpened') is not None:
            self.image_auto_freeze_opened = m.get('ImageAutoFreezeOpened')
        if m.get('ImageLiveFreezeConfig') is not None:
            self.image_live_freeze_config = m.get('ImageLiveFreezeConfig')
        if m.get('ImagePornFreezeConfig') is not None:
            self.image_porn_freeze_config = m.get('ImagePornFreezeConfig')
        if m.get('ImageScanLimit') is not None:
            self.image_scan_limit = m.get('ImageScanLimit')
        if m.get('ImageSceneList') is not None:
            self.image_scene_list = m.get('ImageSceneList')
        if m.get('ImageTerrorismFreezeConfig') is not None:
            self.image_terrorism_freeze_config = m.get('ImageTerrorismFreezeConfig')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ScanImageNoFileType') is not None:
            self.scan_image_no_file_type = m.get('ScanImageNoFileType')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VideoAdFreezeConfig') is not None:
            self.video_ad_freeze_config = m.get('VideoAdFreezeConfig')
        if m.get('VideoAutoFreezeOpened') is not None:
            self.video_auto_freeze_opened = m.get('VideoAutoFreezeOpened')
        if m.get('VideoAutoFreezeSceneList') is not None:
            self.video_auto_freeze_scene_list = m.get('VideoAutoFreezeSceneList')
        if m.get('VideoFrameInterval') is not None:
            self.video_frame_interval = m.get('VideoFrameInterval')
        if m.get('VideoLiveFreezeConfig') is not None:
            self.video_live_freeze_config = m.get('VideoLiveFreezeConfig')
        if m.get('VideoMaxFrames') is not None:
            self.video_max_frames = m.get('VideoMaxFrames')
        if m.get('VideoMaxSize') is not None:
            self.video_max_size = m.get('VideoMaxSize')
        if m.get('VideoPornFreezeConfig') is not None:
            self.video_porn_freeze_config = m.get('VideoPornFreezeConfig')
        if m.get('VideoScanLimit') is not None:
            self.video_scan_limit = m.get('VideoScanLimit')
        if m.get('VideoSceneList') is not None:
            self.video_scene_list = m.get('VideoSceneList')
        if m.get('VideoTerrorismFreezeConfig') is not None:
            self.video_terrorism_freeze_config = m.get('VideoTerrorismFreezeConfig')
        if m.get('VideoVoiceAntispamFreezeConfig') is not None:
            self.video_voice_antispam_freeze_config = m.get('VideoVoiceAntispamFreezeConfig')
        return self


class UpdateOssIncrementCheckSettingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOssIncrementCheckSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateOssIncrementCheckSettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateOssIncrementCheckSettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateOssIncrementCheckSettingResponse, self).to_map()
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
            temp_model = UpdateOssIncrementCheckSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOssStockStatusRequest(TeaModel):
    def __init__(self, audio_auto_freeze_scene_list=None, audio_max_size=None, auto_freeze_type=None,
                 bucket_config_list=None, end_date=None, image_auto_freeze=None, lang=None, operation=None, resource_type_list=None,
                 scene_list=None, source_ip=None, start_date=None, video_auto_freeze_scene_list=None,
                 video_frame_interval=None, video_max_frames=None, video_max_size=None):
        self.audio_auto_freeze_scene_list = audio_auto_freeze_scene_list  # type: str
        self.audio_max_size = audio_max_size  # type: int
        self.auto_freeze_type = auto_freeze_type  # type: str
        self.bucket_config_list = bucket_config_list  # type: str
        self.end_date = end_date  # type: str
        self.image_auto_freeze = image_auto_freeze  # type: str
        self.lang = lang  # type: str
        self.operation = operation  # type: str
        self.resource_type_list = resource_type_list  # type: str
        self.scene_list = scene_list  # type: str
        self.source_ip = source_ip  # type: str
        self.start_date = start_date  # type: str
        self.video_auto_freeze_scene_list = video_auto_freeze_scene_list  # type: str
        self.video_frame_interval = video_frame_interval  # type: int
        self.video_max_frames = video_max_frames  # type: int
        self.video_max_size = video_max_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOssStockStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_auto_freeze_scene_list is not None:
            result['AudioAutoFreezeSceneList'] = self.audio_auto_freeze_scene_list
        if self.audio_max_size is not None:
            result['AudioMaxSize'] = self.audio_max_size
        if self.auto_freeze_type is not None:
            result['AutoFreezeType'] = self.auto_freeze_type
        if self.bucket_config_list is not None:
            result['BucketConfigList'] = self.bucket_config_list
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.image_auto_freeze is not None:
            result['ImageAutoFreeze'] = self.image_auto_freeze
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_type_list is not None:
            result['ResourceTypeList'] = self.resource_type_list
        if self.scene_list is not None:
            result['SceneList'] = self.scene_list
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.video_auto_freeze_scene_list is not None:
            result['VideoAutoFreezeSceneList'] = self.video_auto_freeze_scene_list
        if self.video_frame_interval is not None:
            result['VideoFrameInterval'] = self.video_frame_interval
        if self.video_max_frames is not None:
            result['VideoMaxFrames'] = self.video_max_frames
        if self.video_max_size is not None:
            result['VideoMaxSize'] = self.video_max_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioAutoFreezeSceneList') is not None:
            self.audio_auto_freeze_scene_list = m.get('AudioAutoFreezeSceneList')
        if m.get('AudioMaxSize') is not None:
            self.audio_max_size = m.get('AudioMaxSize')
        if m.get('AutoFreezeType') is not None:
            self.auto_freeze_type = m.get('AutoFreezeType')
        if m.get('BucketConfigList') is not None:
            self.bucket_config_list = m.get('BucketConfigList')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ImageAutoFreeze') is not None:
            self.image_auto_freeze = m.get('ImageAutoFreeze')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceTypeList') is not None:
            self.resource_type_list = m.get('ResourceTypeList')
        if m.get('SceneList') is not None:
            self.scene_list = m.get('SceneList')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('VideoAutoFreezeSceneList') is not None:
            self.video_auto_freeze_scene_list = m.get('VideoAutoFreezeSceneList')
        if m.get('VideoFrameInterval') is not None:
            self.video_frame_interval = m.get('VideoFrameInterval')
        if m.get('VideoMaxFrames') is not None:
            self.video_max_frames = m.get('VideoMaxFrames')
        if m.get('VideoMaxSize') is not None:
            self.video_max_size = m.get('VideoMaxSize')
        return self


class UpdateOssStockStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOssStockStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateOssStockStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateOssStockStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateOssStockStatusResponse, self).to_map()
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
            temp_model = UpdateOssStockStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWebsiteInstanceRequest(TeaModel):
    def __init__(self, domain=None, index_page=None, index_page_scan_interval=None, instance_id=None, lang=None,
                 site_protocol=None, source_ip=None, website_scan_interval=None):
        self.domain = domain  # type: str
        self.index_page = index_page  # type: str
        self.index_page_scan_interval = index_page_scan_interval  # type: int
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.site_protocol = site_protocol  # type: str
        self.source_ip = source_ip  # type: str
        self.website_scan_interval = website_scan_interval  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWebsiteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.index_page is not None:
            result['IndexPage'] = self.index_page
        if self.index_page_scan_interval is not None:
            result['IndexPageScanInterval'] = self.index_page_scan_interval
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.site_protocol is not None:
            result['SiteProtocol'] = self.site_protocol
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.website_scan_interval is not None:
            result['WebsiteScanInterval'] = self.website_scan_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('IndexPage') is not None:
            self.index_page = m.get('IndexPage')
        if m.get('IndexPageScanInterval') is not None:
            self.index_page_scan_interval = m.get('IndexPageScanInterval')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SiteProtocol') is not None:
            self.site_protocol = m.get('SiteProtocol')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('WebsiteScanInterval') is not None:
            self.website_scan_interval = m.get('WebsiteScanInterval')
        return self


class UpdateWebsiteInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWebsiteInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWebsiteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateWebsiteInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWebsiteInstanceResponse, self).to_map()
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
            temp_model = UpdateWebsiteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWebsiteInstanceKeyUrlRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, source_ip=None, urls=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str
        self.urls = urls  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWebsiteInstanceKeyUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.urls is not None:
            result['Urls'] = self.urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Urls') is not None:
            self.urls = m.get('Urls')
        return self


class UpdateWebsiteInstanceKeyUrlResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWebsiteInstanceKeyUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWebsiteInstanceKeyUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateWebsiteInstanceKeyUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWebsiteInstanceKeyUrlResponse, self).to_map()
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
            temp_model = UpdateWebsiteInstanceKeyUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWebsiteInstanceStatusRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, source_ip=None, status=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWebsiteInstanceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateWebsiteInstanceStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWebsiteInstanceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWebsiteInstanceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateWebsiteInstanceStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWebsiteInstanceStatusResponse, self).to_map()
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
            temp_model = UpdateWebsiteInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeCdiBaseBagRequest(TeaModel):
    def __init__(self, client_token=None, commodity_code=None, flow_out_spec=None, instance_id=None,
                 order_type=None, owner_id=None):
        self.client_token = client_token  # type: str
        self.commodity_code = commodity_code  # type: str
        self.flow_out_spec = flow_out_spec  # type: int
        self.instance_id = instance_id  # type: str
        self.order_type = order_type  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeCdiBaseBagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.flow_out_spec is not None:
            result['FlowOutSpec'] = self.flow_out_spec
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('FlowOutSpec') is not None:
            self.flow_out_spec = m.get('FlowOutSpec')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class UpgradeCdiBaseBagResponseBody(TeaModel):
    def __init__(self, code=None, instance_id=None, message=None, order_id=None, request_id=None):
        self.code = code  # type: str
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeCdiBaseBagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeCdiBaseBagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpgradeCdiBaseBagResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeCdiBaseBagResponse, self).to_map()
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
            temp_model = UpgradeCdiBaseBagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadImageToLibRequest(TeaModel):
    def __init__(self, image_lib_id=None, images=None, source_ip=None, urls=None):
        self.image_lib_id = image_lib_id  # type: int
        self.images = images  # type: str
        self.source_ip = source_ip  # type: str
        self.urls = urls  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadImageToLibRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_lib_id is not None:
            result['ImageLibId'] = self.image_lib_id
        if self.images is not None:
            result['Images'] = self.images
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.urls is not None:
            result['Urls'] = self.urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageLibId') is not None:
            self.image_lib_id = m.get('ImageLibId')
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Urls') is not None:
            self.urls = m.get('Urls')
        return self


class UploadImageToLibResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadImageToLibResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadImageToLibResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UploadImageToLibResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadImageToLibResponse, self).to_map()
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
            temp_model = UploadImageToLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyCustomOcrTemplateRequest(TeaModel):
    def __init__(self, id=None, test_img_url=None):
        self.id = id  # type: long
        self.test_img_url = test_img_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyCustomOcrTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.test_img_url is not None:
            result['TestImgUrl'] = self.test_img_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TestImgUrl') is not None:
            self.test_img_url = m.get('TestImgUrl')
        return self


class VerifyCustomOcrTemplateResponseBody(TeaModel):
    def __init__(self, image_url=None, recognize_info=None, request_id=None):
        self.image_url = image_url  # type: str
        self.recognize_info = recognize_info  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyCustomOcrTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.recognize_info is not None:
            result['RecognizeInfo'] = self.recognize_info
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('RecognizeInfo') is not None:
            self.recognize_info = m.get('RecognizeInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyCustomOcrTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyCustomOcrTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyCustomOcrTemplateResponse, self).to_map()
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
            temp_model = VerifyCustomOcrTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyEmailRequest(TeaModel):
    def __init__(self, lang=None, source_ip=None, verify_code=None):
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str
        self.verify_code = verify_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyEmailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class VerifyEmailResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyEmailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyEmailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyEmailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyEmailResponse, self).to_map()
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
            temp_model = VerifyEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyPhoneRequest(TeaModel):
    def __init__(self, lang=None, phone=None, source_ip=None, verify_code=None):
        self.lang = lang  # type: str
        self.phone = phone  # type: str
        self.source_ip = source_ip  # type: str
        self.verify_code = verify_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyPhoneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class VerifyPhoneResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyPhoneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyPhoneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyPhoneResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyPhoneResponse, self).to_map()
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
            temp_model = VerifyPhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyWebsiteInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, source_ip=None, verify_method=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str
        self.verify_method = verify_method  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyWebsiteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.verify_method is not None:
            result['VerifyMethod'] = self.verify_method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VerifyMethod') is not None:
            self.verify_method = m.get('VerifyMethod')
        return self


class VerifyWebsiteInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyWebsiteInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyWebsiteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyWebsiteInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyWebsiteInstanceResponse, self).to_map()
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
            temp_model = VerifyWebsiteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


