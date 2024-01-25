# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CardOcrRequest(TeaModel):
    def __init__(self, doc_type=None, id_face_quality=None, id_ocr_picture_base_64=None, id_ocr_picture_url=None,
                 merchant_biz_id=None, merchant_user_id=None, ocr=None, product_code=None, spoof=None):
        self.doc_type = doc_type  # type: str
        self.id_face_quality = id_face_quality  # type: str
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64  # type: str
        self.id_ocr_picture_url = id_ocr_picture_url  # type: str
        self.merchant_biz_id = merchant_biz_id  # type: str
        self.merchant_user_id = merchant_user_id  # type: str
        self.ocr = ocr  # type: str
        self.product_code = product_code  # type: str
        self.spoof = spoof  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CardOcrRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.id_face_quality is not None:
            result['IdFaceQuality'] = self.id_face_quality
        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64
        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.ocr is not None:
            result['Ocr'] = self.ocr
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.spoof is not None:
            result['Spoof'] = self.spoof
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('IdFaceQuality') is not None:
            self.id_face_quality = m.get('IdFaceQuality')
        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')
        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Spoof') is not None:
            self.spoof = m.get('Spoof')
        return self


class CardOcrResponseBodyResult(TeaModel):
    def __init__(self, ext_card_info=None, ext_id_info=None, passed=None, sub_code=None, transaction_id=None):
        self.ext_card_info = ext_card_info  # type: str
        self.ext_id_info = ext_id_info  # type: str
        self.passed = passed  # type: str
        self.sub_code = sub_code  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CardOcrResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_card_info is not None:
            result['ExtCardInfo'] = self.ext_card_info
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtCardInfo') is not None:
            self.ext_card_info = m.get('ExtCardInfo')
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class CardOcrResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: CardOcrResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CardOcrResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CardOcrResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CardOcrResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CardOcrResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CardOcrResponse, self).to_map()
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
            temp_model = CardOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckResultRequest(TeaModel):
    def __init__(self, extra_image_control_list=None, is_return_image=None, merchant_biz_id=None,
                 return_five_category_spoof_result=None, transaction_id=None):
        self.extra_image_control_list = extra_image_control_list  # type: str
        self.is_return_image = is_return_image  # type: str
        self.merchant_biz_id = merchant_biz_id  # type: str
        self.return_five_category_spoof_result = return_five_category_spoof_result  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_image_control_list is not None:
            result['ExtraImageControlList'] = self.extra_image_control_list
        if self.is_return_image is not None:
            result['IsReturnImage'] = self.is_return_image
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.return_five_category_spoof_result is not None:
            result['ReturnFiveCategorySpoofResult'] = self.return_five_category_spoof_result
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtraImageControlList') is not None:
            self.extra_image_control_list = m.get('ExtraImageControlList')
        if m.get('IsReturnImage') is not None:
            self.is_return_image = m.get('IsReturnImage')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('ReturnFiveCategorySpoofResult') is not None:
            self.return_five_category_spoof_result = m.get('ReturnFiveCategorySpoofResult')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class CheckResultResponseBodyResult(TeaModel):
    def __init__(self, ekyc_result=None, ext_basic_info=None, ext_face_info=None, ext_id_info=None,
                 ext_risk_info=None, passed=None, sub_code=None):
        self.ekyc_result = ekyc_result  # type: str
        self.ext_basic_info = ext_basic_info  # type: str
        self.ext_face_info = ext_face_info  # type: str
        self.ext_id_info = ext_id_info  # type: str
        self.ext_risk_info = ext_risk_info  # type: str
        self.passed = passed  # type: str
        self.sub_code = sub_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckResultResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ekyc_result is not None:
            result['EkycResult'] = self.ekyc_result
        if self.ext_basic_info is not None:
            result['ExtBasicInfo'] = self.ext_basic_info
        if self.ext_face_info is not None:
            result['ExtFaceInfo'] = self.ext_face_info
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info
        if self.ext_risk_info is not None:
            result['ExtRiskInfo'] = self.ext_risk_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EkycResult') is not None:
            self.ekyc_result = m.get('EkycResult')
        if m.get('ExtBasicInfo') is not None:
            self.ext_basic_info = m.get('ExtBasicInfo')
        if m.get('ExtFaceInfo') is not None:
            self.ext_face_info = m.get('ExtFaceInfo')
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')
        if m.get('ExtRiskInfo') is not None:
            self.ext_risk_info = m.get('ExtRiskInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class CheckResultResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: CheckResultResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CheckResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CheckResultResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CheckResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckResultResponse, self).to_map()
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
            temp_model = CheckResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePictureRequest(TeaModel):
    def __init__(self, delete_pic_after_query=None, transaction_id=None):
        self.delete_pic_after_query = delete_pic_after_query  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePictureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_pic_after_query is not None:
            result['DeletePicAfterQuery'] = self.delete_pic_after_query
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeletePicAfterQuery') is not None:
            self.delete_pic_after_query = m.get('DeletePicAfterQuery')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DeletePictureResponseBodyResult(TeaModel):
    def __init__(self, delete_result=None, transaction_id=None):
        self.delete_result = delete_result  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePictureResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_result is not None:
            result['DeleteResult'] = self.delete_result
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeleteResult') is not None:
            self.delete_result = m.get('DeleteResult')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DeletePictureResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: DeletePictureResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeletePictureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeletePictureResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeletePictureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePictureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePictureResponse, self).to_map()
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
            temp_model = DeletePictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVerifyResultRequest(TeaModel):
    def __init__(self, delete_after_query=None, delete_type=None, transaction_id=None):
        self.delete_after_query = delete_after_query  # type: str
        self.delete_type = delete_type  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVerifyResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_after_query is not None:
            result['DeleteAfterQuery'] = self.delete_after_query
        if self.delete_type is not None:
            result['DeleteType'] = self.delete_type
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeleteAfterQuery') is not None:
            self.delete_after_query = m.get('DeleteAfterQuery')
        if m.get('DeleteType') is not None:
            self.delete_type = m.get('DeleteType')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DeleteVerifyResultResponseBodyResult(TeaModel):
    def __init__(self, delete_result=None, transaction_id=None):
        self.delete_result = delete_result  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVerifyResultResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_result is not None:
            result['DeleteResult'] = self.delete_result
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeleteResult') is not None:
            self.delete_result = m.get('DeleteResult')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DeleteVerifyResultResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DeleteVerifyResultResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DeleteVerifyResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DeleteVerifyResultResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DeleteVerifyResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVerifyResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVerifyResultResponse, self).to_map()
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
            temp_model = DeleteVerifyResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAddressLabelsRequest(TeaModel):
    def __init__(self, address=None, coin=None, merchant_biz_id=None):
        self.address = address  # type: str
        self.coin = coin  # type: str
        self.merchant_biz_id = merchant_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAddressLabelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.coin is not None:
            result['Coin'] = self.coin
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Coin') is not None:
            self.coin = m.get('Coin')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        return self


