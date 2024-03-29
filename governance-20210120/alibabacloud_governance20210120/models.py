# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class EnrollAccountRequestBaselineItems(TeaModel):
    def __init__(self, config=None, name=None, skip=None, version=None):
        # The configurations of the baseline item.
        self.config = config  # type: str
        # The name of the baseline item.
        self.name = name  # type: str
        # Specifies whether to skip the baseline item. Valid values:
        # 
        # *   false: The baseline item is not skipped.
        # *   true: The baseline item is skipped.
        self.skip = skip  # type: bool
        # The version of the baseline item.
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
    def __init__(self, account_name_prefix=None, account_uid=None, baseline_id=None, baseline_items=None,
                 display_name=None, folder_id=None, payer_account_uid=None, region_id=None, resell_account_type=None):
        # The prefix for the account name of the member.
        # 
        # *   If the account baseline is applied to an account that is newly created, you must configure this parameter.
        # *   If the account baseline is applied to an existing account, you do not need to configure this parameter.
        self.account_name_prefix = account_name_prefix  # type: str
        # The account ID.
        # 
        # *   If the account baseline is applied to an account that is newly created, you do not need to configure this parameter.
        # *   If the account baseline is applied to an existing account, you must configure this parameter.
        self.account_uid = account_uid  # type: long
        # The baseline ID.
        # 
        # If this parameter is left empty, the default baseline is used.
        self.baseline_id = baseline_id  # type: str
        # An array that contains baseline items.
        # 
        # If this parameter is specified, the configurations of the baseline items are merged with the baseline of the specified account. The configurations of the same baseline items are subject to the configuration of this parameter. We recommend that you leave this parameter empty and configure the `BaselineId` parameter to specify an account baseline and apply the configuration of the account baseline to the account.
        self.baseline_items = baseline_items  # type: list[EnrollAccountRequestBaselineItems]
        # The display name of the account.
        # 
        # *   If the account baseline is applied to an account that is newly created, you must configure this parameter.
        # *   If the account baseline is applied to an existing account, you do not need to configure this parameter.
        self.display_name = display_name  # type: str
        # The ID of the parent folder.
        # 
        # *   If the account baseline is applied to an account that is newly created, you need to specify a parent folder. If you do not configure this parameter, the account is created in the Root folder.
        # *   If the account baseline is applied to an existing account, you do not need to configure this parameter.
        self.folder_id = folder_id  # type: str
        # The ID of the billing account.
        # 
        # *   If the account baseline is applied to an account that is newly created, you need to specify a billing account. If you do not configure this parameter, the self-pay settlement method is used for the account.
        # *   If the account baseline is applied to an existing account, you do not need to configure this parameter.
        self.payer_account_uid = payer_account_uid  # type: long
        # The region ID.
        self.region_id = region_id  # type: str
        # The identity type of the member. Valid values:
        # 
        # *   resell (default): The member is an account for a reseller. A relationship is automatically established between the member and the reseller. The management account of the resource directory must be used as the billing account of the member.
        # *   non_resell: The member is not an account for a reseller. The member is an account that is not associated with a reseller. You can directly use the account to purchase Alibaba Cloud resources. The member is used as its own billing account.
        # 
        # > This parameter is available only for resellers at the international site (alibabacloud.com).
        self.resell_account_type = resell_account_type  # type: str

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
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
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
        if self.resell_account_type is not None:
            result['ResellAccountType'] = self.resell_account_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountNamePrefix') is not None:
            self.account_name_prefix = m.get('AccountNamePrefix')
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
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
        if m.get('ResellAccountType') is not None:
            self.resell_account_type = m.get('ResellAccountType')
        return self


class EnrollAccountResponseBody(TeaModel):
    def __init__(self, account_uid=None, request_id=None):
        # The account ID.
        self.account_uid = account_uid  # type: long
        # The request ID.
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


