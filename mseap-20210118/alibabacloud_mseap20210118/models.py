# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class ActivateLicenseRequest(TeaModel):
    def __init__(self, biz_type=None, license_publisher=None, license_code=None):
        self.biz_type = TeaConverter.to_unicode(biz_type)  # type: unicode
        self.license_publisher = TeaConverter.to_unicode(license_publisher)  # type: unicode
        self.license_code = TeaConverter.to_unicode(license_code)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.license_publisher is not None:
            result['LicensePublisher'] = self.license_publisher
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('LicensePublisher') is not None:
            self.license_publisher = m.get('LicensePublisher')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        return self


class ActivateLicenseResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ActivateLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ActivateLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ActivateLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BusinessLicenseOcrRequest(TeaModel):
    def __init__(self, lang=None, biz_code=None, file_info=None, file_store_type=None):
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.biz_code = TeaConverter.to_unicode(biz_code)  # type: unicode
        self.file_info = TeaConverter.to_unicode(file_info)  # type: unicode
        self.file_store_type = TeaConverter.to_unicode(file_store_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.file_info is not None:
            result['FileInfo'] = self.file_info
        if self.file_store_type is not None:
            result['FileStoreType'] = self.file_store_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('FileInfo') is not None:
            self.file_info = m.get('FileInfo')
        if m.get('FileStoreType') is not None:
            self.file_store_type = m.get('FileStoreType')
        return self


class BusinessLicenseOcrResponseBody(TeaModel):
    def __init__(self, register_number=None, type=None, valid_period=None, request_id=None, address=None,
                 capital=None, legal_person=None, establish_date=None, nationality=None, name=None, business=None,
                 track_id=None):
        self.register_number = TeaConverter.to_unicode(register_number)  # type: unicode
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.valid_period = TeaConverter.to_unicode(valid_period)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.address = TeaConverter.to_unicode(address)  # type: unicode
        self.capital = TeaConverter.to_unicode(capital)  # type: unicode
        self.legal_person = TeaConverter.to_unicode(legal_person)  # type: unicode
        self.establish_date = TeaConverter.to_unicode(establish_date)  # type: unicode
        self.nationality = TeaConverter.to_unicode(nationality)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.business = TeaConverter.to_unicode(business)  # type: unicode
        self.track_id = TeaConverter.to_unicode(track_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.type is not None:
            result['Type'] = self.type
        if self.valid_period is not None:
            result['ValidPeriod'] = self.valid_period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.address is not None:
            result['Address'] = self.address
        if self.capital is not None:
            result['Capital'] = self.capital
        if self.legal_person is not None:
            result['LegalPerson'] = self.legal_person
        if self.establish_date is not None:
            result['EstablishDate'] = self.establish_date
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.name is not None:
            result['Name'] = self.name
        if self.business is not None:
            result['Business'] = self.business
        if self.track_id is not None:
            result['TrackId'] = self.track_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ValidPeriod') is not None:
            self.valid_period = m.get('ValidPeriod')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Capital') is not None:
            self.capital = m.get('Capital')
        if m.get('LegalPerson') is not None:
            self.legal_person = m.get('LegalPerson')
        if m.get('EstablishDate') is not None:
            self.establish_date = m.get('EstablishDate')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('TrackId') is not None:
            self.track_id = m.get('TrackId')
        return self


class BusinessLicenseOcrResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: BusinessLicenseOcrResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = BusinessLicenseOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CertificateQualityRequest(TeaModel):
    def __init__(self, lang=None, biz_code=None, file_info=None, file_store_type=None, certificate_type=None):
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.biz_code = TeaConverter.to_unicode(biz_code)  # type: unicode
        self.file_info = TeaConverter.to_unicode(file_info)  # type: unicode
        self.file_store_type = TeaConverter.to_unicode(file_store_type)  # type: unicode
        self.certificate_type = TeaConverter.to_unicode(certificate_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.file_info is not None:
            result['FileInfo'] = self.file_info
        if self.file_store_type is not None:
            result['FileStoreType'] = self.file_store_type
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('FileInfo') is not None:
            self.file_info = m.get('FileInfo')
        if m.get('FileStoreType') is not None:
            self.file_store_type = m.get('FileStoreType')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        return self


class CertificateQualityResponseBody(TeaModel):
    def __init__(self, contain_seal=None, contain_watermark=None, request_id=None, copy=None, complete=None,
                 national_emblem=None, target_type=None, reflection=None, electronic=None, contain_front=None, text_clarity=None):
        self.contain_seal = TeaConverter.to_unicode(contain_seal)  # type: unicode
        self.contain_watermark = TeaConverter.to_unicode(contain_watermark)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.copy = TeaConverter.to_unicode(copy)  # type: unicode
        self.complete = TeaConverter.to_unicode(complete)  # type: unicode
        self.national_emblem = TeaConverter.to_unicode(national_emblem)  # type: unicode
        self.target_type = TeaConverter.to_unicode(target_type)  # type: unicode
        self.reflection = TeaConverter.to_unicode(reflection)  # type: unicode
        self.electronic = TeaConverter.to_unicode(electronic)  # type: unicode
        self.contain_front = TeaConverter.to_unicode(contain_front)  # type: unicode
        self.text_clarity = TeaConverter.to_unicode(text_clarity)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.contain_seal is not None:
            result['ContainSeal'] = self.contain_seal
        if self.contain_watermark is not None:
            result['ContainWatermark'] = self.contain_watermark
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.copy is not None:
            result['Copy'] = self.copy
        if self.complete is not None:
            result['Complete'] = self.complete
        if self.national_emblem is not None:
            result['NationalEmblem'] = self.national_emblem
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.reflection is not None:
            result['Reflection'] = self.reflection
        if self.electronic is not None:
            result['Electronic'] = self.electronic
        if self.contain_front is not None:
            result['ContainFront'] = self.contain_front
        if self.text_clarity is not None:
            result['TextClarity'] = self.text_clarity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainSeal') is not None:
            self.contain_seal = m.get('ContainSeal')
        if m.get('ContainWatermark') is not None:
            self.contain_watermark = m.get('ContainWatermark')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Copy') is not None:
            self.copy = m.get('Copy')
        if m.get('Complete') is not None:
            self.complete = m.get('Complete')
        if m.get('NationalEmblem') is not None:
            self.national_emblem = m.get('NationalEmblem')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('Reflection') is not None:
            self.reflection = m.get('Reflection')
        if m.get('Electronic') is not None:
            self.electronic = m.get('Electronic')
        if m.get('ContainFront') is not None:
            self.contain_front = m.get('ContainFront')
        if m.get('TextClarity') is not None:
            self.text_clarity = m.get('TextClarity')
        return self


class CertificateQualityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CertificateQualityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CertificateQualityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAgreementStatusRequest(TeaModel):
    def __init__(self, agreement_code=None):
        self.agreement_code = TeaConverter.to_unicode(agreement_code)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.agreement_code is not None:
            result['AgreementCode'] = self.agreement_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgreementCode') is not None:
            self.agreement_code = m.get('AgreementCode')
        return self


class DescribeAgreementStatusResponseBody(TeaModel):
    def __init__(self, status=None, request_id=None, user_id=None, agreement_code=None):
        self.status = status  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.user_id = TeaConverter.to_unicode(user_id)  # type: unicode
        self.agreement_code = TeaConverter.to_unicode(agreement_code)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.agreement_code is not None:
            result['AgreementCode'] = self.agreement_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('AgreementCode') is not None:
            self.agreement_code = m.get('AgreementCode')
        return self


class DescribeAgreementStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAgreementStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeAgreementStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IdentityCardOcrRequest(TeaModel):
    def __init__(self, lang=None, biz_code=None, file_info=None, file_store_type=None):
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.biz_code = TeaConverter.to_unicode(biz_code)  # type: unicode
        self.file_info = TeaConverter.to_unicode(file_info)  # type: unicode
        self.file_store_type = TeaConverter.to_unicode(file_store_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.file_info is not None:
            result['FileInfo'] = self.file_info
        if self.file_store_type is not None:
            result['FileStoreType'] = self.file_store_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('FileInfo') is not None:
            self.file_info = m.get('FileInfo')
        if m.get('FileStoreType') is not None:
            self.file_store_type = m.get('FileStoreType')
        return self


class IdentityCardOcrResponseBody(TeaModel):
    def __init__(self, issue=None, valid_date=None, request_id=None, address=None, id_number=None, gender=None,
                 nationality=None, birth_date=None, track_id=None, name=None):
        self.issue = TeaConverter.to_unicode(issue)  # type: unicode
        self.valid_date = TeaConverter.to_unicode(valid_date)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.address = TeaConverter.to_unicode(address)  # type: unicode
        self.id_number = TeaConverter.to_unicode(id_number)  # type: unicode
        self.gender = TeaConverter.to_unicode(gender)  # type: unicode
        self.nationality = TeaConverter.to_unicode(nationality)  # type: unicode
        self.birth_date = TeaConverter.to_unicode(birth_date)  # type: unicode
        self.track_id = TeaConverter.to_unicode(track_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.issue is not None:
            result['Issue'] = self.issue
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.address is not None:
            result['Address'] = self.address
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.birth_date is not None:
            result['BirthDate'] = self.birth_date
        if self.track_id is not None:
            result['TrackId'] = self.track_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Issue') is not None:
            self.issue = m.get('Issue')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('BirthDate') is not None:
            self.birth_date = m.get('BirthDate')
        if m.get('TrackId') is not None:
            self.track_id = m.get('TrackId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class IdentityCardOcrResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: IdentityCardOcrResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = IdentityCardOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAgreementStatusRequest(TeaModel):
    def __init__(self, agreement_code=None):
        self.agreement_code = TeaConverter.to_unicode(agreement_code)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.agreement_code is not None:
            result['AgreementCode'] = self.agreement_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgreementCode') is not None:
            self.agreement_code = m.get('AgreementCode')
        return self


class UpdateAgreementStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAgreementStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateAgreementStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateAgreementStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


