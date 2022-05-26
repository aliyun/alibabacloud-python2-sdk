# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class EnrollAccountRequestBaselineItems(TeaModel):
    def __init__(self, config=None, name=None, skip=None, version=None):
        # 基线项配置
        self.config = config  # type: str
        # 基线项名称
        self.name = name  # type: str
        # 是否跳过基线项
        self.skip = skip  # type: bool
        # 基线项版本
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnrollAccountRequestBaselineItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.skip is not None:
            result['Skip'] = self.skip
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Skip') is not None:
            self.skip = m.get('Skip')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class EnrollAccountRequest(TeaModel):
    def __init__(self, account_name_prefix=None, account_uid=None, baseline_items=None, display_name=None,
                 folder_id=None, payer_account_uid=None, region_id=None):
        # 账号名称前缀
        self.account_name_prefix = account_name_prefix  # type: str
        # 注册账号ID
        self.account_uid = account_uid  # type: long
        # 基线项配置数组
        self.baseline_items = baseline_items  # type: list[EnrollAccountRequestBaselineItems]
        # 账号显示名称
        self.display_name = display_name  # type: str
        # 父资源夹ID
        self.folder_id = folder_id  # type: str
        # 结算账号ID
        self.payer_account_uid = payer_account_uid  # type: long
        # RegionId
        self.region_id = region_id  # type: str

    def validate(self):
        if self.baseline_items:
            for k in self.baseline_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(EnrollAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name_prefix is not None:
            result['AccountNamePrefix'] = self.account_name_prefix
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k in self.baseline_items:
                result['BaselineItems'].append(k.to_map() if k else None)
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.payer_account_uid is not None:
            result['PayerAccountUid'] = self.payer_account_uid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountNamePrefix') is not None:
            self.account_name_prefix = m.get('AccountNamePrefix')
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k in m.get('BaselineItems'):
                temp_model = EnrollAccountRequestBaselineItems()
                self.baseline_items.append(temp_model.from_map(k))
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('PayerAccountUid') is not None:
            self.payer_account_uid = m.get('PayerAccountUid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnrollAccountResponseBody(TeaModel):
    def __init__(self, account_uid=None, request_id=None):
        # 注册账号ID
        self.account_uid = account_uid  # type: long
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnrollAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnrollAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnrollAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnrollAccountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnrollAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnrolledAccountRequest(TeaModel):
    def __init__(self, account_uid=None, region_id=None):
        # 账号ID
        self.account_uid = account_uid  # type: long
        # RegionId
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnrolledAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetEnrolledAccountResponseBodyErrorInfo(TeaModel):
    def __init__(self, code=None, message=None, recommend=None, request_id=None):
        # 错误码
        self.code = code  # type: str
        # 错误信息
        self.message = message  # type: str
        # 错误处理建议
        self.recommend = recommend  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnrolledAccountResponseBodyErrorInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.recommend is not None:
            result['Recommend'] = self.recommend
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Recommend') is not None:
            self.recommend = m.get('Recommend')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEnrolledAccountResponseBodyInputsBaselineItems(TeaModel):
    def __init__(self, config=None, name=None, skip=None, version=None):
        # 基线项配置
        self.config = config  # type: str
        # 基线项名称
        self.name = name  # type: str
        # 是否跳过基线项
        self.skip = skip  # type: bool
        # 基线项版本
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnrolledAccountResponseBodyInputsBaselineItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.skip is not None:
            result['Skip'] = self.skip
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Skip') is not None:
            self.skip = m.get('Skip')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetEnrolledAccountResponseBodyInputs(TeaModel):
    def __init__(self, account_name_prefix=None, account_uid=None, baseline_items=None, display_name=None,
                 folder_id=None, payer_account_uid=None):
        # 账号名称前缀
        self.account_name_prefix = account_name_prefix  # type: str
        # 账号ID
        self.account_uid = account_uid  # type: long
        # 基线项配置数组
        self.baseline_items = baseline_items  # type: list[GetEnrolledAccountResponseBodyInputsBaselineItems]
        # 账号展示名称
        self.display_name = display_name  # type: str
        # 父资源夹ID
        self.folder_id = folder_id  # type: str
        # 结算账号ID
        self.payer_account_uid = payer_account_uid  # type: long

    def validate(self):
        if self.baseline_items:
            for k in self.baseline_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEnrolledAccountResponseBodyInputs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name_prefix is not None:
            result['AccountNamePrefix'] = self.account_name_prefix
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k in self.baseline_items:
                result['BaselineItems'].append(k.to_map() if k else None)
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.payer_account_uid is not None:
            result['PayerAccountUid'] = self.payer_account_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountNamePrefix') is not None:
            self.account_name_prefix = m.get('AccountNamePrefix')
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k in m.get('BaselineItems'):
                temp_model = GetEnrolledAccountResponseBodyInputsBaselineItems()
                self.baseline_items.append(temp_model.from_map(k))
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('PayerAccountUid') is not None:
            self.payer_account_uid = m.get('PayerAccountUid')
        return self


class GetEnrolledAccountResponseBodyProgress(TeaModel):
    def __init__(self, name=None, status=None):
        # 基线项名称
        self.name = name  # type: str
        # 基线项实施状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnrolledAccountResponseBodyProgress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetEnrolledAccountResponseBody(TeaModel):
    def __init__(self, account_uid=None, create_time=None, display_name=None, error_info=None, folder_id=None,
                 initialized=None, inputs=None, master_account_uid=None, payer_account_uid=None, progress=None, request_id=None,
                 status=None, update_time=None):
        # 账号ID
        self.account_uid = account_uid  # type: long
        # 创建时间
        self.create_time = create_time  # type: str
        # 账号显示名称
        self.display_name = display_name  # type: str
        # 错误信息
        self.error_info = error_info  # type: GetEnrolledAccountResponseBodyErrorInfo
        # 父资源夹ID
        self.folder_id = folder_id  # type: str
        # 是否初始化完成
        self.initialized = initialized  # type: bool
        # 注册账号时的输入参数
        self.inputs = inputs  # type: GetEnrolledAccountResponseBodyInputs
        # 所属的Master账号ID
        self.master_account_uid = master_account_uid  # type: long
        # 结算账号ID
        self.payer_account_uid = payer_account_uid  # type: long
        # 基线实施进度
        self.progress = progress  # type: list[GetEnrolledAccountResponseBodyProgress]
        # 请求ID
        self.request_id = request_id  # type: str
        # 账号注册状态
        self.status = status  # type: str
        # 更新时间
        self.update_time = update_time  # type: str

    def validate(self):
        if self.error_info:
            self.error_info.validate()
        if self.inputs:
            self.inputs.validate()
        if self.progress:
            for k in self.progress:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEnrolledAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info.to_map()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.initialized is not None:
            result['Initialized'] = self.initialized
        if self.inputs is not None:
            result['Inputs'] = self.inputs.to_map()
        if self.master_account_uid is not None:
            result['MasterAccountUid'] = self.master_account_uid
        if self.payer_account_uid is not None:
            result['PayerAccountUid'] = self.payer_account_uid
        result['Progress'] = []
        if self.progress is not None:
            for k in self.progress:
                result['Progress'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ErrorInfo') is not None:
            temp_model = GetEnrolledAccountResponseBodyErrorInfo()
            self.error_info = temp_model.from_map(m['ErrorInfo'])
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('Initialized') is not None:
            self.initialized = m.get('Initialized')
        if m.get('Inputs') is not None:
            temp_model = GetEnrolledAccountResponseBodyInputs()
            self.inputs = temp_model.from_map(m['Inputs'])
        if m.get('MasterAccountUid') is not None:
            self.master_account_uid = m.get('MasterAccountUid')
        if m.get('PayerAccountUid') is not None:
            self.payer_account_uid = m.get('PayerAccountUid')
        self.progress = []
        if m.get('Progress') is not None:
            for k in m.get('Progress'):
                temp_model = GetEnrolledAccountResponseBodyProgress()
                self.progress.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetEnrolledAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEnrolledAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnrolledAccountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEnrolledAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnrolledAccountsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_id=None):
        # 每页的最大数据条数
        self.max_results = max_results  # type: int
        # 查询返回结果下一页的令牌。首次调用API不需要NextToken
        self.next_token = next_token  # type: str
        # RegionId
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnrolledAccountsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListEnrolledAccountsResponseBodyEnrolledAccounts(TeaModel):
    def __init__(self, account_uid=None, create_time=None, display_name=None, folder_id=None,
                 payer_account_uid=None, status=None, update_time=None):
        # 账号ID
        self.account_uid = account_uid  # type: long
        # 创建时间
        self.create_time = create_time  # type: str
        # 账号显示名称
        self.display_name = display_name  # type: str
        # 父资源夹ID
        self.folder_id = folder_id  # type: str
        # 结算账号ID
        self.payer_account_uid = payer_account_uid  # type: long
        # 创建状态
        self.status = status  # type: str
        # 更新时间
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnrolledAccountsResponseBodyEnrolledAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.payer_account_uid is not None:
            result['PayerAccountUid'] = self.payer_account_uid
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('PayerAccountUid') is not None:
            self.payer_account_uid = m.get('PayerAccountUid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListEnrolledAccountsResponseBody(TeaModel):
    def __init__(self, enrolled_accounts=None, next_token=None, request_id=None):
        # 账号列表
        self.enrolled_accounts = enrolled_accounts  # type: list[ListEnrolledAccountsResponseBodyEnrolledAccounts]
        # 查询返回结果下一页的令牌
        self.next_token = next_token  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        if self.enrolled_accounts:
            for k in self.enrolled_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnrolledAccountsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EnrolledAccounts'] = []
        if self.enrolled_accounts is not None:
            for k in self.enrolled_accounts:
                result['EnrolledAccounts'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.enrolled_accounts = []
        if m.get('EnrolledAccounts') is not None:
            for k in m.get('EnrolledAccounts'):
                temp_model = ListEnrolledAccountsResponseBodyEnrolledAccounts()
                self.enrolled_accounts.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEnrolledAccountsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEnrolledAccountsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnrolledAccountsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEnrolledAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