class GetAccountFactoryBaselineRequest(TeaModel):
    def __init__(self, baseline_id=None, region_id=None):
        # The baseline ID.
        self.baseline_id = baseline_id  # type: str
        # The region ID.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountFactoryBaselineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAccountFactoryBaselineResponseBodyBaselineItems(TeaModel):
    def __init__(self, config=None, name=None, version=None):
        # The configuration of the baseline item.
        # 
        # The value is a JSON string.
        self.config = config  # type: str
        # The name of the baseline item.
        self.name = name  # type: str
        # The version of the baseline item.
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountFactoryBaselineResponseBodyBaselineItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetAccountFactoryBaselineResponseBody(TeaModel):
    def __init__(self, baseline_id=None, baseline_items=None, baseline_name=None, create_time=None,
                 description=None, request_id=None, type=None, update_time=None):
        # The baseline ID.
        self.baseline_id = baseline_id  # type: str
        # The baseline items.
        self.baseline_items = baseline_items  # type: list[GetAccountFactoryBaselineResponseBodyBaselineItems]
        # The name of the baseline.
        self.baseline_name = baseline_name  # type: str
        # The time when the baseline was created.
        self.create_time = create_time  # type: str
        # The description of the baseline.
        self.description = description  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The type of the baseline. Valid values:
        # 
        # *   System: default baseline.
        # *   Custom: custom baseline.
        self.type = type  # type: str
        # The time when the baseline was updated.
        self.update_time = update_time  # type: str

    def validate(self):
        if self.baseline_items:
            for k in self.baseline_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAccountFactoryBaselineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k in self.baseline_items:
                result['BaselineItems'].append(k.to_map() if k else None)
        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k in m.get('BaselineItems'):
                temp_model = GetAccountFactoryBaselineResponseBodyBaselineItems()
                self.baseline_items.append(temp_model.from_map(k))
        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetAccountFactoryBaselineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccountFactoryBaselineResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccountFactoryBaselineResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAccountFactoryBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnrolledAccountRequest(TeaModel):
    def __init__(self, account_uid=None, region_id=None):
        # The account ID.
        self.account_uid = account_uid  # type: long
        # The region ID.
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


class GetEnrolledAccountResponseBodyBaselineItems(TeaModel):
    def __init__(self, config=None, name=None, skip=None, version=None):
        self.config = config  # type: str
        self.name = name  # type: str
        self.skip = skip  # type: bool
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnrolledAccountResponseBodyBaselineItems, self).to_map()
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


class GetEnrolledAccountResponseBodyErrorInfo(TeaModel):
    def __init__(self, code=None, message=None, recommend=None, request_id=None):
        # The error code returned.
        self.code = code  # type: str
        # The error message returned.
        self.message = message  # type: str
        # The suggestions that are used to resolve the issue.
        self.recommend = recommend  # type: str
        # The request ID.
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
        # The configurations of the baseline item.
        self.config = config  # type: str
        # The name of the baseline item.
        self.name = name  # type: str
        # Indicates whether to skip the baseline item.
        self.skip = skip  # type: bool
        # The version of the baseline item.
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
        # The prefix for the account name of the member.
        self.account_name_prefix = account_name_prefix  # type: str
        # The account ID.
        self.account_uid = account_uid  # type: long
        # An array that contains baseline items.
        self.baseline_items = baseline_items  # type: list[GetEnrolledAccountResponseBodyInputsBaselineItems]
        # The display name of the account.
        self.display_name = display_name  # type: str
        # The ID of the parent folder.
        self.folder_id = folder_id  # type: str
        # The ID of the billing account.
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
        # The name of the baseline item.
        self.name = name  # type: str
        # The status of applying the account baseline to the account. Valid values:
        # 
        # *   Pending: The account is waiting to be created.
        # *   Running: The account baseline is being applied to the account.
        # *   Finished: The account baseline is applied to the account.
        # *   Failed: The account baseline failed to be applied to the account.
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
    def __init__(self, account_uid=None, baseline_id=None, baseline_items=None, create_time=None, display_name=None,
                 error_info=None, folder_id=None, initialized=None, inputs=None, master_account_uid=None,
                 payer_account_uid=None, progress=None, request_id=None, status=None, update_time=None):
        # The account ID.
        self.account_uid = account_uid  # type: long
        # The ID of the baseline that was applied to the account.
        self.baseline_id = baseline_id  # type: str
        self.baseline_items = baseline_items  # type: list[GetEnrolledAccountResponseBodyBaselineItems]
        # The time at which the account was created.
        self.create_time = create_time  # type: str
        # The display name of the account.
        self.display_name = display_name  # type: str
        # The error message returned.
        self.error_info = error_info  # type: GetEnrolledAccountResponseBodyErrorInfo
        # The ID of the parent folder.
        self.folder_id = folder_id  # type: str
        # Indicates whether the account was initialized.
        self.initialized = initialized  # type: bool
        # The input parameters that are used when you enrolled the account.
        self.inputs = inputs  # type: GetEnrolledAccountResponseBodyInputs
        # The ID of the master account to which the account belongs.
        self.master_account_uid = master_account_uid  # type: long
        # The ID of the billing account.
        self.payer_account_uid = payer_account_uid  # type: long
        # The progress of applying the account baseline to the account.
        self.progress = progress  # type: list[GetEnrolledAccountResponseBodyProgress]
        # The request ID.
        self.request_id = request_id  # type: str
        # The creation status of the account. Valid values:
        # 
        # *   Pending: The account is waiting to be created.
        # *   Running: The account is being created.
        # *   Finished: The account is created.
        # *   Failed: The account failed to be created.
        # *   Scheduling: The account is being scheduled.
        # *   ScheduleFailed: The account failed to be scheduled.
        self.status = status  # type: str
        # The time when the information about the account was updated.
        self.update_time = update_time  # type: str

    def validate(self):
        if self.baseline_items:
            for k in self.baseline_items:
                if k:
                    k.validate()
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
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k in self.baseline_items:
                result['BaselineItems'].append(k.to_map() if k else None)
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
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k in m.get('BaselineItems'):
                temp_model = GetEnrolledAccountResponseBodyBaselineItems()
                self.baseline_items.append(temp_model.from_map(k))
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


class ListAccountFactoryBaselinesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_id=None):
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token  # type: str
        # RegionId
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccountFactoryBaselinesRequest, self).to_map()
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


class ListAccountFactoryBaselinesResponseBodyBaselines(TeaModel):
    def __init__(self, baseline_id=None, baseline_name=None, create_time=None, description=None, type=None,
                 update_time=None):
        # The baseline ID.
        self.baseline_id = baseline_id  # type: str
        # The name of the baseline.
        self.baseline_name = baseline_name  # type: str
        # The time at which the baseline was created.
        self.create_time = create_time  # type: str
        # The description of the baseline.
        self.description = description  # type: str
        # The type of the baseline. Valid values:
        # 
        # *   System: default baseline
        # *   Custom: custom baseline
        self.type = type  # type: str
        # The time when the baseline was updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccountFactoryBaselinesResponseBodyBaselines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListAccountFactoryBaselinesResponseBody(TeaModel):
    def __init__(self, baselines=None, next_token=None, request_id=None):
        # An array that consists of baselines.
        self.baselines = baselines  # type: list[ListAccountFactoryBaselinesResponseBodyBaselines]
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.baselines:
            for k in self.baselines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccountFactoryBaselinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Baselines'] = []
        if self.baselines is not None:
            for k in self.baselines:
                result['Baselines'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.baselines = []
        if m.get('Baselines') is not None:
            for k in m.get('Baselines'):
                temp_model = ListAccountFactoryBaselinesResponseBodyBaselines()
                self.baselines.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAccountFactoryBaselinesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAccountFactoryBaselinesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAccountFactoryBaselinesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAccountFactoryBaselinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnrolledAccountsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_id=None):
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token  # type: str
        # The region ID.
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
    def __init__(self, account_uid=None, baseline_id=None, create_time=None, display_name=None, folder_id=None,
                 payer_account_uid=None, status=None, update_time=None):
        # The account ID.
        self.account_uid = account_uid  # type: long
        # The baseline ID.
        self.baseline_id = baseline_id  # type: str
        # The time at which the account was created.
        self.create_time = create_time  # type: str
        # The display name of the account.
        self.display_name = display_name  # type: str
        # The ID of the parent folder.
        self.folder_id = folder_id  # type: str
        # The ID of the billing account.
        self.payer_account_uid = payer_account_uid  # type: long
        # The creation status of the account. Valid values:
        # 
        # *   Pending: The account is waiting to be created.
        # *   Running: The account is being created.
        # *   Finished: The account is created.
        # *   Failed: The account failed to be created.
        # *   Scheduling: The account is being scheduled.
        # *   ScheduleFailed: The account failed to be scheduled.
        self.status = status  # type: str
        # The time when the information about the account was updated.
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
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
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
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
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
        # The accounts.
        self.enrolled_accounts = enrolled_accounts  # type: list[ListEnrolledAccountsResponseBodyEnrolledAccounts]
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
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


