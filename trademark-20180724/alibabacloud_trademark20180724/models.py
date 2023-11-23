# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AcceptPartnerNotificationRequest(TeaModel):
    def __init__(self, biz_id=None, material=None, operation=None, remark=None):
        self.biz_id = biz_id  # type: str
        self.material = material  # type: str
        self.operation = operation  # type: str
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptPartnerNotificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.material is not None:
            result['Material'] = self.material
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Material') is not None:
            self.material = m.get('Material')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class AcceptPartnerNotificationResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptPartnerNotificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AcceptPartnerNotificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AcceptPartnerNotificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AcceptPartnerNotificationResponse, self).to_map()
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
            temp_model = AcceptPartnerNotificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyNotaryPostRequest(TeaModel):
    def __init__(self, notary_order_id=None, receiver_address=None, receiver_name=None, receiver_phone=None):
        self.notary_order_id = notary_order_id  # type: long
        self.receiver_address = receiver_address  # type: str
        self.receiver_name = receiver_name  # type: str
        self.receiver_phone = receiver_phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyNotaryPostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        if self.receiver_address is not None:
            result['ReceiverAddress'] = self.receiver_address
        if self.receiver_name is not None:
            result['ReceiverName'] = self.receiver_name
        if self.receiver_phone is not None:
            result['ReceiverPhone'] = self.receiver_phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        if m.get('ReceiverAddress') is not None:
            self.receiver_address = m.get('ReceiverAddress')
        if m.get('ReceiverName') is not None:
            self.receiver_name = m.get('ReceiverName')
        if m.get('ReceiverPhone') is not None:
            self.receiver_phone = m.get('ReceiverPhone')
        return self


class ApplyNotaryPostResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyNotaryPostResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ApplyNotaryPostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyNotaryPostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyNotaryPostResponse, self).to_map()
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
            temp_model = ApplyNotaryPostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AskAdjudicationFileRequest(TeaModel):
    def __init__(self, biz_id=None, contact_address=None, contact_city=None, contact_county=None,
                 contact_district=None, contact_name=None, contact_number=None, contact_province=None):
        self.biz_id = biz_id  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_city = contact_city  # type: str
        self.contact_county = contact_county  # type: str
        self.contact_district = contact_district  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_province = contact_province  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AskAdjudicationFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        return self


class AskAdjudicationFileResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AskAdjudicationFileResponseBody, self).to_map()
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


class AskAdjudicationFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AskAdjudicationFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AskAdjudicationFileResponse, self).to_map()
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
            temp_model = AskAdjudicationFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindMaterialRequest(TeaModel):
    def __init__(self, biz_id=None, legal_notice_key=None, loa_oss_key=None, material_id=None):
        self.biz_id = biz_id  # type: str
        self.legal_notice_key = legal_notice_key  # type: str
        self.loa_oss_key = loa_oss_key  # type: str
        self.material_id = material_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.legal_notice_key is not None:
            result['LegalNoticeKey'] = self.legal_notice_key
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LegalNoticeKey') is not None:
            self.legal_notice_key = m.get('LegalNoticeKey')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        return self


class BindMaterialResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindMaterialResponseBody, self).to_map()
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


class BindMaterialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindMaterialResponse, self).to_map()
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
            temp_model = BindMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelTradeOrderRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelTradeOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class CancelTradeOrderResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelTradeOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelTradeOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelTradeOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelTradeOrderResponse, self).to_map()
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
            temp_model = CancelTradeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckFlsmFillRequest(TeaModel):
    def __init__(self, applicant_type=None, oss_key=None, personal_type=None, wtr_name=None):
        self.applicant_type = applicant_type  # type: str
        self.oss_key = oss_key  # type: str
        self.personal_type = personal_type  # type: str
        self.wtr_name = wtr_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckFlsmFillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_type is not None:
            result['ApplicantType'] = self.applicant_type
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.wtr_name is not None:
            result['WtrName'] = self.wtr_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicantType') is not None:
            self.applicant_type = m.get('ApplicantType')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('WtrName') is not None:
            self.wtr_name = m.get('WtrName')
        return self


class CheckFlsmFillResponseBody(TeaModel):
    def __init__(self, request_id=None, tips=None):
        self.request_id = request_id  # type: str
        self.tips = tips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckFlsmFillResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class CheckFlsmFillResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckFlsmFillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckFlsmFillResponse, self).to_map()
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
            temp_model = CheckFlsmFillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckIfCollectedRequest(TeaModel):
    def __init__(self, item_id_list=None, page_num=None, page_size=None, type=None):
        self.item_id_list = item_id_list  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckIfCollectedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id_list is not None:
            result['ItemIdList'] = self.item_id_list
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemIdList') is not None:
            self.item_id_list = m.get('ItemIdList')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CheckIfCollectedResponseBodyDataTrademark(TeaModel):
    def __init__(self, id=None, item_id_list=None, name=None, type=None):
        self.id = id  # type: long
        self.item_id_list = item_id_list  # type: str
        self.name = name  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckIfCollectedResponseBodyDataTrademark, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.item_id_list is not None:
            result['ItemIdList'] = self.item_id_list
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemIdList') is not None:
            self.item_id_list = m.get('ItemIdList')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CheckIfCollectedResponseBodyData(TeaModel):
    def __init__(self, trademark=None):
        self.trademark = trademark  # type: list[CheckIfCollectedResponseBodyDataTrademark]

    def validate(self):
        if self.trademark:
            for k in self.trademark:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CheckIfCollectedResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Trademark'] = []
        if self.trademark is not None:
            for k in self.trademark:
                result['Trademark'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.trademark = []
        if m.get('Trademark') is not None:
            for k in m.get('Trademark'):
                temp_model = CheckIfCollectedResponseBodyDataTrademark()
                self.trademark.append(temp_model.from_map(k))
        return self


class CheckIfCollectedResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: CheckIfCollectedResponseBodyData
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CheckIfCollectedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = CheckIfCollectedResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class CheckIfCollectedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckIfCollectedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckIfCollectedResponse, self).to_map()
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
            temp_model = CheckIfCollectedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckLoaFillRequest(TeaModel):
    def __init__(self, applicant_type=None, biz_type=None, contact_name=None, contact_number=None,
                 contact_zipcode=None, oss_key=None, personal_type=None, principal_name=None, type=None, wtr_name=None):
        self.applicant_type = applicant_type  # type: str
        self.biz_type = biz_type  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_zipcode = contact_zipcode  # type: str
        self.oss_key = oss_key  # type: str
        self.personal_type = personal_type  # type: str
        self.principal_name = principal_name  # type: str
        self.type = type  # type: str
        self.wtr_name = wtr_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckLoaFillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_type is not None:
            result['ApplicantType'] = self.applicant_type
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.type is not None:
            result['Type'] = self.type
        if self.wtr_name is not None:
            result['WtrName'] = self.wtr_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicantType') is not None:
            self.applicant_type = m.get('ApplicantType')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WtrName') is not None:
            self.wtr_name = m.get('WtrName')
        return self


class CheckLoaFillResponseBodyDataErrorMsgs(TeaModel):
    def __init__(self, error_msg=None):
        self.error_msg = error_msg  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckLoaFillResponseBodyDataErrorMsgs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class CheckLoaFillResponseBodyData(TeaModel):
    def __init__(self, address_fill=None, country_fill=None, error_msgs=None, material_name_fill=None,
                 nationality_fill=None, stamp_fill=None, template_url=None, tips=None, trade_mark_name_fill=None):
        self.address_fill = address_fill  # type: bool
        self.country_fill = country_fill  # type: bool
        self.error_msgs = error_msgs  # type: CheckLoaFillResponseBodyDataErrorMsgs
        self.material_name_fill = material_name_fill  # type: bool
        self.nationality_fill = nationality_fill  # type: bool
        self.stamp_fill = stamp_fill  # type: bool
        self.template_url = template_url  # type: str
        self.tips = tips  # type: str
        self.trade_mark_name_fill = trade_mark_name_fill  # type: bool

    def validate(self):
        if self.error_msgs:
            self.error_msgs.validate()

    def to_map(self):
        _map = super(CheckLoaFillResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_fill is not None:
            result['AddressFill'] = self.address_fill
        if self.country_fill is not None:
            result['CountryFill'] = self.country_fill
        if self.error_msgs is not None:
            result['ErrorMsgs'] = self.error_msgs.to_map()
        if self.material_name_fill is not None:
            result['MaterialNameFill'] = self.material_name_fill
        if self.nationality_fill is not None:
            result['NationalityFill'] = self.nationality_fill
        if self.stamp_fill is not None:
            result['StampFill'] = self.stamp_fill
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.trade_mark_name_fill is not None:
            result['TradeMarkNameFill'] = self.trade_mark_name_fill
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressFill') is not None:
            self.address_fill = m.get('AddressFill')
        if m.get('CountryFill') is not None:
            self.country_fill = m.get('CountryFill')
        if m.get('ErrorMsgs') is not None:
            temp_model = CheckLoaFillResponseBodyDataErrorMsgs()
            self.error_msgs = temp_model.from_map(m['ErrorMsgs'])
        if m.get('MaterialNameFill') is not None:
            self.material_name_fill = m.get('MaterialNameFill')
        if m.get('NationalityFill') is not None:
            self.nationality_fill = m.get('NationalityFill')
        if m.get('StampFill') is not None:
            self.stamp_fill = m.get('StampFill')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('TradeMarkNameFill') is not None:
            self.trade_mark_name_fill = m.get('TradeMarkNameFill')
        return self


class CheckLoaFillResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CheckLoaFillResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CheckLoaFillResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CheckLoaFillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckLoaFillResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckLoaFillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckLoaFillResponse, self).to_map()
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
            temp_model = CheckLoaFillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckTrademarkIconRequest(TeaModel):
    def __init__(self, event_scene_type=None, trademark_icon_oss_key=None):
        self.event_scene_type = event_scene_type  # type: int
        self.trademark_icon_oss_key = trademark_icon_oss_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckTrademarkIconRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_scene_type is not None:
            result['EventSceneType'] = self.event_scene_type
        if self.trademark_icon_oss_key is not None:
            result['TrademarkIconOssKey'] = self.trademark_icon_oss_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventSceneType') is not None:
            self.event_scene_type = m.get('EventSceneType')
        if m.get('TrademarkIconOssKey') is not None:
            self.trademark_icon_oss_key = m.get('TrademarkIconOssKey')
        return self


class CheckTrademarkIconResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, result=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckTrademarkIconResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CheckTrademarkIconResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckTrademarkIconResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckTrademarkIconResponse, self).to_map()
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
            temp_model = CheckTrademarkIconResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckTrademarkOrderRequest(TeaModel):
    def __init__(self, agreement_id=None, biz_id=None, channel=None, is_black_icon=None, loa_oss_key=None,
                 logo_goods_id=None, material_id=None, order_data=None, partner_code=None, phone_num=None, real_user_name=None,
                 register_name=None, register_number=None, renew_info_id=None, root_code=None, tm_comment=None, tm_icon=None,
                 tm_name=None, tm_name_type=None, type=None, uid=None, user_id=None):
        self.agreement_id = agreement_id  # type: str
        self.biz_id = biz_id  # type: str
        self.channel = channel  # type: str
        self.is_black_icon = is_black_icon  # type: bool
        self.loa_oss_key = loa_oss_key  # type: str
        self.logo_goods_id = logo_goods_id  # type: str
        self.material_id = material_id  # type: str
        self.order_data = order_data  # type: str
        self.partner_code = partner_code  # type: str
        self.phone_num = phone_num  # type: str
        self.real_user_name = real_user_name  # type: str
        self.register_name = register_name  # type: str
        self.register_number = register_number  # type: str
        self.renew_info_id = renew_info_id  # type: str
        self.root_code = root_code  # type: str
        self.tm_comment = tm_comment  # type: str
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_name_type = tm_name_type  # type: str
        self.type = type  # type: int
        self.uid = uid  # type: str
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckTrademarkOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.is_black_icon is not None:
            result['IsBlackIcon'] = self.is_black_icon
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.logo_goods_id is not None:
            result['LogoGoodsId'] = self.logo_goods_id
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.order_data is not None:
            result['OrderData'] = self.order_data
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.real_user_name is not None:
            result['RealUserName'] = self.real_user_name
        if self.register_name is not None:
            result['RegisterName'] = self.register_name
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.renew_info_id is not None:
            result['RenewInfoId'] = self.renew_info_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('IsBlackIcon') is not None:
            self.is_black_icon = m.get('IsBlackIcon')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('LogoGoodsId') is not None:
            self.logo_goods_id = m.get('LogoGoodsId')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('OrderData') is not None:
            self.order_data = m.get('OrderData')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('RealUserName') is not None:
            self.real_user_name = m.get('RealUserName')
        if m.get('RegisterName') is not None:
            self.register_name = m.get('RegisterName')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('RenewInfoId') is not None:
            self.renew_info_id = m.get('RenewInfoId')
        if m.get('RootCode') is not None:
            self.root_code = m.get('RootCode')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CheckTrademarkOrderResponseBody(TeaModel):
    def __init__(self, data=None, error_msg=None, request_id=None, success=None):
        self.data = data  # type: dict[str, any]
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckTrademarkOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckTrademarkOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckTrademarkOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckTrademarkOrderResponse, self).to_map()
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
            temp_model = CheckTrademarkOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CombineLoaRequest(TeaModel):
    def __init__(self, address=None, applicant_type=None, contact_name=None, contact_phone=None,
                 contact_postcode=None, material_id=None, material_name=None, nationality=None, personal_type=None,
                 principal_name=None, tm_number=None, tm_produce_type=None, trademark_name=None):
        self.address = address  # type: str
        self.applicant_type = applicant_type  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_phone = contact_phone  # type: str
        self.contact_postcode = contact_postcode  # type: str
        self.material_id = material_id  # type: str
        self.material_name = material_name  # type: str
        self.nationality = nationality  # type: str
        self.personal_type = personal_type  # type: str
        self.principal_name = principal_name  # type: int
        self.tm_number = tm_number  # type: str
        self.tm_produce_type = tm_produce_type  # type: str
        self.trademark_name = trademark_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CombineLoaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.applicant_type is not None:
            result['ApplicantType'] = self.applicant_type
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_phone is not None:
            result['ContactPhone'] = self.contact_phone
        if self.contact_postcode is not None:
            result['ContactPostcode'] = self.contact_postcode
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.tm_produce_type is not None:
            result['TmProduceType'] = self.tm_produce_type
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicantType') is not None:
            self.applicant_type = m.get('ApplicantType')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactPhone') is not None:
            self.contact_phone = m.get('ContactPhone')
        if m.get('ContactPostcode') is not None:
            self.contact_postcode = m.get('ContactPostcode')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TmProduceType') is not None:
            self.tm_produce_type = m.get('TmProduceType')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        return self


class CombineLoaResponseBody(TeaModel):
    def __init__(self, request_id=None, template_combine_url=None):
        self.request_id = request_id  # type: str
        self.template_combine_url = template_combine_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CombineLoaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_combine_url is not None:
            result['TemplateCombineUrl'] = self.template_combine_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateCombineUrl') is not None:
            self.template_combine_url = m.get('TemplateCombineUrl')
        return self


class CombineLoaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CombineLoaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CombineLoaResponse, self).to_map()
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
            temp_model = CombineLoaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CombineWTSRequest(TeaModel):
    def __init__(self, address=None, contact=None, contact_address_post=None, contact_mobile=None, material_id=None,
                 material_name=None, nationality=None, principal_name=None, tm_num=None, tm_produce_type=None,
                 trademark_name=None, wts_type=None):
        self.address = address  # type: str
        self.contact = contact  # type: str
        self.contact_address_post = contact_address_post  # type: str
        self.contact_mobile = contact_mobile  # type: str
        self.material_id = material_id  # type: str
        self.material_name = material_name  # type: str
        self.nationality = nationality  # type: str
        self.principal_name = principal_name  # type: str
        self.tm_num = tm_num  # type: str
        self.tm_produce_type = tm_produce_type  # type: str
        self.trademark_name = trademark_name  # type: str
        self.wts_type = wts_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CombineWTSRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.contact is not None:
            result['Contact'] = self.contact
        if self.contact_address_post is not None:
            result['ContactAddressPost'] = self.contact_address_post
        if self.contact_mobile is not None:
            result['ContactMobile'] = self.contact_mobile
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.tm_num is not None:
            result['TmNum'] = self.tm_num
        if self.tm_produce_type is not None:
            result['TmProduceType'] = self.tm_produce_type
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.wts_type is not None:
            result['WtsType'] = self.wts_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')
        if m.get('ContactAddressPost') is not None:
            self.contact_address_post = m.get('ContactAddressPost')
        if m.get('ContactMobile') is not None:
            self.contact_mobile = m.get('ContactMobile')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('TmNum') is not None:
            self.tm_num = m.get('TmNum')
        if m.get('TmProduceType') is not None:
            self.tm_produce_type = m.get('TmProduceType')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('WtsType') is not None:
            self.wts_type = m.get('WtsType')
        return self


class CombineWTSResponseBody(TeaModel):
    def __init__(self, request_id=None, template_combine_url=None):
        self.request_id = request_id  # type: str
        self.template_combine_url = template_combine_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CombineWTSResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_combine_url is not None:
            result['TemplateCombineUrl'] = self.template_combine_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateCombineUrl') is not None:
            self.template_combine_url = m.get('TemplateCombineUrl')
        return self


class CombineWTSResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CombineWTSResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CombineWTSResponse, self).to_map()
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
            temp_model = CombineWTSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ComplementIntentionUserIdRequest(TeaModel):
    def __init__(self, aliyun_kp=None, bid=None, biz_id=None, caller_parent_id=None, caller_type=None,
                 complement_user_id=None, type=None):
        self.aliyun_kp = aliyun_kp  # type: str
        self.bid = bid  # type: str
        self.biz_id = biz_id  # type: str
        self.caller_parent_id = caller_parent_id  # type: long
        self.caller_type = caller_type  # type: str
        self.complement_user_id = complement_user_id  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ComplementIntentionUserIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.caller_parent_id is not None:
            result['CallerParentId'] = self.caller_parent_id
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.complement_user_id is not None:
            result['ComplementUserId'] = self.complement_user_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CallerParentId') is not None:
            self.caller_parent_id = m.get('CallerParentId')
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('ComplementUserId') is not None:
            self.complement_user_id = m.get('ComplementUserId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ComplementIntentionUserIdResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ComplementIntentionUserIdResponseBody, self).to_map()
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


class ComplementIntentionUserIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ComplementIntentionUserIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ComplementIntentionUserIdResponse, self).to_map()
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
            temp_model = ComplementIntentionUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmAdditionalMaterialRequest(TeaModel):
    def __init__(self, biz_id=None, note=None):
        self.biz_id = biz_id  # type: str
        self.note = note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmAdditionalMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class ConfirmAdditionalMaterialResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmAdditionalMaterialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfirmAdditionalMaterialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfirmAdditionalMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfirmAdditionalMaterialResponse, self).to_map()
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
            temp_model = ConfirmAdditionalMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmApplicantRequest(TeaModel):
    def __init__(self, biz_id=None, note=None):
        self.biz_id = biz_id  # type: str
        self.note = note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmApplicantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class ConfirmApplicantResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmApplicantResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfirmApplicantResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfirmApplicantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfirmApplicantResponse, self).to_map()
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
            temp_model = ConfirmApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmDissentOriginalRequest(TeaModel):
    def __init__(self, biz_id=None, contact_address=None, contact_city=None, contact_county=None,
                 contact_district=None, contact_name=None, contact_number=None, contact_province=None, operate_type=None):
        self.biz_id = biz_id  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_city = contact_city  # type: str
        self.contact_county = contact_county  # type: str
        self.contact_district = contact_district  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_province = contact_province  # type: str
        self.operate_type = operate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmDissentOriginalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class ConfirmDissentOriginalResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmDissentOriginalResponseBody, self).to_map()
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


class ConfirmDissentOriginalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfirmDissentOriginalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfirmDissentOriginalResponse, self).to_map()
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
            temp_model = ConfirmDissentOriginalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertImageToGrayRequest(TeaModel):
    def __init__(self, oss_key=None):
        self.oss_key = oss_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertImageToGrayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        return self


class ConvertImageToGrayResponseBody(TeaModel):
    def __init__(self, request_id=None, signature_url=None):
        self.request_id = request_id  # type: str
        self.signature_url = signature_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConvertImageToGrayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature_url is not None:
            result['SignatureUrl'] = self.signature_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignatureUrl') is not None:
            self.signature_url = m.get('SignatureUrl')
        return self


class ConvertImageToGrayResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConvertImageToGrayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConvertImageToGrayResponse, self).to_map()
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
            temp_model = ConvertImageToGrayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyApplicantRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopyApplicantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CopyApplicantResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopyApplicantResponseBody, self).to_map()
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


class CopyApplicantResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CopyApplicantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CopyApplicantResponse, self).to_map()
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
            temp_model = CopyApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentionOrderRequest(TeaModel):
    def __init__(self, channel=None, intention_biz_id=None):
        self.channel = channel  # type: str
        self.intention_biz_id = intention_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntentionOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        return self


class CreateIntentionOrderResponseBodyData(TeaModel):
    def __init__(self, order_ids=None):
        self.order_ids = order_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntentionOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class CreateIntentionOrderResponseBody(TeaModel):
    def __init__(self, data=None, error_msg=None, request_id=None, success=None):
        self.data = data  # type: CreateIntentionOrderResponseBodyData
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateIntentionOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateIntentionOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateIntentionOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateIntentionOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIntentionOrderResponse, self).to_map()
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
            temp_model = CreateIntentionOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentionOrderGeneratingPayRequest(TeaModel):
    def __init__(self, channel=None, intention_biz_id=None, payment_callback=None):
        self.channel = channel  # type: str
        self.intention_biz_id = intention_biz_id  # type: str
        self.payment_callback = payment_callback  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntentionOrderGeneratingPayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.payment_callback is not None:
            result['PaymentCallback'] = self.payment_callback
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PaymentCallback') is not None:
            self.payment_callback = m.get('PaymentCallback')
        return self


class CreateIntentionOrderGeneratingPayResponseBody(TeaModel):
    def __init__(self, error_msg=None, order_ids=None, pay_url=None, request_id=None, success=None):
        self.error_msg = error_msg  # type: str
        self.order_ids = order_ids  # type: list[long]
        self.pay_url = pay_url  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntentionOrderGeneratingPayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        if self.pay_url is not None:
            result['PayUrl'] = self.pay_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        if m.get('PayUrl') is not None:
            self.pay_url = m.get('PayUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateIntentionOrderGeneratingPayResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateIntentionOrderGeneratingPayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIntentionOrderGeneratingPayResponse, self).to_map()
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
            temp_model = CreateIntentionOrderGeneratingPayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrademarkOrderRequest(TeaModel):
    def __init__(self, agreement_id=None, big_dipper_source=None, biz_id=None, channel=None, is_black_icon=None,
                 legal_notice_key=None, loa_oss_key=None, material_id=None, order_data=None, partner_code=None, phone_num=None,
                 principal_name=None, real_user_name=None, register_name=None, register_number=None, renew_info_id=None,
                 root_code=None, session_id=None, tm_comment=None, tm_icon=None, tm_name=None, tm_name_type=None, type=None,
                 ua=None, uid=None, user_id=None):
        self.agreement_id = agreement_id  # type: str
        self.big_dipper_source = big_dipper_source  # type: str
        self.biz_id = biz_id  # type: str
        self.channel = channel  # type: str
        self.is_black_icon = is_black_icon  # type: bool
        self.legal_notice_key = legal_notice_key  # type: str
        self.loa_oss_key = loa_oss_key  # type: str
        self.material_id = material_id  # type: str
        self.order_data = order_data  # type: str
        self.partner_code = partner_code  # type: str
        self.phone_num = phone_num  # type: str
        self.principal_name = principal_name  # type: int
        self.real_user_name = real_user_name  # type: str
        self.register_name = register_name  # type: str
        self.register_number = register_number  # type: str
        self.renew_info_id = renew_info_id  # type: str
        self.root_code = root_code  # type: str
        self.session_id = session_id  # type: str
        self.tm_comment = tm_comment  # type: str
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_name_type = tm_name_type  # type: str
        self.type = type  # type: int
        self.ua = ua  # type: str
        self.uid = uid  # type: str
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrademarkOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.big_dipper_source is not None:
            result['BigDipperSource'] = self.big_dipper_source
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.is_black_icon is not None:
            result['IsBlackIcon'] = self.is_black_icon
        if self.legal_notice_key is not None:
            result['LegalNoticeKey'] = self.legal_notice_key
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.order_data is not None:
            result['OrderData'] = self.order_data
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.real_user_name is not None:
            result['RealUserName'] = self.real_user_name
        if self.register_name is not None:
            result['RegisterName'] = self.register_name
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.renew_info_id is not None:
            result['RenewInfoId'] = self.renew_info_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.type is not None:
            result['Type'] = self.type
        if self.ua is not None:
            result['Ua'] = self.ua
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('BigDipperSource') is not None:
            self.big_dipper_source = m.get('BigDipperSource')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('IsBlackIcon') is not None:
            self.is_black_icon = m.get('IsBlackIcon')
        if m.get('LegalNoticeKey') is not None:
            self.legal_notice_key = m.get('LegalNoticeKey')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('OrderData') is not None:
            self.order_data = m.get('OrderData')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('RealUserName') is not None:
            self.real_user_name = m.get('RealUserName')
        if m.get('RegisterName') is not None:
            self.register_name = m.get('RegisterName')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('RenewInfoId') is not None:
            self.renew_info_id = m.get('RenewInfoId')
        if m.get('RootCode') is not None:
            self.root_code = m.get('RootCode')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Ua') is not None:
            self.ua = m.get('Ua')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateTrademarkOrderResponseBody(TeaModel):
    def __init__(self, error_msg=None, order_id=None, request_id=None, success=None):
        self.error_msg = error_msg  # type: str
        self.order_id = order_id  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrademarkOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTrademarkOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTrademarkOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTrademarkOrderResponse, self).to_map()
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
            temp_model = CreateTrademarkOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMaterialRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteMaterialResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMaterialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMaterialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMaterialResponse, self).to_map()
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
            temp_model = DeleteMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTmMonitorRuleRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTmMonitorRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteTmMonitorRuleResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTmMonitorRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTmMonitorRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTmMonitorRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTmMonitorRuleResponse, self).to_map()
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
            temp_model = DeleteTmMonitorRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrademarkApplicationRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTrademarkApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DeleteTrademarkApplicationResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTrademarkApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTrademarkApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTrademarkApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTrademarkApplicationResponse, self).to_map()
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
            temp_model = DeleteTrademarkApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DenySupplementRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DenySupplementRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DenySupplementResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DenySupplementResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DenySupplementResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DenySupplementResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DenySupplementResponse, self).to_map()
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
            temp_model = DenySupplementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescirbeCombineTrademarkRequest(TeaModel):
    def __init__(self, accurate_match=None, classification=None, name=None, owner_name=None, page_number=None,
                 page_size=None, products=None, registration_number=None, similar_groups=None):
        self.accurate_match = accurate_match  # type: bool
        self.classification = classification  # type: str
        self.name = name  # type: str
        self.owner_name = owner_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.products = products  # type: str
        self.registration_number = registration_number  # type: str
        self.similar_groups = similar_groups  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescirbeCombineTrademarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accurate_match is not None:
            result['AccurateMatch'] = self.accurate_match
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.products is not None:
            result['Products'] = self.products
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.similar_groups is not None:
            result['SimilarGroups'] = self.similar_groups
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccurateMatch') is not None:
            self.accurate_match = m.get('AccurateMatch')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Products') is not None:
            self.products = m.get('Products')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('SimilarGroups') is not None:
            self.similar_groups = m.get('SimilarGroups')
        return self


class DescirbeCombineTrademarkResponseBodyDataAnnouncementList(TeaModel):
    def __init__(self, ann_date=None, ann_number=None, ann_type_code=None, ann_type_name=None, image_url=None,
                 original_image_url=None):
        self.ann_date = ann_date  # type: str
        self.ann_number = ann_number  # type: str
        self.ann_type_code = ann_type_code  # type: str
        self.ann_type_name = ann_type_name  # type: str
        self.image_url = image_url  # type: str
        self.original_image_url = original_image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescirbeCombineTrademarkResponseBodyDataAnnouncementList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ann_date is not None:
            result['AnnDate'] = self.ann_date
        if self.ann_number is not None:
            result['AnnNumber'] = self.ann_number
        if self.ann_type_code is not None:
            result['AnnTypeCode'] = self.ann_type_code
        if self.ann_type_name is not None:
            result['AnnTypeName'] = self.ann_type_name
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.original_image_url is not None:
            result['OriginalImageUrl'] = self.original_image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnnDate') is not None:
            self.ann_date = m.get('AnnDate')
        if m.get('AnnNumber') is not None:
            self.ann_number = m.get('AnnNumber')
        if m.get('AnnTypeCode') is not None:
            self.ann_type_code = m.get('AnnTypeCode')
        if m.get('AnnTypeName') is not None:
            self.ann_type_name = m.get('AnnTypeName')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('OriginalImageUrl') is not None:
            self.original_image_url = m.get('OriginalImageUrl')
        return self


class DescirbeCombineTrademarkResponseBodyDataProcedures(TeaModel):
    def __init__(self, procedure_code=None, procedure_date=None, procedure_name=None, procedure_result=None,
                 procedure_step=None):
        self.procedure_code = procedure_code  # type: str
        self.procedure_date = procedure_date  # type: str
        self.procedure_name = procedure_name  # type: str
        self.procedure_result = procedure_result  # type: str
        self.procedure_step = procedure_step  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescirbeCombineTrademarkResponseBodyDataProcedures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.procedure_code is not None:
            result['ProcedureCode'] = self.procedure_code
        if self.procedure_date is not None:
            result['ProcedureDate'] = self.procedure_date
        if self.procedure_name is not None:
            result['ProcedureName'] = self.procedure_name
        if self.procedure_result is not None:
            result['ProcedureResult'] = self.procedure_result
        if self.procedure_step is not None:
            result['ProcedureStep'] = self.procedure_step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProcedureCode') is not None:
            self.procedure_code = m.get('ProcedureCode')
        if m.get('ProcedureDate') is not None:
            self.procedure_date = m.get('ProcedureDate')
        if m.get('ProcedureName') is not None:
            self.procedure_name = m.get('ProcedureName')
        if m.get('ProcedureResult') is not None:
            self.procedure_result = m.get('ProcedureResult')
        if m.get('ProcedureStep') is not None:
            self.procedure_step = m.get('ProcedureStep')
        return self


class DescirbeCombineTrademarkResponseBodyData(TeaModel):
    def __init__(self, agency=None, announcement_list=None, apply_date=None, classification=None,
                 exclusive_date_limit=None, first_anno_number=None, first_anno_type=None, image=None, index_id=None, intl_reg_date=None,
                 last_procedure_status=None, law_final_status=None, name=None, on_sale=None, owner_address=None, owner_en_address=None,
                 owner_en_name=None, owner_name=None, pre_ann_date=None, pre_ann_number=None, priority_date=None, procedures=None,
                 product_description=None, reg_ann_date=None, reg_ann_number=None, registration_number=None, registration_type=None,
                 second_anno_number=None, second_anno_type=None, share=None, similar_group=None, status=None,
                 subsequent_designation_date=None):
        self.agency = agency  # type: str
        self.announcement_list = announcement_list  # type: list[DescirbeCombineTrademarkResponseBodyDataAnnouncementList]
        self.apply_date = apply_date  # type: str
        self.classification = classification  # type: str
        self.exclusive_date_limit = exclusive_date_limit  # type: str
        self.first_anno_number = first_anno_number  # type: str
        self.first_anno_type = first_anno_type  # type: str
        self.image = image  # type: str
        self.index_id = index_id  # type: str
        self.intl_reg_date = intl_reg_date  # type: str
        self.last_procedure_status = last_procedure_status  # type: str
        self.law_final_status = law_final_status  # type: str
        self.name = name  # type: str
        self.on_sale = on_sale  # type: int
        self.owner_address = owner_address  # type: str
        self.owner_en_address = owner_en_address  # type: str
        self.owner_en_name = owner_en_name  # type: str
        self.owner_name = owner_name  # type: str
        self.pre_ann_date = pre_ann_date  # type: str
        self.pre_ann_number = pre_ann_number  # type: str
        self.priority_date = priority_date  # type: str
        self.procedures = procedures  # type: list[DescirbeCombineTrademarkResponseBodyDataProcedures]
        self.product_description = product_description  # type: str
        self.reg_ann_date = reg_ann_date  # type: str
        self.reg_ann_number = reg_ann_number  # type: str
        self.registration_number = registration_number  # type: str
        self.registration_type = registration_type  # type: str
        self.second_anno_number = second_anno_number  # type: str
        self.second_anno_type = second_anno_type  # type: str
        self.share = share  # type: str
        self.similar_group = similar_group  # type: str
        self.status = status  # type: str
        self.subsequent_designation_date = subsequent_designation_date  # type: str

    def validate(self):
        if self.announcement_list:
            for k in self.announcement_list:
                if k:
                    k.validate()
        if self.procedures:
            for k in self.procedures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescirbeCombineTrademarkResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agency is not None:
            result['Agency'] = self.agency
        result['AnnouncementList'] = []
        if self.announcement_list is not None:
            for k in self.announcement_list:
                result['AnnouncementList'].append(k.to_map() if k else None)
        if self.apply_date is not None:
            result['ApplyDate'] = self.apply_date
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.exclusive_date_limit is not None:
            result['ExclusiveDateLimit'] = self.exclusive_date_limit
        if self.first_anno_number is not None:
            result['FirstAnnoNumber'] = self.first_anno_number
        if self.first_anno_type is not None:
            result['FirstAnnoType'] = self.first_anno_type
        if self.image is not None:
            result['Image'] = self.image
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.intl_reg_date is not None:
            result['IntlRegDate'] = self.intl_reg_date
        if self.last_procedure_status is not None:
            result['LastProcedureStatus'] = self.last_procedure_status
        if self.law_final_status is not None:
            result['LawFinalStatus'] = self.law_final_status
        if self.name is not None:
            result['Name'] = self.name
        if self.on_sale is not None:
            result['OnSale'] = self.on_sale
        if self.owner_address is not None:
            result['OwnerAddress'] = self.owner_address
        if self.owner_en_address is not None:
            result['OwnerEnAddress'] = self.owner_en_address
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.pre_ann_date is not None:
            result['PreAnnDate'] = self.pre_ann_date
        if self.pre_ann_number is not None:
            result['PreAnnNumber'] = self.pre_ann_number
        if self.priority_date is not None:
            result['PriorityDate'] = self.priority_date
        result['Procedures'] = []
        if self.procedures is not None:
            for k in self.procedures:
                result['Procedures'].append(k.to_map() if k else None)
        if self.product_description is not None:
            result['ProductDescription'] = self.product_description
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.reg_ann_number is not None:
            result['RegAnnNumber'] = self.reg_ann_number
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.registration_type is not None:
            result['RegistrationType'] = self.registration_type
        if self.second_anno_number is not None:
            result['SecondAnnoNumber'] = self.second_anno_number
        if self.second_anno_type is not None:
            result['SecondAnnoType'] = self.second_anno_type
        if self.share is not None:
            result['Share'] = self.share
        if self.similar_group is not None:
            result['SimilarGroup'] = self.similar_group
        if self.status is not None:
            result['Status'] = self.status
        if self.subsequent_designation_date is not None:
            result['SubsequentDesignationDate'] = self.subsequent_designation_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Agency') is not None:
            self.agency = m.get('Agency')
        self.announcement_list = []
        if m.get('AnnouncementList') is not None:
            for k in m.get('AnnouncementList'):
                temp_model = DescirbeCombineTrademarkResponseBodyDataAnnouncementList()
                self.announcement_list.append(temp_model.from_map(k))
        if m.get('ApplyDate') is not None:
            self.apply_date = m.get('ApplyDate')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('ExclusiveDateLimit') is not None:
            self.exclusive_date_limit = m.get('ExclusiveDateLimit')
        if m.get('FirstAnnoNumber') is not None:
            self.first_anno_number = m.get('FirstAnnoNumber')
        if m.get('FirstAnnoType') is not None:
            self.first_anno_type = m.get('FirstAnnoType')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('IntlRegDate') is not None:
            self.intl_reg_date = m.get('IntlRegDate')
        if m.get('LastProcedureStatus') is not None:
            self.last_procedure_status = m.get('LastProcedureStatus')
        if m.get('LawFinalStatus') is not None:
            self.law_final_status = m.get('LawFinalStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OnSale') is not None:
            self.on_sale = m.get('OnSale')
        if m.get('OwnerAddress') is not None:
            self.owner_address = m.get('OwnerAddress')
        if m.get('OwnerEnAddress') is not None:
            self.owner_en_address = m.get('OwnerEnAddress')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('PreAnnDate') is not None:
            self.pre_ann_date = m.get('PreAnnDate')
        if m.get('PreAnnNumber') is not None:
            self.pre_ann_number = m.get('PreAnnNumber')
        if m.get('PriorityDate') is not None:
            self.priority_date = m.get('PriorityDate')
        self.procedures = []
        if m.get('Procedures') is not None:
            for k in m.get('Procedures'):
                temp_model = DescirbeCombineTrademarkResponseBodyDataProcedures()
                self.procedures.append(temp_model.from_map(k))
        if m.get('ProductDescription') is not None:
            self.product_description = m.get('ProductDescription')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('RegAnnNumber') is not None:
            self.reg_ann_number = m.get('RegAnnNumber')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('RegistrationType') is not None:
            self.registration_type = m.get('RegistrationType')
        if m.get('SecondAnnoNumber') is not None:
            self.second_anno_number = m.get('SecondAnnoNumber')
        if m.get('SecondAnnoType') is not None:
            self.second_anno_type = m.get('SecondAnnoType')
        if m.get('Share') is not None:
            self.share = m.get('Share')
        if m.get('SimilarGroup') is not None:
            self.similar_group = m.get('SimilarGroup')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubsequentDesignationDate') is not None:
            self.subsequent_designation_date = m.get('SubsequentDesignationDate')
        return self


