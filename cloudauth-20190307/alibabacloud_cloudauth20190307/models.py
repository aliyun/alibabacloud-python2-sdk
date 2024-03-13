# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AIGCFaceVerifyRequest(TeaModel):
    def __init__(self, face_contrast_picture=None, face_contrast_picture_url=None, oss_bucket_name=None,
                 oss_object_name=None, outer_order_no=None, product_code=None, scene_id=None):
        self.face_contrast_picture = face_contrast_picture  # type: str
        self.face_contrast_picture_url = face_contrast_picture_url  # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.scene_id = scene_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AIGCFaceVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class AIGCFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(self, certify_id=None, result=None, score=None):
        self.certify_id = certify_id  # type: str
        self.result = result  # type: str
        self.score = score  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AIGCFaceVerifyResponseBodyResultObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.result is not None:
            result['Result'] = self.result
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class AIGCFaceVerifyResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result_object=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result_object = result_object  # type: AIGCFaceVerifyResponseBodyResultObject

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super(AIGCFaceVerifyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = AIGCFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class AIGCFaceVerifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AIGCFaceVerifyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AIGCFaceVerifyResponse, self).to_map()
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
            temp_model = AIGCFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompareFaceVerifyRequest(TeaModel):
    def __init__(self, crop=None, outer_order_no=None, product_code=None, scene_id=None, source_certify_id=None,
                 source_face_contrast_picture=None, source_face_contrast_picture_url=None, source_oss_bucket_name=None,
                 source_oss_object_name=None, target_certify_id=None, target_face_contrast_picture=None,
                 target_face_contrast_picture_url=None, target_oss_bucket_name=None, target_oss_object_name=None):
        self.crop = crop  # type: str
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.scene_id = scene_id  # type: long
        self.source_certify_id = source_certify_id  # type: str
        self.source_face_contrast_picture = source_face_contrast_picture  # type: str
        self.source_face_contrast_picture_url = source_face_contrast_picture_url  # type: str
        self.source_oss_bucket_name = source_oss_bucket_name  # type: str
        self.source_oss_object_name = source_oss_object_name  # type: str
        self.target_certify_id = target_certify_id  # type: str
        self.target_face_contrast_picture = target_face_contrast_picture  # type: str
        self.target_face_contrast_picture_url = target_face_contrast_picture_url  # type: str
        self.target_oss_bucket_name = target_oss_bucket_name  # type: str
        self.target_oss_object_name = target_oss_object_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompareFaceVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.source_certify_id is not None:
            result['SourceCertifyId'] = self.source_certify_id
        if self.source_face_contrast_picture is not None:
            result['SourceFaceContrastPicture'] = self.source_face_contrast_picture
        if self.source_face_contrast_picture_url is not None:
            result['SourceFaceContrastPictureUrl'] = self.source_face_contrast_picture_url
        if self.source_oss_bucket_name is not None:
            result['SourceOssBucketName'] = self.source_oss_bucket_name
        if self.source_oss_object_name is not None:
            result['SourceOssObjectName'] = self.source_oss_object_name
        if self.target_certify_id is not None:
            result['TargetCertifyId'] = self.target_certify_id
        if self.target_face_contrast_picture is not None:
            result['TargetFaceContrastPicture'] = self.target_face_contrast_picture
        if self.target_face_contrast_picture_url is not None:
            result['TargetFaceContrastPictureUrl'] = self.target_face_contrast_picture_url
        if self.target_oss_bucket_name is not None:
            result['TargetOssBucketName'] = self.target_oss_bucket_name
        if self.target_oss_object_name is not None:
            result['TargetOssObjectName'] = self.target_oss_object_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SourceCertifyId') is not None:
            self.source_certify_id = m.get('SourceCertifyId')
        if m.get('SourceFaceContrastPicture') is not None:
            self.source_face_contrast_picture = m.get('SourceFaceContrastPicture')
        if m.get('SourceFaceContrastPictureUrl') is not None:
            self.source_face_contrast_picture_url = m.get('SourceFaceContrastPictureUrl')
        if m.get('SourceOssBucketName') is not None:
            self.source_oss_bucket_name = m.get('SourceOssBucketName')
        if m.get('SourceOssObjectName') is not None:
            self.source_oss_object_name = m.get('SourceOssObjectName')
        if m.get('TargetCertifyId') is not None:
            self.target_certify_id = m.get('TargetCertifyId')
        if m.get('TargetFaceContrastPicture') is not None:
            self.target_face_contrast_picture = m.get('TargetFaceContrastPicture')
        if m.get('TargetFaceContrastPictureUrl') is not None:
            self.target_face_contrast_picture_url = m.get('TargetFaceContrastPictureUrl')
        if m.get('TargetOssBucketName') is not None:
            self.target_oss_bucket_name = m.get('TargetOssBucketName')
        if m.get('TargetOssObjectName') is not None:
            self.target_oss_object_name = m.get('TargetOssObjectName')
        return self


class CompareFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(self, certify_id=None, passed=None, verify_score=None):
        self.certify_id = certify_id  # type: str
        self.passed = passed  # type: str
        self.verify_score = verify_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompareFaceVerifyResponseBodyResultObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.verify_score is not None:
            result['VerifyScore'] = self.verify_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('VerifyScore') is not None:
            self.verify_score = m.get('VerifyScore')
        return self


class CompareFaceVerifyResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result_object=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result_object = result_object  # type: CompareFaceVerifyResponseBodyResultObject

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super(CompareFaceVerifyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = CompareFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class CompareFaceVerifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CompareFaceVerifyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CompareFaceVerifyResponse, self).to_map()
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
            temp_model = CompareFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompareFacesRequest(TeaModel):
    def __init__(self, source_image_type=None, source_image_value=None, target_image_type=None,
                 target_image_value=None):
        self.source_image_type = source_image_type  # type: str
        self.source_image_value = source_image_value  # type: str
        self.target_image_type = target_image_type  # type: str
        self.target_image_value = target_image_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompareFacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_image_type is not None:
            result['SourceImageType'] = self.source_image_type
        if self.source_image_value is not None:
            result['SourceImageValue'] = self.source_image_value
        if self.target_image_type is not None:
            result['TargetImageType'] = self.target_image_type
        if self.target_image_value is not None:
            result['TargetImageValue'] = self.target_image_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceImageType') is not None:
            self.source_image_type = m.get('SourceImageType')
        if m.get('SourceImageValue') is not None:
            self.source_image_value = m.get('SourceImageValue')
        if m.get('TargetImageType') is not None:
            self.target_image_type = m.get('TargetImageType')
        if m.get('TargetImageValue') is not None:
            self.target_image_value = m.get('TargetImageValue')
        return self


