# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class VerifyMaterialRequest(TeaModel):
    def __init__(self, id_card_back_image_url=None, face_image_url=None, biz_type=None, biz_id=None, name=None,
                 id_card_number=None, id_card_front_image_url=None, user_id=None):
        self.id_card_back_image_url = id_card_back_image_url  # type: str
        self.face_image_url = face_image_url  # type: str
        self.biz_type = biz_type  # type: str
        self.biz_id = biz_id  # type: str
        self.name = name  # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_front_image_url = id_card_front_image_url  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyMaterialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_card_back_image_url is not None:
            result['IdCardBackImageUrl'] = self.id_card_back_image_url
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.id_card_front_image_url is not None:
            result['IdCardFrontImageUrl'] = self.id_card_front_image_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdCardBackImageUrl') is not None:
            self.id_card_back_image_url = m.get('IdCardBackImageUrl')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('IdCardFrontImageUrl') is not None:
            self.id_card_front_image_url = m.get('IdCardFrontImageUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class VerifyMaterialResponseBodyMaterialIdCardInfo(TeaModel):
    def __init__(self, end_date=None, authority=None, address=None, number=None, start_date=None,
                 back_image_url=None, nationality=None, birth=None, name=None, front_image_url=None):
        self.end_date = end_date  # type: str
        self.authority = authority  # type: str
        self.address = address  # type: str
        self.number = number  # type: str
        self.start_date = start_date  # type: str
        self.back_image_url = back_image_url  # type: str
        self.nationality = nationality  # type: str
        self.birth = birth  # type: str
        self.name = name  # type: str
        self.front_image_url = front_image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyMaterialResponseBodyMaterialIdCardInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.address is not None:
            result['Address'] = self.address
        if self.number is not None:
            result['Number'] = self.number
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.name is not None:
            result['Name'] = self.name
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        return self


class VerifyMaterialResponseBodyMaterial(TeaModel):
    def __init__(self, id_card_number=None, face_global_url=None, face_image_url=None, face_mask=None,
                 id_card_name=None, face_quality=None, id_card_info=None):
        self.id_card_number = id_card_number  # type: str
        self.face_global_url = face_global_url  # type: str
        self.face_image_url = face_image_url  # type: str
        self.face_mask = face_mask  # type: str
        self.id_card_name = id_card_name  # type: str
        self.face_quality = face_quality  # type: str
        self.id_card_info = id_card_info  # type: VerifyMaterialResponseBodyMaterialIdCardInfo

    def validate(self):
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        _map = super(VerifyMaterialResponseBodyMaterial, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.face_global_url is not None:
            result['FaceGlobalUrl'] = self.face_global_url
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.face_mask is not None:
            result['FaceMask'] = self.face_mask
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('FaceGlobalUrl') is not None:
            self.face_global_url = m.get('FaceGlobalUrl')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('FaceMask') is not None:
            self.face_mask = m.get('FaceMask')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('IdCardInfo') is not None:
            temp_model = VerifyMaterialResponseBodyMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        return self


class VerifyMaterialResponseBody(TeaModel):
    def __init__(self, authority_comparision_score=None, verify_status=None, request_id=None, verify_token=None,
                 id_card_face_comparison_score=None, material=None):
        self.authority_comparision_score = authority_comparision_score  # type: float
        self.verify_status = verify_status  # type: int
        self.request_id = request_id  # type: str
        self.verify_token = verify_token  # type: str
        self.id_card_face_comparison_score = id_card_face_comparison_score  # type: float
        self.material = material  # type: VerifyMaterialResponseBodyMaterial

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
        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.material is not None:
            result['Material'] = self.material.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorityComparisionScore') is not None:
            self.authority_comparision_score = m.get('AuthorityComparisionScore')
        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        if m.get('Material') is not None:
            temp_model = VerifyMaterialResponseBodyMaterial()
            self.material = temp_model.from_map(m['Material'])
        return self


class VerifyMaterialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: VerifyMaterialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyMaterialResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWhitelistRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, biz_type=None, biz_id=None, id_card_num=None,
                 valid_start_date=None, valid_end_date=None, valid=None, page_size=None, current_page=None):
        self.source_ip = source_ip  # type: str
        self.lang = lang  # type: str
        self.biz_type = biz_type  # type: str
        self.biz_id = biz_id  # type: str
        self.id_card_num = id_card_num  # type: str
        self.valid_start_date = valid_start_date  # type: str
        self.valid_end_date = valid_end_date  # type: str
        self.valid = valid  # type: str
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.id_card_num is not None:
            result['IdCardNum'] = self.id_card_num
        if self.valid_start_date is not None:
            result['ValidStartDate'] = self.valid_start_date
        if self.valid_end_date is not None:
            result['ValidEndDate'] = self.valid_end_date
        if self.valid is not None:
            result['Valid'] = self.valid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IdCardNum') is not None:
            self.id_card_num = m.get('IdCardNum')
        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')
        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeWhitelistResponseBodyItems(TeaModel):
    def __init__(self, end_date=None, gmt_create=None, biz_id=None, start_date=None, id_card_num=None,
                 gmt_modified=None, valid=None, id=None, biz_type=None, uid=None):
        self.end_date = end_date  # type: long
        self.gmt_create = gmt_create  # type: long
        self.biz_id = biz_id  # type: str
        self.start_date = start_date  # type: long
        self.id_card_num = id_card_num  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.valid = valid  # type: int
        self.id = id  # type: long
        self.biz_type = biz_type  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWhitelistResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.id_card_num is not None:
            result['IdCardNum'] = self.id_card_num
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.valid is not None:
            result['Valid'] = self.valid
        if self.id is not None:
            result['Id'] = self.id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('IdCardNum') is not None:
            self.id_card_num = m.get('IdCardNum')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeWhitelistResponseBody(TeaModel):
    def __init__(self, current_page=None, page_size=None, request_id=None, total_count=None, items=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.items = items  # type: list[DescribeWhitelistResponseBodyItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWhitelistResponseBody, self).to_map()
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
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
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
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeWhitelistResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeWhitelistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWhitelistResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppPackageRequest(TeaModel):
    def __init__(self, id=None, package_url=None, platform=None, debug=None):
        self.id = id  # type: long
        self.package_url = package_url  # type: str
        self.platform = platform  # type: str
        self.debug = debug  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.debug is not None:
            result['Debug'] = self.debug
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        return self


class UpdateAppPackageResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppPackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAppPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppPackageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAppPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyTokenRequest(TeaModel):
    def __init__(self, id_card_back_image_url=None, biz_type=None, failed_redirect_url=None,
                 face_retained_image_url=None, callback_seed=None, id_card_front_image_url=None, user_id=None, biz_id=None, name=None,
                 id_card_number=None, passed_redirect_url=None, callback_url=None, user_ip=None, user_phone_number=None,
                 user_regist_time=None):
        self.id_card_back_image_url = id_card_back_image_url  # type: str
        self.biz_type = biz_type  # type: str
        self.failed_redirect_url = failed_redirect_url  # type: str
        self.face_retained_image_url = face_retained_image_url  # type: str
        self.callback_seed = callback_seed  # type: str
        self.id_card_front_image_url = id_card_front_image_url  # type: str
        self.user_id = user_id  # type: str
        self.biz_id = biz_id  # type: str
        self.name = name  # type: str
        self.id_card_number = id_card_number  # type: str
        self.passed_redirect_url = passed_redirect_url  # type: str
        self.callback_url = callback_url  # type: str
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
        if self.id_card_back_image_url is not None:
            result['IdCardBackImageUrl'] = self.id_card_back_image_url
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.failed_redirect_url is not None:
            result['FailedRedirectUrl'] = self.failed_redirect_url
        if self.face_retained_image_url is not None:
            result['FaceRetainedImageUrl'] = self.face_retained_image_url
        if self.callback_seed is not None:
            result['CallbackSeed'] = self.callback_seed
        if self.id_card_front_image_url is not None:
            result['IdCardFrontImageUrl'] = self.id_card_front_image_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.passed_redirect_url is not None:
            result['PassedRedirectUrl'] = self.passed_redirect_url
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.user_ip is not None:
            result['UserIp'] = self.user_ip
        if self.user_phone_number is not None:
            result['UserPhoneNumber'] = self.user_phone_number
        if self.user_regist_time is not None:
            result['UserRegistTime'] = self.user_regist_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdCardBackImageUrl') is not None:
            self.id_card_back_image_url = m.get('IdCardBackImageUrl')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('FailedRedirectUrl') is not None:
            self.failed_redirect_url = m.get('FailedRedirectUrl')
        if m.get('FaceRetainedImageUrl') is not None:
            self.face_retained_image_url = m.get('FaceRetainedImageUrl')
        if m.get('CallbackSeed') is not None:
            self.callback_seed = m.get('CallbackSeed')
        if m.get('IdCardFrontImageUrl') is not None:
            self.id_card_front_image_url = m.get('IdCardFrontImageUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('PassedRedirectUrl') is not None:
            self.passed_redirect_url = m.get('PassedRedirectUrl')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('UserIp') is not None:
            self.user_ip = m.get('UserIp')
        if m.get('UserPhoneNumber') is not None:
            self.user_phone_number = m.get('UserPhoneNumber')
        if m.get('UserRegistTime') is not None:
            self.user_regist_time = m.get('UserRegistTime')
        return self


class DescribeVerifyTokenResponseBodyOssUploadToken(TeaModel):
    def __init__(self, key=None, token=None, secret=None, expired=None, path=None, end_point=None, bucket=None):
        self.key = key  # type: str
        self.token = token  # type: str
        self.secret = secret  # type: str
        self.expired = expired  # type: long
        self.path = path  # type: str
        self.end_point = end_point  # type: str
        self.bucket = bucket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifyTokenResponseBodyOssUploadToken, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.token is not None:
            result['Token'] = self.token
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.path is not None:
            result['Path'] = self.path
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class DescribeVerifyTokenResponseBody(TeaModel):
    def __init__(self, verify_page_url=None, request_id=None, verify_token=None, oss_upload_token=None):
        self.verify_page_url = verify_page_url  # type: str
        self.request_id = request_id  # type: str
        self.verify_token = verify_token  # type: str
        self.oss_upload_token = oss_upload_token  # type: DescribeVerifyTokenResponseBodyOssUploadToken

    def validate(self):
        if self.oss_upload_token:
            self.oss_upload_token.validate()

    def to_map(self):
        _map = super(DescribeVerifyTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verify_page_url is not None:
            result['VerifyPageUrl'] = self.verify_page_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        if self.oss_upload_token is not None:
            result['OssUploadToken'] = self.oss_upload_token.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VerifyPageUrl') is not None:
            self.verify_page_url = m.get('VerifyPageUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        if m.get('OssUploadToken') is not None:
            temp_model = DescribeVerifyTokenResponseBodyOssUploadToken()
            self.oss_upload_token = temp_model.from_map(m['OssUploadToken'])
        return self


class DescribeVerifyTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVerifyTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVerifyTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVerifyTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRPSDKRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, task_id=None):
        self.source_ip = source_ip  # type: str
        self.lang = lang  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRPSDKRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeRPSDKResponseBody(TeaModel):
    def __init__(self, sdk_url=None, request_id=None):
        self.sdk_url = sdk_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRPSDKResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRPSDKResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRPSDKResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRPSDKResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRPSDKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaceUsageRequest(TeaModel):
    def __init__(self, start_date=None, end_date=None):
        self.start_date = start_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaceUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class DescribeFaceUsageResponseBodyFaceUsageList(TeaModel):
    def __init__(self, total_count=None, date=None):
        self.total_count = total_count  # type: long
        self.date = date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaceUsageResponseBodyFaceUsageList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class DescribeFaceUsageResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, face_usage_list=None):
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.face_usage_list = face_usage_list  # type: list[DescribeFaceUsageResponseBodyFaceUsageList]

    def validate(self):
        if self.face_usage_list:
            for k in self.face_usage_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFaceUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['FaceUsageList'] = []
        if self.face_usage_list is not None:
            for k in self.face_usage_list:
                result['FaceUsageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.face_usage_list = []
        if m.get('FaceUsageList') is not None:
            for k in m.get('FaceUsageList'):
                temp_model = DescribeFaceUsageResponseBodyFaceUsageList()
                self.face_usage_list.append(temp_model.from_map(k))
        return self


class DescribeFaceUsageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFaceUsageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFaceUsageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFaceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyUsageRequest(TeaModel):
    def __init__(self, biz_type=None, start_date=None, end_date=None):
        self.biz_type = biz_type  # type: str
        self.start_date = start_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifyUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class DescribeVerifyUsageResponseBodyVerifyUsageList(TeaModel):
    def __init__(self, date=None, pass_count=None, total_count=None, fail_count=None, biz_type=None):
        self.date = date  # type: str
        self.pass_count = pass_count  # type: long
        self.total_count = total_count  # type: long
        self.fail_count = fail_count  # type: long
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifyUsageResponseBodyVerifyUsageList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.pass_count is not None:
            result['PassCount'] = self.pass_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class DescribeVerifyUsageResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, verify_usage_list=None):
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.verify_usage_list = verify_usage_list  # type: list[DescribeVerifyUsageResponseBodyVerifyUsageList]

    def validate(self):
        if self.verify_usage_list:
            for k in self.verify_usage_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVerifyUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VerifyUsageList'] = []
        if self.verify_usage_list is not None:
            for k in self.verify_usage_list:
                result['VerifyUsageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.verify_usage_list = []
        if m.get('VerifyUsageList') is not None:
            for k in m.get('VerifyUsageList'):
                temp_model = DescribeVerifyUsageResponseBodyVerifyUsageList()
                self.verify_usage_list.append(temp_model.from_map(k))
        return self


class DescribeVerifyUsageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVerifyUsageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVerifyUsageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVerifyUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUpdatePackageResultRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUpdatePackageResultRequest, self).to_map()
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


class DescribeUpdatePackageResultResponseBodyAppInfo(TeaModel):
    def __init__(self, type=None, end_date=None, package_name=None, icon=None, start_date=None, name=None, id=None,
                 package_info=None, debug_package_info=None):
        self.type = type  # type: int
        self.end_date = end_date  # type: str
        self.package_name = package_name  # type: str
        self.icon = icon  # type: str
        self.start_date = start_date  # type: str
        self.name = name  # type: str
        self.id = id  # type: long
        self.package_info = package_info  # type: DescribeUpdatePackageResultResponseBodyAppInfoPackageInfo
        self.debug_package_info = debug_package_info  # type: DescribeUpdatePackageResultResponseBodyAppInfoDebugPackageInfo

    def validate(self):
        if self.package_info:
            self.package_info.validate()
        if self.debug_package_info:
            self.debug_package_info.validate()

    def to_map(self):
        _map = super(DescribeUpdatePackageResultResponseBodyAppInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.package_info is not None:
            result['PackageInfo'] = self.package_info.to_map()
        if self.debug_package_info is not None:
            result['DebugPackageInfo'] = self.debug_package_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PackageInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseBodyAppInfoPackageInfo()
            self.package_info = temp_model.from_map(m['PackageInfo'])
        if m.get('DebugPackageInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseBodyAppInfoDebugPackageInfo()
            self.debug_package_info = temp_model.from_map(m['DebugPackageInfo'])
        return self


class DescribeUpdatePackageResultResponseBody(TeaModel):
    def __init__(self, request_id=None, app_info=None):
        self.request_id = request_id  # type: str
        self.app_info = app_info  # type: DescribeUpdatePackageResultResponseBodyAppInfo

    def validate(self):
        if self.app_info:
            self.app_info.validate()

    def to_map(self):
        _map = super(DescribeUpdatePackageResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_info is not None:
            result['AppInfo'] = self.app_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AppInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseBodyAppInfo()
            self.app_info = temp_model.from_map(m['AppInfo'])
        return self


class DescribeUpdatePackageResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUpdatePackageResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUpdatePackageResultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUpdatePackageResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWhitelistRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, biz_type=None, biz_id=None, id_card_num=None, valid_day=None):
        self.source_ip = source_ip  # type: str
        self.lang = lang  # type: str
        self.biz_type = biz_type  # type: str
        self.biz_id = biz_id  # type: str
        self.id_card_num = id_card_num  # type: str
        self.valid_day = valid_day  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.id_card_num is not None:
            result['IdCardNum'] = self.id_card_num
        if self.valid_day is not None:
            result['ValidDay'] = self.valid_day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IdCardNum') is not None:
            self.id_card_num = m.get('IdCardNum')
        if m.get('ValidDay') is not None:
            self.valid_day = m.get('ValidDay')
        return self


class CreateWhitelistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWhitelistResponseBody, self).to_map()
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


class CreateWhitelistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWhitelistResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWhitelistRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, ids=None):
        self.source_ip = source_ip  # type: str
        self.lang = lang  # type: str
        self.ids = ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DeleteWhitelistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWhitelistResponseBody, self).to_map()
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


class DeleteWhitelistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWhitelistResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuthKeyRequest(TeaModel):
    def __init__(self, biz_type=None, user_device_id=None, test=None, auth_years=None):
        self.biz_type = biz_type  # type: str
        self.user_device_id = user_device_id  # type: str
        self.test = test  # type: bool
        self.auth_years = auth_years  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuthKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        if self.test is not None:
            result['Test'] = self.test
        if self.auth_years is not None:
            result['AuthYears'] = self.auth_years
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        if m.get('Test') is not None:
            self.test = m.get('Test')
        if m.get('AuthYears') is not None:
            self.auth_years = m.get('AuthYears')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAuthKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAuthKeyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAuthKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUploadInfoRequest(TeaModel):
    def __init__(self, biz=None):
        self.biz = biz  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUploadInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz is not None:
            result['Biz'] = self.biz
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')
        return self


class DescribeUploadInfoResponseBody(TeaModel):
    def __init__(self, signature=None, host=None, request_id=None, policy=None, accessid=None, folder=None,
                 expire=None):
        self.signature = signature  # type: str
        self.host = host  # type: str
        self.request_id = request_id  # type: str
        self.policy = policy  # type: str
        self.accessid = accessid  # type: str
        self.folder = folder  # type: str
        self.expire = expire  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUploadInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.host is not None:
            result['Host'] = self.host
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.accessid is not None:
            result['Accessid'] = self.accessid
        if self.folder is not None:
            result['Folder'] = self.folder
        if self.expire is not None:
            result['Expire'] = self.expire
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')
        if m.get('Folder') is not None:
            self.folder = m.get('Folder')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        return self


class DescribeUploadInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUploadInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUploadInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUploadInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifySettingResponseBodyVerifySettingList(TeaModel):
    def __init__(self, biz_name=None, solution=None, biz_type=None, step_list=None):
        self.biz_name = biz_name  # type: str
        self.solution = solution  # type: str
        self.biz_type = biz_type  # type: str
        self.step_list = step_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifySettingResponseBodyVerifySettingList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.step_list is not None:
            result['StepList'] = self.step_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('StepList') is not None:
            self.step_list = m.get('StepList')
        return self


class DescribeVerifySettingResponseBody(TeaModel):
    def __init__(self, request_id=None, verify_setting_list=None):
        self.request_id = request_id  # type: str
        self.verify_setting_list = verify_setting_list  # type: list[DescribeVerifySettingResponseBodyVerifySettingList]

    def validate(self):
        if self.verify_setting_list:
            for k in self.verify_setting_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVerifySettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VerifySettingList'] = []
        if self.verify_setting_list is not None:
            for k in self.verify_setting_list:
                result['VerifySettingList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.verify_setting_list = []
        if m.get('VerifySettingList') is not None:
            for k in m.get('VerifySettingList'):
                temp_model = DescribeVerifySettingResponseBodyVerifySettingList()
                self.verify_setting_list.append(temp_model.from_map(k))
        return self


class DescribeVerifySettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVerifySettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVerifySettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVerifySettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyRecordsRequest(TeaModel):
    def __init__(self, total_count=None, page_size=None, current_page=None, biz_type=None, start_date=None,
                 end_date=None, biz_id=None, id_card_num=None, status_list=None, query_id=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int
        self.biz_type = biz_type  # type: str
        self.start_date = start_date  # type: str
        self.end_date = end_date  # type: str
        self.biz_id = biz_id  # type: str
        self.id_card_num = id_card_num  # type: str
        self.status_list = status_list  # type: str
        self.query_id = query_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifyRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.id_card_num is not None:
            result['IdCardNum'] = self.id_card_num
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IdCardNum') is not None:
            self.id_card_num = m.get('IdCardNum')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class DescribeVerifyRecordsResponseBodyRecordsListMaterialIdCardInfo(TeaModel):
    def __init__(self, end_date=None, sex=None, authority=None, address=None, number=None, start_date=None,
                 nationality=None, back_image_url=None, birth=None, name=None, front_image_url=None):
        self.end_date = end_date  # type: str
        self.sex = sex  # type: str
        self.authority = authority  # type: str
        self.address = address  # type: str
        self.number = number  # type: str
        self.start_date = start_date  # type: str
        self.nationality = nationality  # type: str
        self.back_image_url = back_image_url  # type: str
        self.birth = birth  # type: str
        self.name = name  # type: str
        self.front_image_url = front_image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifyRecordsResponseBodyRecordsListMaterialIdCardInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.sex is not None:
            result['Sex'] = self.sex
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.address is not None:
            result['Address'] = self.address
        if self.number is not None:
            result['Number'] = self.number
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.name is not None:
            result['Name'] = self.name
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        return self


class DescribeVerifyRecordsResponseBodyRecordsListMaterial(TeaModel):
    def __init__(self, id_card_number=None, face_image_url=None, id_card_name=None, id_card_info=None):
        self.id_card_number = id_card_number  # type: str
        self.face_image_url = face_image_url  # type: str
        self.id_card_name = id_card_name  # type: str
        self.id_card_info = id_card_info  # type: DescribeVerifyRecordsResponseBodyRecordsListMaterialIdCardInfo

    def validate(self):
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        _map = super(DescribeVerifyRecordsResponseBodyRecordsListMaterial, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('IdCardInfo') is not None:
            temp_model = DescribeVerifyRecordsResponseBodyRecordsListMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        return self


class DescribeVerifyRecordsResponseBodyRecordsList(TeaModel):
    def __init__(self, status=None, finish_time=None, id_card_face_comparison_score=None, biz_id=None,
                 verify_id=None, authority_comparison_score=None, data_stats=None, biz_type=None, material=None):
        self.status = status  # type: int
        self.finish_time = finish_time  # type: long
        self.id_card_face_comparison_score = id_card_face_comparison_score  # type: float
        self.biz_id = biz_id  # type: str
        self.verify_id = verify_id  # type: str
        self.authority_comparison_score = authority_comparison_score  # type: float
        self.data_stats = data_stats  # type: str
        self.biz_type = biz_type  # type: str
        self.material = material  # type: DescribeVerifyRecordsResponseBodyRecordsListMaterial

    def validate(self):
        if self.material:
            self.material.validate()

    def to_map(self):
        _map = super(DescribeVerifyRecordsResponseBodyRecordsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.verify_id is not None:
            result['VerifyId'] = self.verify_id
        if self.authority_comparison_score is not None:
            result['AuthorityComparisonScore'] = self.authority_comparison_score
        if self.data_stats is not None:
            result['DataStats'] = self.data_stats
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.material is not None:
            result['Material'] = self.material.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('VerifyId') is not None:
            self.verify_id = m.get('VerifyId')
        if m.get('AuthorityComparisonScore') is not None:
            self.authority_comparison_score = m.get('AuthorityComparisonScore')
        if m.get('DataStats') is not None:
            self.data_stats = m.get('DataStats')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Material') is not None:
            temp_model = DescribeVerifyRecordsResponseBodyRecordsListMaterial()
            self.material = temp_model.from_map(m['Material'])
        return self


class DescribeVerifyRecordsResponseBody(TeaModel):
    def __init__(self, current_page=None, page_size=None, request_id=None, total_count=None, query_id=None,
                 records_list=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.query_id = query_id  # type: str
        self.records_list = records_list  # type: list[DescribeVerifyRecordsResponseBodyRecordsList]

    def validate(self):
        if self.records_list:
            for k in self.records_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVerifyRecordsResponseBody, self).to_map()
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
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        result['RecordsList'] = []
        if self.records_list is not None:
            for k in self.records_list:
                result['RecordsList'].append(k.to_map() if k else None)
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
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        self.records_list = []
        if m.get('RecordsList') is not None:
            for k in m.get('RecordsList'):
                temp_model = DescribeVerifyRecordsResponseBodyRecordsList()
                self.records_list.append(temp_model.from_map(k))
        return self


class DescribeVerifyRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVerifyRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVerifyRecordsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVerifyRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWhitelistSettingRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, service_code=None, scene_id=None, certify_id=None, cert_no=None,
                 valid_start_date=None, valid_end_date=None, status=None, page_size=None, current_page=None):
        self.source_ip = source_ip  # type: str
        self.lang = lang  # type: str
        self.service_code = service_code  # type: str
        self.scene_id = scene_id  # type: long
        self.certify_id = certify_id  # type: str
        self.cert_no = cert_no  # type: str
        self.valid_start_date = valid_start_date  # type: long
        self.valid_end_date = valid_end_date  # type: long
        self.status = status  # type: str
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWhitelistSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.valid_start_date is not None:
            result['ValidStartDate'] = self.valid_start_date
        if self.valid_end_date is not None:
            result['ValidEndDate'] = self.valid_end_date
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')
        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeWhitelistSettingResponseBodyItems(TeaModel):
    def __init__(self, status=None, gmt_create=None, certify_id=None, cert_no=None, valid_start_date=None,
                 scene_id=None, gmt_modified=None, valid_end_date=None, id=None):
        self.status = status  # type: str
        self.gmt_create = gmt_create  # type: str
        self.certify_id = certify_id  # type: str
        self.cert_no = cert_no  # type: str
        self.valid_start_date = valid_start_date  # type: str
        self.scene_id = scene_id  # type: long
        self.gmt_modified = gmt_modified  # type: str
        self.valid_end_date = valid_end_date  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWhitelistSettingResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.valid_start_date is not None:
            result['ValidStartDate'] = self.valid_start_date
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.valid_end_date is not None:
            result['ValidEndDate'] = self.valid_end_date
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('ValidStartDate') is not None:
            self.valid_start_date = m.get('ValidStartDate')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ValidEndDate') is not None:
            self.valid_end_date = m.get('ValidEndDate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeWhitelistSettingResponseBody(TeaModel):
    def __init__(self, current_page=None, page_size=None, request_id=None, total_count=None, items=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.items = items  # type: list[DescribeWhitelistSettingResponseBodyItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWhitelistSettingResponseBody, self).to_map()
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
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
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
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeWhitelistSettingResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeWhitelistSettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeWhitelistSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWhitelistSettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWhitelistSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRPSDKRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, app_url=None, platform=None):
        self.source_ip = source_ip  # type: str
        self.lang = lang  # type: str
        self.app_url = app_url  # type: str
        self.platform = platform  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRPSDKRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.app_url is not None:
            result['AppUrl'] = self.app_url
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('AppUrl') is not None:
            self.app_url = m.get('AppUrl')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class CreateRPSDKResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRPSDKResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRPSDKResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRPSDKResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRPSDKResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRPSDKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFaceConfigRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, biz_type=None, biz_name=None):
        self.source_ip = source_ip  # type: str
        self.lang = lang  # type: str
        self.biz_type = biz_type  # type: str
        self.biz_name = biz_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFaceConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        return self


class UpdateFaceConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFaceConfigResponseBody, self).to_map()
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


class UpdateFaceConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateFaceConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFaceConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateFaceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaceConfigRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None):
        self.source_ip = source_ip  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaceConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeFaceConfigResponseBodyItems(TeaModel):
    def __init__(self, biz_name=None, biz_type=None, gmt_updated=None):
        self.biz_name = biz_name  # type: str
        self.biz_type = biz_type  # type: str
        self.gmt_updated = gmt_updated  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaceConfigResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.gmt_updated is not None:
            result['GmtUpdated'] = self.gmt_updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('GmtUpdated') is not None:
            self.gmt_updated = m.get('GmtUpdated')
        return self


class DescribeFaceConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, items=None):
        self.request_id = request_id  # type: str
        self.items = items  # type: list[DescribeFaceConfigResponseBodyItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFaceConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeFaceConfigResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeFaceConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFaceConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFaceConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFaceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LivenessFaceVerifyRequest(TeaModel):
    def __init__(self, scene_id=None, outer_order_no=None, product_code=None, face_contrast_picture=None,
                 device_token=None, mobile=None, ip=None, user_id=None, face_contrast_picture_url=None, certify_id=None,
                 oss_bucket_name=None, oss_object_name=None, model=None, crop=None):
        self.scene_id = scene_id  # type: long
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.face_contrast_picture = face_contrast_picture  # type: str
        self.device_token = device_token  # type: str
        self.mobile = mobile  # type: str
        self.ip = ip  # type: str
        self.user_id = user_id  # type: str
        self.face_contrast_picture_url = face_contrast_picture_url  # type: str
        self.certify_id = certify_id  # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.model = model  # type: str
        self.crop = crop  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LivenessFaceVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.model is not None:
            result['Model'] = self.model
        if self.crop is not None:
            result['Crop'] = self.crop
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        return self


class LivenessFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(self, certify_id=None, sub_code=None, material_info=None, passed=None):
        self.certify_id = certify_id  # type: str
        self.sub_code = sub_code  # type: str
        self.material_info = material_info  # type: str
        self.passed = passed  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LivenessFaceVerifyResponseBodyResultObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: LivenessFaceVerifyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LivenessFaceVerifyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LivenessFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppInfoRequest(TeaModel):
    def __init__(self, page_size=None, current_page=None, platform=None):
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int
        self.platform = platform  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
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


class DescribeAppInfoResponseBodyAppInfoList(TeaModel):
    def __init__(self, type=None, end_date=None, package_name=None, icon=None, start_date=None, name=None, id=None,
                 package_info=None, debug_package_info=None):
        self.type = type  # type: int
        self.end_date = end_date  # type: str
        self.package_name = package_name  # type: str
        self.icon = icon  # type: str
        self.start_date = start_date  # type: str
        self.name = name  # type: str
        self.id = id  # type: long
        self.package_info = package_info  # type: DescribeAppInfoResponseBodyAppInfoListPackageInfo
        self.debug_package_info = debug_package_info  # type: DescribeAppInfoResponseBodyAppInfoListDebugPackageInfo

    def validate(self):
        if self.package_info:
            self.package_info.validate()
        if self.debug_package_info:
            self.debug_package_info.validate()

    def to_map(self):
        _map = super(DescribeAppInfoResponseBodyAppInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.package_info is not None:
            result['PackageInfo'] = self.package_info.to_map()
        if self.debug_package_info is not None:
            result['DebugPackageInfo'] = self.debug_package_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PackageInfo') is not None:
            temp_model = DescribeAppInfoResponseBodyAppInfoListPackageInfo()
            self.package_info = temp_model.from_map(m['PackageInfo'])
        if m.get('DebugPackageInfo') is not None:
            temp_model = DescribeAppInfoResponseBodyAppInfoListDebugPackageInfo()
            self.debug_package_info = temp_model.from_map(m['DebugPackageInfo'])
        return self


class DescribeAppInfoResponseBody(TeaModel):
    def __init__(self, current_page=None, request_id=None, page_size=None, total_count=None, app_info_list=None):
        self.current_page = current_page  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.app_info_list = app_info_list  # type: list[DescribeAppInfoResponseBodyAppInfoList]

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k in m.get('AppInfoList'):
                temp_model = DescribeAppInfoResponseBodyAppInfoList()
                self.app_info_list.append(temp_model.from_map(k))
        return self


class DescribeAppInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAppInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeviceInfoRequest(TeaModel):
    def __init__(self, device_id=None, user_device_id=None, biz_type=None, duration=None, expired_day=None):
        self.device_id = device_id  # type: str
        self.user_device_id = user_device_id  # type: str
        self.biz_type = biz_type  # type: str
        self.duration = duration  # type: str
        self.expired_day = expired_day  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        return self


class ModifyDeviceInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, user_device_id=None, device_id=None, expired_day=None, begin_day=None,
                 biz_type=None):
        self.request_id = request_id  # type: str
        self.user_device_id = user_device_id  # type: str
        self.device_id = device_id  # type: str
        self.expired_day = expired_day  # type: str
        self.begin_day = begin_day  # type: str
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        if self.begin_day is not None:
            result['BeginDay'] = self.begin_day
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        if m.get('BeginDay') is not None:
            self.begin_day = m.get('BeginDay')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class ModifyDeviceInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDeviceInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDeviceInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContrastFaceVerifyRequest(TeaModel):
    def __init__(self, scene_id=None, outer_order_no=None, product_code=None, cert_type=None, cert_name=None,
                 cert_no=None, face_contrast_picture=None, device_token=None, mobile=None, ip=None, user_id=None,
                 face_contrast_picture_url=None, certify_id=None, oss_bucket_name=None, oss_object_name=None, model=None,
                 face_contrast_file=None, crop=None):
        self.scene_id = scene_id  # type: long
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.cert_type = cert_type  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_no = cert_no  # type: str
        self.face_contrast_picture = face_contrast_picture  # type: str
        self.device_token = device_token  # type: str
        self.mobile = mobile  # type: str
        self.ip = ip  # type: str
        self.user_id = user_id  # type: str
        self.face_contrast_picture_url = face_contrast_picture_url  # type: str
        self.certify_id = certify_id  # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.model = model  # type: str
        self.face_contrast_file = face_contrast_file  # type: str
        self.crop = crop  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContrastFaceVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.model is not None:
            result['Model'] = self.model
        if self.face_contrast_file is not None:
            result['FaceContrastFile'] = self.face_contrast_file
        if self.crop is not None:
            result['Crop'] = self.crop
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('FaceContrastFile') is not None:
            self.face_contrast_file = m.get('FaceContrastFile')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        return self


class ContrastFaceVerifyAdvanceRequest(TeaModel):
    def __init__(self, face_contrast_file_object=None, scene_id=None, outer_order_no=None, product_code=None,
                 cert_type=None, cert_name=None, cert_no=None, face_contrast_picture=None, device_token=None, mobile=None,
                 ip=None, user_id=None, face_contrast_picture_url=None, certify_id=None, oss_bucket_name=None,
                 oss_object_name=None, model=None, crop=None):
        self.face_contrast_file_object = face_contrast_file_object  # type: READABLE
        self.scene_id = scene_id  # type: long
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.cert_type = cert_type  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_no = cert_no  # type: str
        self.face_contrast_picture = face_contrast_picture  # type: str
        self.device_token = device_token  # type: str
        self.mobile = mobile  # type: str
        self.ip = ip  # type: str
        self.user_id = user_id  # type: str
        self.face_contrast_picture_url = face_contrast_picture_url  # type: str
        self.certify_id = certify_id  # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.model = model  # type: str
        self.crop = crop  # type: str

    def validate(self):
        self.validate_required(self.face_contrast_file_object, 'face_contrast_file_object')

    def to_map(self):
        _map = super(ContrastFaceVerifyAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_contrast_file_object is not None:
            result['FaceContrastFileObject'] = self.face_contrast_file_object
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.model is not None:
            result['Model'] = self.model
        if self.crop is not None:
            result['Crop'] = self.crop
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceContrastFileObject') is not None:
            self.face_contrast_file_object = m.get('FaceContrastFileObject')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        return self


class ContrastFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(self, certify_id=None, sub_code=None, material_info=None, identity_info=None, passed=None):
        self.certify_id = certify_id  # type: str
        self.sub_code = sub_code  # type: str
        self.material_info = material_info  # type: str
        self.identity_info = identity_info  # type: str
        self.passed = passed  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContrastFaceVerifyResponseBodyResultObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.identity_info is not None:
            result['IdentityInfo'] = self.identity_info
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('IdentityInfo') is not None:
            self.identity_info = m.get('IdentityInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ContrastFaceVerifyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ContrastFaceVerifyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ContrastFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyDeviceRequest(TeaModel):
    def __init__(self, certify_id=None, certify_data=None, app_version=None, ext_info=None, device_token=None):
        self.certify_id = certify_id  # type: str
        self.certify_data = certify_data  # type: str
        self.app_version = app_version  # type: str
        self.ext_info = ext_info  # type: str
        self.device_token = device_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.certify_data is not None:
            result['CertifyData'] = self.certify_data
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('CertifyData') is not None:
            self.certify_data = m.get('CertifyData')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        return self


class VerifyDeviceResponseBodyResultObject(TeaModel):
    def __init__(self, ret_code_sub=None, product_ret_code=None, has_next=None, ret_message_sub=None,
                 ext_params=None, validation_ret_code=None):
        self.ret_code_sub = ret_code_sub  # type: str
        self.product_ret_code = product_ret_code  # type: str
        self.has_next = has_next  # type: str
        self.ret_message_sub = ret_message_sub  # type: str
        self.ext_params = ext_params  # type: str
        self.validation_ret_code = validation_ret_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyDeviceResponseBodyResultObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ret_code_sub is not None:
            result['RetCodeSub'] = self.ret_code_sub
        if self.product_ret_code is not None:
            result['ProductRetCode'] = self.product_ret_code
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.ret_message_sub is not None:
            result['RetMessageSub'] = self.ret_message_sub
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.validation_ret_code is not None:
            result['ValidationRetCode'] = self.validation_ret_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RetCodeSub') is not None:
            self.ret_code_sub = m.get('RetCodeSub')
        if m.get('ProductRetCode') is not None:
            self.product_ret_code = m.get('ProductRetCode')
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('RetMessageSub') is not None:
            self.ret_message_sub = m.get('RetMessageSub')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('ValidationRetCode') is not None:
            self.validation_ret_code = m.get('ValidationRetCode')
        return self


class VerifyDeviceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result_object=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result_object = result_object  # type: VerifyDeviceResponseBodyResultObject

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super(VerifyDeviceResponseBody, self).to_map()
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
            temp_model = VerifyDeviceResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class VerifyDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: VerifyDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyDeviceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompareFaceVerifyRequest(TeaModel):
    def __init__(self, scene_id=None, outer_order_no=None, product_code=None, source_face_contrast_picture=None,
                 source_face_contrast_picture_url=None, source_certify_id=None, source_oss_bucket_name=None, source_oss_object_name=None,
                 target_face_contrast_picture=None, target_face_contrast_picture_url=None, target_certify_id=None, target_oss_bucket_name=None,
                 target_oss_object_name=None, crop=None):
        self.scene_id = scene_id  # type: long
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.source_face_contrast_picture = source_face_contrast_picture  # type: str
        self.source_face_contrast_picture_url = source_face_contrast_picture_url  # type: str
        self.source_certify_id = source_certify_id  # type: str
        self.source_oss_bucket_name = source_oss_bucket_name  # type: str
        self.source_oss_object_name = source_oss_object_name  # type: str
        self.target_face_contrast_picture = target_face_contrast_picture  # type: str
        self.target_face_contrast_picture_url = target_face_contrast_picture_url  # type: str
        self.target_certify_id = target_certify_id  # type: str
        self.target_oss_bucket_name = target_oss_bucket_name  # type: str
        self.target_oss_object_name = target_oss_object_name  # type: str
        self.crop = crop  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompareFaceVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.source_face_contrast_picture is not None:
            result['SourceFaceContrastPicture'] = self.source_face_contrast_picture
        if self.source_face_contrast_picture_url is not None:
            result['SourceFaceContrastPictureUrl'] = self.source_face_contrast_picture_url
        if self.source_certify_id is not None:
            result['SourceCertifyId'] = self.source_certify_id
        if self.source_oss_bucket_name is not None:
            result['SourceOssBucketName'] = self.source_oss_bucket_name
        if self.source_oss_object_name is not None:
            result['SourceOssObjectName'] = self.source_oss_object_name
        if self.target_face_contrast_picture is not None:
            result['TargetFaceContrastPicture'] = self.target_face_contrast_picture
        if self.target_face_contrast_picture_url is not None:
            result['TargetFaceContrastPictureUrl'] = self.target_face_contrast_picture_url
        if self.target_certify_id is not None:
            result['TargetCertifyId'] = self.target_certify_id
        if self.target_oss_bucket_name is not None:
            result['TargetOssBucketName'] = self.target_oss_bucket_name
        if self.target_oss_object_name is not None:
            result['TargetOssObjectName'] = self.target_oss_object_name
        if self.crop is not None:
            result['Crop'] = self.crop
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SourceFaceContrastPicture') is not None:
            self.source_face_contrast_picture = m.get('SourceFaceContrastPicture')
        if m.get('SourceFaceContrastPictureUrl') is not None:
            self.source_face_contrast_picture_url = m.get('SourceFaceContrastPictureUrl')
        if m.get('SourceCertifyId') is not None:
            self.source_certify_id = m.get('SourceCertifyId')
        if m.get('SourceOssBucketName') is not None:
            self.source_oss_bucket_name = m.get('SourceOssBucketName')
        if m.get('SourceOssObjectName') is not None:
            self.source_oss_object_name = m.get('SourceOssObjectName')
        if m.get('TargetFaceContrastPicture') is not None:
            self.target_face_contrast_picture = m.get('TargetFaceContrastPicture')
        if m.get('TargetFaceContrastPictureUrl') is not None:
            self.target_face_contrast_picture_url = m.get('TargetFaceContrastPictureUrl')
        if m.get('TargetCertifyId') is not None:
            self.target_certify_id = m.get('TargetCertifyId')
        if m.get('TargetOssBucketName') is not None:
            self.target_oss_bucket_name = m.get('TargetOssBucketName')
        if m.get('TargetOssObjectName') is not None:
            self.target_oss_object_name = m.get('TargetOssObjectName')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        return self


class CompareFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(self, certify_id=None, verify_score=None, passed=None):
        self.certify_id = certify_id  # type: str
        self.verify_score = verify_score  # type: float
        self.passed = passed  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompareFaceVerifyResponseBodyResultObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.verify_score is not None:
            result['VerifyScore'] = self.verify_score
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('VerifyScore') is not None:
            self.verify_score = m.get('VerifyScore')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CompareFaceVerifyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CompareFaceVerifyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CompareFaceVerifyResponseBody()
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
    def __init__(self, sdk_url=None, request_id=None):
        self.sdk_url = sdk_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifySDKResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVerifySDKResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVerifySDKResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVerifySDKResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVerifySDKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceInfoRequest(TeaModel):
    def __init__(self, page_size=None, current_page=None, device_id=None, biz_type=None, user_device_id=None,
                 expired_start_day=None, expired_end_day=None):
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int
        self.device_id = device_id  # type: str
        self.biz_type = biz_type  # type: str
        self.user_device_id = user_device_id  # type: str
        self.expired_start_day = expired_start_day  # type: str
        self.expired_end_day = expired_end_day  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        if self.expired_start_day is not None:
            result['ExpiredStartDay'] = self.expired_start_day
        if self.expired_end_day is not None:
            result['ExpiredEndDay'] = self.expired_end_day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        if m.get('ExpiredStartDay') is not None:
            self.expired_start_day = m.get('ExpiredStartDay')
        if m.get('ExpiredEndDay') is not None:
            self.expired_end_day = m.get('ExpiredEndDay')
        return self


class DescribeDeviceInfoResponseBodyDeviceInfoListDeviceInfo(TeaModel):
    def __init__(self, expired_day=None, user_device_id=None, device_id=None, begin_day=None, biz_type=None):
        self.expired_day = expired_day  # type: str
        self.user_device_id = user_device_id  # type: str
        self.device_id = device_id  # type: str
        self.begin_day = begin_day  # type: str
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceInfoResponseBodyDeviceInfoListDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.begin_day is not None:
            result['BeginDay'] = self.begin_day
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('BeginDay') is not None:
            self.begin_day = m.get('BeginDay')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
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
    def __init__(self, current_page=None, request_id=None, page_size=None, total_count=None, device_info_list=None):
        self.current_page = current_page  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.device_info_list = device_info_list  # type: DescribeDeviceInfoResponseBodyDeviceInfoList

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.device_info_list is not None:
            result['DeviceInfoList'] = self.device_info_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('DeviceInfoList') is not None:
            temp_model = DescribeDeviceInfoResponseBodyDeviceInfoList()
            self.device_info_list = temp_model.from_map(m['DeviceInfoList'])
        return self


class DescribeDeviceInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDeviceInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDeviceInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFaceVerifyRequest(TeaModel):
    def __init__(self, scene_id=None, certify_id=None, picture_return_type=None):
        self.scene_id = scene_id  # type: long
        self.certify_id = certify_id  # type: str
        self.picture_return_type = picture_return_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaceVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.picture_return_type is not None:
            result['PictureReturnType'] = self.picture_return_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('PictureReturnType') is not None:
            self.picture_return_type = m.get('PictureReturnType')
        return self


class DescribeFaceVerifyResponseBodyResultObject(TeaModel):
    def __init__(self, sub_code=None, material_info=None, identity_info=None, device_token=None, passed=None):
        self.sub_code = sub_code  # type: str
        self.material_info = material_info  # type: str
        self.identity_info = identity_info  # type: str
        self.device_token = device_token  # type: str
        self.passed = passed  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFaceVerifyResponseBodyResultObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.identity_info is not None:
            result['IdentityInfo'] = self.identity_info
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.passed is not None:
            result['Passed'] = self.passed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('IdentityInfo') is not None:
            self.identity_info = m.get('IdentityInfo')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFaceVerifyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFaceVerifyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssUploadTokenResponseBodyOssUploadToken(TeaModel):
    def __init__(self, key=None, token=None, secret=None, expired=None, path=None, end_point=None, bucket=None):
        self.key = key  # type: str
        self.token = token  # type: str
        self.secret = secret  # type: str
        self.expired = expired  # type: long
        self.path = path  # type: str
        self.end_point = end_point  # type: str
        self.bucket = bucket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOssUploadTokenResponseBodyOssUploadToken, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.token is not None:
            result['Token'] = self.token
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.path is not None:
            result['Path'] = self.path
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class DescribeOssUploadTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, oss_upload_token=None):
        self.request_id = request_id  # type: str
        self.oss_upload_token = oss_upload_token  # type: DescribeOssUploadTokenResponseBodyOssUploadToken

    def validate(self):
        if self.oss_upload_token:
            self.oss_upload_token.validate()

    def to_map(self):
        _map = super(DescribeOssUploadTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.oss_upload_token is not None:
            result['OssUploadToken'] = self.oss_upload_token.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OssUploadToken') is not None:
            temp_model = DescribeOssUploadTokenResponseBodyOssUploadToken()
            self.oss_upload_token = temp_model.from_map(m['OssUploadToken'])
        return self


class DescribeOssUploadTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeOssUploadTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOssUploadTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeOssUploadTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectFaceAttributesRequest(TeaModel):
    def __init__(self, material_value=None, biz_type=None):
        self.material_value = material_value  # type: str
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectFaceAttributesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_value is not None:
            result['MaterialValue'] = self.material_value
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaterialValue') is not None:
            self.material_value = m.get('MaterialValue')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect(TeaModel):
    def __init__(self, left=None, top=None, width=None, height=None):
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling(TeaModel):
    def __init__(self, value=None, threshold=None):
        self.value = value  # type: float
        self.threshold = threshold  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
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


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes(TeaModel):
    def __init__(self, glasses=None, facequal=None, integrity=None, facetype=None, respirator=None, blur=None,
                 smiling=None, headpose=None):
        self.glasses = glasses  # type: str
        self.facequal = facequal  # type: float
        self.integrity = integrity  # type: int
        self.facetype = facetype  # type: str
        self.respirator = respirator  # type: str
        self.blur = blur  # type: float
        self.smiling = smiling  # type: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling
        self.headpose = headpose  # type: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose

    def validate(self):
        if self.smiling:
            self.smiling.validate()
        if self.headpose:
            self.headpose.validate()

    def to_map(self):
        _map = super(DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.facequal is not None:
            result['Facequal'] = self.facequal
        if self.integrity is not None:
            result['Integrity'] = self.integrity
        if self.facetype is not None:
            result['Facetype'] = self.facetype
        if self.respirator is not None:
            result['Respirator'] = self.respirator
        if self.blur is not None:
            result['Blur'] = self.blur
        if self.smiling is not None:
            result['Smiling'] = self.smiling.to_map()
        if self.headpose is not None:
            result['Headpose'] = self.headpose.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Facequal') is not None:
            self.facequal = m.get('Facequal')
        if m.get('Integrity') is not None:
            self.integrity = m.get('Integrity')
        if m.get('Facetype') is not None:
            self.facetype = m.get('Facetype')
        if m.get('Respirator') is not None:
            self.respirator = m.get('Respirator')
        if m.get('Blur') is not None:
            self.blur = m.get('Blur')
        if m.get('Smiling') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling()
            self.smiling = temp_model.from_map(m['Smiling'])
        if m.get('Headpose') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose()
            self.headpose = temp_model.from_map(m['Headpose'])
        return self


class DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfo(TeaModel):
    def __init__(self, face_rect=None, face_attributes=None):
        self.face_rect = face_rect  # type: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect
        self.face_attributes = face_attributes  # type: DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes

    def validate(self):
        if self.face_rect:
            self.face_rect.validate()
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super(DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_rect is not None:
            result['FaceRect'] = self.face_rect.to_map()
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceRect') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceRect()
            self.face_rect = temp_model.from_map(m['FaceRect'])
        if m.get('FaceAttributes') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfosFaceAttributesDetectInfoFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
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
    def __init__(self, img_height=None, img_width=None, face_infos=None):
        self.img_height = img_height  # type: int
        self.img_width = img_width  # type: int
        self.face_infos = face_infos  # type: DetectFaceAttributesResponseBodyDataFaceInfos

    def validate(self):
        if self.face_infos:
            self.face_infos.validate()

    def to_map(self):
        _map = super(DetectFaceAttributesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.img_height is not None:
            result['ImgHeight'] = self.img_height
        if self.img_width is not None:
            result['ImgWidth'] = self.img_width
        if self.face_infos is not None:
            result['FaceInfos'] = self.face_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImgHeight') is not None:
            self.img_height = m.get('ImgHeight')
        if m.get('ImgWidth') is not None:
            self.img_width = m.get('ImgWidth')
        if m.get('FaceInfos') is not None:
            temp_model = DetectFaceAttributesResponseBodyDataFaceInfos()
            self.face_infos = temp_model.from_map(m['FaceInfos'])
        return self


class DetectFaceAttributesResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, data=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.data = data  # type: DetectFaceAttributesResponseBodyData

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = DetectFaceAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DetectFaceAttributesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetectFaceAttributesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectFaceAttributesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetectFaceAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSdkUrlRequest(TeaModel):
    def __init__(self, id=None, debug=None):
        self.id = id  # type: long
        self.debug = debug  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSdkUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.debug is not None:
            result['Debug'] = self.debug
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        return self


class DescribeSdkUrlResponseBody(TeaModel):
    def __init__(self, sdk_url=None, request_id=None):
        self.sdk_url = sdk_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSdkUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSdkUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSdkUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSdkUrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSdkUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWhitelistSettingRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, service_code=None, ids=None):
        self.source_ip = source_ip  # type: str
        self.lang = lang  # type: str
        self.service_code = service_code  # type: str
        self.ids = ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWhitelistSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DeleteWhitelistSettingResponseBody(TeaModel):
    def __init__(self, result_object=None, request_id=None):
        self.result_object = result_object  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWhitelistSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_object is not None:
            result['ResultObject'] = self.result_object
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResultObject') is not None:
            self.result_object = m.get('ResultObject')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWhitelistSettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteWhitelistSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWhitelistSettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteWhitelistSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVerifySettingRequest(TeaModel):
    def __init__(self, biz_type=None, biz_name=None, solution=None, guide_step=None, privacy_step=None,
                 result_step=None):
        self.biz_type = biz_type  # type: str
        self.biz_name = biz_name  # type: str
        self.solution = solution  # type: str
        self.guide_step = guide_step  # type: bool
        self.privacy_step = privacy_step  # type: bool
        self.result_step = result_step  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVerifySettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.guide_step is not None:
            result['GuideStep'] = self.guide_step
        if self.privacy_step is not None:
            result['PrivacyStep'] = self.privacy_step
        if self.result_step is not None:
            result['ResultStep'] = self.result_step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('GuideStep') is not None:
            self.guide_step = m.get('GuideStep')
        if m.get('PrivacyStep') is not None:
            self.privacy_step = m.get('PrivacyStep')
        if m.get('ResultStep') is not None:
            self.result_step = m.get('ResultStep')
        return self


class UpdateVerifySettingResponseBody(TeaModel):
    def __init__(self, biz_name=None, request_id=None, solution=None, biz_type=None, step_list=None):
        self.biz_name = biz_name  # type: str
        self.request_id = request_id  # type: str
        self.solution = solution  # type: str
        self.biz_type = biz_type  # type: str
        self.step_list = step_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVerifySettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.step_list is not None:
            result['StepList'] = self.step_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('StepList') is not None:
            self.step_list = m.get('StepList')
        return self


class UpdateVerifySettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateVerifySettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVerifySettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateVerifySettingResponseBody()
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
    def __init__(self, end_date=None, authority=None, address=None, number=None, start_date=None,
                 back_image_url=None, nationality=None, birth=None, name=None, front_image_url=None):
        self.end_date = end_date  # type: str
        self.authority = authority  # type: str
        self.address = address  # type: str
        self.number = number  # type: str
        self.start_date = start_date  # type: str
        self.back_image_url = back_image_url  # type: str
        self.nationality = nationality  # type: str
        self.birth = birth  # type: str
        self.name = name  # type: str
        self.front_image_url = front_image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifyResultResponseBodyMaterialIdCardInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.address is not None:
            result['Address'] = self.address
        if self.number is not None:
            result['Number'] = self.number
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.back_image_url is not None:
            result['BackImageUrl'] = self.back_image_url
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.birth is not None:
            result['Birth'] = self.birth
        if self.name is not None:
            result['Name'] = self.name
        if self.front_image_url is not None:
            result['FrontImageUrl'] = self.front_image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('BackImageUrl') is not None:
            self.back_image_url = m.get('BackImageUrl')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Birth') is not None:
            self.birth = m.get('Birth')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FrontImageUrl') is not None:
            self.front_image_url = m.get('FrontImageUrl')
        return self


class DescribeVerifyResultResponseBodyMaterial(TeaModel):
    def __init__(self, id_card_number=None, face_global_url=None, face_image_url=None, face_mask=None,
                 id_card_name=None, face_quality=None, video_urls=None, id_card_info=None):
        self.id_card_number = id_card_number  # type: str
        self.face_global_url = face_global_url  # type: str
        self.face_image_url = face_image_url  # type: str
        self.face_mask = face_mask  # type: bool
        self.id_card_name = id_card_name  # type: str
        self.face_quality = face_quality  # type: str
        self.video_urls = video_urls  # type: list[str]
        self.id_card_info = id_card_info  # type: DescribeVerifyResultResponseBodyMaterialIdCardInfo

    def validate(self):
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        _map = super(DescribeVerifyResultResponseBodyMaterial, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_card_number is not None:
            result['IdCardNumber'] = self.id_card_number
        if self.face_global_url is not None:
            result['FaceGlobalUrl'] = self.face_global_url
        if self.face_image_url is not None:
            result['FaceImageUrl'] = self.face_image_url
        if self.face_mask is not None:
            result['FaceMask'] = self.face_mask
        if self.id_card_name is not None:
            result['IdCardName'] = self.id_card_name
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.video_urls is not None:
            result['VideoUrls'] = self.video_urls
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdCardNumber') is not None:
            self.id_card_number = m.get('IdCardNumber')
        if m.get('FaceGlobalUrl') is not None:
            self.face_global_url = m.get('FaceGlobalUrl')
        if m.get('FaceImageUrl') is not None:
            self.face_image_url = m.get('FaceImageUrl')
        if m.get('FaceMask') is not None:
            self.face_mask = m.get('FaceMask')
        if m.get('IdCardName') is not None:
            self.id_card_name = m.get('IdCardName')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('VideoUrls') is not None:
            self.video_urls = m.get('VideoUrls')
        if m.get('IdCardInfo') is not None:
            temp_model = DescribeVerifyResultResponseBodyMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(m['IdCardInfo'])
        return self


class DescribeVerifyResultResponseBody(TeaModel):
    def __init__(self, authority_comparision_score=None, verify_status=None, request_id=None,
                 face_comparison_score=None, id_card_face_comparison_score=None, material=None):
        self.authority_comparision_score = authority_comparision_score  # type: float
        self.verify_status = verify_status  # type: int
        self.request_id = request_id  # type: str
        self.face_comparison_score = face_comparison_score  # type: float
        self.id_card_face_comparison_score = id_card_face_comparison_score  # type: float
        self.material = material  # type: DescribeVerifyResultResponseBodyMaterial

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
        if self.verify_status is not None:
            result['VerifyStatus'] = self.verify_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.face_comparison_score is not None:
            result['FaceComparisonScore'] = self.face_comparison_score
        if self.id_card_face_comparison_score is not None:
            result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.material is not None:
            result['Material'] = self.material.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorityComparisionScore') is not None:
            self.authority_comparision_score = m.get('AuthorityComparisionScore')
        if m.get('VerifyStatus') is not None:
            self.verify_status = m.get('VerifyStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FaceComparisonScore') is not None:
            self.face_comparison_score = m.get('FaceComparisonScore')
        if m.get('IdCardFaceComparisonScore') is not None:
            self.id_card_face_comparison_score = m.get('IdCardFaceComparisonScore')
        if m.get('Material') is not None:
            temp_model = DescribeVerifyResultResponseBodyMaterial()
            self.material = temp_model.from_map(m['Material'])
        return self


class DescribeVerifyResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVerifyResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVerifyResultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVerifyResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompareFacesRequest(TeaModel):
    def __init__(self, target_image_type=None, source_image_type=None, source_image_value=None,
                 target_image_value=None):
        self.target_image_type = target_image_type  # type: str
        self.source_image_type = source_image_type  # type: str
        self.source_image_value = source_image_value  # type: str
        self.target_image_value = target_image_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompareFacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_image_type is not None:
            result['TargetImageType'] = self.target_image_type
        if self.source_image_type is not None:
            result['SourceImageType'] = self.source_image_type
        if self.source_image_value is not None:
            result['SourceImageValue'] = self.source_image_value
        if self.target_image_value is not None:
            result['TargetImageValue'] = self.target_image_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TargetImageType') is not None:
            self.target_image_type = m.get('TargetImageType')
        if m.get('SourceImageType') is not None:
            self.source_image_type = m.get('SourceImageType')
        if m.get('SourceImageValue') is not None:
            self.source_image_value = m.get('SourceImageValue')
        if m.get('TargetImageValue') is not None:
            self.target_image_value = m.get('TargetImageValue')
        return self


class CompareFacesResponseBodyData(TeaModel):
    def __init__(self, similarity_score=None, confidence_thresholds=None):
        self.similarity_score = similarity_score  # type: float
        self.confidence_thresholds = confidence_thresholds  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompareFacesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.similarity_score is not None:
            result['SimilarityScore'] = self.similarity_score
        if self.confidence_thresholds is not None:
            result['ConfidenceThresholds'] = self.confidence_thresholds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SimilarityScore') is not None:
            self.similarity_score = m.get('SimilarityScore')
        if m.get('ConfidenceThresholds') is not None:
            self.confidence_thresholds = m.get('ConfidenceThresholds')
        return self


class CompareFacesResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, data=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.data = data  # type: CompareFacesResponseBodyData

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = CompareFacesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CompareFacesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CompareFacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CompareFacesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CompareFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFaceConfigRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, biz_type=None, biz_name=None):
        self.source_ip = source_ip  # type: str
        self.lang = lang  # type: str
        self.biz_type = biz_type  # type: str
        self.biz_name = biz_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFaceConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        return self


class CreateFaceConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFaceConfigResponseBody, self).to_map()
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


class CreateFaceConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateFaceConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFaceConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFaceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVerifySDKRequest(TeaModel):
    def __init__(self, app_url=None, platform=None):
        self.app_url = app_url  # type: str
        self.platform = platform  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVerifySDKRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_url is not None:
            result['AppUrl'] = self.app_url
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUrl') is not None:
            self.app_url = m.get('AppUrl')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class CreateVerifySDKResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVerifySDKResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVerifySDKResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateVerifySDKResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVerifySDKResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVerifySDKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitDeviceRequest(TeaModel):
    def __init__(self, certify_id=None, outer_order_no=None, channel=None, merchant=None, product_name=None,
                 produce_node=None, biz_data=None, meta_info=None, certify_principal=None, app_version=None, device_token=None,
                 ua_token=None, web_umid_token=None):
        self.certify_id = certify_id  # type: str
        self.outer_order_no = outer_order_no  # type: str
        self.channel = channel  # type: str
        self.merchant = merchant  # type: str
        self.product_name = product_name  # type: str
        self.produce_node = produce_node  # type: str
        self.biz_data = biz_data  # type: str
        self.meta_info = meta_info  # type: str
        self.certify_principal = certify_principal  # type: str
        self.app_version = app_version  # type: str
        self.device_token = device_token  # type: str
        self.ua_token = ua_token  # type: str
        self.web_umid_token = web_umid_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.merchant is not None:
            result['Merchant'] = self.merchant
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.produce_node is not None:
            result['ProduceNode'] = self.produce_node
        if self.biz_data is not None:
            result['BizData'] = self.biz_data
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.certify_principal is not None:
            result['CertifyPrincipal'] = self.certify_principal
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.ua_token is not None:
            result['UaToken'] = self.ua_token
        if self.web_umid_token is not None:
            result['WebUmidToken'] = self.web_umid_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Merchant') is not None:
            self.merchant = m.get('Merchant')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProduceNode') is not None:
            self.produce_node = m.get('ProduceNode')
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('CertifyPrincipal') is not None:
            self.certify_principal = m.get('CertifyPrincipal')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('UaToken') is not None:
            self.ua_token = m.get('UaToken')
        if m.get('WebUmidToken') is not None:
            self.web_umid_token = m.get('WebUmidToken')
        return self


class InitDeviceResponseBodyResultObject(TeaModel):
    def __init__(self, oss_end_point=None, ret_code_sub=None, protocol=None, certify_id=None, ext_params=None,
                 message=None, file_name=None, access_key_id=None, presigned_url=None, security_token=None,
                 file_name_prefix=None, bucket_name=None, access_key_secret=None, ret_message_sub=None, ret_code=None):
        self.oss_end_point = oss_end_point  # type: str
        self.ret_code_sub = ret_code_sub  # type: str
        self.protocol = protocol  # type: str
        self.certify_id = certify_id  # type: str
        self.ext_params = ext_params  # type: str
        self.message = message  # type: str
        self.file_name = file_name  # type: str
        self.access_key_id = access_key_id  # type: str
        self.presigned_url = presigned_url  # type: str
        self.security_token = security_token  # type: str
        self.file_name_prefix = file_name_prefix  # type: str
        self.bucket_name = bucket_name  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.ret_message_sub = ret_message_sub  # type: str
        self.ret_code = ret_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitDeviceResponseBodyResultObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_end_point is not None:
            result['OssEndPoint'] = self.oss_end_point
        if self.ret_code_sub is not None:
            result['RetCodeSub'] = self.ret_code_sub
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.message is not None:
            result['Message'] = self.message
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.presigned_url is not None:
            result['PresignedUrl'] = self.presigned_url
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.file_name_prefix is not None:
            result['FileNamePrefix'] = self.file_name_prefix
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.ret_message_sub is not None:
            result['RetMessageSub'] = self.ret_message_sub
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssEndPoint') is not None:
            self.oss_end_point = m.get('OssEndPoint')
        if m.get('RetCodeSub') is not None:
            self.ret_code_sub = m.get('RetCodeSub')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('PresignedUrl') is not None:
            self.presigned_url = m.get('PresignedUrl')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('FileNamePrefix') is not None:
            self.file_name_prefix = m.get('FileNamePrefix')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('RetMessageSub') is not None:
            self.ret_message_sub = m.get('RetMessageSub')
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        return self


class InitDeviceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, result_object=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result_object = result_object  # type: InitDeviceResponseBodyResultObject

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super(InitDeviceResponseBody, self).to_map()
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
            temp_model = InitDeviceResponseBodyResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class InitDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InitDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitDeviceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InitDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWhitelistSettingRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, service_code=None, scene_id=None, certify_id=None, cert_no=None,
                 valid_day=None):
        self.source_ip = source_ip  # type: str
        self.lang = lang  # type: str
        self.service_code = service_code  # type: str
        self.scene_id = scene_id  # type: long
        self.certify_id = certify_id  # type: str
        self.cert_no = cert_no  # type: str
        self.valid_day = valid_day  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWhitelistSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.valid_day is not None:
            result['ValidDay'] = self.valid_day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('ValidDay') is not None:
            self.valid_day = m.get('ValidDay')
        return self


class CreateWhitelistSettingResponseBody(TeaModel):
    def __init__(self, result_object=None, request_id=None):
        self.result_object = result_object  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWhitelistSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_object is not None:
            result['ResultObject'] = self.result_object
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResultObject') is not None:
            self.result_object = m.get('ResultObject')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWhitelistSettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateWhitelistSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWhitelistSettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateWhitelistSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserStatusResponseBody(TeaModel):
    def __init__(self, enabled=None, request_id=None):
        self.enabled = enabled  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVerifySettingRequest(TeaModel):
    def __init__(self, biz_type=None, biz_name=None, solution=None, guide_step=None, privacy_step=None,
                 result_step=None):
        self.biz_type = biz_type  # type: str
        self.biz_name = biz_name  # type: str
        self.solution = solution  # type: str
        self.guide_step = guide_step  # type: bool
        self.privacy_step = privacy_step  # type: bool
        self.result_step = result_step  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVerifySettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.guide_step is not None:
            result['GuideStep'] = self.guide_step
        if self.privacy_step is not None:
            result['PrivacyStep'] = self.privacy_step
        if self.result_step is not None:
            result['ResultStep'] = self.result_step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('GuideStep') is not None:
            self.guide_step = m.get('GuideStep')
        if m.get('PrivacyStep') is not None:
            self.privacy_step = m.get('PrivacyStep')
        if m.get('ResultStep') is not None:
            self.result_step = m.get('ResultStep')
        return self


class CreateVerifySettingResponseBody(TeaModel):
    def __init__(self, biz_name=None, request_id=None, solution=None, biz_type=None, step_list=None):
        self.biz_name = biz_name  # type: str
        self.request_id = request_id  # type: str
        self.solution = solution  # type: str
        self.biz_type = biz_type  # type: str
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.step_list is not None:
            result['StepList'] = self.step_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('StepList') is not None:
            self.step_list = m.get('StepList')
        return self


class CreateVerifySettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateVerifySettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVerifySettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVerifySettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitFaceVerifyRequest(TeaModel):
    def __init__(self, scene_id=None, outer_order_no=None, product_code=None, cert_type=None, cert_name=None,
                 cert_no=None, return_url=None, face_contrast_picture=None, meta_info=None, mobile=None, ip=None,
                 user_id=None, face_contrast_picture_url=None, certify_id=None, oss_bucket_name=None, oss_object_name=None,
                 model=None, callback_url=None, callback_token=None, crop=None):
        self.scene_id = scene_id  # type: long
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.cert_type = cert_type  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_no = cert_no  # type: str
        self.return_url = return_url  # type: str
        self.face_contrast_picture = face_contrast_picture  # type: str
        self.meta_info = meta_info  # type: str
        self.mobile = mobile  # type: str
        self.ip = ip  # type: str
        self.user_id = user_id  # type: str
        self.face_contrast_picture_url = face_contrast_picture_url  # type: str
        self.certify_id = certify_id  # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.model = model  # type: str
        self.callback_url = callback_url  # type: str
        self.callback_token = callback_token  # type: str
        self.crop = crop  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitFaceVerifyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.model is not None:
            result['Model'] = self.model
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token
        if self.crop is not None:
            result['Crop'] = self.crop
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InitFaceVerifyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitFaceVerifyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InitFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