class DescribeAddressLabelsResponseBodyData(TeaModel):
    def __init__(self, label_list=None):
        self.label_list = label_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAddressLabelsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_list is not None:
            result['LabelList'] = self.label_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LabelList') is not None:
            self.label_list = m.get('LabelList')
        return self


class DescribeAddressLabelsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeAddressLabelsResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAddressLabelsResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeAddressLabelsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAddressLabelsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAddressLabelsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAddressLabelsResponse, self).to_map()
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
            temp_model = DescribeAddressLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAddressOverviewRequest(TeaModel):
    def __init__(self, address=None, coin=None, merchant_biz_id=None):
        self.address = address  # type: str
        self.coin = coin  # type: str
        self.merchant_biz_id = merchant_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAddressOverviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.coin is not None:
            result['Coin'] = self.coin
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Coin') is not None:
            self.coin = m.get('Coin')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        return self


class DescribeAddressOverviewResponseBodyData(TeaModel):
    def __init__(self, balance=None, first_seen=None, last_seen=None, received_txs_count=None, spent_txs_count=None,
                 total_received=None, total_spent=None, txs_count=None):
        self.balance = balance  # type: float
        self.first_seen = first_seen  # type: long
        self.last_seen = last_seen  # type: long
        self.received_txs_count = received_txs_count  # type: int
        self.spent_txs_count = spent_txs_count  # type: int
        self.total_received = total_received  # type: float
        self.total_spent = total_spent  # type: float
        self.txs_count = txs_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAddressOverviewResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.first_seen is not None:
            result['FirstSeen'] = self.first_seen
        if self.last_seen is not None:
            result['LastSeen'] = self.last_seen
        if self.received_txs_count is not None:
            result['ReceivedTxsCount'] = self.received_txs_count
        if self.spent_txs_count is not None:
            result['SpentTxsCount'] = self.spent_txs_count
        if self.total_received is not None:
            result['TotalReceived'] = self.total_received
        if self.total_spent is not None:
            result['TotalSpent'] = self.total_spent
        if self.txs_count is not None:
            result['TxsCount'] = self.txs_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('FirstSeen') is not None:
            self.first_seen = m.get('FirstSeen')
        if m.get('LastSeen') is not None:
            self.last_seen = m.get('LastSeen')
        if m.get('ReceivedTxsCount') is not None:
            self.received_txs_count = m.get('ReceivedTxsCount')
        if m.get('SpentTxsCount') is not None:
            self.spent_txs_count = m.get('SpentTxsCount')
        if m.get('TotalReceived') is not None:
            self.total_received = m.get('TotalReceived')
        if m.get('TotalSpent') is not None:
            self.total_spent = m.get('TotalSpent')
        if m.get('TxsCount') is not None:
            self.txs_count = m.get('TxsCount')
        return self


class DescribeAddressOverviewResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeAddressOverviewResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAddressOverviewResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeAddressOverviewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAddressOverviewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAddressOverviewResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAddressOverviewResponse, self).to_map()
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
            temp_model = DescribeAddressOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMaliciousAddressRequest(TeaModel):
    def __init__(self, coin=None, end=None, merchant_biz_id=None, start=None):
        self.coin = coin  # type: str
        self.end = end  # type: str
        self.merchant_biz_id = merchant_biz_id  # type: str
        self.start = start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMaliciousAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coin is not None:
            result['Coin'] = self.coin
        if self.end is not None:
            result['End'] = self.end
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Coin') is not None:
            self.coin = m.get('Coin')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class DescribeMaliciousAddressResponseBodyData(TeaModel):
    def __init__(self, add_time=None, address=None, coin=None, detail=None, tag=None):
        self.add_time = add_time  # type: str
        self.address = address  # type: str
        self.coin = coin  # type: str
        self.detail = detail  # type: str
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMaliciousAddressResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_time is not None:
            result['AddTime'] = self.add_time
        if self.address is not None:
            result['Address'] = self.address
        if self.coin is not None:
            result['Coin'] = self.coin
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Coin') is not None:
            self.coin = m.get('Coin')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeMaliciousAddressResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[DescribeMaliciousAddressResponseBodyData]
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMaliciousAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeMaliciousAddressResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeMaliciousAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeMaliciousAddressResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMaliciousAddressResponse, self).to_map()
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
            temp_model = DescribeMaliciousAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskScoreRequest(TeaModel):
    def __init__(self, address=None, coin=None, merchant_biz_id=None):
        self.address = address  # type: str
        self.coin = coin  # type: str
        self.merchant_biz_id = merchant_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRiskScoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.coin is not None:
            result['Coin'] = self.coin
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Coin') is not None:
            self.coin = m.get('Coin')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        return self