class DescirbeCombineTrademarkResponseBody(TeaModel):
    def __init__(self, current_page_number=None, data=None, next_page=None, page_size=None, pre_page=None,
                 request_id=None, total_item_number=None, total_page_number=None):
        self.current_page_number = current_page_number  # type: int
        self.data = data  # type: list[DescirbeCombineTrademarkResponseBodyData]
        self.next_page = next_page  # type: bool
        self.page_size = page_size  # type: int
        self.pre_page = pre_page  # type: bool
        self.request_id = request_id  # type: str
        self.total_item_number = total_item_number  # type: int
        self.total_page_number = total_page_number  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescirbeCombineTrademarkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_number is not None:
            result['CurrentPageNumber'] = self.current_page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_number is not None:
            result['TotalItemNumber'] = self.total_item_number
        if self.total_page_number is not None:
            result['TotalPageNumber'] = self.total_page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNumber') is not None:
            self.current_page_number = m.get('CurrentPageNumber')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescirbeCombineTrademarkResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNumber') is not None:
            self.total_item_number = m.get('TotalItemNumber')
        if m.get('TotalPageNumber') is not None:
            self.total_page_number = m.get('TotalPageNumber')
        return self


class DescirbeCombineTrademarkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescirbeCombineTrademarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescirbeCombineTrademarkResponse, self).to_map()
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
            temp_model = DescirbeCombineTrademarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FillLogisticsRequest(TeaModel):
    def __init__(self, biz_id=None, logistics=None):
        self.biz_id = biz_id  # type: str
        self.logistics = logistics  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FillLogisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.logistics is not None:
            result['Logistics'] = self.logistics
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Logistics') is not None:
            self.logistics = m.get('Logistics')
        return self


class FillLogisticsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(FillLogisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FillLogisticsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FillLogisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FillLogisticsResponse, self).to_map()
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
            temp_model = FillLogisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FilterUnavailableCodesRequest(TeaModel):
    def __init__(self, codes=None):
        self.codes = codes  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilterUnavailableCodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes is not None:
            result['Codes'] = self.codes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes = m.get('Codes')
        return self


class FilterUnavailableCodesShrinkRequest(TeaModel):
    def __init__(self, codes_shrink=None):
        self.codes_shrink = codes_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilterUnavailableCodesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes_shrink is not None:
            result['Codes'] = self.codes_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes_shrink = m.get('Codes')
        return self


class FilterUnavailableCodesResponseBodyData(TeaModel):
    def __init__(self, codes=None):
        self.codes = codes  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilterUnavailableCodesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes is not None:
            result['Codes'] = self.codes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes = m.get('Codes')
        return self


class FilterUnavailableCodesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: FilterUnavailableCodesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(FilterUnavailableCodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = FilterUnavailableCodesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FilterUnavailableCodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FilterUnavailableCodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FilterUnavailableCodesResponse, self).to_map()
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
            temp_model = FilterUnavailableCodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ForceUploadTrademarkOnsaleRequest(TeaModel):
    def __init__(self, begin_time=None, classification_code=None, description=None, end_time=None, label=None,
                 original_price=None, owner_en_name=None, owner_name=None, reason=None, reg_ann_date=None,
                 secondary_classification=None, third_classification=None, tm_icon=None, tm_name=None, tm_number=None, type=None):
        self.begin_time = begin_time  # type: long
        self.classification_code = classification_code  # type: str
        self.description = description  # type: str
        self.end_time = end_time  # type: long
        self.label = label  # type: str
        self.original_price = original_price  # type: float
        self.owner_en_name = owner_en_name  # type: str
        self.owner_name = owner_name  # type: str
        self.reason = reason  # type: str
        self.reg_ann_date = reg_ann_date  # type: long
        self.secondary_classification = secondary_classification  # type: str
        self.third_classification = third_classification  # type: str
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_number = tm_number  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForceUploadTrademarkOnsaleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.label is not None:
            result['Label'] = self.label
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ForceUploadTrademarkOnsaleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForceUploadTrademarkOnsaleResponseBody, self).to_map()
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


class ForceUploadTrademarkOnsaleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ForceUploadTrademarkOnsaleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ForceUploadTrademarkOnsaleResponse, self).to_map()
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
            temp_model = ForceUploadTrademarkOnsaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateQrCodeRequest(TeaModel):
    def __init__(self, field_key=None, oss_key=None, uuid=None):
        self.field_key = field_key  # type: str
        self.oss_key = oss_key  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateQrCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GenerateQrCodeResponseBody(TeaModel):
    def __init__(self, expire_time=None, field_key=None, qrcode_url=None, request_id=None, success=None, uuid=None):
        self.expire_time = expire_time  # type: long
        self.field_key = field_key  # type: str
        self.qrcode_url = qrcode_url  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateQrCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        if self.qrcode_url is not None:
            result['QrcodeUrl'] = self.qrcode_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        if m.get('QrcodeUrl') is not None:
            self.qrcode_url = m.get('QrcodeUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GenerateQrCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateQrCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateQrCodeResponse, self).to_map()
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
            temp_model = GenerateQrCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadFilePolicyRequest(TeaModel):
    def __init__(self, biz_id=None, file_type=None):
        self.biz_id = biz_id  # type: str
        self.file_type = file_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUploadFilePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.file_type is not None:
            result['FileType'] = self.file_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        return self


class GenerateUploadFilePolicyResponseBody(TeaModel):
    def __init__(self, access_id=None, encoded_policy=None, expire_time=None, file_dir=None, host=None,
                 request_id=None, signature=None):
        # accessId
        self.access_id = access_id  # type: str
        # osspolicy
        self.encoded_policy = encoded_policy  # type: str
        self.expire_time = expire_time  # type: long
        self.file_dir = file_dir  # type: str
        self.host = host  # type: str
        self.request_id = request_id  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUploadFilePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.encoded_policy is not None:
            result['EncodedPolicy'] = self.encoded_policy
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.file_dir is not None:
            result['FileDir'] = self.file_dir
        if self.host is not None:
            result['Host'] = self.host
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('EncodedPolicy') is not None:
            self.encoded_policy = m.get('EncodedPolicy')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FileDir') is not None:
            self.file_dir = m.get('FileDir')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class GenerateUploadFilePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateUploadFilePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateUploadFilePolicyResponse, self).to_map()
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
            temp_model = GenerateUploadFilePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthorizationLetterVersionRequest(TeaModel):
    def __init__(self, oss_key=None):
        self.oss_key = oss_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthorizationLetterVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        return self


class GetAuthorizationLetterVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, version=None):
        self.request_id = request_id  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthorizationLetterVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetAuthorizationLetterVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAuthorizationLetterVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAuthorizationLetterVersionResponse, self).to_map()
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
            temp_model = GetAuthorizationLetterVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultPrincipalResponseBody(TeaModel):
    def __init__(self, principal_description=None, principal_name=None, principal_value=None, request_id=None):
        self.principal_description = principal_description  # type: str
        self.principal_name = principal_name  # type: str
        self.principal_value = principal_value  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDefaultPrincipalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_value is not None:
            result['PrincipalValue'] = self.principal_value
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalValue') is not None:
            self.principal_value = m.get('PrincipalValue')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDefaultPrincipalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDefaultPrincipalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDefaultPrincipalResponse, self).to_map()
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
            temp_model = GetDefaultPrincipalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultPrincipalNameRequest(TeaModel):
    def __init__(self, biz_type=None):
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDefaultPrincipalNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class GetDefaultPrincipalNameResponseBody(TeaModel):
    def __init__(self, principal_name=None, request_id=None):
        self.principal_name = principal_name  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDefaultPrincipalNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDefaultPrincipalNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDefaultPrincipalNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDefaultPrincipalNameResponse, self).to_map()
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
            temp_model = GetDefaultPrincipalNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNotaryOrderRequest(TeaModel):
    def __init__(self, notary_order_id=None):
        self.notary_order_id = notary_order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNotaryOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        return self


class GetNotaryOrderResponseBody(TeaModel):
    def __init__(self, aliyun_order_id=None, apply_post_status=None, biz_id=None, business_license=None,
                 business_license_id=None, company_contact_name=None, company_contact_phone=None, error_code=None, error_msg=None,
                 legal_person_id_card=None, legal_person_name=None, legal_person_phone=None, name=None, notary_accept_date=None,
                 notary_certificate=None, notary_failed_date=None, notary_failed_reason=None, notary_order_id=None,
                 notary_platform_name=None, notary_post_receipt=None, notary_status=None, notary_succeed_date=None, notary_type=None,
                 order_date=None, order_price=None, phone=None, receiver_address=None, receiver_name=None, receiver_phone=None,
                 receiver_postal_code=None, request_id=None, seller_back_of_id_card=None, seller_company_name=None,
                 seller_front_of_id_card=None, success=None, tm_accept_certificate=None, tm_classification=None, tm_image=None,
                 tm_name=None, tm_register_certificate=None, tm_register_change_certificate=None, tm_register_no=None,
                 type=None):
        self.aliyun_order_id = aliyun_order_id  # type: str
        self.apply_post_status = apply_post_status  # type: int
        self.biz_id = biz_id  # type: str
        self.business_license = business_license  # type: str
        self.business_license_id = business_license_id  # type: str
        self.company_contact_name = company_contact_name  # type: str
        self.company_contact_phone = company_contact_phone  # type: str
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.legal_person_id_card = legal_person_id_card  # type: str
        self.legal_person_name = legal_person_name  # type: str
        self.legal_person_phone = legal_person_phone  # type: str
        self.name = name  # type: str
        self.notary_accept_date = notary_accept_date  # type: long
        self.notary_certificate = notary_certificate  # type: str
        self.notary_failed_date = notary_failed_date  # type: long
        self.notary_failed_reason = notary_failed_reason  # type: str
        self.notary_order_id = notary_order_id  # type: long
        self.notary_platform_name = notary_platform_name  # type: str
        self.notary_post_receipt = notary_post_receipt  # type: str
        self.notary_status = notary_status  # type: int
        self.notary_succeed_date = notary_succeed_date  # type: long
        self.notary_type = notary_type  # type: int
        self.order_date = order_date  # type: long
        self.order_price = order_price  # type: float
        self.phone = phone  # type: str
        self.receiver_address = receiver_address  # type: str
        self.receiver_name = receiver_name  # type: str
        self.receiver_phone = receiver_phone  # type: str
        self.receiver_postal_code = receiver_postal_code  # type: str
        self.request_id = request_id  # type: str
        self.seller_back_of_id_card = seller_back_of_id_card  # type: str
        self.seller_company_name = seller_company_name  # type: str
        self.seller_front_of_id_card = seller_front_of_id_card  # type: str
        self.success = success  # type: bool
        self.tm_accept_certificate = tm_accept_certificate  # type: str
        self.tm_classification = tm_classification  # type: str
        self.tm_image = tm_image  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_register_certificate = tm_register_certificate  # type: str
        self.tm_register_change_certificate = tm_register_change_certificate  # type: str
        self.tm_register_no = tm_register_no  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNotaryOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.apply_post_status is not None:
            result['ApplyPostStatus'] = self.apply_post_status
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.business_license is not None:
            result['BusinessLicense'] = self.business_license
        if self.business_license_id is not None:
            result['BusinessLicenseId'] = self.business_license_id
        if self.company_contact_name is not None:
            result['CompanyContactName'] = self.company_contact_name
        if self.company_contact_phone is not None:
            result['CompanyContactPhone'] = self.company_contact_phone
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.legal_person_id_card is not None:
            result['LegalPersonIdCard'] = self.legal_person_id_card
        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name
        if self.legal_person_phone is not None:
            result['LegalPersonPhone'] = self.legal_person_phone
        if self.name is not None:
            result['Name'] = self.name
        if self.notary_accept_date is not None:
            result['NotaryAcceptDate'] = self.notary_accept_date
        if self.notary_certificate is not None:
            result['NotaryCertificate'] = self.notary_certificate
        if self.notary_failed_date is not None:
            result['NotaryFailedDate'] = self.notary_failed_date
        if self.notary_failed_reason is not None:
            result['NotaryFailedReason'] = self.notary_failed_reason
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        if self.notary_platform_name is not None:
            result['NotaryPlatformName'] = self.notary_platform_name
        if self.notary_post_receipt is not None:
            result['NotaryPostReceipt'] = self.notary_post_receipt
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.notary_succeed_date is not None:
            result['NotarySucceedDate'] = self.notary_succeed_date
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.order_date is not None:
            result['OrderDate'] = self.order_date
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.receiver_address is not None:
            result['ReceiverAddress'] = self.receiver_address
        if self.receiver_name is not None:
            result['ReceiverName'] = self.receiver_name
        if self.receiver_phone is not None:
            result['ReceiverPhone'] = self.receiver_phone
        if self.receiver_postal_code is not None:
            result['ReceiverPostalCode'] = self.receiver_postal_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.seller_back_of_id_card is not None:
            result['SellerBackOfIdCard'] = self.seller_back_of_id_card
        if self.seller_company_name is not None:
            result['SellerCompanyName'] = self.seller_company_name
        if self.seller_front_of_id_card is not None:
            result['SellerFrontOfIdCard'] = self.seller_front_of_id_card
        if self.success is not None:
            result['Success'] = self.success
        if self.tm_accept_certificate is not None:
            result['TmAcceptCertificate'] = self.tm_accept_certificate
        if self.tm_classification is not None:
            result['TmClassification'] = self.tm_classification
        if self.tm_image is not None:
            result['TmImage'] = self.tm_image
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_register_certificate is not None:
            result['TmRegisterCertificate'] = self.tm_register_certificate
        if self.tm_register_change_certificate is not None:
            result['TmRegisterChangeCertificate'] = self.tm_register_change_certificate
        if self.tm_register_no is not None:
            result['TmRegisterNo'] = self.tm_register_no
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('ApplyPostStatus') is not None:
            self.apply_post_status = m.get('ApplyPostStatus')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BusinessLicense') is not None:
            self.business_license = m.get('BusinessLicense')
        if m.get('BusinessLicenseId') is not None:
            self.business_license_id = m.get('BusinessLicenseId')
        if m.get('CompanyContactName') is not None:
            self.company_contact_name = m.get('CompanyContactName')
        if m.get('CompanyContactPhone') is not None:
            self.company_contact_phone = m.get('CompanyContactPhone')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('LegalPersonIdCard') is not None:
            self.legal_person_id_card = m.get('LegalPersonIdCard')
        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')
        if m.get('LegalPersonPhone') is not None:
            self.legal_person_phone = m.get('LegalPersonPhone')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotaryAcceptDate') is not None:
            self.notary_accept_date = m.get('NotaryAcceptDate')
        if m.get('NotaryCertificate') is not None:
            self.notary_certificate = m.get('NotaryCertificate')
        if m.get('NotaryFailedDate') is not None:
            self.notary_failed_date = m.get('NotaryFailedDate')
        if m.get('NotaryFailedReason') is not None:
            self.notary_failed_reason = m.get('NotaryFailedReason')
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        if m.get('NotaryPlatformName') is not None:
            self.notary_platform_name = m.get('NotaryPlatformName')
        if m.get('NotaryPostReceipt') is not None:
            self.notary_post_receipt = m.get('NotaryPostReceipt')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('NotarySucceedDate') is not None:
            self.notary_succeed_date = m.get('NotarySucceedDate')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('OrderDate') is not None:
            self.order_date = m.get('OrderDate')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ReceiverAddress') is not None:
            self.receiver_address = m.get('ReceiverAddress')
        if m.get('ReceiverName') is not None:
            self.receiver_name = m.get('ReceiverName')
        if m.get('ReceiverPhone') is not None:
            self.receiver_phone = m.get('ReceiverPhone')
        if m.get('ReceiverPostalCode') is not None:
            self.receiver_postal_code = m.get('ReceiverPostalCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SellerBackOfIdCard') is not None:
            self.seller_back_of_id_card = m.get('SellerBackOfIdCard')
        if m.get('SellerCompanyName') is not None:
            self.seller_company_name = m.get('SellerCompanyName')
        if m.get('SellerFrontOfIdCard') is not None:
            self.seller_front_of_id_card = m.get('SellerFrontOfIdCard')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TmAcceptCertificate') is not None:
            self.tm_accept_certificate = m.get('TmAcceptCertificate')
        if m.get('TmClassification') is not None:
            self.tm_classification = m.get('TmClassification')
        if m.get('TmImage') is not None:
            self.tm_image = m.get('TmImage')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmRegisterCertificate') is not None:
            self.tm_register_certificate = m.get('TmRegisterCertificate')
        if m.get('TmRegisterChangeCertificate') is not None:
            self.tm_register_change_certificate = m.get('TmRegisterChangeCertificate')
        if m.get('TmRegisterNo') is not None:
            self.tm_register_no = m.get('TmRegisterNo')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetNotaryOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetNotaryOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNotaryOrderResponse, self).to_map()
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
            temp_model = GetNotaryOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSupportPrincipalNameResponseBodyPrincipals(TeaModel):
    def __init__(self, default_principal=None, principal_description=None, principal_value=None):
        self.default_principal = default_principal  # type: bool
        self.principal_description = principal_description  # type: str
        self.principal_value = principal_value  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSupportPrincipalNameResponseBodyPrincipals, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_principal is not None:
            result['DefaultPrincipal'] = self.default_principal
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.principal_value is not None:
            result['PrincipalValue'] = self.principal_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultPrincipal') is not None:
            self.default_principal = m.get('DefaultPrincipal')
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('PrincipalValue') is not None:
            self.principal_value = m.get('PrincipalValue')
        return self


class GetSupportPrincipalNameResponseBody(TeaModel):
    def __init__(self, principals=None, request_id=None):
        self.principals = principals  # type: list[GetSupportPrincipalNameResponseBodyPrincipals]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.principals:
            for k in self.principals:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSupportPrincipalNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Principals'] = []
        if self.principals is not None:
            for k in self.principals:
                result['Principals'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.principals = []
        if m.get('Principals') is not None:
            for k in m.get('Principals'):
                temp_model = GetSupportPrincipalNameResponseBodyPrincipals()
                self.principals.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSupportPrincipalNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSupportPrincipalNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSupportPrincipalNameResponse, self).to_map()
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
            temp_model = GetSupportPrincipalNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertMaterialRequest(TeaModel):
    def __init__(self, address=None, business_licence_oss_key=None, card_number=None, city=None,
                 contact_address=None, contact_city=None, contact_county=None, contact_district=None, contact_email=None,
                 contact_name=None, contact_number=None, contact_province=None, contact_zipcode=None, country=None,
                 eaddress=None, ename=None, id_card_name=None, id_card_number=None, id_card_oss_key=None,
                 legal_notice_oss_key=None, loa_oss_key=None, name=None, passport_oss_key=None, personal_type=None, principal_name=None,
                 province=None, region=None, town=None, type=None):
        self.address = address  # type: str
        self.business_licence_oss_key = business_licence_oss_key  # type: str
        self.card_number = card_number  # type: str
        self.city = city  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_city = contact_city  # type: str
        self.contact_county = contact_county  # type: str
        self.contact_district = contact_district  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_province = contact_province  # type: str
        self.contact_zipcode = contact_zipcode  # type: str
        self.country = country  # type: str
        self.eaddress = eaddress  # type: str
        self.ename = ename  # type: str
        self.id_card_name = id_card_name  # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_oss_key = id_card_oss_key  # type: str
        self.legal_notice_oss_key = legal_notice_oss_key  # type: str
        self.loa_oss_key = loa_oss_key  # type: str
        self.name = name  # type: str
        self.passport_oss_key = passport_oss_key  # type: str
        self.personal_type = personal_type  # type: long
        self.principal_name = principal_name  # type: int
        self.province = province  # type: str
        self.region = region  # type: int
        self.town = town  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        if self.town is not None:
            result['Town'] = self.town
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class InsertMaterialResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertMaterialResponseBody, self).to_map()
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


class InsertMaterialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InsertMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertMaterialResponse, self).to_map()
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
            temp_model = InsertMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertRenewInfoRequest(TeaModel):
    def __init__(self, address=None, eng_address=None, eng_name=None, name=None, register_time=None):
        self.address = address  # type: str
        self.eng_address = eng_address  # type: str
        self.eng_name = eng_name  # type: str
        self.name = name  # type: str
        self.register_time = register_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRenewInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.name is not None:
            result['Name'] = self.name
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        return self


class InsertRenewInfoResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, id=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.id = id  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertRenewInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertRenewInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InsertRenewInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertRenewInfoResponse, self).to_map()
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
            temp_model = InsertRenewInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertTmMonitorRuleRequest(TeaModel):
    def __init__(self, classification=None, end_apply_date=None, notify_status=None, rule_keyword=None,
                 rule_name=None, rule_source=None, rule_type=None, start_apply_date=None):
        self.classification = classification  # type: dict[str, any]
        self.end_apply_date = end_apply_date  # type: str
        self.notify_status = notify_status  # type: dict[str, any]
        self.rule_keyword = rule_keyword  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_source = rule_source  # type: str
        self.rule_type = rule_type  # type: int
        self.start_apply_date = start_apply_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertTmMonitorRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.end_apply_date is not None:
            result['EndApplyDate'] = self.end_apply_date
        if self.notify_status is not None:
            result['NotifyStatus'] = self.notify_status
        if self.rule_keyword is not None:
            result['RuleKeyword'] = self.rule_keyword
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_apply_date is not None:
            result['StartApplyDate'] = self.start_apply_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('EndApplyDate') is not None:
            self.end_apply_date = m.get('EndApplyDate')
        if m.get('NotifyStatus') is not None:
            self.notify_status = m.get('NotifyStatus')
        if m.get('RuleKeyword') is not None:
            self.rule_keyword = m.get('RuleKeyword')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartApplyDate') is not None:
            self.start_apply_date = m.get('StartApplyDate')
        return self


class InsertTmMonitorRuleShrinkRequest(TeaModel):
    def __init__(self, classification_shrink=None, end_apply_date=None, notify_status_shrink=None,
                 rule_keyword=None, rule_name=None, rule_source=None, rule_type=None, start_apply_date=None):
        self.classification_shrink = classification_shrink  # type: str
        self.end_apply_date = end_apply_date  # type: str
        self.notify_status_shrink = notify_status_shrink  # type: str
        self.rule_keyword = rule_keyword  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_source = rule_source  # type: str
        self.rule_type = rule_type  # type: int
        self.start_apply_date = start_apply_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertTmMonitorRuleShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_shrink is not None:
            result['Classification'] = self.classification_shrink
        if self.end_apply_date is not None:
            result['EndApplyDate'] = self.end_apply_date
        if self.notify_status_shrink is not None:
            result['NotifyStatus'] = self.notify_status_shrink
        if self.rule_keyword is not None:
            result['RuleKeyword'] = self.rule_keyword
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_apply_date is not None:
            result['StartApplyDate'] = self.start_apply_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification_shrink = m.get('Classification')
        if m.get('EndApplyDate') is not None:
            self.end_apply_date = m.get('EndApplyDate')
        if m.get('NotifyStatus') is not None:
            self.notify_status_shrink = m.get('NotifyStatus')
        if m.get('RuleKeyword') is not None:
            self.rule_keyword = m.get('RuleKeyword')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartApplyDate') is not None:
            self.start_apply_date = m.get('StartApplyDate')
        return self


class InsertTmMonitorRuleResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertTmMonitorRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertTmMonitorRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InsertTmMonitorRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertTmMonitorRuleResponse, self).to_map()
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
            temp_model = InsertTmMonitorRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNotaryInfosRequest(TeaModel):
    def __init__(self, biz_order_no=None, notary_type=None, page_num=None, page_size=None, token=None):
        self.biz_order_no = biz_order_no  # type: str
        self.notary_type = notary_type  # type: int
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNotaryInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_order_no is not None:
            result['BizOrderNo'] = self.biz_order_no
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizOrderNo') is not None:
            self.biz_order_no = m.get('BizOrderNo')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class ListNotaryInfosResponseBodyDataNotaryInfo(TeaModel):
    def __init__(self, biz_order_no=None, gmt_modified=None, notary_failed_reason=None, notary_status=None,
                 tm_classification=None, tm_register_no=None, token=None):
        self.biz_order_no = biz_order_no  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.notary_failed_reason = notary_failed_reason  # type: str
        self.notary_status = notary_status  # type: int
        self.tm_classification = tm_classification  # type: str
        self.tm_register_no = tm_register_no  # type: str
        # token
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNotaryInfosResponseBodyDataNotaryInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_order_no is not None:
            result['BizOrderNo'] = self.biz_order_no
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.notary_failed_reason is not None:
            result['NotaryFailedReason'] = self.notary_failed_reason
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.tm_classification is not None:
            result['TmClassification'] = self.tm_classification
        if self.tm_register_no is not None:
            result['TmRegisterNo'] = self.tm_register_no
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizOrderNo') is not None:
            self.biz_order_no = m.get('BizOrderNo')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('NotaryFailedReason') is not None:
            self.notary_failed_reason = m.get('NotaryFailedReason')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('TmClassification') is not None:
            self.tm_classification = m.get('TmClassification')
        if m.get('TmRegisterNo') is not None:
            self.tm_register_no = m.get('TmRegisterNo')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class ListNotaryInfosResponseBodyData(TeaModel):
    def __init__(self, notary_info=None):
        self.notary_info = notary_info  # type: list[ListNotaryInfosResponseBodyDataNotaryInfo]

    def validate(self):
        if self.notary_info:
            for k in self.notary_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNotaryInfosResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NotaryInfo'] = []
        if self.notary_info is not None:
            for k in self.notary_info:
                result['NotaryInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.notary_info = []
        if m.get('NotaryInfo') is not None:
            for k in m.get('NotaryInfo'):
                temp_model = ListNotaryInfosResponseBodyDataNotaryInfo()
                self.notary_info.append(temp_model.from_map(k))
        return self


class ListNotaryInfosResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, error_code=None, error_msg=None, next_page=None,
                 page_size=None, pre_page=None, request_id=None, success=None, total_item_num=None, total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: ListNotaryInfosResponseBodyData
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.next_page = next_page  # type: bool
        self.page_size = page_size  # type: int
        self.pre_page = pre_page  # type: bool
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListNotaryInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = ListNotaryInfosResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListNotaryInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNotaryInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNotaryInfosResponse, self).to_map()
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
            temp_model = ListNotaryInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNotaryOrdersRequest(TeaModel):
    def __init__(self, aliyun_order_id=None, biz_id=None, end_order_date=None, notary_status=None, notary_type=None,
                 page_num=None, page_size=None, sort_by_type=None, sort_key_type=None, start_order_date=None):
        self.aliyun_order_id = aliyun_order_id  # type: str
        self.biz_id = biz_id  # type: str
        self.end_order_date = end_order_date  # type: long
        self.notary_status = notary_status  # type: int
        self.notary_type = notary_type  # type: int
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.sort_by_type = sort_by_type  # type: str
        self.sort_key_type = sort_key_type  # type: int
        self.start_order_date = start_order_date  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNotaryOrdersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.end_order_date is not None:
            result['EndOrderDate'] = self.end_order_date
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by_type is not None:
            result['SortByType'] = self.sort_by_type
        if self.sort_key_type is not None:
            result['SortKeyType'] = self.sort_key_type
        if self.start_order_date is not None:
            result['StartOrderDate'] = self.start_order_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('EndOrderDate') is not None:
            self.end_order_date = m.get('EndOrderDate')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortByType') is not None:
            self.sort_by_type = m.get('SortByType')
        if m.get('SortKeyType') is not None:
            self.sort_key_type = m.get('SortKeyType')
        if m.get('StartOrderDate') is not None:
            self.start_order_date = m.get('StartOrderDate')
        return self


class ListNotaryOrdersResponseBodyDataNotaryOrder(TeaModel):
    def __init__(self, aliyun_order_id=None, apply_post_status=None, biz_id=None, gmt_modified=None,
                 notary_certificate=None, notary_order_id=None, notary_platform_name=None, notary_status=None, notary_type=None,
                 order_date=None, order_price=None, tm_classification=None, tm_image=None, tm_name=None, tm_register_no=None):
        self.aliyun_order_id = aliyun_order_id  # type: str
        self.apply_post_status = apply_post_status  # type: str
        self.biz_id = biz_id  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.notary_certificate = notary_certificate  # type: str
        self.notary_order_id = notary_order_id  # type: long
        self.notary_platform_name = notary_platform_name  # type: str
        self.notary_status = notary_status  # type: int
        self.notary_type = notary_type  # type: int
        self.order_date = order_date  # type: long
        self.order_price = order_price  # type: float
        self.tm_classification = tm_classification  # type: str
        self.tm_image = tm_image  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_register_no = tm_register_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNotaryOrdersResponseBodyDataNotaryOrder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.apply_post_status is not None:
            result['ApplyPostStatus'] = self.apply_post_status
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.notary_certificate is not None:
            result['NotaryCertificate'] = self.notary_certificate
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        if self.notary_platform_name is not None:
            result['NotaryPlatformName'] = self.notary_platform_name
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.order_date is not None:
            result['OrderDate'] = self.order_date
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.tm_classification is not None:
            result['TmClassification'] = self.tm_classification
        if self.tm_image is not None:
            result['TmImage'] = self.tm_image
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_register_no is not None:
            result['TmRegisterNo'] = self.tm_register_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('ApplyPostStatus') is not None:
            self.apply_post_status = m.get('ApplyPostStatus')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('NotaryCertificate') is not None:
            self.notary_certificate = m.get('NotaryCertificate')
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        if m.get('NotaryPlatformName') is not None:
            self.notary_platform_name = m.get('NotaryPlatformName')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('OrderDate') is not None:
            self.order_date = m.get('OrderDate')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('TmClassification') is not None:
            self.tm_classification = m.get('TmClassification')
        if m.get('TmImage') is not None:
            self.tm_image = m.get('TmImage')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmRegisterNo') is not None:
            self.tm_register_no = m.get('TmRegisterNo')
        return self


class ListNotaryOrdersResponseBodyData(TeaModel):
    def __init__(self, notary_order=None):
        self.notary_order = notary_order  # type: list[ListNotaryOrdersResponseBodyDataNotaryOrder]

    def validate(self):
        if self.notary_order:
            for k in self.notary_order:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNotaryOrdersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NotaryOrder'] = []
        if self.notary_order is not None:
            for k in self.notary_order:
                result['NotaryOrder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.notary_order = []
        if m.get('NotaryOrder') is not None:
            for k in m.get('NotaryOrder'):
                temp_model = ListNotaryOrdersResponseBodyDataNotaryOrder()
                self.notary_order.append(temp_model.from_map(k))
        return self


class ListNotaryOrdersResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, error_code=None, error_msg=None, next_page=None,
                 page_size=None, pre_page=None, request_id=None, success=None, total_item_num=None, total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: ListNotaryOrdersResponseBodyData
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.next_page = next_page  # type: bool
        self.page_size = page_size  # type: int
        self.pre_page = pre_page  # type: bool
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListNotaryOrdersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = ListNotaryOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListNotaryOrdersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNotaryOrdersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNotaryOrdersResponse, self).to_map()
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
            temp_model = ListNotaryOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrademarkSbjKeyRequest(TeaModel):
    def __init__(self, principal_key=None, principal_name=None):
        self.principal_key = principal_key  # type: str
        self.principal_name = principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrademarkSbjKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        return self


class ListTrademarkSbjKeyResponseBodyTmSbjKeyInfo(TeaModel):
    def __init__(self, agent_id=None, agree_prot=None, cert_info=None, clear_data=None, hash_data=None,
                 key_type=None, name=None, pin=None, principal_key=None, principal_name=None, sign_cert=None, sign_data=None,
                 start_valid_date=None, submit_sign_data=None, type_cert=None, username=None, valid_date=None, tmurl=None):
        self.agent_id = agent_id  # type: str
        self.agree_prot = agree_prot  # type: str
        self.cert_info = cert_info  # type: str
        self.clear_data = clear_data  # type: str
        self.hash_data = hash_data  # type: str
        self.key_type = key_type  # type: int
        self.name = name  # type: str
        self.pin = pin  # type: str
        self.principal_key = principal_key  # type: str
        self.principal_name = principal_name  # type: str
        self.sign_cert = sign_cert  # type: str
        self.sign_data = sign_data  # type: str
        self.start_valid_date = start_valid_date  # type: str
        self.submit_sign_data = submit_sign_data  # type: str
        self.type_cert = type_cert  # type: str
        self.username = username  # type: str
        self.valid_date = valid_date  # type: str
        self.tmurl = tmurl  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrademarkSbjKeyResponseBodyTmSbjKeyInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agree_prot is not None:
            result['AgreeProt'] = self.agree_prot
        if self.cert_info is not None:
            result['CertInfo'] = self.cert_info
        if self.clear_data is not None:
            result['ClearData'] = self.clear_data
        if self.hash_data is not None:
            result['HashData'] = self.hash_data
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.name is not None:
            result['Name'] = self.name
        if self.pin is not None:
            result['Pin'] = self.pin
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.sign_cert is not None:
            result['SignCert'] = self.sign_cert
        if self.sign_data is not None:
            result['SignData'] = self.sign_data
        if self.start_valid_date is not None:
            result['StartValidDate'] = self.start_valid_date
        if self.submit_sign_data is not None:
            result['SubmitSignData'] = self.submit_sign_data
        if self.type_cert is not None:
            result['TypeCert'] = self.type_cert
        if self.username is not None:
            result['Username'] = self.username
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        if self.tmurl is not None:
            result['tmurl'] = self.tmurl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgreeProt') is not None:
            self.agree_prot = m.get('AgreeProt')
        if m.get('CertInfo') is not None:
            self.cert_info = m.get('CertInfo')
        if m.get('ClearData') is not None:
            self.clear_data = m.get('ClearData')
        if m.get('HashData') is not None:
            self.hash_data = m.get('HashData')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pin') is not None:
            self.pin = m.get('Pin')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('SignCert') is not None:
            self.sign_cert = m.get('SignCert')
        if m.get('SignData') is not None:
            self.sign_data = m.get('SignData')
        if m.get('StartValidDate') is not None:
            self.start_valid_date = m.get('StartValidDate')
        if m.get('SubmitSignData') is not None:
            self.submit_sign_data = m.get('SubmitSignData')
        if m.get('TypeCert') is not None:
            self.type_cert = m.get('TypeCert')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        if m.get('tmurl') is not None:
            self.tmurl = m.get('tmurl')
        return self


class ListTrademarkSbjKeyResponseBody(TeaModel):
    def __init__(self, request_id=None, tm_sbj_key_info=None):
        self.request_id = request_id  # type: str
        self.tm_sbj_key_info = tm_sbj_key_info  # type: list[ListTrademarkSbjKeyResponseBodyTmSbjKeyInfo]

    def validate(self):
        if self.tm_sbj_key_info:
            for k in self.tm_sbj_key_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTrademarkSbjKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TmSbjKeyInfo'] = []
        if self.tm_sbj_key_info is not None:
            for k in self.tm_sbj_key_info:
                result['TmSbjKeyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tm_sbj_key_info = []
        if m.get('TmSbjKeyInfo') is not None:
            for k in m.get('TmSbjKeyInfo'):
                temp_model = ListTrademarkSbjKeyResponseBodyTmSbjKeyInfo()
                self.tm_sbj_key_info.append(temp_model.from_map(k))
        return self


class ListTrademarkSbjKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTrademarkSbjKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTrademarkSbjKeyResponse, self).to_map()
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
            temp_model = ListTrademarkSbjKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySubmitTransferMaterailRequest(TeaModel):
    def __init__(self, addr=None, assignee_proxy=None, biz_id=None, buyer_business_license=None,
                 buyer_business_license_translation=None, buyer_id_card=None, card_no=None, card_type=None, complete=None, contact_email=None,
                 contact_mobile=None, contact_name=None, name=None, notarization=None, note=None, other=None,
                 registration_cert=None, seller_apply=None, seller_business_license=None, seller_business_license_translation=None,
                 seller_id_card=None, seller_proxy=None, trade_material_full_update=None):
        self.addr = addr  # type: str
        self.assignee_proxy = assignee_proxy  # type: str
        self.biz_id = biz_id  # type: str
        self.buyer_business_license = buyer_business_license  # type: str
        self.buyer_business_license_translation = buyer_business_license_translation  # type: str
        self.buyer_id_card = buyer_id_card  # type: str
        self.card_no = card_no  # type: str
        self.card_type = card_type  # type: str
        self.complete = complete  # type: bool
        self.contact_email = contact_email  # type: str
        self.contact_mobile = contact_mobile  # type: str
        self.contact_name = contact_name  # type: str
        self.name = name  # type: str
        self.notarization = notarization  # type: str
        self.note = note  # type: str
        self.other = other  # type: dict[str, any]
        self.registration_cert = registration_cert  # type: str
        self.seller_apply = seller_apply  # type: str
        self.seller_business_license = seller_business_license  # type: str
        self.seller_business_license_translation = seller_business_license_translation  # type: str
        self.seller_id_card = seller_id_card  # type: str
        self.seller_proxy = seller_proxy  # type: str
        self.trade_material_full_update = trade_material_full_update  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySubmitTransferMaterailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addr is not None:
            result['Addr'] = self.addr
        if self.assignee_proxy is not None:
            result['AssigneeProxy'] = self.assignee_proxy
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.buyer_business_license is not None:
            result['BuyerBusinessLicense'] = self.buyer_business_license
        if self.buyer_business_license_translation is not None:
            result['BuyerBusinessLicenseTranslation'] = self.buyer_business_license_translation
        if self.buyer_id_card is not None:
            result['BuyerIdCard'] = self.buyer_id_card
        if self.card_no is not None:
            result['CardNo'] = self.card_no
        if self.card_type is not None:
            result['CardType'] = self.card_type
        if self.complete is not None:
            result['Complete'] = self.complete
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_mobile is not None:
            result['ContactMobile'] = self.contact_mobile
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.name is not None:
            result['Name'] = self.name
        if self.notarization is not None:
            result['Notarization'] = self.notarization
        if self.note is not None:
            result['Note'] = self.note
        if self.other is not None:
            result['Other'] = self.other
        if self.registration_cert is not None:
            result['RegistrationCert'] = self.registration_cert
        if self.seller_apply is not None:
            result['SellerApply'] = self.seller_apply
        if self.seller_business_license is not None:
            result['SellerBusinessLicense'] = self.seller_business_license
        if self.seller_business_license_translation is not None:
            result['SellerBusinessLicenseTranslation'] = self.seller_business_license_translation
        if self.seller_id_card is not None:
            result['SellerIdCard'] = self.seller_id_card
        if self.seller_proxy is not None:
            result['SellerProxy'] = self.seller_proxy
        if self.trade_material_full_update is not None:
            result['TradeMaterialFullUpdate'] = self.trade_material_full_update
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')
        if m.get('AssigneeProxy') is not None:
            self.assignee_proxy = m.get('AssigneeProxy')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BuyerBusinessLicense') is not None:
            self.buyer_business_license = m.get('BuyerBusinessLicense')
        if m.get('BuyerBusinessLicenseTranslation') is not None:
            self.buyer_business_license_translation = m.get('BuyerBusinessLicenseTranslation')
        if m.get('BuyerIdCard') is not None:
            self.buyer_id_card = m.get('BuyerIdCard')
        if m.get('CardNo') is not None:
            self.card_no = m.get('CardNo')
        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')
        if m.get('Complete') is not None:
            self.complete = m.get('Complete')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactMobile') is not None:
            self.contact_mobile = m.get('ContactMobile')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Notarization') is not None:
            self.notarization = m.get('Notarization')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Other') is not None:
            self.other = m.get('Other')
        if m.get('RegistrationCert') is not None:
            self.registration_cert = m.get('RegistrationCert')
        if m.get('SellerApply') is not None:
            self.seller_apply = m.get('SellerApply')
        if m.get('SellerBusinessLicense') is not None:
            self.seller_business_license = m.get('SellerBusinessLicense')
        if m.get('SellerBusinessLicenseTranslation') is not None:
            self.seller_business_license_translation = m.get('SellerBusinessLicenseTranslation')
        if m.get('SellerIdCard') is not None:
            self.seller_id_card = m.get('SellerIdCard')
        if m.get('SellerProxy') is not None:
            self.seller_proxy = m.get('SellerProxy')
        if m.get('TradeMaterialFullUpdate') is not None:
            self.trade_material_full_update = m.get('TradeMaterialFullUpdate')
        return self