class CompareFacesResponseBodyData(TeaModel):
    def __init__(self, confidence_thresholds=None, similarity_score=None):
        self.confidence_thresholds = confidence_thresholds  # type: str
        self.similarity_score = similarity_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompareFacesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_thresholds is not None:
            result['ConfidenceThresholds'] = self.confidence_thresholds
        if self.similarity_score is not None:
            result['SimilarityScore'] = self.similarity_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfidenceThresholds') is not None:
            self.confidence_thresholds = m.get('ConfidenceThresholds')
        if m.get('SimilarityScore') is not None:
            self.similarity_score = m.get('SimilarityScore')
        return self


class CompareFacesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CompareFacesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CompareFacesResponseBody, self).to_map()
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
            temp_model = CompareFacesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CompareFacesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CompareFacesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CompareFacesResponse, self).to_map()
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
            temp_model = CompareFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContrastFaceVerifyRequest(TeaModel):
    def __init__(self, cert_name=None, cert_no=None, cert_type=None, certify_id=None, crop=None, device_token=None,
                 encrypt_type=None, face_contrast_file=None, face_contrast_picture=None, face_contrast_picture_url=None,
                 ip=None, mobile=None, model=None, oss_bucket_name=None, oss_object_name=None, outer_order_no=None,
                 product_code=None, scene_id=None, user_id=None):
        self.cert_name = cert_name  # type: str
        self.cert_no = cert_no  # type: str
        self.cert_type = cert_type  # type: str
        self.certify_id = certify_id  # type: str
        self.crop = crop  # type: str
        self.device_token = device_token  # type: str
        self.encrypt_type = encrypt_type  # type: str
        self.face_contrast_file = face_contrast_file  # type: str
        self.face_contrast_picture = face_contrast_picture  # type: str
        self.face_contrast_picture_url = face_contrast_picture_url  # type: str
        self.ip = ip  # type: str
        self.mobile = mobile  # type: str
        self.model = model  # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.scene_id = scene_id  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContrastFaceVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.face_contrast_file is not None:
            result['FaceContrastFile'] = self.face_contrast_file
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.model is not None:
            result['Model'] = self.model
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('FaceContrastFile') is not None:
            self.face_contrast_file = m.get('FaceContrastFile')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ContrastFaceVerifyAdvanceRequest(TeaModel):
    def __init__(self, cert_name=None, cert_no=None, cert_type=None, certify_id=None, crop=None, device_token=None,
                 encrypt_type=None, face_contrast_file_object=None, face_contrast_picture=None, face_contrast_picture_url=None,
                 ip=None, mobile=None, model=None, oss_bucket_name=None, oss_object_name=None, outer_order_no=None,
                 product_code=None, scene_id=None, user_id=None):
        self.cert_name = cert_name  # type: str
        self.cert_no = cert_no  # type: str
        self.cert_type = cert_type  # type: str
        self.certify_id = certify_id  # type: str
        self.crop = crop  # type: str
        self.device_token = device_token  # type: str
        self.encrypt_type = encrypt_type  # type: str
        self.face_contrast_file_object = face_contrast_file_object  # type: READABLE
        self.face_contrast_picture = face_contrast_picture  # type: str
        self.face_contrast_picture_url = face_contrast_picture_url  # type: str
        self.ip = ip  # type: str
        self.mobile = mobile  # type: str
        self.model = model  # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.scene_id = scene_id  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContrastFaceVerifyAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.face_contrast_file_object is not None:
            result['FaceContrastFile'] = self.face_contrast_file_object
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.model is not None:
            result['Model'] = self.model
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('FaceContrastFile') is not None:
            self.face_contrast_file_object = m.get('FaceContrastFile')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ContrastFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(self, certify_id=None, identity_info=None, material_info=None, passed=None, sub_code=None):
        self.certify_id = certify_id  # type: str
        self.identity_info = identity_info  # type: str
        self.material_info = material_info  # type: str
        self.passed = passed  # type: str
        self.sub_code = sub_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContrastFaceVerifyResponseBodyResultObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.identity_info is not None:
            result['IdentityInfo'] = self.identity_info
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('IdentityInfo') is not None:
            self.identity_info = m.get('IdentityInfo')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class ContrastFaceVerifyResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result_object=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result_object = result_object  # type: ContrastFaceVerifyResponseBodyResultObject

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super(ContrastFaceVerifyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = ContrastFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class ContrastFaceVerifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ContrastFaceVerifyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ContrastFaceVerifyResponse, self).to_map()
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
            temp_model = ContrastFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuthKeyRequest(TeaModel):
    def __init__(self, auth_years=None, biz_type=None, test=None, user_device_id=None):
        self.auth_years = auth_years  # type: int
        self.biz_type = biz_type  # type: str
        self.test = test  # type: bool
        self.user_device_id = user_device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuthKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_years is not None:
            result['AuthYears'] = self.auth_years
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.test is not None:
            result['Test'] = self.test
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthYears') is not None:
            self.auth_years = m.get('AuthYears')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Test') is not None:
            self.test = m.get('Test')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        return self


class CreateAuthKeyResponseBody(TeaModel):
    def __init__(self, auth_key=None, request_id=None):
        self.auth_key = auth_key  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuthKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAuthKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAuthKeyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAuthKeyResponse, self).to_map()
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
            temp_model = CreateAuthKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVerifySettingRequest(TeaModel):
    def __init__(self, biz_name=None, biz_type=None, guide_step=None, privacy_step=None, result_step=None,
                 solution=None):
        self.biz_name = biz_name  # type: str
        self.biz_type = biz_type  # type: str
        self.guide_step = guide_step  # type: bool
        self.privacy_step = privacy_step  # type: bool
        self.result_step = result_step  # type: bool
        self.solution = solution  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVerifySettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.guide_step is not None:
            result['GuideStep'] = self.guide_step
        if self.privacy_step is not None:
            result['PrivacyStep'] = self.privacy_step
        if self.result_step is not None:
            result['ResultStep'] = self.result_step
        if self.solution is not None:
            result['Solution'] = self.solution
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('GuideStep') is not None:
            self.guide_step = m.get('GuideStep')
        if m.get('PrivacyStep') is not None:
            self.privacy_step = m.get('PrivacyStep')
        if m.get('ResultStep') is not None:
            self.result_step = m.get('ResultStep')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        return self