class DescribeRiskScoreResponseBodyData(TeaModel):
    def __init__(self, detail_list=None, hacking_event=None, risk_level=None, score=None):
        self.detail_list = detail_list  # type: list[str]
        self.hacking_event = hacking_event  # type: str
        self.risk_level = risk_level  # type: str
        self.score = score  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRiskScoreResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_list is not None:
            result['DetailList'] = self.detail_list
        if self.hacking_event is not None:
            result['HackingEvent'] = self.hacking_event
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DetailList') is not None:
            self.detail_list = m.get('DetailList')
        if m.get('HackingEvent') is not None:
            self.hacking_event = m.get('HackingEvent')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class DescribeRiskScoreResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeRiskScoreResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeRiskScoreResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeRiskScoreResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRiskScoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRiskScoreResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRiskScoreResponse, self).to_map()
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
            temp_model = DescribeRiskScoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTransactionsListRequest(TeaModel):
    def __init__(self, address=None, coin=None, end_timestamp=None, merchant_biz_id=None, page=None,
                 start_timestamp=None, type=None):
        self.address = address  # type: str
        self.coin = coin  # type: str
        self.end_timestamp = end_timestamp  # type: long
        self.merchant_biz_id = merchant_biz_id  # type: str
        self.page = page  # type: long
        self.start_timestamp = start_timestamp  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTransactionsListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.coin is not None:
            result['Coin'] = self.coin
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.page is not None:
            result['Page'] = self.page
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Coin') is not None:
            self.coin = m.get('Coin')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeTransactionsListResponseBodyDataIn(TeaModel):
    def __init__(self, address=None, amount=None, label=None, tx_hash_list=None, type=None):
        self.address = address  # type: str
        self.amount = amount  # type: float
        self.label = label  # type: str
        self.tx_hash_list = tx_hash_list  # type: list[str]
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTransactionsListResponseBodyDataIn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.label is not None:
            result['Label'] = self.label
        if self.tx_hash_list is not None:
            result['TxHashList'] = self.tx_hash_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('TxHashList') is not None:
            self.tx_hash_list = m.get('TxHashList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeTransactionsListResponseBodyDataOut(TeaModel):
    def __init__(self, address=None, amount=None, label=None, tx_hash_list=None, type=None):
        self.address = address  # type: str
        self.amount = amount  # type: float
        self.label = label  # type: str
        self.tx_hash_list = tx_hash_list  # type: list[str]
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTransactionsListResponseBodyDataOut, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.label is not None:
            result['Label'] = self.label
        if self.tx_hash_list is not None:
            result['TxHashList'] = self.tx_hash_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('TxHashList') is not None:
            self.tx_hash_list = m.get('TxHashList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeTransactionsListResponseBodyData(TeaModel):
    def __init__(self, in_=None, out=None, page=None, total_pages=None, transactions_on_page=None):
        self.in_ = in_  # type: list[DescribeTransactionsListResponseBodyDataIn]
        self.out = out  # type: list[DescribeTransactionsListResponseBodyDataOut]
        self.page = page  # type: long
        self.total_pages = total_pages  # type: long
        self.transactions_on_page = transactions_on_page  # type: long

    def validate(self):
        if self.in_:
            for k in self.in_:
                if k:
                    k.validate()
        if self.out:
            for k in self.out:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTransactionsListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['In'] = []
        if self.in_ is not None:
            for k in self.in_:
                result['In'].append(k.to_map() if k else None)
        result['Out'] = []
        if self.out is not None:
            for k in self.out:
                result['Out'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.transactions_on_page is not None:
            result['TransactionsOnPage'] = self.transactions_on_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.in_ = []
        if m.get('In') is not None:
            for k in m.get('In'):
                temp_model = DescribeTransactionsListResponseBodyDataIn()
                self.in_.append(temp_model.from_map(k))
        self.out = []
        if m.get('Out') is not None:
            for k in m.get('Out'):
                temp_model = DescribeTransactionsListResponseBodyDataOut()
                self.out.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TransactionsOnPage') is not None:
            self.transactions_on_page = m.get('TransactionsOnPage')
        return self


class DescribeTransactionsListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeTransactionsListResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeTransactionsListResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeTransactionsListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeTransactionsListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTransactionsListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTransactionsListResponse, self).to_map()
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
            temp_model = DescribeTransactionsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWeb3AddressLabelsRequest(TeaModel):
    def __init__(self, address=None, chain_short_name=None, merchant_biz_id=None):
        # The address hash.
        self.address = address  # type: str
        # This is the short name of blockchain。
        # [ ETH, MATIC, BNB ]
        self.chain_short_name = chain_short_name  # type: str
        # A unique business ID for tracing purpose. For example，the sequence ID from the merchant\"s business-related database.
        self.merchant_biz_id = merchant_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWeb3AddressLabelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.chain_short_name is not None:
            result['ChainShortName'] = self.chain_short_name
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ChainShortName') is not None:
            self.chain_short_name = m.get('ChainShortName')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        return self


class DescribeWeb3AddressLabelsResponseBodyData(TeaModel):
    def __init__(self, address=None, balance=None, balance_symbol=None, chain_name=None, chain_short_name=None,
                 contract_address=None, create_contract_address=None, create_contract_transaction_hash=None,
                 custom_risk_assessment=None, first_transaction_time=None, is_producer_address=None, last_transaction_time=None,
                 receive_amount=None, send_amount=None, tag=None, token=None, token_amount=None, token_list=None,
                 transaction_count=None):
        # address
        self.address = address  # type: str
        # amount of native currency
        self.balance = balance  # type: str
        # native currency of the chain
        self.balance_symbol = balance_symbol  # type: str
        # ChainNameEnumstring name of blockchain
        self.chain_name = chain_name  # type: str
        # ChainShortName
        self.chain_short_name = chain_short_name  # type: str
        # 0: EOA; 1: Contract
        self.contract_address = contract_address  # type: str
        # the address of deployer if the current address is a contract, null if the current address is an EOA
        self.create_contract_address = create_contract_address  # type: str
        # contract creation hash if the current address is a contract, null if the current address is an EOA
        self.create_contract_transaction_hash = create_contract_transaction_hash  # type: str
        # customized assessment detail
        self.custom_risk_assessment = custom_risk_assessment  # type: str
        # the first transaction hash sent by the address
        self.first_transaction_time = first_transaction_time  # type: str
        # 0: Not validator; 1: validator
        self.is_producer_address = is_producer_address  # type: str
        # the latest transaction hash sent by the address
        self.last_transaction_time = last_transaction_time  # type: str
        # the amount of native currency received in 180 days
        self.receive_amount = receive_amount  # type: str
        # the amount of native currency sent in 180 days
        self.send_amount = send_amount  # type: str
        # tag
        self.tag = tag  # type: str
        # if the address is an erc20 token, returns the token name
        self.token = token  # type: str
        # the number of erc20 tokens involved with current address in 180 days
        self.token_amount = token_amount  # type: int
        # address of erc20 tokens involved with current address in 180 days
        self.token_list = token_list  # type: str
        # the number of transactions
        self.transaction_count = transaction_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWeb3AddressLabelsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.balance_symbol is not None:
            result['BalanceSymbol'] = self.balance_symbol
        if self.chain_name is not None:
            result['ChainName'] = self.chain_name
        if self.chain_short_name is not None:
            result['ChainShortName'] = self.chain_short_name
        if self.contract_address is not None:
            result['ContractAddress'] = self.contract_address
        if self.create_contract_address is not None:
            result['CreateContractAddress'] = self.create_contract_address
        if self.create_contract_transaction_hash is not None:
            result['CreateContractTransactionHash'] = self.create_contract_transaction_hash
        if self.custom_risk_assessment is not None:
            result['CustomRiskAssessment'] = self.custom_risk_assessment
        if self.first_transaction_time is not None:
            result['FirstTransactionTime'] = self.first_transaction_time
        if self.is_producer_address is not None:
            result['IsProducerAddress'] = self.is_producer_address
        if self.last_transaction_time is not None:
            result['LastTransactionTime'] = self.last_transaction_time
        if self.receive_amount is not None:
            result['ReceiveAmount'] = self.receive_amount
        if self.send_amount is not None:
            result['SendAmount'] = self.send_amount
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.token is not None:
            result['Token'] = self.token
        if self.token_amount is not None:
            result['TokenAmount'] = self.token_amount
        if self.token_list is not None:
            result['TokenList'] = self.token_list
        if self.transaction_count is not None:
            result['TransactionCount'] = self.transaction_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('BalanceSymbol') is not None:
            self.balance_symbol = m.get('BalanceSymbol')
        if m.get('ChainName') is not None:
            self.chain_name = m.get('ChainName')
        if m.get('ChainShortName') is not None:
            self.chain_short_name = m.get('ChainShortName')
        if m.get('ContractAddress') is not None:
            self.contract_address = m.get('ContractAddress')
        if m.get('CreateContractAddress') is not None:
            self.create_contract_address = m.get('CreateContractAddress')
        if m.get('CreateContractTransactionHash') is not None:
            self.create_contract_transaction_hash = m.get('CreateContractTransactionHash')
        if m.get('CustomRiskAssessment') is not None:
            self.custom_risk_assessment = m.get('CustomRiskAssessment')
        if m.get('FirstTransactionTime') is not None:
            self.first_transaction_time = m.get('FirstTransactionTime')
        if m.get('IsProducerAddress') is not None:
            self.is_producer_address = m.get('IsProducerAddress')
        if m.get('LastTransactionTime') is not None:
            self.last_transaction_time = m.get('LastTransactionTime')
        if m.get('ReceiveAmount') is not None:
            self.receive_amount = m.get('ReceiveAmount')
        if m.get('SendAmount') is not None:
            self.send_amount = m.get('SendAmount')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TokenAmount') is not None:
            self.token_amount = m.get('TokenAmount')
        if m.get('TokenList') is not None:
            self.token_list = m.get('TokenList')
        if m.get('TransactionCount') is not None:
            self.transaction_count = m.get('TransactionCount')
        return self


class DescribeWeb3AddressLabelsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None):
        # Return code. For the full list of codes, see Codes and Messages.
        self.code = code  # type: str
        # data
        self.data = data  # type: DescribeWeb3AddressLabelsResponseBodyData
        # The HTTP status code
        self.http_status_code = http_status_code  # type: int
        # Response detailed message.
        self.message = message  # type: str
        # The unique ID of the request, which can be used to locate issues.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeWeb3AddressLabelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = DescribeWeb3AddressLabelsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWeb3AddressLabelsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWeb3AddressLabelsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWeb3AddressLabelsResponse, self).to_map()
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
            temp_model = DescribeWeb3AddressLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWeb3RiskScoreRequest(TeaModel):
    def __init__(self, chain_short_name=None, depth=None, merchant_biz_id=None, object_id=None, object_type=None):
        # This is the short name of blockchain。
        # [ ETH, MATIC, BNB ]
        self.chain_short_name = chain_short_name  # type: str
        # minimum: 1
        # maximum: 100
        # the maximum depth for risk analysis. For UTXO-based blockchains, default and maximum is enforced at 100.
        # For account-based blockchains, default and maximum is enforced at 6
        self.depth = depth  # type: int
        # A unique business ID for tracing purpose. For example，the sequence ID from the merchant\"s business-related database.
        self.merchant_biz_id = merchant_biz_id  # type: str
        # For TRANSACTION objects, you need to provide the transaction hash。
        # For ADDRESS objects, you need to provide the address or reference address hash。
        self.object_id = object_id  # type: str
        # The object of the analysis.
        # [ TRANSACTION, ADDRESS ]
        self.object_type = object_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWeb3RiskScoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_short_name is not None:
            result['ChainShortName'] = self.chain_short_name
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChainShortName') is not None:
            self.chain_short_name = m.get('ChainShortName')
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        return self


class DescribeWeb3RiskScoreResponseBodyDataRiskResults(TeaModel):
    def __init__(self, description=None, severity=None, type=None):
        # description
        self.description = description  # type: str
        # [ CRITICAL, HIGH, MEDIUM, LOW, NO ]
        # 100: Critical
        # 67-99: High risk
        # 34-66: Medium risk
        # 1-33: Low risk
        # 0: No risk
        self.severity = severity  # type: str
        # Address
        # Transaction
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWeb3RiskScoreResponseBodyDataRiskResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeWeb3RiskScoreResponseBodyData(TeaModel):
    def __init__(self, risk_results=None, score=None):
        # risk results
        self.risk_results = risk_results  # type: list[DescribeWeb3RiskScoreResponseBodyDataRiskResults]
        # Risk score
        self.score = score  # type: str

    def validate(self):
        if self.risk_results:
            for k in self.risk_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWeb3RiskScoreResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RiskResults'] = []
        if self.risk_results is not None:
            for k in self.risk_results:
                result['RiskResults'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.risk_results = []
        if m.get('RiskResults') is not None:
            for k in m.get('RiskResults'):
                temp_model = DescribeWeb3RiskScoreResponseBodyDataRiskResults()
                self.risk_results.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class DescribeWeb3RiskScoreResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None):
        # Return code. For the full list of codes, see Codes and Messages.
        self.code = code  # type: str
        # data
        self.data = data  # type: DescribeWeb3RiskScoreResponseBodyData
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # Response detailed message.
        self.message = message  # type: str
        # The unique ID of the request, which can be used to locate issues.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeWeb3RiskScoreResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = DescribeWeb3RiskScoreResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWeb3RiskScoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWeb3RiskScoreResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWeb3RiskScoreResponse, self).to_map()
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
            temp_model = DescribeWeb3RiskScoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWeb3TransactionLabelsRequest(TeaModel):
    def __init__(self, chain_short_name=None, merchant_biz_id=None, transaction=None):
        # This is the short name of blockchain。
        # [ ETH, MATIC, BNB ]
        self.chain_short_name = chain_short_name  # type: str
        # A unique business ID for tracing purpose. For example，the sequence ID from the merchant\"s business-related database.
        self.merchant_biz_id = merchant_biz_id  # type: str
        # The Transaction hash.
        self.transaction = transaction  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWeb3TransactionLabelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_short_name is not None:
            result['ChainShortName'] = self.chain_short_name
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.transaction is not None:
            result['Transaction'] = self.transaction
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChainShortName') is not None:
            self.chain_short_name = m.get('ChainShortName')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('Transaction') is not None:
            self.transaction = m.get('Transaction')
        return self


class DescribeWeb3TransactionLabelsResponseBodyDataContractDetails(TeaModel):
    def __init__(self, amount=None, from_=None, gas_limit=None, index=None, to=None):
        # the value of internal transaction
        self.amount = amount  # type: str
        # the sender of internal transaction
        self.from_ = from_  # type: str
        # the gaslimit of internal transaction
        self.gas_limit = gas_limit  # type: int
        # the call layer of internal transaction
        self.index = index  # type: int
        # the receiver of internal transaction
        self.to = to  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWeb3TransactionLabelsResponseBodyDataContractDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.from_ is not None:
            result['From'] = self.from_
        if self.gas_limit is not None:
            result['GasLimit'] = self.gas_limit
        if self.index is not None:
            result['Index'] = self.index
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('GasLimit') is not None:
            self.gas_limit = m.get('GasLimit')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class DescribeWeb3TransactionLabelsResponseBodyDataInputDetails(TeaModel):
    def __init__(self, amount=None, input_hash=None, is_contract=None, tag=None):
        # example: 15. the amount of transation sent by the address
        self.amount = amount  # type: int
        # the address hash
        self.input_hash = input_hash  # type: str
        # example: true. is it a contract
        self.is_contract = is_contract  # type: str
        # example: Dex . the tag of the address
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWeb3TransactionLabelsResponseBodyDataInputDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.input_hash is not None:
            result['InputHash'] = self.input_hash
        if self.is_contract is not None:
            result['IsContract'] = self.is_contract
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('InputHash') is not None:
            self.input_hash = m.get('InputHash')
        if m.get('IsContract') is not None:
            self.is_contract = m.get('IsContract')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeWeb3TransactionLabelsResponseBodyDataOutputDetails(TeaModel):
    def __init__(self, amount=None, input_hash=None, is_contract=None, tag=None):
        # example: 15. the amount of transation sent by the address
        self.amount = amount  # type: int
        # the address hash
        self.input_hash = input_hash  # type: str
        # example: true. is it a contract
        self.is_contract = is_contract  # type: str
        # example: Dex. the tag of the address
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWeb3TransactionLabelsResponseBodyDataOutputDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.input_hash is not None:
            result['InputHash'] = self.input_hash
        if self.is_contract is not None:
            result['IsContract'] = self.is_contract
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('InputHash') is not None:
            self.input_hash = m.get('InputHash')
        if m.get('IsContract') is not None:
            self.is_contract = m.get('IsContract')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeWeb3TransactionLabelsResponseBodyDataTokenTransferDetails(TeaModel):
    def __init__(self, amount=None, from_=None, index=None, symbol=None, to=None, token=None,
                 token_contract_address=None, token_id=None):
        # the token amount
        self.amount = amount  # type: str
        # the sender of the token
        self.from_ = from_  # type: str
        # the call layer of to token transfer
        self.index = index  # type: int
        # the token symbol
        self.symbol = symbol  # type: str
        # the receiver of the token
        self.to = to  # type: str
        # the token name
        self.token = token  # type: str
        # the token address
        self.token_contract_address = token_contract_address  # type: str
        # NFT ID, if the token is erc721
        self.token_id = token_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWeb3TransactionLabelsResponseBodyDataTokenTransferDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.from_ is not None:
            result['From'] = self.from_
        if self.index is not None:
            result['Index'] = self.index
        if self.symbol is not None:
            result['Symbol'] = self.symbol
        if self.to is not None:
            result['To'] = self.to
        if self.token is not None:
            result['Token'] = self.token
        if self.token_contract_address is not None:
            result['TokenContractAddress'] = self.token_contract_address
        if self.token_id is not None:
            result['TokenId'] = self.token_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TokenContractAddress') is not None:
            self.token_contract_address = m.get('TokenContractAddress')
        if m.get('TokenId') is not None:
            self.token_id = m.get('TokenId')
        return self


class DescribeWeb3TransactionLabelsResponseBodyData(TeaModel):
    def __init__(self, amount=None, chain_name=None, chain_short_name=None, contract_details=None, error_log=None,
                 gas_limit=None, gas_price=None, gas_used=None, height=None, index=None, input_data=None, input_details=None,
                 method_id=None, nonce=None, output_details=None, state=None, token_transfer_details=None,
                 transaction_symbol=None, transaction_time=None, transaction_type=None, txfee=None, txid=None):
        # the amount of native currency
        self.amount = amount  # type: str
        # chainName
        self.chain_name = chain_name  # type: str
        # short name of blockchain
        self.chain_short_name = chain_short_name  # type: str
        # contract details
        self.contract_details = contract_details  # type: list[DescribeWeb3TransactionLabelsResponseBodyDataContractDetails]
        # error log
        self.error_log = error_log  # type: str
        # gasLimit
        self.gas_limit = gas_limit  # type: int
        # gasPrice
        self.gas_price = gas_price  # type: str
        # gasUsed
        self.gas_used = gas_used  # type: int
        # height
        self.height = height  # type: int
        # the position of the transaction in the block
        self.index = index  # type: int
        # input data
        self.input_data = input_data  # type: str
        # input details
        self.input_details = input_details  # type: list[DescribeWeb3TransactionLabelsResponseBodyDataInputDetails]
        # the method name of contract call. For external transaction method: [\"CALL\",\"CALLCODE\",\"DELEGATECALL\",\"STATICCALL\"]; for internal transaction method: the first 4 bytes of the hash of the method name
        self.method_id = method_id  # type: str
        # nonce
        self.nonce = nonce  # type: str
        # output details
        self.output_details = output_details  # type: list[DescribeWeb3TransactionLabelsResponseBodyDataOutputDetails]
        # the transaction state. 1: success 0: fail
        self.state = state  # type: int
        # token transfer details
        self.token_transfer_details = token_transfer_details  # type: list[DescribeWeb3TransactionLabelsResponseBodyDataTokenTransferDetails]
        # the symbol of native currency
        self.transaction_symbol = transaction_symbol  # type: str
        # the block timestamp
        self.transaction_time = transaction_time  # type: str
        # Integer	0: legacy; 1: eip 2930; 2: eip 1559
        self.transaction_type = transaction_type  # type: str
        # the transaction fee in eth
        self.txfee = txfee  # type: str
        # Txid
        self.txid = txid  # type: str

    def validate(self):
        if self.contract_details:
            for k in self.contract_details:
                if k:
                    k.validate()
        if self.input_details:
            for k in self.input_details:
                if k:
                    k.validate()
        if self.output_details:
            for k in self.output_details:
                if k:
                    k.validate()
        if self.token_transfer_details:
            for k in self.token_transfer_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWeb3TransactionLabelsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.chain_name is not None:
            result['ChainName'] = self.chain_name
        if self.chain_short_name is not None:
            result['ChainShortName'] = self.chain_short_name
        result['ContractDetails'] = []
        if self.contract_details is not None:
            for k in self.contract_details:
                result['ContractDetails'].append(k.to_map() if k else None)
        if self.error_log is not None:
            result['ErrorLog'] = self.error_log
        if self.gas_limit is not None:
            result['GasLimit'] = self.gas_limit
        if self.gas_price is not None:
            result['GasPrice'] = self.gas_price
        if self.gas_used is not None:
            result['GasUsed'] = self.gas_used
        if self.height is not None:
            result['Height'] = self.height
        if self.index is not None:
            result['Index'] = self.index
        if self.input_data is not None:
            result['InputData'] = self.input_data
        result['InputDetails'] = []
        if self.input_details is not None:
            for k in self.input_details:
                result['InputDetails'].append(k.to_map() if k else None)
        if self.method_id is not None:
            result['MethodId'] = self.method_id
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        result['OutputDetails'] = []
        if self.output_details is not None:
            for k in self.output_details:
                result['OutputDetails'].append(k.to_map() if k else None)
        if self.state is not None:
            result['State'] = self.state
        result['TokenTransferDetails'] = []
        if self.token_transfer_details is not None:
            for k in self.token_transfer_details:
                result['TokenTransferDetails'].append(k.to_map() if k else None)
        if self.transaction_symbol is not None:
            result['TransactionSymbol'] = self.transaction_symbol
        if self.transaction_time is not None:
            result['TransactionTime'] = self.transaction_time
        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type
        if self.txfee is not None:
            result['Txfee'] = self.txfee
        if self.txid is not None:
            result['Txid'] = self.txid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ChainName') is not None:
            self.chain_name = m.get('ChainName')
        if m.get('ChainShortName') is not None:
            self.chain_short_name = m.get('ChainShortName')
        self.contract_details = []
        if m.get('ContractDetails') is not None:
            for k in m.get('ContractDetails'):
                temp_model = DescribeWeb3TransactionLabelsResponseBodyDataContractDetails()
                self.contract_details.append(temp_model.from_map(k))
        if m.get('ErrorLog') is not None:
            self.error_log = m.get('ErrorLog')
        if m.get('GasLimit') is not None:
            self.gas_limit = m.get('GasLimit')
        if m.get('GasPrice') is not None:
            self.gas_price = m.get('GasPrice')
        if m.get('GasUsed') is not None:
            self.gas_used = m.get('GasUsed')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('InputData') is not None:
            self.input_data = m.get('InputData')
        self.input_details = []
        if m.get('InputDetails') is not None:
            for k in m.get('InputDetails'):
                temp_model = DescribeWeb3TransactionLabelsResponseBodyDataInputDetails()
                self.input_details.append(temp_model.from_map(k))
        if m.get('MethodId') is not None:
            self.method_id = m.get('MethodId')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        self.output_details = []
        if m.get('OutputDetails') is not None:
            for k in m.get('OutputDetails'):
                temp_model = DescribeWeb3TransactionLabelsResponseBodyDataOutputDetails()
                self.output_details.append(temp_model.from_map(k))
        if m.get('State') is not None:
            self.state = m.get('State')
        self.token_transfer_details = []
        if m.get('TokenTransferDetails') is not None:
            for k in m.get('TokenTransferDetails'):
                temp_model = DescribeWeb3TransactionLabelsResponseBodyDataTokenTransferDetails()
                self.token_transfer_details.append(temp_model.from_map(k))
        if m.get('TransactionSymbol') is not None:
            self.transaction_symbol = m.get('TransactionSymbol')
        if m.get('TransactionTime') is not None:
            self.transaction_time = m.get('TransactionTime')
        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')
        if m.get('Txfee') is not None:
            self.txfee = m.get('Txfee')
        if m.get('Txid') is not None:
            self.txid = m.get('Txid')
        return self


class DescribeWeb3TransactionLabelsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None):
        # Return code. For the full list of codes, see Codes and Messages.
        self.code = code  # type: str
        # data
        self.data = data  # type: DescribeWeb3TransactionLabelsResponseBodyData
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # Response detailed message.
        self.message = message  # type: str
        # The unique ID of the request, which can be used to locate issues.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeWeb3TransactionLabelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = DescribeWeb3TransactionLabelsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWeb3TransactionLabelsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWeb3TransactionLabelsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWeb3TransactionLabelsResponse, self).to_map()
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
            temp_model = DescribeWeb3TransactionLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DocOcrRequest(TeaModel):
    def __init__(self, doc_type=None, id_face_quality=None, id_ocr_picture_base_64=None, id_ocr_picture_url=None,
                 merchant_biz_id=None, merchant_user_id=None, ocr=None, product_code=None, spoof=None):
        self.doc_type = doc_type  # type: str
        self.id_face_quality = id_face_quality  # type: str
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64  # type: str
        self.id_ocr_picture_url = id_ocr_picture_url  # type: str
        self.merchant_biz_id = merchant_biz_id  # type: str
        self.merchant_user_id = merchant_user_id  # type: str
        self.ocr = ocr  # type: str
        self.product_code = product_code  # type: str
        self.spoof = spoof  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DocOcrRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.id_face_quality is not None:
            result['IdFaceQuality'] = self.id_face_quality
        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64
        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.ocr is not None:
            result['Ocr'] = self.ocr
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.spoof is not None:
            result['Spoof'] = self.spoof
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('IdFaceQuality') is not None:
            self.id_face_quality = m.get('IdFaceQuality')
        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')
        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Spoof') is not None:
            self.spoof = m.get('Spoof')
        return self