class ModifySubmitTransferMaterailShrinkRequest(TeaModel):
    def __init__(self, addr=None, assignee_proxy=None, biz_id=None, buyer_business_license=None,
                 buyer_business_license_translation=None, buyer_id_card=None, card_no=None, card_type=None, complete=None, contact_email=None,
                 contact_mobile=None, contact_name=None, name=None, notarization=None, note=None, other_shrink=None,
                 registration_cert=None, seller_apply=None, seller_business_license=None, seller_business_license_translation=None,
                 seller_id_card=None, seller_proxy=None, trade_material_full_update=None):
        self.addr = addr  # type: str
        self.assignee_proxy = assignee_proxy  # type: str
        self.biz_id = biz_id  # type: str
        self.buyer_business_license = buyer_business_license  # type: str
        self.buyer_business_license_translation = buyer_business_license_translation  # type: str
        self.buyer_id_card = buyer_id_card  # type: str
        self.card_no = card_no  # type: str
        self.card_type = card_type  # type: str
        self.complete = complete  # type: bool
        self.contact_email = contact_email  # type: str
        self.contact_mobile = contact_mobile  # type: str
        self.contact_name = contact_name  # type: str
        self.name = name  # type: str
        self.notarization = notarization  # type: str
        self.note = note  # type: str
        self.other_shrink = other_shrink  # type: str
        self.registration_cert = registration_cert  # type: str
        self.seller_apply = seller_apply  # type: str
        self.seller_business_license = seller_business_license  # type: str
        self.seller_business_license_translation = seller_business_license_translation  # type: str
        self.seller_id_card = seller_id_card  # type: str
        self.seller_proxy = seller_proxy  # type: str
        self.trade_material_full_update = trade_material_full_update  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySubmitTransferMaterailShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addr is not None:
            result['Addr'] = self.addr
        if self.assignee_proxy is not None:
            result['AssigneeProxy'] = self.assignee_proxy
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.buyer_business_license is not None:
            result['BuyerBusinessLicense'] = self.buyer_business_license
        if self.buyer_business_license_translation is not None:
            result['BuyerBusinessLicenseTranslation'] = self.buyer_business_license_translation
        if self.buyer_id_card is not None:
            result['BuyerIdCard'] = self.buyer_id_card
        if self.card_no is not None:
            result['CardNo'] = self.card_no
        if self.card_type is not None:
            result['CardType'] = self.card_type
        if self.complete is not None:
            result['Complete'] = self.complete
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_mobile is not None:
            result['ContactMobile'] = self.contact_mobile
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.name is not None:
            result['Name'] = self.name
        if self.notarization is not None:
            result['Notarization'] = self.notarization
        if self.note is not None:
            result['Note'] = self.note
        if self.other_shrink is not None:
            result['Other'] = self.other_shrink
        if self.registration_cert is not None:
            result['RegistrationCert'] = self.registration_cert
        if self.seller_apply is not None:
            result['SellerApply'] = self.seller_apply
        if self.seller_business_license is not None:
            result['SellerBusinessLicense'] = self.seller_business_license
        if self.seller_business_license_translation is not None:
            result['SellerBusinessLicenseTranslation'] = self.seller_business_license_translation
        if self.seller_id_card is not None:
            result['SellerIdCard'] = self.seller_id_card
        if self.seller_proxy is not None:
            result['SellerProxy'] = self.seller_proxy
        if self.trade_material_full_update is not None:
            result['TradeMaterialFullUpdate'] = self.trade_material_full_update
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')
        if m.get('AssigneeProxy') is not None:
            self.assignee_proxy = m.get('AssigneeProxy')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BuyerBusinessLicense') is not None:
            self.buyer_business_license = m.get('BuyerBusinessLicense')
        if m.get('BuyerBusinessLicenseTranslation') is not None:
            self.buyer_business_license_translation = m.get('BuyerBusinessLicenseTranslation')
        if m.get('BuyerIdCard') is not None:
            self.buyer_id_card = m.get('BuyerIdCard')
        if m.get('CardNo') is not None:
            self.card_no = m.get('CardNo')
        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')
        if m.get('Complete') is not None:
            self.complete = m.get('Complete')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactMobile') is not None:
            self.contact_mobile = m.get('ContactMobile')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Notarization') is not None:
            self.notarization = m.get('Notarization')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Other') is not None:
            self.other_shrink = m.get('Other')
        if m.get('RegistrationCert') is not None:
            self.registration_cert = m.get('RegistrationCert')
        if m.get('SellerApply') is not None:
            self.seller_apply = m.get('SellerApply')
        if m.get('SellerBusinessLicense') is not None:
            self.seller_business_license = m.get('SellerBusinessLicense')
        if m.get('SellerBusinessLicenseTranslation') is not None:
            self.seller_business_license_translation = m.get('SellerBusinessLicenseTranslation')
        if m.get('SellerIdCard') is not None:
            self.seller_id_card = m.get('SellerIdCard')
        if m.get('SellerProxy') is not None:
            self.seller_proxy = m.get('SellerProxy')
        if m.get('TradeMaterialFullUpdate') is not None:
            self.trade_material_full_update = m.get('TradeMaterialFullUpdate')
        return self


class ModifySubmitTransferMaterailResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySubmitTransferMaterailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifySubmitTransferMaterailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySubmitTransferMaterailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySubmitTransferMaterailResponse, self).to_map()
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
            temp_model = ModifySubmitTransferMaterailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateProduceRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, ext_map=None, operate_type=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.ext_map = ext_map  # type: str
        self.operate_type = operate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateProduceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.ext_map is not None:
            result['ExtMap'] = self.ext_map
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtMap') is not None:
            self.ext_map = m.get('ExtMap')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class OperateProduceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateProduceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class OperateProduceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OperateProduceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OperateProduceResponse, self).to_map()
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
            temp_model = OperateProduceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PartnerUpdateTrademarkNameRequest(TeaModel):
    def __init__(self, aliyun_kp=None, bid=None, biz_id=None, caller_parent_id=None, caller_type=None,
                 event_scene_type=None, intention_biz_id=None, tm_comment=None, tm_icon=None, tm_name=None, type=None):
        self.aliyun_kp = aliyun_kp  # type: str
        self.bid = bid  # type: str
        self.biz_id = biz_id  # type: str
        self.caller_parent_id = caller_parent_id  # type: long
        self.caller_type = caller_type  # type: str
        self.event_scene_type = event_scene_type  # type: long
        self.intention_biz_id = intention_biz_id  # type: str
        self.tm_comment = tm_comment  # type: str
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PartnerUpdateTrademarkNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.caller_parent_id is not None:
            result['CallerParentId'] = self.caller_parent_id
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.event_scene_type is not None:
            result['EventSceneType'] = self.event_scene_type
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CallerParentId') is not None:
            self.caller_parent_id = m.get('CallerParentId')
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('EventSceneType') is not None:
            self.event_scene_type = m.get('EventSceneType')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PartnerUpdateTrademarkNameResponseBody(TeaModel):
    def __init__(self, allow_retry=None, app_name=None, dynamic_code=None, dynamic_message=None, error_code=None,
                 error_msg=None, http_status_code=None, request_id=None, success=None):
        self.allow_retry = allow_retry  # type: bool
        self.app_name = app_name  # type: str
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PartnerUpdateTrademarkNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PartnerUpdateTrademarkNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PartnerUpdateTrademarkNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PartnerUpdateTrademarkNameResponse, self).to_map()
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
            temp_model = PartnerUpdateTrademarkNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCommunicationLogsRequest(TeaModel):
    def __init__(self, biz_id=None, page_num=None, page_size=None, type=None):
        self.biz_id = biz_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCommunicationLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryCommunicationLogsResponseBodyDataTaskList(TeaModel):
    def __init__(self, biz_id=None, create_time=None, note=None, partner_code=None, update_time=None):
        self.biz_id = biz_id  # type: str
        self.create_time = create_time  # type: long
        self.note = note  # type: str
        self.partner_code = partner_code  # type: str
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCommunicationLogsResponseBodyDataTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.note is not None:
            result['Note'] = self.note
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryCommunicationLogsResponseBodyData(TeaModel):
    def __init__(self, task_list=None):
        self.task_list = task_list  # type: list[QueryCommunicationLogsResponseBodyDataTaskList]

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryCommunicationLogsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = QueryCommunicationLogsResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class QueryCommunicationLogsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: QueryCommunicationLogsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryCommunicationLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryCommunicationLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryCommunicationLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryCommunicationLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCommunicationLogsResponse, self).to_map()
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
            temp_model = QueryCommunicationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCredentialsInfoRequest(TeaModel):
    def __init__(self, company_name=None, material_type=None, oss_key=None):
        self.company_name = company_name  # type: str
        self.material_type = material_type  # type: str
        self.oss_key = oss_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCredentialsInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        return self