class CreateVerifySettingResponseBody(TeaModel):
    def __init__(self, biz_name=None, biz_type=None, request_id=None, solution=None, step_list=None):
        self.biz_name = biz_name  # type: str
        self.biz_type = biz_type  # type: str
        self.request_id = request_id  # type: str
        self.solution = solution  # type: str
        self.step_list = step_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVerifySettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.step_list is not None:
            result['StepList'] = self.step_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('StepList') is not None:
            self.step_list = m.get('StepList')
        return self


class CreateVerifySettingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVerifySettingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVerifySettingResponse, self).to_map()
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
            temp_model = CreateVerifySettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceInfoRequest(TeaModel):
    def __init__(self, biz_type=None, current_page=None, device_id=None, expired_end_day=None,
                 expired_start_day=None, page_size=None, user_device_id=None):
        self.biz_type = biz_type  # type: str
        self.current_page = current_page  # type: int
        self.device_id = device_id  # type: str
        self.expired_end_day = expired_end_day  # type: str
        self.expired_start_day = expired_start_day  # type: str
        self.page_size = page_size  # type: int
        self.user_device_id = user_device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.expired_end_day is not None:
            result['ExpiredEndDay'] = self.expired_end_day
        if self.expired_start_day is not None:
            result['ExpiredStartDay'] = self.expired_start_day
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ExpiredEndDay') is not None:
            self.expired_end_day = m.get('ExpiredEndDay')
        if m.get('ExpiredStartDay') is not None:
            self.expired_start_day = m.get('ExpiredStartDay')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        return self


class DescribeDeviceInfoResponseBodyDeviceInfoListDeviceInfo(TeaModel):
    def __init__(self, begin_day=None, biz_type=None, device_id=None, expired_day=None, user_device_id=None):
        self.begin_day = begin_day  # type: str
        self.biz_type = biz_type  # type: str
        self.device_id = device_id  # type: str
        self.expired_day = expired_day  # type: str
        self.user_device_id = user_device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceInfoResponseBodyDeviceInfoListDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_day is not None:
            result['BeginDay'] = self.begin_day
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginDay') is not None:
            self.begin_day = m.get('BeginDay')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        return self