class DocOcrResponseBodyResult(TeaModel):
    def __init__(self, ext_id_info=None, passed=None, sub_code=None, transaction_id=None):
        self.ext_id_info = ext_id_info  # type: str
        self.passed = passed  # type: str
        self.sub_code = sub_code  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DocOcrResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class DocOcrResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: DocOcrResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DocOcrResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DocOcrResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DocOcrResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DocOcrResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DocOcrResponse, self).to_map()
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
            temp_model = DocOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EkycVerifyRequest(TeaModel):
    def __init__(self, authorize=None, crop=None, doc_name=None, doc_no=None, doc_type=None,
                 face_picture_base_64=None, face_picture_url=None, id_ocr_picture_base_64=None, id_ocr_picture_url=None,
                 merchant_biz_id=None, merchant_user_id=None, product_code=None):
        self.authorize = authorize  # type: str
        self.crop = crop  # type: str
        self.doc_name = doc_name  # type: str
        self.doc_no = doc_no  # type: str
        self.doc_type = doc_type  # type: str
        self.face_picture_base_64 = face_picture_base_64  # type: str
        self.face_picture_url = face_picture_url  # type: str
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64  # type: str
        self.id_ocr_picture_url = id_ocr_picture_url  # type: str
        self.merchant_biz_id = merchant_biz_id  # type: str
        self.merchant_user_id = merchant_user_id  # type: str
        self.product_code = product_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EkycVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorize is not None:
            result['Authorize'] = self.authorize
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.doc_no is not None:
            result['DocNo'] = self.doc_no
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64
        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url
        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64
        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Authorize') is not None:
            self.authorize = m.get('Authorize')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('DocNo') is not None:
            self.doc_no = m.get('DocNo')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')
        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')
        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')
        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class EkycVerifyResponseBodyResult(TeaModel):
    def __init__(self, ext_face_info=None, ext_id_info=None, passed=None, sub_code=None, transaction_id=None):
        self.ext_face_info = ext_face_info  # type: str
        self.ext_id_info = ext_id_info  # type: str
        self.passed = passed  # type: str
        self.sub_code = sub_code  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EkycVerifyResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_face_info is not None:
            result['ExtFaceInfo'] = self.ext_face_info
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtFaceInfo') is not None:
            self.ext_face_info = m.get('ExtFaceInfo')
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class EkycVerifyResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: EkycVerifyResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(EkycVerifyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = EkycVerifyResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class EkycVerifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EkycVerifyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EkycVerifyResponse, self).to_map()
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
            temp_model = EkycVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FaceCompareRequest(TeaModel):
    def __init__(self, merchant_biz_id=None, source_face_picture=None, source_face_picture_url=None,
                 target_face_picture=None, target_face_picture_url=None):
        self.merchant_biz_id = merchant_biz_id  # type: str
        self.source_face_picture = source_face_picture  # type: str
        self.source_face_picture_url = source_face_picture_url  # type: str
        self.target_face_picture = target_face_picture  # type: str
        self.target_face_picture_url = target_face_picture_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FaceCompareRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.source_face_picture is not None:
            result['SourceFacePicture'] = self.source_face_picture
        if self.source_face_picture_url is not None:
            result['SourceFacePictureUrl'] = self.source_face_picture_url
        if self.target_face_picture is not None:
            result['TargetFacePicture'] = self.target_face_picture
        if self.target_face_picture_url is not None:
            result['TargetFacePictureUrl'] = self.target_face_picture_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('SourceFacePicture') is not None:
            self.source_face_picture = m.get('SourceFacePicture')
        if m.get('SourceFacePictureUrl') is not None:
            self.source_face_picture_url = m.get('SourceFacePictureUrl')
        if m.get('TargetFacePicture') is not None:
            self.target_face_picture = m.get('TargetFacePicture')
        if m.get('TargetFacePictureUrl') is not None:
            self.target_face_picture_url = m.get('TargetFacePictureUrl')
        return self


