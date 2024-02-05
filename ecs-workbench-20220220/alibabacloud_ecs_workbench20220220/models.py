# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class LoginInstanceRequestInstanceLoginInfoOptionsContainerInfo(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, container_name=None, deployment=None, endpoint=None,
                 headers=None, namespace=None, pod_name=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.container_name = container_name  # type: str
        self.deployment = deployment  # type: str
        self.endpoint = endpoint  # type: str
        self.headers = headers  # type: dict[str, any]
        self.namespace = namespace  # type: str
        self.pod_name = pod_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoginInstanceRequestInstanceLoginInfoOptionsContainerInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.deployment is not None:
            result['Deployment'] = self.deployment
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('Deployment') is not None:
            self.deployment = m.get('Deployment')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        return self


class LoginInstanceRequestInstanceLoginInfoOptions(TeaModel):
    def __init__(self, audio_mute_seconds=None, container_info=None, fixed_height=None, fixed_width=None,
                 notification_event_types=None, notification_recipient_url=None, notification_retry_interval_seconds=None,
                 notification_retry_limit=None, operation_disable_seconds=None, session_control=None, video_freeze_seconds=None):
        self.audio_mute_seconds = audio_mute_seconds  # type: int
        self.container_info = container_info  # type: LoginInstanceRequestInstanceLoginInfoOptionsContainerInfo
        self.fixed_height = fixed_height  # type: int
        self.fixed_width = fixed_width  # type: int
        self.notification_event_types = notification_event_types  # type: str
        self.notification_recipient_url = notification_recipient_url  # type: str
        self.notification_retry_interval_seconds = notification_retry_interval_seconds  # type: int
        self.notification_retry_limit = notification_retry_limit  # type: int
        self.operation_disable_seconds = operation_disable_seconds  # type: int
        self.session_control = session_control  # type: str
        self.video_freeze_seconds = video_freeze_seconds  # type: int

    def validate(self):
        if self.container_info:
            self.container_info.validate()

    def to_map(self):
        _map = super(LoginInstanceRequestInstanceLoginInfoOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_mute_seconds is not None:
            result['AudioMuteSeconds'] = self.audio_mute_seconds
        if self.container_info is not None:
            result['ContainerInfo'] = self.container_info.to_map()
        if self.fixed_height is not None:
            result['FixedHeight'] = self.fixed_height
        if self.fixed_width is not None:
            result['FixedWidth'] = self.fixed_width
        if self.notification_event_types is not None:
            result['NotificationEventTypes'] = self.notification_event_types
        if self.notification_recipient_url is not None:
            result['NotificationRecipientUrl'] = self.notification_recipient_url
        if self.notification_retry_interval_seconds is not None:
            result['NotificationRetryIntervalSeconds'] = self.notification_retry_interval_seconds
        if self.notification_retry_limit is not None:
            result['NotificationRetryLimit'] = self.notification_retry_limit
        if self.operation_disable_seconds is not None:
            result['OperationDisableSeconds'] = self.operation_disable_seconds
        if self.session_control is not None:
            result['SessionControl'] = self.session_control
        if self.video_freeze_seconds is not None:
            result['VideoFreezeSeconds'] = self.video_freeze_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioMuteSeconds') is not None:
            self.audio_mute_seconds = m.get('AudioMuteSeconds')
        if m.get('ContainerInfo') is not None:
            temp_model = LoginInstanceRequestInstanceLoginInfoOptionsContainerInfo()
            self.container_info = temp_model.from_map(m['ContainerInfo'])
        if m.get('FixedHeight') is not None:
            self.fixed_height = m.get('FixedHeight')
        if m.get('FixedWidth') is not None:
            self.fixed_width = m.get('FixedWidth')
        if m.get('NotificationEventTypes') is not None:
            self.notification_event_types = m.get('NotificationEventTypes')
        if m.get('NotificationRecipientUrl') is not None:
            self.notification_recipient_url = m.get('NotificationRecipientUrl')
        if m.get('NotificationRetryIntervalSeconds') is not None:
            self.notification_retry_interval_seconds = m.get('NotificationRetryIntervalSeconds')
        if m.get('NotificationRetryLimit') is not None:
            self.notification_retry_limit = m.get('NotificationRetryLimit')
        if m.get('OperationDisableSeconds') is not None:
            self.operation_disable_seconds = m.get('OperationDisableSeconds')
        if m.get('SessionControl') is not None:
            self.session_control = m.get('SessionControl')
        if m.get('VideoFreezeSeconds') is not None:
            self.video_freeze_seconds = m.get('VideoFreezeSeconds')
        return self


class LoginInstanceRequestInstanceLoginInfo(TeaModel):
    def __init__(self, authentication_type=None, certificate=None, credential_token=None,
                 docker_container_name=None, docker_exec=None, duration_seconds=None, expire_time=None, host=None, instance_id=None,
                 instance_type=None, login_by_instance_credential=None, login_by_instance_shortcut=None,
                 network_access_mode=None, options=None, pass_phrase=None, password=None, port=None, protocol=None, region_id=None,
                 resource_group_id=None, shortcut_token=None, username=None, vpc_id=None):
        self.authentication_type = authentication_type  # type: str
        self.certificate = certificate  # type: str
        self.credential_token = credential_token  # type: str
        self.docker_container_name = docker_container_name  # type: str
        self.docker_exec = docker_exec  # type: str
        self.duration_seconds = duration_seconds  # type: long
        self.expire_time = expire_time  # type: str
        self.host = host  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.login_by_instance_credential = login_by_instance_credential  # type: bool
        self.login_by_instance_shortcut = login_by_instance_shortcut  # type: bool
        self.network_access_mode = network_access_mode  # type: str
        self.options = options  # type: LoginInstanceRequestInstanceLoginInfoOptions
        self.pass_phrase = pass_phrase  # type: str
        self.password = password  # type: str
        self.port = port  # type: int
        self.protocol = protocol  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.shortcut_token = shortcut_token  # type: str
        self.username = username  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        _map = super(LoginInstanceRequestInstanceLoginInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_type is not None:
            result['AuthenticationType'] = self.authentication_type
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.credential_token is not None:
            result['CredentialToken'] = self.credential_token
        if self.docker_container_name is not None:
            result['DockerContainerName'] = self.docker_container_name
        if self.docker_exec is not None:
            result['DockerExec'] = self.docker_exec
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.login_by_instance_credential is not None:
            result['LoginByInstanceCredential'] = self.login_by_instance_credential
        if self.login_by_instance_shortcut is not None:
            result['LoginByInstanceShortcut'] = self.login_by_instance_shortcut
        if self.network_access_mode is not None:
            result['NetworkAccessMode'] = self.network_access_mode
        if self.options is not None:
            result['Options'] = self.options.to_map()
        if self.pass_phrase is not None:
            result['PassPhrase'] = self.pass_phrase
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.shortcut_token is not None:
            result['ShortcutToken'] = self.shortcut_token
        if self.username is not None:
            result['Username'] = self.username
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthenticationType') is not None:
            self.authentication_type = m.get('AuthenticationType')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('CredentialToken') is not None:
            self.credential_token = m.get('CredentialToken')
        if m.get('DockerContainerName') is not None:
            self.docker_container_name = m.get('DockerContainerName')
        if m.get('DockerExec') is not None:
            self.docker_exec = m.get('DockerExec')
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LoginByInstanceCredential') is not None:
            self.login_by_instance_credential = m.get('LoginByInstanceCredential')
        if m.get('LoginByInstanceShortcut') is not None:
            self.login_by_instance_shortcut = m.get('LoginByInstanceShortcut')
        if m.get('NetworkAccessMode') is not None:
            self.network_access_mode = m.get('NetworkAccessMode')
        if m.get('Options') is not None:
            temp_model = LoginInstanceRequestInstanceLoginInfoOptions()
            self.options = temp_model.from_map(m['Options'])
        if m.get('PassPhrase') is not None:
            self.pass_phrase = m.get('PassPhrase')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShortcutToken') is not None:
            self.shortcut_token = m.get('ShortcutToken')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class LoginInstanceRequestPartnerInfo(TeaModel):
    def __init__(self, partner_id=None, partner_name=None):
        self.partner_id = partner_id  # type: str
        self.partner_name = partner_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoginInstanceRequestPartnerInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.partner_id is not None:
            result['PartnerId'] = self.partner_id
        if self.partner_name is not None:
            result['PartnerName'] = self.partner_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PartnerId') is not None:
            self.partner_id = m.get('PartnerId')
        if m.get('PartnerName') is not None:
            self.partner_name = m.get('PartnerName')
        return self


class LoginInstanceRequestUserAccountOptions(TeaModel):
    def __init__(self, login_limit=None):
        self.login_limit = login_limit  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoginInstanceRequestUserAccountOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_limit is not None:
            result['LoginLimit'] = self.login_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoginLimit') is not None:
            self.login_limit = m.get('LoginLimit')
        return self


class LoginInstanceRequestUserAccount(TeaModel):
    def __init__(self, account_id=None, account_platform=None, account_structure=None, duration_seconds=None,
                 emp_id=None, expire_time=None, login_name=None, options=None, parent_id=None):
        self.account_id = account_id  # type: long
        self.account_platform = account_platform  # type: str
        self.account_structure = account_structure  # type: str
        self.duration_seconds = duration_seconds  # type: long
        self.emp_id = emp_id  # type: str
        self.expire_time = expire_time  # type: str
        self.login_name = login_name  # type: str
        self.options = options  # type: LoginInstanceRequestUserAccountOptions
        self.parent_id = parent_id  # type: long

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        _map = super(LoginInstanceRequestUserAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_platform is not None:
            result['AccountPlatform'] = self.account_platform
        if self.account_structure is not None:
            result['AccountStructure'] = self.account_structure
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        if self.emp_id is not None:
            result['EmpId'] = self.emp_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.login_name is not None:
            result['LoginName'] = self.login_name
        if self.options is not None:
            result['Options'] = self.options.to_map()
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountPlatform') is not None:
            self.account_platform = m.get('AccountPlatform')
        if m.get('AccountStructure') is not None:
            self.account_structure = m.get('AccountStructure')
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        if m.get('EmpId') is not None:
            self.emp_id = m.get('EmpId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')
        if m.get('Options') is not None:
            temp_model = LoginInstanceRequestUserAccountOptions()
            self.options = temp_model.from_map(m['Options'])
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class LoginInstanceRequest(TeaModel):
    def __init__(self, instance_login_info=None, partner_info=None, user_account=None):
        self.instance_login_info = instance_login_info  # type: LoginInstanceRequestInstanceLoginInfo
        self.partner_info = partner_info  # type: LoginInstanceRequestPartnerInfo
        self.user_account = user_account  # type: LoginInstanceRequestUserAccount

    def validate(self):
        if self.instance_login_info:
            self.instance_login_info.validate()
        if self.partner_info:
            self.partner_info.validate()
        if self.user_account:
            self.user_account.validate()

    def to_map(self):
        _map = super(LoginInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_login_info is not None:
            result['InstanceLoginInfo'] = self.instance_login_info.to_map()
        if self.partner_info is not None:
            result['PartnerInfo'] = self.partner_info.to_map()
        if self.user_account is not None:
            result['UserAccount'] = self.user_account.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceLoginInfo') is not None:
            temp_model = LoginInstanceRequestInstanceLoginInfo()
            self.instance_login_info = temp_model.from_map(m['InstanceLoginInfo'])
        if m.get('PartnerInfo') is not None:
            temp_model = LoginInstanceRequestPartnerInfo()
            self.partner_info = temp_model.from_map(m['PartnerInfo'])
        if m.get('UserAccount') is not None:
            temp_model = LoginInstanceRequestUserAccount()
            self.user_account = temp_model.from_map(m['UserAccount'])
        return self


class LoginInstanceResponseBodyRootDisposableAccount(TeaModel):
    def __init__(self, login_form_action_url=None, login_url=None):
        self.login_form_action_url = login_form_action_url  # type: str
        self.login_url = login_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoginInstanceResponseBodyRootDisposableAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_form_action_url is not None:
            result['LoginFormActionUrl'] = self.login_form_action_url
        if self.login_url is not None:
            result['LoginUrl'] = self.login_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoginFormActionUrl') is not None:
            self.login_form_action_url = m.get('LoginFormActionUrl')
        if m.get('LoginUrl') is not None:
            self.login_url = m.get('LoginUrl')
        return self


class LoginInstanceResponseBodyRootInstanceLoginInfoListInstanceLoginView(TeaModel):
    def __init__(self, default_view_url=None):
        self.default_view_url = default_view_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoginInstanceResponseBodyRootInstanceLoginInfoListInstanceLoginView, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_view_url is not None:
            result['DefaultViewUrl'] = self.default_view_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultViewUrl') is not None:
            self.default_view_url = m.get('DefaultViewUrl')
        return self


class LoginInstanceResponseBodyRootInstanceLoginInfoList(TeaModel):
    def __init__(self, instance_id=None, instance_login_token=None, instance_login_view=None, login_success=None):
        self.instance_id = instance_id  # type: str
        self.instance_login_token = instance_login_token  # type: str
        self.instance_login_view = instance_login_view  # type: LoginInstanceResponseBodyRootInstanceLoginInfoListInstanceLoginView
        self.login_success = login_success  # type: bool

    def validate(self):
        if self.instance_login_view:
            self.instance_login_view.validate()

    def to_map(self):
        _map = super(LoginInstanceResponseBodyRootInstanceLoginInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_login_token is not None:
            result['InstanceLoginToken'] = self.instance_login_token
        if self.instance_login_view is not None:
            result['InstanceLoginView'] = self.instance_login_view.to_map()
        if self.login_success is not None:
            result['LoginSuccess'] = self.login_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceLoginToken') is not None:
            self.instance_login_token = m.get('InstanceLoginToken')
        if m.get('InstanceLoginView') is not None:
            temp_model = LoginInstanceResponseBodyRootInstanceLoginInfoListInstanceLoginView()
            self.instance_login_view = temp_model.from_map(m['InstanceLoginView'])
        if m.get('LoginSuccess') is not None:
            self.login_success = m.get('LoginSuccess')
        return self


class LoginInstanceResponseBodyRootSessionControl(TeaModel):
    def __init__(self, base_url=None):
        self.base_url = base_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoginInstanceResponseBodyRootSessionControl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_url is not None:
            result['BaseUrl'] = self.base_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')
        return self


class LoginInstanceResponseBodyRoot(TeaModel):
    def __init__(self, disposable_account=None, instance_login_info_list=None, session_control=None):
        self.disposable_account = disposable_account  # type: LoginInstanceResponseBodyRootDisposableAccount
        self.instance_login_info_list = instance_login_info_list  # type: list[LoginInstanceResponseBodyRootInstanceLoginInfoList]
        self.session_control = session_control  # type: LoginInstanceResponseBodyRootSessionControl

    def validate(self):
        if self.disposable_account:
            self.disposable_account.validate()
        if self.instance_login_info_list:
            for k in self.instance_login_info_list:
                if k:
                    k.validate()
        if self.session_control:
            self.session_control.validate()

    def to_map(self):
        _map = super(LoginInstanceResponseBodyRoot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disposable_account is not None:
            result['DisposableAccount'] = self.disposable_account.to_map()
        result['InstanceLoginInfoList'] = []
        if self.instance_login_info_list is not None:
            for k in self.instance_login_info_list:
                result['InstanceLoginInfoList'].append(k.to_map() if k else None)
        if self.session_control is not None:
            result['SessionControl'] = self.session_control.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisposableAccount') is not None:
            temp_model = LoginInstanceResponseBodyRootDisposableAccount()
            self.disposable_account = temp_model.from_map(m['DisposableAccount'])
        self.instance_login_info_list = []
        if m.get('InstanceLoginInfoList') is not None:
            for k in m.get('InstanceLoginInfoList'):
                temp_model = LoginInstanceResponseBodyRootInstanceLoginInfoList()
                self.instance_login_info_list.append(temp_model.from_map(k))
        if m.get('SessionControl') is not None:
            temp_model = LoginInstanceResponseBodyRootSessionControl()
            self.session_control = temp_model.from_map(m['SessionControl'])
        return self


class LoginInstanceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, root=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.root = root  # type: LoginInstanceResponseBodyRoot
        self.success = success  # type: str

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        _map = super(LoginInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root is not None:
            result['Root'] = self.root.to_map()
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
        if m.get('Root') is not None:
            temp_model = LoginInstanceResponseBodyRoot()
            self.root = temp_model.from_map(m['Root'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class LoginInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LoginInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LoginInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LoginInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