class DescribeDeviceInfoResponseBodyDeviceInfoList(TeaModel):
    def __init__(self, device_info=None):
        self.device_info = device_info  # type: list[DescribeDeviceInfoResponseBodyDeviceInfoListDeviceInfo]

    def validate(self):
        if self.device_info:
            for k in self.device_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDeviceInfoResponseBodyDeviceInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceInfo'] = []
        if self.device_info is not None:
            for k in self.device_info:
                result['DeviceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.device_info = []
        if m.get('DeviceInfo') is not None:
            for k in m.get('DeviceInfo'):
                temp_model = DescribeDeviceInfoResponseBodyDeviceInfoListDeviceInfo()
                self.device_info.append(temp_model.from_map(k))
        return self


class DescribeDeviceInfoResponseBody(TeaModel):
    def __init__(self, current_page=None, device_info_list=None, page_size=None, request_id=None, total_count=None):
        self.current_page = current_page  # type: int
        self.device_info_list = device_info_list  # type: DescribeDeviceInfoResponseBodyDeviceInfoList
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.device_info_list:
            self.device_info_list.validate()

    def to_map(self):
        _map = super(DescribeDeviceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_info_list is not None:
            result['DeviceInfoList'] = self.device_info_list.to_map()
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
        if m.get('DeviceInfoList') is not None:
            temp_model = DescribeDeviceInfoResponseBodyDeviceInfoList()
            self.device_info_list = temp_model.from_map(m['DeviceInfoList'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDeviceInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDeviceInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDeviceInfoResponse, self).to_map()
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
            temp_model = DescribeDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaceVerifyRequest(TeaModel):
    def __init__(self, certify_id=None, picture_return_type=None, scene_id=None):
        self.certify_id = certify_id  # type: str
        self.picture_return_type = picture_return_type  # type: str
        self.scene_id = scene_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaceVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.picture_return_type is not None:
            result['PictureReturnType'] = self.picture_return_type
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('PictureReturnType') is not None:
            self.picture_return_type = m.get('PictureReturnType')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class DescribeFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(self, device_risk=None, device_token=None, identity_info=None, material_info=None, passed=None,
                 sub_code=None, success=None, user_info=None):
        self.device_risk = device_risk  # type: str
        self.device_token = device_token  # type: str
        self.identity_info = identity_info  # type: str
        self.material_info = material_info  # type: str
        self.passed = passed  # type: str
        self.sub_code = sub_code  # type: str
        self.success = success  # type: str
        self.user_info = user_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaceVerifyResponseBodyResultObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_risk is not None:
            result['DeviceRisk'] = self.device_risk
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.identity_info is not None:
            result['IdentityInfo'] = self.identity_info
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.success is not None:
            result['Success'] = self.success
        if self.user_info is not None:
            result['UserInfo'] = self.user_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceRisk') is not None:
            self.device_risk = m.get('DeviceRisk')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('IdentityInfo') is not None:
            self.identity_info = m.get('IdentityInfo')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UserInfo') is not None:
            self.user_info = m.get('UserInfo')
        return self


class DescribeFaceVerifyResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result_object=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result_object = result_object  # type: DescribeFaceVerifyResponseBodyResultObject

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super(DescribeFaceVerifyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = DescribeFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class DescribeFaceVerifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFaceVerifyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFaceVerifyResponse, self).to_map()
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
            temp_model = DescribeFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssUploadTokenResponseBodyOssUploadToken(TeaModel):
    def __init__(self, bucket=None, end_point=None, expired=None, key=None, path=None, secret=None, token=None):
        self.bucket = bucket  # type: str
        self.end_point = end_point  # type: str
        self.expired = expired  # type: long
        self.key = key  # type: str
        self.path = path  # type: str
        self.secret = secret  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssUploadTokenResponseBodyOssUploadToken, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.key is not None:
            result['Key'] = self.key
        if self.path is not None:
            result['Path'] = self.path
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DescribeOssUploadTokenResponseBody(TeaModel):
    def __init__(self, oss_upload_token=None, request_id=None):
        self.oss_upload_token = oss_upload_token  # type: DescribeOssUploadTokenResponseBodyOssUploadToken
        self.request_id = request_id  # type: str

    def validate(self):
        if self.oss_upload_token:
            self.oss_upload_token.validate()

    def to_map(self):
        _map = super(DescribeOssUploadTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_upload_token is not None:
            result['OssUploadToken'] = self.oss_upload_token.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssUploadToken') is not None:
            temp_model = DescribeOssUploadTokenResponseBodyOssUploadToken()
            self.oss_upload_token = temp_model.from_map(m['OssUploadToken'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOssUploadTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOssUploadTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOssUploadTokenResponse, self).to_map()
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
            temp_model = DescribeOssUploadTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSmartStatisticsPageListRequest(TeaModel):
    def __init__(self, current_page=None, end_date=None, page_size=None, scene_id=None, service_code=None,
                 start_date=None):
        self.current_page = current_page  # type: str
        self.end_date = end_date  # type: str
        self.page_size = page_size  # type: str
        self.scene_id = scene_id  # type: str
        self.service_code = service_code  # type: str
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSmartStatisticsPageListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeSmartStatisticsPageListResponseBodyItems(TeaModel):
    def __init__(self, date=None, pass_rate=None, product_code=None, scene_id=None, scene_name=None,
                 success_count=None, total_count=None):
        self.date = date  # type: str
        self.pass_rate = pass_rate  # type: str
        self.product_code = product_code  # type: str
        self.scene_id = scene_id  # type: long
        self.scene_name = scene_name  # type: str
        self.success_count = success_count  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSmartStatisticsPageListResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.pass_rate is not None:
            result['PassRate'] = self.pass_rate
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('PassRate') is not None:
            self.pass_rate = m.get('PassRate')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSmartStatisticsPageListResponseBody(TeaModel):
    def __init__(self, current_page=None, items=None, page_size=None, request_id=None, total_count=None,
                 total_page=None):
        self.current_page = current_page  # type: int
        self.items = items  # type: list[DescribeSmartStatisticsPageListResponseBodyItems]
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSmartStatisticsPageListResponseBody, self).to_map()
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
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSmartStatisticsPageListResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class DescribeSmartStatisticsPageListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSmartStatisticsPageListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSmartStatisticsPageListResponse, self).to_map()
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
            temp_model = DescribeSmartStatisticsPageListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyResultRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifyResultRequest, self).to_map()
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


class DescribeVerifyResultResponseBodyMaterialIdCardInfo(TeaModel):
    def __init__(self, address=None, authority=None, back_image_url=None, birth=None, end_date=None,
                 front_image_url=None, name=None, nationality=None, number=None, start_date=None):
        self.address = address  # type: str
        self.authority = authority  # type: str
        self.back_image_url = back_image_url  # type: str
        self.birth = birth  # type: str
        self.end_date = end_date  # type: str
        self.front_image_url = front_image_url  # type: str
        self.name = name  # type: str
        self.nationality = nationality  # type: str
        self.number = number  # type: str
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifyResultResponseBodyMaterialIdCardInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.number is not None:
            result['Number'] = self.number
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeVerifyResultResponseBodyMaterial(TeaModel):
    def __init__(self, face_global_url=None, face_image_url=None, face_mask=None, face_quality=None,
                 id_card_info=None, id_card_name=None, id_card_number=None, video_urls=None):
        self.face_global_url = face_global_url  # type: str
        self.face_image_url = face_image_url  # type: str
        self.face_mask = face_mask  # type: bool
        self.face_quality = face_quality  # type: str
        self.id_card_info = id_card_info  # type: DescribeVerifyResultResponseBodyMaterialIdCardInfo
        self.id_card_name = id_card_name  # type: str
        self.id_card_number = id_card_number  # type: str
        self.video_urls = video_urls  # type: list[str]

    def validate(self):
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        _map = super(DescribeVerifyResultResponseBodyMaterial, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_global_url is not None:
            result['FaceGlobalUrl'] = self.face_global_url
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.face_mask is not None:
            result['FaceMask'] = self.face_mask
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.video_urls is not None:
            result['VideoUrls'] = self.video_urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceGlobalUrl') is not None:
            self.face_global_url = m.get('FaceGlobalUrl')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('FaceMask') is not None:
            self.face_mask = m.get('FaceMask')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('IdCardInfo') is not None:
            temp_model = DescribeVerifyResultResponseBodyMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('VideoUrls') is not None:
            self.video_urls = m.get('VideoUrls')
        return self


class DescribeVerifyResultResponseBody(TeaModel):
    def __init__(self, authority_comparision_score=None, face_comparison_score=None,
                 id_card_face_comparison_score=None, material=None, request_id=None, verify_status=None):
        self.authority_comparision_score = authority_comparision_score  # type: float
        self.face_comparison_score = face_comparison_score  # type: float
        self.id_card_face_comparison_score = id_card_face_comparison_score  # type: float
        self.material = material  # type: DescribeVerifyResultResponseBodyMaterial
        self.request_id = request_id  # type: str
        self.verify_status = verify_status  # type: int

    def validate(self):
        if self.material:
            self.material.validate()

    def to_map(self):
        _map = super(DescribeVerifyResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority_comparision_score is not None:
            result['AuthorityComparisionScore'] = self.authority_comparision_score
        if self.face_comparison_score is not None:
            result['FaceComparisonScore'] = self.face_comparison_score
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.material is not None:
            result['Material'] = self.material.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorityComparisionScore') is not None:
            self.authority_comparision_score = m.get('AuthorityComparisionScore')
        if m.get('FaceComparisonScore') is not None:
            self.face_comparison_score = m.get('FaceComparisonScore')
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        if m.get('Material') is not None:
            temp_model = DescribeVerifyResultResponseBodyMaterial()
            self.material = temp_model.from_map(m['Material'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')
        return self


class DescribeVerifyResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVerifyResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVerifyResultResponse, self).to_map()
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
            temp_model = DescribeVerifyResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifySDKRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifySDKRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeVerifySDKResponseBody(TeaModel):
    def __init__(self, request_id=None, sdk_url=None):
        self.request_id = request_id  # type: str
        self.sdk_url = sdk_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifySDKResponseBody, self).to_map()
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


class DescribeVerifySDKResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVerifySDKResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVerifySDKResponse, self).to_map()
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
            temp_model = DescribeVerifySDKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyTokenRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, callback_seed=None, callback_url=None,
                 face_retained_image_url=None, failed_redirect_url=None, id_card_back_image_url=None, id_card_front_image_url=None,
                 id_card_number=None, name=None, passed_redirect_url=None, user_id=None, user_ip=None, user_phone_number=None,
                 user_regist_time=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.callback_seed = callback_seed  # type: str
        self.callback_url = callback_url  # type: str
        self.face_retained_image_url = face_retained_image_url  # type: str
        self.failed_redirect_url = failed_redirect_url  # type: str
        self.id_card_back_image_url = id_card_back_image_url  # type: str
        self.id_card_front_image_url = id_card_front_image_url  # type: str
        self.id_card_number = id_card_number  # type: str
        self.name = name  # type: str
        self.passed_redirect_url = passed_redirect_url  # type: str
        self.user_id = user_id  # type: str
        self.user_ip = user_ip  # type: str
        self.user_phone_number = user_phone_number  # type: str
        self.user_regist_time = user_regist_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifyTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.callback_seed is not None:
            result['CallbackSeed'] = self.callback_seed
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.face_retained_image_url is not None:
            result['FaceRetainedImageUrl'] = self.face_retained_image_url
        if self.failed_redirect_url is not None:
            result['FailedRedirectUrl'] = self.failed_redirect_url
        if self.id_card_back_image_url is not None:
            result['IdCardBackImageUrl'] = self.id_card_back_image_url
        if self.id_card_front_image_url is not None:
            result['IdCardFrontImageUrl'] = self.id_card_front_image_url
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.name is not None:
            result['Name'] = self.name
        if self.passed_redirect_url is not None:
            result['PassedRedirectUrl'] = self.passed_redirect_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_ip is not None:
            result['UserIp'] = self.user_ip
        if self.user_phone_number is not None:
            result['UserPhoneNumber'] = self.user_phone_number
        if self.user_regist_time is not None:
            result['UserRegistTime'] = self.user_regist_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CallbackSeed') is not None:
            self.callback_seed = m.get('CallbackSeed')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('FaceRetainedImageUrl') is not None:
            self.face_retained_image_url = m.get('FaceRetainedImageUrl')
        if m.get('FailedRedirectUrl') is not None:
            self.failed_redirect_url = m.get('FailedRedirectUrl')
        if m.get('IdCardBackImageUrl') is not None:
            self.id_card_back_image_url = m.get('IdCardBackImageUrl')
        if m.get('IdCardFrontImageUrl') is not None:
            self.id_card_front_image_url = m.get('IdCardFrontImageUrl')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PassedRedirectUrl') is not None:
            self.passed_redirect_url = m.get('PassedRedirectUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserIp') is not None:
            self.user_ip = m.get('UserIp')
        if m.get('UserPhoneNumber') is not None:
            self.user_phone_number = m.get('UserPhoneNumber')
        if m.get('UserRegistTime') is not None:
            self.user_regist_time = m.get('UserRegistTime')
        return self


class DescribeVerifyTokenResponseBodyOssUploadToken(TeaModel):
    def __init__(self, bucket=None, end_point=None, expired=None, key=None, path=None, secret=None, token=None):
        self.bucket = bucket  # type: str
        self.end_point = end_point  # type: str
        self.expired = expired  # type: long
        self.key = key  # type: str
        self.path = path  # type: str
        self.secret = secret  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifyTokenResponseBodyOssUploadToken, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.key is not None:
            result['Key'] = self.key
        if self.path is not None:
            result['Path'] = self.path
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DescribeVerifyTokenResponseBody(TeaModel):
    def __init__(self, oss_upload_token=None, request_id=None, verify_page_url=None, verify_token=None):
        self.oss_upload_token = oss_upload_token  # type: DescribeVerifyTokenResponseBodyOssUploadToken
        self.request_id = request_id  # type: str
        self.verify_page_url = verify_page_url  # type: str
        self.verify_token = verify_token  # type: str

    def validate(self):
        if self.oss_upload_token:
            self.oss_upload_token.validate()

    def to_map(self):
        _map = super(DescribeVerifyTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_upload_token is not None:
            result['OssUploadToken'] = self.oss_upload_token.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_page_url is not None:
            result['VerifyPageUrl'] = self.verify_page_url
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssUploadToken') is not None:
            temp_model = DescribeVerifyTokenResponseBodyOssUploadToken()
            self.oss_upload_token = temp_model.from_map(m['OssUploadToken'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyPageUrl') is not None:
            self.verify_page_url = m.get('VerifyPageUrl')
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        return self


class DescribeVerifyTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVerifyTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVerifyTokenResponse, self).to_map()
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
            temp_model = DescribeVerifyTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectFaceAttributesRequest(TeaModel):
    def __init__(self, biz_type=None, material_value=None):
        self.biz_type = biz_type  # type: str
        self.material_value = material_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectFaceAttributesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.material_value is not None:
            result['MaterialValue'] = self.material_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('MaterialValue') is not None:
            self.material_value = m.get('MaterialValue')
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose(TeaModel):
    def __init__(self, pitch_angle=None, roll_angle=None, yaw_angle=None):
        self.pitch_angle = pitch_angle  # type: float
        self.roll_angle = roll_angle  # type: float
        self.yaw_angle = yaw_angle  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch_angle is not None:
            result['PitchAngle'] = self.pitch_angle
        if self.roll_angle is not None:
            result['RollAngle'] = self.roll_angle
        if self.yaw_angle is not None:
            result['YawAngle'] = self.yaw_angle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PitchAngle') is not None:
            self.pitch_angle = m.get('PitchAngle')
        if m.get('RollAngle') is not None:
            self.roll_angle = m.get('RollAngle')
        if m.get('YawAngle') is not None:
            self.yaw_angle = m.get('YawAngle')
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling(TeaModel):
    def __init__(self, threshold=None, value=None):
        self.threshold = threshold  # type: float
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes(TeaModel):
    def __init__(self, blur=None, facequal=None, facetype=None, glasses=None, headpose=None, integrity=None,
                 respirator=None, smiling=None):
        self.blur = blur  # type: float
        self.facequal = facequal  # type: float
        self.facetype = facetype  # type: str
        self.glasses = glasses  # type: str
        self.headpose = headpose  # type: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose
        self.integrity = integrity  # type: int
        self.respirator = respirator  # type: str
        self.smiling = smiling  # type: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling

    def validate(self):
        if self.headpose:
            self.headpose.validate()
        if self.smiling:
            self.smiling.validate()

    def to_map(self):
        _map = super(DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blur is not None:
            result['Blur'] = self.blur
        if self.facequal is not None:
            result['Facequal'] = self.facequal
        if self.facetype is not None:
            result['Facetype'] = self.facetype
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.headpose is not None:
            result['Headpose'] = self.headpose.to_map()
        if self.integrity is not None:
            result['Integrity'] = self.integrity
        if self.respirator is not None:
            result['Respirator'] = self.respirator
        if self.smiling is not None:
            result['Smiling'] = self.smiling.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Blur') is not None:
            self.blur = m.get('Blur')
        if m.get('Facequal') is not None:
            self.facequal = m.get('Facequal')
        if m.get('Facetype') is not None:
            self.facetype = m.get('Facetype')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Headpose') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose()
            self.headpose = temp_model.from_map(m['Headpose'])
        if m.get('Integrity') is not None:
            self.integrity = m.get('Integrity')
        if m.get('Respirator') is not None:
            self.respirator = m.get('Respirator')
        if m.get('Smiling') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling()
            self.smiling = temp_model.from_map(m['Smiling'])
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect(TeaModel):
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfo(TeaModel):
    def __init__(self, face_attributes=None, face_rect=None):
        self.face_attributes = face_attributes  # type: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes
        self.face_rect = face_rect  # type: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect

    def validate(self):
        if self.face_attributes:
            self.face_attributes.validate()
        if self.face_rect:
            self.face_rect.validate()

    def to_map(self):
        _map = super(DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        if self.face_rect is not None:
            result['FaceRect'] = self.face_rect.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceAttributes') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        if m.get('FaceRect') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect()
            self.face_rect = temp_model.from_map(m['FaceRect'])
        return self


class DetectFaceAttributesResponseBodyDataFaceInfos(TeaModel):
    def __init__(self, face_attributes_detect_info=None):
        self.face_attributes_detect_info = face_attributes_detect_info  # type: list[DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfo]

    def validate(self):
        if self.face_attributes_detect_info:
            for k in self.face_attributes_detect_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectFaceAttributesResponseBodyDataFaceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FaceAttributesDetectInfo'] = []
        if self.face_attributes_detect_info is not None:
            for k in self.face_attributes_detect_info:
                result['FaceAttributesDetectInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.face_attributes_detect_info = []
        if m.get('FaceAttributesDetectInfo') is not None:
            for k in m.get('FaceAttributesDetectInfo'):
                temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfo()
                self.face_attributes_detect_info.append(temp_model.from_map(k))
        return self


class DetectFaceAttributesResponseBodyData(TeaModel):
    def __init__(self, face_infos=None, img_height=None, img_width=None):
        self.face_infos = face_infos  # type: DetectFaceAttributesResponseBodyDataFaceInfos
        self.img_height = img_height  # type: int
        self.img_width = img_width  # type: int

    def validate(self):
        if self.face_infos:
            self.face_infos.validate()

    def to_map(self):
        _map = super(DetectFaceAttributesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_infos is not None:
            result['FaceInfos'] = self.face_infos.to_map()
        if self.img_height is not None:
            result['ImgHeight'] = self.img_height
        if self.img_width is not None:
            result['ImgWidth'] = self.img_width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceInfos') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfos()
            self.face_infos = temp_model.from_map(m['FaceInfos'])
        if m.get('ImgHeight') is not None:
            self.img_height = m.get('ImgHeight')
        if m.get('ImgWidth') is not None:
            self.img_width = m.get('ImgWidth')
        return self


class DetectFaceAttributesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DetectFaceAttributesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DetectFaceAttributesResponseBody, self).to_map()
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
            temp_model = DetectFaceAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetectFaceAttributesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetectFaceAttributesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectFaceAttributesResponse, self).to_map()
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
            temp_model = DetectFaceAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Id2MetaVerifyRequest(TeaModel):
    def __init__(self, identify_num=None, param_type=None, user_name=None):
        self.identify_num = identify_num  # type: str
        self.param_type = param_type  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Id2MetaVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Id2MetaVerifyResponseBodyResultObject(TeaModel):
    def __init__(self, biz_code=None):
        self.biz_code = biz_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Id2MetaVerifyResponseBodyResultObject, self).to_map()
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


class Id2MetaVerifyResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result_object=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result_object = result_object  # type: Id2MetaVerifyResponseBodyResultObject

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super(Id2MetaVerifyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = Id2MetaVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class Id2MetaVerifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Id2MetaVerifyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(Id2MetaVerifyResponse, self).to_map()
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
            temp_model = Id2MetaVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitFaceVerifyRequest(TeaModel):
    def __init__(self, auth_id=None, birthday=None, callback_token=None, callback_url=None, cert_name=None,
                 cert_no=None, cert_type=None, certify_id=None, certify_url_style=None, certify_url_type=None, crop=None,
                 encrypt_type=None, face_contrast_picture=None, face_contrast_picture_url=None, face_guard_output=None, ip=None,
                 meta_info=None, mobile=None, mode=None, model=None, oss_bucket_name=None, oss_object_name=None,
                 outer_order_no=None, procedure_priority=None, product_code=None, rarely_characters=None, read_img=None,
                 return_url=None, scene_id=None, suitable_type=None, user_id=None, validity_date=None,
                 voluntary_customized_content=None):
        self.auth_id = auth_id  # type: str
        self.birthday = birthday  # type: str
        self.callback_token = callback_token  # type: str
        self.callback_url = callback_url  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_no = cert_no  # type: str
        self.cert_type = cert_type  # type: str
        self.certify_id = certify_id  # type: str
        self.certify_url_style = certify_url_style  # type: str
        self.certify_url_type = certify_url_type  # type: str
        self.crop = crop  # type: str
        self.encrypt_type = encrypt_type  # type: str
        self.face_contrast_picture = face_contrast_picture  # type: str
        self.face_contrast_picture_url = face_contrast_picture_url  # type: str
        self.face_guard_output = face_guard_output  # type: str
        self.ip = ip  # type: str
        self.meta_info = meta_info  # type: str
        self.mobile = mobile  # type: str
        self.mode = mode  # type: str
        self.model = model  # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.outer_order_no = outer_order_no  # type: str
        self.procedure_priority = procedure_priority  # type: str
        self.product_code = product_code  # type: str
        self.rarely_characters = rarely_characters  # type: str
        self.read_img = read_img  # type: str
        self.return_url = return_url  # type: str
        self.scene_id = scene_id  # type: long
        self.suitable_type = suitable_type  # type: str
        self.user_id = user_id  # type: str
        self.validity_date = validity_date  # type: str
        self.voluntary_customized_content = voluntary_customized_content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitFaceVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_id is not None:
            result['AuthId'] = self.auth_id
        if self.birthday is not None:
            result['Birthday'] = self.birthday
        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.certify_url_style is not None:
            result['CertifyUrlStyle'] = self.certify_url_style
        if self.certify_url_type is not None:
            result['CertifyUrlType'] = self.certify_url_type
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.face_guard_output is not None:
            result['FaceGuardOutput'] = self.face_guard_output
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.model is not None:
            result['Model'] = self.model
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.procedure_priority is not None:
            result['ProcedurePriority'] = self.procedure_priority
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.rarely_characters is not None:
            result['RarelyCharacters'] = self.rarely_characters
        if self.read_img is not None:
            result['ReadImg'] = self.read_img
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.suitable_type is not None:
            result['SuitableType'] = self.suitable_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.validity_date is not None:
            result['ValidityDate'] = self.validity_date
        if self.voluntary_customized_content is not None:
            result['VoluntaryCustomizedContent'] = self.voluntary_customized_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')
        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')
        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('CertifyUrlStyle') is not None:
            self.certify_url_style = m.get('CertifyUrlStyle')
        if m.get('CertifyUrlType') is not None:
            self.certify_url_type = m.get('CertifyUrlType')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('FaceGuardOutput') is not None:
            self.face_guard_output = m.get('FaceGuardOutput')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProcedurePriority') is not None:
            self.procedure_priority = m.get('ProcedurePriority')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RarelyCharacters') is not None:
            self.rarely_characters = m.get('RarelyCharacters')
        if m.get('ReadImg') is not None:
            self.read_img = m.get('ReadImg')
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SuitableType') is not None:
            self.suitable_type = m.get('SuitableType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ValidityDate') is not None:
            self.validity_date = m.get('ValidityDate')
        if m.get('VoluntaryCustomizedContent') is not None:
            self.voluntary_customized_content = m.get('VoluntaryCustomizedContent')
        return self


class InitFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(self, certify_id=None, certify_url=None):
        self.certify_id = certify_id  # type: str
        self.certify_url = certify_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitFaceVerifyResponseBodyResultObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.certify_url is not None:
            result['CertifyUrl'] = self.certify_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('CertifyUrl') is not None:
            self.certify_url = m.get('CertifyUrl')
        return self


class InitFaceVerifyResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result_object=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result_object = result_object  # type: InitFaceVerifyResponseBodyResultObject

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super(InitFaceVerifyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = InitFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class InitFaceVerifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InitFaceVerifyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitFaceVerifyResponse, self).to_map()
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
            temp_model = InitFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LivenessFaceVerifyRequest(TeaModel):
    def __init__(self, certify_id=None, crop=None, device_token=None, face_contrast_picture=None,
                 face_contrast_picture_url=None, ip=None, mobile=None, model=None, oss_bucket_name=None, oss_object_name=None,
                 outer_order_no=None, product_code=None, scene_id=None, user_id=None):
        self.certify_id = certify_id  # type: str
        self.crop = crop  # type: str
        self.device_token = device_token  # type: str
        self.face_contrast_picture = face_contrast_picture  # type: str
        self.face_contrast_picture_url = face_contrast_picture_url  # type: str
        self.ip = ip  # type: str
        self.mobile = mobile  # type: str
        self.model = model  # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.scene_id = scene_id  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LivenessFaceVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.model is not None:
            result['Model'] = self.model
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class LivenessFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(self, certify_id=None, material_info=None, passed=None, sub_code=None):
        self.certify_id = certify_id  # type: str
        self.material_info = material_info  # type: str
        self.passed = passed  # type: str
        self.sub_code = sub_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LivenessFaceVerifyResponseBodyResultObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class LivenessFaceVerifyResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result_object=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result_object = result_object  # type: LivenessFaceVerifyResponseBodyResultObject

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super(LivenessFaceVerifyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = LivenessFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class LivenessFaceVerifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LivenessFaceVerifyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LivenessFaceVerifyResponse, self).to_map()
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
            temp_model = LivenessFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Mobile3MetaDetailVerifyRequest(TeaModel):
    def __init__(self, identify_num=None, mobile=None, param_type=None, user_name=None):
        self.identify_num = identify_num  # type: str
        self.mobile = mobile  # type: str
        self.param_type = param_type  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Mobile3MetaDetailVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
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
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Mobile3MetaDetailVerifyResponseBodyResultObject(TeaModel):
    def __init__(self, biz_code=None, isp_name=None, sub_code=None):
        self.biz_code = biz_code  # type: str
        self.isp_name = isp_name  # type: str
        self.sub_code = sub_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Mobile3MetaDetailVerifyResponseBodyResultObject, self).to_map()
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


class Mobile3MetaDetailVerifyResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result_object=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result_object = result_object  # type: Mobile3MetaDetailVerifyResponseBodyResultObject

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super(Mobile3MetaDetailVerifyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = Mobile3MetaDetailVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class Mobile3MetaDetailVerifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Mobile3MetaDetailVerifyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(Mobile3MetaDetailVerifyResponse, self).to_map()
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
            temp_model = Mobile3MetaDetailVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Mobile3MetaSimpleVerifyRequest(TeaModel):
    def __init__(self, identify_num=None, mobile=None, param_type=None, user_name=None):
        self.identify_num = identify_num  # type: str
        self.mobile = mobile  # type: str
        self.param_type = param_type  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Mobile3MetaSimpleVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.param_type is not None:
            result['ParamType'] = self.param_type
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
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class Mobile3MetaSimpleVerifyResponseBodyResultObject(TeaModel):
    def __init__(self, biz_code=None, isp_name=None):
        self.biz_code = biz_code  # type: str
        self.isp_name = isp_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Mobile3MetaSimpleVerifyResponseBodyResultObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        return self


class Mobile3MetaSimpleVerifyResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result_object=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result_object = result_object  # type: Mobile3MetaSimpleVerifyResponseBodyResultObject

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super(Mobile3MetaSimpleVerifyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = Mobile3MetaSimpleVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class Mobile3MetaSimpleVerifyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Mobile3MetaSimpleVerifyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(Mobile3MetaSimpleVerifyResponse, self).to_map()
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
            temp_model = Mobile3MetaSimpleVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeviceInfoRequest(TeaModel):
    def __init__(self, biz_type=None, device_id=None, duration=None, expired_day=None, user_device_id=None):
        self.biz_type = biz_type  # type: str
        self.device_id = device_id  # type: str
        self.duration = duration  # type: str
        self.expired_day = expired_day  # type: str
        self.user_device_id = user_device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        return self


class ModifyDeviceInfoResponseBody(TeaModel):
    def __init__(self, begin_day=None, biz_type=None, device_id=None, expired_day=None, request_id=None,
                 user_device_id=None):
        self.begin_day = begin_day  # type: str
        self.biz_type = biz_type  # type: str
        self.device_id = device_id  # type: str
        self.expired_day = expired_day  # type: str
        self.request_id = request_id  # type: str
        self.user_device_id = user_device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_day is not None:
            result['BeginDay'] = self.begin_day
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginDay') is not None:
            self.begin_day = m.get('BeginDay')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        return self


class ModifyDeviceInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDeviceInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDeviceInfoResponse, self).to_map()
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
            temp_model = ModifyDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyMaterialRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None, face_image_url=None, id_card_back_image_url=None,
                 id_card_front_image_url=None, id_card_number=None, name=None, user_id=None):
        self.biz_id = biz_id  # type: str
        self.biz_type = biz_type  # type: str
        self.face_image_url = face_image_url  # type: str
        self.id_card_back_image_url = id_card_back_image_url  # type: str
        self.id_card_front_image_url = id_card_front_image_url  # type: str
        self.id_card_number = id_card_number  # type: str
        self.name = name  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.id_card_back_image_url is not None:
            result['IdCardBackImageUrl'] = self.id_card_back_image_url
        if self.id_card_front_image_url is not None:
            result['IdCardFrontImageUrl'] = self.id_card_front_image_url
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.name is not None:
            result['Name'] = self.name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('IdCardBackImageUrl') is not None:
            self.id_card_back_image_url = m.get('IdCardBackImageUrl')
        if m.get('IdCardFrontImageUrl') is not None:
            self.id_card_front_image_url = m.get('IdCardFrontImageUrl')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class VerifyMaterialResponseBodyMaterialIdCardInfo(TeaModel):
    def __init__(self, address=None, authority=None, back_image_url=None, birth=None, end_date=None,
                 front_image_url=None, name=None, nationality=None, number=None, start_date=None):
        self.address = address  # type: str
        self.authority = authority  # type: str
        self.back_image_url = back_image_url  # type: str
        self.birth = birth  # type: str
        self.end_date = end_date  # type: str
        self.front_image_url = front_image_url  # type: str
        self.name = name  # type: str
        self.nationality = nationality  # type: str
        self.number = number  # type: str
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyMaterialResponseBodyMaterialIdCardInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.number is not None:
            result['Number'] = self.number
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class VerifyMaterialResponseBodyMaterial(TeaModel):
    def __init__(self, face_global_url=None, face_image_url=None, face_mask=None, face_quality=None,
                 id_card_info=None, id_card_name=None, id_card_number=None):
        self.face_global_url = face_global_url  # type: str
        self.face_image_url = face_image_url  # type: str
        self.face_mask = face_mask  # type: str
        self.face_quality = face_quality  # type: str
        self.id_card_info = id_card_info  # type: VerifyMaterialResponseBodyMaterialIdCardInfo
        self.id_card_name = id_card_name  # type: str
        self.id_card_number = id_card_number  # type: str

    def validate(self):
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        _map = super(VerifyMaterialResponseBodyMaterial, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_global_url is not None:
            result['FaceGlobalUrl'] = self.face_global_url
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.face_mask is not None:
            result['FaceMask'] = self.face_mask
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceGlobalUrl') is not None:
            self.face_global_url = m.get('FaceGlobalUrl')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('FaceMask') is not None:
            self.face_mask = m.get('FaceMask')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('IdCardInfo') is not None:
            temp_model = VerifyMaterialResponseBodyMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        return self


class VerifyMaterialResponseBody(TeaModel):
    def __init__(self, authority_comparision_score=None, id_card_face_comparison_score=None, material=None,
                 request_id=None, verify_status=None, verify_token=None):
        self.authority_comparision_score = authority_comparision_score  # type: float
        self.id_card_face_comparison_score = id_card_face_comparison_score  # type: float
        self.material = material  # type: VerifyMaterialResponseBodyMaterial
        self.request_id = request_id  # type: str
        self.verify_status = verify_status  # type: int
        self.verify_token = verify_token  # type: str

    def validate(self):
        if self.material:
            self.material.validate()

    def to_map(self):
        _map = super(VerifyMaterialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority_comparision_score is not None:
            result['AuthorityComparisionScore'] = self.authority_comparision_score
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.material is not None:
            result['Material'] = self.material.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorityComparisionScore') is not None:
            self.authority_comparision_score = m.get('AuthorityComparisionScore')
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        if m.get('Material') is not None:
            temp_model = VerifyMaterialResponseBodyMaterial()
            self.material = temp_model.from_map(m['Material'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        return self


class VerifyMaterialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyMaterialResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyMaterialResponse, self).to_map()
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
            temp_model = VerifyMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