class QueryCredentialsInfoResponseBodyCredentialsInfo(TeaModel):
    def __init__(self, address=None, card_number=None, company_name=None, person_name=None, province=None):
        self.address = address  # type: str
        self.card_number = card_number  # type: str
        self.company_name = company_name  # type: str
        self.person_name = person_name  # type: str
        self.province = province  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCredentialsInfoResponseBodyCredentialsInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.person_name is not None:
            result['PersonName'] = self.person_name
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('PersonName') is not None:
            self.person_name = m.get('PersonName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class QueryCredentialsInfoResponseBody(TeaModel):
    def __init__(self, credentials_info=None, request_id=None):
        self.credentials_info = credentials_info  # type: QueryCredentialsInfoResponseBodyCredentialsInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.credentials_info:
            self.credentials_info.validate()

    def to_map(self):
        _map = super(QueryCredentialsInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credentials_info is not None:
            result['CredentialsInfo'] = self.credentials_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialsInfo') is not None:
            temp_model = QueryCredentialsInfoResponseBodyCredentialsInfo()
            self.credentials_info = temp_model.from_map(m['CredentialsInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryCredentialsInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryCredentialsInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCredentialsInfoResponse, self).to_map()
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
            temp_model = QueryCredentialsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryExtensionAttributeRequest(TeaModel):
    def __init__(self, attribute_key=None, biz_id=None):
        self.attribute_key = attribute_key  # type: str
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryExtensionAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryExtensionAttributeResponseBody(TeaModel):
    def __init__(self, attribute_value=None, code=None, message=None, request_id=None, success=None):
        self.attribute_value = attribute_value  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryExtensionAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryExtensionAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryExtensionAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryExtensionAttributeResponse, self).to_map()
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
            temp_model = QueryExtensionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentionDetailRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryIntentionDetailResponseBody(TeaModel):
    def __init__(self, biz_id=None, classification=None, create_time=None, description=None, mobile=None,
                 partner_mobile=None, register_number=None, relation_biz_id=None, request_id=None, status=None, type=None,
                 update_time=None, user_id=None, user_name=None):
        self.biz_id = biz_id  # type: str
        self.classification = classification  # type: str
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.mobile = mobile  # type: str
        self.partner_mobile = partner_mobile  # type: str
        self.register_number = register_number  # type: str
        self.relation_biz_id = relation_biz_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: int
        self.type = type  # type: int
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.partner_mobile is not None:
            result['PartnerMobile'] = self.partner_mobile
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.relation_biz_id is not None:
            result['RelationBizId'] = self.relation_biz_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PartnerMobile') is not None:
            self.partner_mobile = m.get('PartnerMobile')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('RelationBizId') is not None:
            self.relation_biz_id = m.get('RelationBizId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryIntentionDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryIntentionDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryIntentionDetailResponse, self).to_map()
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
            temp_model = QueryIntentionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentionListRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, sort_filed=None, sort_order=None, status=None, type=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.sort_filed = sort_filed  # type: str
        self.sort_order = sort_order  # type: str
        self.status = status  # type: int
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryIntentionListResponseBodyDataIntention(TeaModel):
    def __init__(self, biz_id=None, classification=None, create_time=None, description=None, register_number=None,
                 status=None, type=None, update_time=None, user_id=None):
        self.biz_id = biz_id  # type: str
        self.classification = classification  # type: str
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.register_number = register_number  # type: str
        self.status = status  # type: int
        self.type = type  # type: int
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionListResponseBodyDataIntention, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryIntentionListResponseBodyData(TeaModel):
    def __init__(self, intention=None):
        self.intention = intention  # type: list[QueryIntentionListResponseBodyDataIntention]

    def validate(self):
        if self.intention:
            for k in self.intention:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryIntentionListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Intention'] = []
        if self.intention is not None:
            for k in self.intention:
                result['Intention'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.intention = []
        if m.get('Intention') is not None:
            for k in m.get('Intention'):
                temp_model = QueryIntentionListResponseBodyDataIntention()
                self.intention.append(temp_model.from_map(k))
        return self


class QueryIntentionListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryIntentionListResponseBodyData
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryIntentionListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryIntentionListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryIntentionListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryIntentionListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryIntentionListResponse, self).to_map()
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
            temp_model = QueryIntentionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentionOwnerRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionOwnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryIntentionOwnerResponseBodyModule(TeaModel):
    def __init__(self, owner_id=None, owner_name=None):
        self.owner_id = owner_id  # type: float
        self.owner_name = owner_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionOwnerResponseBodyModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        return self


class QueryIntentionOwnerResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, module=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.module = module  # type: QueryIntentionOwnerResponseBodyModule
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super(QueryIntentionOwnerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Module') is not None:
            temp_model = QueryIntentionOwnerResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryIntentionOwnerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryIntentionOwnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryIntentionOwnerResponse, self).to_map()
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
            temp_model = QueryIntentionOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentionPriceRequest(TeaModel):
    def __init__(self, channel=None, intention_biz_id=None):
        self.channel = channel  # type: str
        self.intention_biz_id = intention_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        return self


class QueryIntentionPriceResponseBodyDataTmProducesFirstClassification(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionPriceResponseBodyDataTmProducesFirstClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryIntentionPriceResponseBodyDataTmProducesThirdClassificationThirdClassifications(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryIntentionPriceResponseBodyDataTmProducesThirdClassificationThirdClassifications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryIntentionPriceResponseBodyDataTmProducesThirdClassification(TeaModel):
    def __init__(self, third_classifications=None):
        self.third_classifications = third_classifications  # type: list[QueryIntentionPriceResponseBodyDataTmProducesThirdClassificationThirdClassifications]

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryIntentionPriceResponseBodyDataTmProducesThirdClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryIntentionPriceResponseBodyDataTmProducesThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryIntentionPriceResponseBodyDataTmProduces(TeaModel):
    def __init__(self, biz_id=None, create_time=None, first_classification=None, loa_url=None, material_id=None,
                 material_name=None, note=None, order_price=None, service_price=None, status=None, supplement_id=None,
                 supplement_status=None, third_classification=None, tm_icon=None, tm_name=None, tm_number=None, total_price=None,
                 type=None, update_time=None):
        self.biz_id = biz_id  # type: str
        self.create_time = create_time  # type: long
        self.first_classification = first_classification  # type: QueryIntentionPriceResponseBodyDataTmProducesFirstClassification
        self.loa_url = loa_url  # type: str
        self.material_id = material_id  # type: str
        self.material_name = material_name  # type: str
        self.note = note  # type: str
        self.order_price = order_price  # type: float
        self.service_price = service_price  # type: float
        self.status = status  # type: int
        self.supplement_id = supplement_id  # type: long
        self.supplement_status = supplement_status  # type: int
        self.third_classification = third_classification  # type: QueryIntentionPriceResponseBodyDataTmProducesThirdClassification
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_number = tm_number  # type: str
        self.total_price = total_price  # type: float
        self.type = type  # type: int
        self.update_time = update_time  # type: long

    def validate(self):
        if self.first_classification:
            self.first_classification.validate()
        if self.third_classification:
            self.third_classification.validate()

    def to_map(self):
        _map = super(QueryIntentionPriceResponseBodyDataTmProduces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.note is not None:
            result['Note'] = self.note
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.status is not None:
            result['Status'] = self.status
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FirstClassification') is not None:
            temp_model = QueryIntentionPriceResponseBodyDataTmProducesFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('ThirdClassification') is not None:
            temp_model = QueryIntentionPriceResponseBodyDataTmProducesThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryIntentionPriceResponseBodyData(TeaModel):
    def __init__(self, tm_produces=None):
        self.tm_produces = tm_produces  # type: list[QueryIntentionPriceResponseBodyDataTmProduces]

    def validate(self):
        if self.tm_produces:
            for k in self.tm_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryIntentionPriceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmProduces'] = []
        if self.tm_produces is not None:
            for k in self.tm_produces:
                result['TmProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tm_produces = []
        if m.get('TmProduces') is not None:
            for k in m.get('TmProduces'):
                temp_model = QueryIntentionPriceResponseBodyDataTmProduces()
                self.tm_produces.append(temp_model.from_map(k))
        return self


class QueryIntentionPriceResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryIntentionPriceResponseBodyData
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryIntentionPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryIntentionPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryIntentionPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryIntentionPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryIntentionPriceResponse, self).to_map()
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
            temp_model = QueryIntentionPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMaterialRequest(TeaModel):
    def __init__(self, id=None, query_unconfirmed_info=None):
        self.id = id  # type: long
        self.query_unconfirmed_info = query_unconfirmed_info  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.query_unconfirmed_info is not None:
            result['QueryUnconfirmedInfo'] = self.query_unconfirmed_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('QueryUnconfirmedInfo') is not None:
            self.query_unconfirmed_info = m.get('QueryUnconfirmedInfo')
        return self


class QueryMaterialResponseBodyReviewAdditionalFiles(TeaModel):
    def __init__(self, review_additional_file=None):
        self.review_additional_file = review_additional_file  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMaterialResponseBodyReviewAdditionalFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_additional_file is not None:
            result['ReviewAdditionalFile'] = self.review_additional_file
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReviewAdditionalFile') is not None:
            self.review_additional_file = m.get('ReviewAdditionalFile')
        return self


class QueryMaterialResponseBody(TeaModel):
    def __init__(self, address=None, business_licence_url=None, card_number=None, city=None, contact_address=None,
                 contact_city=None, contact_county=None, contact_district=None, contact_email=None, contact_name=None,
                 contact_number=None, contact_province=None, contact_zipcode=None, country=None, eaddress=None, ename=None,
                 evidence_catalog_path=None, evidence_ofservice_path=None, evidence_path=None, expiration_date=None,
                 factandreason_pdf_path=None, fgsq_path=None, file_bg_path=None, file_fs_sq_path=None, file_gt_path=None,
                 file_yg_path=None, id=None, id_card_name=None, id_card_number=None, id_card_url=None, legal_notice_key=None,
                 legal_notice_url=None, loa_status=None, loa_url=None, material_version=None, name=None, note=None, passport_url=None,
                 personal_type=None, principal_description=None, principal_name=None, province=None, reason=None, region=None,
                 request_id=None, review_additional_files=None, review_application_file=None, status=None,
                 supplement_evidence_catalog_file=None, supplement_evidence_material_file=None, supplement_reason_file=None, system_version=None,
                 town=None, type=None, valid_date=None):
        self.address = address  # type: str
        self.business_licence_url = business_licence_url  # type: str
        self.card_number = card_number  # type: str
        self.city = city  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_city = contact_city  # type: str
        self.contact_county = contact_county  # type: str
        self.contact_district = contact_district  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_province = contact_province  # type: str
        self.contact_zipcode = contact_zipcode  # type: str
        self.country = country  # type: str
        self.eaddress = eaddress  # type: str
        self.ename = ename  # type: str
        self.evidence_catalog_path = evidence_catalog_path  # type: str
        self.evidence_ofservice_path = evidence_ofservice_path  # type: str
        self.evidence_path = evidence_path  # type: str
        self.expiration_date = expiration_date  # type: long
        self.factandreason_pdf_path = factandreason_pdf_path  # type: str
        self.fgsq_path = fgsq_path  # type: str
        self.file_bg_path = file_bg_path  # type: str
        self.file_fs_sq_path = file_fs_sq_path  # type: str
        self.file_gt_path = file_gt_path  # type: str
        self.file_yg_path = file_yg_path  # type: str
        # id
        self.id = id  # type: long
        self.id_card_name = id_card_name  # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_url = id_card_url  # type: str
        self.legal_notice_key = legal_notice_key  # type: str
        self.legal_notice_url = legal_notice_url  # type: str
        self.loa_status = loa_status  # type: int
        self.loa_url = loa_url  # type: str
        self.material_version = material_version  # type: str
        self.name = name  # type: str
        self.note = note  # type: str
        self.passport_url = passport_url  # type: str
        self.personal_type = personal_type  # type: long
        self.principal_description = principal_description  # type: str
        self.principal_name = principal_name  # type: int
        self.province = province  # type: str
        self.reason = reason  # type: str
        self.region = region  # type: int
        self.request_id = request_id  # type: str
        self.review_additional_files = review_additional_files  # type: QueryMaterialResponseBodyReviewAdditionalFiles
        self.review_application_file = review_application_file  # type: str
        self.status = status  # type: int
        self.supplement_evidence_catalog_file = supplement_evidence_catalog_file  # type: str
        self.supplement_evidence_material_file = supplement_evidence_material_file  # type: str
        self.supplement_reason_file = supplement_reason_file  # type: str
        self.system_version = system_version  # type: str
        self.town = town  # type: str
        self.type = type  # type: int
        self.valid_date = valid_date  # type: long

    def validate(self):
        if self.review_additional_files:
            self.review_additional_files.validate()

    def to_map(self):
        _map = super(QueryMaterialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.evidence_catalog_path is not None:
            result['EvidenceCatalogPath'] = self.evidence_catalog_path
        if self.evidence_ofservice_path is not None:
            result['EvidenceOfservicePath'] = self.evidence_ofservice_path
        if self.evidence_path is not None:
            result['EvidencePath'] = self.evidence_path
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.factandreason_pdf_path is not None:
            result['FactandreasonPdfPath'] = self.factandreason_pdf_path
        if self.fgsq_path is not None:
            result['FgsqPath'] = self.fgsq_path
        if self.file_bg_path is not None:
            result['FileBgPath'] = self.file_bg_path
        if self.file_fs_sq_path is not None:
            result['FileFsSqPath'] = self.file_fs_sq_path
        if self.file_gt_path is not None:
            result['FileGtPath'] = self.file_gt_path
        if self.file_yg_path is not None:
            result['FileYgPath'] = self.file_yg_path
        if self.id is not None:
            result['Id'] = self.id
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.legal_notice_key is not None:
            result['LegalNoticeKey'] = self.legal_notice_key
        if self.legal_notice_url is not None:
            result['LegalNoticeUrl'] = self.legal_notice_url
        if self.loa_status is not None:
            result['LoaStatus'] = self.loa_status
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_version is not None:
            result['MaterialVersion'] = self.material_version
        if self.name is not None:
            result['Name'] = self.name
        if self.note is not None:
            result['Note'] = self.note
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.province is not None:
            result['Province'] = self.province
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.review_additional_files is not None:
            result['ReviewAdditionalFiles'] = self.review_additional_files.to_map()
        if self.review_application_file is not None:
            result['ReviewApplicationFile'] = self.review_application_file
        if self.status is not None:
            result['Status'] = self.status
        if self.supplement_evidence_catalog_file is not None:
            result['SupplementEvidenceCatalogFile'] = self.supplement_evidence_catalog_file
        if self.supplement_evidence_material_file is not None:
            result['SupplementEvidenceMaterialFile'] = self.supplement_evidence_material_file
        if self.supplement_reason_file is not None:
            result['SupplementReasonFile'] = self.supplement_reason_file
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.town is not None:
            result['Town'] = self.town
        if self.type is not None:
            result['Type'] = self.type
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('EvidenceCatalogPath') is not None:
            self.evidence_catalog_path = m.get('EvidenceCatalogPath')
        if m.get('EvidenceOfservicePath') is not None:
            self.evidence_ofservice_path = m.get('EvidenceOfservicePath')
        if m.get('EvidencePath') is not None:
            self.evidence_path = m.get('EvidencePath')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('FactandreasonPdfPath') is not None:
            self.factandreason_pdf_path = m.get('FactandreasonPdfPath')
        if m.get('FgsqPath') is not None:
            self.fgsq_path = m.get('FgsqPath')
        if m.get('FileBgPath') is not None:
            self.file_bg_path = m.get('FileBgPath')
        if m.get('FileFsSqPath') is not None:
            self.file_fs_sq_path = m.get('FileFsSqPath')
        if m.get('FileGtPath') is not None:
            self.file_gt_path = m.get('FileGtPath')
        if m.get('FileYgPath') is not None:
            self.file_yg_path = m.get('FileYgPath')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LegalNoticeKey') is not None:
            self.legal_notice_key = m.get('LegalNoticeKey')
        if m.get('LegalNoticeUrl') is not None:
            self.legal_notice_url = m.get('LegalNoticeUrl')
        if m.get('LoaStatus') is not None:
            self.loa_status = m.get('LoaStatus')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialVersion') is not None:
            self.material_version = m.get('MaterialVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReviewAdditionalFiles') is not None:
            temp_model = QueryMaterialResponseBodyReviewAdditionalFiles()
            self.review_additional_files = temp_model.from_map(m['ReviewAdditionalFiles'])
        if m.get('ReviewApplicationFile') is not None:
            self.review_application_file = m.get('ReviewApplicationFile')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplementEvidenceCatalogFile') is not None:
            self.supplement_evidence_catalog_file = m.get('SupplementEvidenceCatalogFile')
        if m.get('SupplementEvidenceMaterialFile') is not None:
            self.supplement_evidence_material_file = m.get('SupplementEvidenceMaterialFile')
        if m.get('SupplementReasonFile') is not None:
            self.supplement_reason_file = m.get('SupplementReasonFile')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        return self


class QueryMaterialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMaterialResponse, self).to_map()
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
            temp_model = QueryMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMaterialListRequest(TeaModel):
    def __init__(self, card_number=None, material_id=None, material_version=None, name=None, page_num=None,
                 page_size=None, principal_name=None, region=None, status=None, system_version=None, type=None):
        self.card_number = card_number  # type: str
        self.material_id = material_id  # type: long
        self.material_version = material_version  # type: str
        self.name = name  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.principal_name = principal_name  # type: int
        self.region = region  # type: int
        self.status = status  # type: int
        self.system_version = system_version  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMaterialListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_version is not None:
            result['MaterialVersion'] = self.material_version
        if self.name is not None:
            result['Name'] = self.name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialVersion') is not None:
            self.material_version = m.get('MaterialVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryMaterialListResponseBodyDataTrademark(TeaModel):
    def __init__(self, card_number=None, contact_name=None, id=None, loa_key=None, loa_status=None,
                 material_version=None, name=None, principal_description=None, principal_name=None, reason=None, region=None,
                 status=None, system_version=None, type=None, valid_date=None):
        self.card_number = card_number  # type: str
        self.contact_name = contact_name  # type: str
        self.id = id  # type: long
        self.loa_key = loa_key  # type: str
        self.loa_status = loa_status  # type: int
        self.material_version = material_version  # type: str
        self.name = name  # type: str
        self.principal_description = principal_description  # type: str
        self.principal_name = principal_name  # type: int
        self.reason = reason  # type: str
        self.region = region  # type: int
        self.status = status  # type: int
        self.system_version = system_version  # type: str
        self.type = type  # type: int
        self.valid_date = valid_date  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMaterialListResponseBodyDataTrademark, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.id is not None:
            result['Id'] = self.id
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.loa_status is not None:
            result['LoaStatus'] = self.loa_status
        if self.material_version is not None:
            result['MaterialVersion'] = self.material_version
        if self.name is not None:
            result['Name'] = self.name
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.type is not None:
            result['Type'] = self.type
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('LoaStatus') is not None:
            self.loa_status = m.get('LoaStatus')
        if m.get('MaterialVersion') is not None:
            self.material_version = m.get('MaterialVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        return self


class QueryMaterialListResponseBodyData(TeaModel):
    def __init__(self, trademark=None):
        self.trademark = trademark  # type: list[QueryMaterialListResponseBodyDataTrademark]

    def validate(self):
        if self.trademark:
            for k in self.trademark:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMaterialListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Trademark'] = []
        if self.trademark is not None:
            for k in self.trademark:
                result['Trademark'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.trademark = []
        if m.get('Trademark') is not None:
            for k in m.get('Trademark'):
                temp_model = QueryMaterialListResponseBodyDataTrademark()
                self.trademark.append(temp_model.from_map(k))
        return self


class QueryMaterialListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryMaterialListResponseBodyData
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryMaterialListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryMaterialListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryMaterialListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMaterialListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMaterialListResponse, self).to_map()
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
            temp_model = QueryMaterialListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonitorKeywordsRequest(TeaModel):
    def __init__(self, keywords=None, rule_type=None):
        self.keywords = keywords  # type: list[str]
        self.rule_type = rule_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMonitorKeywordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class QueryMonitorKeywordsResponseBodyData(TeaModel):
    def __init__(self, keywords=None):
        self.keywords = keywords  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMonitorKeywordsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        return self


class QueryMonitorKeywordsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: QueryMonitorKeywordsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryMonitorKeywordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryMonitorKeywordsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryMonitorKeywordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMonitorKeywordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMonitorKeywordsResponse, self).to_map()
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
            temp_model = QueryMonitorKeywordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOfficialFileCustomListRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOfficialFileCustomListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryOfficialFileCustomListResponseBodyDataCustomList(TeaModel):
    def __init__(self, create_time=None, download_url=None, end_accept_time=None, expire_time=None, remark=None,
                 start_accept_time=None, status=None):
        self.create_time = create_time  # type: long
        self.download_url = download_url  # type: str
        self.end_accept_time = end_accept_time  # type: long
        self.expire_time = expire_time  # type: long
        self.remark = remark  # type: str
        self.start_accept_time = start_accept_time  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOfficialFileCustomListResponseBodyDataCustomList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.end_accept_time is not None:
            result['EndAcceptTime'] = self.end_accept_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.start_accept_time is not None:
            result['StartAcceptTime'] = self.start_accept_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('EndAcceptTime') is not None:
            self.end_accept_time = m.get('EndAcceptTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('StartAcceptTime') is not None:
            self.start_accept_time = m.get('StartAcceptTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryOfficialFileCustomListResponseBodyData(TeaModel):
    def __init__(self, custom_list=None):
        self.custom_list = custom_list  # type: list[QueryOfficialFileCustomListResponseBodyDataCustomList]

    def validate(self):
        if self.custom_list:
            for k in self.custom_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryOfficialFileCustomListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomList'] = []
        if self.custom_list is not None:
            for k in self.custom_list:
                result['CustomList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_list = []
        if m.get('CustomList') is not None:
            for k in m.get('CustomList'):
                temp_model = QueryOfficialFileCustomListResponseBodyDataCustomList()
                self.custom_list.append(temp_model.from_map(k))
        return self


class QueryOfficialFileCustomListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryOfficialFileCustomListResponseBodyData
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryOfficialFileCustomListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryOfficialFileCustomListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryOfficialFileCustomListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryOfficialFileCustomListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOfficialFileCustomListResponse, self).to_map()
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
            temp_model = QueryOfficialFileCustomListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderLogisticsListRequest(TeaModel):
    def __init__(self, file_type=None, page_num=None, page_size=None, produce_order_id=None, register_number=None):
        self.file_type = file_type  # type: str
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.produce_order_id = produce_order_id  # type: str
        self.register_number = register_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrderLogisticsListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.produce_order_id is not None:
            result['ProduceOrderId'] = self.produce_order_id
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProduceOrderId') is not None:
            self.produce_order_id = m.get('ProduceOrderId')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        return self


class QueryOrderLogisticsListResponseBodyData(TeaModel):
    def __init__(self, biz_id=None, file_identifier=None, file_type=None, logistics_no=None, produce_order_id=None,
                 tm_icon=None, tm_name=None, tm_number=None):
        self.biz_id = biz_id  # type: str
        self.file_identifier = file_identifier  # type: str
        self.file_type = file_type  # type: str
        self.logistics_no = logistics_no  # type: str
        self.produce_order_id = produce_order_id  # type: str
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_number = tm_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOrderLogisticsListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.file_identifier is not None:
            result['FileIdentifier'] = self.file_identifier
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.produce_order_id is not None:
            result['ProduceOrderId'] = self.produce_order_id
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('FileIdentifier') is not None:
            self.file_identifier = m.get('FileIdentifier')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('ProduceOrderId') is not None:
            self.produce_order_id = m.get('ProduceOrderId')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        return self


class QueryOrderLogisticsListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: list[QueryOrderLogisticsListResponseBodyData]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryOrderLogisticsListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryOrderLogisticsListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryOrderLogisticsListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryOrderLogisticsListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOrderLogisticsListResponse, self).to_map()
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
            temp_model = QueryOrderLogisticsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOssResourcesRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOssResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryOssResourcesResponseBodyDataTaskList(TeaModel):
    def __init__(self, biz_id=None, create_time=None, name=None, oss_url=None, update_time=None):
        self.biz_id = biz_id  # type: str
        self.create_time = create_time  # type: long
        self.name = name  # type: str
        self.oss_url = oss_url  # type: str
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOssResourcesResponseBodyDataTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryOssResourcesResponseBodyData(TeaModel):
    def __init__(self, task_list=None):
        self.task_list = task_list  # type: list[QueryOssResourcesResponseBodyDataTaskList]

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryOssResourcesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = QueryOssResourcesResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class QueryOssResourcesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: QueryOssResourcesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryOssResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryOssResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryOssResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryOssResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOssResourcesResponse, self).to_map()
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
            temp_model = QueryOssResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProduceDetailRequest(TeaModel):
    def __init__(self, apply_no=None, biz_id=None, order_id=None):
        self.apply_no = apply_no  # type: str
        self.biz_id = biz_id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryProduceDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_no is not None:
            result['ApplyNo'] = self.apply_no
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyNo') is not None:
            self.apply_no = m.get('ApplyNo')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class QueryProduceDetailResponseBodyFlags(TeaModel):
    def __init__(self, flags=None):
        self.flags = flags  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryProduceDetailResponseBodyFlags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flags is not None:
            result['Flags'] = self.flags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flags') is not None:
            self.flags = m.get('Flags')
        return self


class QueryProduceDetailResponseBodyLeafCodesLeafCodes(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryProduceDetailResponseBodyLeafCodesLeafCodes, self).to_map()
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


class QueryProduceDetailResponseBodyLeafCodes(TeaModel):
    def __init__(self, leaf_codes=None):
        self.leaf_codes = leaf_codes  # type: list[QueryProduceDetailResponseBodyLeafCodesLeafCodes]

    def validate(self):
        if self.leaf_codes:
            for k in self.leaf_codes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryProduceDetailResponseBodyLeafCodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LeafCodes'] = []
        if self.leaf_codes is not None:
            for k in self.leaf_codes:
                result['LeafCodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.leaf_codes = []
        if m.get('LeafCodes') is not None:
            for k in m.get('LeafCodes'):
                temp_model = QueryProduceDetailResponseBodyLeafCodesLeafCodes()
                self.leaf_codes.append(temp_model.from_map(k))
        return self


class QueryProduceDetailResponseBodyMaterialDetail(TeaModel):
    def __init__(self, address=None, business_licence_url=None, card_number=None, city=None, contact_address=None,
                 contact_email=None, contact_name=None, contact_number=None, contact_zipcode=None, country=None, eaddress=None,
                 ename=None, expiration_date=None, id_card_url=None, loa_url=None, name=None, passport_url=None,
                 province=None, region=None, status=None, town=None, type=None):
        self.address = address  # type: str
        self.business_licence_url = business_licence_url  # type: str
        self.card_number = card_number  # type: str
        self.city = city  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_zipcode = contact_zipcode  # type: str
        self.country = country  # type: str
        self.eaddress = eaddress  # type: str
        self.ename = ename  # type: str
        self.expiration_date = expiration_date  # type: str
        self.id_card_url = id_card_url  # type: str
        self.loa_url = loa_url  # type: str
        self.name = name  # type: str
        self.passport_url = passport_url  # type: str
        self.province = province  # type: str
        self.region = region  # type: int
        self.status = status  # type: int
        self.town = town  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryProduceDetailResponseBodyMaterialDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.town is not None:
            result['Town'] = self.town
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryProduceDetailResponseBodyRootCode(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryProduceDetailResponseBodyRootCode, self).to_map()
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


class QueryProduceDetailResponseBody(TeaModel):
    def __init__(self, accept_url=None, agreement_id=None, biz_id=None, cn_info_url=None, extend_info=None,
                 flags=None, gray_icon_url=None, issue_date=None, leaf_codes=None, loa_url=None, material_detail=None,
                 note=None, order_id=None, principal_name=None, request_id=None, root_code=None, status=None,
                 submit_count=None, tm_icon=None, tm_name=None, tm_name_type=None, tm_number=None, tm_order_id=None, type=None):
        self.accept_url = accept_url  # type: str
        self.agreement_id = agreement_id  # type: str
        self.biz_id = biz_id  # type: str
        self.cn_info_url = cn_info_url  # type: str
        self.extend_info = extend_info  # type: dict[str, any]
        self.flags = flags  # type: QueryProduceDetailResponseBodyFlags
        self.gray_icon_url = gray_icon_url  # type: str
        self.issue_date = issue_date  # type: str
        self.leaf_codes = leaf_codes  # type: QueryProduceDetailResponseBodyLeafCodes
        self.loa_url = loa_url  # type: str
        self.material_detail = material_detail  # type: QueryProduceDetailResponseBodyMaterialDetail
        self.note = note  # type: str
        self.order_id = order_id  # type: str
        self.principal_name = principal_name  # type: int
        self.request_id = request_id  # type: str
        self.root_code = root_code  # type: QueryProduceDetailResponseBodyRootCode
        self.status = status  # type: int
        self.submit_count = submit_count  # type: int
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_name_type = tm_name_type  # type: int
        self.tm_number = tm_number  # type: str
        self.tm_order_id = tm_order_id  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.flags:
            self.flags.validate()
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_detail:
            self.material_detail.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super(QueryProduceDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_url is not None:
            result['AcceptUrl'] = self.accept_url
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.flags is not None:
            result['Flags'] = self.flags.to_map()
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.issue_date is not None:
            result['IssueDate'] = self.issue_date
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_detail is not None:
            result['MaterialDetail'] = self.material_detail.to_map()
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_count is not None:
            result['SubmitCount'] = self.submit_count
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.tm_order_id is not None:
            result['TmOrderId'] = self.tm_order_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptUrl') is not None:
            self.accept_url = m.get('AcceptUrl')
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Flags') is not None:
            temp_model = QueryProduceDetailResponseBodyFlags()
            self.flags = temp_model.from_map(m['Flags'])
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('IssueDate') is not None:
            self.issue_date = m.get('IssueDate')
        if m.get('LeafCodes') is not None:
            temp_model = QueryProduceDetailResponseBodyLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialDetail') is not None:
            temp_model = QueryProduceDetailResponseBodyMaterialDetail()
            self.material_detail = temp_model.from_map(m['MaterialDetail'])
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootCode') is not None:
            temp_model = QueryProduceDetailResponseBodyRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitCount') is not None:
            self.submit_count = m.get('SubmitCount')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TmOrderId') is not None:
            self.tm_order_id = m.get('TmOrderId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryProduceDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryProduceDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryProduceDetailResponse, self).to_map()
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
            temp_model = QueryProduceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProduceListRequest(TeaModel):
    def __init__(self, biz_id=None, create_time_left=None, create_time_right=None, material_name=None,
                 order_id=None, page_num=None, page_size=None, status=None, tm_name=None, tm_number=None, type=None,
                 user_id=None):
        self.biz_id = biz_id  # type: str
        self.create_time_left = create_time_left  # type: long
        self.create_time_right = create_time_right  # type: long
        self.material_name = material_name  # type: str
        self.order_id = order_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: int
        self.tm_name = tm_name  # type: str
        self.tm_number = tm_number  # type: str
        self.type = type  # type: int
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryProduceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time_left is not None:
            result['CreateTimeLeft'] = self.create_time_left
        if self.create_time_right is not None:
            result['CreateTimeRight'] = self.create_time_right
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTimeLeft') is not None:
            self.create_time_left = m.get('CreateTimeLeft')
        if m.get('CreateTimeRight') is not None:
            self.create_time_right = m.get('CreateTimeRight')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryProduceListResponseBodyDataTmProducesClassification(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryProduceListResponseBodyDataTmProducesClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryProduceListResponseBodyDataTmProduces(TeaModel):
    def __init__(self, agreement_id=None, biz_id=None, classification=None, create_time=None, loa_url=None,
                 material_name=None, note=None, order_id=None, order_price=None, principal_name=None, receipt_url=None,
                 status=None, submit_count=None, tm_icon=None, tm_name=None, tm_number=None, type=None, update_time=None,
                 user_id=None):
        self.agreement_id = agreement_id  # type: str
        self.biz_id = biz_id  # type: str
        self.classification = classification  # type: QueryProduceListResponseBodyDataTmProducesClassification
        self.create_time = create_time  # type: long
        self.loa_url = loa_url  # type: str
        self.material_name = material_name  # type: str
        self.note = note  # type: str
        self.order_id = order_id  # type: str
        self.order_price = order_price  # type: float
        self.principal_name = principal_name  # type: int
        self.receipt_url = receipt_url  # type: str
        self.status = status  # type: int
        self.submit_count = submit_count  # type: int
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_number = tm_number  # type: str
        self.type = type  # type: int
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        if self.classification:
            self.classification.validate()

    def to_map(self):
        _map = super(QueryProduceListResponseBodyDataTmProduces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification is not None:
            result['Classification'] = self.classification.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_count is not None:
            result['SubmitCount'] = self.submit_count
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Classification') is not None:
            temp_model = QueryProduceListResponseBodyDataTmProducesClassification()
            self.classification = temp_model.from_map(m['Classification'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitCount') is not None:
            self.submit_count = m.get('SubmitCount')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryProduceListResponseBodyData(TeaModel):
    def __init__(self, tm_produces=None):
        self.tm_produces = tm_produces  # type: list[QueryProduceListResponseBodyDataTmProduces]

    def validate(self):
        if self.tm_produces:
            for k in self.tm_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryProduceListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmProduces'] = []
        if self.tm_produces is not None:
            for k in self.tm_produces:
                result['TmProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tm_produces = []
        if m.get('TmProduces') is not None:
            for k in m.get('TmProduces'):
                temp_model = QueryProduceListResponseBodyDataTmProduces()
                self.tm_produces.append(temp_model.from_map(k))
        return self


class QueryProduceListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, next_page=None, page_size=None, pre_page=None,
                 request_id=None, total_item_num=None, total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryProduceListResponseBodyData
        self.next_page = next_page  # type: bool
        self.page_size = page_size  # type: int
        self.pre_page = pre_page  # type: bool
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryProduceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryProduceListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryProduceListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryProduceListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryProduceListResponse, self).to_map()
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
            temp_model = QueryProduceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryQrCodeUploadStatusRequest(TeaModel):
    def __init__(self, field_key=None, oss_key=None, uuid=None):
        self.field_key = field_key  # type: str
        self.oss_key = oss_key  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryQrCodeUploadStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryQrCodeUploadStatusResponseBody(TeaModel):
    def __init__(self, oss_key=None, oss_url=None, request_id=None, status=None, success=None):
        self.oss_key = oss_key  # type: str
        self.oss_url = oss_url  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: int
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryQrCodeUploadStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryQrCodeUploadStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryQrCodeUploadStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryQrCodeUploadStatusResponse, self).to_map()
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
            temp_model = QueryQrCodeUploadStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySbjRuleRequest(TeaModel):
    def __init__(self, biz_type=None, rule_id=None):
        self.biz_type = biz_type  # type: str
        self.rule_id = rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySbjRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class QuerySbjRuleResponseBodySbjRuleListSbjRuleItemFrontendOptionsFrontendOption(TeaModel):
    def __init__(self, title=None, value=None):
        self.title = title  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySbjRuleResponseBodySbjRuleListSbjRuleItemFrontendOptionsFrontendOption, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['title'] = self.title
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class QuerySbjRuleResponseBodySbjRuleListSbjRuleItemFrontendOptions(TeaModel):
    def __init__(self, frontend_option=None):
        self.frontend_option = frontend_option  # type: list[QuerySbjRuleResponseBodySbjRuleListSbjRuleItemFrontendOptionsFrontendOption]

    def validate(self):
        if self.frontend_option:
            for k in self.frontend_option:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySbjRuleResponseBodySbjRuleListSbjRuleItemFrontendOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FrontendOption'] = []
        if self.frontend_option is not None:
            for k in self.frontend_option:
                result['FrontendOption'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.frontend_option = []
        if m.get('FrontendOption') is not None:
            for k in m.get('FrontendOption'):
                temp_model = QuerySbjRuleResponseBodySbjRuleListSbjRuleItemFrontendOptionsFrontendOption()
                self.frontend_option.append(temp_model.from_map(k))
        return self


class QuerySbjRuleResponseBodySbjRuleListSbjRuleItem(TeaModel):
    def __init__(self, default_value=None, esp_ext_field_name=None, field_name=None, file_type=None,
                 frontend_options=None, frontend_type=None, required_expression=None, sbj_field_id=None, show_expression=None,
                 trademark_service_expression=None, validate_regular_expression=None):
        self.default_value = default_value  # type: str
        self.esp_ext_field_name = esp_ext_field_name  # type: str
        self.field_name = field_name  # type: str
        self.file_type = file_type  # type: str
        self.frontend_options = frontend_options  # type: QuerySbjRuleResponseBodySbjRuleListSbjRuleItemFrontendOptions
        self.frontend_type = frontend_type  # type: str
        self.required_expression = required_expression  # type: str
        self.sbj_field_id = sbj_field_id  # type: str
        self.show_expression = show_expression  # type: str
        self.trademark_service_expression = trademark_service_expression  # type: str
        self.validate_regular_expression = validate_regular_expression  # type: str

    def validate(self):
        if self.frontend_options:
            self.frontend_options.validate()

    def to_map(self):
        _map = super(QuerySbjRuleResponseBodySbjRuleListSbjRuleItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.esp_ext_field_name is not None:
            result['EspExtFieldName'] = self.esp_ext_field_name
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.frontend_options is not None:
            result['FrontendOptions'] = self.frontend_options.to_map()
        if self.frontend_type is not None:
            result['FrontendType'] = self.frontend_type
        if self.required_expression is not None:
            result['RequiredExpression'] = self.required_expression
        if self.sbj_field_id is not None:
            result['SbjFieldId'] = self.sbj_field_id
        if self.show_expression is not None:
            result['ShowExpression'] = self.show_expression
        if self.trademark_service_expression is not None:
            result['TrademarkServiceExpression'] = self.trademark_service_expression
        if self.validate_regular_expression is not None:
            result['ValidateRegularExpression'] = self.validate_regular_expression
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('EspExtFieldName') is not None:
            self.esp_ext_field_name = m.get('EspExtFieldName')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FrontendOptions') is not None:
            temp_model = QuerySbjRuleResponseBodySbjRuleListSbjRuleItemFrontendOptions()
            self.frontend_options = temp_model.from_map(m['FrontendOptions'])
        if m.get('FrontendType') is not None:
            self.frontend_type = m.get('FrontendType')
        if m.get('RequiredExpression') is not None:
            self.required_expression = m.get('RequiredExpression')
        if m.get('SbjFieldId') is not None:
            self.sbj_field_id = m.get('SbjFieldId')
        if m.get('ShowExpression') is not None:
            self.show_expression = m.get('ShowExpression')
        if m.get('TrademarkServiceExpression') is not None:
            self.trademark_service_expression = m.get('TrademarkServiceExpression')
        if m.get('ValidateRegularExpression') is not None:
            self.validate_regular_expression = m.get('ValidateRegularExpression')
        return self


class QuerySbjRuleResponseBodySbjRuleList(TeaModel):
    def __init__(self, sbj_rule_item=None):
        self.sbj_rule_item = sbj_rule_item  # type: list[QuerySbjRuleResponseBodySbjRuleListSbjRuleItem]

    def validate(self):
        if self.sbj_rule_item:
            for k in self.sbj_rule_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySbjRuleResponseBodySbjRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SbjRuleItem'] = []
        if self.sbj_rule_item is not None:
            for k in self.sbj_rule_item:
                result['SbjRuleItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sbj_rule_item = []
        if m.get('SbjRuleItem') is not None:
            for k in m.get('SbjRuleItem'):
                temp_model = QuerySbjRuleResponseBodySbjRuleListSbjRuleItem()
                self.sbj_rule_item.append(temp_model.from_map(k))
        return self


class QuerySbjRuleResponseBody(TeaModel):
    def __init__(self, biz_type=None, request_id=None, rule_id=None, sbj_rule_list=None):
        self.biz_type = biz_type  # type: str
        self.request_id = request_id  # type: str
        self.rule_id = rule_id  # type: str
        self.sbj_rule_list = sbj_rule_list  # type: QuerySbjRuleResponseBodySbjRuleList

    def validate(self):
        if self.sbj_rule_list:
            self.sbj_rule_list.validate()

    def to_map(self):
        _map = super(QuerySbjRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.sbj_rule_list is not None:
            result['SbjRuleList'] = self.sbj_rule_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SbjRuleList') is not None:
            temp_model = QuerySbjRuleResponseBodySbjRuleList()
            self.sbj_rule_list = temp_model.from_map(m['SbjRuleList'])
        return self


class QuerySbjRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySbjRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySbjRuleResponse, self).to_map()
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
            temp_model = QuerySbjRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySupplementDetailRequest(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySupplementDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QuerySupplementDetailResponseBodyFileTemplateUrls(TeaModel):
    def __init__(self, file_template_urls=None):
        self.file_template_urls = file_template_urls  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySupplementDetailResponseBodyFileTemplateUrls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileTemplateUrls') is not None:
            self.file_template_urls = m.get('FileTemplateUrls')
        return self


class QuerySupplementDetailResponseBody(TeaModel):
    def __init__(self, accept_dead_time=None, accept_time=None, content=None, file_name=None,
                 file_template_urls=None, id=None, operate_time=None, reason=None, request_id=None, sbj_dead_time=None, send_time=None,
                 serial_number=None, status=None, tm_number=None, type=None, upload_file_template_url=None):
        self.accept_dead_time = accept_dead_time  # type: long
        self.accept_time = accept_time  # type: long
        self.content = content  # type: str
        self.file_name = file_name  # type: str
        self.file_template_urls = file_template_urls  # type: QuerySupplementDetailResponseBodyFileTemplateUrls
        self.id = id  # type: long
        self.operate_time = operate_time  # type: long
        self.reason = reason  # type: str
        self.request_id = request_id  # type: str
        self.sbj_dead_time = sbj_dead_time  # type: long
        self.send_time = send_time  # type: long
        self.serial_number = serial_number  # type: str
        self.status = status  # type: int
        self.tm_number = tm_number  # type: str
        self.type = type  # type: int
        self.upload_file_template_url = upload_file_template_url  # type: str

    def validate(self):
        if self.file_template_urls:
            self.file_template_urls.validate()

    def to_map(self):
        _map = super(QuerySupplementDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_dead_time is not None:
            result['AcceptDeadTime'] = self.accept_dead_time
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.content is not None:
            result['Content'] = self.content
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sbj_dead_time is not None:
            result['SbjDeadTime'] = self.sbj_dead_time
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        if self.upload_file_template_url is not None:
            result['UploadFileTemplateUrl'] = self.upload_file_template_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptDeadTime') is not None:
            self.accept_dead_time = m.get('AcceptDeadTime')
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileTemplateUrls') is not None:
            temp_model = QuerySupplementDetailResponseBodyFileTemplateUrls()
            self.file_template_urls = temp_model.from_map(m['FileTemplateUrls'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SbjDeadTime') is not None:
            self.sbj_dead_time = m.get('SbjDeadTime')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UploadFileTemplateUrl') is not None:
            self.upload_file_template_url = m.get('UploadFileTemplateUrl')
        return self


class QuerySupplementDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySupplementDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySupplementDetailResponse, self).to_map()
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
            temp_model = QuerySupplementDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskListRequest(TeaModel):
    def __init__(self, biz_type=None, page_num=None, page_size=None):
        self.biz_type = biz_type  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTaskListResponseBodyDataTaskList(TeaModel):
    def __init__(self, complete_time=None, create_time=None, err_msg=None, file_name=None, result=None,
                 task_status=None, task_type=None):
        self.complete_time = complete_time  # type: long
        self.create_time = create_time  # type: long
        self.err_msg = err_msg  # type: str
        self.file_name = file_name  # type: str
        self.result = result  # type: str
        self.task_status = task_status  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskListResponseBodyDataTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.result is not None:
            result['Result'] = self.result
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class QueryTaskListResponseBodyData(TeaModel):
    def __init__(self, task_list=None):
        self.task_list = task_list  # type: list[QueryTaskListResponseBodyDataTaskList]

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTaskListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = QueryTaskListResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class QueryTaskListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryTaskListResponseBodyData
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTaskListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTaskListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTaskListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTaskListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTaskListResponse, self).to_map()
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
            temp_model = QueryTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTmCollectionPageListRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTmCollectionPageListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTmCollectionPageListResponseBodyDataTrademark(TeaModel):
    def __init__(self, classification=None, collected=None, collection_content=None, id=None, item_id=None,
                 tm_name=None):
        self.classification = classification  # type: str
        self.collected = collected  # type: bool
        self.collection_content = collection_content  # type: str
        self.id = id  # type: long
        self.item_id = item_id  # type: str
        self.tm_name = tm_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTmCollectionPageListResponseBodyDataTrademark, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.collected is not None:
            result['Collected'] = self.collected
        if self.collection_content is not None:
            result['CollectionContent'] = self.collection_content
        if self.id is not None:
            result['Id'] = self.id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Collected') is not None:
            self.collected = m.get('Collected')
        if m.get('CollectionContent') is not None:
            self.collection_content = m.get('CollectionContent')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        return self


class QueryTmCollectionPageListResponseBodyData(TeaModel):
    def __init__(self, trademark=None):
        self.trademark = trademark  # type: list[QueryTmCollectionPageListResponseBodyDataTrademark]

    def validate(self):
        if self.trademark:
            for k in self.trademark:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTmCollectionPageListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Trademark'] = []
        if self.trademark is not None:
            for k in self.trademark:
                result['Trademark'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.trademark = []
        if m.get('Trademark') is not None:
            for k in m.get('Trademark'):
                temp_model = QueryTmCollectionPageListResponseBodyDataTrademark()
                self.trademark.append(temp_model.from_map(k))
        return self


class QueryTmCollectionPageListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryTmCollectionPageListResponseBodyData
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTmCollectionPageListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTmCollectionPageListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTmCollectionPageListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTmCollectionPageListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTmCollectionPageListResponse, self).to_map()
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
            temp_model = QueryTmCollectionPageListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTmSbjProduceRequest(TeaModel):
    def __init__(self, high_priority_biz_type_str=None, high_priority_material_name_str=None,
                 high_priority_order_id_str=None, high_priority_user_id_str=None, principal_key=None, principal_name=None, producer_type=None,
                 query_order_page_size=None):
        self.high_priority_biz_type_str = high_priority_biz_type_str  # type: str
        self.high_priority_material_name_str = high_priority_material_name_str  # type: str
        self.high_priority_order_id_str = high_priority_order_id_str  # type: str
        self.high_priority_user_id_str = high_priority_user_id_str  # type: str
        self.principal_key = principal_key  # type: str
        self.principal_name = principal_name  # type: str
        self.producer_type = producer_type  # type: str
        self.query_order_page_size = query_order_page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTmSbjProduceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.high_priority_biz_type_str is not None:
            result['HighPriorityBizTypeStr'] = self.high_priority_biz_type_str
        if self.high_priority_material_name_str is not None:
            result['HighPriorityMaterialNameStr'] = self.high_priority_material_name_str
        if self.high_priority_order_id_str is not None:
            result['HighPriorityOrderIdStr'] = self.high_priority_order_id_str
        if self.high_priority_user_id_str is not None:
            result['HighPriorityUserIdStr'] = self.high_priority_user_id_str
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.producer_type is not None:
            result['ProducerType'] = self.producer_type
        if self.query_order_page_size is not None:
            result['QueryOrderPageSize'] = self.query_order_page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HighPriorityBizTypeStr') is not None:
            self.high_priority_biz_type_str = m.get('HighPriorityBizTypeStr')
        if m.get('HighPriorityMaterialNameStr') is not None:
            self.high_priority_material_name_str = m.get('HighPriorityMaterialNameStr')
        if m.get('HighPriorityOrderIdStr') is not None:
            self.high_priority_order_id_str = m.get('HighPriorityOrderIdStr')
        if m.get('HighPriorityUserIdStr') is not None:
            self.high_priority_user_id_str = m.get('HighPriorityUserIdStr')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProducerType') is not None:
            self.producer_type = m.get('ProducerType')
        if m.get('QueryOrderPageSize') is not None:
            self.query_order_page_size = m.get('QueryOrderPageSize')
        return self


class QueryTmSbjProduceResponseBodyMoudleTmSbjProduceListExtend(TeaModel):
    def __init__(self, bid=None, black_icon=None, loa_oss_key=None, logo_goods_id=None, material_id=None,
                 submit_count=None, tm_nametype=None):
        self.bid = bid  # type: long
        self.black_icon = black_icon  # type: bool
        self.loa_oss_key = loa_oss_key  # type: str
        self.logo_goods_id = logo_goods_id  # type: str
        self.material_id = material_id  # type: str
        self.submit_count = submit_count  # type: long
        self.tm_nametype = tm_nametype  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTmSbjProduceResponseBodyMoudleTmSbjProduceListExtend, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.black_icon is not None:
            result['BlackIcon'] = self.black_icon
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.logo_goods_id is not None:
            result['LogoGoodsId'] = self.logo_goods_id
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.submit_count is not None:
            result['SubmitCount'] = self.submit_count
        if self.tm_nametype is not None:
            result['TmNametype'] = self.tm_nametype
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BlackIcon') is not None:
            self.black_icon = m.get('BlackIcon')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('LogoGoodsId') is not None:
            self.logo_goods_id = m.get('LogoGoodsId')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('SubmitCount') is not None:
            self.submit_count = m.get('SubmitCount')
        if m.get('TmNametype') is not None:
            self.tm_nametype = m.get('TmNametype')
        return self


class QueryTmSbjProduceResponseBodyMoudleTmSbjProduceList(TeaModel):
    def __init__(self, bit_flag=None, biz_id=None, classification_code=None, delete_flag=None, env=None, extend=None,
                 loa_id=None, main_order_id=None, material_id=None, material_name=None, order_id=None, order_price=None,
                 principal_key=None, principal_name=None, product_type=None, risk_source=None, status=None,
                 submit_audit_time=None, submit_status=None, submit_time=None, submit_times=None, tm_code=None, tm_icon=None,
                 tm_name=None, type=None, user_id=None):
        self.bit_flag = bit_flag  # type: long
        self.biz_id = biz_id  # type: str
        self.classification_code = classification_code  # type: str
        self.delete_flag = delete_flag  # type: str
        self.env = env  # type: str
        self.extend = extend  # type: QueryTmSbjProduceResponseBodyMoudleTmSbjProduceListExtend
        self.loa_id = loa_id  # type: long
        self.main_order_id = main_order_id  # type: str
        self.material_id = material_id  # type: long
        self.material_name = material_name  # type: str
        self.order_id = order_id  # type: str
        self.order_price = order_price  # type: float
        self.principal_key = principal_key  # type: str
        self.principal_name = principal_name  # type: str
        self.product_type = product_type  # type: str
        self.risk_source = risk_source  # type: str
        self.status = status  # type: str
        self.submit_audit_time = submit_audit_time  # type: long
        self.submit_status = submit_status  # type: str
        self.submit_time = submit_time  # type: long
        self.submit_times = submit_times  # type: long
        self.tm_code = tm_code  # type: str
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.type = type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.extend:
            self.extend.validate()

    def to_map(self):
        _map = super(QueryTmSbjProduceResponseBodyMoudleTmSbjProduceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_flag is not None:
            result['BitFlag'] = self.bit_flag
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.delete_flag is not None:
            result['DeleteFlag'] = self.delete_flag
        if self.env is not None:
            result['Env'] = self.env
        if self.extend is not None:
            result['Extend'] = self.extend.to_map()
        if self.loa_id is not None:
            result['LoaId'] = self.loa_id
        if self.main_order_id is not None:
            result['MainOrderId'] = self.main_order_id
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.risk_source is not None:
            result['RiskSource'] = self.risk_source
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_audit_time is not None:
            result['SubmitAuditTime'] = self.submit_audit_time
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.submit_times is not None:
            result['SubmitTimes'] = self.submit_times
        if self.tm_code is not None:
            result['TmCode'] = self.tm_code
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BitFlag') is not None:
            self.bit_flag = m.get('BitFlag')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('DeleteFlag') is not None:
            self.delete_flag = m.get('DeleteFlag')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Extend') is not None:
            temp_model = QueryTmSbjProduceResponseBodyMoudleTmSbjProduceListExtend()
            self.extend = temp_model.from_map(m['Extend'])
        if m.get('LoaId') is not None:
            self.loa_id = m.get('LoaId')
        if m.get('MainOrderId') is not None:
            self.main_order_id = m.get('MainOrderId')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RiskSource') is not None:
            self.risk_source = m.get('RiskSource')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitAuditTime') is not None:
            self.submit_audit_time = m.get('SubmitAuditTime')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('SubmitTimes') is not None:
            self.submit_times = m.get('SubmitTimes')
        if m.get('TmCode') is not None:
            self.tm_code = m.get('TmCode')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTmSbjProduceResponseBodyMoudle(TeaModel):
    def __init__(self, tm_sbj_produce_list=None):
        self.tm_sbj_produce_list = tm_sbj_produce_list  # type: list[QueryTmSbjProduceResponseBodyMoudleTmSbjProduceList]

    def validate(self):
        if self.tm_sbj_produce_list:
            for k in self.tm_sbj_produce_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTmSbjProduceResponseBodyMoudle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmSbjProduceList'] = []
        if self.tm_sbj_produce_list is not None:
            for k in self.tm_sbj_produce_list:
                result['TmSbjProduceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tm_sbj_produce_list = []
        if m.get('TmSbjProduceList') is not None:
            for k in m.get('TmSbjProduceList'):
                temp_model = QueryTmSbjProduceResponseBodyMoudleTmSbjProduceList()
                self.tm_sbj_produce_list.append(temp_model.from_map(k))
        return self


class QueryTmSbjProduceResponseBody(TeaModel):
    def __init__(self, moudle=None, request_id=None):
        self.moudle = moudle  # type: QueryTmSbjProduceResponseBodyMoudle
        self.request_id = request_id  # type: str

    def validate(self):
        if self.moudle:
            self.moudle.validate()

    def to_map(self):
        _map = super(QueryTmSbjProduceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.moudle is not None:
            result['Moudle'] = self.moudle.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Moudle') is not None:
            temp_model = QueryTmSbjProduceResponseBodyMoudle()
            self.moudle = temp_model.from_map(m['Moudle'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTmSbjProduceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTmSbjProduceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTmSbjProduceResponse, self).to_map()
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
            temp_model = QueryTmSbjProduceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTmSbjProduceDetailRequest(TeaModel):
    def __init__(self, biz_id=None, order_id=None):
        self.biz_id = biz_id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTmSbjProduceDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class QueryTmSbjProduceDetailResponseBodyFlags(TeaModel):
    def __init__(self, flags=None):
        self.flags = flags  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTmSbjProduceDetailResponseBodyFlags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flags is not None:
            result['Flags'] = self.flags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flags') is not None:
            self.flags = m.get('Flags')
        return self


class QueryTmSbjProduceDetailResponseBodyLeafCodesLeafCodes(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTmSbjProduceDetailResponseBodyLeafCodesLeafCodes, self).to_map()
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


class QueryTmSbjProduceDetailResponseBodyLeafCodes(TeaModel):
    def __init__(self, leaf_codes=None):
        self.leaf_codes = leaf_codes  # type: list[QueryTmSbjProduceDetailResponseBodyLeafCodesLeafCodes]

    def validate(self):
        if self.leaf_codes:
            for k in self.leaf_codes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTmSbjProduceDetailResponseBodyLeafCodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LeafCodes'] = []
        if self.leaf_codes is not None:
            for k in self.leaf_codes:
                result['LeafCodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.leaf_codes = []
        if m.get('LeafCodes') is not None:
            for k in m.get('LeafCodes'):
                temp_model = QueryTmSbjProduceDetailResponseBodyLeafCodesLeafCodes()
                self.leaf_codes.append(temp_model.from_map(k))
        return self


class QueryTmSbjProduceDetailResponseBodyMaterialDetail(TeaModel):
    def __init__(self, address=None, business_licence_url=None, card_number=None, city=None, contact_address=None,
                 contact_email=None, contact_name=None, contact_number=None, contact_province=None, contact_zipcode=None,
                 country=None, detailed_contact_address=None, eaddress=None, ename=None, expiration_date=None,
                 id_card_number=None, id_card_url=None, loa_url=None, name=None, passport_url=None, personal_type=None,
                 province=None, region=None, status=None, town=None, type=None):
        self.address = address  # type: str
        self.business_licence_url = business_licence_url  # type: str
        self.card_number = card_number  # type: str
        self.city = city  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_province = contact_province  # type: str
        self.contact_zipcode = contact_zipcode  # type: str
        self.country = country  # type: str
        self.detailed_contact_address = detailed_contact_address  # type: str
        self.eaddress = eaddress  # type: str
        self.ename = ename  # type: str
        self.expiration_date = expiration_date  # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_url = id_card_url  # type: str
        self.loa_url = loa_url  # type: str
        self.name = name  # type: str
        self.passport_url = passport_url  # type: str
        self.personal_type = personal_type  # type: int
        self.province = province  # type: str
        self.region = region  # type: int
        self.status = status  # type: int
        self.town = town  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTmSbjProduceDetailResponseBodyMaterialDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.country is not None:
            result['Country'] = self.country
        if self.detailed_contact_address is not None:
            result['DetailedContactAddress'] = self.detailed_contact_address
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.town is not None:
            result['Town'] = self.town
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('DetailedContactAddress') is not None:
            self.detailed_contact_address = m.get('DetailedContactAddress')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTmSbjProduceDetailResponseBodyRootCode(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTmSbjProduceDetailResponseBodyRootCode, self).to_map()
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


class QueryTmSbjProduceDetailResponseBody(TeaModel):
    def __init__(self, accept_url=None, biz_id=None, cn_info_url=None, extend_info=None, flags=None,
                 gray_icon_url=None, issue_date=None, leaf_codes=None, loa_url=None, material_detail=None, material_name=None,
                 note=None, order_id=None, principal_name=None, request_id=None, root_code=None, status=None,
                 submit_count=None, submit_status=None, tm_icon=None, tm_name=None, tm_name_type=None, tm_number=None,
                 tm_order_id=None, type=None):
        self.accept_url = accept_url  # type: str
        self.biz_id = biz_id  # type: str
        self.cn_info_url = cn_info_url  # type: str
        self.extend_info = extend_info  # type: dict[str, any]
        self.flags = flags  # type: QueryTmSbjProduceDetailResponseBodyFlags
        self.gray_icon_url = gray_icon_url  # type: str
        self.issue_date = issue_date  # type: str
        self.leaf_codes = leaf_codes  # type: QueryTmSbjProduceDetailResponseBodyLeafCodes
        self.loa_url = loa_url  # type: str
        self.material_detail = material_detail  # type: QueryTmSbjProduceDetailResponseBodyMaterialDetail
        self.material_name = material_name  # type: str
        self.note = note  # type: str
        self.order_id = order_id  # type: str
        self.principal_name = principal_name  # type: int
        self.request_id = request_id  # type: str
        self.root_code = root_code  # type: QueryTmSbjProduceDetailResponseBodyRootCode
        self.status = status  # type: int
        self.submit_count = submit_count  # type: int
        self.submit_status = submit_status  # type: str
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_name_type = tm_name_type  # type: int
        self.tm_number = tm_number  # type: str
        self.tm_order_id = tm_order_id  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.flags:
            self.flags.validate()
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_detail:
            self.material_detail.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super(QueryTmSbjProduceDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_url is not None:
            result['AcceptUrl'] = self.accept_url
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.flags is not None:
            result['Flags'] = self.flags.to_map()
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.issue_date is not None:
            result['IssueDate'] = self.issue_date
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_detail is not None:
            result['MaterialDetail'] = self.material_detail.to_map()
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_count is not None:
            result['SubmitCount'] = self.submit_count
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.tm_order_id is not None:
            result['TmOrderId'] = self.tm_order_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptUrl') is not None:
            self.accept_url = m.get('AcceptUrl')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Flags') is not None:
            temp_model = QueryTmSbjProduceDetailResponseBodyFlags()
            self.flags = temp_model.from_map(m['Flags'])
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('IssueDate') is not None:
            self.issue_date = m.get('IssueDate')
        if m.get('LeafCodes') is not None:
            temp_model = QueryTmSbjProduceDetailResponseBodyLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialDetail') is not None:
            temp_model = QueryTmSbjProduceDetailResponseBodyMaterialDetail()
            self.material_detail = temp_model.from_map(m['MaterialDetail'])
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootCode') is not None:
            temp_model = QueryTmSbjProduceDetailResponseBodyRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitCount') is not None:
            self.submit_count = m.get('SubmitCount')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TmOrderId') is not None:
            self.tm_order_id = m.get('TmOrderId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTmSbjProduceDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTmSbjProduceDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTmSbjProduceDetailResponse, self).to_map()
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
            temp_model = QueryTmSbjProduceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeIntentionUserListRequest(TeaModel):
    def __init__(self, begin=None, biz_id=None, end=None, page_num=None, page_size=None, status=None, type=None):
        self.begin = begin  # type: long
        self.biz_id = biz_id  # type: str
        self.end = end  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: int
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeIntentionUserListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.end is not None:
            result['End'] = self.end
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTradeIntentionUserListResponseBodyDataTrademark(TeaModel):
    def __init__(self, biz_id=None, classification=None, description=None, document_date=None, document_name=None,
                 document_url=None, grade=None, mobile=None, register_number=None, status=None, type=None, user_name=None):
        self.biz_id = biz_id  # type: str
        self.classification = classification  # type: str
        self.description = description  # type: str
        self.document_date = document_date  # type: str
        self.document_name = document_name  # type: str
        self.document_url = document_url  # type: str
        self.grade = grade  # type: int
        self.mobile = mobile  # type: str
        self.register_number = register_number  # type: str
        self.status = status  # type: int
        self.type = type  # type: int
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeIntentionUserListResponseBodyDataTrademark, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.description is not None:
            result['Description'] = self.description
        if self.document_date is not None:
            result['DocumentDate'] = self.document_date
        if self.document_name is not None:
            result['DocumentName'] = self.document_name
        if self.document_url is not None:
            result['DocumentUrl'] = self.document_url
        if self.grade is not None:
            result['Grade'] = self.grade
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocumentDate') is not None:
            self.document_date = m.get('DocumentDate')
        if m.get('DocumentName') is not None:
            self.document_name = m.get('DocumentName')
        if m.get('DocumentUrl') is not None:
            self.document_url = m.get('DocumentUrl')
        if m.get('Grade') is not None:
            self.grade = m.get('Grade')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryTradeIntentionUserListResponseBodyData(TeaModel):
    def __init__(self, trademark=None):
        self.trademark = trademark  # type: list[QueryTradeIntentionUserListResponseBodyDataTrademark]

    def validate(self):
        if self.trademark:
            for k in self.trademark:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeIntentionUserListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Trademark'] = []
        if self.trademark is not None:
            for k in self.trademark:
                result['Trademark'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.trademark = []
        if m.get('Trademark') is not None:
            for k in m.get('Trademark'):
                temp_model = QueryTradeIntentionUserListResponseBodyDataTrademark()
                self.trademark.append(temp_model.from_map(k))
        return self


class QueryTradeIntentionUserListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryTradeIntentionUserListResponseBodyData
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTradeIntentionUserListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeIntentionUserListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTradeIntentionUserListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTradeIntentionUserListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTradeIntentionUserListResponse, self).to_map()
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
            temp_model = QueryTradeIntentionUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationDetailRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryTradeMarkApplicationDetailResponseBodyAdminUploads(TeaModel):
    def __init__(self, license_pic_url=None, loa_pic_url=None):
        self.license_pic_url = license_pic_url  # type: str
        self.loa_pic_url = loa_pic_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyAdminUploads, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_pic_url is not None:
            result['LicensePicUrl'] = self.license_pic_url
        if self.loa_pic_url is not None:
            result['LoaPicUrl'] = self.loa_pic_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LicensePicUrl') is not None:
            self.license_pic_url = m.get('LicensePicUrl')
        if m.get('LoaPicUrl') is not None:
            self.loa_pic_url = m.get('LoaPicUrl')
        return self


class QueryTradeMarkApplicationDetailResponseBodyFirstClassification(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyFirstClassification, self).to_map()
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


class QueryTradeMarkApplicationDetailResponseBodyFlags(TeaModel):
    def __init__(self, flag=None):
        self.flag = flag  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyFlags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flag is not None:
            result['Flag'] = self.flag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        return self


class QueryTradeMarkApplicationDetailResponseBodyJudgeResultUrl(TeaModel):
    def __init__(self, judge_result_url=None):
        self.judge_result_url = judge_result_url  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyJudgeResultUrl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.judge_result_url is not None:
            result['JudgeResultUrl'] = self.judge_result_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JudgeResultUrl') is not None:
            self.judge_result_url = m.get('JudgeResultUrl')
        return self


class QueryTradeMarkApplicationDetailResponseBodyMaterialDetailReviewAdditionalFiles(TeaModel):
    def __init__(self, review_additional_file=None):
        self.review_additional_file = review_additional_file  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyMaterialDetailReviewAdditionalFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_additional_file is not None:
            result['ReviewAdditionalFile'] = self.review_additional_file
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReviewAdditionalFile') is not None:
            self.review_additional_file = m.get('ReviewAdditionalFile')
        return self


class QueryTradeMarkApplicationDetailResponseBodyMaterialDetail(TeaModel):
    def __init__(self, address=None, business_licence_url=None, card_number=None, city=None, contact_address=None,
                 contact_city=None, contact_district=None, contact_email=None, contact_name=None, contact_number=None,
                 contact_province=None, contact_zipcode=None, country=None, detailed_contact_address=None, eaddress=None, ename=None,
                 expiration_date=None, fact_and_reason_pdf_path=None, id_card_name=None, id_card_number=None, id_card_url=None,
                 legal_notice_url=None, loa_url=None, material_version=None, name=None, passport_url=None, personal_type=None,
                 principal_name=None, province=None, region=None, review_additional_files=None, review_application_file=None,
                 status=None, supplement_evidence_catalog_file=None, supplement_evidence_material_file=None,
                 supplement_reason_file=None, town=None, type=None):
        self.address = address  # type: str
        self.business_licence_url = business_licence_url  # type: str
        self.card_number = card_number  # type: str
        self.city = city  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_city = contact_city  # type: str
        self.contact_district = contact_district  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_province = contact_province  # type: str
        self.contact_zipcode = contact_zipcode  # type: str
        self.country = country  # type: str
        self.detailed_contact_address = detailed_contact_address  # type: str
        self.eaddress = eaddress  # type: str
        self.ename = ename  # type: str
        self.expiration_date = expiration_date  # type: str
        self.fact_and_reason_pdf_path = fact_and_reason_pdf_path  # type: str
        self.id_card_name = id_card_name  # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_url = id_card_url  # type: str
        self.legal_notice_url = legal_notice_url  # type: str
        self.loa_url = loa_url  # type: str
        self.material_version = material_version  # type: str
        self.name = name  # type: str
        self.passport_url = passport_url  # type: str
        self.personal_type = personal_type  # type: long
        self.principal_name = principal_name  # type: int
        self.province = province  # type: str
        self.region = region  # type: int
        self.review_additional_files = review_additional_files  # type: QueryTradeMarkApplicationDetailResponseBodyMaterialDetailReviewAdditionalFiles
        self.review_application_file = review_application_file  # type: str
        self.status = status  # type: int
        self.supplement_evidence_catalog_file = supplement_evidence_catalog_file  # type: str
        self.supplement_evidence_material_file = supplement_evidence_material_file  # type: str
        self.supplement_reason_file = supplement_reason_file  # type: str
        self.town = town  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.review_additional_files:
            self.review_additional_files.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyMaterialDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.country is not None:
            result['Country'] = self.country
        if self.detailed_contact_address is not None:
            result['DetailedContactAddress'] = self.detailed_contact_address
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.fact_and_reason_pdf_path is not None:
            result['FactAndReasonPdfPath'] = self.fact_and_reason_pdf_path
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.legal_notice_url is not None:
            result['LegalNoticeUrl'] = self.legal_notice_url
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_version is not None:
            result['MaterialVersion'] = self.material_version
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        if self.review_additional_files is not None:
            result['ReviewAdditionalFiles'] = self.review_additional_files.to_map()
        if self.review_application_file is not None:
            result['ReviewApplicationFile'] = self.review_application_file
        if self.status is not None:
            result['Status'] = self.status
        if self.supplement_evidence_catalog_file is not None:
            result['SupplementEvidenceCatalogFile'] = self.supplement_evidence_catalog_file
        if self.supplement_evidence_material_file is not None:
            result['SupplementEvidenceMaterialFile'] = self.supplement_evidence_material_file
        if self.supplement_reason_file is not None:
            result['SupplementReasonFile'] = self.supplement_reason_file
        if self.town is not None:
            result['Town'] = self.town
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('DetailedContactAddress') is not None:
            self.detailed_contact_address = m.get('DetailedContactAddress')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('FactAndReasonPdfPath') is not None:
            self.fact_and_reason_pdf_path = m.get('FactAndReasonPdfPath')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LegalNoticeUrl') is not None:
            self.legal_notice_url = m.get('LegalNoticeUrl')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialVersion') is not None:
            self.material_version = m.get('MaterialVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReviewAdditionalFiles') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyMaterialDetailReviewAdditionalFiles()
            self.review_additional_files = temp_model.from_map(m['ReviewAdditionalFiles'])
        if m.get('ReviewApplicationFile') is not None:
            self.review_application_file = m.get('ReviewApplicationFile')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplementEvidenceCatalogFile') is not None:
            self.supplement_evidence_catalog_file = m.get('SupplementEvidenceCatalogFile')
        if m.get('SupplementEvidenceMaterialFile') is not None:
            self.supplement_evidence_material_file = m.get('SupplementEvidenceMaterialFile')
        if m.get('SupplementReasonFile') is not None:
            self.supplement_reason_file = m.get('SupplementReasonFile')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTradeMarkApplicationDetailResponseBodyReceiptUrl(TeaModel):
    def __init__(self, receipt_url=None):
        self.receipt_url = receipt_url  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyReceiptUrl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        return self


class QueryTradeMarkApplicationDetailResponseBodyRenewResponse(TeaModel):
    def __init__(self, address=None, eng_address=None, eng_name=None, name=None, register_time=None,
                 submit_sbjtime=None):
        self.address = address  # type: str
        self.eng_address = eng_address  # type: str
        self.eng_name = eng_name  # type: str
        self.name = name  # type: str
        self.register_time = register_time  # type: long
        self.submit_sbjtime = submit_sbjtime  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyRenewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.name is not None:
            result['Name'] = self.name
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.submit_sbjtime is not None:
            result['SubmitSbjtime'] = self.submit_sbjtime
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('SubmitSbjtime') is not None:
            self.submit_sbjtime = m.get('SubmitSbjtime')
        return self


class QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFilesReviewSupplements(TeaModel):
    def __init__(self, review_supplement=None):
        self.review_supplement = review_supplement  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFilesReviewSupplements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_supplement is not None:
            result['ReviewSupplement'] = self.review_supplement
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReviewSupplement') is not None:
            self.review_supplement = m.get('ReviewSupplement')
        return self


class QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFiles(TeaModel):
    def __init__(self, review_audit=None, review_keep=None, review_part=None, review_pass=None,
                 review_supplements=None):
        self.review_audit = review_audit  # type: str
        self.review_keep = review_keep  # type: str
        self.review_part = review_part  # type: str
        self.review_pass = review_pass  # type: str
        self.review_supplements = review_supplements  # type: QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFilesReviewSupplements

    def validate(self):
        if self.review_supplements:
            self.review_supplements.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_audit is not None:
            result['ReviewAudit'] = self.review_audit
        if self.review_keep is not None:
            result['ReviewKeep'] = self.review_keep
        if self.review_part is not None:
            result['ReviewPart'] = self.review_part
        if self.review_pass is not None:
            result['ReviewPass'] = self.review_pass
        if self.review_supplements is not None:
            result['ReviewSupplements'] = self.review_supplements.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReviewAudit') is not None:
            self.review_audit = m.get('ReviewAudit')
        if m.get('ReviewKeep') is not None:
            self.review_keep = m.get('ReviewKeep')
        if m.get('ReviewPart') is not None:
            self.review_part = m.get('ReviewPart')
        if m.get('ReviewPass') is not None:
            self.review_pass = m.get('ReviewPass')
        if m.get('ReviewSupplements') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFilesReviewSupplements()
            self.review_supplements = temp_model.from_map(m['ReviewSupplements'])
        return self


class QueryTradeMarkApplicationDetailResponseBodySupplementsSupplementsFileTemplateUrls(TeaModel):
    def __init__(self, file_template_urls=None):
        self.file_template_urls = file_template_urls  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodySupplementsSupplementsFileTemplateUrls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileTemplateUrls') is not None:
            self.file_template_urls = m.get('FileTemplateUrls')
        return self


class QueryTradeMarkApplicationDetailResponseBodySupplementsSupplements(TeaModel):
    def __init__(self, accept_dead_time=None, accept_time=None, batch_num=None, content=None,
                 file_template_urls=None, filename=None, id=None, operate_time=None, order_id=None, sbj_dead_time=None, send_time=None,
                 serial_number=None, status=None, tm_number=None, type=None, upload_file_template_url=None):
        self.accept_dead_time = accept_dead_time  # type: long
        self.accept_time = accept_time  # type: long
        self.batch_num = batch_num  # type: str
        self.content = content  # type: str
        self.file_template_urls = file_template_urls  # type: QueryTradeMarkApplicationDetailResponseBodySupplementsSupplementsFileTemplateUrls
        self.filename = filename  # type: str
        self.id = id  # type: long
        self.operate_time = operate_time  # type: long
        self.order_id = order_id  # type: str
        self.sbj_dead_time = sbj_dead_time  # type: long
        self.send_time = send_time  # type: long
        self.serial_number = serial_number  # type: str
        self.status = status  # type: int
        self.tm_number = tm_number  # type: str
        self.type = type  # type: int
        self.upload_file_template_url = upload_file_template_url  # type: str

    def validate(self):
        if self.file_template_urls:
            self.file_template_urls.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodySupplementsSupplements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_dead_time is not None:
            result['AcceptDeadTime'] = self.accept_dead_time
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.batch_num is not None:
            result['BatchNum'] = self.batch_num
        if self.content is not None:
            result['Content'] = self.content
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls.to_map()
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.id is not None:
            result['Id'] = self.id
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.sbj_dead_time is not None:
            result['SbjDeadTime'] = self.sbj_dead_time
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        if self.upload_file_template_url is not None:
            result['UploadFileTemplateUrl'] = self.upload_file_template_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptDeadTime') is not None:
            self.accept_dead_time = m.get('AcceptDeadTime')
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('BatchNum') is not None:
            self.batch_num = m.get('BatchNum')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('FileTemplateUrls') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodySupplementsSupplementsFileTemplateUrls()
            self.file_template_urls = temp_model.from_map(m['FileTemplateUrls'])
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('SbjDeadTime') is not None:
            self.sbj_dead_time = m.get('SbjDeadTime')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UploadFileTemplateUrl') is not None:
            self.upload_file_template_url = m.get('UploadFileTemplateUrl')
        return self


class QueryTradeMarkApplicationDetailResponseBodySupplements(TeaModel):
    def __init__(self, supplements=None):
        self.supplements = supplements  # type: list[QueryTradeMarkApplicationDetailResponseBodySupplementsSupplements]

    def validate(self):
        if self.supplements:
            for k in self.supplements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodySupplements, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Supplements'] = []
        if self.supplements is not None:
            for k in self.supplements:
                result['Supplements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.supplements = []
        if m.get('Supplements') is not None:
            for k in m.get('Supplements'):
                temp_model = QueryTradeMarkApplicationDetailResponseBodySupplementsSupplements()
                self.supplements.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationDetailResponseBodyThirdClassificationThirdClassifications(TeaModel):
    def __init__(self, code=None, name=None):
        self.code = code  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyThirdClassificationThirdClassifications, self).to_map()
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


class QueryTradeMarkApplicationDetailResponseBodyThirdClassification(TeaModel):
    def __init__(self, third_classifications=None):
        self.third_classifications = third_classifications  # type: list[QueryTradeMarkApplicationDetailResponseBodyThirdClassificationThirdClassifications]

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBodyThirdClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryTradeMarkApplicationDetailResponseBodyThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationDetailResponseBody(TeaModel):
    def __init__(self, accept_url=None, admin_uploads=None, biz_id=None, create_time=None, extend_info=None,
                 first_classification=None, flags=None, gray_icon_url=None, judge_result_url=None, legal_notice_url=None, loa_url=None,
                 logistics_certificate_url=None, logistics_no=None, material_detail=None, material_id=None, not_accept_url=None, note=None,
                 order_id=None, order_price=None, partner_code=None, partner_mobile=None, partner_name=None,
                 principal_name=None, receipt_url=None, recv_user_logistics=None, renew_response=None, request_id=None,
                 review_official_files=None, send_sbj_logistics=None, send_time=None, send_user_logistics=None, service_price=None,
                 specification=None, status=None, submit_audit_time=None, submit_time=None, supplements=None, system_version=None,
                 third_classification=None, tm_icon=None, tm_name=None, tm_name_type=None, tm_number=None, total_price=None, type=None,
                 update_time=None):
        self.accept_url = accept_url  # type: str
        self.admin_uploads = admin_uploads  # type: QueryTradeMarkApplicationDetailResponseBodyAdminUploads
        self.biz_id = biz_id  # type: str
        self.create_time = create_time  # type: long
        self.extend_info = extend_info  # type: dict[str, any]
        self.first_classification = first_classification  # type: QueryTradeMarkApplicationDetailResponseBodyFirstClassification
        self.flags = flags  # type: QueryTradeMarkApplicationDetailResponseBodyFlags
        self.gray_icon_url = gray_icon_url  # type: str
        self.judge_result_url = judge_result_url  # type: QueryTradeMarkApplicationDetailResponseBodyJudgeResultUrl
        self.legal_notice_url = legal_notice_url  # type: str
        self.loa_url = loa_url  # type: str
        self.logistics_certificate_url = logistics_certificate_url  # type: str
        self.logistics_no = logistics_no  # type: str
        self.material_detail = material_detail  # type: QueryTradeMarkApplicationDetailResponseBodyMaterialDetail
        self.material_id = material_id  # type: long
        self.not_accept_url = not_accept_url  # type: str
        self.note = note  # type: str
        self.order_id = order_id  # type: str
        self.order_price = order_price  # type: float
        self.partner_code = partner_code  # type: str
        self.partner_mobile = partner_mobile  # type: str
        self.partner_name = partner_name  # type: str
        self.principal_name = principal_name  # type: int
        self.receipt_url = receipt_url  # type: QueryTradeMarkApplicationDetailResponseBodyReceiptUrl
        self.recv_user_logistics = recv_user_logistics  # type: str
        self.renew_response = renew_response  # type: QueryTradeMarkApplicationDetailResponseBodyRenewResponse
        self.request_id = request_id  # type: str
        self.review_official_files = review_official_files  # type: QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFiles
        self.send_sbj_logistics = send_sbj_logistics  # type: str
        self.send_time = send_time  # type: str
        self.send_user_logistics = send_user_logistics  # type: str
        self.service_price = service_price  # type: float
        self.specification = specification  # type: int
        self.status = status  # type: int
        self.submit_audit_time = submit_audit_time  # type: long
        self.submit_time = submit_time  # type: long
        self.supplements = supplements  # type: QueryTradeMarkApplicationDetailResponseBodySupplements
        self.system_version = system_version  # type: str
        self.third_classification = third_classification  # type: QueryTradeMarkApplicationDetailResponseBodyThirdClassification
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_name_type = tm_name_type  # type: int
        self.tm_number = tm_number  # type: str
        self.total_price = total_price  # type: float
        self.type = type  # type: int
        self.update_time = update_time  # type: long

    def validate(self):
        if self.admin_uploads:
            self.admin_uploads.validate()
        if self.first_classification:
            self.first_classification.validate()
        if self.flags:
            self.flags.validate()
        if self.judge_result_url:
            self.judge_result_url.validate()
        if self.material_detail:
            self.material_detail.validate()
        if self.receipt_url:
            self.receipt_url.validate()
        if self.renew_response:
            self.renew_response.validate()
        if self.review_official_files:
            self.review_official_files.validate()
        if self.supplements:
            self.supplements.validate()
        if self.third_classification:
            self.third_classification.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_url is not None:
            result['AcceptUrl'] = self.accept_url
        if self.admin_uploads is not None:
            result['AdminUploads'] = self.admin_uploads.to_map()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.flags is not None:
            result['Flags'] = self.flags.to_map()
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.judge_result_url is not None:
            result['JudgeResultUrl'] = self.judge_result_url.to_map()
        if self.legal_notice_url is not None:
            result['LegalNoticeUrl'] = self.legal_notice_url
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.logistics_certificate_url is not None:
            result['LogisticsCertificateUrl'] = self.logistics_certificate_url
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.material_detail is not None:
            result['MaterialDetail'] = self.material_detail.to_map()
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.not_accept_url is not None:
            result['NotAcceptUrl'] = self.not_accept_url
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.partner_mobile is not None:
            result['PartnerMobile'] = self.partner_mobile
        if self.partner_name is not None:
            result['PartnerName'] = self.partner_name
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url.to_map()
        if self.recv_user_logistics is not None:
            result['RecvUserLogistics'] = self.recv_user_logistics
        if self.renew_response is not None:
            result['RenewResponse'] = self.renew_response.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.review_official_files is not None:
            result['ReviewOfficialFiles'] = self.review_official_files.to_map()
        if self.send_sbj_logistics is not None:
            result['SendSbjLogistics'] = self.send_sbj_logistics
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.send_user_logistics is not None:
            result['SendUserLogistics'] = self.send_user_logistics
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_audit_time is not None:
            result['SubmitAuditTime'] = self.submit_audit_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.supplements is not None:
            result['Supplements'] = self.supplements.to_map()
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptUrl') is not None:
            self.accept_url = m.get('AcceptUrl')
        if m.get('AdminUploads') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyAdminUploads()
            self.admin_uploads = temp_model.from_map(m['AdminUploads'])
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FirstClassification') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('Flags') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyFlags()
            self.flags = temp_model.from_map(m['Flags'])
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('JudgeResultUrl') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyJudgeResultUrl()
            self.judge_result_url = temp_model.from_map(m['JudgeResultUrl'])
        if m.get('LegalNoticeUrl') is not None:
            self.legal_notice_url = m.get('LegalNoticeUrl')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('LogisticsCertificateUrl') is not None:
            self.logistics_certificate_url = m.get('LogisticsCertificateUrl')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('MaterialDetail') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyMaterialDetail()
            self.material_detail = temp_model.from_map(m['MaterialDetail'])
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('NotAcceptUrl') is not None:
            self.not_accept_url = m.get('NotAcceptUrl')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PartnerMobile') is not None:
            self.partner_mobile = m.get('PartnerMobile')
        if m.get('PartnerName') is not None:
            self.partner_name = m.get('PartnerName')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ReceiptUrl') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyReceiptUrl()
            self.receipt_url = temp_model.from_map(m['ReceiptUrl'])
        if m.get('RecvUserLogistics') is not None:
            self.recv_user_logistics = m.get('RecvUserLogistics')
        if m.get('RenewResponse') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyRenewResponse()
            self.renew_response = temp_model.from_map(m['RenewResponse'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReviewOfficialFiles') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFiles()
            self.review_official_files = temp_model.from_map(m['ReviewOfficialFiles'])
        if m.get('SendSbjLogistics') is not None:
            self.send_sbj_logistics = m.get('SendSbjLogistics')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SendUserLogistics') is not None:
            self.send_user_logistics = m.get('SendUserLogistics')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitAuditTime') is not None:
            self.submit_audit_time = m.get('SubmitAuditTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('Supplements') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodySupplements()
            self.supplements = temp_model.from_map(m['Supplements'])
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('ThirdClassification') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryTradeMarkApplicationDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTradeMarkApplicationDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationDetailResponse, self).to_map()
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
            temp_model = QueryTradeMarkApplicationDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationLogsRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryTradeMarkApplicationLogsResponseBodyDataData(TeaModel):
    def __init__(self, biz_id=None, biz_status=None, extend_content=None, note=None, operate_time=None,
                 operate_type=None, to_biz_status=None):
        self.biz_id = biz_id  # type: str
        self.biz_status = biz_status  # type: int
        self.extend_content = extend_content  # type: str
        self.note = note  # type: str
        self.operate_time = operate_time  # type: long
        self.operate_type = operate_type  # type: int
        self.to_biz_status = to_biz_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationLogsResponseBodyDataData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.extend_content is not None:
            result['ExtendContent'] = self.extend_content
        if self.note is not None:
            result['Note'] = self.note
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.to_biz_status is not None:
            result['ToBizStatus'] = self.to_biz_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('ExtendContent') is not None:
            self.extend_content = m.get('ExtendContent')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('ToBizStatus') is not None:
            self.to_biz_status = m.get('ToBizStatus')
        return self


class QueryTradeMarkApplicationLogsResponseBodyData(TeaModel):
    def __init__(self, data=None):
        self.data = data  # type: list[QueryTradeMarkApplicationLogsResponseBodyDataData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationLogsResponseBodyData, self).to_map()
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
                temp_model = QueryTradeMarkApplicationLogsResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationLogsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: QueryTradeMarkApplicationLogsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryTradeMarkApplicationLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTradeMarkApplicationLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTradeMarkApplicationLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationLogsResponse, self).to_map()
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
            temp_model = QueryTradeMarkApplicationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationsRequest(TeaModel):
    def __init__(self, biz_id=None, classification_code=None, hidden=None, intention_biz_id=None, logistics_no=None,
                 material_name=None, order_id=None, page_num=None, page_size=None, product_type=None, sort_filed=None,
                 sort_order=None, specification=None, status=None, status_list=None, supplement_status=None, tm_name=None,
                 tm_number=None, type=None):
        self.biz_id = biz_id  # type: str
        self.classification_code = classification_code  # type: str
        self.hidden = hidden  # type: int
        self.intention_biz_id = intention_biz_id  # type: str
        self.logistics_no = logistics_no  # type: str
        self.material_name = material_name  # type: str
        self.order_id = order_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.product_type = product_type  # type: int
        self.sort_filed = sort_filed  # type: str
        self.sort_order = sort_order  # type: str
        self.specification = specification  # type: int
        self.status = status  # type: int
        self.status_list = status_list  # type: list[int]
        self.supplement_status = supplement_status  # type: int
        self.tm_name = tm_name  # type: str
        self.tm_number = tm_number  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.hidden is not None:
            result['Hidden'] = self.hidden
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.status is not None:
            result['Status'] = self.status
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTradeMarkApplicationsShrinkRequest(TeaModel):
    def __init__(self, biz_id=None, classification_code=None, hidden=None, intention_biz_id=None, logistics_no=None,
                 material_name=None, order_id=None, page_num=None, page_size=None, product_type=None, sort_filed=None,
                 sort_order=None, specification=None, status=None, status_list_shrink=None, supplement_status=None,
                 tm_name=None, tm_number=None, type=None):
        self.biz_id = biz_id  # type: str
        self.classification_code = classification_code  # type: str
        self.hidden = hidden  # type: int
        self.intention_biz_id = intention_biz_id  # type: str
        self.logistics_no = logistics_no  # type: str
        self.material_name = material_name  # type: str
        self.order_id = order_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.product_type = product_type  # type: int
        self.sort_filed = sort_filed  # type: str
        self.sort_order = sort_order  # type: str
        self.specification = specification  # type: int
        self.status = status  # type: int
        self.status_list_shrink = status_list_shrink  # type: str
        self.supplement_status = supplement_status  # type: int
        self.tm_name = tm_name  # type: str
        self.tm_number = tm_number  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.hidden is not None:
            result['Hidden'] = self.hidden
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.status is not None:
            result['Status'] = self.status
        if self.status_list_shrink is not None:
            result['StatusList'] = self.status_list_shrink
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusList') is not None:
            self.status_list_shrink = m.get('StatusList')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesFirstClassification(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBodyDataTmProducesFirstClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesFlags(TeaModel):
    def __init__(self, flags=None):
        self.flags = flags  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBodyDataTmProducesFlags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flags is not None:
            result['Flags'] = self.flags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flags') is not None:
            self.flags = m.get('Flags')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesRenewResponse(TeaModel):
    def __init__(self, address=None, eng_address=None, eng_name=None, name=None, register_time=None,
                 submit_sbjtime=None):
        self.address = address  # type: str
        self.eng_address = eng_address  # type: str
        self.eng_name = eng_name  # type: str
        self.name = name  # type: str
        self.register_time = register_time  # type: long
        self.submit_sbjtime = submit_sbjtime  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBodyDataTmProducesRenewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.name is not None:
            result['Name'] = self.name
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.submit_sbjtime is not None:
            result['SubmitSbjtime'] = self.submit_sbjtime
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('SubmitSbjtime') is not None:
            self.submit_sbjtime = m.get('SubmitSbjtime')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassificationThirdClassifications(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassificationThirdClassifications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassification(TeaModel):
    def __init__(self, third_classifications=None):
        self.third_classifications = third_classifications  # type: list[QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassificationThirdClassifications]

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProduces(TeaModel):
    def __init__(self, agreement_id=None, biz_id=None, create_time=None, first_classification=None, flags=None,
                 loa_url=None, material_id=None, material_name=None, note=None, order_id=None, order_price=None,
                 principal_name=None, remark=None, renew_response=None, service_price=None, show_go_to_defend_button=None,
                 specification=None, status=None, submit_audit_time=None, submit_time=None, supplement_id=None,
                 supplement_status=None, system_version=None, third_classification=None, tm_icon=None, tm_name=None, tm_number=None,
                 total_price=None, type=None, update_time=None, user_id=None):
        self.agreement_id = agreement_id  # type: str
        self.biz_id = biz_id  # type: str
        self.create_time = create_time  # type: long
        self.first_classification = first_classification  # type: QueryTradeMarkApplicationsResponseBodyDataTmProducesFirstClassification
        self.flags = flags  # type: QueryTradeMarkApplicationsResponseBodyDataTmProducesFlags
        self.loa_url = loa_url  # type: str
        self.material_id = material_id  # type: long
        self.material_name = material_name  # type: str
        self.note = note  # type: str
        self.order_id = order_id  # type: str
        self.order_price = order_price  # type: float
        self.principal_name = principal_name  # type: int
        self.remark = remark  # type: str
        self.renew_response = renew_response  # type: QueryTradeMarkApplicationsResponseBodyDataTmProducesRenewResponse
        self.service_price = service_price  # type: float
        self.show_go_to_defend_button = show_go_to_defend_button  # type: bool
        self.specification = specification  # type: int
        self.status = status  # type: int
        self.submit_audit_time = submit_audit_time  # type: long
        self.submit_time = submit_time  # type: long
        self.supplement_id = supplement_id  # type: long
        self.supplement_status = supplement_status  # type: int
        self.system_version = system_version  # type: str
        self.third_classification = third_classification  # type: QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassification
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_number = tm_number  # type: str
        self.total_price = total_price  # type: float
        self.type = type  # type: int
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        if self.first_classification:
            self.first_classification.validate()
        if self.flags:
            self.flags.validate()
        if self.renew_response:
            self.renew_response.validate()
        if self.third_classification:
            self.third_classification.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBodyDataTmProduces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_id is not None:
            result['AgreementId'] = self.agreement_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.flags is not None:
            result['Flags'] = self.flags.to_map()
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.note is not None:
            result['Note'] = self.note
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.renew_response is not None:
            result['RenewResponse'] = self.renew_response.to_map()
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.show_go_to_defend_button is not None:
            result['ShowGoToDefendButton'] = self.show_go_to_defend_button
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_audit_time is not None:
            result['SubmitAuditTime'] = self.submit_audit_time
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgreementId') is not None:
            self.agreement_id = m.get('AgreementId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FirstClassification') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('Flags') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesFlags()
            self.flags = temp_model.from_map(m['Flags'])
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RenewResponse') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesRenewResponse()
            self.renew_response = temp_model.from_map(m['RenewResponse'])
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('ShowGoToDefendButton') is not None:
            self.show_go_to_defend_button = m.get('ShowGoToDefendButton')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitAuditTime') is not None:
            self.submit_audit_time = m.get('SubmitAuditTime')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('ThirdClassification') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTradeMarkApplicationsResponseBodyData(TeaModel):
    def __init__(self, tm_produces=None):
        self.tm_produces = tm_produces  # type: list[QueryTradeMarkApplicationsResponseBodyDataTmProduces]

    def validate(self):
        if self.tm_produces:
            for k in self.tm_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmProduces'] = []
        if self.tm_produces is not None:
            for k in self.tm_produces:
                result['TmProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tm_produces = []
        if m.get('TmProduces') is not None:
            for k in m.get('TmProduces'):
                temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProduces()
                self.tm_produces.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryTradeMarkApplicationsResponseBodyData
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTradeMarkApplicationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTradeMarkApplicationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsResponse, self).to_map()
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
            temp_model = QueryTradeMarkApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationsByIntentionRequest(TeaModel):
    def __init__(self, channel=None, intention_biz_id=None, page_num=None, page_size=None, tm_produce_status=None):
        self.channel = channel  # type: str
        self.intention_biz_id = intention_biz_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.tm_produce_status = tm_produce_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tm_produce_status is not None:
            result['TmProduceStatus'] = self.tm_produce_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TmProduceStatus') is not None:
            self.tm_produce_status = m.get('TmProduceStatus')
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesFirstClassification(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesFirstClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassificationThirdClassifications(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassificationThirdClassifications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassification(TeaModel):
    def __init__(self, third_classifications=None):
        self.third_classifications = third_classifications  # type: list[QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassificationThirdClassifications]

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProduces(TeaModel):
    def __init__(self, biz_id=None, create_time=None, first_classification=None, loa_url=None, material_id=None,
                 material_name=None, note=None, order_price=None, principal_description=None, principal_value=None,
                 service_price=None, status=None, supplement_id=None, supplement_status=None, third_classification=None,
                 tm_icon=None, tm_name=None, tm_number=None, total_price=None, type=None, update_time=None):
        self.biz_id = biz_id  # type: str
        self.create_time = create_time  # type: long
        self.first_classification = first_classification  # type: QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesFirstClassification
        self.loa_url = loa_url  # type: str
        self.material_id = material_id  # type: str
        self.material_name = material_name  # type: str
        self.note = note  # type: str
        self.order_price = order_price  # type: float
        self.principal_description = principal_description  # type: str
        self.principal_value = principal_value  # type: int
        self.service_price = service_price  # type: float
        self.status = status  # type: int
        self.supplement_id = supplement_id  # type: long
        self.supplement_status = supplement_status  # type: int
        self.third_classification = third_classification  # type: QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassification
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_number = tm_number  # type: str
        self.total_price = total_price  # type: float
        self.type = type  # type: int
        self.update_time = update_time  # type: long

    def validate(self):
        if self.first_classification:
            self.first_classification.validate()
        if self.third_classification:
            self.third_classification.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProduces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.note is not None:
            result['Note'] = self.note
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.principal_value is not None:
            result['PrincipalValue'] = self.principal_value
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.status is not None:
            result['Status'] = self.status
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FirstClassification') is not None:
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('PrincipalValue') is not None:
            self.principal_value = m.get('PrincipalValue')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('ThirdClassification') is not None:
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyData(TeaModel):
    def __init__(self, tm_produces=None):
        self.tm_produces = tm_produces  # type: list[QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProduces]

    def validate(self):
        if self.tm_produces:
            for k in self.tm_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmProduces'] = []
        if self.tm_produces is not None:
            for k in self.tm_produces:
                result['TmProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tm_produces = []
        if m.get('TmProduces') is not None:
            for k in m.get('TmProduces'):
                temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProduces()
                self.tm_produces.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsByIntentionResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryTradeMarkApplicationsByIntentionResponseBodyData
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTradeMarkApplicationsByIntentionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTradeMarkApplicationsByIntentionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTradeMarkApplicationsByIntentionResponse, self).to_map()
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
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeProduceDetailRequest(TeaModel):
    def __init__(self, biz_id=None):
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeProduceDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryTradeProduceDetailResponseBodyData(TeaModel):
    def __init__(self, allow_cancel=None, biz_id=None, buyer_status=None, classification=None,
                 confiscate_amount=None, create_time=None, exclusive_date_limit=None, extend=None, final_amount=None, icon=None,
                 operate_note=None, paid_amount=None, pre_amount=None, pre_order_id=None, refund_amount=None,
                 register_number=None, share=None, source=None, third_code=None, tm_name=None, update_time=None, user_id=None):
        self.allow_cancel = allow_cancel  # type: bool
        self.biz_id = biz_id  # type: str
        self.buyer_status = buyer_status  # type: int
        self.classification = classification  # type: str
        self.confiscate_amount = confiscate_amount  # type: float
        self.create_time = create_time  # type: long
        self.exclusive_date_limit = exclusive_date_limit  # type: str
        self.extend = extend  # type: dict[str, any]
        self.final_amount = final_amount  # type: float
        self.icon = icon  # type: str
        self.operate_note = operate_note  # type: str
        self.paid_amount = paid_amount  # type: float
        self.pre_amount = pre_amount  # type: float
        self.pre_order_id = pre_order_id  # type: str
        self.refund_amount = refund_amount  # type: float
        self.register_number = register_number  # type: str
        self.share = share  # type: str
        self.source = source  # type: int
        self.third_code = third_code  # type: str
        self.tm_name = tm_name  # type: str
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeProduceDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_cancel is not None:
            result['AllowCancel'] = self.allow_cancel
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.buyer_status is not None:
            result['BuyerStatus'] = self.buyer_status
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.confiscate_amount is not None:
            result['ConfiscateAmount'] = self.confiscate_amount
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.exclusive_date_limit is not None:
            result['ExclusiveDateLimit'] = self.exclusive_date_limit
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.final_amount is not None:
            result['FinalAmount'] = self.final_amount
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.operate_note is not None:
            result['OperateNote'] = self.operate_note
        if self.paid_amount is not None:
            result['PaidAmount'] = self.paid_amount
        if self.pre_amount is not None:
            result['PreAmount'] = self.pre_amount
        if self.pre_order_id is not None:
            result['PreOrderId'] = self.pre_order_id
        if self.refund_amount is not None:
            result['RefundAmount'] = self.refund_amount
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.share is not None:
            result['Share'] = self.share
        if self.source is not None:
            result['Source'] = self.source
        if self.third_code is not None:
            result['ThirdCode'] = self.third_code
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowCancel') is not None:
            self.allow_cancel = m.get('AllowCancel')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BuyerStatus') is not None:
            self.buyer_status = m.get('BuyerStatus')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('ConfiscateAmount') is not None:
            self.confiscate_amount = m.get('ConfiscateAmount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExclusiveDateLimit') is not None:
            self.exclusive_date_limit = m.get('ExclusiveDateLimit')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('FinalAmount') is not None:
            self.final_amount = m.get('FinalAmount')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('OperateNote') is not None:
            self.operate_note = m.get('OperateNote')
        if m.get('PaidAmount') is not None:
            self.paid_amount = m.get('PaidAmount')
        if m.get('PreAmount') is not None:
            self.pre_amount = m.get('PreAmount')
        if m.get('PreOrderId') is not None:
            self.pre_order_id = m.get('PreOrderId')
        if m.get('RefundAmount') is not None:
            self.refund_amount = m.get('RefundAmount')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Share') is not None:
            self.share = m.get('Share')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('ThirdCode') is not None:
            self.third_code = m.get('ThirdCode')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTradeProduceDetailResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: QueryTradeProduceDetailResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTradeProduceDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryTradeProduceDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTradeProduceDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTradeProduceDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTradeProduceDetailResponse, self).to_map()
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
            temp_model = QueryTradeProduceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeProduceListRequest(TeaModel):
    def __init__(self, biz_id=None, buyer_status=None, page_num=None, page_size=None, pre_order_id=None,
                 register_number=None, sort_filed=None, sort_order=None):
        self.biz_id = biz_id  # type: str
        self.buyer_status = buyer_status  # type: int
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.pre_order_id = pre_order_id  # type: str
        self.register_number = register_number  # type: str
        self.sort_filed = sort_filed  # type: str
        self.sort_order = sort_order  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeProduceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.buyer_status is not None:
            result['BuyerStatus'] = self.buyer_status
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_order_id is not None:
            result['PreOrderId'] = self.pre_order_id
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BuyerStatus') is not None:
            self.buyer_status = m.get('BuyerStatus')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PreOrderId') is not None:
            self.pre_order_id = m.get('PreOrderId')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class QueryTradeProduceListResponseBodyDataTradeProduces(TeaModel):
    def __init__(self, allow_cancel=None, biz_id=None, buyer_status=None, classification=None, create_time=None,
                 fail_reason=None, final_amount=None, icon=None, operate_note=None, pre_amount=None, pre_order_id=None,
                 register_number=None, source=None, update_time=None, user_id=None):
        self.allow_cancel = allow_cancel  # type: bool
        self.biz_id = biz_id  # type: str
        self.buyer_status = buyer_status  # type: int
        self.classification = classification  # type: str
        self.create_time = create_time  # type: long
        self.fail_reason = fail_reason  # type: int
        self.final_amount = final_amount  # type: float
        self.icon = icon  # type: str
        self.operate_note = operate_note  # type: str
        self.pre_amount = pre_amount  # type: float
        self.pre_order_id = pre_order_id  # type: str
        self.register_number = register_number  # type: str
        self.source = source  # type: int
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTradeProduceListResponseBodyDataTradeProduces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_cancel is not None:
            result['AllowCancel'] = self.allow_cancel
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.buyer_status is not None:
            result['BuyerStatus'] = self.buyer_status
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.final_amount is not None:
            result['FinalAmount'] = self.final_amount
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.operate_note is not None:
            result['OperateNote'] = self.operate_note
        if self.pre_amount is not None:
            result['PreAmount'] = self.pre_amount
        if self.pre_order_id is not None:
            result['PreOrderId'] = self.pre_order_id
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.source is not None:
            result['Source'] = self.source
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowCancel') is not None:
            self.allow_cancel = m.get('AllowCancel')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BuyerStatus') is not None:
            self.buyer_status = m.get('BuyerStatus')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('FinalAmount') is not None:
            self.final_amount = m.get('FinalAmount')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('OperateNote') is not None:
            self.operate_note = m.get('OperateNote')
        if m.get('PreAmount') is not None:
            self.pre_amount = m.get('PreAmount')
        if m.get('PreOrderId') is not None:
            self.pre_order_id = m.get('PreOrderId')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTradeProduceListResponseBodyData(TeaModel):
    def __init__(self, trade_produces=None):
        self.trade_produces = trade_produces  # type: list[QueryTradeProduceListResponseBodyDataTradeProduces]

    def validate(self):
        if self.trade_produces:
            for k in self.trade_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTradeProduceListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TradeProduces'] = []
        if self.trade_produces is not None:
            for k in self.trade_produces:
                result['TradeProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.trade_produces = []
        if m.get('TradeProduces') is not None:
            for k in m.get('TradeProduces'):
                temp_model = QueryTradeProduceListResponseBodyDataTradeProduces()
                self.trade_produces.append(temp_model.from_map(k))
        return self


class QueryTradeProduceListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, page_size=None, request_id=None, total_item_num=None,
                 total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryTradeProduceListResponseBodyData
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTradeProduceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeProduceListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTradeProduceListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTradeProduceListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTradeProduceListResponse, self).to_map()
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
            temp_model = QueryTradeProduceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkDetailByApplyNumberRequest(TeaModel):
    def __init__(self, apply_number=None, env=None):
        self.apply_number = apply_number  # type: str
        self.env = env  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_number is not None:
            result['ApplyNumber'] = self.apply_number
        if self.env is not None:
            result['Env'] = self.env
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyNumber') is not None:
            self.apply_number = m.get('ApplyNumber')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        return self


class QueryTrademarkDetailByApplyNumberResponseBodyMoudleLeafCodesLeafCode(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberResponseBodyMoudleLeafCodesLeafCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTrademarkDetailByApplyNumberResponseBodyMoudleLeafCodes(TeaModel):
    def __init__(self, leaf_code=None):
        self.leaf_code = leaf_code  # type: list[QueryTrademarkDetailByApplyNumberResponseBodyMoudleLeafCodesLeafCode]

    def validate(self):
        if self.leaf_code:
            for k in self.leaf_code:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberResponseBodyMoudleLeafCodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['leafCode'] = []
        if self.leaf_code is not None:
            for k in self.leaf_code:
                result['leafCode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.leaf_code = []
        if m.get('leafCode') is not None:
            for k in m.get('leafCode'):
                temp_model = QueryTrademarkDetailByApplyNumberResponseBodyMoudleLeafCodesLeafCode()
                self.leaf_code.append(temp_model.from_map(k))
        return self


class QueryTrademarkDetailByApplyNumberResponseBodyMoudleMaterialInfo(TeaModel):
    def __init__(self, address=None, business_licence_url=None, card_number=None, cn_info_url=None,
                 contact_address=None, contact_email=None, contact_name=None, contact_phone_number=None, contact_zip_code=None,
                 country=None, eaddress=None, ename=None, id_card_number=None, id_card_url=None, loa_key=None, loa_url=None,
                 name=None, passport_url=None, personal_type=None, post_code=None, province=None,
                 reason_file_oss_key=None, region=None, review_file_map=None, type=None):
        self.address = address  # type: str
        self.business_licence_url = business_licence_url  # type: str
        self.card_number = card_number  # type: str
        self.cn_info_url = cn_info_url  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_phone_number = contact_phone_number  # type: str
        self.contact_zip_code = contact_zip_code  # type: str
        self.country = country  # type: str
        self.eaddress = eaddress  # type: str
        self.ename = ename  # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_url = id_card_url  # type: str
        self.loa_key = loa_key  # type: str
        self.loa_url = loa_url  # type: str
        self.name = name  # type: str
        self.passport_url = passport_url  # type: str
        self.personal_type = personal_type  # type: int
        self.post_code = post_code  # type: str
        self.province = province  # type: str
        self.reason_file_oss_key = reason_file_oss_key  # type: str
        self.region = region  # type: int
        self.review_file_map = review_file_map  # type: dict[str, any]
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberResponseBodyMoudleMaterialInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_phone_number is not None:
            result['ContactPhoneNumber'] = self.contact_phone_number
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.post_code is not None:
            result['PostCode'] = self.post_code
        if self.province is not None:
            result['Province'] = self.province
        if self.reason_file_oss_key is not None:
            result['ReasonFileOssKey'] = self.reason_file_oss_key
        if self.region is not None:
            result['Region'] = self.region
        if self.review_file_map is not None:
            result['ReviewFileMap'] = self.review_file_map
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactPhoneNumber') is not None:
            self.contact_phone_number = m.get('ContactPhoneNumber')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ReasonFileOssKey') is not None:
            self.reason_file_oss_key = m.get('ReasonFileOssKey')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReviewFileMap') is not None:
            self.review_file_map = m.get('ReviewFileMap')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTrademarkDetailByApplyNumberResponseBodyMoudleRootCode(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberResponseBodyMoudleRootCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTrademarkDetailByApplyNumberResponseBodyMoudle(TeaModel):
    def __init__(self, bit_flag=None, biz_id=None, biz_type=None, extend_info=None, gray_icon_url=None, icon=None,
                 leaf_codes=None, material_info=None, order_id=None, partner_code=None, principal_key=None,
                 principal_name=None, produce_type=None, root_code=None, status=None, status_str=None, submit_audit_time_str=None,
                 submit_audit_time_value=None, submit_status=None, submit_time_str=None, submit_time_value=None, submit_times=None,
                 trademark_name=None, trademark_name_type=None, trademark_number=None):
        self.bit_flag = bit_flag  # type: int
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.extend_info = extend_info  # type: dict[str, any]
        self.gray_icon_url = gray_icon_url  # type: str
        self.icon = icon  # type: str
        self.leaf_codes = leaf_codes  # type: QueryTrademarkDetailByApplyNumberResponseBodyMoudleLeafCodes
        self.material_info = material_info  # type: QueryTrademarkDetailByApplyNumberResponseBodyMoudleMaterialInfo
        self.order_id = order_id  # type: str
        self.partner_code = partner_code  # type: str
        self.principal_key = principal_key  # type: str
        self.principal_name = principal_name  # type: str
        self.produce_type = produce_type  # type: str
        self.root_code = root_code  # type: QueryTrademarkDetailByApplyNumberResponseBodyMoudleRootCode
        self.status = status  # type: str
        self.status_str = status_str  # type: str
        self.submit_audit_time_str = submit_audit_time_str  # type: str
        self.submit_audit_time_value = submit_audit_time_value  # type: long
        self.submit_status = submit_status  # type: str
        self.submit_time_str = submit_time_str  # type: str
        self.submit_time_value = submit_time_value  # type: long
        self.submit_times = submit_times  # type: int
        self.trademark_name = trademark_name  # type: str
        self.trademark_name_type = trademark_name_type  # type: int
        self.trademark_number = trademark_number  # type: str

    def validate(self):
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_info:
            self.material_info.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberResponseBodyMoudle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_flag is not None:
            result['BitFlag'] = self.bit_flag
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_str is not None:
            result['StatusStr'] = self.status_str
        if self.submit_audit_time_str is not None:
            result['SubmitAuditTimeStr'] = self.submit_audit_time_str
        if self.submit_audit_time_value is not None:
            result['SubmitAuditTimeValue'] = self.submit_audit_time_value
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time_str is not None:
            result['SubmitTimeStr'] = self.submit_time_str
        if self.submit_time_value is not None:
            result['SubmitTimeValue'] = self.submit_time_value
        if self.submit_times is not None:
            result['SubmitTimes'] = self.submit_times
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BitFlag') is not None:
            self.bit_flag = m.get('BitFlag')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LeafCodes') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberResponseBodyMoudleLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('MaterialInfo') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberResponseBodyMoudleMaterialInfo()
            self.material_info = temp_model.from_map(m['MaterialInfo'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        if m.get('RootCode') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberResponseBodyMoudleRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusStr') is not None:
            self.status_str = m.get('StatusStr')
        if m.get('SubmitAuditTimeStr') is not None:
            self.submit_audit_time_str = m.get('SubmitAuditTimeStr')
        if m.get('SubmitAuditTimeValue') is not None:
            self.submit_audit_time_value = m.get('SubmitAuditTimeValue')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTimeStr') is not None:
            self.submit_time_str = m.get('SubmitTimeStr')
        if m.get('SubmitTimeValue') is not None:
            self.submit_time_value = m.get('SubmitTimeValue')
        if m.get('SubmitTimes') is not None:
            self.submit_times = m.get('SubmitTimes')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        return self


class QueryTrademarkDetailByApplyNumberResponseBody(TeaModel):
    def __init__(self, moudle=None, request_id=None):
        self.moudle = moudle  # type: QueryTrademarkDetailByApplyNumberResponseBodyMoudle
        self.request_id = request_id  # type: str

    def validate(self):
        if self.moudle:
            self.moudle.validate()

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.moudle is not None:
            result['Moudle'] = self.moudle.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Moudle') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberResponseBodyMoudle()
            self.moudle = temp_model.from_map(m['Moudle'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTrademarkDetailByApplyNumberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTrademarkDetailByApplyNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberResponse, self).to_map()
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
            temp_model = QueryTrademarkDetailByApplyNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkDetailByApplyNumberEspRequest(TeaModel):
    def __init__(self, apply_number=None, biz_type=None):
        self.apply_number = apply_number  # type: str
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberEspRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_number is not None:
            result['ApplyNumber'] = self.apply_number
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyNumber') is not None:
            self.apply_number = m.get('ApplyNumber')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleLeafCodesLeafCode(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleLeafCodesLeafCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleLeafCodes(TeaModel):
    def __init__(self, leaf_code=None):
        self.leaf_code = leaf_code  # type: list[QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleLeafCodesLeafCode]

    def validate(self):
        if self.leaf_code:
            for k in self.leaf_code:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleLeafCodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['leafCode'] = []
        if self.leaf_code is not None:
            for k in self.leaf_code:
                result['leafCode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.leaf_code = []
        if m.get('leafCode') is not None:
            for k in m.get('leafCode'):
                temp_model = QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleLeafCodesLeafCode()
                self.leaf_code.append(temp_model.from_map(k))
        return self


class QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleMaterialInfo(TeaModel):
    def __init__(self, address=None, business_licence_url=None, card_number=None, cn_info_url=None,
                 contact_address=None, contact_email=None, contact_name=None, contact_phone_number=None, contact_zip_code=None,
                 country=None, eaddress=None, ename=None, id_card_number=None, id_card_url=None, loa_key=None, loa_url=None,
                 name=None, passport_url=None, personal_type=None, post_code=None, province=None,
                 reason_file_oss_key=None, region=None, review_file_map=None, type=None):
        self.address = address  # type: str
        self.business_licence_url = business_licence_url  # type: str
        self.card_number = card_number  # type: str
        self.cn_info_url = cn_info_url  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_phone_number = contact_phone_number  # type: str
        self.contact_zip_code = contact_zip_code  # type: str
        self.country = country  # type: str
        self.eaddress = eaddress  # type: str
        self.ename = ename  # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_url = id_card_url  # type: str
        self.loa_key = loa_key  # type: str
        self.loa_url = loa_url  # type: str
        self.name = name  # type: str
        self.passport_url = passport_url  # type: str
        self.personal_type = personal_type  # type: int
        self.post_code = post_code  # type: str
        self.province = province  # type: str
        self.reason_file_oss_key = reason_file_oss_key  # type: str
        self.region = region  # type: int
        self.review_file_map = review_file_map  # type: dict[str, any]
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleMaterialInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_phone_number is not None:
            result['ContactPhoneNumber'] = self.contact_phone_number
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.post_code is not None:
            result['PostCode'] = self.post_code
        if self.province is not None:
            result['Province'] = self.province
        if self.reason_file_oss_key is not None:
            result['ReasonFileOssKey'] = self.reason_file_oss_key
        if self.region is not None:
            result['Region'] = self.region
        if self.review_file_map is not None:
            result['ReviewFileMap'] = self.review_file_map
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactPhoneNumber') is not None:
            self.contact_phone_number = m.get('ContactPhoneNumber')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ReasonFileOssKey') is not None:
            self.reason_file_oss_key = m.get('ReasonFileOssKey')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReviewFileMap') is not None:
            self.review_file_map = m.get('ReviewFileMap')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleRootCode(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleRootCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTrademarkDetailByApplyNumberEspResponseBodyMoudle(TeaModel):
    def __init__(self, bit_flag=None, biz_id=None, biz_type=None, extend_info=None, gray_icon_url=None, icon=None,
                 leaf_codes=None, material_info=None, order_id=None, partner_code=None, principal_key=None,
                 principal_name=None, produce_type=None, root_code=None, status=None, status_str=None, submit_audit_time_str=None,
                 submit_audit_time_value=None, submit_status=None, submit_time_str=None, submit_time_value=None, submit_times=None,
                 trademark_name=None, trademark_name_type=None, trademark_number=None):
        self.bit_flag = bit_flag  # type: int
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.extend_info = extend_info  # type: dict[str, any]
        self.gray_icon_url = gray_icon_url  # type: str
        self.icon = icon  # type: str
        self.leaf_codes = leaf_codes  # type: QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleLeafCodes
        self.material_info = material_info  # type: QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleMaterialInfo
        self.order_id = order_id  # type: str
        self.partner_code = partner_code  # type: str
        self.principal_key = principal_key  # type: str
        self.principal_name = principal_name  # type: str
        self.produce_type = produce_type  # type: str
        self.root_code = root_code  # type: QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleRootCode
        self.status = status  # type: str
        self.status_str = status_str  # type: str
        self.submit_audit_time_str = submit_audit_time_str  # type: str
        self.submit_audit_time_value = submit_audit_time_value  # type: long
        self.submit_status = submit_status  # type: str
        self.submit_time_str = submit_time_str  # type: str
        self.submit_time_value = submit_time_value  # type: long
        self.submit_times = submit_times  # type: int
        self.trademark_name = trademark_name  # type: str
        self.trademark_name_type = trademark_name_type  # type: int
        self.trademark_number = trademark_number  # type: str

    def validate(self):
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_info:
            self.material_info.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberEspResponseBodyMoudle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_flag is not None:
            result['BitFlag'] = self.bit_flag
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_str is not None:
            result['StatusStr'] = self.status_str
        if self.submit_audit_time_str is not None:
            result['SubmitAuditTimeStr'] = self.submit_audit_time_str
        if self.submit_audit_time_value is not None:
            result['SubmitAuditTimeValue'] = self.submit_audit_time_value
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time_str is not None:
            result['SubmitTimeStr'] = self.submit_time_str
        if self.submit_time_value is not None:
            result['SubmitTimeValue'] = self.submit_time_value
        if self.submit_times is not None:
            result['SubmitTimes'] = self.submit_times
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BitFlag') is not None:
            self.bit_flag = m.get('BitFlag')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LeafCodes') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('MaterialInfo') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleMaterialInfo()
            self.material_info = temp_model.from_map(m['MaterialInfo'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        if m.get('RootCode') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberEspResponseBodyMoudleRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusStr') is not None:
            self.status_str = m.get('StatusStr')
        if m.get('SubmitAuditTimeStr') is not None:
            self.submit_audit_time_str = m.get('SubmitAuditTimeStr')
        if m.get('SubmitAuditTimeValue') is not None:
            self.submit_audit_time_value = m.get('SubmitAuditTimeValue')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTimeStr') is not None:
            self.submit_time_str = m.get('SubmitTimeStr')
        if m.get('SubmitTimeValue') is not None:
            self.submit_time_value = m.get('SubmitTimeValue')
        if m.get('SubmitTimes') is not None:
            self.submit_times = m.get('SubmitTimes')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        return self


class QueryTrademarkDetailByApplyNumberEspResponseBody(TeaModel):
    def __init__(self, moudle=None, request_id=None):
        self.moudle = moudle  # type: QueryTrademarkDetailByApplyNumberEspResponseBodyMoudle
        self.request_id = request_id  # type: str

    def validate(self):
        if self.moudle:
            self.moudle.validate()

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberEspResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.moudle is not None:
            result['Moudle'] = self.moudle.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Moudle') is not None:
            temp_model = QueryTrademarkDetailByApplyNumberEspResponseBodyMoudle()
            self.moudle = temp_model.from_map(m['Moudle'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTrademarkDetailByApplyNumberEspResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTrademarkDetailByApplyNumberEspResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTrademarkDetailByApplyNumberEspResponse, self).to_map()
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
            temp_model = QueryTrademarkDetailByApplyNumberEspResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkModelDetailRequest(TeaModel):
    def __init__(self, biz_id=None, env=None, order_id=None, review_supplement_material=None):
        self.biz_id = biz_id  # type: str
        self.env = env  # type: str
        self.order_id = order_id  # type: str
        self.review_supplement_material = review_supplement_material  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.env is not None:
            result['Env'] = self.env
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.review_supplement_material is not None:
            result['ReviewSupplementMaterial'] = self.review_supplement_material
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ReviewSupplementMaterial') is not None:
            self.review_supplement_material = m.get('ReviewSupplementMaterial')
        return self


class QueryTrademarkModelDetailResponseBodyMoudleLeafCodesLeafCode(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelDetailResponseBodyMoudleLeafCodesLeafCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTrademarkModelDetailResponseBodyMoudleLeafCodes(TeaModel):
    def __init__(self, leaf_code=None):
        self.leaf_code = leaf_code  # type: list[QueryTrademarkModelDetailResponseBodyMoudleLeafCodesLeafCode]

    def validate(self):
        if self.leaf_code:
            for k in self.leaf_code:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelDetailResponseBodyMoudleLeafCodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['leafCode'] = []
        if self.leaf_code is not None:
            for k in self.leaf_code:
                result['leafCode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.leaf_code = []
        if m.get('leafCode') is not None:
            for k in m.get('leafCode'):
                temp_model = QueryTrademarkModelDetailResponseBodyMoudleLeafCodesLeafCode()
                self.leaf_code.append(temp_model.from_map(k))
        return self


class QueryTrademarkModelDetailResponseBodyMoudleMaterialInfo(TeaModel):
    def __init__(self, address=None, business_licence_url=None, card_number=None, cn_info_url=None,
                 contact_address=None, contact_email=None, contact_name=None, contact_phone_number=None, contact_zip_code=None,
                 country=None, eaddress=None, ename=None, id_card_number=None, id_card_url=None, loa_key=None, loa_url=None,
                 name=None, passport_url=None, personal_type=None, post_code=None, province=None,
                 reason_file_oss_key=None, region=None, review_file_map=None, type=None):
        self.address = address  # type: str
        self.business_licence_url = business_licence_url  # type: str
        self.card_number = card_number  # type: str
        self.cn_info_url = cn_info_url  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_phone_number = contact_phone_number  # type: str
        self.contact_zip_code = contact_zip_code  # type: str
        self.country = country  # type: str
        self.eaddress = eaddress  # type: str
        self.ename = ename  # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_url = id_card_url  # type: str
        self.loa_key = loa_key  # type: str
        self.loa_url = loa_url  # type: str
        self.name = name  # type: str
        self.passport_url = passport_url  # type: str
        self.personal_type = personal_type  # type: int
        self.post_code = post_code  # type: str
        self.province = province  # type: str
        self.reason_file_oss_key = reason_file_oss_key  # type: str
        self.region = region  # type: int
        self.review_file_map = review_file_map  # type: dict[str, any]
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelDetailResponseBodyMoudleMaterialInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_phone_number is not None:
            result['ContactPhoneNumber'] = self.contact_phone_number
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.post_code is not None:
            result['PostCode'] = self.post_code
        if self.province is not None:
            result['Province'] = self.province
        if self.reason_file_oss_key is not None:
            result['ReasonFileOssKey'] = self.reason_file_oss_key
        if self.region is not None:
            result['Region'] = self.region
        if self.review_file_map is not None:
            result['ReviewFileMap'] = self.review_file_map
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactPhoneNumber') is not None:
            self.contact_phone_number = m.get('ContactPhoneNumber')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ReasonFileOssKey') is not None:
            self.reason_file_oss_key = m.get('ReasonFileOssKey')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReviewFileMap') is not None:
            self.review_file_map = m.get('ReviewFileMap')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTrademarkModelDetailResponseBodyMoudleRootCode(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelDetailResponseBodyMoudleRootCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTrademarkModelDetailResponseBodyMoudle(TeaModel):
    def __init__(self, bit_flag=None, biz_id=None, biz_type=None, extend_info=None, gray_icon_url=None, icon=None,
                 leaf_codes=None, material_info=None, order_id=None, partner_code=None, principal_key=None,
                 principal_name=None, produce_type=None, request_id=None, root_code=None, status=None, status_str=None,
                 submit_audit_time_str=None, submit_audit_time_value=None, submit_status=None, submit_time_str=None,
                 submit_time_value=None, submit_times=None, trademark_name=None, trademark_name_type=None, trademark_number=None):
        self.bit_flag = bit_flag  # type: int
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.extend_info = extend_info  # type: dict[str, any]
        self.gray_icon_url = gray_icon_url  # type: str
        self.icon = icon  # type: str
        self.leaf_codes = leaf_codes  # type: QueryTrademarkModelDetailResponseBodyMoudleLeafCodes
        self.material_info = material_info  # type: QueryTrademarkModelDetailResponseBodyMoudleMaterialInfo
        self.order_id = order_id  # type: str
        self.partner_code = partner_code  # type: str
        self.principal_key = principal_key  # type: str
        self.principal_name = principal_name  # type: str
        self.produce_type = produce_type  # type: str
        self.request_id = request_id  # type: str
        self.root_code = root_code  # type: QueryTrademarkModelDetailResponseBodyMoudleRootCode
        self.status = status  # type: str
        self.status_str = status_str  # type: str
        self.submit_audit_time_str = submit_audit_time_str  # type: str
        self.submit_audit_time_value = submit_audit_time_value  # type: long
        self.submit_status = submit_status  # type: str
        self.submit_time_str = submit_time_str  # type: str
        self.submit_time_value = submit_time_value  # type: long
        self.submit_times = submit_times  # type: int
        self.trademark_name = trademark_name  # type: str
        self.trademark_name_type = trademark_name_type  # type: int
        self.trademark_number = trademark_number  # type: str

    def validate(self):
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_info:
            self.material_info.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelDetailResponseBodyMoudle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_flag is not None:
            result['BitFlag'] = self.bit_flag
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_str is not None:
            result['StatusStr'] = self.status_str
        if self.submit_audit_time_str is not None:
            result['SubmitAuditTimeStr'] = self.submit_audit_time_str
        if self.submit_audit_time_value is not None:
            result['SubmitAuditTimeValue'] = self.submit_audit_time_value
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time_str is not None:
            result['SubmitTimeStr'] = self.submit_time_str
        if self.submit_time_value is not None:
            result['SubmitTimeValue'] = self.submit_time_value
        if self.submit_times is not None:
            result['SubmitTimes'] = self.submit_times
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BitFlag') is not None:
            self.bit_flag = m.get('BitFlag')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LeafCodes') is not None:
            temp_model = QueryTrademarkModelDetailResponseBodyMoudleLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('MaterialInfo') is not None:
            temp_model = QueryTrademarkModelDetailResponseBodyMoudleMaterialInfo()
            self.material_info = temp_model.from_map(m['MaterialInfo'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootCode') is not None:
            temp_model = QueryTrademarkModelDetailResponseBodyMoudleRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusStr') is not None:
            self.status_str = m.get('StatusStr')
        if m.get('SubmitAuditTimeStr') is not None:
            self.submit_audit_time_str = m.get('SubmitAuditTimeStr')
        if m.get('SubmitAuditTimeValue') is not None:
            self.submit_audit_time_value = m.get('SubmitAuditTimeValue')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTimeStr') is not None:
            self.submit_time_str = m.get('SubmitTimeStr')
        if m.get('SubmitTimeValue') is not None:
            self.submit_time_value = m.get('SubmitTimeValue')
        if m.get('SubmitTimes') is not None:
            self.submit_times = m.get('SubmitTimes')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        return self


class QueryTrademarkModelDetailResponseBody(TeaModel):
    def __init__(self, moudle=None):
        self.moudle = moudle  # type: QueryTrademarkModelDetailResponseBodyMoudle

    def validate(self):
        if self.moudle:
            self.moudle.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.moudle is not None:
            result['Moudle'] = self.moudle.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Moudle') is not None:
            temp_model = QueryTrademarkModelDetailResponseBodyMoudle()
            self.moudle = temp_model.from_map(m['Moudle'])
        return self


class QueryTrademarkModelDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTrademarkModelDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelDetailResponse, self).to_map()
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
            temp_model = QueryTrademarkModelDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkModelEspDetailRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelEspDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class QueryTrademarkModelEspDetailResponseBodyMoudleLeafCodesLeafCode(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelEspDetailResponseBodyMoudleLeafCodesLeafCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTrademarkModelEspDetailResponseBodyMoudleLeafCodes(TeaModel):
    def __init__(self, leaf_code=None):
        self.leaf_code = leaf_code  # type: list[QueryTrademarkModelEspDetailResponseBodyMoudleLeafCodesLeafCode]

    def validate(self):
        if self.leaf_code:
            for k in self.leaf_code:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelEspDetailResponseBodyMoudleLeafCodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['leafCode'] = []
        if self.leaf_code is not None:
            for k in self.leaf_code:
                result['leafCode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.leaf_code = []
        if m.get('leafCode') is not None:
            for k in m.get('leafCode'):
                temp_model = QueryTrademarkModelEspDetailResponseBodyMoudleLeafCodesLeafCode()
                self.leaf_code.append(temp_model.from_map(k))
        return self


class QueryTrademarkModelEspDetailResponseBodyMoudleMaterialInfo(TeaModel):
    def __init__(self, address=None, business_licence_url=None, card_number=None, cn_info_url=None,
                 contact_address=None, contact_email=None, contact_zip_code=None, country=None, eaddress=None, ename=None,
                 id_card_number=None, id_card_url=None, loa_key=None, loa_url=None, name=None, passport_url=None,
                 personal_type=None, post_code=None, province=None, reason_file_oss_key=None, region=None, type=None):
        self.address = address  # type: str
        self.business_licence_url = business_licence_url  # type: str
        self.card_number = card_number  # type: str
        self.cn_info_url = cn_info_url  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_zip_code = contact_zip_code  # type: str
        self.country = country  # type: str
        self.eaddress = eaddress  # type: str
        self.ename = ename  # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_url = id_card_url  # type: str
        self.loa_key = loa_key  # type: str
        self.loa_url = loa_url  # type: str
        self.name = name  # type: str
        self.passport_url = passport_url  # type: str
        self.personal_type = personal_type  # type: str
        self.post_code = post_code  # type: str
        self.province = province  # type: str
        self.reason_file_oss_key = reason_file_oss_key  # type: str
        self.region = region  # type: int
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelEspDetailResponseBodyMoudleMaterialInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.post_code is not None:
            result['PostCode'] = self.post_code
        if self.province is not None:
            result['Province'] = self.province
        if self.reason_file_oss_key is not None:
            result['ReasonFileOssKey'] = self.reason_file_oss_key
        if self.region is not None:
            result['Region'] = self.region
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ReasonFileOssKey') is not None:
            self.reason_file_oss_key = m.get('ReasonFileOssKey')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTrademarkModelEspDetailResponseBodyMoudleRootCode(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelEspDetailResponseBodyMoudleRootCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTrademarkModelEspDetailResponseBodyMoudle(TeaModel):
    def __init__(self, bit_flag=None, biz_id=None, biz_type=None, extend_info=None, gray_icon_url=None, icon=None,
                 leaf_codes=None, material_info=None, order_id=None, partner_code=None, principal_key=None,
                 principal_name=None, produce_type=None, request_id=None, root_code=None, status=None, status_str=None,
                 submit_audit_time=None, submit_status=None, submit_time=None, submit_times=None, trademark_name=None,
                 trademark_name_type=None, trademark_number=None):
        self.bit_flag = bit_flag  # type: int
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.extend_info = extend_info  # type: dict[str, any]
        self.gray_icon_url = gray_icon_url  # type: str
        self.icon = icon  # type: str
        self.leaf_codes = leaf_codes  # type: QueryTrademarkModelEspDetailResponseBodyMoudleLeafCodes
        self.material_info = material_info  # type: QueryTrademarkModelEspDetailResponseBodyMoudleMaterialInfo
        self.order_id = order_id  # type: str
        self.partner_code = partner_code  # type: str
        self.principal_key = principal_key  # type: str
        self.principal_name = principal_name  # type: str
        self.produce_type = produce_type  # type: str
        self.request_id = request_id  # type: str
        self.root_code = root_code  # type: QueryTrademarkModelEspDetailResponseBodyMoudleRootCode
        self.status = status  # type: str
        self.status_str = status_str  # type: str
        self.submit_audit_time = submit_audit_time  # type: long
        self.submit_status = submit_status  # type: str
        self.submit_time = submit_time  # type: long
        self.submit_times = submit_times  # type: int
        self.trademark_name = trademark_name  # type: str
        self.trademark_name_type = trademark_name_type  # type: int
        self.trademark_number = trademark_number  # type: str

    def validate(self):
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_info:
            self.material_info.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelEspDetailResponseBodyMoudle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_flag is not None:
            result['BitFlag'] = self.bit_flag
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_str is not None:
            result['StatusStr'] = self.status_str
        if self.submit_audit_time is not None:
            result['SubmitAuditTime'] = self.submit_audit_time
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.submit_times is not None:
            result['SubmitTimes'] = self.submit_times
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BitFlag') is not None:
            self.bit_flag = m.get('BitFlag')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LeafCodes') is not None:
            temp_model = QueryTrademarkModelEspDetailResponseBodyMoudleLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('MaterialInfo') is not None:
            temp_model = QueryTrademarkModelEspDetailResponseBodyMoudleMaterialInfo()
            self.material_info = temp_model.from_map(m['MaterialInfo'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootCode') is not None:
            temp_model = QueryTrademarkModelEspDetailResponseBodyMoudleRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusStr') is not None:
            self.status_str = m.get('StatusStr')
        if m.get('SubmitAuditTime') is not None:
            self.submit_audit_time = m.get('SubmitAuditTime')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('SubmitTimes') is not None:
            self.submit_times = m.get('SubmitTimes')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        return self


class QueryTrademarkModelEspDetailResponseBody(TeaModel):
    def __init__(self, moudle=None):
        self.moudle = moudle  # type: QueryTrademarkModelEspDetailResponseBodyMoudle

    def validate(self):
        if self.moudle:
            self.moudle.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelEspDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.moudle is not None:
            result['Moudle'] = self.moudle.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Moudle') is not None:
            temp_model = QueryTrademarkModelEspDetailResponseBodyMoudle()
            self.moudle = temp_model.from_map(m['Moudle'])
        return self


class QueryTrademarkModelEspDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTrademarkModelEspDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelEspDetailResponse, self).to_map()
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
            temp_model = QueryTrademarkModelEspDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkModelEspListRequest(TeaModel):
    def __init__(self, additional_submit_status=None, additional_submit_time=None, biz_id=None, biz_type=None,
                 env=None, exist_status=None, order_id=None, order_ids_str=None, order_instance_id=None, page_num=None,
                 page_size=None, principal_key=None, principal_name=None, status=None, submit_status=None, submit_time=None):
        self.additional_submit_status = additional_submit_status  # type: str
        self.additional_submit_time = additional_submit_time  # type: str
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.env = env  # type: str
        self.exist_status = exist_status  # type: list[str]
        self.order_id = order_id  # type: str
        self.order_ids_str = order_ids_str  # type: str
        self.order_instance_id = order_instance_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.principal_key = principal_key  # type: str
        self.principal_name = principal_name  # type: str
        self.status = status  # type: str
        self.submit_status = submit_status  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelEspListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_submit_status is not None:
            result['AdditionalSubmitStatus'] = self.additional_submit_status
        if self.additional_submit_time is not None:
            result['AdditionalSubmitTime'] = self.additional_submit_time
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.env is not None:
            result['Env'] = self.env
        if self.exist_status is not None:
            result['ExistStatus'] = self.exist_status
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_ids_str is not None:
            result['OrderIdsStr'] = self.order_ids_str
        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdditionalSubmitStatus') is not None:
            self.additional_submit_status = m.get('AdditionalSubmitStatus')
        if m.get('AdditionalSubmitTime') is not None:
            self.additional_submit_time = m.get('AdditionalSubmitTime')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('ExistStatus') is not None:
            self.exist_status = m.get('ExistStatus')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderIdsStr') is not None:
            self.order_ids_str = m.get('OrderIdsStr')
        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class QueryTrademarkModelEspListShrinkRequest(TeaModel):
    def __init__(self, additional_submit_status=None, additional_submit_time=None, biz_id=None, biz_type=None,
                 env=None, exist_status_shrink=None, order_id=None, order_ids_str=None, order_instance_id=None,
                 page_num=None, page_size=None, principal_key=None, principal_name=None, status=None, submit_status=None,
                 submit_time=None):
        self.additional_submit_status = additional_submit_status  # type: str
        self.additional_submit_time = additional_submit_time  # type: str
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.env = env  # type: str
        self.exist_status_shrink = exist_status_shrink  # type: str
        self.order_id = order_id  # type: str
        self.order_ids_str = order_ids_str  # type: str
        self.order_instance_id = order_instance_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.principal_key = principal_key  # type: str
        self.principal_name = principal_name  # type: str
        self.status = status  # type: str
        self.submit_status = submit_status  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelEspListShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_submit_status is not None:
            result['AdditionalSubmitStatus'] = self.additional_submit_status
        if self.additional_submit_time is not None:
            result['AdditionalSubmitTime'] = self.additional_submit_time
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.env is not None:
            result['Env'] = self.env
        if self.exist_status_shrink is not None:
            result['ExistStatus'] = self.exist_status_shrink
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_ids_str is not None:
            result['OrderIdsStr'] = self.order_ids_str
        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdditionalSubmitStatus') is not None:
            self.additional_submit_status = m.get('AdditionalSubmitStatus')
        if m.get('AdditionalSubmitTime') is not None:
            self.additional_submit_time = m.get('AdditionalSubmitTime')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('ExistStatus') is not None:
            self.exist_status_shrink = m.get('ExistStatus')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderIdsStr') is not None:
            self.order_ids_str = m.get('OrderIdsStr')
        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class QueryTrademarkModelEspListResponseBodyMoudleDataItemLeafCodesLeafCode(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelEspListResponseBodyMoudleDataItemLeafCodesLeafCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTrademarkModelEspListResponseBodyMoudleDataItemLeafCodes(TeaModel):
    def __init__(self, leaf_code=None):
        self.leaf_code = leaf_code  # type: list[QueryTrademarkModelEspListResponseBodyMoudleDataItemLeafCodesLeafCode]

    def validate(self):
        if self.leaf_code:
            for k in self.leaf_code:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelEspListResponseBodyMoudleDataItemLeafCodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['leafCode'] = []
        if self.leaf_code is not None:
            for k in self.leaf_code:
                result['leafCode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.leaf_code = []
        if m.get('leafCode') is not None:
            for k in m.get('leafCode'):
                temp_model = QueryTrademarkModelEspListResponseBodyMoudleDataItemLeafCodesLeafCode()
                self.leaf_code.append(temp_model.from_map(k))
        return self


class QueryTrademarkModelEspListResponseBodyMoudleDataItemMaterialInfo(TeaModel):
    def __init__(self, address=None, business_licence_url=None, card_number=None, cn_info_url=None,
                 contact_address=None, contact_email=None, contact_zip_code=None, country=None, eaddress=None, ename=None,
                 id_card_number=None, id_card_url=None, loa_key=None, loa_url=None, name=None, passport_url=None,
                 personal_type=None, post_code=None, province=None, reason_file_oss_key=None, region=None, type=None):
        self.address = address  # type: str
        self.business_licence_url = business_licence_url  # type: str
        self.card_number = card_number  # type: str
        self.cn_info_url = cn_info_url  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_zip_code = contact_zip_code  # type: str
        self.country = country  # type: str
        self.eaddress = eaddress  # type: str
        self.ename = ename  # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_url = id_card_url  # type: str
        self.loa_key = loa_key  # type: str
        self.loa_url = loa_url  # type: str
        self.name = name  # type: str
        self.passport_url = passport_url  # type: str
        self.personal_type = personal_type  # type: str
        self.post_code = post_code  # type: str
        self.province = province  # type: str
        self.reason_file_oss_key = reason_file_oss_key  # type: str
        self.region = region  # type: int
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelEspListResponseBodyMoudleDataItemMaterialInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.post_code is not None:
            result['PostCode'] = self.post_code
        if self.province is not None:
            result['Province'] = self.province
        if self.reason_file_oss_key is not None:
            result['ReasonFileOssKey'] = self.reason_file_oss_key
        if self.region is not None:
            result['Region'] = self.region
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ReasonFileOssKey') is not None:
            self.reason_file_oss_key = m.get('ReasonFileOssKey')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTrademarkModelEspListResponseBodyMoudleDataItemRootCode(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelEspListResponseBodyMoudleDataItemRootCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTrademarkModelEspListResponseBodyMoudleDataItem(TeaModel):
    def __init__(self, bit_flag=None, biz_id=None, biz_type=None, extend_info=None, gray_icon_url=None, icon=None,
                 leaf_codes=None, material_info=None, order_id=None, partner_code=None, principal_key=None,
                 principal_name=None, produce_type=None, root_code=None, status=None, status_str=None, submit_audit_time=None,
                 submit_status=None, submit_time=None, submit_times=None, trademark_name=None, trademark_name_type=None,
                 trademark_number=None):
        self.bit_flag = bit_flag  # type: int
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.extend_info = extend_info  # type: dict[str, any]
        self.gray_icon_url = gray_icon_url  # type: str
        self.icon = icon  # type: str
        self.leaf_codes = leaf_codes  # type: QueryTrademarkModelEspListResponseBodyMoudleDataItemLeafCodes
        self.material_info = material_info  # type: QueryTrademarkModelEspListResponseBodyMoudleDataItemMaterialInfo
        self.order_id = order_id  # type: str
        self.partner_code = partner_code  # type: str
        self.principal_key = principal_key  # type: str
        self.principal_name = principal_name  # type: str
        self.produce_type = produce_type  # type: str
        self.root_code = root_code  # type: QueryTrademarkModelEspListResponseBodyMoudleDataItemRootCode
        self.status = status  # type: str
        self.status_str = status_str  # type: str
        self.submit_audit_time = submit_audit_time  # type: long
        self.submit_status = submit_status  # type: str
        self.submit_time = submit_time  # type: long
        self.submit_times = submit_times  # type: int
        self.trademark_name = trademark_name  # type: str
        self.trademark_name_type = trademark_name_type  # type: int
        self.trademark_number = trademark_number  # type: str

    def validate(self):
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_info:
            self.material_info.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelEspListResponseBodyMoudleDataItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_flag is not None:
            result['BitFlag'] = self.bit_flag
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_str is not None:
            result['StatusStr'] = self.status_str
        if self.submit_audit_time is not None:
            result['SubmitAuditTime'] = self.submit_audit_time
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.submit_times is not None:
            result['SubmitTimes'] = self.submit_times
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BitFlag') is not None:
            self.bit_flag = m.get('BitFlag')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LeafCodes') is not None:
            temp_model = QueryTrademarkModelEspListResponseBodyMoudleDataItemLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('MaterialInfo') is not None:
            temp_model = QueryTrademarkModelEspListResponseBodyMoudleDataItemMaterialInfo()
            self.material_info = temp_model.from_map(m['MaterialInfo'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        if m.get('RootCode') is not None:
            temp_model = QueryTrademarkModelEspListResponseBodyMoudleDataItemRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusStr') is not None:
            self.status_str = m.get('StatusStr')
        if m.get('SubmitAuditTime') is not None:
            self.submit_audit_time = m.get('SubmitAuditTime')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('SubmitTimes') is not None:
            self.submit_times = m.get('SubmitTimes')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        return self


class QueryTrademarkModelEspListResponseBodyMoudleData(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[QueryTrademarkModelEspListResponseBodyMoudleDataItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelEspListResponseBodyMoudleData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['item'] = []
        if self.item is not None:
            for k in self.item:
                result['item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('item') is not None:
            for k in m.get('item'):
                temp_model = QueryTrademarkModelEspListResponseBodyMoudleDataItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryTrademarkModelEspListResponseBodyMoudle(TeaModel):
    def __init__(self, data=None, request_id=None, total_page_num=None):
        self.data = data  # type: QueryTrademarkModelEspListResponseBodyMoudleData
        self.request_id = request_id  # type: str
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelEspListResponseBodyMoudle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryTrademarkModelEspListResponseBodyMoudleData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTrademarkModelEspListResponseBody(TeaModel):
    def __init__(self, moudle=None):
        self.moudle = moudle  # type: QueryTrademarkModelEspListResponseBodyMoudle

    def validate(self):
        if self.moudle:
            self.moudle.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelEspListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.moudle is not None:
            result['Moudle'] = self.moudle.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Moudle') is not None:
            temp_model = QueryTrademarkModelEspListResponseBodyMoudle()
            self.moudle = temp_model.from_map(m['Moudle'])
        return self


class QueryTrademarkModelEspListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTrademarkModelEspListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelEspListResponse, self).to_map()
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
            temp_model = QueryTrademarkModelEspListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkModelListRequest(TeaModel):
    def __init__(self, env=None, order_ids_str=None, page_num=None, page_size=None, principal_key=None,
                 principal_name=None, produce_types_str=None, status=None, submit_start=None, submit_status=None, submit_time=None):
        self.env = env  # type: str
        self.order_ids_str = order_ids_str  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.principal_key = principal_key  # type: str
        self.principal_name = principal_name  # type: str
        self.produce_types_str = produce_types_str  # type: str
        self.status = status  # type: str
        self.submit_start = submit_start  # type: str
        self.submit_status = submit_status  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.order_ids_str is not None:
            result['OrderIdsStr'] = self.order_ids_str
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.produce_types_str is not None:
            result['ProduceTypesStr'] = self.produce_types_str
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_start is not None:
            result['SubmitStart'] = self.submit_start
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OrderIdsStr') is not None:
            self.order_ids_str = m.get('OrderIdsStr')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProduceTypesStr') is not None:
            self.produce_types_str = m.get('ProduceTypesStr')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitStart') is not None:
            self.submit_start = m.get('SubmitStart')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class QueryTrademarkModelListResponseBodyMoudleDataItemLeafCodesLeafCode(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelListResponseBodyMoudleDataItemLeafCodesLeafCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTrademarkModelListResponseBodyMoudleDataItemLeafCodes(TeaModel):
    def __init__(self, leaf_code=None):
        self.leaf_code = leaf_code  # type: list[QueryTrademarkModelListResponseBodyMoudleDataItemLeafCodesLeafCode]

    def validate(self):
        if self.leaf_code:
            for k in self.leaf_code:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelListResponseBodyMoudleDataItemLeafCodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['leafCode'] = []
        if self.leaf_code is not None:
            for k in self.leaf_code:
                result['leafCode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.leaf_code = []
        if m.get('leafCode') is not None:
            for k in m.get('leafCode'):
                temp_model = QueryTrademarkModelListResponseBodyMoudleDataItemLeafCodesLeafCode()
                self.leaf_code.append(temp_model.from_map(k))
        return self


class QueryTrademarkModelListResponseBodyMoudleDataItemMaterialInfo(TeaModel):
    def __init__(self, address=None, business_licence_url=None, card_number=None, cn_info_url=None,
                 contact_address=None, contact_email=None, contact_zip_code=None, country=None, eaddress=None, ename=None,
                 id_card_number=None, id_card_url=None, loa_key=None, loa_url=None, name=None, passport_url=None,
                 personal_type=None, post_code=None, province=None, reason_file_oss_key=None, region=None, type=None):
        self.address = address  # type: str
        self.business_licence_url = business_licence_url  # type: str
        self.card_number = card_number  # type: str
        self.cn_info_url = cn_info_url  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_zip_code = contact_zip_code  # type: str
        self.country = country  # type: str
        self.eaddress = eaddress  # type: str
        self.ename = ename  # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_url = id_card_url  # type: str
        self.loa_key = loa_key  # type: str
        self.loa_url = loa_url  # type: str
        self.name = name  # type: str
        self.passport_url = passport_url  # type: str
        self.personal_type = personal_type  # type: int
        self.post_code = post_code  # type: str
        self.province = province  # type: str
        self.reason_file_oss_key = reason_file_oss_key  # type: str
        self.region = region  # type: int
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelListResponseBodyMoudleDataItemMaterialInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.cn_info_url is not None:
            result['CnInfoUrl'] = self.cn_info_url
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.post_code is not None:
            result['PostCode'] = self.post_code
        if self.province is not None:
            result['Province'] = self.province
        if self.reason_file_oss_key is not None:
            result['ReasonFileOssKey'] = self.reason_file_oss_key
        if self.region is not None:
            result['Region'] = self.region
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('CnInfoUrl') is not None:
            self.cn_info_url = m.get('CnInfoUrl')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('ReasonFileOssKey') is not None:
            self.reason_file_oss_key = m.get('ReasonFileOssKey')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryTrademarkModelListResponseBodyMoudleDataItemRootCode(TeaModel):
    def __init__(self, classification_code=None, classification_name=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkModelListResponseBodyMoudleDataItemRootCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        return self


class QueryTrademarkModelListResponseBodyMoudleDataItem(TeaModel):
    def __init__(self, bit_flag=None, biz_id=None, biz_type=None, extend_info=None, gray_icon_url=None, icon=None,
                 leaf_codes=None, material_info=None, order_id=None, partner_code=None, principal_key=None,
                 principal_name=None, produce_type=None, root_code=None, status=None, status_str=None, submit_audit_time_str=None,
                 submit_audit_time_value=None, submit_status=None, submit_time_str=None, submit_time_value=None, submit_times=None,
                 trademark_name=None, trademark_name_type=None, trademark_number=None):
        self.bit_flag = bit_flag  # type: int
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.extend_info = extend_info  # type: dict[str, any]
        self.gray_icon_url = gray_icon_url  # type: str
        self.icon = icon  # type: str
        self.leaf_codes = leaf_codes  # type: QueryTrademarkModelListResponseBodyMoudleDataItemLeafCodes
        self.material_info = material_info  # type: QueryTrademarkModelListResponseBodyMoudleDataItemMaterialInfo
        self.order_id = order_id  # type: str
        self.partner_code = partner_code  # type: str
        self.principal_key = principal_key  # type: str
        self.principal_name = principal_name  # type: str
        self.produce_type = produce_type  # type: str
        self.root_code = root_code  # type: QueryTrademarkModelListResponseBodyMoudleDataItemRootCode
        self.status = status  # type: str
        self.status_str = status_str  # type: str
        self.submit_audit_time_str = submit_audit_time_str  # type: str
        self.submit_audit_time_value = submit_audit_time_value  # type: long
        self.submit_status = submit_status  # type: str
        self.submit_time_str = submit_time_str  # type: str
        self.submit_time_value = submit_time_value  # type: long
        self.submit_times = submit_times  # type: int
        self.trademark_name = trademark_name  # type: str
        self.trademark_name_type = trademark_name_type  # type: int
        self.trademark_number = trademark_number  # type: str

    def validate(self):
        if self.leaf_codes:
            self.leaf_codes.validate()
        if self.material_info:
            self.material_info.validate()
        if self.root_code:
            self.root_code.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelListResponseBodyMoudleDataItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_flag is not None:
            result['BitFlag'] = self.bit_flag
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.leaf_codes is not None:
            result['LeafCodes'] = self.leaf_codes.to_map()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        if self.root_code is not None:
            result['RootCode'] = self.root_code.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_str is not None:
            result['StatusStr'] = self.status_str
        if self.submit_audit_time_str is not None:
            result['SubmitAuditTimeStr'] = self.submit_audit_time_str
        if self.submit_audit_time_value is not None:
            result['SubmitAuditTimeValue'] = self.submit_audit_time_value
        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status
        if self.submit_time_str is not None:
            result['SubmitTimeStr'] = self.submit_time_str
        if self.submit_time_value is not None:
            result['SubmitTimeValue'] = self.submit_time_value
        if self.submit_times is not None:
            result['SubmitTimes'] = self.submit_times
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.trademark_name_type is not None:
            result['TrademarkNameType'] = self.trademark_name_type
        if self.trademark_number is not None:
            result['TrademarkNumber'] = self.trademark_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BitFlag') is not None:
            self.bit_flag = m.get('BitFlag')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('LeafCodes') is not None:
            temp_model = QueryTrademarkModelListResponseBodyMoudleDataItemLeafCodes()
            self.leaf_codes = temp_model.from_map(m['LeafCodes'])
        if m.get('MaterialInfo') is not None:
            temp_model = QueryTrademarkModelListResponseBodyMoudleDataItemMaterialInfo()
            self.material_info = temp_model.from_map(m['MaterialInfo'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        if m.get('RootCode') is not None:
            temp_model = QueryTrademarkModelListResponseBodyMoudleDataItemRootCode()
            self.root_code = temp_model.from_map(m['RootCode'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusStr') is not None:
            self.status_str = m.get('StatusStr')
        if m.get('SubmitAuditTimeStr') is not None:
            self.submit_audit_time_str = m.get('SubmitAuditTimeStr')
        if m.get('SubmitAuditTimeValue') is not None:
            self.submit_audit_time_value = m.get('SubmitAuditTimeValue')
        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')
        if m.get('SubmitTimeStr') is not None:
            self.submit_time_str = m.get('SubmitTimeStr')
        if m.get('SubmitTimeValue') is not None:
            self.submit_time_value = m.get('SubmitTimeValue')
        if m.get('SubmitTimes') is not None:
            self.submit_times = m.get('SubmitTimes')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('TrademarkNameType') is not None:
            self.trademark_name_type = m.get('TrademarkNameType')
        if m.get('TrademarkNumber') is not None:
            self.trademark_number = m.get('TrademarkNumber')
        return self


class QueryTrademarkModelListResponseBodyMoudleData(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[QueryTrademarkModelListResponseBodyMoudleDataItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelListResponseBodyMoudleData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['item'] = []
        if self.item is not None:
            for k in self.item:
                result['item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('item') is not None:
            for k in m.get('item'):
                temp_model = QueryTrademarkModelListResponseBodyMoudleDataItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryTrademarkModelListResponseBodyMoudle(TeaModel):
    def __init__(self, data=None, request_id=None, total_page_num=None):
        self.data = data  # type: QueryTrademarkModelListResponseBodyMoudleData
        self.request_id = request_id  # type: str
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelListResponseBodyMoudle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryTrademarkModelListResponseBodyMoudleData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTrademarkModelListResponseBody(TeaModel):
    def __init__(self, moudle=None):
        self.moudle = moudle  # type: QueryTrademarkModelListResponseBodyMoudle

    def validate(self):
        if self.moudle:
            self.moudle.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.moudle is not None:
            result['Moudle'] = self.moudle.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Moudle') is not None:
            temp_model = QueryTrademarkModelListResponseBodyMoudle()
            self.moudle = temp_model.from_map(m['Moudle'])
        return self


class QueryTrademarkModelListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTrademarkModelListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTrademarkModelListResponse, self).to_map()
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
            temp_model = QueryTrademarkModelListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkMonitorResultsRequest(TeaModel):
    def __init__(self, action_type=None, apply_year=None, classification=None, page_num=None, page_size=None,
                 procedure_status=None, registration_number=None, rule_id=None, tm_name=None):
        self.action_type = action_type  # type: int
        self.apply_year = apply_year  # type: str
        self.classification = classification  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.procedure_status = procedure_status  # type: int
        self.registration_number = registration_number  # type: str
        self.rule_id = rule_id  # type: long
        self.tm_name = tm_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkMonitorResultsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.apply_year is not None:
            result['ApplyYear'] = self.apply_year
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.procedure_status is not None:
            result['ProcedureStatus'] = self.procedure_status
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('ApplyYear') is not None:
            self.apply_year = m.get('ApplyYear')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProcedureStatus') is not None:
            self.procedure_status = m.get('ProcedureStatus')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        return self


class QueryTrademarkMonitorResultsResponseBodyDataTmMonitorResult(TeaModel):
    def __init__(self, apply_date=None, chesan_end_date=None, classification=None, data_create_time=None,
                 data_update_time=None, owner_en_name=None, owner_name=None, registration_number=None, rule_id=None, tm_image=None,
                 tm_name=None, tm_procedure_status_desc=None, tm_uid=None, user_id=None, wuxiao_end_date=None,
                 xuzhan_end_date=None, yiyi_end_date=None):
        self.apply_date = apply_date  # type: str
        self.chesan_end_date = chesan_end_date  # type: str
        self.classification = classification  # type: str
        self.data_create_time = data_create_time  # type: long
        self.data_update_time = data_update_time  # type: long
        self.owner_en_name = owner_en_name  # type: str
        self.owner_name = owner_name  # type: str
        self.registration_number = registration_number  # type: str
        self.rule_id = rule_id  # type: str
        self.tm_image = tm_image  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_procedure_status_desc = tm_procedure_status_desc  # type: str
        self.tm_uid = tm_uid  # type: str
        self.user_id = user_id  # type: str
        self.wuxiao_end_date = wuxiao_end_date  # type: str
        self.xuzhan_end_date = xuzhan_end_date  # type: str
        self.yiyi_end_date = yiyi_end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkMonitorResultsResponseBodyDataTmMonitorResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_date is not None:
            result['ApplyDate'] = self.apply_date
        if self.chesan_end_date is not None:
            result['ChesanEndDate'] = self.chesan_end_date
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.data_create_time is not None:
            result['DataCreateTime'] = self.data_create_time
        if self.data_update_time is not None:
            result['DataUpdateTime'] = self.data_update_time
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.tm_image is not None:
            result['TmImage'] = self.tm_image
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_procedure_status_desc is not None:
            result['TmProcedureStatusDesc'] = self.tm_procedure_status_desc
        if self.tm_uid is not None:
            result['TmUid'] = self.tm_uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.wuxiao_end_date is not None:
            result['WuxiaoEndDate'] = self.wuxiao_end_date
        if self.xuzhan_end_date is not None:
            result['XuzhanEndDate'] = self.xuzhan_end_date
        if self.yiyi_end_date is not None:
            result['YiyiEndDate'] = self.yiyi_end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyDate') is not None:
            self.apply_date = m.get('ApplyDate')
        if m.get('ChesanEndDate') is not None:
            self.chesan_end_date = m.get('ChesanEndDate')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('DataCreateTime') is not None:
            self.data_create_time = m.get('DataCreateTime')
        if m.get('DataUpdateTime') is not None:
            self.data_update_time = m.get('DataUpdateTime')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TmImage') is not None:
            self.tm_image = m.get('TmImage')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmProcedureStatusDesc') is not None:
            self.tm_procedure_status_desc = m.get('TmProcedureStatusDesc')
        if m.get('TmUid') is not None:
            self.tm_uid = m.get('TmUid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WuxiaoEndDate') is not None:
            self.wuxiao_end_date = m.get('WuxiaoEndDate')
        if m.get('XuzhanEndDate') is not None:
            self.xuzhan_end_date = m.get('XuzhanEndDate')
        if m.get('YiyiEndDate') is not None:
            self.yiyi_end_date = m.get('YiyiEndDate')
        return self


class QueryTrademarkMonitorResultsResponseBodyData(TeaModel):
    def __init__(self, tm_monitor_result=None):
        self.tm_monitor_result = tm_monitor_result  # type: list[QueryTrademarkMonitorResultsResponseBodyDataTmMonitorResult]

    def validate(self):
        if self.tm_monitor_result:
            for k in self.tm_monitor_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkMonitorResultsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmMonitorResult'] = []
        if self.tm_monitor_result is not None:
            for k in self.tm_monitor_result:
                result['TmMonitorResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tm_monitor_result = []
        if m.get('TmMonitorResult') is not None:
            for k in m.get('TmMonitorResult'):
                temp_model = QueryTrademarkMonitorResultsResponseBodyDataTmMonitorResult()
                self.tm_monitor_result.append(temp_model.from_map(k))
        return self


class QueryTrademarkMonitorResultsResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, next_page=None, page_size=None, pre_page=None,
                 request_id=None, total_item_num=None, total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryTrademarkMonitorResultsResponseBodyData
        self.next_page = next_page  # type: bool
        self.page_size = page_size  # type: int
        self.pre_page = pre_page  # type: bool
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTrademarkMonitorResultsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTrademarkMonitorResultsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTrademarkMonitorResultsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTrademarkMonitorResultsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTrademarkMonitorResultsResponse, self).to_map()
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
            temp_model = QueryTrademarkMonitorResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkMonitorRulesRequest(TeaModel):
    def __init__(self, id=None, notify_update=None, page_num=None, page_size=None, rule_name=None):
        self.id = id  # type: str
        self.notify_update = notify_update  # type: int
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkMonitorRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.notify_update is not None:
            result['NotifyUpdate'] = self.notify_update
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NotifyUpdate') is not None:
            self.notify_update = m.get('NotifyUpdate')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class QueryTrademarkMonitorRulesResponseBodyDataTmMonitorRule(TeaModel):
    def __init__(self, create_time=None, end_time=None, env=None, id=None, last_finish_time=None, last_run_time=None,
                 last_update_time=None, notify_update=None, rule_detail=None, rule_extend=None, rule_keyword=None, rule_name=None,
                 rule_source=None, rule_status=None, rule_type=None, start_time=None, update_time=None, user_id=None,
                 version=None):
        self.create_time = create_time  # type: str
        self.end_time = end_time  # type: str
        self.env = env  # type: str
        self.id = id  # type: str
        self.last_finish_time = last_finish_time  # type: str
        self.last_run_time = last_run_time  # type: str
        self.last_update_time = last_update_time  # type: str
        self.notify_update = notify_update  # type: int
        self.rule_detail = rule_detail  # type: str
        self.rule_extend = rule_extend  # type: str
        self.rule_keyword = rule_keyword  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_source = rule_source  # type: str
        self.rule_status = rule_status  # type: str
        self.rule_type = rule_type  # type: int
        self.start_time = start_time  # type: str
        self.update_time = update_time  # type: str
        self.user_id = user_id  # type: str
        self.version = version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkMonitorRulesResponseBodyDataTmMonitorRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.env is not None:
            result['Env'] = self.env
        if self.id is not None:
            result['Id'] = self.id
        if self.last_finish_time is not None:
            result['LastFinishTime'] = self.last_finish_time
        if self.last_run_time is not None:
            result['LastRunTime'] = self.last_run_time
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.notify_update is not None:
            result['NotifyUpdate'] = self.notify_update
        if self.rule_detail is not None:
            result['RuleDetail'] = self.rule_detail
        if self.rule_extend is not None:
            result['RuleExtend'] = self.rule_extend
        if self.rule_keyword is not None:
            result['RuleKeyword'] = self.rule_keyword
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastFinishTime') is not None:
            self.last_finish_time = m.get('LastFinishTime')
        if m.get('LastRunTime') is not None:
            self.last_run_time = m.get('LastRunTime')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('NotifyUpdate') is not None:
            self.notify_update = m.get('NotifyUpdate')
        if m.get('RuleDetail') is not None:
            self.rule_detail = m.get('RuleDetail')
        if m.get('RuleExtend') is not None:
            self.rule_extend = m.get('RuleExtend')
        if m.get('RuleKeyword') is not None:
            self.rule_keyword = m.get('RuleKeyword')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class QueryTrademarkMonitorRulesResponseBodyData(TeaModel):
    def __init__(self, tm_monitor_rule=None):
        self.tm_monitor_rule = tm_monitor_rule  # type: list[QueryTrademarkMonitorRulesResponseBodyDataTmMonitorRule]

    def validate(self):
        if self.tm_monitor_rule:
            for k in self.tm_monitor_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkMonitorRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmMonitorRule'] = []
        if self.tm_monitor_rule is not None:
            for k in self.tm_monitor_rule:
                result['TmMonitorRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tm_monitor_rule = []
        if m.get('TmMonitorRule') is not None:
            for k in m.get('TmMonitorRule'):
                temp_model = QueryTrademarkMonitorRulesResponseBodyDataTmMonitorRule()
                self.tm_monitor_rule.append(temp_model.from_map(k))
        return self


class QueryTrademarkMonitorRulesResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, next_page=None, page_size=None, pre_page=None,
                 request_id=None, total_item_num=None, total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryTrademarkMonitorRulesResponseBodyData
        self.next_page = next_page  # type: bool
        self.page_size = page_size  # type: int
        self.pre_page = pre_page  # type: bool
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTrademarkMonitorRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('Data') is not None:
            temp_model = QueryTrademarkMonitorRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryTrademarkMonitorRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTrademarkMonitorRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTrademarkMonitorRulesResponse, self).to_map()
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
            temp_model = QueryTrademarkMonitorRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkOnSaleRequest(TeaModel):
    def __init__(self, classification=None, page_num=None, page_size=None, register_code=None, register_number=None,
                 tm_type=None):
        self.classification = classification  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.register_code = register_code  # type: str
        self.register_number = register_number  # type: str
        self.tm_type = tm_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkOnSaleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.tm_type is not None:
            result['TmType'] = self.tm_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('TmType') is not None:
            self.tm_type = m.get('TmType')
        return self


class QueryTrademarkOnSaleResponseBodyTrademarks(TeaModel):
    def __init__(self, audit_result=None, classification=None, icon=None, order_price=None,
                 registration_number=None, status=None, tm_type=None, trademark_name=None):
        self.audit_result = audit_result  # type: str
        self.classification = classification  # type: str
        self.icon = icon  # type: str
        self.order_price = order_price  # type: str
        self.registration_number = registration_number  # type: str
        self.status = status  # type: long
        self.tm_type = tm_type  # type: str
        self.trademark_name = trademark_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkOnSaleResponseBodyTrademarks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.status is not None:
            result['Status'] = self.status
        if self.tm_type is not None:
            result['TmType'] = self.tm_type
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TmType') is not None:
            self.tm_type = m.get('TmType')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        return self


class QueryTrademarkOnSaleResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, total_page_number=None,
                 trademarks=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.total_page_number = total_page_number  # type: int
        self.trademarks = trademarks  # type: list[QueryTrademarkOnSaleResponseBodyTrademarks]

    def validate(self):
        if self.trademarks:
            for k in self.trademarks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkOnSaleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page_number is not None:
            result['TotalPageNumber'] = self.total_page_number
        result['Trademarks'] = []
        if self.trademarks is not None:
            for k in self.trademarks:
                result['Trademarks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPageNumber') is not None:
            self.total_page_number = m.get('TotalPageNumber')
        self.trademarks = []
        if m.get('Trademarks') is not None:
            for k in m.get('Trademarks'):
                temp_model = QueryTrademarkOnSaleResponseBodyTrademarks()
                self.trademarks.append(temp_model.from_map(k))
        return self


class QueryTrademarkOnSaleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTrademarkOnSaleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTrademarkOnSaleResponse, self).to_map()
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
            temp_model = QueryTrademarkOnSaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkPriceRequest(TeaModel):
    def __init__(self, order_data=None, tm_icon=None, tm_name=None, type=None, user_id=None):
        self.order_data = order_data  # type: dict[str, any]
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.type = type  # type: int
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_data is not None:
            result['OrderData'] = self.order_data
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderData') is not None:
            self.order_data = m.get('OrderData')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTrademarkPriceShrinkRequest(TeaModel):
    def __init__(self, order_data_shrink=None, tm_icon=None, tm_name=None, type=None, user_id=None):
        self.order_data_shrink = order_data_shrink  # type: str
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.type = type  # type: int
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkPriceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_data_shrink is not None:
            result['OrderData'] = self.order_data_shrink
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderData') is not None:
            self.order_data_shrink = m.get('OrderData')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTrademarkPriceResponseBodyPricesPrices(TeaModel):
    def __init__(self, classification_code=None, currency=None, discount_price=None, original_price=None,
                 trade_price=None):
        self.classification_code = classification_code  # type: str
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkPriceResponseBodyPricesPrices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryTrademarkPriceResponseBodyPrices(TeaModel):
    def __init__(self, prices=None):
        self.prices = prices  # type: list[QueryTrademarkPriceResponseBodyPricesPrices]

    def validate(self):
        if self.prices:
            for k in self.prices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkPriceResponseBodyPrices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Prices'] = []
        if self.prices is not None:
            for k in self.prices:
                result['Prices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.prices = []
        if m.get('Prices') is not None:
            for k in m.get('Prices'):
                temp_model = QueryTrademarkPriceResponseBodyPricesPrices()
                self.prices.append(temp_model.from_map(k))
        return self


class QueryTrademarkPriceResponseBody(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, prices=None, request_id=None,
                 trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.prices = prices  # type: QueryTrademarkPriceResponseBodyPrices
        self.request_id = request_id  # type: str
        self.trade_price = trade_price  # type: float

    def validate(self):
        if self.prices:
            self.prices.validate()

    def to_map(self):
        _map = super(QueryTrademarkPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.prices is not None:
            result['Prices'] = self.prices.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('Prices') is not None:
            temp_model = QueryTrademarkPriceResponseBodyPrices()
            self.prices = temp_model.from_map(m['Prices'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryTrademarkPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTrademarkPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTrademarkPriceResponse, self).to_map()
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
            temp_model = QueryTrademarkPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkUploadAuditResultRequest(TeaModel):
    def __init__(self, classification=None, page_num=None, page_size=None, register_code=None, register_number=None,
                 tm_type=None):
        self.classification = classification  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.register_code = register_code  # type: str
        self.register_number = register_number  # type: str
        self.tm_type = tm_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkUploadAuditResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.tm_type is not None:
            result['TmType'] = self.tm_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('TmType') is not None:
            self.tm_type = m.get('TmType')
        return self


class QueryTrademarkUploadAuditResultResponseBodyTrademarks(TeaModel):
    def __init__(self, audit_result=None, classification=None, icon=None, order_price=None,
                 registration_number=None, status=None, tm_type=None, trademark_name=None):
        self.audit_result = audit_result  # type: str
        self.classification = classification  # type: str
        self.icon = icon  # type: str
        self.order_price = order_price  # type: str
        self.registration_number = registration_number  # type: str
        self.status = status  # type: long
        self.tm_type = tm_type  # type: str
        self.trademark_name = trademark_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTrademarkUploadAuditResultResponseBodyTrademarks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.status is not None:
            result['Status'] = self.status
        if self.tm_type is not None:
            result['TmType'] = self.tm_type
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TmType') is not None:
            self.tm_type = m.get('TmType')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        return self


class QueryTrademarkUploadAuditResultResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, total_page_number=None,
                 trademarks=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.total_page_number = total_page_number  # type: int
        self.trademarks = trademarks  # type: list[QueryTrademarkUploadAuditResultResponseBodyTrademarks]

    def validate(self):
        if self.trademarks:
            for k in self.trademarks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTrademarkUploadAuditResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page_number is not None:
            result['TotalPageNumber'] = self.total_page_number
        result['Trademarks'] = []
        if self.trademarks is not None:
            for k in self.trademarks:
                result['Trademarks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPageNumber') is not None:
            self.total_page_number = m.get('TotalPageNumber')
        self.trademarks = []
        if m.get('Trademarks') is not None:
            for k in m.get('Trademarks'):
                temp_model = QueryTrademarkUploadAuditResultResponseBodyTrademarks()
                self.trademarks.append(temp_model.from_map(k))
        return self


class QueryTrademarkUploadAuditResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTrademarkUploadAuditResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTrademarkUploadAuditResultResponse, self).to_map()
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
            temp_model = QueryTrademarkUploadAuditResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecordBankBalanceRequest(TeaModel):
    def __init__(self, action_date=None, balance=None, principal_name=None):
        self.action_date = action_date  # type: long
        self.balance = balance  # type: str
        self.principal_name = principal_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecordBankBalanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_date is not None:
            result['ActionDate'] = self.action_date
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionDate') is not None:
            self.action_date = m.get('ActionDate')
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        return self


class RecordBankBalanceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecordBankBalanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RecordBankBalanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecordBankBalanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecordBankBalanceResponse, self).to_map()
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
            temp_model = RecordBankBalanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundProduceRequest(TeaModel):
    def __init__(self, biz_id=None, refund_type=None):
        self.biz_id = biz_id  # type: str
        self.refund_type = refund_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundProduceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.refund_type is not None:
            result['RefundType'] = self.refund_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('RefundType') is not None:
            self.refund_type = m.get('RefundType')
        return self


class RefundProduceResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundProduceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefundProduceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefundProduceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefundProduceResponse, self).to_map()
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
            temp_model = RefundProduceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefuseAdditionalMaterialRequest(TeaModel):
    def __init__(self, biz_id=None, note=None):
        self.biz_id = biz_id  # type: str
        self.note = note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefuseAdditionalMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class RefuseAdditionalMaterialResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefuseAdditionalMaterialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefuseAdditionalMaterialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefuseAdditionalMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefuseAdditionalMaterialResponse, self).to_map()
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
            temp_model = RefuseAdditionalMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefuseApplicantRequest(TeaModel):
    def __init__(self, biz_id=None, note=None):
        self.biz_id = biz_id  # type: str
        self.note = note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefuseApplicantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class RefuseApplicantResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefuseApplicantResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefuseApplicantResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefuseApplicantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefuseApplicantResponse, self).to_map()
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
            temp_model = RefuseApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectApplicantRequest(TeaModel):
    def __init__(self, instance_id=None, note=None):
        self.instance_id = instance_id  # type: str
        self.note = note  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectApplicantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class RejectApplicantResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectApplicantResponseBody, self).to_map()
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


class RejectApplicantResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RejectApplicantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RejectApplicantResponse, self).to_map()
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
            temp_model = RejectApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveClassificationConditionsRequest(TeaModel):
    def __init__(self, biz_id=None, condition=None, type=None):
        self.biz_id = biz_id  # type: str
        self.condition = condition  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveClassificationConditionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.condition is not None:
            result['Condition'] = self.condition
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SaveClassificationConditionsResponseBodyInvalidList(TeaModel):
    def __init__(self, classification_code=None, classification_name=None, official_code=None, parent_code=None):
        self.classification_code = classification_code  # type: str
        self.classification_name = classification_name  # type: str
        self.official_code = official_code  # type: str
        self.parent_code = parent_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveClassificationConditionsResponseBodyInvalidList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.official_code is not None:
            result['OfficialCode'] = self.official_code
        if self.parent_code is not None:
            result['ParentCode'] = self.parent_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('OfficialCode') is not None:
            self.official_code = m.get('OfficialCode')
        if m.get('ParentCode') is not None:
            self.parent_code = m.get('ParentCode')
        return self


class SaveClassificationConditionsResponseBody(TeaModel):
    def __init__(self, error_msg=None, invalid_list=None, request_id=None, success=None, tag_name=None):
        self.error_msg = error_msg  # type: str
        self.invalid_list = invalid_list  # type: list[SaveClassificationConditionsResponseBodyInvalidList]
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.tag_name = tag_name  # type: str

    def validate(self):
        if self.invalid_list:
            for k in self.invalid_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveClassificationConditionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['InvalidList'] = []
        if self.invalid_list is not None:
            for k in self.invalid_list:
                result['InvalidList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.invalid_list = []
        if m.get('InvalidList') is not None:
            for k in m.get('InvalidList'):
                temp_model = SaveClassificationConditionsResponseBodyInvalidList()
                self.invalid_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class SaveClassificationConditionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveClassificationConditionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveClassificationConditionsResponse, self).to_map()
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
            temp_model = SaveClassificationConditionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveExtensionAttributeRequest(TeaModel):
    def __init__(self, attribute_key=None, attribute_value=None, biz_id=None):
        self.attribute_key = attribute_key  # type: str
        self.attribute_value = attribute_value  # type: str
        self.biz_id = biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveExtensionAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class SaveExtensionAttributeResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveExtensionAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveExtensionAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveExtensionAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveExtensionAttributeResponse, self).to_map()
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
            temp_model = SaveExtensionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskRequest(TeaModel):
    def __init__(self, biz_type=None, request=None):
        self.biz_type = biz_type  # type: str
        self.request = request  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.request is not None:
            result['Request'] = self.request
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Request') is not None:
            self.request = m.get('Request')
        return self


class SaveTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskResponseBody, self).to_map()
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


class SaveTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveTaskResponse, self).to_map()
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
            temp_model = SaveTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskForOfficialFileCustomRequest(TeaModel):
    def __init__(self, end_accept_time=None, start_accept_time=None):
        self.end_accept_time = end_accept_time  # type: long
        self.start_accept_time = start_accept_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskForOfficialFileCustomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_accept_time is not None:
            result['EndAcceptTime'] = self.end_accept_time
        if self.start_accept_time is not None:
            result['StartAcceptTime'] = self.start_accept_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndAcceptTime') is not None:
            self.end_accept_time = m.get('EndAcceptTime')
        if m.get('StartAcceptTime') is not None:
            self.start_accept_time = m.get('StartAcceptTime')
        return self


class SaveTaskForOfficialFileCustomResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskForOfficialFileCustomResponseBody, self).to_map()
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


class SaveTaskForOfficialFileCustomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveTaskForOfficialFileCustomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveTaskForOfficialFileCustomResponse, self).to_map()
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
            temp_model = SaveTaskForOfficialFileCustomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTradeMarkReviewMaterialDetailRequest(TeaModel):
    def __init__(self, additional_oss_key_list=None, address=None, application_oss_key=None, biz_id=None,
                 business_licence_oss_key=None, card_number=None, change_name=None, contact_address=None, contact_email=None,
                 contact_name=None, contact_number=None, country=None, eng_address=None, eng_name=None, id_card_oss_key=None,
                 legal_notice_oss_key=None, loa_oss_key=None, name=None, passport_oss_key=None, province=None, region=None,
                 review_material_additional_json=None, separate=None, submit_online=None, submit_type=None, supplement_flag=None, type=None):
        self.additional_oss_key_list = additional_oss_key_list  # type: dict[str, any]
        self.address = address  # type: str
        self.application_oss_key = application_oss_key  # type: str
        self.biz_id = biz_id  # type: str
        self.business_licence_oss_key = business_licence_oss_key  # type: str
        self.card_number = card_number  # type: str
        self.change_name = change_name  # type: bool
        self.contact_address = contact_address  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.country = country  # type: str
        self.eng_address = eng_address  # type: str
        self.eng_name = eng_name  # type: str
        self.id_card_oss_key = id_card_oss_key  # type: str
        self.legal_notice_oss_key = legal_notice_oss_key  # type: str
        self.loa_oss_key = loa_oss_key  # type: str
        self.name = name  # type: str
        self.passport_oss_key = passport_oss_key  # type: str
        self.province = province  # type: str
        self.region = region  # type: int
        self.review_material_additional_json = review_material_additional_json  # type: str
        self.separate = separate  # type: bool
        self.submit_online = submit_online  # type: bool
        self.submit_type = submit_type  # type: int
        self.supplement_flag = supplement_flag  # type: bool
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTradeMarkReviewMaterialDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_oss_key_list is not None:
            result['AdditionalOssKeyList'] = self.additional_oss_key_list
        if self.address is not None:
            result['Address'] = self.address
        if self.application_oss_key is not None:
            result['ApplicationOssKey'] = self.application_oss_key
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.change_name is not None:
            result['ChangeName'] = self.change_name
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.country is not None:
            result['Country'] = self.country
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        if self.review_material_additional_json is not None:
            result['ReviewMaterialAdditionalJson'] = self.review_material_additional_json
        if self.separate is not None:
            result['Separate'] = self.separate
        if self.submit_online is not None:
            result['SubmitOnline'] = self.submit_online
        if self.submit_type is not None:
            result['SubmitType'] = self.submit_type
        if self.supplement_flag is not None:
            result['SupplementFlag'] = self.supplement_flag
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdditionalOssKeyList') is not None:
            self.additional_oss_key_list = m.get('AdditionalOssKeyList')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicationOssKey') is not None:
            self.application_oss_key = m.get('ApplicationOssKey')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ChangeName') is not None:
            self.change_name = m.get('ChangeName')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReviewMaterialAdditionalJson') is not None:
            self.review_material_additional_json = m.get('ReviewMaterialAdditionalJson')
        if m.get('Separate') is not None:
            self.separate = m.get('Separate')
        if m.get('SubmitOnline') is not None:
            self.submit_online = m.get('SubmitOnline')
        if m.get('SubmitType') is not None:
            self.submit_type = m.get('SubmitType')
        if m.get('SupplementFlag') is not None:
            self.supplement_flag = m.get('SupplementFlag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SaveTradeMarkReviewMaterialDetailShrinkRequest(TeaModel):
    def __init__(self, additional_oss_key_list_shrink=None, address=None, application_oss_key=None, biz_id=None,
                 business_licence_oss_key=None, card_number=None, change_name=None, contact_address=None, contact_email=None,
                 contact_name=None, contact_number=None, country=None, eng_address=None, eng_name=None, id_card_oss_key=None,
                 legal_notice_oss_key=None, loa_oss_key=None, name=None, passport_oss_key=None, province=None, region=None,
                 review_material_additional_json=None, separate=None, submit_online=None, submit_type=None, supplement_flag=None, type=None):
        self.additional_oss_key_list_shrink = additional_oss_key_list_shrink  # type: str
        self.address = address  # type: str
        self.application_oss_key = application_oss_key  # type: str
        self.biz_id = biz_id  # type: str
        self.business_licence_oss_key = business_licence_oss_key  # type: str
        self.card_number = card_number  # type: str
        self.change_name = change_name  # type: bool
        self.contact_address = contact_address  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.country = country  # type: str
        self.eng_address = eng_address  # type: str
        self.eng_name = eng_name  # type: str
        self.id_card_oss_key = id_card_oss_key  # type: str
        self.legal_notice_oss_key = legal_notice_oss_key  # type: str
        self.loa_oss_key = loa_oss_key  # type: str
        self.name = name  # type: str
        self.passport_oss_key = passport_oss_key  # type: str
        self.province = province  # type: str
        self.region = region  # type: int
        self.review_material_additional_json = review_material_additional_json  # type: str
        self.separate = separate  # type: bool
        self.submit_online = submit_online  # type: bool
        self.submit_type = submit_type  # type: int
        self.supplement_flag = supplement_flag  # type: bool
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTradeMarkReviewMaterialDetailShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_oss_key_list_shrink is not None:
            result['AdditionalOssKeyList'] = self.additional_oss_key_list_shrink
        if self.address is not None:
            result['Address'] = self.address
        if self.application_oss_key is not None:
            result['ApplicationOssKey'] = self.application_oss_key
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.change_name is not None:
            result['ChangeName'] = self.change_name
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.country is not None:
            result['Country'] = self.country
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        if self.review_material_additional_json is not None:
            result['ReviewMaterialAdditionalJson'] = self.review_material_additional_json
        if self.separate is not None:
            result['Separate'] = self.separate
        if self.submit_online is not None:
            result['SubmitOnline'] = self.submit_online
        if self.submit_type is not None:
            result['SubmitType'] = self.submit_type
        if self.supplement_flag is not None:
            result['SupplementFlag'] = self.supplement_flag
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdditionalOssKeyList') is not None:
            self.additional_oss_key_list_shrink = m.get('AdditionalOssKeyList')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ApplicationOssKey') is not None:
            self.application_oss_key = m.get('ApplicationOssKey')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ChangeName') is not None:
            self.change_name = m.get('ChangeName')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReviewMaterialAdditionalJson') is not None:
            self.review_material_additional_json = m.get('ReviewMaterialAdditionalJson')
        if m.get('Separate') is not None:
            self.separate = m.get('Separate')
        if m.get('SubmitOnline') is not None:
            self.submit_online = m.get('SubmitOnline')
        if m.get('SubmitType') is not None:
            self.submit_type = m.get('SubmitType')
        if m.get('SupplementFlag') is not None:
            self.supplement_flag = m.get('SupplementFlag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SaveTradeMarkReviewMaterialDetailResponseBody(TeaModel):
    def __init__(self, error_msg=None, request_id=None, success=None):
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTradeMarkReviewMaterialDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveTradeMarkReviewMaterialDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveTradeMarkReviewMaterialDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveTradeMarkReviewMaterialDetailResponse, self).to_map()
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
            temp_model = SaveTradeMarkReviewMaterialDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SbjOperateRequest(TeaModel):
    def __init__(self, amount=None, apply_no=None, audit_status=None, biz_id=None, file_date=None, file_oss_key=None,
                 message=None, operate_type=None, order_no=None, receipt_oss_key=None, submitted_success=None):
        self.amount = amount  # type: str
        self.apply_no = apply_no  # type: str
        self.audit_status = audit_status  # type: bool
        self.biz_id = biz_id  # type: str
        self.file_date = file_date  # type: str
        self.file_oss_key = file_oss_key  # type: str
        self.message = message  # type: str
        self.operate_type = operate_type  # type: str
        self.order_no = order_no  # type: str
        self.receipt_oss_key = receipt_oss_key  # type: str
        self.submitted_success = submitted_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SbjOperateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.apply_no is not None:
            result['ApplyNo'] = self.apply_no
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.file_date is not None:
            result['FileDate'] = self.file_date
        if self.file_oss_key is not None:
            result['FileOssKey'] = self.file_oss_key
        if self.message is not None:
            result['Message'] = self.message
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        if self.receipt_oss_key is not None:
            result['ReceiptOssKey'] = self.receipt_oss_key
        if self.submitted_success is not None:
            result['SubmittedSuccess'] = self.submitted_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ApplyNo') is not None:
            self.apply_no = m.get('ApplyNo')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('FileDate') is not None:
            self.file_date = m.get('FileDate')
        if m.get('FileOssKey') is not None:
            self.file_oss_key = m.get('FileOssKey')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        if m.get('ReceiptOssKey') is not None:
            self.receipt_oss_key = m.get('ReceiptOssKey')
        if m.get('SubmittedSuccess') is not None:
            self.submitted_success = m.get('SubmittedSuccess')
        return self


class SbjOperateResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SbjOperateResponseBody, self).to_map()
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


class SbjOperateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SbjOperateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SbjOperateResponse, self).to_map()
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
            temp_model = SbjOperateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SbjOperateNewRequest(TeaModel):
    def __init__(self, add_submit_count=None, allow_resubmit=None, amount=None, apply_no=None, audit_status=None,
                 biz_id=None, change_status=None, error_msg_screenshot=None, file_date=None, file_oss_key=None,
                 message=None, operate_type=None, order_no=None, receipt_oss_key=None, submitted_success=None,
                 success_type=None):
        self.add_submit_count = add_submit_count  # type: bool
        self.allow_resubmit = allow_resubmit  # type: bool
        self.amount = amount  # type: str
        self.apply_no = apply_no  # type: str
        self.audit_status = audit_status  # type: bool
        self.biz_id = biz_id  # type: str
        self.change_status = change_status  # type: bool
        self.error_msg_screenshot = error_msg_screenshot  # type: str
        self.file_date = file_date  # type: str
        self.file_oss_key = file_oss_key  # type: str
        self.message = message  # type: str
        self.operate_type = operate_type  # type: str
        self.order_no = order_no  # type: str
        self.receipt_oss_key = receipt_oss_key  # type: str
        self.submitted_success = submitted_success  # type: bool
        self.success_type = success_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SbjOperateNewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_submit_count is not None:
            result['AddSubmitCount'] = self.add_submit_count
        if self.allow_resubmit is not None:
            result['AllowResubmit'] = self.allow_resubmit
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.apply_no is not None:
            result['ApplyNo'] = self.apply_no
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.change_status is not None:
            result['ChangeStatus'] = self.change_status
        if self.error_msg_screenshot is not None:
            result['ErrorMsgScreenshot'] = self.error_msg_screenshot
        if self.file_date is not None:
            result['FileDate'] = self.file_date
        if self.file_oss_key is not None:
            result['FileOssKey'] = self.file_oss_key
        if self.message is not None:
            result['Message'] = self.message
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        if self.receipt_oss_key is not None:
            result['ReceiptOssKey'] = self.receipt_oss_key
        if self.submitted_success is not None:
            result['SubmittedSuccess'] = self.submitted_success
        if self.success_type is not None:
            result['SuccessType'] = self.success_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddSubmitCount') is not None:
            self.add_submit_count = m.get('AddSubmitCount')
        if m.get('AllowResubmit') is not None:
            self.allow_resubmit = m.get('AllowResubmit')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ApplyNo') is not None:
            self.apply_no = m.get('ApplyNo')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ChangeStatus') is not None:
            self.change_status = m.get('ChangeStatus')
        if m.get('ErrorMsgScreenshot') is not None:
            self.error_msg_screenshot = m.get('ErrorMsgScreenshot')
        if m.get('FileDate') is not None:
            self.file_date = m.get('FileDate')
        if m.get('FileOssKey') is not None:
            self.file_oss_key = m.get('FileOssKey')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        if m.get('ReceiptOssKey') is not None:
            self.receipt_oss_key = m.get('ReceiptOssKey')
        if m.get('SubmittedSuccess') is not None:
            self.submitted_success = m.get('SubmittedSuccess')
        if m.get('SuccessType') is not None:
            self.success_type = m.get('SuccessType')
        return self


class SbjOperateNewResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SbjOperateNewResponseBody, self).to_map()
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


class SbjOperateNewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SbjOperateNewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SbjOperateNewResponse, self).to_map()
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
            temp_model = SbjOperateNewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SbrainServiceExecuteRequest(TeaModel):
    def __init__(self, execute_params=None, product_code=None, reference_no=None, reference_type=None,
                 scene_code=None, scheme_id=None, service_place=None, source=None, target=None):
        self.execute_params = execute_params  # type: dict[str, any]
        self.product_code = product_code  # type: str
        self.reference_no = reference_no  # type: str
        self.reference_type = reference_type  # type: str
        self.scene_code = scene_code  # type: str
        self.scheme_id = scheme_id  # type: long
        self.service_place = service_place  # type: str
        self.source = source  # type: str
        self.target = target  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SbrainServiceExecuteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execute_params is not None:
            result['ExecuteParams'] = self.execute_params
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.reference_no is not None:
            result['ReferenceNo'] = self.reference_no
        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        if self.service_place is not None:
            result['ServicePlace'] = self.service_place
        if self.source is not None:
            result['Source'] = self.source
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecuteParams') is not None:
            self.execute_params = m.get('ExecuteParams')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReferenceNo') is not None:
            self.reference_no = m.get('ReferenceNo')
        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        if m.get('ServicePlace') is not None:
            self.service_place = m.get('ServicePlace')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class SbrainServiceExecuteShrinkRequest(TeaModel):
    def __init__(self, execute_params_shrink=None, product_code=None, reference_no=None, reference_type=None,
                 scene_code=None, scheme_id=None, service_place=None, source=None, target=None):
        self.execute_params_shrink = execute_params_shrink  # type: str
        self.product_code = product_code  # type: str
        self.reference_no = reference_no  # type: str
        self.reference_type = reference_type  # type: str
        self.scene_code = scene_code  # type: str
        self.scheme_id = scheme_id  # type: long
        self.service_place = service_place  # type: str
        self.source = source  # type: str
        self.target = target  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SbrainServiceExecuteShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execute_params_shrink is not None:
            result['ExecuteParams'] = self.execute_params_shrink
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.reference_no is not None:
            result['ReferenceNo'] = self.reference_no
        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        if self.service_place is not None:
            result['ServicePlace'] = self.service_place
        if self.source is not None:
            result['Source'] = self.source
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecuteParams') is not None:
            self.execute_params_shrink = m.get('ExecuteParams')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReferenceNo') is not None:
            self.reference_no = m.get('ReferenceNo')
        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        if m.get('ServicePlace') is not None:
            self.service_place = m.get('ServicePlace')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class SbrainServiceExecuteResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: any
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SbrainServiceExecuteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SbrainServiceExecuteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SbrainServiceExecuteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SbrainServiceExecuteResponse, self).to_map()
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
            temp_model = SbrainServiceExecuteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SbrainServiceHasRunningTaskBatchQueryRequest(TeaModel):
    def __init__(self, product_code=None, reference_nos=None, reference_type=None, source=None, task_type=None):
        self.product_code = product_code  # type: str
        self.reference_nos = reference_nos  # type: list[str]
        self.reference_type = reference_type  # type: str
        self.source = source  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SbrainServiceHasRunningTaskBatchQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.reference_nos is not None:
            result['ReferenceNos'] = self.reference_nos
        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type
        if self.source is not None:
            result['Source'] = self.source
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReferenceNos') is not None:
            self.reference_nos = m.get('ReferenceNos')
        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class SbrainServiceHasRunningTaskBatchQueryShrinkRequest(TeaModel):
    def __init__(self, product_code=None, reference_nos_shrink=None, reference_type=None, source=None,
                 task_type=None):
        self.product_code = product_code  # type: str
        self.reference_nos_shrink = reference_nos_shrink  # type: str
        self.reference_type = reference_type  # type: str
        self.source = source  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SbrainServiceHasRunningTaskBatchQueryShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.reference_nos_shrink is not None:
            result['ReferenceNos'] = self.reference_nos_shrink
        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type
        if self.source is not None:
            result['Source'] = self.source
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReferenceNos') is not None:
            self.reference_nos_shrink = m.get('ReferenceNos')
        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class SbrainServiceHasRunningTaskBatchQueryResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: any
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SbrainServiceHasRunningTaskBatchQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SbrainServiceHasRunningTaskBatchQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SbrainServiceHasRunningTaskBatchQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SbrainServiceHasRunningTaskBatchQueryResponse, self).to_map()
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
            temp_model = SbrainServiceHasRunningTaskBatchQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SbrainServiceSchemeMatchRequest(TeaModel):
    def __init__(self, match_params=None, product_code=None, reference_no=None, reference_type=None,
                 scene_code=None, source=None):
        self.match_params = match_params  # type: dict[str, any]
        self.product_code = product_code  # type: str
        self.reference_no = reference_no  # type: str
        self.reference_type = reference_type  # type: str
        self.scene_code = scene_code  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SbrainServiceSchemeMatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_params is not None:
            result['MatchParams'] = self.match_params
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.reference_no is not None:
            result['ReferenceNo'] = self.reference_no
        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MatchParams') is not None:
            self.match_params = m.get('MatchParams')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReferenceNo') is not None:
            self.reference_no = m.get('ReferenceNo')
        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class SbrainServiceSchemeMatchShrinkRequest(TeaModel):
    def __init__(self, match_params_shrink=None, product_code=None, reference_no=None, reference_type=None,
                 scene_code=None, source=None):
        self.match_params_shrink = match_params_shrink  # type: str
        self.product_code = product_code  # type: str
        self.reference_no = reference_no  # type: str
        self.reference_type = reference_type  # type: str
        self.scene_code = scene_code  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SbrainServiceSchemeMatchShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_params_shrink is not None:
            result['MatchParams'] = self.match_params_shrink
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.reference_no is not None:
            result['ReferenceNo'] = self.reference_no
        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MatchParams') is not None:
            self.match_params_shrink = m.get('MatchParams')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ReferenceNo') is not None:
            self.reference_no = m.get('ReferenceNo')
        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class SbrainServiceSchemeMatchResponseBodyDataSchemeContentContentModules(TeaModel):
    def __init__(self, tag=None, action=None, module_data=None, module_data_source=None,
                 module_data_source_type=None, name=None, target=None):
        self.tag = tag  # type: str
        self.action = action  # type: str
        self.module_data = module_data  # type: str
        self.module_data_source = module_data_source  # type: str
        self.module_data_source_type = module_data_source_type  # type: str
        self.name = name  # type: str
        self.target = target  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SbrainServiceSchemeMatchResponseBodyDataSchemeContentContentModules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.action is not None:
            result['action'] = self.action
        if self.module_data is not None:
            result['moduleData'] = self.module_data
        if self.module_data_source is not None:
            result['moduleDataSource'] = self.module_data_source
        if self.module_data_source_type is not None:
            result['moduleDataSourceType'] = self.module_data_source_type
        if self.name is not None:
            result['name'] = self.name
        if self.target is not None:
            result['target'] = self.target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('moduleData') is not None:
            self.module_data = m.get('moduleData')
        if m.get('moduleDataSource') is not None:
            self.module_data_source = m.get('moduleDataSource')
        if m.get('moduleDataSourceType') is not None:
            self.module_data_source_type = m.get('moduleDataSourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('target') is not None:
            self.target = m.get('target')
        return self


class SbrainServiceSchemeMatchResponseBodyDataSchemeContent(TeaModel):
    def __init__(self, content_index=None, content_modules=None, display=None):
        self.content_index = content_index  # type: int
        self.content_modules = content_modules  # type: list[SbrainServiceSchemeMatchResponseBodyDataSchemeContentContentModules]
        self.display = display  # type: str

    def validate(self):
        if self.content_modules:
            for k in self.content_modules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SbrainServiceSchemeMatchResponseBodyDataSchemeContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_index is not None:
            result['ContentIndex'] = self.content_index
        result['ContentModules'] = []
        if self.content_modules is not None:
            for k in self.content_modules:
                result['ContentModules'].append(k.to_map() if k else None)
        if self.display is not None:
            result['Display'] = self.display
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContentIndex') is not None:
            self.content_index = m.get('ContentIndex')
        self.content_modules = []
        if m.get('ContentModules') is not None:
            for k in m.get('ContentModules'):
                temp_model = SbrainServiceSchemeMatchResponseBodyDataSchemeContentContentModules()
                self.content_modules.append(temp_model.from_map(k))
        if m.get('Display') is not None:
            self.display = m.get('Display')
        return self


class SbrainServiceSchemeMatchResponseBodyData(TeaModel):
    def __init__(self, scene_code=None, scheme_content=None, scheme_id=None):
        self.scene_code = scene_code  # type: str
        self.scheme_content = scheme_content  # type: SbrainServiceSchemeMatchResponseBodyDataSchemeContent
        self.scheme_id = scheme_id  # type: long

    def validate(self):
        if self.scheme_content:
            self.scheme_content.validate()

    def to_map(self):
        _map = super(SbrainServiceSchemeMatchResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.scheme_content is not None:
            result['SchemeContent'] = self.scheme_content.to_map()
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('SchemeContent') is not None:
            temp_model = SbrainServiceSchemeMatchResponseBodyDataSchemeContent()
            self.scheme_content = temp_model.from_map(m['SchemeContent'])
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        return self


class SbrainServiceSchemeMatchResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: SbrainServiceSchemeMatchResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SbrainServiceSchemeMatchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SbrainServiceSchemeMatchResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SbrainServiceSchemeMatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SbrainServiceSchemeMatchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SbrainServiceSchemeMatchResponse, self).to_map()
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
            temp_model = SbrainServiceSchemeMatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTmOnsalesRequest(TeaModel):
    def __init__(self, classification=None, keyword=None, order_price_left=None, order_price_right=None,
                 page_num=None, page_size=None, product_code=None, query_all=None, reg_left=None, reg_right=None,
                 register_number=None, sort_name=None, sort_order=None, tag=None, tm_name=None, top_search=None):
        self.classification = classification  # type: str
        self.keyword = keyword  # type: str
        self.order_price_left = order_price_left  # type: long
        self.order_price_right = order_price_right  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.product_code = product_code  # type: str
        self.query_all = query_all  # type: bool
        self.reg_left = reg_left  # type: int
        self.reg_right = reg_right  # type: int
        self.register_number = register_number  # type: str
        self.sort_name = sort_name  # type: str
        self.sort_order = sort_order  # type: str
        self.tag = tag  # type: str
        self.tm_name = tm_name  # type: str
        self.top_search = top_search  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTmOnsalesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.order_price_left is not None:
            result['OrderPriceLeft'] = self.order_price_left
        if self.order_price_right is not None:
            result['OrderPriceRight'] = self.order_price_right
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.query_all is not None:
            result['QueryAll'] = self.query_all
        if self.reg_left is not None:
            result['RegLeft'] = self.reg_left
        if self.reg_right is not None:
            result['RegRight'] = self.reg_right
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.sort_name is not None:
            result['SortName'] = self.sort_name
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.top_search is not None:
            result['TopSearch'] = self.top_search
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OrderPriceLeft') is not None:
            self.order_price_left = m.get('OrderPriceLeft')
        if m.get('OrderPriceRight') is not None:
            self.order_price_right = m.get('OrderPriceRight')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QueryAll') is not None:
            self.query_all = m.get('QueryAll')
        if m.get('RegLeft') is not None:
            self.reg_left = m.get('RegLeft')
        if m.get('RegRight') is not None:
            self.reg_right = m.get('RegRight')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('SortName') is not None:
            self.sort_name = m.get('SortName')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TopSearch') is not None:
            self.top_search = m.get('TopSearch')
        return self


class SearchTmOnsalesResponseBodyTrademarks(TeaModel):
    def __init__(self, classification=None, icon=None, order_price=None, partner_code=None, product_code=None,
                 product_desc=None, registration_number=None, status=None, trademark_name=None, uid=None):
        self.classification = classification  # type: str
        self.icon = icon  # type: str
        self.order_price = order_price  # type: str
        self.partner_code = partner_code  # type: str
        self.product_code = product_code  # type: str
        self.product_desc = product_desc  # type: str
        self.registration_number = registration_number  # type: str
        self.status = status  # type: long
        self.trademark_name = trademark_name  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTmOnsalesResponseBodyTrademarks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_desc is not None:
            result['ProductDesc'] = self.product_desc
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.status is not None:
            result['Status'] = self.status
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductDesc') is not None:
            self.product_desc = m.get('ProductDesc')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class SearchTmOnsalesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, total_page_number=None,
                 trademarks=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.total_page_number = total_page_number  # type: int
        self.trademarks = trademarks  # type: list[SearchTmOnsalesResponseBodyTrademarks]

    def validate(self):
        if self.trademarks:
            for k in self.trademarks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTmOnsalesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page_number is not None:
            result['TotalPageNumber'] = self.total_page_number
        result['Trademarks'] = []
        if self.trademarks is not None:
            for k in self.trademarks:
                result['Trademarks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPageNumber') is not None:
            self.total_page_number = m.get('TotalPageNumber')
        self.trademarks = []
        if m.get('Trademarks') is not None:
            for k in m.get('Trademarks'):
                temp_model = SearchTmOnsalesResponseBodyTrademarks()
                self.trademarks.append(temp_model.from_map(k))
        return self


class SearchTmOnsalesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchTmOnsalesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchTmOnsalesResponse, self).to_map()
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
            temp_model = SearchTmOnsalesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartNotaryRequest(TeaModel):
    def __init__(self, notary_order_id=None):
        self.notary_order_id = notary_order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartNotaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        return self


class StartNotaryResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, notary_url=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.notary_url = notary_url  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartNotaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.notary_url is not None:
            result['NotaryUrl'] = self.notary_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('NotaryUrl') is not None:
            self.notary_url = m.get('NotaryUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartNotaryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartNotaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartNotaryResponse, self).to_map()
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
            temp_model = StartNotaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StoreMaterialTemporarilyRequest(TeaModel):
    def __init__(self, address=None, business_licence_oss_key=None, card_number=None, city=None,
                 contact_address=None, contact_city=None, contact_county=None, contact_district=None, contact_email=None,
                 contact_name=None, contact_number=None, contact_province=None, contact_zipcode=None, country=None,
                 eaddress=None, ename=None, id_card_name=None, id_card_number=None, id_card_oss_key=None,
                 legal_notice_oss_key=None, loa_oss_key=None, name=None, passport_oss_key=None, personal_type=None, principal_name=None,
                 province=None, region=None, town=None, type=None):
        self.address = address  # type: str
        self.business_licence_oss_key = business_licence_oss_key  # type: str
        self.card_number = card_number  # type: str
        self.city = city  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_city = contact_city  # type: str
        self.contact_county = contact_county  # type: str
        self.contact_district = contact_district  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_province = contact_province  # type: str
        self.contact_zipcode = contact_zipcode  # type: str
        self.country = country  # type: str
        self.eaddress = eaddress  # type: str
        self.ename = ename  # type: str
        self.id_card_name = id_card_name  # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_oss_key = id_card_oss_key  # type: str
        self.legal_notice_oss_key = legal_notice_oss_key  # type: str
        self.loa_oss_key = loa_oss_key  # type: str
        self.name = name  # type: str
        self.passport_oss_key = passport_oss_key  # type: str
        self.personal_type = personal_type  # type: long
        self.principal_name = principal_name  # type: int
        self.province = province  # type: str
        self.region = region  # type: str
        self.town = town  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StoreMaterialTemporarilyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.country is not None:
            result['Country'] = self.country
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        if self.town is not None:
            result['Town'] = self.town
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class StoreMaterialTemporarilyResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StoreMaterialTemporarilyResponseBody, self).to_map()
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


class StoreMaterialTemporarilyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StoreMaterialTemporarilyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StoreMaterialTemporarilyResponse, self).to_map()
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
            temp_model = StoreMaterialTemporarilyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSupplementRequest(TeaModel):
    def __init__(self, content=None, id=None, operate_type=None, upload_oss_key_list=None):
        self.content = content  # type: str
        self.id = id  # type: long
        self.operate_type = operate_type  # type: str
        self.upload_oss_key_list = upload_oss_key_list  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSupplementRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.upload_oss_key_list is not None:
            result['UploadOssKeyList'] = self.upload_oss_key_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('UploadOssKeyList') is not None:
            self.upload_oss_key_list = m.get('UploadOssKeyList')
        return self


class SubmitSupplementShrinkRequest(TeaModel):
    def __init__(self, content=None, id=None, operate_type=None, upload_oss_key_list_shrink=None):
        self.content = content  # type: str
        self.id = id  # type: long
        self.operate_type = operate_type  # type: str
        self.upload_oss_key_list_shrink = upload_oss_key_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSupplementShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.upload_oss_key_list_shrink is not None:
            result['UploadOssKeyList'] = self.upload_oss_key_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('UploadOssKeyList') is not None:
            self.upload_oss_key_list_shrink = m.get('UploadOssKeyList')
        return self


class SubmitSupplementResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSupplementResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitSupplementResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitSupplementResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitSupplementResponse, self).to_map()
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
            temp_model = SubmitSupplementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTrademarkApplicationComplaintRequest(TeaModel):
    def __init__(self, biz_id=None, content=None, files=None):
        self.biz_id = biz_id  # type: str
        self.content = content  # type: str
        self.files = files  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTrademarkApplicationComplaintRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.content is not None:
            result['Content'] = self.content
        if self.files is not None:
            result['Files'] = self.files
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Files') is not None:
            self.files = m.get('Files')
        return self


class SubmitTrademarkApplicationComplaintShrinkRequest(TeaModel):
    def __init__(self, biz_id=None, content=None, files_shrink=None):
        self.biz_id = biz_id  # type: str
        self.content = content  # type: str
        self.files_shrink = files_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTrademarkApplicationComplaintShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.content is not None:
            result['Content'] = self.content
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        return self


class SubmitTrademarkApplicationComplaintResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTrademarkApplicationComplaintResponseBody, self).to_map()
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


class SubmitTrademarkApplicationComplaintResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitTrademarkApplicationComplaintResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitTrademarkApplicationComplaintResponse, self).to_map()
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
            temp_model = SubmitTrademarkApplicationComplaintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncTrademarkRequest(TeaModel):
    def __init__(self, begin_time=None, classification_code=None, description=None, end_time=None, label=None,
                 original_price=None, owner_en_name=None, owner_name=None, reason=None, reg_ann_date=None,
                 secondary_classification=None, status=None, third_classification=None, tm_icon=None, tm_name=None, tm_number=None, type=None):
        self.begin_time = begin_time  # type: long
        self.classification_code = classification_code  # type: str
        self.description = description  # type: str
        self.end_time = end_time  # type: long
        self.label = label  # type: str
        self.original_price = original_price  # type: float
        self.owner_en_name = owner_en_name  # type: str
        self.owner_name = owner_name  # type: str
        self.reason = reason  # type: str
        self.reg_ann_date = reg_ann_date  # type: long
        self.secondary_classification = secondary_classification  # type: str
        self.status = status  # type: str
        self.third_classification = third_classification  # type: str
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_number = tm_number  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncTrademarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.label is not None:
            result['Label'] = self.label
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.status is not None:
            result['Status'] = self.status
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SyncTrademarkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncTrademarkResponseBody, self).to_map()
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


class SyncTrademarkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SyncTrademarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SyncTrademarkResponse, self).to_map()
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
            temp_model = SyncTrademarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicantContacterRequest(TeaModel):
    def __init__(self, applicant_id=None, biz_id=None, contact_address=None, contact_city=None,
                 contact_district=None, contact_email=None, contact_name=None, contact_number=None, contact_province=None,
                 contact_zip_code=None):
        self.applicant_id = applicant_id  # type: long
        self.biz_id = biz_id  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_city = contact_city  # type: str
        self.contact_district = contact_district  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_province = contact_province  # type: str
        self.contact_zip_code = contact_zip_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicantContacterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        return self


class UpdateApplicantContacterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicantContacterResponseBody, self).to_map()
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


class UpdateApplicantContacterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateApplicantContacterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApplicantContacterResponse, self).to_map()
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
            temp_model = UpdateApplicantContacterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMaterialRequest(TeaModel):
    def __init__(self, address=None, business_licence_oss_key=None, card_number=None, city=None,
                 contact_address=None, contact_city=None, contact_county=None, contact_district=None, contact_email=None,
                 contact_name=None, contact_number=None, contact_province=None, contact_zipcode=None, eaddress=None, ename=None,
                 id=None, id_card_name=None, id_card_number=None, id_card_oss_key=None, legal_notice_oss_key=None,
                 loa_id=None, loa_oss_key=None, name=None, passport_oss_key=None, personal_type=None, province=None,
                 town=None):
        self.address = address  # type: str
        self.business_licence_oss_key = business_licence_oss_key  # type: str
        self.card_number = card_number  # type: str
        self.city = city  # type: str
        self.contact_address = contact_address  # type: str
        self.contact_city = contact_city  # type: str
        self.contact_county = contact_county  # type: str
        self.contact_district = contact_district  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_number = contact_number  # type: str
        self.contact_province = contact_province  # type: str
        self.contact_zipcode = contact_zipcode  # type: str
        self.eaddress = eaddress  # type: str
        self.ename = ename  # type: str
        self.id = id  # type: long
        self.id_card_name = id_card_name  # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_oss_key = id_card_oss_key  # type: str
        self.legal_notice_oss_key = legal_notice_oss_key  # type: str
        self.loa_id = loa_id  # type: long
        self.loa_oss_key = loa_oss_key  # type: str
        self.name = name  # type: str
        self.passport_oss_key = passport_oss_key  # type: str
        self.personal_type = personal_type  # type: long
        self.province = province  # type: str
        self.town = town  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.city is not None:
            result['City'] = self.city
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.ename is not None:
            result['EName'] = self.ename
        if self.id is not None:
            result['Id'] = self.id
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.loa_id is not None:
            result['LoaId'] = self.loa_id
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.personal_type is not None:
            result['PersonalType'] = self.personal_type
        if self.province is not None:
            result['Province'] = self.province
        if self.town is not None:
            result['Town'] = self.town
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('LoaId') is not None:
            self.loa_id = m.get('LoaId')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('PersonalType') is not None:
            self.personal_type = m.get('PersonalType')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        return self


class UpdateMaterialResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMaterialResponseBody, self).to_map()
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


class UpdateMaterialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateMaterialResponse, self).to_map()
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
            temp_model = UpdateMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProduceRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, ext_map=None, operate_type=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.ext_map = ext_map  # type: str
        self.operate_type = operate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProduceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.ext_map is not None:
            result['ExtMap'] = self.ext_map
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtMap') is not None:
            self.ext_map = m.get('ExtMap')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class UpdateProduceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProduceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProduceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateProduceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProduceResponse, self).to_map()
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
            temp_model = UpdateProduceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProduceLoaIdRequest(TeaModel):
    def __init__(self, biz_id=None, loa_oss_key=None):
        self.biz_id = biz_id  # type: str
        self.loa_oss_key = loa_oss_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProduceLoaIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        return self


class UpdateProduceLoaIdResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProduceLoaIdResponseBody, self).to_map()
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


class UpdateProduceLoaIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateProduceLoaIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProduceLoaIdResponse, self).to_map()
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
            temp_model = UpdateProduceLoaIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSendMaterialNumRequest(TeaModel):
    def __init__(self, biz_id=None, num=None, operate_type=None):
        self.biz_id = biz_id  # type: str
        self.num = num  # type: str
        self.operate_type = operate_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSendMaterialNumRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.num is not None:
            result['Num'] = self.num
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class UpdateSendMaterialNumResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSendMaterialNumResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSendMaterialNumResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSendMaterialNumResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSendMaterialNumResponse, self).to_map()
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
            temp_model = UpdateSendMaterialNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrademarkNameRequest(TeaModel):
    def __init__(self, biz_id=None, client_token=None, tm_comment=None, tm_icon=None, tm_name=None, type=None):
        self.biz_id = biz_id  # type: str
        self.client_token = client_token  # type: str
        self.tm_comment = tm_comment  # type: str
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.type = type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTrademarkNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateTrademarkNameResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTrademarkNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTrademarkNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTrademarkNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTrademarkNameResponse, self).to_map()
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
            temp_model = UpdateTrademarkNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrademarkOnsaleRequest(TeaModel):
    def __init__(self, begin_time=None, classification_code=None, description=None, end_time=None, label=None,
                 original_price=None, owner_en_name=None, owner_name=None, reason=None, reg_ann_date=None,
                 secondary_classification=None, third_classification=None, tm_icon=None, tm_name=None, tm_number=None, tm_type=None,
                 trade_tm_detail_json=None, type=None):
        self.begin_time = begin_time  # type: long
        self.classification_code = classification_code  # type: str
        self.description = description  # type: str
        self.end_time = end_time  # type: long
        self.label = label  # type: str
        self.original_price = original_price  # type: float
        self.owner_en_name = owner_en_name  # type: str
        self.owner_name = owner_name  # type: str
        self.reason = reason  # type: str
        self.reg_ann_date = reg_ann_date  # type: long
        self.secondary_classification = secondary_classification  # type: str
        self.third_classification = third_classification  # type: str
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_number = tm_number  # type: str
        self.tm_type = tm_type  # type: str
        self.trade_tm_detail_json = trade_tm_detail_json  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTrademarkOnsaleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.label is not None:
            result['Label'] = self.label
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.tm_type is not None:
            result['TmType'] = self.tm_type
        if self.trade_tm_detail_json is not None:
            result['TradeTmDetailJson'] = self.trade_tm_detail_json
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TmType') is not None:
            self.tm_type = m.get('TmType')
        if m.get('TradeTmDetailJson') is not None:
            self.trade_tm_detail_json = m.get('TradeTmDetailJson')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateTrademarkOnsaleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTrademarkOnsaleResponseBody, self).to_map()
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


class UpdateTrademarkOnsaleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTrademarkOnsaleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTrademarkOnsaleResponse, self).to_map()
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
            temp_model = UpdateTrademarkOnsaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadNotaryDataRequest(TeaModel):
    def __init__(self, biz_order_no=None, notary_type=None, upload_context=None):
        self.biz_order_no = biz_order_no  # type: str
        self.notary_type = notary_type  # type: int
        self.upload_context = upload_context  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadNotaryDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_order_no is not None:
            result['BizOrderNo'] = self.biz_order_no
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.upload_context is not None:
            result['UploadContext'] = self.upload_context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizOrderNo') is not None:
            self.biz_order_no = m.get('BizOrderNo')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('UploadContext') is not None:
            self.upload_context = m.get('UploadContext')
        return self


class UploadNotaryDataResponseBody(TeaModel):
    def __init__(self, request_id=None, user_auth_url=None):
        self.request_id = request_id  # type: str
        self.user_auth_url = user_auth_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadNotaryDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_auth_url is not None:
            result['UserAuthUrl'] = self.user_auth_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserAuthUrl') is not None:
            self.user_auth_url = m.get('UserAuthUrl')
        return self


class UploadNotaryDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UploadNotaryDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadNotaryDataResponse, self).to_map()
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
            temp_model = UploadNotaryDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadTrademarkOnSaleRequest(TeaModel):
    def __init__(self, begin_time=None, classification_code=None, description=None, end_time=None, label=None,
                 original_price=None, owner_en_name=None, owner_name=None, reason=None, reg_ann_date=None,
                 secondary_classification=None, status=None, third_classification=None, tm_icon=None, tm_name=None, tm_number=None,
                 tm_type=None, trade_tm_detail_json=None, type=None):
        self.begin_time = begin_time  # type: long
        self.classification_code = classification_code  # type: str
        self.description = description  # type: str
        self.end_time = end_time  # type: long
        self.label = label  # type: str
        self.original_price = original_price  # type: float
        self.owner_en_name = owner_en_name  # type: str
        self.owner_name = owner_name  # type: str
        self.reason = reason  # type: str
        self.reg_ann_date = reg_ann_date  # type: long
        self.secondary_classification = secondary_classification  # type: str
        self.status = status  # type: str
        self.third_classification = third_classification  # type: str
        self.tm_icon = tm_icon  # type: str
        self.tm_name = tm_name  # type: str
        self.tm_number = tm_number  # type: str
        self.tm_type = tm_type  # type: str
        self.trade_tm_detail_json = trade_tm_detail_json  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadTrademarkOnSaleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.label is not None:
            result['Label'] = self.label
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.status is not None:
            result['Status'] = self.status
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.tm_type is not None:
            result['TmType'] = self.tm_type
        if self.trade_tm_detail_json is not None:
            result['TradeTmDetailJson'] = self.trade_tm_detail_json
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('TmType') is not None:
            self.tm_type = m.get('TmType')
        if m.get('TradeTmDetailJson') is not None:
            self.trade_tm_detail_json = m.get('TradeTmDetailJson')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UploadTrademarkOnSaleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadTrademarkOnSaleResponseBody, self).to_map()
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


class UploadTrademarkOnSaleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UploadTrademarkOnSaleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadTrademarkOnSaleResponse, self).to_map()
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
            temp_model = UploadTrademarkOnSaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteCommunicationLogRequest(TeaModel):
    def __init__(self, biz_id=None, note=None, target_id=None):
        self.biz_id = biz_id  # type: str
        self.note = note  # type: str
        self.target_id = target_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WriteCommunicationLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        return self


class WriteCommunicationLogResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(WriteCommunicationLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class WriteCommunicationLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: WriteCommunicationLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(WriteCommunicationLogResponse, self).to_map()
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
            temp_model = WriteCommunicationLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteIntentionCommunicationLogRequest(TeaModel):
    def __init__(self, biz_id=None, note=None, reject=None):
        self.biz_id = biz_id  # type: str
        self.note = note  # type: str
        self.reject = reject  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(WriteIntentionCommunicationLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        if self.reject is not None:
            result['Reject'] = self.reject
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Reject') is not None:
            self.reject = m.get('Reject')
        return self


class WriteIntentionCommunicationLogResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(WriteIntentionCommunicationLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class WriteIntentionCommunicationLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: WriteIntentionCommunicationLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(WriteIntentionCommunicationLogResponse, self).to_map()
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
            temp_model = WriteIntentionCommunicationLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


