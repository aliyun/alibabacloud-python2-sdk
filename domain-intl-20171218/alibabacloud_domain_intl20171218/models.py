# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AcknowledgeTaskResultRequest(TeaModel):
    def __init__(self, lang=None, task_detail_no=None, user_client_ip=None):
        self.lang = lang  # type: str
        self.task_detail_no = task_detail_no  # type: list[str]
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcknowledgeTaskResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class AcknowledgeTaskResultResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcknowledgeTaskResultResponseBody, self).to_map()
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


class AcknowledgeTaskResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AcknowledgeTaskResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AcknowledgeTaskResultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AcknowledgeTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchFuzzyMatchDomainSensitiveWordRequest(TeaModel):
    def __init__(self, keyword=None, lang=None, user_client_ip=None):
        self.keyword = keyword  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchFuzzyMatchDomainSensitiveWordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWordsMatchedSensitiveWord(TeaModel):
    def __init__(self, word=None):
        self.word = word  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWordsMatchedSensitiveWord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWords(TeaModel):
    def __init__(self, matched_sensitive_word=None):
        self.matched_sensitive_word = matched_sensitive_word  # type: list[BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWordsMatchedSensitiveWord]

    def validate(self):
        if self.matched_sensitive_word:
            for k in self.matched_sensitive_word:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MatchedSensitiveWord'] = []
        if self.matched_sensitive_word is not None:
            for k in self.matched_sensitive_word:
                result['MatchedSensitiveWord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.matched_sensitive_word = []
        if m.get('MatchedSensitiveWord') is not None:
            for k in m.get('MatchedSensitiveWord'):
                temp_model = BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWordsMatchedSensitiveWord()
                self.matched_sensitive_word.append(temp_model.from_map(k))
        return self


class BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResult(TeaModel):
    def __init__(self, exist=None, keyword=None, matched_sentive_words=None):
        self.exist = exist  # type: bool
        self.keyword = keyword  # type: str
        self.matched_sentive_words = matched_sentive_words  # type: BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWords

    def validate(self):
        if self.matched_sentive_words:
            self.matched_sentive_words.validate()

    def to_map(self):
        _map = super(BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist is not None:
            result['Exist'] = self.exist
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.matched_sentive_words is not None:
            result['MatchedSentiveWords'] = self.matched_sentive_words.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Exist') is not None:
            self.exist = m.get('Exist')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MatchedSentiveWords') is not None:
            temp_model = BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResultMatchedSentiveWords()
            self.matched_sentive_words = temp_model.from_map(m['MatchedSentiveWords'])
        return self


class BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultList(TeaModel):
    def __init__(self, sensitive_word_match_result=None):
        self.sensitive_word_match_result = sensitive_word_match_result  # type: list[BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResult]

    def validate(self):
        if self.sensitive_word_match_result:
            for k in self.sensitive_word_match_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SensitiveWordMatchResult'] = []
        if self.sensitive_word_match_result is not None:
            for k in self.sensitive_word_match_result:
                result['SensitiveWordMatchResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sensitive_word_match_result = []
        if m.get('SensitiveWordMatchResult') is not None:
            for k in m.get('SensitiveWordMatchResult'):
                temp_model = BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultListSensitiveWordMatchResult()
                self.sensitive_word_match_result.append(temp_model.from_map(k))
        return self


class BatchFuzzyMatchDomainSensitiveWordResponseBody(TeaModel):
    def __init__(self, request_id=None, sensitive_word_match_result_list=None):
        self.request_id = request_id  # type: str
        self.sensitive_word_match_result_list = sensitive_word_match_result_list  # type: BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultList

    def validate(self):
        if self.sensitive_word_match_result_list:
            self.sensitive_word_match_result_list.validate()

    def to_map(self):
        _map = super(BatchFuzzyMatchDomainSensitiveWordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sensitive_word_match_result_list is not None:
            result['SensitiveWordMatchResultList'] = self.sensitive_word_match_result_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SensitiveWordMatchResultList') is not None:
            temp_model = BatchFuzzyMatchDomainSensitiveWordResponseBodySensitiveWordMatchResultList()
            self.sensitive_word_match_result_list = temp_model.from_map(m['SensitiveWordMatchResultList'])
        return self


class BatchFuzzyMatchDomainSensitiveWordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchFuzzyMatchDomainSensitiveWordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchFuzzyMatchDomainSensitiveWordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchFuzzyMatchDomainSensitiveWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelDomainVerificationRequest(TeaModel):
    def __init__(self, action_type=None, instance_id=None, lang=None, user_client_ip=None):
        self.action_type = action_type  # type: str
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelDomainVerificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class CancelDomainVerificationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelDomainVerificationResponseBody, self).to_map()
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


class CancelDomainVerificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelDomainVerificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelDomainVerificationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelDomainVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelTaskRequest(TeaModel):
    def __init__(self, lang=None, task_no=None, user_client_ip=None):
        self.lang = lang  # type: str
        self.task_no = task_no  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class CancelTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelTaskResponseBody, self).to_map()
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


class CancelTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDomainRequest(TeaModel):
    def __init__(self, domain_name=None, fee_command=None, fee_currency=None, fee_period=None, lang=None,
                 user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.fee_command = fee_command  # type: str
        self.fee_currency = fee_currency  # type: str
        self.fee_period = fee_period  # type: int
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.fee_command is not None:
            result['FeeCommand'] = self.fee_command
        if self.fee_currency is not None:
            result['FeeCurrency'] = self.fee_currency
        if self.fee_period is not None:
            result['FeePeriod'] = self.fee_period
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FeeCommand') is not None:
            self.fee_command = m.get('FeeCommand')
        if m.get('FeeCurrency') is not None:
            self.fee_currency = m.get('FeeCurrency')
        if m.get('FeePeriod') is not None:
            self.fee_period = m.get('FeePeriod')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class CheckDomainResponseBody(TeaModel):
    def __init__(self, avail=None, domain_name=None, dynamic_check=None, premium=None, price=None, reason=None,
                 request_id=None):
        self.avail = avail  # type: str
        self.domain_name = domain_name  # type: str
        self.dynamic_check = dynamic_check  # type: bool
        self.premium = premium  # type: str
        self.price = price  # type: long
        self.reason = reason  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avail is not None:
            result['Avail'] = self.avail
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.dynamic_check is not None:
            result['DynamicCheck'] = self.dynamic_check
        if self.premium is not None:
            result['Premium'] = self.premium
        if self.price is not None:
            result['Price'] = self.price
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Avail') is not None:
            self.avail = m.get('Avail')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DynamicCheck') is not None:
            self.dynamic_check = m.get('DynamicCheck')
        if m.get('Premium') is not None:
            self.premium = m.get('Premium')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDomainSunriseClaimRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDomainSunriseClaimRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class CheckDomainSunriseClaimResponseBody(TeaModel):
    def __init__(self, claim_key=None, request_id=None, result=None):
        self.claim_key = claim_key  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckDomainSunriseClaimResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claim_key is not None:
            result['ClaimKey'] = self.claim_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClaimKey') is not None:
            self.claim_key = m.get('ClaimKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CheckDomainSunriseClaimResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckDomainSunriseClaimResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckDomainSunriseClaimResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckDomainSunriseClaimResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckTransferInFeasibilityRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, transfer_authorization_code=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.transfer_authorization_code = transfer_authorization_code  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckTransferInFeasibilityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.transfer_authorization_code is not None:
            result['TransferAuthorizationCode'] = self.transfer_authorization_code
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TransferAuthorizationCode') is not None:
            self.transfer_authorization_code = m.get('TransferAuthorizationCode')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class CheckTransferInFeasibilityResponseBody(TeaModel):
    def __init__(self, can_transfer=None, code=None, message=None, product_id=None, request_id=None):
        self.can_transfer = can_transfer  # type: bool
        self.code = code  # type: str
        self.message = message  # type: str
        self.product_id = product_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckTransferInFeasibilityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_transfer is not None:
            result['CanTransfer'] = self.can_transfer
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanTransfer') is not None:
            self.can_transfer = m.get('CanTransfer')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckTransferInFeasibilityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckTransferInFeasibilityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckTransferInFeasibilityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckTransferInFeasibilityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmTransferInEmailRequest(TeaModel):
    def __init__(self, domain_name=None, email=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: list[str]
        self.email = email  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmTransferInEmailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class ConfirmTransferInEmailResponseBodyFailList(TeaModel):
    def __init__(self, fail_domain=None):
        self.fail_domain = fail_domain  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmTransferInEmailResponseBodyFailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_domain is not None:
            result['FailDomain'] = self.fail_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailDomain') is not None:
            self.fail_domain = m.get('FailDomain')
        return self


class ConfirmTransferInEmailResponseBodySuccessList(TeaModel):
    def __init__(self, success_domain=None):
        self.success_domain = success_domain  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmTransferInEmailResponseBodySuccessList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success_domain is not None:
            result['SuccessDomain'] = self.success_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SuccessDomain') is not None:
            self.success_domain = m.get('SuccessDomain')
        return self


class ConfirmTransferInEmailResponseBody(TeaModel):
    def __init__(self, fail_list=None, request_id=None, success_list=None):
        self.fail_list = fail_list  # type: ConfirmTransferInEmailResponseBodyFailList
        self.request_id = request_id  # type: str
        self.success_list = success_list  # type: ConfirmTransferInEmailResponseBodySuccessList

    def validate(self):
        if self.fail_list:
            self.fail_list.validate()
        if self.success_list:
            self.success_list.validate()

    def to_map(self):
        _map = super(ConfirmTransferInEmailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_list is not None:
            result['FailList'] = self.fail_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_list is not None:
            result['SuccessList'] = self.success_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailList') is not None:
            temp_model = ConfirmTransferInEmailResponseBodyFailList()
            self.fail_list = temp_model.from_map(m['FailList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessList') is not None:
            temp_model = ConfirmTransferInEmailResponseBodySuccessList()
            self.success_list = temp_model.from_map(m['SuccessList'])
        return self


class ConfirmTransferInEmailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfirmTransferInEmailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfirmTransferInEmailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ConfirmTransferInEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEmailVerificationRequest(TeaModel):
    def __init__(self, email=None, lang=None, user_client_ip=None):
        self.email = email  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEmailVerificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DeleteEmailVerificationResponseBodyFailList(TeaModel):
    def __init__(self, code=None, email=None, message=None):
        self.code = code  # type: str
        self.email = email  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEmailVerificationResponseBodyFailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.email is not None:
            result['Email'] = self.email
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteEmailVerificationResponseBodySuccessList(TeaModel):
    def __init__(self, code=None, email=None, message=None):
        self.code = code  # type: str
        self.email = email  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEmailVerificationResponseBodySuccessList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.email is not None:
            result['Email'] = self.email
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteEmailVerificationResponseBody(TeaModel):
    def __init__(self, fail_list=None, request_id=None, success_list=None):
        self.fail_list = fail_list  # type: list[DeleteEmailVerificationResponseBodyFailList]
        self.request_id = request_id  # type: str
        self.success_list = success_list  # type: list[DeleteEmailVerificationResponseBodySuccessList]

    def validate(self):
        if self.fail_list:
            for k in self.fail_list:
                if k:
                    k.validate()
        if self.success_list:
            for k in self.success_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DeleteEmailVerificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailList'] = []
        if self.fail_list is not None:
            for k in self.fail_list:
                result['FailList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SuccessList'] = []
        if self.success_list is not None:
            for k in self.success_list:
                result['SuccessList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.fail_list = []
        if m.get('FailList') is not None:
            for k in m.get('FailList'):
                temp_model = DeleteEmailVerificationResponseBodyFailList()
                self.fail_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.success_list = []
        if m.get('SuccessList') is not None:
            for k in m.get('SuccessList'):
                temp_model = DeleteEmailVerificationResponseBodySuccessList()
                self.success_list.append(temp_model.from_map(k))
        return self


class DeleteEmailVerificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEmailVerificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEmailVerificationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEmailVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRegistrantProfileRequest(TeaModel):
    def __init__(self, lang=None, registrant_profile_id=None, user_client_ip=None):
        self.lang = lang  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRegistrantProfileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DeleteRegistrantProfileResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRegistrantProfileResponseBody, self).to_map()
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


class DeleteRegistrantProfileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRegistrantProfileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRegistrantProfileResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRegistrantProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EmailVerifiedRequest(TeaModel):
    def __init__(self, email=None, lang=None, user_client_ip=None):
        self.email = email  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EmailVerifiedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class EmailVerifiedResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EmailVerifiedResponseBody, self).to_map()
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


class EmailVerifiedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EmailVerifiedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EmailVerifiedResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EmailVerifiedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FuzzyMatchDomainSensitiveWordRequest(TeaModel):
    def __init__(self, keyword=None, lang=None, user_client_ip=None):
        self.keyword = keyword  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FuzzyMatchDomainSensitiveWordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWordsMatchedSensitiveWord(TeaModel):
    def __init__(self, word=None):
        self.word = word  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWordsMatchedSensitiveWord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWords(TeaModel):
    def __init__(self, matched_sensitive_word=None):
        self.matched_sensitive_word = matched_sensitive_word  # type: list[FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWordsMatchedSensitiveWord]

    def validate(self):
        if self.matched_sensitive_word:
            for k in self.matched_sensitive_word:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MatchedSensitiveWord'] = []
        if self.matched_sensitive_word is not None:
            for k in self.matched_sensitive_word:
                result['MatchedSensitiveWord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.matched_sensitive_word = []
        if m.get('MatchedSensitiveWord') is not None:
            for k in m.get('MatchedSensitiveWord'):
                temp_model = FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWordsMatchedSensitiveWord()
                self.matched_sensitive_word.append(temp_model.from_map(k))
        return self


class FuzzyMatchDomainSensitiveWordResponseBody(TeaModel):
    def __init__(self, exist=None, keyword=None, matched_sentive_words=None, request_id=None):
        self.exist = exist  # type: bool
        self.keyword = keyword  # type: str
        self.matched_sentive_words = matched_sentive_words  # type: FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWords
        self.request_id = request_id  # type: str

    def validate(self):
        if self.matched_sentive_words:
            self.matched_sentive_words.validate()

    def to_map(self):
        _map = super(FuzzyMatchDomainSensitiveWordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist is not None:
            result['Exist'] = self.exist
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.matched_sentive_words is not None:
            result['MatchedSentiveWords'] = self.matched_sentive_words.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Exist') is not None:
            self.exist = m.get('Exist')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MatchedSentiveWords') is not None:
            temp_model = FuzzyMatchDomainSensitiveWordResponseBodyMatchedSentiveWords()
            self.matched_sentive_words = temp_model.from_map(m['MatchedSentiveWords'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FuzzyMatchDomainSensitiveWordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FuzzyMatchDomainSensitiveWordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FuzzyMatchDomainSensitiveWordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FuzzyMatchDomainSensitiveWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEmailVerificationRequest(TeaModel):
    def __init__(self, begin_create_time=None, email=None, end_create_time=None, lang=None, page_num=None,
                 page_size=None, user_client_ip=None, verification_status=None):
        self.begin_create_time = begin_create_time  # type: long
        self.email = email  # type: str
        self.end_create_time = end_create_time  # type: long
        self.lang = lang  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.user_client_ip = user_client_ip  # type: str
        self.verification_status = verification_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEmailVerificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_create_time is not None:
            result['BeginCreateTime'] = self.begin_create_time
        if self.email is not None:
            result['Email'] = self.email
        if self.end_create_time is not None:
            result['EndCreateTime'] = self.end_create_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginCreateTime') is not None:
            self.begin_create_time = m.get('BeginCreateTime')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndCreateTime') is not None:
            self.end_create_time = m.get('EndCreateTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class ListEmailVerificationResponseBodyData(TeaModel):
    def __init__(self, confirm_ip=None, email=None, email_verification_no=None, gmt_create=None, gmt_modified=None,
                 send_ip=None, token_send_time=None, user_id=None, verification_status=None, verification_time=None):
        self.confirm_ip = confirm_ip  # type: str
        self.email = email  # type: str
        self.email_verification_no = email_verification_no  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.send_ip = send_ip  # type: str
        self.token_send_time = token_send_time  # type: str
        self.user_id = user_id  # type: str
        self.verification_status = verification_status  # type: int
        self.verification_time = verification_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEmailVerificationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confirm_ip is not None:
            result['ConfirmIp'] = self.confirm_ip
        if self.email is not None:
            result['Email'] = self.email
        if self.email_verification_no is not None:
            result['EmailVerificationNo'] = self.email_verification_no
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.send_ip is not None:
            result['SendIp'] = self.send_ip
        if self.token_send_time is not None:
            result['TokenSendTime'] = self.token_send_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.verification_time is not None:
            result['VerificationTime'] = self.verification_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfirmIp') is not None:
            self.confirm_ip = m.get('ConfirmIp')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EmailVerificationNo') is not None:
            self.email_verification_no = m.get('EmailVerificationNo')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('SendIp') is not None:
            self.send_ip = m.get('SendIp')
        if m.get('TokenSendTime') is not None:
            self.token_send_time = m.get('TokenSendTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('VerificationTime') is not None:
            self.verification_time = m.get('VerificationTime')
        return self


class ListEmailVerificationResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, next_page=None, page_size=None, pre_page=None,
                 request_id=None, total_item_num=None, total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: list[ListEmailVerificationResponseBodyData]
        self.next_page = next_page  # type: bool
        self.page_size = page_size  # type: int
        self.pre_page = pre_page  # type: bool
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEmailVerificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
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
                temp_model = ListEmailVerificationResponseBodyData()
                self.data.append(temp_model.from_map(k))
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


class ListEmailVerificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEmailVerificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEmailVerificationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEmailVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LookupTmchNoticeRequest(TeaModel):
    def __init__(self, claim_key=None, lang=None, user_client_ip=None):
        self.claim_key = claim_key  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LookupTmchNoticeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claim_key is not None:
            result['ClaimKey'] = self.claim_key
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClaimKey') is not None:
            self.claim_key = m.get('ClaimKey')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class LookupTmchNoticeResponseBodyClaimsClaimClassDescsClassDesc(TeaModel):
    def __init__(self, class_num=None, desc=None):
        self.class_num = class_num  # type: int
        self.desc = desc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LookupTmchNoticeResponseBodyClaimsClaimClassDescsClassDesc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_num is not None:
            result['ClassNum'] = self.class_num
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassNum') is not None:
            self.class_num = m.get('ClassNum')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class LookupTmchNoticeResponseBodyClaimsClaimClassDescs(TeaModel):
    def __init__(self, class_desc=None):
        self.class_desc = class_desc  # type: list[LookupTmchNoticeResponseBodyClaimsClaimClassDescsClassDesc]

    def validate(self):
        if self.class_desc:
            for k in self.class_desc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(LookupTmchNoticeResponseBodyClaimsClaimClassDescs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClassDesc'] = []
        if self.class_desc is not None:
            for k in self.class_desc:
                result['ClassDesc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.class_desc = []
        if m.get('ClassDesc') is not None:
            for k in m.get('ClassDesc'):
                temp_model = LookupTmchNoticeResponseBodyClaimsClaimClassDescsClassDesc()
                self.class_desc.append(temp_model.from_map(k))
        return self


class LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddrStreet(TeaModel):
    def __init__(self, street=None):
        self.street = street  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddrStreet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.street is not None:
            result['Street'] = self.street
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Street') is not None:
            self.street = m.get('Street')
        return self


class LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddr(TeaModel):
    def __init__(self, cc=None, city=None, pc=None, sp=None, street=None):
        self.cc = cc  # type: str
        self.city = city  # type: str
        self.pc = pc  # type: str
        self.sp = sp  # type: str
        self.street = street  # type: LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddrStreet

    def validate(self):
        if self.street:
            self.street.validate()

    def to_map(self):
        _map = super(LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddr, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cc is not None:
            result['Cc'] = self.cc
        if self.city is not None:
            result['City'] = self.city
        if self.pc is not None:
            result['Pc'] = self.pc
        if self.sp is not None:
            result['Sp'] = self.sp
        if self.street is not None:
            result['Street'] = self.street.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cc') is not None:
            self.cc = m.get('Cc')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Pc') is not None:
            self.pc = m.get('Pc')
        if m.get('Sp') is not None:
            self.sp = m.get('Sp')
        if m.get('Street') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddrStreet()
            self.street = temp_model.from_map(m['Street'])
        return self


class LookupTmchNoticeResponseBodyClaimsClaimContactsContact(TeaModel):
    def __init__(self, addr=None, email=None, fax=None, name=None, org=None, type=None, voice=None):
        self.addr = addr  # type: LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddr
        self.email = email  # type: str
        self.fax = fax  # type: str
        self.name = name  # type: str
        self.org = org  # type: str
        self.type = type  # type: str
        self.voice = voice  # type: str

    def validate(self):
        if self.addr:
            self.addr.validate()

    def to_map(self):
        _map = super(LookupTmchNoticeResponseBodyClaimsClaimContactsContact, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addr is not None:
            result['Addr'] = self.addr.to_map()
        if self.email is not None:
            result['Email'] = self.email
        if self.fax is not None:
            result['Fax'] = self.fax
        if self.name is not None:
            result['Name'] = self.name
        if self.org is not None:
            result['Org'] = self.org
        if self.type is not None:
            result['Type'] = self.type
        if self.voice is not None:
            result['Voice'] = self.voice
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addr') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimContactsContactAddr()
            self.addr = temp_model.from_map(m['Addr'])
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Fax') is not None:
            self.fax = m.get('Fax')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Org') is not None:
            self.org = m.get('Org')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        return self


class LookupTmchNoticeResponseBodyClaimsClaimContacts(TeaModel):
    def __init__(self, contact=None):
        self.contact = contact  # type: list[LookupTmchNoticeResponseBodyClaimsClaimContactsContact]

    def validate(self):
        if self.contact:
            for k in self.contact:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(LookupTmchNoticeResponseBodyClaimsClaimContacts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contact'] = []
        if self.contact is not None:
            for k in self.contact:
                result['Contact'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.contact = []
        if m.get('Contact') is not None:
            for k in m.get('Contact'):
                temp_model = LookupTmchNoticeResponseBodyClaimsClaimContactsContact()
                self.contact.append(temp_model.from_map(k))
        return self


class LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddrStreet(TeaModel):
    def __init__(self, street=None):
        self.street = street  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddrStreet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.street is not None:
            result['Street'] = self.street
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Street') is not None:
            self.street = m.get('Street')
        return self


class LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddr(TeaModel):
    def __init__(self, cc=None, city=None, pc=None, sp=None, street=None):
        self.cc = cc  # type: str
        self.city = city  # type: str
        self.pc = pc  # type: str
        self.sp = sp  # type: str
        self.street = street  # type: LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddrStreet

    def validate(self):
        if self.street:
            self.street.validate()

    def to_map(self):
        _map = super(LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddr, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cc is not None:
            result['Cc'] = self.cc
        if self.city is not None:
            result['City'] = self.city
        if self.pc is not None:
            result['Pc'] = self.pc
        if self.sp is not None:
            result['Sp'] = self.sp
        if self.street is not None:
            result['Street'] = self.street.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cc') is not None:
            self.cc = m.get('Cc')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Pc') is not None:
            self.pc = m.get('Pc')
        if m.get('Sp') is not None:
            self.sp = m.get('Sp')
        if m.get('Street') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddrStreet()
            self.street = temp_model.from_map(m['Street'])
        return self


class LookupTmchNoticeResponseBodyClaimsClaimHoldersHolder(TeaModel):
    def __init__(self, addr=None, entitlement=None, org=None):
        self.addr = addr  # type: LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddr
        self.entitlement = entitlement  # type: str
        self.org = org  # type: str

    def validate(self):
        if self.addr:
            self.addr.validate()

    def to_map(self):
        _map = super(LookupTmchNoticeResponseBodyClaimsClaimHoldersHolder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addr is not None:
            result['Addr'] = self.addr.to_map()
        if self.entitlement is not None:
            result['Entitlement'] = self.entitlement
        if self.org is not None:
            result['Org'] = self.org
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addr') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimHoldersHolderAddr()
            self.addr = temp_model.from_map(m['Addr'])
        if m.get('Entitlement') is not None:
            self.entitlement = m.get('Entitlement')
        if m.get('Org') is not None:
            self.org = m.get('Org')
        return self


class LookupTmchNoticeResponseBodyClaimsClaimHolders(TeaModel):
    def __init__(self, holder=None):
        self.holder = holder  # type: list[LookupTmchNoticeResponseBodyClaimsClaimHoldersHolder]

    def validate(self):
        if self.holder:
            for k in self.holder:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(LookupTmchNoticeResponseBodyClaimsClaimHolders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Holder'] = []
        if self.holder is not None:
            for k in self.holder:
                result['Holder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.holder = []
        if m.get('Holder') is not None:
            for k in m.get('Holder'):
                temp_model = LookupTmchNoticeResponseBodyClaimsClaimHoldersHolder()
                self.holder.append(temp_model.from_map(k))
        return self


class LookupTmchNoticeResponseBodyClaimsClaimJurDesc(TeaModel):
    def __init__(self, desc=None, jur_cc=None):
        self.desc = desc  # type: str
        self.jur_cc = jur_cc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LookupTmchNoticeResponseBodyClaimsClaimJurDesc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.jur_cc is not None:
            result['JurCC'] = self.jur_cc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('JurCC') is not None:
            self.jur_cc = m.get('JurCC')
        return self


class LookupTmchNoticeResponseBodyClaimsClaim(TeaModel):
    def __init__(self, class_descs=None, contacts=None, goods_and_services=None, holders=None, jur_desc=None,
                 mark_name=None):
        self.class_descs = class_descs  # type: LookupTmchNoticeResponseBodyClaimsClaimClassDescs
        self.contacts = contacts  # type: LookupTmchNoticeResponseBodyClaimsClaimContacts
        self.goods_and_services = goods_and_services  # type: str
        self.holders = holders  # type: LookupTmchNoticeResponseBodyClaimsClaimHolders
        self.jur_desc = jur_desc  # type: LookupTmchNoticeResponseBodyClaimsClaimJurDesc
        self.mark_name = mark_name  # type: str

    def validate(self):
        if self.class_descs:
            self.class_descs.validate()
        if self.contacts:
            self.contacts.validate()
        if self.holders:
            self.holders.validate()
        if self.jur_desc:
            self.jur_desc.validate()

    def to_map(self):
        _map = super(LookupTmchNoticeResponseBodyClaimsClaim, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_descs is not None:
            result['ClassDescs'] = self.class_descs.to_map()
        if self.contacts is not None:
            result['Contacts'] = self.contacts.to_map()
        if self.goods_and_services is not None:
            result['GoodsAndServices'] = self.goods_and_services
        if self.holders is not None:
            result['Holders'] = self.holders.to_map()
        if self.jur_desc is not None:
            result['JurDesc'] = self.jur_desc.to_map()
        if self.mark_name is not None:
            result['MarkName'] = self.mark_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassDescs') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimClassDescs()
            self.class_descs = temp_model.from_map(m['ClassDescs'])
        if m.get('Contacts') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimContacts()
            self.contacts = temp_model.from_map(m['Contacts'])
        if m.get('GoodsAndServices') is not None:
            self.goods_and_services = m.get('GoodsAndServices')
        if m.get('Holders') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimHolders()
            self.holders = temp_model.from_map(m['Holders'])
        if m.get('JurDesc') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaimsClaimJurDesc()
            self.jur_desc = temp_model.from_map(m['JurDesc'])
        if m.get('MarkName') is not None:
            self.mark_name = m.get('MarkName')
        return self


class LookupTmchNoticeResponseBodyClaims(TeaModel):
    def __init__(self, claim=None):
        self.claim = claim  # type: list[LookupTmchNoticeResponseBodyClaimsClaim]

    def validate(self):
        if self.claim:
            for k in self.claim:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(LookupTmchNoticeResponseBodyClaims, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Claim'] = []
        if self.claim is not None:
            for k in self.claim:
                result['Claim'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.claim = []
        if m.get('Claim') is not None:
            for k in m.get('Claim'):
                temp_model = LookupTmchNoticeResponseBodyClaimsClaim()
                self.claim.append(temp_model.from_map(k))
        return self


class LookupTmchNoticeResponseBody(TeaModel):
    def __init__(self, claims=None, id=None, label=None, not_after=None, not_before=None, request_id=None):
        self.claims = claims  # type: LookupTmchNoticeResponseBodyClaims
        self.id = id  # type: long
        self.label = label  # type: str
        self.not_after = not_after  # type: str
        self.not_before = not_before  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.claims:
            self.claims.validate()

    def to_map(self):
        _map = super(LookupTmchNoticeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.claims is not None:
            result['Claims'] = self.claims.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.not_after is not None:
            result['NotAfter'] = self.not_after
        if self.not_before is not None:
            result['NotBefore'] = self.not_before
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Claims') is not None:
            temp_model = LookupTmchNoticeResponseBodyClaims()
            self.claims = temp_model.from_map(m['Claims'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')
        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LookupTmchNoticeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LookupTmchNoticeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LookupTmchNoticeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LookupTmchNoticeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PollTaskResultRequest(TeaModel):
    def __init__(self, domain_name=None, instance_id=None, lang=None, page_num=None, page_size=None, task_no=None,
                 task_result_status=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.task_no = task_no  # type: str
        self.task_result_status = task_result_status  # type: int
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PollTaskResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_result_status is not None:
            result['TaskResultStatus'] = self.task_result_status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskResultStatus') is not None:
            self.task_result_status = m.get('TaskResultStatus')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class PollTaskResultResponseBodyDataTaskDetail(TeaModel):
    def __init__(self, create_time=None, domain_name=None, error_msg=None, instance_id=None, task_detail_no=None,
                 task_no=None, task_result=None, task_status=None, task_status_code=None, task_type=None,
                 task_type_description=None, try_count=None, update_time=None):
        self.create_time = create_time  # type: str
        self.domain_name = domain_name  # type: str
        self.error_msg = error_msg  # type: str
        self.instance_id = instance_id  # type: str
        self.task_detail_no = task_detail_no  # type: str
        self.task_no = task_no  # type: str
        self.task_result = task_result  # type: str
        self.task_status = task_status  # type: str
        self.task_status_code = task_status_code  # type: int
        self.task_type = task_type  # type: str
        self.task_type_description = task_type_description  # type: str
        self.try_count = try_count  # type: int
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PollTaskResultResponseBodyDataTaskDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        if self.try_count is not None:
            result['TryCount'] = self.try_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class PollTaskResultResponseBodyData(TeaModel):
    def __init__(self, task_detail=None):
        self.task_detail = task_detail  # type: list[PollTaskResultResponseBodyDataTaskDetail]

    def validate(self):
        if self.task_detail:
            for k in self.task_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PollTaskResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskDetail'] = []
        if self.task_detail is not None:
            for k in self.task_detail:
                result['TaskDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_detail = []
        if m.get('TaskDetail') is not None:
            for k in m.get('TaskDetail'):
                temp_model = PollTaskResultResponseBodyDataTaskDetail()
                self.task_detail.append(temp_model.from_map(k))
        return self


class PollTaskResultResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, next_page=None, page_size=None, pre_page=None,
                 request_id=None, total_item_num=None, total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: PollTaskResultResponseBodyData
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
        _map = super(PollTaskResultResponseBody, self).to_map()
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
            temp_model = PollTaskResultResponseBodyData()
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


class PollTaskResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PollTaskResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PollTaskResultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PollTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryArtExtensionRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryArtExtensionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryArtExtensionResponseBody(TeaModel):
    def __init__(self, date_or_period=None, dimensions=None, features=None, inscriptions_and_markings=None,
                 maker=None, materials_and_techniques=None, object_type=None, reference=None, request_id=None,
                 subject=None, title=None):
        self.date_or_period = date_or_period  # type: str
        self.dimensions = dimensions  # type: str
        self.features = features  # type: str
        self.inscriptions_and_markings = inscriptions_and_markings  # type: str
        self.maker = maker  # type: str
        self.materials_and_techniques = materials_and_techniques  # type: str
        self.object_type = object_type  # type: str
        self.reference = reference  # type: str
        self.request_id = request_id  # type: str
        self.subject = subject  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryArtExtensionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_or_period is not None:
            result['DateOrPeriod'] = self.date_or_period
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.features is not None:
            result['Features'] = self.features
        if self.inscriptions_and_markings is not None:
            result['InscriptionsAndMarkings'] = self.inscriptions_and_markings
        if self.maker is not None:
            result['Maker'] = self.maker
        if self.materials_and_techniques is not None:
            result['MaterialsAndTechniques'] = self.materials_and_techniques
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.reference is not None:
            result['Reference'] = self.reference
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DateOrPeriod') is not None:
            self.date_or_period = m.get('DateOrPeriod')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('InscriptionsAndMarkings') is not None:
            self.inscriptions_and_markings = m.get('InscriptionsAndMarkings')
        if m.get('Maker') is not None:
            self.maker = m.get('Maker')
        if m.get('MaterialsAndTechniques') is not None:
            self.materials_and_techniques = m.get('MaterialsAndTechniques')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Reference') is not None:
            self.reference = m.get('Reference')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class QueryArtExtensionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryArtExtensionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryArtExtensionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryArtExtensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChangeLogListRequest(TeaModel):
    def __init__(self, domain_name=None, end_date=None, lang=None, page_num=None, page_size=None, start_date=None,
                 user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.end_date = end_date  # type: long
        self.lang = lang  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.start_date = start_date  # type: long
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryChangeLogListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryChangeLogListResponseBodyDataChangeLog(TeaModel):
    def __init__(self, details=None, domain_name=None, operation=None, operation_ipaddress=None, result=None,
                 time=None):
        self.details = details  # type: str
        self.domain_name = domain_name  # type: str
        self.operation = operation  # type: str
        self.operation_ipaddress = operation_ipaddress  # type: str
        self.result = result  # type: str
        self.time = time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryChangeLogListResponseBodyDataChangeLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.details is not None:
            result['Details'] = self.details
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.operation_ipaddress is not None:
            result['OperationIPAddress'] = self.operation_ipaddress
        if self.result is not None:
            result['Result'] = self.result
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('OperationIPAddress') is not None:
            self.operation_ipaddress = m.get('OperationIPAddress')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QueryChangeLogListResponseBodyData(TeaModel):
    def __init__(self, change_log=None):
        self.change_log = change_log  # type: list[QueryChangeLogListResponseBodyDataChangeLog]

    def validate(self):
        if self.change_log:
            for k in self.change_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryChangeLogListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChangeLog'] = []
        if self.change_log is not None:
            for k in self.change_log:
                result['ChangeLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.change_log = []
        if m.get('ChangeLog') is not None:
            for k in m.get('ChangeLog'):
                temp_model = QueryChangeLogListResponseBodyDataChangeLog()
                self.change_log.append(temp_model.from_map(k))
        return self


class QueryChangeLogListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, next_page=None, page_size=None, pre_page=None,
                 request_id=None, result_limit=None, total_item_num=None, total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryChangeLogListResponseBodyData
        self.next_page = next_page  # type: bool
        self.page_size = page_size  # type: int
        self.pre_page = pre_page  # type: bool
        self.request_id = request_id  # type: str
        self.result_limit = result_limit  # type: bool
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryChangeLogListResponseBody, self).to_map()
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
        if self.result_limit is not None:
            result['ResultLimit'] = self.result_limit
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
            temp_model = QueryChangeLogListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultLimit') is not None:
            self.result_limit = m.get('ResultLimit')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryChangeLogListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryChangeLogListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryChangeLogListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryChangeLogListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryContactInfoRequest(TeaModel):
    def __init__(self, contact_type=None, domain_name=None, lang=None, user_client_ip=None):
        self.contact_type = contact_type  # type: str
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryContactInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_type is not None:
            result['ContactType'] = self.contact_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryContactInfoResponseBody(TeaModel):
    def __init__(self, address=None, city=None, country=None, create_date=None, email=None, postal_code=None,
                 province=None, registrant_name=None, registrant_organization=None, request_id=None, tel_area=None,
                 tel_ext=None, telephone=None):
        self.address = address  # type: str
        self.city = city  # type: str
        self.country = country  # type: str
        self.create_date = create_date  # type: str
        self.email = email  # type: str
        self.postal_code = postal_code  # type: str
        self.province = province  # type: str
        self.registrant_name = registrant_name  # type: str
        self.registrant_organization = registrant_organization  # type: str
        self.request_id = request_id  # type: str
        self.tel_area = tel_area  # type: str
        self.tel_ext = tel_ext  # type: str
        self.telephone = telephone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryContactInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.email is not None:
            result['Email'] = self.email
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        return self


class QueryContactInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryContactInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryContactInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryContactInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDSRecordRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDSRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryDSRecordResponseBodyDSRecordList(TeaModel):
    def __init__(self, algorithm=None, digest=None, digest_type=None, key_tag=None):
        self.algorithm = algorithm  # type: int
        self.digest = digest  # type: str
        self.digest_type = digest_type  # type: int
        self.key_tag = key_tag  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDSRecordResponseBodyDSRecordList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.digest_type is not None:
            result['DigestType'] = self.digest_type
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('DigestType') is not None:
            self.digest_type = m.get('DigestType')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        return self


class QueryDSRecordResponseBody(TeaModel):
    def __init__(self, dsrecord_list=None, request_id=None):
        self.dsrecord_list = dsrecord_list  # type: list[QueryDSRecordResponseBodyDSRecordList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dsrecord_list:
            for k in self.dsrecord_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDSRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DSRecordList'] = []
        if self.dsrecord_list is not None:
            for k in self.dsrecord_list:
                result['DSRecordList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dsrecord_list = []
        if m.get('DSRecordList') is not None:
            for k in m.get('DSRecordList'):
                temp_model = QueryDSRecordResponseBodyDSRecordList()
                self.dsrecord_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDSRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDSRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDSRecordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryDSRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDnsHostRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, user_client_ip=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDnsHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryDnsHostResponseBodyDnsHostList(TeaModel):
    def __init__(self, dns_name=None, ip_list=None):
        self.dns_name = dns_name  # type: str
        self.ip_list = ip_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDnsHostResponseBodyDnsHostList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        return self


class QueryDnsHostResponseBody(TeaModel):
    def __init__(self, dns_host_list=None, request_id=None):
        self.dns_host_list = dns_host_list  # type: list[QueryDnsHostResponseBodyDnsHostList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dns_host_list:
            for k in self.dns_host_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDnsHostResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DnsHostList'] = []
        if self.dns_host_list is not None:
            for k in self.dns_host_list:
                result['DnsHostList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dns_host_list = []
        if m.get('DnsHostList') is not None:
            for k in m.get('DnsHostList'):
                temp_model = QueryDnsHostResponseBodyDnsHostList()
                self.dns_host_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDnsHostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDnsHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDnsHostResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryDnsHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDomainByDomainNameRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDomainByDomainNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryDomainByDomainNameResponseBodyDnsList(TeaModel):
    def __init__(self, dns=None):
        self.dns = dns  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDomainByDomainNameResponseBodyDnsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns is not None:
            result['Dns'] = self.dns
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dns') is not None:
            self.dns = m.get('Dns')
        return self


class QueryDomainByDomainNameResponseBody(TeaModel):
    def __init__(self, dns_list=None, domain_name=None, domain_name_proxy_service=None,
                 domain_name_verification_status=None, email=None, email_verification_client_hold=None, email_verification_status=None,
                 expiration_date=None, expiration_date_long=None, instance_id=None, premium=None, real_name_status=None,
                 registrant_name=None, registrant_organization=None, registrant_type=None, registrant_updating_status=None,
                 registration_date=None, registration_date_long=None, request_id=None, transfer_out_status=None,
                 transfer_prohibition_lock=None, update_prohibition_lock=None, user_id=None):
        self.dns_list = dns_list  # type: QueryDomainByDomainNameResponseBodyDnsList
        self.domain_name = domain_name  # type: str
        self.domain_name_proxy_service = domain_name_proxy_service  # type: bool
        self.domain_name_verification_status = domain_name_verification_status  # type: str
        self.email = email  # type: str
        self.email_verification_client_hold = email_verification_client_hold  # type: bool
        self.email_verification_status = email_verification_status  # type: int
        self.expiration_date = expiration_date  # type: str
        self.expiration_date_long = expiration_date_long  # type: long
        self.instance_id = instance_id  # type: str
        self.premium = premium  # type: bool
        self.real_name_status = real_name_status  # type: str
        self.registrant_name = registrant_name  # type: str
        self.registrant_organization = registrant_organization  # type: str
        self.registrant_type = registrant_type  # type: str
        self.registrant_updating_status = registrant_updating_status  # type: str
        self.registration_date = registration_date  # type: str
        self.registration_date_long = registration_date_long  # type: long
        self.request_id = request_id  # type: str
        self.transfer_out_status = transfer_out_status  # type: str
        self.transfer_prohibition_lock = transfer_prohibition_lock  # type: str
        self.update_prohibition_lock = update_prohibition_lock  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.dns_list:
            self.dns_list.validate()

    def to_map(self):
        _map = super(QueryDomainByDomainNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_list is not None:
            result['DnsList'] = self.dns_list.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_proxy_service is not None:
            result['DomainNameProxyService'] = self.domain_name_proxy_service
        if self.domain_name_verification_status is not None:
            result['DomainNameVerificationStatus'] = self.domain_name_verification_status
        if self.email is not None:
            result['Email'] = self.email
        if self.email_verification_client_hold is not None:
            result['EmailVerificationClientHold'] = self.email_verification_client_hold
        if self.email_verification_status is not None:
            result['EmailVerificationStatus'] = self.email_verification_status
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.expiration_date_long is not None:
            result['ExpirationDateLong'] = self.expiration_date_long
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.premium is not None:
            result['Premium'] = self.premium
        if self.real_name_status is not None:
            result['RealNameStatus'] = self.real_name_status
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.registrant_updating_status is not None:
            result['RegistrantUpdatingStatus'] = self.registrant_updating_status
        if self.registration_date is not None:
            result['RegistrationDate'] = self.registration_date
        if self.registration_date_long is not None:
            result['RegistrationDateLong'] = self.registration_date_long
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transfer_out_status is not None:
            result['TransferOutStatus'] = self.transfer_out_status
        if self.transfer_prohibition_lock is not None:
            result['TransferProhibitionLock'] = self.transfer_prohibition_lock
        if self.update_prohibition_lock is not None:
            result['UpdateProhibitionLock'] = self.update_prohibition_lock
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DnsList') is not None:
            temp_model = QueryDomainByDomainNameResponseBodyDnsList()
            self.dns_list = temp_model.from_map(m['DnsList'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameProxyService') is not None:
            self.domain_name_proxy_service = m.get('DomainNameProxyService')
        if m.get('DomainNameVerificationStatus') is not None:
            self.domain_name_verification_status = m.get('DomainNameVerificationStatus')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EmailVerificationClientHold') is not None:
            self.email_verification_client_hold = m.get('EmailVerificationClientHold')
        if m.get('EmailVerificationStatus') is not None:
            self.email_verification_status = m.get('EmailVerificationStatus')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('ExpirationDateLong') is not None:
            self.expiration_date_long = m.get('ExpirationDateLong')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Premium') is not None:
            self.premium = m.get('Premium')
        if m.get('RealNameStatus') is not None:
            self.real_name_status = m.get('RealNameStatus')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('RegistrantUpdatingStatus') is not None:
            self.registrant_updating_status = m.get('RegistrantUpdatingStatus')
        if m.get('RegistrationDate') is not None:
            self.registration_date = m.get('RegistrationDate')
        if m.get('RegistrationDateLong') is not None:
            self.registration_date_long = m.get('RegistrationDateLong')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransferOutStatus') is not None:
            self.transfer_out_status = m.get('TransferOutStatus')
        if m.get('TransferProhibitionLock') is not None:
            self.transfer_prohibition_lock = m.get('TransferProhibitionLock')
        if m.get('UpdateProhibitionLock') is not None:
            self.update_prohibition_lock = m.get('UpdateProhibitionLock')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryDomainByDomainNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDomainByDomainNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDomainByDomainNameResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryDomainByDomainNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDomainByInstanceIdRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, user_client_ip=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDomainByInstanceIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryDomainByInstanceIdResponseBodyDnsList(TeaModel):
    def __init__(self, dns=None):
        self.dns = dns  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDomainByInstanceIdResponseBodyDnsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns is not None:
            result['Dns'] = self.dns
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dns') is not None:
            self.dns = m.get('Dns')
        return self


class QueryDomainByInstanceIdResponseBody(TeaModel):
    def __init__(self, dns_list=None, domain_name=None, domain_name_proxy_service=None,
                 domain_name_verification_status=None, email=None, email_verification_client_hold=None, email_verification_status=None,
                 expiration_date=None, expiration_date_long=None, instance_id=None, premium=None, real_name_status=None,
                 registrant_name=None, registrant_organization=None, registrant_type=None, registrant_updating_status=None,
                 registration_date=None, registration_date_long=None, request_id=None, transfer_out_status=None,
                 transfer_prohibition_lock=None, update_prohibition_lock=None, user_id=None):
        self.dns_list = dns_list  # type: QueryDomainByInstanceIdResponseBodyDnsList
        self.domain_name = domain_name  # type: str
        self.domain_name_proxy_service = domain_name_proxy_service  # type: bool
        self.domain_name_verification_status = domain_name_verification_status  # type: str
        self.email = email  # type: str
        self.email_verification_client_hold = email_verification_client_hold  # type: bool
        self.email_verification_status = email_verification_status  # type: int
        self.expiration_date = expiration_date  # type: str
        self.expiration_date_long = expiration_date_long  # type: long
        self.instance_id = instance_id  # type: str
        self.premium = premium  # type: bool
        self.real_name_status = real_name_status  # type: str
        self.registrant_name = registrant_name  # type: str
        self.registrant_organization = registrant_organization  # type: str
        self.registrant_type = registrant_type  # type: str
        self.registrant_updating_status = registrant_updating_status  # type: str
        self.registration_date = registration_date  # type: str
        self.registration_date_long = registration_date_long  # type: long
        self.request_id = request_id  # type: str
        self.transfer_out_status = transfer_out_status  # type: str
        self.transfer_prohibition_lock = transfer_prohibition_lock  # type: str
        self.update_prohibition_lock = update_prohibition_lock  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.dns_list:
            self.dns_list.validate()

    def to_map(self):
        _map = super(QueryDomainByInstanceIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_list is not None:
            result['DnsList'] = self.dns_list.to_map()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_proxy_service is not None:
            result['DomainNameProxyService'] = self.domain_name_proxy_service
        if self.domain_name_verification_status is not None:
            result['DomainNameVerificationStatus'] = self.domain_name_verification_status
        if self.email is not None:
            result['Email'] = self.email
        if self.email_verification_client_hold is not None:
            result['EmailVerificationClientHold'] = self.email_verification_client_hold
        if self.email_verification_status is not None:
            result['EmailVerificationStatus'] = self.email_verification_status
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.expiration_date_long is not None:
            result['ExpirationDateLong'] = self.expiration_date_long
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.premium is not None:
            result['Premium'] = self.premium
        if self.real_name_status is not None:
            result['RealNameStatus'] = self.real_name_status
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.registrant_updating_status is not None:
            result['RegistrantUpdatingStatus'] = self.registrant_updating_status
        if self.registration_date is not None:
            result['RegistrationDate'] = self.registration_date
        if self.registration_date_long is not None:
            result['RegistrationDateLong'] = self.registration_date_long
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transfer_out_status is not None:
            result['TransferOutStatus'] = self.transfer_out_status
        if self.transfer_prohibition_lock is not None:
            result['TransferProhibitionLock'] = self.transfer_prohibition_lock
        if self.update_prohibition_lock is not None:
            result['UpdateProhibitionLock'] = self.update_prohibition_lock
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DnsList') is not None:
            temp_model = QueryDomainByInstanceIdResponseBodyDnsList()
            self.dns_list = temp_model.from_map(m['DnsList'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameProxyService') is not None:
            self.domain_name_proxy_service = m.get('DomainNameProxyService')
        if m.get('DomainNameVerificationStatus') is not None:
            self.domain_name_verification_status = m.get('DomainNameVerificationStatus')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EmailVerificationClientHold') is not None:
            self.email_verification_client_hold = m.get('EmailVerificationClientHold')
        if m.get('EmailVerificationStatus') is not None:
            self.email_verification_status = m.get('EmailVerificationStatus')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('ExpirationDateLong') is not None:
            self.expiration_date_long = m.get('ExpirationDateLong')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Premium') is not None:
            self.premium = m.get('Premium')
        if m.get('RealNameStatus') is not None:
            self.real_name_status = m.get('RealNameStatus')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('RegistrantUpdatingStatus') is not None:
            self.registrant_updating_status = m.get('RegistrantUpdatingStatus')
        if m.get('RegistrationDate') is not None:
            self.registration_date = m.get('RegistrationDate')
        if m.get('RegistrationDateLong') is not None:
            self.registration_date_long = m.get('RegistrationDateLong')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransferOutStatus') is not None:
            self.transfer_out_status = m.get('TransferOutStatus')
        if m.get('TransferProhibitionLock') is not None:
            self.transfer_prohibition_lock = m.get('TransferProhibitionLock')
        if m.get('UpdateProhibitionLock') is not None:
            self.update_prohibition_lock = m.get('UpdateProhibitionLock')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryDomainByInstanceIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDomainByInstanceIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDomainByInstanceIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryDomainByInstanceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDomainListRequest(TeaModel):
    def __init__(self, domain_name=None, end_expiration_date=None, end_registration_date=None, lang=None,
                 order_by_type=None, order_key_type=None, page_num=None, page_size=None, product_domain_type=None,
                 query_type=None, start_expiration_date=None, start_registration_date=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.end_expiration_date = end_expiration_date  # type: long
        self.end_registration_date = end_registration_date  # type: long
        self.lang = lang  # type: str
        self.order_by_type = order_by_type  # type: str
        self.order_key_type = order_key_type  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.product_domain_type = product_domain_type  # type: str
        self.query_type = query_type  # type: str
        self.start_expiration_date = start_expiration_date  # type: long
        self.start_registration_date = start_registration_date  # type: long
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDomainListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_expiration_date is not None:
            result['EndExpirationDate'] = self.end_expiration_date
        if self.end_registration_date is not None:
            result['EndRegistrationDate'] = self.end_registration_date
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.order_by_type is not None:
            result['OrderByType'] = self.order_by_type
        if self.order_key_type is not None:
            result['OrderKeyType'] = self.order_key_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_domain_type is not None:
            result['ProductDomainType'] = self.product_domain_type
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.start_expiration_date is not None:
            result['StartExpirationDate'] = self.start_expiration_date
        if self.start_registration_date is not None:
            result['StartRegistrationDate'] = self.start_registration_date
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndExpirationDate') is not None:
            self.end_expiration_date = m.get('EndExpirationDate')
        if m.get('EndRegistrationDate') is not None:
            self.end_registration_date = m.get('EndRegistrationDate')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OrderByType') is not None:
            self.order_by_type = m.get('OrderByType')
        if m.get('OrderKeyType') is not None:
            self.order_key_type = m.get('OrderKeyType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductDomainType') is not None:
            self.product_domain_type = m.get('ProductDomainType')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('StartExpirationDate') is not None:
            self.start_expiration_date = m.get('StartExpirationDate')
        if m.get('StartRegistrationDate') is not None:
            self.start_registration_date = m.get('StartRegistrationDate')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryDomainListResponseBodyDataDomain(TeaModel):
    def __init__(self, domain_audit_status=None, domain_name=None, domain_status=None, domain_type=None,
                 expiration_curr_date_diff=None, expiration_date=None, expiration_date_long=None, expiration_date_status=None,
                 instance_id=None, premium=None, product_id=None, registrant_type=None, registration_date=None,
                 registration_date_long=None, remark=None):
        self.domain_audit_status = domain_audit_status  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.domain_type = domain_type  # type: str
        self.expiration_curr_date_diff = expiration_curr_date_diff  # type: int
        self.expiration_date = expiration_date  # type: str
        self.expiration_date_long = expiration_date_long  # type: long
        self.expiration_date_status = expiration_date_status  # type: str
        self.instance_id = instance_id  # type: str
        self.premium = premium  # type: bool
        self.product_id = product_id  # type: str
        self.registrant_type = registrant_type  # type: str
        self.registration_date = registration_date  # type: str
        self.registration_date_long = registration_date_long  # type: long
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDomainListResponseBodyDataDomain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_audit_status is not None:
            result['DomainAuditStatus'] = self.domain_audit_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.expiration_curr_date_diff is not None:
            result['ExpirationCurrDateDiff'] = self.expiration_curr_date_diff
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.expiration_date_long is not None:
            result['ExpirationDateLong'] = self.expiration_date_long
        if self.expiration_date_status is not None:
            result['ExpirationDateStatus'] = self.expiration_date_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.premium is not None:
            result['Premium'] = self.premium
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.registration_date is not None:
            result['RegistrationDate'] = self.registration_date
        if self.registration_date_long is not None:
            result['RegistrationDateLong'] = self.registration_date_long
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainAuditStatus') is not None:
            self.domain_audit_status = m.get('DomainAuditStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('ExpirationCurrDateDiff') is not None:
            self.expiration_curr_date_diff = m.get('ExpirationCurrDateDiff')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('ExpirationDateLong') is not None:
            self.expiration_date_long = m.get('ExpirationDateLong')
        if m.get('ExpirationDateStatus') is not None:
            self.expiration_date_status = m.get('ExpirationDateStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Premium') is not None:
            self.premium = m.get('Premium')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('RegistrationDate') is not None:
            self.registration_date = m.get('RegistrationDate')
        if m.get('RegistrationDateLong') is not None:
            self.registration_date_long = m.get('RegistrationDateLong')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class QueryDomainListResponseBodyData(TeaModel):
    def __init__(self, domain=None):
        self.domain = domain  # type: list[QueryDomainListResponseBodyDataDomain]

    def validate(self):
        if self.domain:
            for k in self.domain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDomainListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Domain'] = []
        if self.domain is not None:
            for k in self.domain:
                result['Domain'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain = []
        if m.get('Domain') is not None:
            for k in m.get('Domain'):
                temp_model = QueryDomainListResponseBodyDataDomain()
                self.domain.append(temp_model.from_map(k))
        return self


class QueryDomainListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, next_page=None, page_size=None, pre_page=None,
                 request_id=None, total_item_num=None, total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryDomainListResponseBodyData
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
        _map = super(QueryDomainListResponseBody, self).to_map()
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
            temp_model = QueryDomainListResponseBodyData()
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


class QueryDomainListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDomainListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDomainListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryDomainListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDomainRealNameVerificationInfoRequest(TeaModel):
    def __init__(self, domain_name=None, fetch_image=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.fetch_image = fetch_image  # type: bool
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDomainRealNameVerificationInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.fetch_image is not None:
            result['FetchImage'] = self.fetch_image
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FetchImage') is not None:
            self.fetch_image = m.get('FetchImage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryDomainRealNameVerificationInfoResponseBody(TeaModel):
    def __init__(self, domain_name=None, identity_credential=None, identity_credential_no=None,
                 identity_credential_type=None, identity_credential_url=None, instance_id=None, request_id=None, submission_date=None):
        self.domain_name = domain_name  # type: str
        self.identity_credential = identity_credential  # type: str
        self.identity_credential_no = identity_credential_no  # type: str
        self.identity_credential_type = identity_credential_type  # type: str
        self.identity_credential_url = identity_credential_url  # type: str
        self.instance_id = instance_id  # type: str
        self.request_id = request_id  # type: str
        self.submission_date = submission_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDomainRealNameVerificationInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential
        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no
        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type
        if self.identity_credential_url is not None:
            result['IdentityCredentialUrl'] = self.identity_credential_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.submission_date is not None:
            result['SubmissionDate'] = self.submission_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')
        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')
        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')
        if m.get('IdentityCredentialUrl') is not None:
            self.identity_credential_url = m.get('IdentityCredentialUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubmissionDate') is not None:
            self.submission_date = m.get('SubmissionDate')
        return self


class QueryDomainRealNameVerificationInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDomainRealNameVerificationInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDomainRealNameVerificationInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryDomainRealNameVerificationInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEnsAssociationRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEnsAssociationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryEnsAssociationResponseBody(TeaModel):
    def __init__(self, address=None, request_id=None):
        self.address = address  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEnsAssociationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryEnsAssociationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryEnsAssociationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryEnsAssociationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryEnsAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFailReasonForDomainRealNameVerificationRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, real_name_verification_action=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.real_name_verification_action = real_name_verification_action  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFailReasonForDomainRealNameVerificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.real_name_verification_action is not None:
            result['RealNameVerificationAction'] = self.real_name_verification_action
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RealNameVerificationAction') is not None:
            self.real_name_verification_action = m.get('RealNameVerificationAction')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryFailReasonForDomainRealNameVerificationResponseBodyData(TeaModel):
    def __init__(self, date=None, fail_reason=None):
        self.date = date  # type: str
        self.fail_reason = fail_reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFailReasonForDomainRealNameVerificationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        return self


class QueryFailReasonForDomainRealNameVerificationResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[QueryFailReasonForDomainRealNameVerificationResponseBodyData]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFailReasonForDomainRealNameVerificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryFailReasonForDomainRealNameVerificationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryFailReasonForDomainRealNameVerificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFailReasonForDomainRealNameVerificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFailReasonForDomainRealNameVerificationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryFailReasonForDomainRealNameVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFailReasonForRegistrantProfileRealNameVerificationRequest(TeaModel):
    def __init__(self, lang=None, registrant_profile_id=None, user_client_ip=None):
        self.lang = lang  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFailReasonForRegistrantProfileRealNameVerificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileID'] = self.registrant_profile_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileID') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileID')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryFailReasonForRegistrantProfileRealNameVerificationResponseBodyData(TeaModel):
    def __init__(self, date=None, fail_reason=None):
        self.date = date  # type: str
        self.fail_reason = fail_reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFailReasonForRegistrantProfileRealNameVerificationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        return self


class QueryFailReasonForRegistrantProfileRealNameVerificationResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[QueryFailReasonForRegistrantProfileRealNameVerificationResponseBodyData]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFailReasonForRegistrantProfileRealNameVerificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryFailReasonForRegistrantProfileRealNameVerificationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryFailReasonForRegistrantProfileRealNameVerificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFailReasonForRegistrantProfileRealNameVerificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFailReasonForRegistrantProfileRealNameVerificationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryFailReasonForRegistrantProfileRealNameVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLocalEnsAssociationRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryLocalEnsAssociationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryLocalEnsAssociationResponseBody(TeaModel):
    def __init__(self, address=None, request_id=None):
        self.address = address  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryLocalEnsAssociationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryLocalEnsAssociationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryLocalEnsAssociationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryLocalEnsAssociationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryLocalEnsAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRegistrantProfileRealNameVerificationInfoRequest(TeaModel):
    def __init__(self, fetch_image=None, lang=None, registrant_profile_id=None, user_client_ip=None):
        self.fetch_image = fetch_image  # type: bool
        self.lang = lang  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRegistrantProfileRealNameVerificationInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fetch_image is not None:
            result['FetchImage'] = self.fetch_image
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FetchImage') is not None:
            self.fetch_image = m.get('FetchImage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryRegistrantProfileRealNameVerificationInfoResponseBody(TeaModel):
    def __init__(self, identity_credential=None, identity_credential_no=None, identity_credential_type=None,
                 identity_credential_url=None, modification_date=None, registrant_profile_id=None, request_id=None, submission_date=None):
        self.identity_credential = identity_credential  # type: str
        self.identity_credential_no = identity_credential_no  # type: str
        self.identity_credential_type = identity_credential_type  # type: str
        self.identity_credential_url = identity_credential_url  # type: str
        self.modification_date = modification_date  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.request_id = request_id  # type: str
        self.submission_date = submission_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRegistrantProfileRealNameVerificationInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential
        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no
        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type
        if self.identity_credential_url is not None:
            result['IdentityCredentialUrl'] = self.identity_credential_url
        if self.modification_date is not None:
            result['ModificationDate'] = self.modification_date
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.submission_date is not None:
            result['SubmissionDate'] = self.submission_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')
        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')
        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')
        if m.get('IdentityCredentialUrl') is not None:
            self.identity_credential_url = m.get('IdentityCredentialUrl')
        if m.get('ModificationDate') is not None:
            self.modification_date = m.get('ModificationDate')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubmissionDate') is not None:
            self.submission_date = m.get('SubmissionDate')
        return self


class QueryRegistrantProfileRealNameVerificationInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRegistrantProfileRealNameVerificationInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRegistrantProfileRealNameVerificationInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryRegistrantProfileRealNameVerificationInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRegistrantProfilesRequest(TeaModel):
    def __init__(self, default_registrant_profile=None, email=None, lang=None, page_num=None, page_size=None,
                 real_name_status=None, registrant_organization=None, registrant_profile_id=None, registrant_profile_type=None,
                 registrant_type=None, user_client_ip=None):
        self.default_registrant_profile = default_registrant_profile  # type: bool
        self.email = email  # type: str
        self.lang = lang  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.real_name_status = real_name_status  # type: str
        self.registrant_organization = registrant_organization  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.registrant_profile_type = registrant_profile_type  # type: str
        self.registrant_type = registrant_type  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRegistrantProfilesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_registrant_profile is not None:
            result['DefaultRegistrantProfile'] = self.default_registrant_profile
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.real_name_status is not None:
            result['RealNameStatus'] = self.real_name_status
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.registrant_profile_type is not None:
            result['RegistrantProfileType'] = self.registrant_profile_type
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultRegistrantProfile') is not None:
            self.default_registrant_profile = m.get('DefaultRegistrantProfile')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RealNameStatus') is not None:
            self.real_name_status = m.get('RealNameStatus')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('RegistrantProfileType') is not None:
            self.registrant_profile_type = m.get('RegistrantProfileType')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryRegistrantProfilesResponseBodyRegistrantProfilesRegistrantProfile(TeaModel):
    def __init__(self, address=None, city=None, country=None, create_time=None, default_registrant_profile=None,
                 email=None, email_verification_status=None, postal_code=None, province=None, real_name_status=None,
                 registrant_name=None, registrant_organization=None, registrant_profile_id=None, registrant_profile_type=None,
                 registrant_type=None, tel_area=None, tel_ext=None, telephone=None, update_time=None):
        self.address = address  # type: str
        self.city = city  # type: str
        self.country = country  # type: str
        self.create_time = create_time  # type: str
        self.default_registrant_profile = default_registrant_profile  # type: bool
        self.email = email  # type: str
        self.email_verification_status = email_verification_status  # type: int
        self.postal_code = postal_code  # type: str
        self.province = province  # type: str
        self.real_name_status = real_name_status  # type: str
        self.registrant_name = registrant_name  # type: str
        self.registrant_organization = registrant_organization  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.registrant_profile_type = registrant_profile_type  # type: str
        self.registrant_type = registrant_type  # type: str
        self.tel_area = tel_area  # type: str
        self.tel_ext = tel_ext  # type: str
        self.telephone = telephone  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRegistrantProfilesResponseBodyRegistrantProfilesRegistrantProfile, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_registrant_profile is not None:
            result['DefaultRegistrantProfile'] = self.default_registrant_profile
        if self.email is not None:
            result['Email'] = self.email
        if self.email_verification_status is not None:
            result['EmailVerificationStatus'] = self.email_verification_status
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.real_name_status is not None:
            result['RealNameStatus'] = self.real_name_status
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.registrant_profile_type is not None:
            result['RegistrantProfileType'] = self.registrant_profile_type
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultRegistrantProfile') is not None:
            self.default_registrant_profile = m.get('DefaultRegistrantProfile')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EmailVerificationStatus') is not None:
            self.email_verification_status = m.get('EmailVerificationStatus')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RealNameStatus') is not None:
            self.real_name_status = m.get('RealNameStatus')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('RegistrantProfileType') is not None:
            self.registrant_profile_type = m.get('RegistrantProfileType')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryRegistrantProfilesResponseBodyRegistrantProfiles(TeaModel):
    def __init__(self, registrant_profile=None):
        self.registrant_profile = registrant_profile  # type: list[QueryRegistrantProfilesResponseBodyRegistrantProfilesRegistrantProfile]

    def validate(self):
        if self.registrant_profile:
            for k in self.registrant_profile:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryRegistrantProfilesResponseBodyRegistrantProfiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegistrantProfile'] = []
        if self.registrant_profile is not None:
            for k in self.registrant_profile:
                result['RegistrantProfile'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.registrant_profile = []
        if m.get('RegistrantProfile') is not None:
            for k in m.get('RegistrantProfile'):
                temp_model = QueryRegistrantProfilesResponseBodyRegistrantProfilesRegistrantProfile()
                self.registrant_profile.append(temp_model.from_map(k))
        return self


class QueryRegistrantProfilesResponseBody(TeaModel):
    def __init__(self, current_page_num=None, next_page=None, page_size=None, pre_page=None,
                 registrant_profiles=None, request_id=None, total_item_num=None, total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.next_page = next_page  # type: bool
        self.page_size = page_size  # type: int
        self.pre_page = pre_page  # type: bool
        self.registrant_profiles = registrant_profiles  # type: QueryRegistrantProfilesResponseBodyRegistrantProfiles
        self.request_id = request_id  # type: str
        self.total_item_num = total_item_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.registrant_profiles:
            self.registrant_profiles.validate()

    def to_map(self):
        _map = super(QueryRegistrantProfilesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.registrant_profiles is not None:
            result['RegistrantProfiles'] = self.registrant_profiles.to_map()
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
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('RegistrantProfiles') is not None:
            temp_model = QueryRegistrantProfilesResponseBodyRegistrantProfiles()
            self.registrant_profiles = temp_model.from_map(m['RegistrantProfiles'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryRegistrantProfilesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRegistrantProfilesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRegistrantProfilesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryRegistrantProfilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskDetailHistoryRequest(TeaModel):
    def __init__(self, domain_name=None, domain_name_cursor=None, lang=None, page_size=None,
                 task_detail_no_cursor=None, task_no=None, task_status=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.domain_name_cursor = domain_name_cursor  # type: str
        self.lang = lang  # type: str
        self.page_size = page_size  # type: int
        self.task_detail_no_cursor = task_detail_no_cursor  # type: str
        self.task_no = task_no  # type: str
        self.task_status = task_status  # type: int
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskDetailHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_cursor is not None:
            result['DomainNameCursor'] = self.domain_name_cursor
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_detail_no_cursor is not None:
            result['TaskDetailNoCursor'] = self.task_detail_no_cursor
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameCursor') is not None:
            self.domain_name_cursor = m.get('DomainNameCursor')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskDetailNoCursor') is not None:
            self.task_detail_no_cursor = m.get('TaskDetailNoCursor')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryTaskDetailHistoryResponseBodyCurrentPageCursor(TeaModel):
    def __init__(self, create_time=None, domain_name=None, error_msg=None, instance_id=None, task_detail_no=None,
                 task_no=None, task_status=None, task_status_code=None, task_type=None, task_type_description=None,
                 try_count=None, update_time=None):
        self.create_time = create_time  # type: str
        self.domain_name = domain_name  # type: str
        self.error_msg = error_msg  # type: str
        self.instance_id = instance_id  # type: str
        self.task_detail_no = task_detail_no  # type: str
        self.task_no = task_no  # type: str
        self.task_status = task_status  # type: str
        self.task_status_code = task_status_code  # type: int
        self.task_type = task_type  # type: str
        self.task_type_description = task_type_description  # type: str
        self.try_count = try_count  # type: int
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskDetailHistoryResponseBodyCurrentPageCursor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        if self.try_count is not None:
            result['TryCount'] = self.try_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryTaskDetailHistoryResponseBodyNextPageCursor(TeaModel):
    def __init__(self, create_time=None, domain_name=None, error_msg=None, instance_id=None, task_detail_no=None,
                 task_no=None, task_status=None, task_status_code=None, task_type=None, task_type_description=None,
                 try_count=None, update_time=None):
        self.create_time = create_time  # type: str
        self.domain_name = domain_name  # type: str
        self.error_msg = error_msg  # type: str
        self.instance_id = instance_id  # type: str
        self.task_detail_no = task_detail_no  # type: str
        self.task_no = task_no  # type: str
        self.task_status = task_status  # type: str
        self.task_status_code = task_status_code  # type: int
        self.task_type = task_type  # type: str
        self.task_type_description = task_type_description  # type: str
        self.try_count = try_count  # type: int
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskDetailHistoryResponseBodyNextPageCursor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        if self.try_count is not None:
            result['TryCount'] = self.try_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryTaskDetailHistoryResponseBodyObjects(TeaModel):
    def __init__(self, create_time=None, domain_name=None, error_msg=None, instance_id=None, task_detail_no=None,
                 task_no=None, task_status=None, task_status_code=None, task_type=None, task_type_description=None,
                 try_count=None, update_time=None):
        self.create_time = create_time  # type: str
        self.domain_name = domain_name  # type: str
        self.error_msg = error_msg  # type: str
        self.instance_id = instance_id  # type: str
        self.task_detail_no = task_detail_no  # type: str
        self.task_no = task_no  # type: str
        self.task_status = task_status  # type: str
        self.task_status_code = task_status_code  # type: int
        self.task_type = task_type  # type: str
        self.task_type_description = task_type_description  # type: str
        self.try_count = try_count  # type: int
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskDetailHistoryResponseBodyObjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        if self.try_count is not None:
            result['TryCount'] = self.try_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryTaskDetailHistoryResponseBodyPrePageCursor(TeaModel):
    def __init__(self, create_time=None, domain_name=None, error_msg=None, instance_id=None, task_detail_no=None,
                 task_no=None, task_status=None, task_status_code=None, task_type=None, task_type_description=None,
                 try_count=None, update_time=None):
        self.create_time = create_time  # type: str
        self.domain_name = domain_name  # type: str
        self.error_msg = error_msg  # type: str
        self.instance_id = instance_id  # type: str
        self.task_detail_no = task_detail_no  # type: str
        self.task_no = task_no  # type: str
        self.task_status = task_status  # type: str
        self.task_status_code = task_status_code  # type: int
        self.task_type = task_type  # type: str
        self.task_type_description = task_type_description  # type: str
        self.try_count = try_count  # type: int
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskDetailHistoryResponseBodyPrePageCursor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        if self.try_count is not None:
            result['TryCount'] = self.try_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryTaskDetailHistoryResponseBody(TeaModel):
    def __init__(self, current_page_cursor=None, next_page_cursor=None, objects=None, page_size=None,
                 pre_page_cursor=None, request_id=None):
        self.current_page_cursor = current_page_cursor  # type: QueryTaskDetailHistoryResponseBodyCurrentPageCursor
        self.next_page_cursor = next_page_cursor  # type: QueryTaskDetailHistoryResponseBodyNextPageCursor
        self.objects = objects  # type: list[QueryTaskDetailHistoryResponseBodyObjects]
        self.page_size = page_size  # type: int
        self.pre_page_cursor = pre_page_cursor  # type: QueryTaskDetailHistoryResponseBodyPrePageCursor
        self.request_id = request_id  # type: str

    def validate(self):
        if self.current_page_cursor:
            self.current_page_cursor.validate()
        if self.next_page_cursor:
            self.next_page_cursor.validate()
        if self.objects:
            for k in self.objects:
                if k:
                    k.validate()
        if self.pre_page_cursor:
            self.pre_page_cursor.validate()

    def to_map(self):
        _map = super(QueryTaskDetailHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_cursor is not None:
            result['CurrentPageCursor'] = self.current_page_cursor.to_map()
        if self.next_page_cursor is not None:
            result['NextPageCursor'] = self.next_page_cursor.to_map()
        result['Objects'] = []
        if self.objects is not None:
            for k in self.objects:
                result['Objects'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page_cursor is not None:
            result['PrePageCursor'] = self.pre_page_cursor.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageCursor') is not None:
            temp_model = QueryTaskDetailHistoryResponseBodyCurrentPageCursor()
            self.current_page_cursor = temp_model.from_map(m['CurrentPageCursor'])
        if m.get('NextPageCursor') is not None:
            temp_model = QueryTaskDetailHistoryResponseBodyNextPageCursor()
            self.next_page_cursor = temp_model.from_map(m['NextPageCursor'])
        self.objects = []
        if m.get('Objects') is not None:
            for k in m.get('Objects'):
                temp_model = QueryTaskDetailHistoryResponseBodyObjects()
                self.objects.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePageCursor') is not None:
            temp_model = QueryTaskDetailHistoryResponseBodyPrePageCursor()
            self.pre_page_cursor = temp_model.from_map(m['PrePageCursor'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTaskDetailHistoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTaskDetailHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTaskDetailHistoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTaskDetailHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskDetailListRequest(TeaModel):
    def __init__(self, domain_name=None, instance_id=None, lang=None, page_num=None, page_size=None, task_no=None,
                 task_status=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.task_no = task_no  # type: str
        self.task_status = task_status  # type: int
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskDetailListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryTaskDetailListResponseBodyDataTaskDetail(TeaModel):
    def __init__(self, create_time=None, domain_name=None, error_msg=None, instance_id=None, task_detail_no=None,
                 task_no=None, task_result=None, task_status=None, task_status_code=None, task_type=None,
                 task_type_description=None, try_count=None, update_time=None):
        self.create_time = create_time  # type: str
        self.domain_name = domain_name  # type: str
        self.error_msg = error_msg  # type: str
        self.instance_id = instance_id  # type: str
        self.task_detail_no = task_detail_no  # type: str
        self.task_no = task_no  # type: str
        self.task_result = task_result  # type: str
        self.task_status = task_status  # type: str
        self.task_status_code = task_status_code  # type: int
        self.task_type = task_type  # type: str
        self.task_type_description = task_type_description  # type: str
        self.try_count = try_count  # type: int
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskDetailListResponseBodyDataTaskDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        if self.try_count is not None:
            result['TryCount'] = self.try_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class QueryTaskDetailListResponseBodyData(TeaModel):
    def __init__(self, task_detail=None):
        self.task_detail = task_detail  # type: list[QueryTaskDetailListResponseBodyDataTaskDetail]

    def validate(self):
        if self.task_detail:
            for k in self.task_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTaskDetailListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskDetail'] = []
        if self.task_detail is not None:
            for k in self.task_detail:
                result['TaskDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_detail = []
        if m.get('TaskDetail') is not None:
            for k in m.get('TaskDetail'):
                temp_model = QueryTaskDetailListResponseBodyDataTaskDetail()
                self.task_detail.append(temp_model.from_map(k))
        return self


class QueryTaskDetailListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, next_page=None, page_size=None, pre_page=None,
                 request_id=None, total_item_num=None, total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryTaskDetailListResponseBodyData
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
        _map = super(QueryTaskDetailListResponseBody, self).to_map()
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
            temp_model = QueryTaskDetailListResponseBodyData()
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


class QueryTaskDetailListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTaskDetailListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTaskDetailListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTaskDetailListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskInfoHistoryRequest(TeaModel):
    def __init__(self, begin_create_time=None, create_time_cursor=None, end_create_time=None, lang=None,
                 page_size=None, task_no_cursor=None, user_client_ip=None):
        self.begin_create_time = begin_create_time  # type: long
        self.create_time_cursor = create_time_cursor  # type: long
        self.end_create_time = end_create_time  # type: long
        self.lang = lang  # type: str
        self.page_size = page_size  # type: int
        self.task_no_cursor = task_no_cursor  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskInfoHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_create_time is not None:
            result['BeginCreateTime'] = self.begin_create_time
        if self.create_time_cursor is not None:
            result['CreateTimeCursor'] = self.create_time_cursor
        if self.end_create_time is not None:
            result['EndCreateTime'] = self.end_create_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_no_cursor is not None:
            result['TaskNoCursor'] = self.task_no_cursor
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginCreateTime') is not None:
            self.begin_create_time = m.get('BeginCreateTime')
        if m.get('CreateTimeCursor') is not None:
            self.create_time_cursor = m.get('CreateTimeCursor')
        if m.get('EndCreateTime') is not None:
            self.end_create_time = m.get('EndCreateTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskNoCursor') is not None:
            self.task_no_cursor = m.get('TaskNoCursor')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryTaskInfoHistoryResponseBodyCurrentPageCursor(TeaModel):
    def __init__(self, clientip=None, create_time=None, create_time_long=None, task_no=None, task_num=None,
                 task_status=None, task_status_code=None, task_type=None, task_type_description=None):
        self.clientip = clientip  # type: str
        self.create_time = create_time  # type: str
        self.create_time_long = create_time_long  # type: long
        self.task_no = task_no  # type: str
        self.task_num = task_num  # type: int
        self.task_status = task_status  # type: str
        self.task_status_code = task_status_code  # type: int
        self.task_type = task_type  # type: str
        self.task_type_description = task_type_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskInfoHistoryResponseBodyCurrentPageCursor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clientip is not None:
            result['Clientip'] = self.clientip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_num is not None:
            result['TaskNum'] = self.task_num
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Clientip') is not None:
            self.clientip = m.get('Clientip')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        return self


class QueryTaskInfoHistoryResponseBodyNextPageCursor(TeaModel):
    def __init__(self, clientip=None, create_time=None, create_time_long=None, task_no=None, task_num=None,
                 task_status=None, task_status_code=None, task_type=None, task_type_description=None):
        self.clientip = clientip  # type: str
        self.create_time = create_time  # type: str
        self.create_time_long = create_time_long  # type: long
        self.task_no = task_no  # type: str
        self.task_num = task_num  # type: int
        self.task_status = task_status  # type: str
        self.task_status_code = task_status_code  # type: int
        self.task_type = task_type  # type: str
        self.task_type_description = task_type_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskInfoHistoryResponseBodyNextPageCursor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clientip is not None:
            result['Clientip'] = self.clientip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_num is not None:
            result['TaskNum'] = self.task_num
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Clientip') is not None:
            self.clientip = m.get('Clientip')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        return self


class QueryTaskInfoHistoryResponseBodyObjects(TeaModel):
    def __init__(self, clientip=None, create_time=None, create_time_long=None, task_no=None, task_num=None,
                 task_status=None, task_status_code=None, task_type=None, task_type_description=None):
        self.clientip = clientip  # type: str
        self.create_time = create_time  # type: str
        self.create_time_long = create_time_long  # type: long
        self.task_no = task_no  # type: str
        self.task_num = task_num  # type: int
        self.task_status = task_status  # type: str
        self.task_status_code = task_status_code  # type: int
        self.task_type = task_type  # type: str
        self.task_type_description = task_type_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskInfoHistoryResponseBodyObjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clientip is not None:
            result['Clientip'] = self.clientip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_num is not None:
            result['TaskNum'] = self.task_num
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Clientip') is not None:
            self.clientip = m.get('Clientip')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        return self


class QueryTaskInfoHistoryResponseBodyPrePageCursor(TeaModel):
    def __init__(self, clientip=None, create_time=None, create_time_long=None, task_no=None, task_num=None,
                 task_status=None, task_status_code=None, task_type=None, task_type_description=None):
        self.clientip = clientip  # type: str
        self.create_time = create_time  # type: str
        self.create_time_long = create_time_long  # type: long
        self.task_no = task_no  # type: str
        self.task_num = task_num  # type: int
        self.task_status = task_status  # type: str
        self.task_status_code = task_status_code  # type: int
        self.task_type = task_type  # type: str
        self.task_type_description = task_type_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskInfoHistoryResponseBodyPrePageCursor, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clientip is not None:
            result['Clientip'] = self.clientip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_num is not None:
            result['TaskNum'] = self.task_num
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Clientip') is not None:
            self.clientip = m.get('Clientip')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        return self


class QueryTaskInfoHistoryResponseBody(TeaModel):
    def __init__(self, current_page_cursor=None, next_page_cursor=None, objects=None, page_size=None,
                 pre_page_cursor=None, request_id=None):
        self.current_page_cursor = current_page_cursor  # type: QueryTaskInfoHistoryResponseBodyCurrentPageCursor
        self.next_page_cursor = next_page_cursor  # type: QueryTaskInfoHistoryResponseBodyNextPageCursor
        self.objects = objects  # type: list[QueryTaskInfoHistoryResponseBodyObjects]
        self.page_size = page_size  # type: int
        self.pre_page_cursor = pre_page_cursor  # type: QueryTaskInfoHistoryResponseBodyPrePageCursor
        self.request_id = request_id  # type: str

    def validate(self):
        if self.current_page_cursor:
            self.current_page_cursor.validate()
        if self.next_page_cursor:
            self.next_page_cursor.validate()
        if self.objects:
            for k in self.objects:
                if k:
                    k.validate()
        if self.pre_page_cursor:
            self.pre_page_cursor.validate()

    def to_map(self):
        _map = super(QueryTaskInfoHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_cursor is not None:
            result['CurrentPageCursor'] = self.current_page_cursor.to_map()
        if self.next_page_cursor is not None:
            result['NextPageCursor'] = self.next_page_cursor.to_map()
        result['Objects'] = []
        if self.objects is not None:
            for k in self.objects:
                result['Objects'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page_cursor is not None:
            result['PrePageCursor'] = self.pre_page_cursor.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPageCursor') is not None:
            temp_model = QueryTaskInfoHistoryResponseBodyCurrentPageCursor()
            self.current_page_cursor = temp_model.from_map(m['CurrentPageCursor'])
        if m.get('NextPageCursor') is not None:
            temp_model = QueryTaskInfoHistoryResponseBodyNextPageCursor()
            self.next_page_cursor = temp_model.from_map(m['NextPageCursor'])
        self.objects = []
        if m.get('Objects') is not None:
            for k in m.get('Objects'):
                temp_model = QueryTaskInfoHistoryResponseBodyObjects()
                self.objects.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePageCursor') is not None:
            temp_model = QueryTaskInfoHistoryResponseBodyPrePageCursor()
            self.pre_page_cursor = temp_model.from_map(m['PrePageCursor'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTaskInfoHistoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTaskInfoHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTaskInfoHistoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTaskInfoHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskListRequest(TeaModel):
    def __init__(self, begin_create_time=None, end_create_time=None, lang=None, page_num=None, page_size=None,
                 user_client_ip=None):
        self.begin_create_time = begin_create_time  # type: long
        self.end_create_time = end_create_time  # type: long
        self.lang = lang  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_create_time is not None:
            result['BeginCreateTime'] = self.begin_create_time
        if self.end_create_time is not None:
            result['EndCreateTime'] = self.end_create_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginCreateTime') is not None:
            self.begin_create_time = m.get('BeginCreateTime')
        if m.get('EndCreateTime') is not None:
            self.end_create_time = m.get('EndCreateTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryTaskListResponseBodyDataTaskInfo(TeaModel):
    def __init__(self, clientip=None, create_time=None, task_cancel_status=None, task_cancel_status_code=None,
                 task_no=None, task_num=None, task_status=None, task_status_code=None, task_type=None,
                 task_type_description=None):
        self.clientip = clientip  # type: str
        self.create_time = create_time  # type: str
        self.task_cancel_status = task_cancel_status  # type: str
        self.task_cancel_status_code = task_cancel_status_code  # type: int
        self.task_no = task_no  # type: str
        self.task_num = task_num  # type: int
        self.task_status = task_status  # type: str
        self.task_status_code = task_status_code  # type: int
        self.task_type = task_type  # type: str
        self.task_type_description = task_type_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskListResponseBodyDataTaskInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clientip is not None:
            result['Clientip'] = self.clientip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.task_cancel_status is not None:
            result['TaskCancelStatus'] = self.task_cancel_status
        if self.task_cancel_status_code is not None:
            result['TaskCancelStatusCode'] = self.task_cancel_status_code
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        if self.task_num is not None:
            result['TaskNum'] = self.task_num
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Clientip') is not None:
            self.clientip = m.get('Clientip')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TaskCancelStatus') is not None:
            self.task_cancel_status = m.get('TaskCancelStatus')
        if m.get('TaskCancelStatusCode') is not None:
            self.task_cancel_status_code = m.get('TaskCancelStatusCode')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')
        return self


class QueryTaskListResponseBodyData(TeaModel):
    def __init__(self, task_info=None):
        self.task_info = task_info  # type: list[QueryTaskListResponseBodyDataTaskInfo]

    def validate(self):
        if self.task_info:
            for k in self.task_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTaskListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskInfo'] = []
        if self.task_info is not None:
            for k in self.task_info:
                result['TaskInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_info = []
        if m.get('TaskInfo') is not None:
            for k in m.get('TaskInfo'):
                temp_model = QueryTaskListResponseBodyDataTaskInfo()
                self.task_info.append(temp_model.from_map(k))
        return self


class QueryTaskListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, next_page=None, page_size=None, pre_page=None,
                 request_id=None, total_item_num=None, total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryTaskListResponseBodyData
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
        _map = super(QueryTaskListResponseBody, self).to_map()
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
            temp_model = QueryTaskListResponseBodyData()
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


class QueryTransferInByInstanceIdRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, user_client_ip=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTransferInByInstanceIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryTransferInByInstanceIdResponseBody(TeaModel):
    def __init__(self, domain_name=None, email=None, expiration_date=None, expiration_date_long=None,
                 instance_id=None, modification_date=None, modification_date_long=None, need_mail_check=None,
                 progress_bar_type=None, request_id=None, result_code=None, result_date=None, result_date_long=None, result_msg=None,
                 simple_transfer_in_status=None, status=None, submission_date=None, submission_date_long=None,
                 transfer_authorization_code_submission_date=None, transfer_authorization_code_submission_date_long=None, user_id=None,
                 whois_mail_status=None):
        self.domain_name = domain_name  # type: str
        self.email = email  # type: str
        self.expiration_date = expiration_date  # type: str
        self.expiration_date_long = expiration_date_long  # type: long
        self.instance_id = instance_id  # type: str
        self.modification_date = modification_date  # type: str
        self.modification_date_long = modification_date_long  # type: long
        self.need_mail_check = need_mail_check  # type: bool
        self.progress_bar_type = progress_bar_type  # type: int
        self.request_id = request_id  # type: str
        self.result_code = result_code  # type: str
        self.result_date = result_date  # type: str
        self.result_date_long = result_date_long  # type: long
        self.result_msg = result_msg  # type: str
        self.simple_transfer_in_status = simple_transfer_in_status  # type: str
        self.status = status  # type: int
        self.submission_date = submission_date  # type: str
        self.submission_date_long = submission_date_long  # type: long
        self.transfer_authorization_code_submission_date = transfer_authorization_code_submission_date  # type: str
        self.transfer_authorization_code_submission_date_long = transfer_authorization_code_submission_date_long  # type: long
        self.user_id = user_id  # type: str
        self.whois_mail_status = whois_mail_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTransferInByInstanceIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.expiration_date_long is not None:
            result['ExpirationDateLong'] = self.expiration_date_long
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modification_date is not None:
            result['ModificationDate'] = self.modification_date
        if self.modification_date_long is not None:
            result['ModificationDateLong'] = self.modification_date_long
        if self.need_mail_check is not None:
            result['NeedMailCheck'] = self.need_mail_check
        if self.progress_bar_type is not None:
            result['ProgressBarType'] = self.progress_bar_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_date is not None:
            result['ResultDate'] = self.result_date
        if self.result_date_long is not None:
            result['ResultDateLong'] = self.result_date_long
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.simple_transfer_in_status is not None:
            result['SimpleTransferInStatus'] = self.simple_transfer_in_status
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_date is not None:
            result['SubmissionDate'] = self.submission_date
        if self.submission_date_long is not None:
            result['SubmissionDateLong'] = self.submission_date_long
        if self.transfer_authorization_code_submission_date is not None:
            result['TransferAuthorizationCodeSubmissionDate'] = self.transfer_authorization_code_submission_date
        if self.transfer_authorization_code_submission_date_long is not None:
            result['TransferAuthorizationCodeSubmissionDateLong'] = self.transfer_authorization_code_submission_date_long
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.whois_mail_status is not None:
            result['WhoisMailStatus'] = self.whois_mail_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('ExpirationDateLong') is not None:
            self.expiration_date_long = m.get('ExpirationDateLong')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModificationDate') is not None:
            self.modification_date = m.get('ModificationDate')
        if m.get('ModificationDateLong') is not None:
            self.modification_date_long = m.get('ModificationDateLong')
        if m.get('NeedMailCheck') is not None:
            self.need_mail_check = m.get('NeedMailCheck')
        if m.get('ProgressBarType') is not None:
            self.progress_bar_type = m.get('ProgressBarType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultDate') is not None:
            self.result_date = m.get('ResultDate')
        if m.get('ResultDateLong') is not None:
            self.result_date_long = m.get('ResultDateLong')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('SimpleTransferInStatus') is not None:
            self.simple_transfer_in_status = m.get('SimpleTransferInStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionDate') is not None:
            self.submission_date = m.get('SubmissionDate')
        if m.get('SubmissionDateLong') is not None:
            self.submission_date_long = m.get('SubmissionDateLong')
        if m.get('TransferAuthorizationCodeSubmissionDate') is not None:
            self.transfer_authorization_code_submission_date = m.get('TransferAuthorizationCodeSubmissionDate')
        if m.get('TransferAuthorizationCodeSubmissionDateLong') is not None:
            self.transfer_authorization_code_submission_date_long = m.get('TransferAuthorizationCodeSubmissionDateLong')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WhoisMailStatus') is not None:
            self.whois_mail_status = m.get('WhoisMailStatus')
        return self


class QueryTransferInByInstanceIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTransferInByInstanceIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTransferInByInstanceIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTransferInByInstanceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTransferInListRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, page_num=None, page_size=None, simple_transfer_in_status=None,
                 submission_end_date=None, submission_start_date=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.simple_transfer_in_status = simple_transfer_in_status  # type: str
        self.submission_end_date = submission_end_date  # type: long
        self.submission_start_date = submission_start_date  # type: long
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTransferInListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.simple_transfer_in_status is not None:
            result['SimpleTransferInStatus'] = self.simple_transfer_in_status
        if self.submission_end_date is not None:
            result['SubmissionEndDate'] = self.submission_end_date
        if self.submission_start_date is not None:
            result['SubmissionStartDate'] = self.submission_start_date
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SimpleTransferInStatus') is not None:
            self.simple_transfer_in_status = m.get('SimpleTransferInStatus')
        if m.get('SubmissionEndDate') is not None:
            self.submission_end_date = m.get('SubmissionEndDate')
        if m.get('SubmissionStartDate') is not None:
            self.submission_start_date = m.get('SubmissionStartDate')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryTransferInListResponseBodyDataTransferInInfo(TeaModel):
    def __init__(self, domain_name=None, email=None, expiration_date=None, expiration_date_long=None,
                 instance_id=None, modification_date=None, modification_date_long=None, need_mail_check=None,
                 progress_bar_type=None, result_code=None, result_date=None, result_date_long=None, result_msg=None,
                 simple_transfer_in_status=None, status=None, submission_date=None, submission_date_long=None,
                 transfer_authorization_code_submission_date=None, transfer_authorization_code_submission_date_long=None, user_id=None,
                 whois_mail_status=None):
        self.domain_name = domain_name  # type: str
        self.email = email  # type: str
        self.expiration_date = expiration_date  # type: str
        self.expiration_date_long = expiration_date_long  # type: long
        self.instance_id = instance_id  # type: str
        self.modification_date = modification_date  # type: str
        self.modification_date_long = modification_date_long  # type: long
        self.need_mail_check = need_mail_check  # type: bool
        self.progress_bar_type = progress_bar_type  # type: int
        self.result_code = result_code  # type: str
        self.result_date = result_date  # type: str
        self.result_date_long = result_date_long  # type: long
        self.result_msg = result_msg  # type: str
        self.simple_transfer_in_status = simple_transfer_in_status  # type: str
        self.status = status  # type: int
        self.submission_date = submission_date  # type: str
        self.submission_date_long = submission_date_long  # type: long
        self.transfer_authorization_code_submission_date = transfer_authorization_code_submission_date  # type: str
        self.transfer_authorization_code_submission_date_long = transfer_authorization_code_submission_date_long  # type: long
        self.user_id = user_id  # type: str
        self.whois_mail_status = whois_mail_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTransferInListResponseBodyDataTransferInInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.expiration_date_long is not None:
            result['ExpirationDateLong'] = self.expiration_date_long
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modification_date is not None:
            result['ModificationDate'] = self.modification_date
        if self.modification_date_long is not None:
            result['ModificationDateLong'] = self.modification_date_long
        if self.need_mail_check is not None:
            result['NeedMailCheck'] = self.need_mail_check
        if self.progress_bar_type is not None:
            result['ProgressBarType'] = self.progress_bar_type
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_date is not None:
            result['ResultDate'] = self.result_date
        if self.result_date_long is not None:
            result['ResultDateLong'] = self.result_date_long
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.simple_transfer_in_status is not None:
            result['SimpleTransferInStatus'] = self.simple_transfer_in_status
        if self.status is not None:
            result['Status'] = self.status
        if self.submission_date is not None:
            result['SubmissionDate'] = self.submission_date
        if self.submission_date_long is not None:
            result['SubmissionDateLong'] = self.submission_date_long
        if self.transfer_authorization_code_submission_date is not None:
            result['TransferAuthorizationCodeSubmissionDate'] = self.transfer_authorization_code_submission_date
        if self.transfer_authorization_code_submission_date_long is not None:
            result['TransferAuthorizationCodeSubmissionDateLong'] = self.transfer_authorization_code_submission_date_long
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.whois_mail_status is not None:
            result['WhoisMailStatus'] = self.whois_mail_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('ExpirationDateLong') is not None:
            self.expiration_date_long = m.get('ExpirationDateLong')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModificationDate') is not None:
            self.modification_date = m.get('ModificationDate')
        if m.get('ModificationDateLong') is not None:
            self.modification_date_long = m.get('ModificationDateLong')
        if m.get('NeedMailCheck') is not None:
            self.need_mail_check = m.get('NeedMailCheck')
        if m.get('ProgressBarType') is not None:
            self.progress_bar_type = m.get('ProgressBarType')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultDate') is not None:
            self.result_date = m.get('ResultDate')
        if m.get('ResultDateLong') is not None:
            self.result_date_long = m.get('ResultDateLong')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('SimpleTransferInStatus') is not None:
            self.simple_transfer_in_status = m.get('SimpleTransferInStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmissionDate') is not None:
            self.submission_date = m.get('SubmissionDate')
        if m.get('SubmissionDateLong') is not None:
            self.submission_date_long = m.get('SubmissionDateLong')
        if m.get('TransferAuthorizationCodeSubmissionDate') is not None:
            self.transfer_authorization_code_submission_date = m.get('TransferAuthorizationCodeSubmissionDate')
        if m.get('TransferAuthorizationCodeSubmissionDateLong') is not None:
            self.transfer_authorization_code_submission_date_long = m.get('TransferAuthorizationCodeSubmissionDateLong')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WhoisMailStatus') is not None:
            self.whois_mail_status = m.get('WhoisMailStatus')
        return self


class QueryTransferInListResponseBodyData(TeaModel):
    def __init__(self, transfer_in_info=None):
        self.transfer_in_info = transfer_in_info  # type: list[QueryTransferInListResponseBodyDataTransferInInfo]

    def validate(self):
        if self.transfer_in_info:
            for k in self.transfer_in_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTransferInListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TransferInInfo'] = []
        if self.transfer_in_info is not None:
            for k in self.transfer_in_info:
                result['TransferInInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.transfer_in_info = []
        if m.get('TransferInInfo') is not None:
            for k in m.get('TransferInInfo'):
                temp_model = QueryTransferInListResponseBodyDataTransferInInfo()
                self.transfer_in_info.append(temp_model.from_map(k))
        return self


class QueryTransferInListResponseBody(TeaModel):
    def __init__(self, current_page_num=None, data=None, next_page=None, page_size=None, pre_page=None,
                 request_id=None, total_item_num=None, total_page_num=None):
        self.current_page_num = current_page_num  # type: int
        self.data = data  # type: QueryTransferInListResponseBodyData
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
        _map = super(QueryTransferInListResponseBody, self).to_map()
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
            temp_model = QueryTransferInListResponseBodyData()
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


class QueryTransferInListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTransferInListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTransferInListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTransferInListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTransferOutInfoRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTransferOutInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class QueryTransferOutInfoResponseBody(TeaModel):
    def __init__(self, email=None, expiration_date=None, pending_request_date=None, request_id=None,
                 result_code=None, result_msg=None, status=None, transfer_authorization_code_send_date=None):
        self.email = email  # type: str
        self.expiration_date = expiration_date  # type: str
        self.pending_request_date = pending_request_date  # type: str
        self.request_id = request_id  # type: str
        self.result_code = result_code  # type: str
        self.result_msg = result_msg  # type: str
        self.status = status  # type: int
        self.transfer_authorization_code_send_date = transfer_authorization_code_send_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTransferOutInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.pending_request_date is not None:
            result['PendingRequestDate'] = self.pending_request_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.status is not None:
            result['Status'] = self.status
        if self.transfer_authorization_code_send_date is not None:
            result['TransferAuthorizationCodeSendDate'] = self.transfer_authorization_code_send_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('PendingRequestDate') is not None:
            self.pending_request_date = m.get('PendingRequestDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransferAuthorizationCodeSendDate') is not None:
            self.transfer_authorization_code_send_date = m.get('TransferAuthorizationCodeSendDate')
        return self


class QueryTransferOutInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTransferOutInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTransferOutInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTransferOutInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegistrantProfileRealNameVerificationRequest(TeaModel):
    def __init__(self, identity_credential=None, identity_credential_no=None, identity_credential_type=None,
                 lang=None, registrant_profile_id=None, user_client_ip=None):
        self.identity_credential = identity_credential  # type: str
        self.identity_credential_no = identity_credential_no  # type: str
        self.identity_credential_type = identity_credential_type  # type: str
        self.lang = lang  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegistrantProfileRealNameVerificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential
        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no
        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileID'] = self.registrant_profile_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')
        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')
        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileID') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileID')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class RegistrantProfileRealNameVerificationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegistrantProfileRealNameVerificationResponseBody, self).to_map()
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


class RegistrantProfileRealNameVerificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RegistrantProfileRealNameVerificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegistrantProfileRealNameVerificationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RegistrantProfileRealNameVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResendEmailVerificationRequest(TeaModel):
    def __init__(self, email=None, lang=None, user_client_ip=None):
        self.email = email  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResendEmailVerificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class ResendEmailVerificationResponseBodyFailList(TeaModel):
    def __init__(self, code=None, email=None, message=None):
        self.code = code  # type: str
        self.email = email  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResendEmailVerificationResponseBodyFailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.email is not None:
            result['Email'] = self.email
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ResendEmailVerificationResponseBodySuccessList(TeaModel):
    def __init__(self, code=None, email=None, message=None):
        self.code = code  # type: str
        self.email = email  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResendEmailVerificationResponseBodySuccessList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.email is not None:
            result['Email'] = self.email
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ResendEmailVerificationResponseBody(TeaModel):
    def __init__(self, fail_list=None, request_id=None, success_list=None):
        self.fail_list = fail_list  # type: list[ResendEmailVerificationResponseBodyFailList]
        self.request_id = request_id  # type: str
        self.success_list = success_list  # type: list[ResendEmailVerificationResponseBodySuccessList]

    def validate(self):
        if self.fail_list:
            for k in self.fail_list:
                if k:
                    k.validate()
        if self.success_list:
            for k in self.success_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ResendEmailVerificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailList'] = []
        if self.fail_list is not None:
            for k in self.fail_list:
                result['FailList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SuccessList'] = []
        if self.success_list is not None:
            for k in self.success_list:
                result['SuccessList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.fail_list = []
        if m.get('FailList') is not None:
            for k in m.get('FailList'):
                temp_model = ResendEmailVerificationResponseBodyFailList()
                self.fail_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.success_list = []
        if m.get('SuccessList') is not None:
            for k in m.get('SuccessList'):
                temp_model = ResendEmailVerificationResponseBodySuccessList()
                self.success_list.append(temp_model.from_map(k))
        return self


class ResendEmailVerificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResendEmailVerificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResendEmailVerificationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResendEmailVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForCreatingOrderActivateRequestOrderActivateParam(TeaModel):
    def __init__(self, address=None, aliyun_dns=None, city=None, country=None, dns_1=None, dns_2=None,
                 domain_name=None, email=None, enable_domain_proxy=None, permit_premium_activation=None, postal_code=None,
                 province=None, registrant_name=None, registrant_organization=None, registrant_profile_id=None,
                 registrant_type=None, subscription_duration=None, tel_area=None, tel_ext=None, telephone=None,
                 trademark_domain_activation=None):
        self.address = address  # type: str
        self.aliyun_dns = aliyun_dns  # type: bool
        self.city = city  # type: str
        self.country = country  # type: str
        self.dns_1 = dns_1  # type: str
        self.dns_2 = dns_2  # type: str
        self.domain_name = domain_name  # type: str
        self.email = email  # type: str
        self.enable_domain_proxy = enable_domain_proxy  # type: bool
        self.permit_premium_activation = permit_premium_activation  # type: bool
        self.postal_code = postal_code  # type: str
        self.province = province  # type: str
        self.registrant_name = registrant_name  # type: str
        self.registrant_organization = registrant_organization  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.registrant_type = registrant_type  # type: str
        self.subscription_duration = subscription_duration  # type: int
        self.tel_area = tel_area  # type: str
        self.tel_ext = tel_ext  # type: str
        self.telephone = telephone  # type: str
        self.trademark_domain_activation = trademark_domain_activation  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderActivateRequestOrderActivateParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.aliyun_dns is not None:
            result['AliyunDns'] = self.aliyun_dns
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.dns_1 is not None:
            result['Dns1'] = self.dns_1
        if self.dns_2 is not None:
            result['Dns2'] = self.dns_2
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.enable_domain_proxy is not None:
            result['EnableDomainProxy'] = self.enable_domain_proxy
        if self.permit_premium_activation is not None:
            result['PermitPremiumActivation'] = self.permit_premium_activation
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.subscription_duration is not None:
            result['SubscriptionDuration'] = self.subscription_duration
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.trademark_domain_activation is not None:
            result['TrademarkDomainActivation'] = self.trademark_domain_activation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AliyunDns') is not None:
            self.aliyun_dns = m.get('AliyunDns')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Dns1') is not None:
            self.dns_1 = m.get('Dns1')
        if m.get('Dns2') is not None:
            self.dns_2 = m.get('Dns2')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EnableDomainProxy') is not None:
            self.enable_domain_proxy = m.get('EnableDomainProxy')
        if m.get('PermitPremiumActivation') is not None:
            self.permit_premium_activation = m.get('PermitPremiumActivation')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('SubscriptionDuration') is not None:
            self.subscription_duration = m.get('SubscriptionDuration')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('TrademarkDomainActivation') is not None:
            self.trademark_domain_activation = m.get('TrademarkDomainActivation')
        return self


class SaveBatchTaskForCreatingOrderActivateRequest(TeaModel):
    def __init__(self, coupon_no=None, lang=None, order_activate_param=None, promotion_no=None, use_coupon=None,
                 use_promotion=None, user_client_ip=None):
        self.coupon_no = coupon_no  # type: str
        self.lang = lang  # type: str
        self.order_activate_param = order_activate_param  # type: list[SaveBatchTaskForCreatingOrderActivateRequestOrderActivateParam]
        self.promotion_no = promotion_no  # type: str
        self.use_coupon = use_coupon  # type: bool
        self.use_promotion = use_promotion  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        if self.order_activate_param:
            for k in self.order_activate_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderActivateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.lang is not None:
            result['Lang'] = self.lang
        result['OrderActivateParam'] = []
        if self.order_activate_param is not None:
            for k in self.order_activate_param:
                result['OrderActivateParam'].append(k.to_map() if k else None)
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        self.order_activate_param = []
        if m.get('OrderActivateParam') is not None:
            for k in m.get('OrderActivateParam'):
                temp_model = SaveBatchTaskForCreatingOrderActivateRequestOrderActivateParam()
                self.order_activate_param.append(temp_model.from_map(k))
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForCreatingOrderActivateResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderActivateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForCreatingOrderActivateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveBatchTaskForCreatingOrderActivateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderActivateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveBatchTaskForCreatingOrderActivateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForCreatingOrderRedeemRequestOrderRedeemParam(TeaModel):
    def __init__(self, current_expiration_date=None, domain_name=None):
        self.current_expiration_date = current_expiration_date  # type: long
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderRedeemRequestOrderRedeemParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_expiration_date is not None:
            result['CurrentExpirationDate'] = self.current_expiration_date
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentExpirationDate') is not None:
            self.current_expiration_date = m.get('CurrentExpirationDate')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class SaveBatchTaskForCreatingOrderRedeemRequest(TeaModel):
    def __init__(self, coupon_no=None, lang=None, order_redeem_param=None, promotion_no=None, use_coupon=None,
                 use_promotion=None, user_client_ip=None):
        self.coupon_no = coupon_no  # type: str
        self.lang = lang  # type: str
        self.order_redeem_param = order_redeem_param  # type: list[SaveBatchTaskForCreatingOrderRedeemRequestOrderRedeemParam]
        self.promotion_no = promotion_no  # type: str
        self.use_coupon = use_coupon  # type: bool
        self.use_promotion = use_promotion  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        if self.order_redeem_param:
            for k in self.order_redeem_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderRedeemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.lang is not None:
            result['Lang'] = self.lang
        result['OrderRedeemParam'] = []
        if self.order_redeem_param is not None:
            for k in self.order_redeem_param:
                result['OrderRedeemParam'].append(k.to_map() if k else None)
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        self.order_redeem_param = []
        if m.get('OrderRedeemParam') is not None:
            for k in m.get('OrderRedeemParam'):
                temp_model = SaveBatchTaskForCreatingOrderRedeemRequestOrderRedeemParam()
                self.order_redeem_param.append(temp_model.from_map(k))
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForCreatingOrderRedeemResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderRedeemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForCreatingOrderRedeemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveBatchTaskForCreatingOrderRedeemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderRedeemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveBatchTaskForCreatingOrderRedeemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForCreatingOrderRenewRequestOrderRenewParam(TeaModel):
    def __init__(self, current_expiration_date=None, domain_name=None, subscription_duration=None):
        self.current_expiration_date = current_expiration_date  # type: long
        self.domain_name = domain_name  # type: str
        self.subscription_duration = subscription_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderRenewRequestOrderRenewParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_expiration_date is not None:
            result['CurrentExpirationDate'] = self.current_expiration_date
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.subscription_duration is not None:
            result['SubscriptionDuration'] = self.subscription_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentExpirationDate') is not None:
            self.current_expiration_date = m.get('CurrentExpirationDate')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('SubscriptionDuration') is not None:
            self.subscription_duration = m.get('SubscriptionDuration')
        return self


class SaveBatchTaskForCreatingOrderRenewRequest(TeaModel):
    def __init__(self, coupon_no=None, lang=None, order_renew_param=None, promotion_no=None, use_coupon=None,
                 use_promotion=None, user_client_ip=None):
        self.coupon_no = coupon_no  # type: str
        self.lang = lang  # type: str
        self.order_renew_param = order_renew_param  # type: list[SaveBatchTaskForCreatingOrderRenewRequestOrderRenewParam]
        self.promotion_no = promotion_no  # type: str
        self.use_coupon = use_coupon  # type: bool
        self.use_promotion = use_promotion  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        if self.order_renew_param:
            for k in self.order_renew_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderRenewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.lang is not None:
            result['Lang'] = self.lang
        result['OrderRenewParam'] = []
        if self.order_renew_param is not None:
            for k in self.order_renew_param:
                result['OrderRenewParam'].append(k.to_map() if k else None)
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        self.order_renew_param = []
        if m.get('OrderRenewParam') is not None:
            for k in m.get('OrderRenewParam'):
                temp_model = SaveBatchTaskForCreatingOrderRenewRequestOrderRenewParam()
                self.order_renew_param.append(temp_model.from_map(k))
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForCreatingOrderRenewResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderRenewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForCreatingOrderRenewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveBatchTaskForCreatingOrderRenewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderRenewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveBatchTaskForCreatingOrderRenewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForCreatingOrderTransferRequestOrderTransferParam(TeaModel):
    def __init__(self, authorization_code=None, domain_name=None, permit_premium_transfer=None,
                 registrant_profile_id=None):
        self.authorization_code = authorization_code  # type: str
        self.domain_name = domain_name  # type: str
        self.permit_premium_transfer = permit_premium_transfer  # type: bool
        self.registrant_profile_id = registrant_profile_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderTransferRequestOrderTransferParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_code is not None:
            result['AuthorizationCode'] = self.authorization_code
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.permit_premium_transfer is not None:
            result['PermitPremiumTransfer'] = self.permit_premium_transfer
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationCode') is not None:
            self.authorization_code = m.get('AuthorizationCode')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PermitPremiumTransfer') is not None:
            self.permit_premium_transfer = m.get('PermitPremiumTransfer')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        return self


class SaveBatchTaskForCreatingOrderTransferRequest(TeaModel):
    def __init__(self, coupon_no=None, lang=None, order_transfer_param=None, promotion_no=None, use_coupon=None,
                 use_promotion=None, user_client_ip=None):
        self.coupon_no = coupon_no  # type: str
        self.lang = lang  # type: str
        self.order_transfer_param = order_transfer_param  # type: list[SaveBatchTaskForCreatingOrderTransferRequestOrderTransferParam]
        self.promotion_no = promotion_no  # type: str
        self.use_coupon = use_coupon  # type: bool
        self.use_promotion = use_promotion  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        if self.order_transfer_param:
            for k in self.order_transfer_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderTransferRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.lang is not None:
            result['Lang'] = self.lang
        result['OrderTransferParam'] = []
        if self.order_transfer_param is not None:
            for k in self.order_transfer_param:
                result['OrderTransferParam'].append(k.to_map() if k else None)
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        self.order_transfer_param = []
        if m.get('OrderTransferParam') is not None:
            for k in m.get('OrderTransferParam'):
                temp_model = SaveBatchTaskForCreatingOrderTransferRequestOrderTransferParam()
                self.order_transfer_param.append(temp_model.from_map(k))
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForCreatingOrderTransferResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderTransferResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForCreatingOrderTransferResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveBatchTaskForCreatingOrderTransferResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForCreatingOrderTransferResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveBatchTaskForCreatingOrderTransferResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForDomainNameProxyServiceRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None, status=None):
        self.domain_name = domain_name  # type: list[str]
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForDomainNameProxyServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class SaveBatchTaskForDomainNameProxyServiceResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForDomainNameProxyServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForDomainNameProxyServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveBatchTaskForDomainNameProxyServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForDomainNameProxyServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveBatchTaskForDomainNameProxyServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForModifyingDomainDnsRequest(TeaModel):
    def __init__(self, aliyun_dns=None, domain_name=None, domain_name_server=None, lang=None, user_client_ip=None):
        self.aliyun_dns = aliyun_dns  # type: bool
        self.domain_name = domain_name  # type: list[str]
        self.domain_name_server = domain_name_server  # type: list[str]
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForModifyingDomainDnsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_dns is not None:
            result['AliyunDns'] = self.aliyun_dns
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_server is not None:
            result['DomainNameServer'] = self.domain_name_server
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunDns') is not None:
            self.aliyun_dns = m.get('AliyunDns')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameServer') is not None:
            self.domain_name_server = m.get('DomainNameServer')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForModifyingDomainDnsResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForModifyingDomainDnsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForModifyingDomainDnsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveBatchTaskForModifyingDomainDnsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForModifyingDomainDnsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveBatchTaskForModifyingDomainDnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForReserveDropListDomainRequestDomains(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForReserveDropListDomainRequestDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class SaveBatchTaskForReserveDropListDomainRequest(TeaModel):
    def __init__(self, contact_template_id=None, domains=None):
        self.contact_template_id = contact_template_id  # type: str
        self.domains = domains  # type: list[SaveBatchTaskForReserveDropListDomainRequestDomains]

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForReserveDropListDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_template_id is not None:
            result['ContactTemplateId'] = self.contact_template_id
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactTemplateId') is not None:
            self.contact_template_id = m.get('ContactTemplateId')
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = SaveBatchTaskForReserveDropListDomainRequestDomains()
                self.domains.append(temp_model.from_map(k))
        return self


class SaveBatchTaskForReserveDropListDomainResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForReserveDropListDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForReserveDropListDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveBatchTaskForReserveDropListDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForReserveDropListDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveBatchTaskForReserveDropListDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForTransferProhibitionLockRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, status=None, user_client_ip=None):
        self.domain_name = domain_name  # type: list[str]
        self.lang = lang  # type: str
        self.status = status  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForTransferProhibitionLockRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForTransferProhibitionLockResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForTransferProhibitionLockResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForTransferProhibitionLockResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveBatchTaskForTransferProhibitionLockResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForTransferProhibitionLockResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveBatchTaskForTransferProhibitionLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForUpdateProhibitionLockRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, status=None, user_client_ip=None):
        self.domain_name = domain_name  # type: list[str]
        self.lang = lang  # type: str
        self.status = status  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForUpdateProhibitionLockRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForUpdateProhibitionLockResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForUpdateProhibitionLockResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForUpdateProhibitionLockResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveBatchTaskForUpdateProhibitionLockResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForUpdateProhibitionLockResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveBatchTaskForUpdateProhibitionLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForUpdatingContactInfoRequest(TeaModel):
    def __init__(self, add_transfer_lock=None, contact_type=None, domain_name=None, lang=None,
                 registrant_profile_id=None, user_client_ip=None):
        self.add_transfer_lock = add_transfer_lock  # type: bool
        self.contact_type = contact_type  # type: str
        self.domain_name = domain_name  # type: list[str]
        self.lang = lang  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForUpdatingContactInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_transfer_lock is not None:
            result['AddTransferLock'] = self.add_transfer_lock
        if self.contact_type is not None:
            result['ContactType'] = self.contact_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddTransferLock') is not None:
            self.add_transfer_lock = m.get('AddTransferLock')
        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForUpdatingContactInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForUpdatingContactInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForUpdatingContactInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveBatchTaskForUpdatingContactInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForUpdatingContactInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveBatchTaskForUpdatingContactInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBatchTaskForUpdatingContactInfoByNewContactRequest(TeaModel):
    def __init__(self, address=None, city=None, contact_type=None, country=None, domain_name=None, email=None,
                 lang=None, postal_code=None, province=None, registrant_name=None, registrant_organization=None,
                 tel_area=None, tel_ext=None, telephone=None, transfer_out_prohibited=None, user_client_ip=None):
        self.address = address  # type: str
        self.city = city  # type: str
        self.contact_type = contact_type  # type: str
        self.country = country  # type: str
        self.domain_name = domain_name  # type: list[str]
        self.email = email  # type: str
        self.lang = lang  # type: str
        self.postal_code = postal_code  # type: str
        self.province = province  # type: str
        self.registrant_name = registrant_name  # type: str
        self.registrant_organization = registrant_organization  # type: str
        self.tel_area = tel_area  # type: str
        self.tel_ext = tel_ext  # type: str
        self.telephone = telephone  # type: str
        self.transfer_out_prohibited = transfer_out_prohibited  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForUpdatingContactInfoByNewContactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.city is not None:
            result['City'] = self.city
        if self.contact_type is not None:
            result['ContactType'] = self.contact_type
        if self.country is not None:
            result['Country'] = self.country
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.transfer_out_prohibited is not None:
            result['TransferOutProhibited'] = self.transfer_out_prohibited
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('TransferOutProhibited') is not None:
            self.transfer_out_prohibited = m.get('TransferOutProhibited')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveBatchTaskForUpdatingContactInfoByNewContactResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveBatchTaskForUpdatingContactInfoByNewContactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveBatchTaskForUpdatingContactInfoByNewContactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveBatchTaskForUpdatingContactInfoByNewContactResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveBatchTaskForUpdatingContactInfoByNewContactResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveBatchTaskForUpdatingContactInfoByNewContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveRegistrantProfileRequest(TeaModel):
    def __init__(self, address=None, city=None, country=None, default_registrant_profile=None, email=None, lang=None,
                 postal_code=None, province=None, registrant_name=None, registrant_organization=None,
                 registrant_profile_id=None, registrant_profile_type=None, registrant_type=None, tel_area=None, tel_ext=None,
                 telephone=None, user_client_ip=None):
        self.address = address  # type: str
        self.city = city  # type: str
        self.country = country  # type: str
        self.default_registrant_profile = default_registrant_profile  # type: bool
        self.email = email  # type: str
        self.lang = lang  # type: str
        self.postal_code = postal_code  # type: str
        self.province = province  # type: str
        self.registrant_name = registrant_name  # type: str
        self.registrant_organization = registrant_organization  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.registrant_profile_type = registrant_profile_type  # type: str
        self.registrant_type = registrant_type  # type: str
        self.tel_area = tel_area  # type: str
        self.tel_ext = tel_ext  # type: str
        self.telephone = telephone  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveRegistrantProfileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.default_registrant_profile is not None:
            result['DefaultRegistrantProfile'] = self.default_registrant_profile
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.registrant_profile_type is not None:
            result['RegistrantProfileType'] = self.registrant_profile_type
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('DefaultRegistrantProfile') is not None:
            self.default_registrant_profile = m.get('DefaultRegistrantProfile')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('RegistrantProfileType') is not None:
            self.registrant_profile_type = m.get('RegistrantProfileType')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveRegistrantProfileResponseBody(TeaModel):
    def __init__(self, registrant_profile_id=None, request_id=None):
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveRegistrantProfileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveRegistrantProfileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveRegistrantProfileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveRegistrantProfileResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveRegistrantProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForAddingDSRecordRequest(TeaModel):
    def __init__(self, algorithm=None, digest=None, digest_type=None, domain_name=None, key_tag=None, lang=None,
                 user_client_ip=None):
        self.algorithm = algorithm  # type: int
        self.digest = digest  # type: str
        self.digest_type = digest_type  # type: int
        self.domain_name = domain_name  # type: str
        self.key_tag = key_tag  # type: int
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForAddingDSRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.digest_type is not None:
            result['DigestType'] = self.digest_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('DigestType') is not None:
            self.digest_type = m.get('DigestType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForAddingDSRecordResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForAddingDSRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForAddingDSRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForAddingDSRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForAddingDSRecordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForAddingDSRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForApprovingTransferOutRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForApprovingTransferOutRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForApprovingTransferOutResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForApprovingTransferOutResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForApprovingTransferOutResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForApprovingTransferOutResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForApprovingTransferOutResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForApprovingTransferOutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForAssociatingEnsRequest(TeaModel):
    def __init__(self, address=None, domain_name=None, lang=None, user_client_ip=None):
        self.address = address  # type: str
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForAssociatingEnsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForAssociatingEnsResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForAssociatingEnsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForAssociatingEnsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForAssociatingEnsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForAssociatingEnsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForAssociatingEnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForCancelingTransferInRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForCancelingTransferInRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForCancelingTransferInResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForCancelingTransferInResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForCancelingTransferInResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForCancelingTransferInResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForCancelingTransferInResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForCancelingTransferInResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForCancelingTransferOutRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForCancelingTransferOutRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForCancelingTransferOutResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForCancelingTransferOutResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForCancelingTransferOutResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForCancelingTransferOutResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForCancelingTransferOutResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForCancelingTransferOutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForCreatingDnsHostRequest(TeaModel):
    def __init__(self, dns_name=None, instance_id=None, ip=None, lang=None, user_client_ip=None):
        self.dns_name = dns_name  # type: str
        self.instance_id = instance_id  # type: str
        self.ip = ip  # type: list[str]
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingDnsHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForCreatingDnsHostResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingDnsHostResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForCreatingDnsHostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForCreatingDnsHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingDnsHostResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForCreatingDnsHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForCreatingOrderActivateRequest(TeaModel):
    def __init__(self, address=None, aliyun_dns=None, city=None, country=None, coupon_no=None, dns_1=None, dns_2=None,
                 domain_name=None, email=None, enable_domain_proxy=None, lang=None, permit_premium_activation=None,
                 postal_code=None, promotion_no=None, province=None, registrant_name=None, registrant_organization=None,
                 registrant_profile_id=None, registrant_type=None, subscription_duration=None, tel_area=None, tel_ext=None,
                 telephone=None, trademark_domain_activation=None, use_coupon=None, use_promotion=None, user_client_ip=None):
        self.address = address  # type: str
        self.aliyun_dns = aliyun_dns  # type: bool
        self.city = city  # type: str
        self.country = country  # type: str
        self.coupon_no = coupon_no  # type: str
        self.dns_1 = dns_1  # type: str
        self.dns_2 = dns_2  # type: str
        self.domain_name = domain_name  # type: str
        self.email = email  # type: str
        self.enable_domain_proxy = enable_domain_proxy  # type: bool
        self.lang = lang  # type: str
        self.permit_premium_activation = permit_premium_activation  # type: bool
        self.postal_code = postal_code  # type: str
        self.promotion_no = promotion_no  # type: str
        self.province = province  # type: str
        self.registrant_name = registrant_name  # type: str
        self.registrant_organization = registrant_organization  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.registrant_type = registrant_type  # type: str
        self.subscription_duration = subscription_duration  # type: int
        self.tel_area = tel_area  # type: str
        self.tel_ext = tel_ext  # type: str
        self.telephone = telephone  # type: str
        self.trademark_domain_activation = trademark_domain_activation  # type: bool
        self.use_coupon = use_coupon  # type: bool
        self.use_promotion = use_promotion  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingOrderActivateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.aliyun_dns is not None:
            result['AliyunDns'] = self.aliyun_dns
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.dns_1 is not None:
            result['Dns1'] = self.dns_1
        if self.dns_2 is not None:
            result['Dns2'] = self.dns_2
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.enable_domain_proxy is not None:
            result['EnableDomainProxy'] = self.enable_domain_proxy
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.permit_premium_activation is not None:
            result['PermitPremiumActivation'] = self.permit_premium_activation
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.province is not None:
            result['Province'] = self.province
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.subscription_duration is not None:
            result['SubscriptionDuration'] = self.subscription_duration
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.trademark_domain_activation is not None:
            result['TrademarkDomainActivation'] = self.trademark_domain_activation
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AliyunDns') is not None:
            self.aliyun_dns = m.get('AliyunDns')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('Dns1') is not None:
            self.dns_1 = m.get('Dns1')
        if m.get('Dns2') is not None:
            self.dns_2 = m.get('Dns2')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EnableDomainProxy') is not None:
            self.enable_domain_proxy = m.get('EnableDomainProxy')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PermitPremiumActivation') is not None:
            self.permit_premium_activation = m.get('PermitPremiumActivation')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('SubscriptionDuration') is not None:
            self.subscription_duration = m.get('SubscriptionDuration')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('TrademarkDomainActivation') is not None:
            self.trademark_domain_activation = m.get('TrademarkDomainActivation')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForCreatingOrderActivateResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingOrderActivateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForCreatingOrderActivateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForCreatingOrderActivateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingOrderActivateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForCreatingOrderActivateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForCreatingOrderRedeemRequest(TeaModel):
    def __init__(self, coupon_no=None, current_expiration_date=None, domain_name=None, lang=None, promotion_no=None,
                 use_coupon=None, use_promotion=None, user_client_ip=None):
        self.coupon_no = coupon_no  # type: str
        self.current_expiration_date = current_expiration_date  # type: long
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.promotion_no = promotion_no  # type: str
        self.use_coupon = use_coupon  # type: bool
        self.use_promotion = use_promotion  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingOrderRedeemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.current_expiration_date is not None:
            result['CurrentExpirationDate'] = self.current_expiration_date
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('CurrentExpirationDate') is not None:
            self.current_expiration_date = m.get('CurrentExpirationDate')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForCreatingOrderRedeemResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingOrderRedeemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForCreatingOrderRedeemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForCreatingOrderRedeemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingOrderRedeemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForCreatingOrderRedeemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForCreatingOrderRenewRequest(TeaModel):
    def __init__(self, coupon_no=None, current_expiration_date=None, domain_name=None, lang=None, promotion_no=None,
                 subscription_duration=None, use_coupon=None, use_promotion=None, user_client_ip=None):
        self.coupon_no = coupon_no  # type: str
        self.current_expiration_date = current_expiration_date  # type: long
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.promotion_no = promotion_no  # type: str
        self.subscription_duration = subscription_duration  # type: int
        self.use_coupon = use_coupon  # type: bool
        self.use_promotion = use_promotion  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingOrderRenewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.current_expiration_date is not None:
            result['CurrentExpirationDate'] = self.current_expiration_date
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.subscription_duration is not None:
            result['SubscriptionDuration'] = self.subscription_duration
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('CurrentExpirationDate') is not None:
            self.current_expiration_date = m.get('CurrentExpirationDate')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('SubscriptionDuration') is not None:
            self.subscription_duration = m.get('SubscriptionDuration')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForCreatingOrderRenewResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingOrderRenewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForCreatingOrderRenewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForCreatingOrderRenewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingOrderRenewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForCreatingOrderRenewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForCreatingOrderTransferRequest(TeaModel):
    def __init__(self, authorization_code=None, coupon_no=None, domain_name=None, lang=None,
                 permit_premium_transfer=None, promotion_no=None, registrant_profile_id=None, use_coupon=None, use_promotion=None,
                 user_client_ip=None):
        self.authorization_code = authorization_code  # type: str
        self.coupon_no = coupon_no  # type: str
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.permit_premium_transfer = permit_premium_transfer  # type: bool
        self.promotion_no = promotion_no  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.use_coupon = use_coupon  # type: bool
        self.use_promotion = use_promotion  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingOrderTransferRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_code is not None:
            result['AuthorizationCode'] = self.authorization_code
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.permit_premium_transfer is not None:
            result['PermitPremiumTransfer'] = self.permit_premium_transfer
        if self.promotion_no is not None:
            result['PromotionNo'] = self.promotion_no
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon
        if self.use_promotion is not None:
            result['UsePromotion'] = self.use_promotion
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationCode') is not None:
            self.authorization_code = m.get('AuthorizationCode')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PermitPremiumTransfer') is not None:
            self.permit_premium_transfer = m.get('PermitPremiumTransfer')
        if m.get('PromotionNo') is not None:
            self.promotion_no = m.get('PromotionNo')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')
        if m.get('UsePromotion') is not None:
            self.use_promotion = m.get('UsePromotion')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForCreatingOrderTransferResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingOrderTransferResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForCreatingOrderTransferResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForCreatingOrderTransferResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForCreatingOrderTransferResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForCreatingOrderTransferResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForDeletingDSRecordRequest(TeaModel):
    def __init__(self, domain_name=None, key_tag=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.key_tag = key_tag  # type: int
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForDeletingDSRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForDeletingDSRecordResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForDeletingDSRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForDeletingDSRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForDeletingDSRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForDeletingDSRecordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForDeletingDSRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForDeletingDnsHostRequest(TeaModel):
    def __init__(self, dns_name=None, instance_id=None, ip=None, lang=None, user_client_ip=None):
        self.dns_name = dns_name  # type: str
        self.instance_id = instance_id  # type: str
        self.ip = ip  # type: list[str]
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForDeletingDnsHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForDeletingDnsHostResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForDeletingDnsHostResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForDeletingDnsHostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForDeletingDnsHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForDeletingDnsHostResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForDeletingDnsHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForDisassociatingEnsRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForDisassociatingEnsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForDisassociatingEnsResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForDisassociatingEnsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForDisassociatingEnsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForDisassociatingEnsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForDisassociatingEnsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForDisassociatingEnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForDomainNameProxyServiceRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, status=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.status = status  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForDomainNameProxyServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForDomainNameProxyServiceResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForDomainNameProxyServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForDomainNameProxyServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForDomainNameProxyServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForDomainNameProxyServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForDomainNameProxyServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForModifyingDSRecordRequest(TeaModel):
    def __init__(self, algorithm=None, digest=None, digest_type=None, domain_name=None, key_tag=None, lang=None,
                 user_client_ip=None):
        self.algorithm = algorithm  # type: int
        self.digest = digest  # type: str
        self.digest_type = digest_type  # type: int
        self.domain_name = domain_name  # type: str
        self.key_tag = key_tag  # type: int
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForModifyingDSRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.digest_type is not None:
            result['DigestType'] = self.digest_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.key_tag is not None:
            result['KeyTag'] = self.key_tag
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('DigestType') is not None:
            self.digest_type = m.get('DigestType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('KeyTag') is not None:
            self.key_tag = m.get('KeyTag')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForModifyingDSRecordResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForModifyingDSRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForModifyingDSRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForModifyingDSRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForModifyingDSRecordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForModifyingDSRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForModifyingDnsHostRequest(TeaModel):
    def __init__(self, dns_name=None, instance_id=None, ip=None, lang=None, user_client_ip=None):
        self.dns_name = dns_name  # type: str
        self.instance_id = instance_id  # type: str
        self.ip = ip  # type: list[str]
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForModifyingDnsHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForModifyingDnsHostResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForModifyingDnsHostResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForModifyingDnsHostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForModifyingDnsHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForModifyingDnsHostResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForModifyingDnsHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForQueryingTransferAuthorizationCodeRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForQueryingTransferAuthorizationCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForQueryingTransferAuthorizationCodeResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForQueryingTransferAuthorizationCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForQueryingTransferAuthorizationCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForQueryingTransferAuthorizationCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForQueryingTransferAuthorizationCodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForQueryingTransferAuthorizationCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForSaveArtExtensionRequest(TeaModel):
    def __init__(self, date_or_period=None, dimensions=None, domain_name=None, features=None,
                 inscriptions_and_markings=None, lang=None, maker=None, materials_and_techniques=None, object_type=None, reference=None,
                 subject=None, title=None):
        self.date_or_period = date_or_period  # type: str
        self.dimensions = dimensions  # type: str
        self.domain_name = domain_name  # type: str
        self.features = features  # type: str
        self.inscriptions_and_markings = inscriptions_and_markings  # type: str
        self.lang = lang  # type: str
        self.maker = maker  # type: str
        self.materials_and_techniques = materials_and_techniques  # type: str
        self.object_type = object_type  # type: str
        self.reference = reference  # type: str
        self.subject = subject  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForSaveArtExtensionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_or_period is not None:
            result['DateOrPeriod'] = self.date_or_period
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.features is not None:
            result['Features'] = self.features
        if self.inscriptions_and_markings is not None:
            result['InscriptionsAndMarkings'] = self.inscriptions_and_markings
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.maker is not None:
            result['Maker'] = self.maker
        if self.materials_and_techniques is not None:
            result['MaterialsAndTechniques'] = self.materials_and_techniques
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.reference is not None:
            result['Reference'] = self.reference
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DateOrPeriod') is not None:
            self.date_or_period = m.get('DateOrPeriod')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('InscriptionsAndMarkings') is not None:
            self.inscriptions_and_markings = m.get('InscriptionsAndMarkings')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Maker') is not None:
            self.maker = m.get('Maker')
        if m.get('MaterialsAndTechniques') is not None:
            self.materials_and_techniques = m.get('MaterialsAndTechniques')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Reference') is not None:
            self.reference = m.get('Reference')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SaveSingleTaskForSaveArtExtensionResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForSaveArtExtensionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForSaveArtExtensionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForSaveArtExtensionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForSaveArtExtensionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForSaveArtExtensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForSynchronizingDSRecordRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForSynchronizingDSRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForSynchronizingDSRecordResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForSynchronizingDSRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForSynchronizingDSRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForSynchronizingDSRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForSynchronizingDSRecordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForSynchronizingDSRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForSynchronizingDnsHostRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, user_client_ip=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForSynchronizingDnsHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForSynchronizingDnsHostResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForSynchronizingDnsHostResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForSynchronizingDnsHostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForSynchronizingDnsHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForSynchronizingDnsHostResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForSynchronizingDnsHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForTransferProhibitionLockRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, status=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.status = status  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForTransferProhibitionLockRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForTransferProhibitionLockResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForTransferProhibitionLockResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForTransferProhibitionLockResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForTransferProhibitionLockResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForTransferProhibitionLockResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForTransferProhibitionLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForUpdateProhibitionLockRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, status=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.status = status  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForUpdateProhibitionLockRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForUpdateProhibitionLockResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForUpdateProhibitionLockResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForUpdateProhibitionLockResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForUpdateProhibitionLockResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForUpdateProhibitionLockResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForUpdateProhibitionLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveSingleTaskForUpdatingContactInfoRequest(TeaModel):
    def __init__(self, add_transfer_lock=None, contact_type=None, domain_name=None, instance_id=None, lang=None,
                 registrant_profile_id=None, user_client_ip=None):
        self.add_transfer_lock = add_transfer_lock  # type: bool
        self.contact_type = contact_type  # type: str
        self.domain_name = domain_name  # type: str
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForUpdatingContactInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_transfer_lock is not None:
            result['AddTransferLock'] = self.add_transfer_lock
        if self.contact_type is not None:
            result['ContactType'] = self.contact_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddTransferLock') is not None:
            self.add_transfer_lock = m.get('AddTransferLock')
        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveSingleTaskForUpdatingContactInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveSingleTaskForUpdatingContactInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveSingleTaskForUpdatingContactInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveSingleTaskForUpdatingContactInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveSingleTaskForUpdatingContactInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveSingleTaskForUpdatingContactInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskForSubmittingDomainDeleteRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, user_client_ip=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskForSubmittingDomainDeleteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveTaskForSubmittingDomainDeleteResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskForSubmittingDomainDeleteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveTaskForSubmittingDomainDeleteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveTaskForSubmittingDomainDeleteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveTaskForSubmittingDomainDeleteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveTaskForSubmittingDomainDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest(TeaModel):
    def __init__(self, domain_name=None, identity_credential=None, identity_credential_no=None,
                 identity_credential_type=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: list[str]
        self.identity_credential = identity_credential  # type: str
        self.identity_credential_no = identity_credential_no  # type: str
        self.identity_credential_type = identity_credential_type  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential
        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no
        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')
        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')
        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest(TeaModel):
    def __init__(self, domain_name=None, instance_id=None, lang=None, registrant_profile_id=None,
                 user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest(TeaModel):
    def __init__(self, address=None, city=None, country=None, domain_name=None, email=None, identity_credential=None,
                 identity_credential_no=None, identity_credential_type=None, lang=None, postal_code=None, province=None,
                 registrant_name=None, registrant_organization=None, registrant_type=None, tel_area=None, tel_ext=None,
                 telephone=None, transfer_out_prohibited=None, user_client_ip=None):
        self.address = address  # type: str
        self.city = city  # type: str
        self.country = country  # type: str
        self.domain_name = domain_name  # type: list[str]
        self.email = email  # type: str
        self.identity_credential = identity_credential  # type: str
        self.identity_credential_no = identity_credential_no  # type: str
        self.identity_credential_type = identity_credential_type  # type: str
        self.lang = lang  # type: str
        self.postal_code = postal_code  # type: str
        self.province = province  # type: str
        self.registrant_name = registrant_name  # type: str
        self.registrant_organization = registrant_organization  # type: str
        self.registrant_type = registrant_type  # type: str
        self.tel_area = tel_area  # type: str
        self.tel_ext = tel_ext  # type: str
        self.telephone = telephone  # type: str
        self.transfer_out_prohibited = transfer_out_prohibited  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential
        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no
        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.transfer_out_prohibited is not None:
            result['TransferOutProhibited'] = self.transfer_out_prohibited
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')
        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')
        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('TransferOutProhibited') is not None:
            self.transfer_out_prohibited = m.get('TransferOutProhibited')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, registrant_profile_id=None, transfer_out_prohibited=None,
                 user_client_ip=None):
        self.domain_name = domain_name  # type: list[str]
        self.lang = lang  # type: str
        self.registrant_profile_id = registrant_profile_id  # type: long
        self.transfer_out_prohibited = transfer_out_prohibited  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id
        if self.transfer_out_prohibited is not None:
            result['TransferOutProhibited'] = self.transfer_out_prohibited
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')
        if m.get('TransferOutProhibited') is not None:
            self.transfer_out_prohibited = m.get('TransferOutProhibited')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponseBody(TeaModel):
    def __init__(self, request_id=None, task_no=None):
        self.request_id = request_id  # type: str
        self.task_no = task_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_no is not None:
            result['TaskNo'] = self.task_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')
        return self


class SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitEmailVerificationRequest(TeaModel):
    def __init__(self, email=None, lang=None, send_if_exist=None, user_client_ip=None):
        self.email = email  # type: str
        self.lang = lang  # type: str
        self.send_if_exist = send_if_exist  # type: bool
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitEmailVerificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.send_if_exist is not None:
            result['SendIfExist'] = self.send_if_exist
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SendIfExist') is not None:
            self.send_if_exist = m.get('SendIfExist')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SubmitEmailVerificationResponseBodyExistList(TeaModel):
    def __init__(self, code=None, email=None, message=None):
        self.code = code  # type: str
        self.email = email  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitEmailVerificationResponseBodyExistList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.email is not None:
            result['Email'] = self.email
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SubmitEmailVerificationResponseBodyFailList(TeaModel):
    def __init__(self, code=None, email=None, message=None):
        self.code = code  # type: str
        self.email = email  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitEmailVerificationResponseBodyFailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.email is not None:
            result['Email'] = self.email
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SubmitEmailVerificationResponseBodySuccessList(TeaModel):
    def __init__(self, code=None, email=None, message=None):
        self.code = code  # type: str
        self.email = email  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitEmailVerificationResponseBodySuccessList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.email is not None:
            result['Email'] = self.email
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SubmitEmailVerificationResponseBody(TeaModel):
    def __init__(self, exist_list=None, fail_list=None, request_id=None, success_list=None):
        self.exist_list = exist_list  # type: list[SubmitEmailVerificationResponseBodyExistList]
        self.fail_list = fail_list  # type: list[SubmitEmailVerificationResponseBodyFailList]
        self.request_id = request_id  # type: str
        self.success_list = success_list  # type: list[SubmitEmailVerificationResponseBodySuccessList]

    def validate(self):
        if self.exist_list:
            for k in self.exist_list:
                if k:
                    k.validate()
        if self.fail_list:
            for k in self.fail_list:
                if k:
                    k.validate()
        if self.success_list:
            for k in self.success_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SubmitEmailVerificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExistList'] = []
        if self.exist_list is not None:
            for k in self.exist_list:
                result['ExistList'].append(k.to_map() if k else None)
        result['FailList'] = []
        if self.fail_list is not None:
            for k in self.fail_list:
                result['FailList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SuccessList'] = []
        if self.success_list is not None:
            for k in self.success_list:
                result['SuccessList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.exist_list = []
        if m.get('ExistList') is not None:
            for k in m.get('ExistList'):
                temp_model = SubmitEmailVerificationResponseBodyExistList()
                self.exist_list.append(temp_model.from_map(k))
        self.fail_list = []
        if m.get('FailList') is not None:
            for k in m.get('FailList'):
                temp_model = SubmitEmailVerificationResponseBodyFailList()
                self.fail_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.success_list = []
        if m.get('SuccessList') is not None:
            for k in m.get('SuccessList'):
                temp_model = SubmitEmailVerificationResponseBodySuccessList()
                self.success_list.append(temp_model.from_map(k))
        return self


class SubmitEmailVerificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitEmailVerificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitEmailVerificationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitEmailVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferInCheckMailTokenRequest(TeaModel):
    def __init__(self, lang=None, token=None, user_client_ip=None):
        self.lang = lang  # type: str
        self.token = token  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferInCheckMailTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.token is not None:
            result['Token'] = self.token
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class TransferInCheckMailTokenResponseBodyFailList(TeaModel):
    def __init__(self, fail_domain=None):
        self.fail_domain = fail_domain  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferInCheckMailTokenResponseBodyFailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_domain is not None:
            result['FailDomain'] = self.fail_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailDomain') is not None:
            self.fail_domain = m.get('FailDomain')
        return self


class TransferInCheckMailTokenResponseBodySuccessList(TeaModel):
    def __init__(self, success_domain=None):
        self.success_domain = success_domain  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferInCheckMailTokenResponseBodySuccessList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success_domain is not None:
            result['SuccessDomain'] = self.success_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SuccessDomain') is not None:
            self.success_domain = m.get('SuccessDomain')
        return self


class TransferInCheckMailTokenResponseBody(TeaModel):
    def __init__(self, fail_list=None, request_id=None, success_list=None):
        self.fail_list = fail_list  # type: TransferInCheckMailTokenResponseBodyFailList
        self.request_id = request_id  # type: str
        self.success_list = success_list  # type: TransferInCheckMailTokenResponseBodySuccessList

    def validate(self):
        if self.fail_list:
            self.fail_list.validate()
        if self.success_list:
            self.success_list.validate()

    def to_map(self):
        _map = super(TransferInCheckMailTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_list is not None:
            result['FailList'] = self.fail_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_list is not None:
            result['SuccessList'] = self.success_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailList') is not None:
            temp_model = TransferInCheckMailTokenResponseBodyFailList()
            self.fail_list = temp_model.from_map(m['FailList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessList') is not None:
            temp_model = TransferInCheckMailTokenResponseBodySuccessList()
            self.success_list = temp_model.from_map(m['SuccessList'])
        return self


class TransferInCheckMailTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TransferInCheckMailTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferInCheckMailTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TransferInCheckMailTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferInReenterTransferAuthorizationCodeRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, transfer_authorization_code=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.transfer_authorization_code = transfer_authorization_code  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferInReenterTransferAuthorizationCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.transfer_authorization_code is not None:
            result['TransferAuthorizationCode'] = self.transfer_authorization_code
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TransferAuthorizationCode') is not None:
            self.transfer_authorization_code = m.get('TransferAuthorizationCode')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class TransferInReenterTransferAuthorizationCodeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferInReenterTransferAuthorizationCodeResponseBody, self).to_map()
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


class TransferInReenterTransferAuthorizationCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TransferInReenterTransferAuthorizationCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferInReenterTransferAuthorizationCodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TransferInReenterTransferAuthorizationCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferInRefetchWhoisEmailRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferInRefetchWhoisEmailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class TransferInRefetchWhoisEmailResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferInRefetchWhoisEmailResponseBody, self).to_map()
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


class TransferInRefetchWhoisEmailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TransferInRefetchWhoisEmailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferInRefetchWhoisEmailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TransferInRefetchWhoisEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferInResendMailTokenRequest(TeaModel):
    def __init__(self, domain_name=None, lang=None, user_client_ip=None):
        self.domain_name = domain_name  # type: str
        self.lang = lang  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferInResendMailTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class TransferInResendMailTokenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferInResendMailTokenResponseBody, self).to_map()
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


class TransferInResendMailTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TransferInResendMailTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferInResendMailTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TransferInResendMailTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyContactFieldRequest(TeaModel):
    def __init__(self, address=None, city=None, country=None, domain_name=None, email=None, lang=None,
                 postal_code=None, province=None, registrant_name=None, registrant_organization=None, registrant_type=None,
                 tel_area=None, tel_ext=None, telephone=None, user_client_ip=None):
        self.address = address  # type: str
        self.city = city  # type: str
        self.country = country  # type: str
        self.domain_name = domain_name  # type: str
        self.email = email  # type: str
        self.lang = lang  # type: str
        self.postal_code = postal_code  # type: str
        self.province = province  # type: str
        self.registrant_name = registrant_name  # type: str
        self.registrant_organization = registrant_organization  # type: str
        self.registrant_type = registrant_type  # type: str
        self.tel_area = tel_area  # type: str
        self.tel_ext = tel_ext  # type: str
        self.telephone = telephone  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyContactFieldRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name
        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization
        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type
        if self.tel_area is not None:
            result['TelArea'] = self.tel_area
        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')
        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')
        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')
        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')
        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class VerifyContactFieldResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyContactFieldResponseBody, self).to_map()
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


class VerifyContactFieldResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyContactFieldResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyContactFieldResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VerifyContactFieldResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyEmailRequest(TeaModel):
    def __init__(self, lang=None, token=None, user_client_ip=None):
        self.lang = lang  # type: str
        self.token = token  # type: str
        self.user_client_ip = user_client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyEmailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.token is not None:
            result['Token'] = self.token
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