class FaceCompareResponseBodyResult(TeaModel):
    def __init__(self, face_comparison_score=None, passed=None, transaction_id=None):
        self.face_comparison_score = face_comparison_score  # type: float
        self.passed = passed  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FaceCompareResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_comparison_score is not None:
            result['FaceComparisonScore'] = self.face_comparison_score
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceComparisonScore') is not None:
            self.face_comparison_score = m.get('FaceComparisonScore')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class FaceCompareResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: FaceCompareResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(FaceCompareResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = FaceCompareResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class FaceCompareResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FaceCompareResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FaceCompareResponse, self).to_map()
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
            temp_model = FaceCompareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FaceLivenessRequest(TeaModel):
    def __init__(self, crop=None, face_picture_base_64=None, face_picture_url=None, face_quality=None,
                 merchant_biz_id=None, merchant_user_id=None, occlusion=None, product_code=None):
        self.crop = crop  # type: str
        self.face_picture_base_64 = face_picture_base_64  # type: str
        self.face_picture_url = face_picture_url  # type: str
        self.face_quality = face_quality  # type: str
        self.merchant_biz_id = merchant_biz_id  # type: str
        self.merchant_user_id = merchant_user_id  # type: str
        self.occlusion = occlusion  # type: str
        self.product_code = product_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FaceLivenessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64
        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.occlusion is not None:
            result['Occlusion'] = self.occlusion
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')
        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('Occlusion') is not None:
            self.occlusion = m.get('Occlusion')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class FaceLivenessResponseBodyResultExtFaceInfo(TeaModel):
    def __init__(self, face_attack=None, face_quality_score=None, occlusion_result=None):
        self.face_attack = face_attack  # type: str
        self.face_quality_score = face_quality_score  # type: float
        self.occlusion_result = occlusion_result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FaceLivenessResponseBodyResultExtFaceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_attack is not None:
            result['FaceAttack'] = self.face_attack
        if self.face_quality_score is not None:
            result['FaceQualityScore'] = self.face_quality_score
        if self.occlusion_result is not None:
            result['OcclusionResult'] = self.occlusion_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceAttack') is not None:
            self.face_attack = m.get('FaceAttack')
        if m.get('FaceQualityScore') is not None:
            self.face_quality_score = m.get('FaceQualityScore')
        if m.get('OcclusionResult') is not None:
            self.occlusion_result = m.get('OcclusionResult')
        return self


