# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateTaskDetailAdmins(TeaModel):
    def __init__(self, users=None):
        self.users = users  # type: list[SimpleUser]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTaskDetailAdmins, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = SimpleUser()
                self.users.append(temp_model.from_map(k))
        return self


class CreateTaskDetailTaskWorkflow(TeaModel):
    def __init__(self, node_name=None):
        self.node_name = node_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTaskDetailTaskWorkflow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class CreateTaskDetail(TeaModel):
    def __init__(self, admins=None, allow_append_data=None, assign_config=None, dataset_proxy_relations=None,
                 exif=None, tags=None, task_name=None, task_template_config=None, task_workflow=None, template_id=None,
                 uuid=None):
        self.admins = admins  # type: CreateTaskDetailAdmins
        self.allow_append_data = allow_append_data  # type: bool
        self.assign_config = assign_config  # type: TaskAssginConfig
        self.dataset_proxy_relations = dataset_proxy_relations  # type: list[DatasetProxyConfig]
        self.exif = exif  # type: dict[str, any]
        self.tags = tags  # type: list[str]
        self.task_name = task_name  # type: str
        self.task_template_config = task_template_config  # type: TaskTemplateConfig
        self.task_workflow = task_workflow  # type: list[CreateTaskDetailTaskWorkflow]
        self.template_id = template_id  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        if self.admins:
            self.admins.validate()
        if self.assign_config:
            self.assign_config.validate()
        if self.dataset_proxy_relations:
            for k in self.dataset_proxy_relations:
                if k:
                    k.validate()
        if self.task_template_config:
            self.task_template_config.validate()
        if self.task_workflow:
            for k in self.task_workflow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTaskDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admins is not None:
            result['Admins'] = self.admins.to_map()
        if self.allow_append_data is not None:
            result['AllowAppendData'] = self.allow_append_data
        if self.assign_config is not None:
            result['AssignConfig'] = self.assign_config.to_map()
        result['DatasetProxyRelations'] = []
        if self.dataset_proxy_relations is not None:
            for k in self.dataset_proxy_relations:
                result['DatasetProxyRelations'].append(k.to_map() if k else None)
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_template_config is not None:
            result['TaskTemplateConfig'] = self.task_template_config.to_map()
        result['TaskWorkflow'] = []
        if self.task_workflow is not None:
            for k in self.task_workflow:
                result['TaskWorkflow'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.uuid is not None:
            result['UUID'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Admins') is not None:
            temp_model = CreateTaskDetailAdmins()
            self.admins = temp_model.from_map(m['Admins'])
        if m.get('AllowAppendData') is not None:
            self.allow_append_data = m.get('AllowAppendData')
        if m.get('AssignConfig') is not None:
            temp_model = TaskAssginConfig()
            self.assign_config = temp_model.from_map(m['AssignConfig'])
        self.dataset_proxy_relations = []
        if m.get('DatasetProxyRelations') is not None:
            for k in m.get('DatasetProxyRelations'):
                temp_model = DatasetProxyConfig()
                self.dataset_proxy_relations.append(temp_model.from_map(k))
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskTemplateConfig') is not None:
            temp_model = TaskTemplateConfig()
            self.task_template_config = temp_model.from_map(m['TaskTemplateConfig'])
        self.task_workflow = []
        if m.get('TaskWorkflow') is not None:
            for k in m.get('TaskWorkflow'):
                temp_model = CreateTaskDetailTaskWorkflow()
                self.task_workflow.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        return self


class DatasetProxyConfig(TeaModel):
    def __init__(self, dataset_type=None, source=None, source_dataset_id=None):
        self.dataset_type = dataset_type  # type: str
        self.source = source  # type: str
        self.source_dataset_id = source_dataset_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DatasetProxyConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type
        if self.source is not None:
            result['Source'] = self.source
        if self.source_dataset_id is not None:
            result['SourceDatasetId'] = self.source_dataset_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceDatasetId') is not None:
            self.source_dataset_id = m.get('SourceDatasetId')
        return self


class FlowJobInfo(TeaModel):
    def __init__(self, display=None, job_id=None, job_type=None, message_id=None, process_type=None, task_id=None):
        self.display = display  # type: bool
        self.job_id = job_id  # type: str
        self.job_type = job_type  # type: str
        self.message_id = message_id  # type: str
        self.process_type = process_type  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FlowJobInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.process_type is not None:
            result['ProcessType'] = self.process_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('ProcessType') is not None:
            self.process_type = m.get('ProcessType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class JobJobResult(TeaModel):
    def __init__(self, result_link=None):
        self.result_link = result_link  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobJobResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_link is not None:
            result['ResultLink'] = self.result_link
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResultLink') is not None:
            self.result_link = m.get('ResultLink')
        return self


class Job(TeaModel):
    def __init__(self, creator=None, gmt_create_time=None, gmt_modified_time=None, job_id=None, job_result=None,
                 job_type=None, status=None):
        self.creator = creator  # type: SimpleUser
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.job_id = job_id  # type: str
        self.job_result = job_result  # type: JobJobResult
        self.job_type = job_type  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.job_result:
            self.job_result.validate()

    def to_map(self):
        _map = super(Job, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_result is not None:
            result['JobResult'] = self.job_result.to_map()
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Creator') is not None:
            temp_model = SimpleUser()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobResult') is not None:
            temp_model = JobJobResult()
            self.job_result = temp_model.from_map(m['JobResult'])
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class MarkResult(TeaModel):
    def __init__(self, is_need_vote_judge=None, mark_result=None, mark_result_id=None, mark_time=None,
                 mark_title=None, progress=None, question_id=None, result_type=None, user_mark_result_id=None, version=None):
        self.is_need_vote_judge = is_need_vote_judge  # type: bool
        self.mark_result = mark_result  # type: str
        self.mark_result_id = mark_result_id  # type: str
        self.mark_time = mark_time  # type: str
        self.mark_title = mark_title  # type: str
        self.progress = progress  # type: str
        self.question_id = question_id  # type: str
        self.result_type = result_type  # type: str
        self.user_mark_result_id = user_mark_result_id  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MarkResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_need_vote_judge is not None:
            result['IsNeedVoteJudge'] = self.is_need_vote_judge
        if self.mark_result is not None:
            result['MarkResult'] = self.mark_result
        if self.mark_result_id is not None:
            result['MarkResultId'] = self.mark_result_id
        if self.mark_time is not None:
            result['MarkTime'] = self.mark_time
        if self.mark_title is not None:
            result['MarkTitle'] = self.mark_title
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.question_id is not None:
            result['QuestionId'] = self.question_id
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.user_mark_result_id is not None:
            result['UserMarkResultId'] = self.user_mark_result_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsNeedVoteJudge') is not None:
            self.is_need_vote_judge = m.get('IsNeedVoteJudge')
        if m.get('MarkResult') is not None:
            self.mark_result = m.get('MarkResult')
        if m.get('MarkResultId') is not None:
            self.mark_result_id = m.get('MarkResultId')
        if m.get('MarkTime') is not None:
            self.mark_time = m.get('MarkTime')
        if m.get('MarkTitle') is not None:
            self.mark_title = m.get('MarkTitle')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('QuestionId') is not None:
            self.question_id = m.get('QuestionId')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('UserMarkResultId') is not None:
            self.user_mark_result_id = m.get('UserMarkResultId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class QuestionOption(TeaModel):
    def __init__(self, children=None, color=None, key=None, label=None, remark=None, shortcut=None):
        self.children = children  # type: list[QuestionOption]
        self.color = color  # type: str
        self.key = key  # type: str
        self.label = label  # type: str
        self.remark = remark  # type: str
        self.shortcut = shortcut  # type: str

    def validate(self):
        if self.children:
            for k in self.children:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuestionOption, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Children'] = []
        if self.children is not None:
            for k in self.children:
                result['Children'].append(k.to_map() if k else None)
        if self.color is not None:
            result['Color'] = self.color
        if self.key is not None:
            result['Key'] = self.key
        if self.label is not None:
            result['Label'] = self.label
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.shortcut is not None:
            result['Shortcut'] = self.shortcut
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k in m.get('Children'):
                temp_model = QuestionOption()
                self.children.append(temp_model.from_map(k))
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Shortcut') is not None:
            self.shortcut = m.get('Shortcut')
        return self


class QuestionPlugin(TeaModel):
    def __init__(self, can_select=None, children=None, default_result=None, display=None, exif=None,
                 hot_key_map=None, mark_title=None, mark_title_alias=None, must_fill=None, options=None, pre_options=None,
                 question_id=None, rule=None, select_group=None, selected=None, type=None):
        self.can_select = can_select  # type: bool
        self.children = children  # type: list[QuestionPlugin]
        self.default_result = default_result  # type: str
        self.display = display  # type: bool
        self.exif = exif  # type: dict[str, any]
        self.hot_key_map = hot_key_map  # type: str
        self.mark_title = mark_title  # type: str
        self.mark_title_alias = mark_title_alias  # type: str
        self.must_fill = must_fill  # type: bool
        self.options = options  # type: list[QuestionOption]
        self.pre_options = pre_options  # type: list[str]
        self.question_id = question_id  # type: str
        self.rule = rule  # type: str
        self.select_group = select_group  # type: str
        self.selected = selected  # type: bool
        self.type = type  # type: str

    def validate(self):
        if self.children:
            for k in self.children:
                if k:
                    k.validate()
        if self.options:
            for k in self.options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuestionPlugin, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_select is not None:
            result['CanSelect'] = self.can_select
        result['Children'] = []
        if self.children is not None:
            for k in self.children:
                result['Children'].append(k.to_map() if k else None)
        if self.default_result is not None:
            result['DefaultResult'] = self.default_result
        if self.display is not None:
            result['Display'] = self.display
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.hot_key_map is not None:
            result['HotKeyMap'] = self.hot_key_map
        if self.mark_title is not None:
            result['MarkTitle'] = self.mark_title
        if self.mark_title_alias is not None:
            result['MarkTitleAlias'] = self.mark_title_alias
        if self.must_fill is not None:
            result['MustFill'] = self.must_fill
        result['Options'] = []
        if self.options is not None:
            for k in self.options:
                result['Options'].append(k.to_map() if k else None)
        if self.pre_options is not None:
            result['PreOptions'] = self.pre_options
        if self.question_id is not None:
            result['QuestionId'] = self.question_id
        if self.rule is not None:
            result['Rule'] = self.rule
        if self.select_group is not None:
            result['SelectGroup'] = self.select_group
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanSelect') is not None:
            self.can_select = m.get('CanSelect')
        self.children = []
        if m.get('Children') is not None:
            for k in m.get('Children'):
                temp_model = QuestionPlugin()
                self.children.append(temp_model.from_map(k))
        if m.get('DefaultResult') is not None:
            self.default_result = m.get('DefaultResult')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('HotKeyMap') is not None:
            self.hot_key_map = m.get('HotKeyMap')
        if m.get('MarkTitle') is not None:
            self.mark_title = m.get('MarkTitle')
        if m.get('MarkTitleAlias') is not None:
            self.mark_title_alias = m.get('MarkTitleAlias')
        if m.get('MustFill') is not None:
            self.must_fill = m.get('MustFill')
        self.options = []
        if m.get('Options') is not None:
            for k in m.get('Options'):
                temp_model = QuestionOption()
                self.options.append(temp_model.from_map(k))
        if m.get('PreOptions') is not None:
            self.pre_options = m.get('PreOptions')
        if m.get('QuestionId') is not None:
            self.question_id = m.get('QuestionId')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        if m.get('SelectGroup') is not None:
            self.select_group = m.get('SelectGroup')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SimpleSubtaskItems(TeaModel):
    def __init__(self, abandon_flag=None, abandon_remark=None, data_id=None, feedback_flag=None,
                 feedback_remark=None, fixed_flag=None, item_id=None, mine=None, reject_flag=None, state=None, weight=None):
        self.abandon_flag = abandon_flag  # type: bool
        self.abandon_remark = abandon_remark  # type: str
        self.data_id = data_id  # type: str
        self.feedback_flag = feedback_flag  # type: bool
        self.feedback_remark = feedback_remark  # type: str
        self.fixed_flag = fixed_flag  # type: bool
        self.item_id = item_id  # type: long
        self.mine = mine  # type: long
        self.reject_flag = reject_flag  # type: bool
        self.state = state  # type: str
        self.weight = weight  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SimpleSubtaskItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandon_flag is not None:
            result['AbandonFlag'] = self.abandon_flag
        if self.abandon_remark is not None:
            result['AbandonRemark'] = self.abandon_remark
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.feedback_flag is not None:
            result['FeedbackFlag'] = self.feedback_flag
        if self.feedback_remark is not None:
            result['FeedbackRemark'] = self.feedback_remark
        if self.fixed_flag is not None:
            result['FixedFlag'] = self.fixed_flag
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.mine is not None:
            result['Mine'] = self.mine
        if self.reject_flag is not None:
            result['RejectFlag'] = self.reject_flag
        if self.state is not None:
            result['State'] = self.state
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AbandonFlag') is not None:
            self.abandon_flag = m.get('AbandonFlag')
        if m.get('AbandonRemark') is not None:
            self.abandon_remark = m.get('AbandonRemark')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('FeedbackFlag') is not None:
            self.feedback_flag = m.get('FeedbackFlag')
        if m.get('FeedbackRemark') is not None:
            self.feedback_remark = m.get('FeedbackRemark')
        if m.get('FixedFlag') is not None:
            self.fixed_flag = m.get('FixedFlag')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Mine') is not None:
            self.mine = m.get('Mine')
        if m.get('RejectFlag') is not None:
            self.reject_flag = m.get('RejectFlag')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class SimpleSubtask(TeaModel):
    def __init__(self, items=None, status=None, subtask_id=None):
        self.items = items  # type: list[SimpleSubtaskItems]
        self.status = status  # type: str
        self.subtask_id = subtask_id  # type: long

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SimpleSubtask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.subtask_id is not None:
            result['SubtaskId'] = self.subtask_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = SimpleSubtaskItems()
                self.items.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubtaskId') is not None:
            self.subtask_id = m.get('SubtaskId')
        return self


class SimpleTask(TeaModel):
    def __init__(self, archived=None, archived_infos=None, creator=None, gmt_create_time=None,
                 gmt_modified_time=None, label_style=None, modifier=None, ref_task_id=None, remark=None, stage=None, status=None,
                 tags=None, task_id=None, task_name=None, task_type=None, template_id=None, tenant_id=None, uuid=None,
                 workflow_nodes=None):
        self.archived = archived  # type: bool
        self.archived_infos = archived_infos  # type: str
        self.creator = creator  # type: SimpleUser
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.label_style = label_style  # type: str
        self.modifier = modifier  # type: SimpleUser
        self.ref_task_id = ref_task_id  # type: str
        self.remark = remark  # type: str
        self.stage = stage  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: list[str]
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str
        self.task_type = task_type  # type: str
        self.template_id = template_id  # type: str
        self.tenant_id = tenant_id  # type: str
        self.uuid = uuid  # type: str
        self.workflow_nodes = workflow_nodes  # type: list[str]

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()

    def to_map(self):
        _map = super(SimpleTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archived is not None:
            result['Archived'] = self.archived
        if self.archived_infos is not None:
            result['ArchivedInfos'] = self.archived_infos
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.label_style is not None:
            result['LabelStyle'] = self.label_style
        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()
        if self.ref_task_id is not None:
            result['RefTaskId'] = self.ref_task_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.stage is not None:
            result['Stage'] = self.stage
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.uuid is not None:
            result['UUID'] = self.uuid
        if self.workflow_nodes is not None:
            result['WorkflowNodes'] = self.workflow_nodes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Archived') is not None:
            self.archived = m.get('Archived')
        if m.get('ArchivedInfos') is not None:
            self.archived_infos = m.get('ArchivedInfos')
        if m.get('Creator') is not None:
            temp_model = SimpleUser()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LabelStyle') is not None:
            self.label_style = m.get('LabelStyle')
        if m.get('Modifier') is not None:
            temp_model = SimpleUser()
            self.modifier = temp_model.from_map(m['Modifier'])
        if m.get('RefTaskId') is not None:
            self.ref_task_id = m.get('RefTaskId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Stage') is not None:
            self.stage = m.get('Stage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        if m.get('WorkflowNodes') is not None:
            self.workflow_nodes = m.get('WorkflowNodes')
        return self


class SimpleTemplate(TeaModel):
    def __init__(self, abandon_reasons=None, description=None, gmt_create_time=None, gmt_modified_time=None,
                 shared_mode=None, status=None, tags=None, template_id=None, template_name=None, tenant_id=None, type=None):
        self.abandon_reasons = abandon_reasons  # type: str
        self.description = description  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.shared_mode = shared_mode  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: list[str]
        self.template_id = template_id  # type: str
        self.template_name = template_name  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SimpleTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandon_reasons is not None:
            result['AbandonReasons'] = self.abandon_reasons
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.shared_mode is not None:
            result['SharedMode'] = self.shared_mode
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AbandonReasons') is not None:
            self.abandon_reasons = m.get('AbandonReasons')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('SharedMode') is not None:
            self.shared_mode = m.get('SharedMode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SimpleTenant(TeaModel):
    def __init__(self, creator=None, description=None, gmt_create_time=None, gmt_modified_time=None, modifier=None,
                 role=None, tenant_id=None, tenant_name=None, uuid=None):
        self.creator = creator  # type: SimpleUser
        self.description = description  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.modifier = modifier  # type: SimpleUser
        self.role = role  # type: str
        self.tenant_id = tenant_id  # type: str
        self.tenant_name = tenant_name  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()

    def to_map(self):
        _map = super(SimpleTenant, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()
        if self.role is not None:
            result['Role'] = self.role
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.uuid is not None:
            result['UUID'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Creator') is not None:
            temp_model = SimpleUser()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Modifier') is not None:
            temp_model = SimpleUser()
            self.modifier = temp_model.from_map(m['Modifier'])
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        return self


class SimpleUser(TeaModel):
    def __init__(self, account_no=None, account_type=None, role=None, user_id=None, user_name=None):
        self.account_no = account_no  # type: str
        self.account_type = account_type  # type: str
        self.role = role  # type: str
        self.user_id = user_id  # type: long
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SimpleUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_no is not None:
            result['AccountNo'] = self.account_no
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.role is not None:
            result['Role'] = self.role
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class SimpleWorkforce(TeaModel):
    def __init__(self, user_ids=None, work_node_id=None):
        self.user_ids = user_ids  # type: list[long]
        self.work_node_id = work_node_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SimpleWorkforce, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        if self.work_node_id is not None:
            result['WorkNodeId'] = self.work_node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        if m.get('WorkNodeId') is not None:
            self.work_node_id = m.get('WorkNodeId')
        return self


class SingleTenant(TeaModel):
    def __init__(self, description=None, status=None, tenant_id=None, tenant_name=None, uuid=None):
        self.description = description  # type: str
        self.status = status  # type: str
        self.tenant_id = tenant_id  # type: str
        self.tenant_name = tenant_name  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SingleTenant, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.uuid is not None:
            result['UUID'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        return self


class SubtaskDetailItems(TeaModel):
    def __init__(self, abandon_flag=None, abandon_remark=None, data_id=None, feedback_flag=None,
                 feedback_remark=None, fixed_flag=None, mine=None, reject_flag=None, state=None, weight=None):
        self.abandon_flag = abandon_flag  # type: bool
        self.abandon_remark = abandon_remark  # type: str
        self.data_id = data_id  # type: str
        self.feedback_flag = feedback_flag  # type: bool
        self.feedback_remark = feedback_remark  # type: str
        self.fixed_flag = fixed_flag  # type: bool
        self.mine = mine  # type: long
        self.reject_flag = reject_flag  # type: bool
        self.state = state  # type: str
        self.weight = weight  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubtaskDetailItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandon_flag is not None:
            result['AbandonFlag'] = self.abandon_flag
        if self.abandon_remark is not None:
            result['AbandonRemark'] = self.abandon_remark
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.feedback_flag is not None:
            result['FeedbackFlag'] = self.feedback_flag
        if self.feedback_remark is not None:
            result['FeedbackRemark'] = self.feedback_remark
        if self.fixed_flag is not None:
            result['FixedFlag'] = self.fixed_flag
        if self.mine is not None:
            result['Mine'] = self.mine
        if self.reject_flag is not None:
            result['RejectFlag'] = self.reject_flag
        if self.state is not None:
            result['State'] = self.state
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AbandonFlag') is not None:
            self.abandon_flag = m.get('AbandonFlag')
        if m.get('AbandonRemark') is not None:
            self.abandon_remark = m.get('AbandonRemark')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('FeedbackFlag') is not None:
            self.feedback_flag = m.get('FeedbackFlag')
        if m.get('FeedbackRemark') is not None:
            self.feedback_remark = m.get('FeedbackRemark')
        if m.get('FixedFlag') is not None:
            self.fixed_flag = m.get('FixedFlag')
        if m.get('Mine') is not None:
            self.mine = m.get('Mine')
        if m.get('RejectFlag') is not None:
            self.reject_flag = m.get('RejectFlag')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class SubtaskDetail(TeaModel):
    def __init__(self, can_discard=None, can_reassign=None, can_release=None, current_work_node=None,
                 ext_configs=None, items=None, status=None, subtask_id=None, task_id=None, weight=None, work_node_state=None,
                 workforce=None):
        self.can_discard = can_discard  # type: bool
        self.can_reassign = can_reassign  # type: bool
        self.can_release = can_release  # type: bool
        self.current_work_node = current_work_node  # type: str
        self.ext_configs = ext_configs  # type: str
        self.items = items  # type: list[SubtaskDetailItems]
        self.status = status  # type: str
        self.subtask_id = subtask_id  # type: str
        self.task_id = task_id  # type: str
        self.weight = weight  # type: long
        self.work_node_state = work_node_state  # type: str
        self.workforce = workforce  # type: list[Workforce]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()
        if self.workforce:
            for k in self.workforce:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SubtaskDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_discard is not None:
            result['CanDiscard'] = self.can_discard
        if self.can_reassign is not None:
            result['CanReassign'] = self.can_reassign
        if self.can_release is not None:
            result['CanRelease'] = self.can_release
        if self.current_work_node is not None:
            result['CurrentWorkNode'] = self.current_work_node
        if self.ext_configs is not None:
            result['ExtConfigs'] = self.ext_configs
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.subtask_id is not None:
            result['SubtaskId'] = self.subtask_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.work_node_state is not None:
            result['WorkNodeState'] = self.work_node_state
        result['Workforce'] = []
        if self.workforce is not None:
            for k in self.workforce:
                result['Workforce'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanDiscard') is not None:
            self.can_discard = m.get('CanDiscard')
        if m.get('CanReassign') is not None:
            self.can_reassign = m.get('CanReassign')
        if m.get('CanRelease') is not None:
            self.can_release = m.get('CanRelease')
        if m.get('CurrentWorkNode') is not None:
            self.current_work_node = m.get('CurrentWorkNode')
        if m.get('ExtConfigs') is not None:
            self.ext_configs = m.get('ExtConfigs')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = SubtaskDetailItems()
                self.items.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubtaskId') is not None:
            self.subtask_id = m.get('SubtaskId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('WorkNodeState') is not None:
            self.work_node_state = m.get('WorkNodeState')
        self.workforce = []
        if m.get('Workforce') is not None:
            for k in m.get('Workforce'):
                temp_model = Workforce()
                self.workforce.append(temp_model.from_map(k))
        return self


class SubtaskItemDetailAnnotations(TeaModel):
    def __init__(self, abandon_flag=None, abandon_remark=None, data_id=None, feedback_flag=None,
                 feedback_remark=None, fixed_flag=None, mine=None, reject_flag=None, state=None, weight=None):
        self.abandon_flag = abandon_flag  # type: bool
        self.abandon_remark = abandon_remark  # type: str
        self.data_id = data_id  # type: str
        self.feedback_flag = feedback_flag  # type: bool
        self.feedback_remark = feedback_remark  # type: str
        self.fixed_flag = fixed_flag  # type: bool
        self.mine = mine  # type: long
        self.reject_flag = reject_flag  # type: bool
        self.state = state  # type: str
        self.weight = weight  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubtaskItemDetailAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandon_flag is not None:
            result['AbandonFlag'] = self.abandon_flag
        if self.abandon_remark is not None:
            result['AbandonRemark'] = self.abandon_remark
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.feedback_flag is not None:
            result['FeedbackFlag'] = self.feedback_flag
        if self.feedback_remark is not None:
            result['FeedbackRemark'] = self.feedback_remark
        if self.fixed_flag is not None:
            result['FixedFlag'] = self.fixed_flag
        if self.mine is not None:
            result['Mine'] = self.mine
        if self.reject_flag is not None:
            result['RejectFlag'] = self.reject_flag
        if self.state is not None:
            result['State'] = self.state
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AbandonFlag') is not None:
            self.abandon_flag = m.get('AbandonFlag')
        if m.get('AbandonRemark') is not None:
            self.abandon_remark = m.get('AbandonRemark')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('FeedbackFlag') is not None:
            self.feedback_flag = m.get('FeedbackFlag')
        if m.get('FeedbackRemark') is not None:
            self.feedback_remark = m.get('FeedbackRemark')
        if m.get('FixedFlag') is not None:
            self.fixed_flag = m.get('FixedFlag')
        if m.get('Mine') is not None:
            self.mine = m.get('Mine')
        if m.get('RejectFlag') is not None:
            self.reject_flag = m.get('RejectFlag')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class SubtaskItemDetail(TeaModel):
    def __init__(self, annotations=None, data_source=None, item_id=None):
        self.annotations = annotations  # type: list[SubtaskItemDetailAnnotations]
        self.data_source = data_source  # type: dict[str, any]
        self.item_id = item_id  # type: long

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SubtaskItemDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = SubtaskItemDetailAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        return self


class TaskAssginConfig(TeaModel):
    def __init__(self, assign_count=None, assign_field=None, assign_sub_task_count=None, assign_type=None):
        self.assign_count = assign_count  # type: long
        self.assign_field = assign_field  # type: str
        self.assign_sub_task_count = assign_sub_task_count  # type: str
        self.assign_type = assign_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskAssginConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_count is not None:
            result['AssignCount'] = self.assign_count
        if self.assign_field is not None:
            result['AssignField'] = self.assign_field
        if self.assign_sub_task_count is not None:
            result['AssignSubTaskCount'] = self.assign_sub_task_count
        if self.assign_type is not None:
            result['AssignType'] = self.assign_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssignCount') is not None:
            self.assign_count = m.get('AssignCount')
        if m.get('AssignField') is not None:
            self.assign_field = m.get('AssignField')
        if m.get('AssignSubTaskCount') is not None:
            self.assign_sub_task_count = m.get('AssignSubTaskCount')
        if m.get('AssignType') is not None:
            self.assign_type = m.get('AssignType')
        return self


class TaskDetailDatasetProxyRelations(TeaModel):
    def __init__(self, dataset_id=None, dataset_type=None, exif=None, source=None, source_biz_id=None,
                 source_dataset_id=None):
        self.dataset_id = dataset_id  # type: str
        self.dataset_type = dataset_type  # type: str
        self.exif = exif  # type: dict[str, any]
        self.source = source  # type: str
        self.source_biz_id = source_biz_id  # type: str
        self.source_dataset_id = source_dataset_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskDetailDatasetProxyRelations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.source is not None:
            result['Source'] = self.source
        if self.source_biz_id is not None:
            result['SourceBizId'] = self.source_biz_id
        if self.source_dataset_id is not None:
            result['SourceDatasetId'] = self.source_dataset_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceBizId') is not None:
            self.source_biz_id = m.get('SourceBizId')
        if m.get('SourceDatasetId') is not None:
            self.source_dataset_id = m.get('SourceDatasetId')
        return self


class TaskDetailTaskTemplateConfig(TeaModel):
    def __init__(self, exif=None, resource_key=None, robot_config=None, select_questions=None,
                 template_option_map=None, template_relation_id=None):
        self.exif = exif  # type: dict[str, any]
        self.resource_key = resource_key  # type: str
        self.robot_config = robot_config  # type: dict[str, any]
        self.select_questions = select_questions  # type: list[str]
        self.template_option_map = template_option_map  # type: dict[str, any]
        self.template_relation_id = template_relation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskDetailTaskTemplateConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.robot_config is not None:
            result['RobotConfig'] = self.robot_config
        if self.select_questions is not None:
            result['SelectQuestions'] = self.select_questions
        if self.template_option_map is not None:
            result['TemplateOptionMap'] = self.template_option_map
        if self.template_relation_id is not None:
            result['TemplateRelationId'] = self.template_relation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('RobotConfig') is not None:
            self.robot_config = m.get('RobotConfig')
        if m.get('SelectQuestions') is not None:
            self.select_questions = m.get('SelectQuestions')
        if m.get('TemplateOptionMap') is not None:
            self.template_option_map = m.get('TemplateOptionMap')
        if m.get('TemplateRelationId') is not None:
            self.template_relation_id = m.get('TemplateRelationId')
        return self


class TaskDetailTaskWorkflow(TeaModel):
    def __init__(self, exif=None, groups=None, node_name=None, users=None):
        self.exif = exif  # type: dict[str, any]
        self.groups = groups  # type: list[str]
        self.node_name = node_name  # type: str
        self.users = users  # type: list[SimpleUser]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TaskDetailTaskWorkflow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = SimpleUser()
                self.users.append(temp_model.from_map(k))
        return self


class TaskDetail(TeaModel):
    def __init__(self, admins=None, alert_time=None, allow_append_data=None, archived=None, archived_infos=None,
                 assign_config=None, creator=None, dataset_proxy_relations=None, exif=None, gmt_create_time=None,
                 gmt_modified_time=None, label_style=None, mine_configs=None, modifier=None, notice_config=None, period_config=None,
                 ref_task_id=None, relate_task_config=None, remark=None, result_callback_config=None, stage=None, status=None,
                 tags=None, task_id=None, task_name=None, task_template_config=None, task_type=None, task_workflow=None,
                 template_id=None, tenant_id=None, tenant_name=None, uuid=None, vote_configs=None, workflow_nodes=None,
                 run_msg=None):
        self.admins = admins  # type: list[SimpleUser]
        self.alert_time = alert_time  # type: long
        self.allow_append_data = allow_append_data  # type: bool
        self.archived = archived  # type: bool
        self.archived_infos = archived_infos  # type: str
        self.assign_config = assign_config  # type: dict[str, any]
        self.creator = creator  # type: SimpleUser
        self.dataset_proxy_relations = dataset_proxy_relations  # type: list[TaskDetailDatasetProxyRelations]
        self.exif = exif  # type: dict[str, any]
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.label_style = label_style  # type: str
        self.mine_configs = mine_configs  # type: dict[str, any]
        self.modifier = modifier  # type: SimpleUser
        self.notice_config = notice_config  # type: dict[str, any]
        self.period_config = period_config  # type: dict[str, any]
        self.ref_task_id = ref_task_id  # type: str
        self.relate_task_config = relate_task_config  # type: dict[str, any]
        self.remark = remark  # type: str
        self.result_callback_config = result_callback_config  # type: dict[str, any]
        self.stage = stage  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: list[str]
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str
        self.task_template_config = task_template_config  # type: TaskDetailTaskTemplateConfig
        self.task_type = task_type  # type: str
        self.task_workflow = task_workflow  # type: list[TaskDetailTaskWorkflow]
        self.template_id = template_id  # type: str
        self.tenant_id = tenant_id  # type: str
        self.tenant_name = tenant_name  # type: str
        self.uuid = uuid  # type: str
        self.vote_configs = vote_configs  # type: dict[str, any]
        self.workflow_nodes = workflow_nodes  # type: list[str]
        self.run_msg = run_msg  # type: str

    def validate(self):
        if self.admins:
            for k in self.admins:
                if k:
                    k.validate()
        if self.creator:
            self.creator.validate()
        if self.dataset_proxy_relations:
            for k in self.dataset_proxy_relations:
                if k:
                    k.validate()
        if self.modifier:
            self.modifier.validate()
        if self.task_template_config:
            self.task_template_config.validate()
        if self.task_workflow:
            for k in self.task_workflow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TaskDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Admins'] = []
        if self.admins is not None:
            for k in self.admins:
                result['Admins'].append(k.to_map() if k else None)
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time
        if self.allow_append_data is not None:
            result['AllowAppendData'] = self.allow_append_data
        if self.archived is not None:
            result['Archived'] = self.archived
        if self.archived_infos is not None:
            result['ArchivedInfos'] = self.archived_infos
        if self.assign_config is not None:
            result['AssignConfig'] = self.assign_config
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        result['DatasetProxyRelations'] = []
        if self.dataset_proxy_relations is not None:
            for k in self.dataset_proxy_relations:
                result['DatasetProxyRelations'].append(k.to_map() if k else None)
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.label_style is not None:
            result['LabelStyle'] = self.label_style
        if self.mine_configs is not None:
            result['MineConfigs'] = self.mine_configs
        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()
        if self.notice_config is not None:
            result['NoticeConfig'] = self.notice_config
        if self.period_config is not None:
            result['PeriodConfig'] = self.period_config
        if self.ref_task_id is not None:
            result['RefTaskId'] = self.ref_task_id
        if self.relate_task_config is not None:
            result['RelateTaskConfig'] = self.relate_task_config
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.result_callback_config is not None:
            result['ResultCallbackConfig'] = self.result_callback_config
        if self.stage is not None:
            result['Stage'] = self.stage
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_template_config is not None:
            result['TaskTemplateConfig'] = self.task_template_config.to_map()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        result['TaskWorkflow'] = []
        if self.task_workflow is not None:
            for k in self.task_workflow:
                result['TaskWorkflow'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.uuid is not None:
            result['UUID'] = self.uuid
        if self.vote_configs is not None:
            result['VoteConfigs'] = self.vote_configs
        if self.workflow_nodes is not None:
            result['WorkflowNodes'] = self.workflow_nodes
        if self.run_msg is not None:
            result['runMsg'] = self.run_msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.admins = []
        if m.get('Admins') is not None:
            for k in m.get('Admins'):
                temp_model = SimpleUser()
                self.admins.append(temp_model.from_map(k))
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')
        if m.get('AllowAppendData') is not None:
            self.allow_append_data = m.get('AllowAppendData')
        if m.get('Archived') is not None:
            self.archived = m.get('Archived')
        if m.get('ArchivedInfos') is not None:
            self.archived_infos = m.get('ArchivedInfos')
        if m.get('AssignConfig') is not None:
            self.assign_config = m.get('AssignConfig')
        if m.get('Creator') is not None:
            temp_model = SimpleUser()
            self.creator = temp_model.from_map(m['Creator'])
        self.dataset_proxy_relations = []
        if m.get('DatasetProxyRelations') is not None:
            for k in m.get('DatasetProxyRelations'):
                temp_model = TaskDetailDatasetProxyRelations()
                self.dataset_proxy_relations.append(temp_model.from_map(k))
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LabelStyle') is not None:
            self.label_style = m.get('LabelStyle')
        if m.get('MineConfigs') is not None:
            self.mine_configs = m.get('MineConfigs')
        if m.get('Modifier') is not None:
            temp_model = SimpleUser()
            self.modifier = temp_model.from_map(m['Modifier'])
        if m.get('NoticeConfig') is not None:
            self.notice_config = m.get('NoticeConfig')
        if m.get('PeriodConfig') is not None:
            self.period_config = m.get('PeriodConfig')
        if m.get('RefTaskId') is not None:
            self.ref_task_id = m.get('RefTaskId')
        if m.get('RelateTaskConfig') is not None:
            self.relate_task_config = m.get('RelateTaskConfig')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResultCallbackConfig') is not None:
            self.result_callback_config = m.get('ResultCallbackConfig')
        if m.get('Stage') is not None:
            self.stage = m.get('Stage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskTemplateConfig') is not None:
            temp_model = TaskDetailTaskTemplateConfig()
            self.task_template_config = temp_model.from_map(m['TaskTemplateConfig'])
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        self.task_workflow = []
        if m.get('TaskWorkflow') is not None:
            for k in m.get('TaskWorkflow'):
                temp_model = TaskDetailTaskWorkflow()
                self.task_workflow.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        if m.get('VoteConfigs') is not None:
            self.vote_configs = m.get('VoteConfigs')
        if m.get('WorkflowNodes') is not None:
            self.workflow_nodes = m.get('WorkflowNodes')
        if m.get('runMsg') is not None:
            self.run_msg = m.get('runMsg')
        return self


class TaskStatistic(TeaModel):
    def __init__(self, accept_item_count=None, check_abandon=None, check_accuracy=None, check_efficiency=None,
                 checked_accuracy=None, checked_error=None, checked_reject_count=None, final_abandon_count=None,
                 finished_item_count=None, finished_subtask_count=None, mark_efficiency=None, pre_mark_fixed_count=None,
                 sampled_accuracy=None, sampled_error_count=None, sampled_reject_count=None, sampling_accuracy=None,
                 total_check_count=None, total_check_time=None, total_checked_count=None, total_item_count=None,
                 total_mark_time=None, total_sampled_count=None, total_sampling_count=None, total_subtask_count=None,
                 total_work_time=None):
        self.accept_item_count = accept_item_count  # type: float
        self.check_abandon = check_abandon  # type: float
        self.check_accuracy = check_accuracy  # type: float
        self.check_efficiency = check_efficiency  # type: float
        self.checked_accuracy = checked_accuracy  # type: float
        self.checked_error = checked_error  # type: float
        self.checked_reject_count = checked_reject_count  # type: float
        self.final_abandon_count = final_abandon_count  # type: float
        self.finished_item_count = finished_item_count  # type: long
        self.finished_subtask_count = finished_subtask_count  # type: long
        self.mark_efficiency = mark_efficiency  # type: float
        self.pre_mark_fixed_count = pre_mark_fixed_count  # type: float
        self.sampled_accuracy = sampled_accuracy  # type: float
        self.sampled_error_count = sampled_error_count  # type: float
        self.sampled_reject_count = sampled_reject_count  # type: float
        self.sampling_accuracy = sampling_accuracy  # type: float
        self.total_check_count = total_check_count  # type: float
        self.total_check_time = total_check_time  # type: float
        self.total_checked_count = total_checked_count  # type: float
        self.total_item_count = total_item_count  # type: long
        self.total_mark_time = total_mark_time  # type: float
        self.total_sampled_count = total_sampled_count  # type: float
        self.total_sampling_count = total_sampling_count  # type: float
        self.total_subtask_count = total_subtask_count  # type: long
        self.total_work_time = total_work_time  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskStatistic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_item_count is not None:
            result['AcceptItemCount'] = self.accept_item_count
        if self.check_abandon is not None:
            result['CheckAbandon'] = self.check_abandon
        if self.check_accuracy is not None:
            result['CheckAccuracy'] = self.check_accuracy
        if self.check_efficiency is not None:
            result['CheckEfficiency'] = self.check_efficiency
        if self.checked_accuracy is not None:
            result['CheckedAccuracy'] = self.checked_accuracy
        if self.checked_error is not None:
            result['CheckedError'] = self.checked_error
        if self.checked_reject_count is not None:
            result['CheckedRejectCount'] = self.checked_reject_count
        if self.final_abandon_count is not None:
            result['FinalAbandonCount'] = self.final_abandon_count
        if self.finished_item_count is not None:
            result['FinishedItemCount'] = self.finished_item_count
        if self.finished_subtask_count is not None:
            result['FinishedSubtaskCount'] = self.finished_subtask_count
        if self.mark_efficiency is not None:
            result['MarkEfficiency'] = self.mark_efficiency
        if self.pre_mark_fixed_count is not None:
            result['PreMarkFixedCount'] = self.pre_mark_fixed_count
        if self.sampled_accuracy is not None:
            result['SampledAccuracy'] = self.sampled_accuracy
        if self.sampled_error_count is not None:
            result['SampledErrorCount'] = self.sampled_error_count
        if self.sampled_reject_count is not None:
            result['SampledRejectCount'] = self.sampled_reject_count
        if self.sampling_accuracy is not None:
            result['SamplingAccuracy'] = self.sampling_accuracy
        if self.total_check_count is not None:
            result['TotalCheckCount'] = self.total_check_count
        if self.total_check_time is not None:
            result['TotalCheckTime'] = self.total_check_time
        if self.total_checked_count is not None:
            result['TotalCheckedCount'] = self.total_checked_count
        if self.total_item_count is not None:
            result['TotalItemCount'] = self.total_item_count
        if self.total_mark_time is not None:
            result['TotalMarkTime'] = self.total_mark_time
        if self.total_sampled_count is not None:
            result['TotalSampledCount'] = self.total_sampled_count
        if self.total_sampling_count is not None:
            result['TotalSamplingCount'] = self.total_sampling_count
        if self.total_subtask_count is not None:
            result['TotalSubtaskCount'] = self.total_subtask_count
        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptItemCount') is not None:
            self.accept_item_count = m.get('AcceptItemCount')
        if m.get('CheckAbandon') is not None:
            self.check_abandon = m.get('CheckAbandon')
        if m.get('CheckAccuracy') is not None:
            self.check_accuracy = m.get('CheckAccuracy')
        if m.get('CheckEfficiency') is not None:
            self.check_efficiency = m.get('CheckEfficiency')
        if m.get('CheckedAccuracy') is not None:
            self.checked_accuracy = m.get('CheckedAccuracy')
        if m.get('CheckedError') is not None:
            self.checked_error = m.get('CheckedError')
        if m.get('CheckedRejectCount') is not None:
            self.checked_reject_count = m.get('CheckedRejectCount')
        if m.get('FinalAbandonCount') is not None:
            self.final_abandon_count = m.get('FinalAbandonCount')
        if m.get('FinishedItemCount') is not None:
            self.finished_item_count = m.get('FinishedItemCount')
        if m.get('FinishedSubtaskCount') is not None:
            self.finished_subtask_count = m.get('FinishedSubtaskCount')
        if m.get('MarkEfficiency') is not None:
            self.mark_efficiency = m.get('MarkEfficiency')
        if m.get('PreMarkFixedCount') is not None:
            self.pre_mark_fixed_count = m.get('PreMarkFixedCount')
        if m.get('SampledAccuracy') is not None:
            self.sampled_accuracy = m.get('SampledAccuracy')
        if m.get('SampledErrorCount') is not None:
            self.sampled_error_count = m.get('SampledErrorCount')
        if m.get('SampledRejectCount') is not None:
            self.sampled_reject_count = m.get('SampledRejectCount')
        if m.get('SamplingAccuracy') is not None:
            self.sampling_accuracy = m.get('SamplingAccuracy')
        if m.get('TotalCheckCount') is not None:
            self.total_check_count = m.get('TotalCheckCount')
        if m.get('TotalCheckTime') is not None:
            self.total_check_time = m.get('TotalCheckTime')
        if m.get('TotalCheckedCount') is not None:
            self.total_checked_count = m.get('TotalCheckedCount')
        if m.get('TotalItemCount') is not None:
            self.total_item_count = m.get('TotalItemCount')
        if m.get('TotalMarkTime') is not None:
            self.total_mark_time = m.get('TotalMarkTime')
        if m.get('TotalSampledCount') is not None:
            self.total_sampled_count = m.get('TotalSampledCount')
        if m.get('TotalSamplingCount') is not None:
            self.total_sampling_count = m.get('TotalSamplingCount')
        if m.get('TotalSubtaskCount') is not None:
            self.total_subtask_count = m.get('TotalSubtaskCount')
        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')
        return self


class TaskTemplateConfig(TeaModel):
    def __init__(self, exif=None, resource_key=None, select_questions=None, template_option_map=None,
                 template_relation_id=None):
        self.exif = exif  # type: dict[str, str]
        self.resource_key = resource_key  # type: str
        self.select_questions = select_questions  # type: list[str]
        self.template_option_map = template_option_map  # type: dict[str, str]
        self.template_relation_id = template_relation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskTemplateConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
        if self.select_questions is not None:
            result['SelectQuestions'] = self.select_questions
        if self.template_option_map is not None:
            result['TemplateOptionMap'] = self.template_option_map
        if self.template_relation_id is not None:
            result['TemplateRelationId'] = self.template_relation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')
        if m.get('SelectQuestions') is not None:
            self.select_questions = m.get('SelectQuestions')
        if m.get('TemplateOptionMap') is not None:
            self.template_option_map = m.get('TemplateOptionMap')
        if m.get('TemplateRelationId') is not None:
            self.template_relation_id = m.get('TemplateRelationId')
        return self


class TemplateDTOViewConfigs(TeaModel):
    def __init__(self, view_plugins=None):
        self.view_plugins = view_plugins  # type: list[ViewPlugin]

    def validate(self):
        if self.view_plugins:
            for k in self.view_plugins:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TemplateDTOViewConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ViewPlugins'] = []
        if self.view_plugins is not None:
            for k in self.view_plugins:
                result['ViewPlugins'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.view_plugins = []
        if m.get('ViewPlugins') is not None:
            for k in m.get('ViewPlugins'):
                temp_model = ViewPlugin()
                self.view_plugins.append(temp_model.from_map(k))
        return self


class TemplateDTO(TeaModel):
    def __init__(self, classify=None, description=None, exif=None, question_configs=None, robot_configs=None,
                 shared_mode=None, tags=None, template_id=None, template_name=None, view_configs=None):
        self.classify = classify  # type: str
        self.description = description  # type: str
        self.exif = exif  # type: dict[str, any]
        self.question_configs = question_configs  # type: list[QuestionPlugin]
        self.robot_configs = robot_configs  # type: list[dict[str, any]]
        self.shared_mode = shared_mode  # type: str
        self.tags = tags  # type: list[str]
        self.template_id = template_id  # type: str
        self.template_name = template_name  # type: str
        self.view_configs = view_configs  # type: TemplateDTOViewConfigs

    def validate(self):
        if self.question_configs:
            for k in self.question_configs:
                if k:
                    k.validate()
        if self.view_configs:
            self.view_configs.validate()

    def to_map(self):
        _map = super(TemplateDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.description is not None:
            result['Description'] = self.description
        if self.exif is not None:
            result['Exif'] = self.exif
        result['QuestionConfigs'] = []
        if self.question_configs is not None:
            for k in self.question_configs:
                result['QuestionConfigs'].append(k.to_map() if k else None)
        if self.robot_configs is not None:
            result['RobotConfigs'] = self.robot_configs
        if self.shared_mode is not None:
            result['SharedMode'] = self.shared_mode
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.view_configs is not None:
            result['ViewConfigs'] = self.view_configs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        self.question_configs = []
        if m.get('QuestionConfigs') is not None:
            for k in m.get('QuestionConfigs'):
                temp_model = QuestionPlugin()
                self.question_configs.append(temp_model.from_map(k))
        if m.get('RobotConfigs') is not None:
            self.robot_configs = m.get('RobotConfigs')
        if m.get('SharedMode') is not None:
            self.shared_mode = m.get('SharedMode')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('ViewConfigs') is not None:
            temp_model = TemplateDTOViewConfigs()
            self.view_configs = temp_model.from_map(m['ViewConfigs'])
        return self


class TemplateDetailViewConfigs(TeaModel):
    def __init__(self, view_plugins=None):
        self.view_plugins = view_plugins  # type: list[ViewPlugin]

    def validate(self):
        if self.view_plugins:
            for k in self.view_plugins:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TemplateDetailViewConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ViewPlugins'] = []
        if self.view_plugins is not None:
            for k in self.view_plugins:
                result['ViewPlugins'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.view_plugins = []
        if m.get('ViewPlugins') is not None:
            for k in m.get('ViewPlugins'):
                temp_model = ViewPlugin()
                self.view_plugins.append(temp_model.from_map(k))
        return self


class TemplateDetail(TeaModel):
    def __init__(self, abandon_reasons=None, classify=None, creator=None, description=None, exif=None,
                 gmt_create_time=None, gmt_modified_time=None, modifier=None, question_configs=None, shared_mode=None, status=None,
                 tags=None, template_id=None, template_name=None, tenant_id=None, type=None, view_configs=None):
        self.abandon_reasons = abandon_reasons  # type: list[str]
        self.classify = classify  # type: str
        self.creator = creator  # type: SimpleUser
        self.description = description  # type: str
        self.exif = exif  # type: dict[str, any]
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.modifier = modifier  # type: SimpleUser
        self.question_configs = question_configs  # type: list[QuestionPlugin]
        self.shared_mode = shared_mode  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: list[str]
        self.template_id = template_id  # type: str
        self.template_name = template_name  # type: str
        self.tenant_id = tenant_id  # type: str
        self.type = type  # type: str
        self.view_configs = view_configs  # type: TemplateDetailViewConfigs

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()
        if self.question_configs:
            for k in self.question_configs:
                if k:
                    k.validate()
        if self.view_configs:
            self.view_configs.validate()

    def to_map(self):
        _map = super(TemplateDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandon_reasons is not None:
            result['AbandonReasons'] = self.abandon_reasons
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()
        result['QuestionConfigs'] = []
        if self.question_configs is not None:
            for k in self.question_configs:
                result['QuestionConfigs'].append(k.to_map() if k else None)
        if self.shared_mode is not None:
            result['SharedMode'] = self.shared_mode
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.view_configs is not None:
            result['ViewConfigs'] = self.view_configs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AbandonReasons') is not None:
            self.abandon_reasons = m.get('AbandonReasons')
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('Creator') is not None:
            temp_model = SimpleUser()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Modifier') is not None:
            temp_model = SimpleUser()
            self.modifier = temp_model.from_map(m['Modifier'])
        self.question_configs = []
        if m.get('QuestionConfigs') is not None:
            for k in m.get('QuestionConfigs'):
                temp_model = QuestionPlugin()
                self.question_configs.append(temp_model.from_map(k))
        if m.get('SharedMode') is not None:
            self.shared_mode = m.get('SharedMode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ViewConfigs') is not None:
            temp_model = TemplateDetailViewConfigs()
            self.view_configs = temp_model.from_map(m['ViewConfigs'])
        return self


class TemplateQuestion(TeaModel):
    def __init__(self, children=None, exif=None, mark_title=None, options=None, pre_options=None, question_id=None,
                 type=None):
        self.children = children  # type: list[TemplateQuestion]
        self.exif = exif  # type: dict[str, any]
        self.mark_title = mark_title  # type: str
        self.options = options  # type: list[QuestionOption]
        self.pre_options = pre_options  # type: list[str]
        self.question_id = question_id  # type: long
        self.type = type  # type: str

    def validate(self):
        if self.children:
            for k in self.children:
                if k:
                    k.validate()
        if self.options:
            for k in self.options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TemplateQuestion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Children'] = []
        if self.children is not None:
            for k in self.children:
                result['Children'].append(k.to_map() if k else None)
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.mark_title is not None:
            result['MarkTitle'] = self.mark_title
        result['Options'] = []
        if self.options is not None:
            for k in self.options:
                result['Options'].append(k.to_map() if k else None)
        if self.pre_options is not None:
            result['PreOptions'] = self.pre_options
        if self.question_id is not None:
            result['QuestionId'] = self.question_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k in m.get('Children'):
                temp_model = TemplateQuestion()
                self.children.append(temp_model.from_map(k))
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('MarkTitle') is not None:
            self.mark_title = m.get('MarkTitle')
        self.options = []
        if m.get('Options') is not None:
            for k in m.get('Options'):
                temp_model = QuestionOption()
                self.options.append(temp_model.from_map(k))
        if m.get('PreOptions') is not None:
            self.pre_options = m.get('PreOptions')
        if m.get('QuestionId') is not None:
            self.question_id = m.get('QuestionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class TemplateViewFieldsVisitInfo(TeaModel):
    def __init__(self, afts_conf=None, oss_conf=None):
        self.afts_conf = afts_conf  # type: dict[str, any]
        self.oss_conf = oss_conf  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(TemplateViewFieldsVisitInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.afts_conf is not None:
            result['AftsConf'] = self.afts_conf
        if self.oss_conf is not None:
            result['OssConf'] = self.oss_conf
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AftsConf') is not None:
            self.afts_conf = m.get('AftsConf')
        if m.get('OssConf') is not None:
            self.oss_conf = m.get('OssConf')
        return self


class TemplateViewFields(TeaModel):
    def __init__(self, display_ori_img=None, field_name=None, type=None, visit_info=None):
        self.display_ori_img = display_ori_img  # type: bool
        self.field_name = field_name  # type: str
        self.type = type  # type: str
        self.visit_info = visit_info  # type: TemplateViewFieldsVisitInfo

    def validate(self):
        if self.visit_info:
            self.visit_info.validate()

    def to_map(self):
        _map = super(TemplateViewFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_ori_img is not None:
            result['DisplayOriImg'] = self.display_ori_img
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.type is not None:
            result['Type'] = self.type
        if self.visit_info is not None:
            result['VisitInfo'] = self.visit_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayOriImg') is not None:
            self.display_ori_img = m.get('DisplayOriImg')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VisitInfo') is not None:
            temp_model = TemplateViewFieldsVisitInfo()
            self.visit_info = temp_model.from_map(m['VisitInfo'])
        return self


class TemplateView(TeaModel):
    def __init__(self, fields=None):
        self.fields = fields  # type: list[TemplateViewFields]

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TemplateView, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = TemplateViewFields()
                self.fields.append(temp_model.from_map(k))
        return self


class UpdateTaskDTO(TeaModel):
    def __init__(self, exif=None, remark=None, tags=None, task_name=None):
        self.exif = exif  # type: dict[str, str]
        self.remark = remark  # type: str
        self.tags = tags  # type: list[str]
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTaskDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class UserStatistic(TeaModel):
    def __init__(self, accepted_mark_items_count=None, check_count=None, checked_accepted_count=None,
                 checked_accuracy=None, mark_efficiency=None, mark_time=None, sampling_accuracy=None, sampling_count=None,
                 sampling_error_count=None, total_mark_items_count=None, user_id=None):
        self.accepted_mark_items_count = accepted_mark_items_count  # type: float
        self.check_count = check_count  # type: float
        self.checked_accepted_count = checked_accepted_count  # type: float
        self.checked_accuracy = checked_accuracy  # type: float
        self.mark_efficiency = mark_efficiency  # type: float
        self.mark_time = mark_time  # type: float
        self.sampling_accuracy = sampling_accuracy  # type: float
        self.sampling_count = sampling_count  # type: float
        self.sampling_error_count = sampling_error_count  # type: float
        self.total_mark_items_count = total_mark_items_count  # type: float
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UserStatistic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accepted_mark_items_count is not None:
            result['AcceptedMarkItemsCount'] = self.accepted_mark_items_count
        if self.check_count is not None:
            result['CheckCount'] = self.check_count
        if self.checked_accepted_count is not None:
            result['CheckedAcceptedCount'] = self.checked_accepted_count
        if self.checked_accuracy is not None:
            result['CheckedAccuracy'] = self.checked_accuracy
        if self.mark_efficiency is not None:
            result['MarkEfficiency'] = self.mark_efficiency
        if self.mark_time is not None:
            result['MarkTime'] = self.mark_time
        if self.sampling_accuracy is not None:
            result['SamplingAccuracy'] = self.sampling_accuracy
        if self.sampling_count is not None:
            result['SamplingCount'] = self.sampling_count
        if self.sampling_error_count is not None:
            result['SamplingErrorCount'] = self.sampling_error_count
        if self.total_mark_items_count is not None:
            result['TotalMarkItemsCount'] = self.total_mark_items_count
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptedMarkItemsCount') is not None:
            self.accepted_mark_items_count = m.get('AcceptedMarkItemsCount')
        if m.get('CheckCount') is not None:
            self.check_count = m.get('CheckCount')
        if m.get('CheckedAcceptedCount') is not None:
            self.checked_accepted_count = m.get('CheckedAcceptedCount')
        if m.get('CheckedAccuracy') is not None:
            self.checked_accuracy = m.get('CheckedAccuracy')
        if m.get('MarkEfficiency') is not None:
            self.mark_efficiency = m.get('MarkEfficiency')
        if m.get('MarkTime') is not None:
            self.mark_time = m.get('MarkTime')
        if m.get('SamplingAccuracy') is not None:
            self.sampling_accuracy = m.get('SamplingAccuracy')
        if m.get('SamplingCount') is not None:
            self.sampling_count = m.get('SamplingCount')
        if m.get('SamplingErrorCount') is not None:
            self.sampling_error_count = m.get('SamplingErrorCount')
        if m.get('TotalMarkItemsCount') is not None:
            self.total_mark_items_count = m.get('TotalMarkItemsCount')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ViewPluginVisitInfo(TeaModel):
    def __init__(self, afts_conf=None, oss_conf=None):
        self.afts_conf = afts_conf  # type: dict[str, any]
        self.oss_conf = oss_conf  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ViewPluginVisitInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.afts_conf is not None:
            result['aftsConf'] = self.afts_conf
        if self.oss_conf is not None:
            result['ossConf'] = self.oss_conf
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aftsConf') is not None:
            self.afts_conf = m.get('aftsConf')
        if m.get('ossConf') is not None:
            self.oss_conf = m.get('ossConf')
        return self


class ViewPlugin(TeaModel):
    def __init__(self, bind_field=None, convertor=None, cors_proxy=None, display_ori_img=None, exif=None, hide=None,
                 plugins=None, relation_question_ids=None, type=None, visit_info=None):
        self.bind_field = bind_field  # type: str
        self.convertor = convertor  # type: str
        self.cors_proxy = cors_proxy  # type: bool
        self.display_ori_img = display_ori_img  # type: bool
        self.exif = exif  # type: dict[str, any]
        self.hide = hide  # type: bool
        self.plugins = plugins  # type: dict[str, any]
        self.relation_question_ids = relation_question_ids  # type: list[str]
        self.type = type  # type: str
        self.visit_info = visit_info  # type: ViewPluginVisitInfo

    def validate(self):
        if self.visit_info:
            self.visit_info.validate()

    def to_map(self):
        _map = super(ViewPlugin, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_field is not None:
            result['BindField'] = self.bind_field
        if self.convertor is not None:
            result['Convertor'] = self.convertor
        if self.cors_proxy is not None:
            result['CorsProxy'] = self.cors_proxy
        if self.display_ori_img is not None:
            result['DisplayOriImg'] = self.display_ori_img
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.hide is not None:
            result['Hide'] = self.hide
        if self.plugins is not None:
            result['Plugins'] = self.plugins
        if self.relation_question_ids is not None:
            result['RelationQuestionIds'] = self.relation_question_ids
        if self.type is not None:
            result['Type'] = self.type
        if self.visit_info is not None:
            result['VisitInfo'] = self.visit_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindField') is not None:
            self.bind_field = m.get('BindField')
        if m.get('Convertor') is not None:
            self.convertor = m.get('Convertor')
        if m.get('CorsProxy') is not None:
            self.cors_proxy = m.get('CorsProxy')
        if m.get('DisplayOriImg') is not None:
            self.display_ori_img = m.get('DisplayOriImg')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('Hide') is not None:
            self.hide = m.get('Hide')
        if m.get('Plugins') is not None:
            self.plugins = m.get('Plugins')
        if m.get('RelationQuestionIds') is not None:
            self.relation_question_ids = m.get('RelationQuestionIds')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VisitInfo') is not None:
            temp_model = ViewPluginVisitInfo()
            self.visit_info = temp_model.from_map(m['VisitInfo'])
        return self


class Workforce(TeaModel):
    def __init__(self, node_type=None, users=None, work_node_id=None):
        self.node_type = node_type  # type: str
        self.users = users  # type: list[SimpleUser]
        self.work_node_id = work_node_id  # type: int

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Workforce, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        if self.work_node_id is not None:
            result['WorkNodeId'] = self.work_node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = SimpleUser()
                self.users.append(temp_model.from_map(k))
        if m.get('WorkNodeId') is not None:
            self.work_node_id = m.get('WorkNodeId')
        return self


class AddWorkNodeWorkforceRequest(TeaModel):
    def __init__(self, user_ids=None):
        self.user_ids = user_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkNodeWorkforceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class AddWorkNodeWorkforceResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWorkNodeWorkforceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
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
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddWorkNodeWorkforceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddWorkNodeWorkforceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddWorkNodeWorkforceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddWorkNodeWorkforceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: CreateTaskDetail

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateTaskDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, task_id=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: TemplateDTO

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = TemplateDTO()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, template_id=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequest(TeaModel):
    def __init__(self, account_no=None, account_type=None, role=None, user_name=None):
        self.account_no = account_no  # type: str
        self.account_type = account_type  # type: str
        self.role = role  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_no is not None:
            result['AccountNo'] = self.account_no
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.role is not None:
            result['Role'] = self.role
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, user_id=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTaskResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
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
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, template_id=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
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
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportAnnotationsRequest(TeaModel):
    def __init__(self, oss_path=None, register_dataset=None, target=None):
        self.oss_path = oss_path  # type: str
        self.register_dataset = register_dataset  # type: str
        self.target = target  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportAnnotationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.register_dataset is not None:
            result['RegisterDataset'] = self.register_dataset
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('RegisterDataset') is not None:
            self.register_dataset = m.get('RegisterDataset')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ExportAnnotationsResponseBody(TeaModel):
    def __init__(self, code=None, details=None, flow_job=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.flow_job = flow_job  # type: FlowJobInfo
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.flow_job:
            self.flow_job.validate()

    def to_map(self):
        _map = super(ExportAnnotationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.flow_job is not None:
            result['FlowJob'] = self.flow_job.to_map()
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
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('FlowJob') is not None:
            temp_model = FlowJobInfo()
            self.flow_job = temp_model.from_map(m['FlowJob'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportAnnotationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExportAnnotationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportAnnotationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExportAnnotationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRequest(TeaModel):
    def __init__(self, job_type=None):
        self.job_type = job_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_type is not None:
            result['JobType'] = self.job_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(self, code=None, details=None, job=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.job = job  # type: Job
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super(GetJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.job is not None:
            result['Job'] = self.job.to_map()
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
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Job') is not None:
            temp_model = Job()
            self.job = temp_model.from_map(m['Job'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubtaskResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, subtask=None, success=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.subtask = subtask  # type: SimpleSubtask
        self.success = success  # type: bool

    def validate(self):
        if self.subtask:
            self.subtask.validate()

    def to_map(self):
        _map = super(GetSubtaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subtask is not None:
            result['Subtask'] = self.subtask.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Subtask') is not None:
            temp_model = SimpleSubtask()
            self.subtask = temp_model.from_map(m['Subtask'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSubtaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSubtaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSubtaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSubtaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubtaskItemResponseBody(TeaModel):
    def __init__(self, code=None, details=None, item=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.item = item  # type: SubtaskItemDetail
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        _map = super(GetSubtaskItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.item is not None:
            result['Item'] = self.item.to_map()
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
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Item') is not None:
            temp_model = SubtaskItemDetail()
            self.item = temp_model.from_map(m['Item'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSubtaskItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSubtaskItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSubtaskItemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSubtaskItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, task=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.task = task  # type: TaskDetail

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super(GetTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task is not None:
            result['Task'] = self.task.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Task') is not None:
            temp_model = TaskDetail()
            self.task = temp_model.from_map(m['Task'])
        return self


class GetTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskStatisticsRequest(TeaModel):
    def __init__(self, stat_type=None):
        self.stat_type = stat_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stat_type is not None:
            result['StatType'] = self.stat_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StatType') is not None:
            self.stat_type = m.get('StatType')
        return self


class GetTaskStatisticsResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, task_statistics=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.task_statistics = task_statistics  # type: TaskStatistic

    def validate(self):
        if self.task_statistics:
            self.task_statistics.validate()

    def to_map(self):
        _map = super(GetTaskStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_statistics is not None:
            result['TaskStatistics'] = self.task_statistics.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskStatistics') is not None:
            temp_model = TaskStatistic()
            self.task_statistics = temp_model.from_map(m['TaskStatistics'])
        return self


class GetTaskStatisticsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskStatisticsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskStatusResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, task_status=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.task_status = task_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskTemplateResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, template=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.template = template  # type: TemplateDetail

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(GetTaskTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Template') is not None:
            temp_model = TemplateDetail()
            self.template = temp_model.from_map(m['Template'])
        return self


class GetTaskTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskTemplateQuestionsResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, questions=None, request_id=None, success=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.questions = questions  # type: list[QuestionPlugin]
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.questions:
            for k in self.questions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTaskTemplateQuestionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        result['Questions'] = []
        if self.questions is not None:
            for k in self.questions:
                result['Questions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.questions = []
        if m.get('Questions') is not None:
            for k in m.get('Questions'):
                temp_model = QuestionPlugin()
                self.questions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTaskTemplateQuestionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskTemplateQuestionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskTemplateQuestionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskTemplateQuestionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskTemplateViewsResponseBodyViews(TeaModel):
    def __init__(self, view_plugins=None):
        self.view_plugins = view_plugins  # type: list[ViewPlugin]

    def validate(self):
        if self.view_plugins:
            for k in self.view_plugins:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTaskTemplateViewsResponseBodyViews, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ViewPlugins'] = []
        if self.view_plugins is not None:
            for k in self.view_plugins:
                result['ViewPlugins'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.view_plugins = []
        if m.get('ViewPlugins') is not None:
            for k in m.get('ViewPlugins'):
                temp_model = ViewPlugin()
                self.view_plugins.append(temp_model.from_map(k))
        return self


class GetTaskTemplateViewsResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, views=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.views = views  # type: GetTaskTemplateViewsResponseBodyViews

    def validate(self):
        if self.views:
            self.views.validate()

    def to_map(self):
        _map = super(GetTaskTemplateViewsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.views is not None:
            result['Views'] = self.views.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Views') is not None:
            temp_model = GetTaskTemplateViewsResponseBodyViews()
            self.views = temp_model.from_map(m['Views'])
        return self


class GetTaskTemplateViewsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskTemplateViewsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskTemplateViewsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskTemplateViewsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskWorkforceResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, workforce=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.workforce = workforce  # type: list[Workforce]

    def validate(self):
        if self.workforce:
            for k in self.workforce:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTaskWorkforceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['Workforce'] = []
        if self.workforce is not None:
            for k in self.workforce:
                result['Workforce'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.workforce = []
        if m.get('Workforce') is not None:
            for k in m.get('Workforce'):
                temp_model = Workforce()
                self.workforce.append(temp_model.from_map(k))
        return self


class GetTaskWorkforceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskWorkforceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskWorkforceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskWorkforceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskWorkforceStatisticRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, stat_type=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.stat_type = stat_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskWorkforceStatisticRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.stat_type is not None:
            result['StatType'] = self.stat_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StatType') is not None:
            self.stat_type = m.get('StatType')
        return self


class GetTaskWorkforceStatisticResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, total_count=None, total_page=None, users_statistic=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int
        self.users_statistic = users_statistic  # type: list[UserStatistic]

    def validate(self):
        if self.users_statistic:
            for k in self.users_statistic:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTaskWorkforceStatisticResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        result['UsersStatistic'] = []
        if self.users_statistic is not None:
            for k in self.users_statistic:
                result['UsersStatistic'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        self.users_statistic = []
        if m.get('UsersStatistic') is not None:
            for k in m.get('UsersStatistic'):
                temp_model = UserStatistic()
                self.users_statistic.append(temp_model.from_map(k))
        return self


class GetTaskWorkforceStatisticResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskWorkforceStatisticResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTaskWorkforceStatisticResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskWorkforceStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, template=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.template = template  # type: TemplateDetail

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(GetTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Template') is not None:
            temp_model = TemplateDetail()
            self.template = temp_model.from_map(m['Template'])
        return self


class GetTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateQuestionsResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, question_configs=None, request_id=None, success=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.question_configs = question_configs  # type: list[QuestionPlugin]
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.question_configs:
            for k in self.question_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTemplateQuestionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        result['QuestionConfigs'] = []
        if self.question_configs is not None:
            for k in self.question_configs:
                result['QuestionConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.question_configs = []
        if m.get('QuestionConfigs') is not None:
            for k in m.get('QuestionConfigs'):
                temp_model = QuestionPlugin()
                self.question_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTemplateQuestionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTemplateQuestionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTemplateQuestionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTemplateQuestionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateViewResponseBodyViewConfigs(TeaModel):
    def __init__(self, view_plugins=None):
        self.view_plugins = view_plugins  # type: list[ViewPlugin]

    def validate(self):
        if self.view_plugins:
            for k in self.view_plugins:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTemplateViewResponseBodyViewConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ViewPlugins'] = []
        if self.view_plugins is not None:
            for k in self.view_plugins:
                result['ViewPlugins'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.view_plugins = []
        if m.get('ViewPlugins') is not None:
            for k in m.get('ViewPlugins'):
                temp_model = ViewPlugin()
                self.view_plugins.append(temp_model.from_map(k))
        return self


class GetTemplateViewResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, view_configs=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.view_configs = view_configs  # type: GetTemplateViewResponseBodyViewConfigs

    def validate(self):
        if self.view_configs:
            self.view_configs.validate()

    def to_map(self):
        _map = super(GetTemplateViewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.view_configs is not None:
            result['ViewConfigs'] = self.view_configs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ViewConfigs') is not None:
            temp_model = GetTemplateViewResponseBodyViewConfigs()
            self.view_configs = temp_model.from_map(m['ViewConfigs'])
        return self


class GetTemplateViewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTemplateViewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTemplateViewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTemplateViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTenantResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, tenant=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.tenant = tenant  # type: SingleTenant

    def validate(self):
        if self.tenant:
            self.tenant.validate()

    def to_map(self):
        _map = super(GetTenantResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.tenant is not None:
            result['Tenant'] = self.tenant.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Tenant') is not None:
            temp_model = SingleTenant()
            self.tenant = temp_model.from_map(m['Tenant'])
        return self


class GetTenantResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTenantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTenantResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, user=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.user = user  # type: SimpleUser

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super(GetUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('User') is not None:
            temp_model = SimpleUser()
            self.user = temp_model.from_map(m['User'])
        return self


class GetUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(self, job_type=None, page_number=None, page_size=None):
        self.job_type = job_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(self, code=None, details=None, jobs=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None, total_page=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.jobs = jobs  # type: list[Job]
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = Job()
                self.jobs.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListJobsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubtaskItemsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubtaskItemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSubtaskItemsResponseBody(TeaModel):
    def __init__(self, code=None, details=None, items=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None, total_page=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.items = items  # type: list[SubtaskItemDetail]
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSubtaskItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = SubtaskItemDetail()
                self.items.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListSubtaskItemsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSubtaskItemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSubtaskItemsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSubtaskItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubtasksRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubtasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSubtasksResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, page_number=None, page_size=None, request_id=None,
                 subtasks=None, success=None, total_count=None, total_page=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.subtasks = subtasks  # type: list[SubtaskDetail]
        self.success = success  # type: bool
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        if self.subtasks:
            for k in self.subtasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSubtasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Subtasks'] = []
        if self.subtasks is not None:
            for k in self.subtasks:
                result['Subtasks'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.subtasks = []
        if m.get('Subtasks') is not None:
            for k in m.get('Subtasks'):
                temp_model = SubtaskDetail()
                self.subtasks.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListSubtasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSubtasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSubtasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSubtasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, tasks=None, total_count=None, total_page=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.tasks = tasks  # type: list[SimpleTask]
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = SimpleTask()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, search_key=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.search_key = search_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, templates=None, total_count=None, total_page=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.templates = templates  # type: list[SimpleTemplate]
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = SimpleTemplate()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTemplatesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTenantsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTenantsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTenantsResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, tenants=None, total_count=None, total_page=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.tenants = tenants  # type: list[SimpleTenant]
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        if self.tenants:
            for k in self.tenants:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTenantsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['Tenants'] = []
        if self.tenants is not None:
            for k in self.tenants:
                result['Tenants'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tenants = []
        if m.get('Tenants') is not None:
            for k in m.get('Tenants'):
                temp_model = SimpleTenant()
                self.tenants.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListTenantsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTenantsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTenantsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTenantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, total_count=None, total_page=None, users=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int
        self.users = users  # type: list[SimpleUser]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = SimpleUser()
                self.users.append(temp_model.from_map(k))
        return self


class ListUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveWorkNodeWorkforceRequest(TeaModel):
    def __init__(self, user_ids=None):
        self.user_ids = user_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveWorkNodeWorkforceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class RemoveWorkNodeWorkforceResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveWorkNodeWorkforceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
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
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveWorkNodeWorkforceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveWorkNodeWorkforceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveWorkNodeWorkforceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveWorkNodeWorkforceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: UpdateTaskDTO

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UpdateTaskDTO()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
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
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskWorkforceRequest(TeaModel):
    def __init__(self, workforce=None):
        self.workforce = workforce  # type: list[SimpleWorkforce]

    def validate(self):
        if self.workforce:
            for k in self.workforce:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateTaskWorkforceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Workforce'] = []
        if self.workforce is not None:
            for k in self.workforce:
                result['Workforce'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.workforce = []
        if m.get('Workforce') is not None:
            for k in m.get('Workforce'):
                temp_model = SimpleWorkforce()
                self.workforce.append(temp_model.from_map(k))
        return self


class UpdateTaskWorkforceResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTaskWorkforceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
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
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTaskWorkforceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTaskWorkforceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTaskWorkforceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTaskWorkforceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: TemplateDTO

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = TemplateDTO()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, template_id=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTenantRequest(TeaModel):
    def __init__(self, description=None, tenant_name=None):
        self.description = description  # type: str
        self.tenant_name = tenant_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTenantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        return self


class UpdateTenantResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTenantResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
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
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTenantResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTenantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTenantResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(self, role=None, user_name=None):
        self.role = role  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role is not None:
            result['Role'] = self.role
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(self, code=None, details=None, message=None, request_id=None, success=None, user_id=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