class FaceLivenessResponseBodyResult(TeaModel):
    def __init__(self, ext_face_info=None, passed=None, sub_code=None, transaction_id=None):
        self.ext_face_info = ext_face_info  # type: FaceLivenessResponseBodyResultExtFaceInfo
        self.passed = passed  # type: str
        self.sub_code = sub_code  # type: str
        self.transaction_id = transaction_id  # type: str

    def validate(self):
        if self.ext_face_info:
            self.ext_face_info.validate()

    def to_map(self):
        _map = super(FaceLivenessResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_face_info is not None:
            result['ExtFaceInfo'] = self.ext_face_info.to_map()
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtFaceInfo') is not None:
            temp_model = FaceLivenessResponseBodyResultExtFaceInfo()
            self.ext_face_info = temp_model.from_map(m['ExtFaceInfo'])
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class FaceLivenessResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: FaceLivenessResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(FaceLivenessResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = FaceLivenessResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class FaceLivenessResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FaceLivenessResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FaceLivenessResponse, self).to_map()
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
            temp_model = FaceLivenessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FraudResultCallBackRequest(TeaModel):
    def __init__(self, certify_id=None, ext_params=None, result_code=None, verify_deploy_env=None):
        self.certify_id = certify_id  # type: str
        self.ext_params = ext_params  # type: str
        self.result_code = result_code  # type: str
        self.verify_deploy_env = verify_deploy_env  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FraudResultCallBackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.verify_deploy_env is not None:
            result['VerifyDeployEnv'] = self.verify_deploy_env
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('VerifyDeployEnv') is not None:
            self.verify_deploy_env = m.get('VerifyDeployEnv')
        return self


class FraudResultCallBackResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(FraudResultCallBackResponseBody, self).to_map()
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


class FraudResultCallBackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FraudResultCallBackResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FraudResultCallBackResponse, self).to_map()
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
            temp_model = FraudResultCallBackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Id2MetaVerifyIntlRequest(TeaModel):
    def __init__(self, identify_num=None, param_type=None, product_code=None, user_name=None):
        self.identify_num = identify_num  # type: str
        self.param_type = param_type  # type: str
        self.product_code = product_code  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Id2MetaVerifyIntlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Id2MetaVerifyIntlResponseBodyResult(TeaModel):
    def __init__(self, biz_code=None):
        self.biz_code = biz_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Id2MetaVerifyIntlResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        return self


class Id2MetaVerifyIntlResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: Id2MetaVerifyIntlResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(Id2MetaVerifyIntlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = Id2MetaVerifyIntlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class Id2MetaVerifyIntlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Id2MetaVerifyIntlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(Id2MetaVerifyIntlResponse, self).to_map()
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
            temp_model = Id2MetaVerifyIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeRequest(TeaModel):
    def __init__(self, authorize=None, callback_token=None, callback_url=None, crop=None, doc_scan_mode=None,
                 doc_type=None, face_picture_base_64=None, face_picture_url=None, flow_type=None, id_face_quality=None,
                 id_spoof=None, language_config=None, merchant_biz_id=None, merchant_user_id=None, meta_info=None, ocr=None,
                 operation_mode=None, pages=None, product_code=None, product_config=None, product_flow=None, return_url=None,
                 scene_code=None, service_level=None):
        self.authorize = authorize  # type: str
        self.callback_token = callback_token  # type: str
        self.callback_url = callback_url  # type: str
        self.crop = crop  # type: str
        self.doc_scan_mode = doc_scan_mode  # type: str
        self.doc_type = doc_type  # type: str
        self.face_picture_base_64 = face_picture_base_64  # type: str
        self.face_picture_url = face_picture_url  # type: str
        self.flow_type = flow_type  # type: str
        self.id_face_quality = id_face_quality  # type: str
        self.id_spoof = id_spoof  # type: str
        self.language_config = language_config  # type: str
        self.merchant_biz_id = merchant_biz_id  # type: str
        self.merchant_user_id = merchant_user_id  # type: str
        self.meta_info = meta_info  # type: str
        # OCR。
        self.ocr = ocr  # type: str
        self.operation_mode = operation_mode  # type: str
        self.pages = pages  # type: str
        self.product_code = product_code  # type: str
        self.product_config = product_config  # type: str
        self.product_flow = product_flow  # type: str
        self.return_url = return_url  # type: str
        self.scene_code = scene_code  # type: str
        self.service_level = service_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitializeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorize is not None:
            result['Authorize'] = self.authorize
        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.doc_scan_mode is not None:
            result['DocScanMode'] = self.doc_scan_mode
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64
        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.id_face_quality is not None:
            result['IdFaceQuality'] = self.id_face_quality
        if self.id_spoof is not None:
            result['IdSpoof'] = self.id_spoof
        if self.language_config is not None:
            result['LanguageConfig'] = self.language_config
        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id
        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.ocr is not None:
            result['Ocr'] = self.ocr
        if self.operation_mode is not None:
            result['OperationMode'] = self.operation_mode
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_config is not None:
            result['ProductConfig'] = self.product_config
        if self.product_flow is not None:
            result['ProductFlow'] = self.product_flow
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.service_level is not None:
            result['ServiceLevel'] = self.service_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Authorize') is not None:
            self.authorize = m.get('Authorize')
        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('DocScanMode') is not None:
            self.doc_scan_mode = m.get('DocScanMode')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')
        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('IdFaceQuality') is not None:
            self.id_face_quality = m.get('IdFaceQuality')
        if m.get('IdSpoof') is not None:
            self.id_spoof = m.get('IdSpoof')
        if m.get('LanguageConfig') is not None:
            self.language_config = m.get('LanguageConfig')
        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')
        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')
        if m.get('OperationMode') is not None:
            self.operation_mode = m.get('OperationMode')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductConfig') is not None:
            self.product_config = m.get('ProductConfig')
        if m.get('ProductFlow') is not None:
            self.product_flow = m.get('ProductFlow')
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('ServiceLevel') is not None:
            self.service_level = m.get('ServiceLevel')
        return self


class InitializeResponseBodyResult(TeaModel):
    def __init__(self, client_cfg=None, transaction_id=None, transaction_url=None):
        self.client_cfg = client_cfg  # type: str
        self.transaction_id = transaction_id  # type: str
        self.transaction_url = transaction_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitializeResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_cfg is not None:
            result['ClientCfg'] = self.client_cfg
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        if self.transaction_url is not None:
            result['TransactionUrl'] = self.transaction_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientCfg') is not None:
            self.client_cfg = m.get('ClientCfg')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        if m.get('TransactionUrl') is not None:
            self.transaction_url = m.get('TransactionUrl')
        return self


class InitializeResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: InitializeResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(InitializeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = InitializeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class InitializeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InitializeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitializeResponse, self).to_map()
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
            temp_model = InitializeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Mobile3MetaVerifyIntlRequest(TeaModel):
    def __init__(self, identify_num=None, mobile=None, param_type=None, product_code=None, user_name=None):
        self.identify_num = identify_num  # type: str
        self.mobile = mobile  # type: str
        self.param_type = param_type  # type: str
        self.product_code = product_code  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Mobile3MetaVerifyIntlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Mobile3MetaVerifyIntlResponseBodyResult(TeaModel):
    def __init__(self, biz_code=None, isp_name=None, sub_code=None):
        self.biz_code = biz_code  # type: str
        self.isp_name = isp_name  # type: str
        self.sub_code = sub_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Mobile3MetaVerifyIntlResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class Mobile3MetaVerifyIntlResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: Mobile3MetaVerifyIntlResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(Mobile3MetaVerifyIntlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = Mobile3MetaVerifyIntlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class Mobile3MetaVerifyIntlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Mobile3MetaVerifyIntlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(Mobile3MetaVerifyIntlResponse, self).to_map()
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
            temp_model = Mobile3MetaVerifyIntlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


