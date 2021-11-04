# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddEditingProjectMaterialsRequest(TeaModel):
    def __init__(self, material_maps=None, project_id=None):
        # 素材ID
        self.material_maps = material_maps  # type: str
        # 云剪辑工程ID
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEditingProjectMaterialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_maps is not None:
            result['MaterialMaps'] = self.material_maps
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaterialMaps') is not None:
            self.material_maps = m.get('MaterialMaps')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class AddEditingProjectMaterialsResponseBodyLiveMaterials(TeaModel):
    def __init__(self, app_name=None, domain_name=None, live_url=None, stream_name=None):
        self.app_name = app_name  # type: str
        self.domain_name = domain_name  # type: str
        self.live_url = live_url  # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEditingProjectMaterialsResponseBodyLiveMaterials, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(self, bitrate=None, duration=None, file_name=None, file_size=None, file_status=None, file_type=None,
                 file_url=None, format_name=None, height=None, region=None, width=None):
        # 码率
        self.bitrate = bitrate  # type: str
        # 时长
        self.duration = duration  # type: str
        # 文件名
        self.file_name = file_name  # type: str
        # 文件大小（字节）
        self.file_size = file_size  # type: str
        # 文件状态
        self.file_status = file_status  # type: str
        # 文件类型
        self.file_type = file_type  # type: str
        # 文件oss地址
        self.file_url = file_url  # type: str
        # 封装格式
        self.format_name = format_name  # type: str
        # 高
        self.height = height  # type: str
        # 文件存储区域
        self.region = region  # type: str
        # 宽
        self.width = width  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.height is not None:
            result['Height'] = self.height
        if self.region is not None:
            result['Region'] = self.region
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(self, file_basic_info=None):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info  # type: AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super(AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class AddEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(self, business_type=None, category=None, cover_url=None, create_time=None, deleted_time=None,
                 description=None, input_url=None, media_id=None, media_tags=None, media_type=None, modified_time=None,
                 snapshots=None, source=None, sprite_images=None, status=None, title=None, transcode_status=None,
                 user_data=None):
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 分类
        self.category = category  # type: str
        # 封面地址
        self.cover_url = cover_url  # type: str
        # 媒资创建时间
        self.create_time = create_time  # type: str
        # 媒资删除时间
        self.deleted_time = deleted_time  # type: str
        # 内容描述
        self.description = description  # type: str
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url  # type: str
        # MediaId
        self.media_id = media_id  # type: str
        # 标签
        self.media_tags = media_tags  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 媒资修改时间
        self.modified_time = modified_time  # type: str
        # 截图
        self.snapshots = snapshots  # type: str
        # 来源
        self.source = source  # type: str
        # 雪碧图
        self.sprite_images = sprite_images  # type: str
        # 资源状态
        self.status = status  # type: str
        # 标题
        self.title = title  # type: str
        # 转码状态
        self.transcode_status = transcode_status  # type: str
        # 用户数据
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.category is not None:
            result['Category'] = self.category
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.description is not None:
            result['Description'] = self.description
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.source is not None:
            result['Source'] = self.source
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class AddEditingProjectMaterialsResponseBodyMediaInfos(TeaModel):
    def __init__(self, file_info_list=None, media_basic_info=None, media_id=None):
        # FileInfos
        self.file_info_list = file_info_list  # type: list[AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoList]
        # BasicInfo
        self.media_basic_info = media_basic_info  # type: AddEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo
        # 媒资ID
        self.media_id = media_id  # type: str

    def validate(self):
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()
        if self.media_basic_info:
            self.media_basic_info.validate()

    def to_map(self):
        _map = super(AddEditingProjectMaterialsResponseBodyMediaInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = AddEditingProjectMaterialsResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        if m.get('MediaBasicInfo') is not None:
            temp_model = AddEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class AddEditingProjectMaterialsResponseBody(TeaModel):
    def __init__(self, live_materials=None, media_infos=None, project_id=None, project_materials=None,
                 request_id=None):
        self.live_materials = live_materials  # type: list[AddEditingProjectMaterialsResponseBodyLiveMaterials]
        # 符合要求的媒资集合
        self.media_infos = media_infos  # type: list[AddEditingProjectMaterialsResponseBodyMediaInfos]
        self.project_id = project_id  # type: str
        self.project_materials = project_materials  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.live_materials:
            for k in self.live_materials:
                if k:
                    k.validate()
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddEditingProjectMaterialsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveMaterials'] = []
        if self.live_materials is not None:
            for k in self.live_materials:
                result['LiveMaterials'].append(k.to_map() if k else None)
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_materials is not None:
            result['ProjectMaterials'] = self.project_materials
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.live_materials = []
        if m.get('LiveMaterials') is not None:
            for k in m.get('LiveMaterials'):
                temp_model = AddEditingProjectMaterialsResponseBodyLiveMaterials()
                self.live_materials.append(temp_model.from_map(k))
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = AddEditingProjectMaterialsResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectMaterials') is not None:
            self.project_materials = m.get('ProjectMaterials')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddEditingProjectMaterialsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddEditingProjectMaterialsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddEditingProjectMaterialsResponse, self).to_map()
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
            temp_model = AddEditingProjectMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTemplateRequest(TeaModel):
    def __init__(self, config=None, cover_url=None, name=None, preview_media=None, related_mediaids=None,
                 source=None, status=None, type=None):
        # 参见Timeline模板Config文档
        self.config = config  # type: str
        # 模板封面
        self.cover_url = cover_url  # type: str
        # 模板名称
        self.name = name  # type: str
        # 预览视频媒资id
        self.preview_media = preview_media  # type: str
        # 模板相关素材，模板编辑器使用
        self.related_mediaids = related_mediaids  # type: str
        # 模板创建来源，默认OpenAPI
        self.source = source  # type: str
        # 模板状态
        self.status = status  # type: str
        # 模板类型，取值范围：Timeline
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.name is not None:
            result['Name'] = self.name
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.related_mediaids is not None:
            result['RelatedMediaids'] = self.related_mediaids
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('RelatedMediaids') is not None:
            self.related_mediaids = m.get('RelatedMediaids')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddTemplateResponseBodyTemplate(TeaModel):
    def __init__(self, config=None, cover_url=None, create_source=None, modified_source=None, name=None,
                 preview_media=None, status=None, template_id=None, type=None):
        # 参见Timeline模板Config文档
        self.config = config  # type: str
        # 模板封面
        self.cover_url = cover_url  # type: str
        # 模板创建来源
        self.create_source = create_source  # type: str
        # 模板修改来源
        self.modified_source = modified_source  # type: str
        # 模板名称
        self.name = name  # type: str
        # 预览视频媒资id
        self.preview_media = preview_media  # type: str
        # 模板状态
        self.status = status  # type: str
        # 模板Id
        self.template_id = template_id  # type: str
        # 模板类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTemplateResponseBodyTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        if self.name is not None:
            result['Name'] = self.name
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 模板信息
        self.template = template  # type: AddTemplateResponseBodyTemplate

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(AddTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = AddTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class AddTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddTemplateResponse, self).to_map()
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
            temp_model = AddTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetMediaInfosRequest(TeaModel):
    def __init__(self, addition_type=None, media_ids=None):
        self.addition_type = addition_type  # type: str
        self.media_ids = media_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetMediaInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addition_type is not None:
            result['AdditionType'] = self.addition_type
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdditionType') is not None:
            self.addition_type = m.get('AdditionType')
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')
        return self


class BatchGetMediaInfosResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(self, bitrate=None, duration=None, file_name=None, file_size=None, file_status=None, file_type=None,
                 file_url=None, format_name=None, height=None, region=None, width=None):
        # 码率
        self.bitrate = bitrate  # type: str
        # 时长
        self.duration = duration  # type: str
        # 文件名
        self.file_name = file_name  # type: str
        # 文件大小（字节）
        self.file_size = file_size  # type: str
        # 文件状态
        self.file_status = file_status  # type: str
        # 文件类型
        self.file_type = file_type  # type: str
        # 文件oss地址
        self.file_url = file_url  # type: str
        # 封装格式
        self.format_name = format_name  # type: str
        # 高
        self.height = height  # type: str
        # 文件存储区域
        self.region = region  # type: str
        # 宽
        self.width = width  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetMediaInfosResponseBodyMediaInfosFileInfoListFileBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.height is not None:
            result['Height'] = self.height
        if self.region is not None:
            result['Region'] = self.region
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class BatchGetMediaInfosResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(self, file_basic_info=None):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info  # type: BatchGetMediaInfosResponseBodyMediaInfosFileInfoListFileBasicInfo

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super(BatchGetMediaInfosResponseBodyMediaInfosFileInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = BatchGetMediaInfosResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class BatchGetMediaInfosResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(self, business_type=None, category=None, cover_url=None, create_time=None, deleted_time=None,
                 description=None, input_url=None, media_id=None, media_tags=None, media_type=None, modified_time=None,
                 snapshots=None, source=None, sprite_images=None, status=None, title=None, transcode_status=None,
                 user_data=None):
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 分类
        self.category = category  # type: str
        # 封面地址
        self.cover_url = cover_url  # type: str
        # 媒资创建时间
        self.create_time = create_time  # type: str
        # 媒资删除时间
        self.deleted_time = deleted_time  # type: str
        # 内容描述
        self.description = description  # type: str
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url  # type: str
        # MediaId
        self.media_id = media_id  # type: str
        # 标签
        self.media_tags = media_tags  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 媒资修改时间
        self.modified_time = modified_time  # type: str
        # 截图
        self.snapshots = snapshots  # type: str
        # 来源
        self.source = source  # type: str
        # 雪碧图
        self.sprite_images = sprite_images  # type: str
        # 资源状态
        self.status = status  # type: str
        # 标题
        self.title = title  # type: str
        # 转码状态
        self.transcode_status = transcode_status  # type: str
        # 用户数据
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetMediaInfosResponseBodyMediaInfosMediaBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.category is not None:
            result['Category'] = self.category
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.description is not None:
            result['Description'] = self.description
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.source is not None:
            result['Source'] = self.source
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class BatchGetMediaInfosResponseBodyMediaInfos(TeaModel):
    def __init__(self, file_info_list=None, media_basic_info=None, media_id=None):
        # FileInfos
        self.file_info_list = file_info_list  # type: list[BatchGetMediaInfosResponseBodyMediaInfosFileInfoList]
        # BasicInfo
        self.media_basic_info = media_basic_info  # type: BatchGetMediaInfosResponseBodyMediaInfosMediaBasicInfo
        # 媒资ID
        self.media_id = media_id  # type: str

    def validate(self):
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()
        if self.media_basic_info:
            self.media_basic_info.validate()

    def to_map(self):
        _map = super(BatchGetMediaInfosResponseBodyMediaInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = BatchGetMediaInfosResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        if m.get('MediaBasicInfo') is not None:
            temp_model = BatchGetMediaInfosResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class BatchGetMediaInfosResponseBody(TeaModel):
    def __init__(self, media_infos=None, request_id=None):
        # 符合要求的媒资集合
        self.media_infos = media_infos  # type: list[BatchGetMediaInfosResponseBodyMediaInfos]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchGetMediaInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = BatchGetMediaInfosResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchGetMediaInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchGetMediaInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchGetMediaInfosResponse, self).to_map()
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
            temp_model = BatchGetMediaInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEditingProjectRequest(TeaModel):
    def __init__(self, business_config=None, cover_url=None, description=None, material_maps=None,
                 project_type=None, timeline=None, title=None):
        # 工程业务配置。如果是直播剪辑工程必填OutputMediaConfig.StorageLocation,   Path 不填默认合成的直播片段存储在根路径下 OutputMediaTarget 不填默认oss-object，可以填vod-media 表示存储到vod  OutputMediaTarget 为vod-media 时，Path不生效。
        self.business_config = business_config  # type: str
        # 云剪辑工程封面
        self.cover_url = cover_url  # type: str
        # 云剪辑工程描述
        self.description = description  # type: str
        # 工程关联素材，多个素材以逗号（,）分隔；每种类型最多支持10个素材ID
        self.material_maps = material_maps  # type: str
        # 剪辑工程类型，EditingProject: 普通剪辑工程；LiveEditingProject: 直播剪辑工程
        self.project_type = project_type  # type: str
        # 云剪辑工程时间线，Json格式
        self.timeline = timeline  # type: str
        # 云剪辑工程标题
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEditingProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_config is not None:
            result['BusinessConfig'] = self.business_config
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.description is not None:
            result['Description'] = self.description
        if self.material_maps is not None:
            result['MaterialMaps'] = self.material_maps
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessConfig') is not None:
            self.business_config = m.get('BusinessConfig')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaterialMaps') is not None:
            self.material_maps = m.get('MaterialMaps')
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateEditingProjectResponseBodyProject(TeaModel):
    def __init__(self, business_config=None, business_status=None, cover_url=None, create_source=None,
                 create_time=None, description=None, duration=None, modified_source=None, modified_time=None, project_id=None,
                 project_type=None, status=None, status_name=None, template_type=None, timeline=None, title=None):
        # 工程业务配置
        self.business_config = business_config  # type: str
        # 业务状态，业务状态 /** 预约中 **/ RESERVING(0, "Reserving"), /** 预约取消 **/ RESERVATION_CANCELED(1, "ReservationCanceled"), /** 直播中 **/ BROADCASTING(3, "BroadCasting"), /** 加载失败 **/ LOADING_FAILED(4, "LoadingFailed"), /** 直播结束 **/ LIVE_FINISHED(5, "LiveFinished");
        self.business_status = business_status  # type: str
        # 云剪辑工程封面。
        self.cover_url = cover_url  # type: str
        # 云剪辑工程创建方式  -OpenAPI  -AliyunConsole  -WebSDK -LiveEditingOpenAPI -LiveEditingConsole
        self.create_source = create_source  # type: str
        # 云剪辑工程创建时间
        self.create_time = create_time  # type: str
        # 云剪辑工程描述
        self.description = description  # type: str
        # 云剪辑工程时长
        self.duration = duration  # type: float
        # 云剪辑工程创建方式  -OpenAPI  -AliyunConsole  -WebSDK -LiveEditingOpenAPI -LiveEditingConsole
        self.modified_source = modified_source  # type: str
        # 云剪辑工程编辑时间
        self.modified_time = modified_time  # type: str
        # 云剪辑工程ID
        self.project_id = project_id  # type: str
        # 剪辑工程类型，EditingProject: 普通剪辑工程；LiveEditingProject: 直播剪辑工程
        self.project_type = project_type  # type: str
        # 云剪辑工程状态。  所有云剪辑工程状态列表：  -1:Draft  -2:Editing  -3:Producing  -4:Produced  -5:ProduceFailed  -7:Deleted
        self.status = status  # type: long
        # 云剪辑状态名称，对应状态列表中状态名称。
        self.status_name = status_name  # type: str
        self.template_type = template_type  # type: str
        # 云剪辑工程时间线，Json格式
        self.timeline = timeline  # type: str
        # 云剪辑工程标题
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEditingProjectResponseBodyProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_config is not None:
            result['BusinessConfig'] = self.business_config
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        if self.status is not None:
            result['Status'] = self.status
        if self.status_name is not None:
            result['StatusName'] = self.status_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessConfig') is not None:
            self.business_config = m.get('BusinessConfig')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateEditingProjectResponseBody(TeaModel):
    def __init__(self, project=None, request_id=None):
        self.project = project  # type: CreateEditingProjectResponseBodyProject
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super(CreateEditingProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = CreateEditingProjectResponseBodyProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEditingProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEditingProjectResponse, self).to_map()
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
            temp_model = CreateEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEditingProjectMaterialsRequest(TeaModel):
    def __init__(self, material_ids=None, material_type=None, project_id=None):
        # 素材ID
        self.material_ids = material_ids  # type: str
        # 素材类型
        self.material_type = material_type  # type: str
        # 云剪辑工程ID
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEditingProjectMaterialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_ids is not None:
            result['MaterialIds'] = self.material_ids
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaterialIds') is not None:
            self.material_ids = m.get('MaterialIds')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteEditingProjectMaterialsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEditingProjectMaterialsResponseBody, self).to_map()
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


class DeleteEditingProjectMaterialsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEditingProjectMaterialsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEditingProjectMaterialsResponse, self).to_map()
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
            temp_model = DeleteEditingProjectMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEditingProjectsRequest(TeaModel):
    def __init__(self, project_ids=None):
        # 云剪辑工程ID。支持多个云剪辑工程，以逗号分隔。
        self.project_ids = project_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEditingProjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        return self


class DeleteEditingProjectsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEditingProjectsResponseBody, self).to_map()
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


class DeleteEditingProjectsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEditingProjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEditingProjectsResponse, self).to_map()
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
            temp_model = DeleteEditingProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMediaInfosRequest(TeaModel):
    def __init__(self, input_urls=None, media_ids=None):
        # 待注册的媒资在相应系统中的地址
        self.input_urls = input_urls  # type: str
        # ICE 媒资ID
        self.media_ids = media_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMediaInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_urls is not None:
            result['InputURLs'] = self.input_urls
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputURLs') is not None:
            self.input_urls = m.get('InputURLs')
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')
        return self


class DeleteMediaInfosResponseBody(TeaModel):
    def __init__(self, ignored_list=None, request_id=None):
        # 出现获取错误的ID或inputUr
        self.ignored_list = ignored_list  # type: list[str]
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMediaInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ignored_list is not None:
            result['IgnoredList'] = self.ignored_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IgnoredList') is not None:
            self.ignored_list = m.get('IgnoredList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteMediaInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteMediaInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMediaInfosResponse, self).to_map()
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
            temp_model = DeleteMediaInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSmartJobRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSmartJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteSmartJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None, state=None):
        self.job_id = job_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSmartJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DeleteSmartJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSmartJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSmartJobResponse, self).to_map()
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
            temp_model = DeleteSmartJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(self, template_ids=None):
        # 模板id，多个id用英文逗号隔开
        self.template_ids = template_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateResponseBody, self).to_map()
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


class DeleteTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIceProductStatusResponseBody(TeaModel):
    def __init__(self, iceservice_avaliable=None, request_id=None):
        self.iceservice_avaliable = iceservice_avaliable  # type: bool
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIceProductStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iceservice_avaliable is not None:
            result['ICEServiceAvaliable'] = self.iceservice_avaliable
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ICEServiceAvaliable') is not None:
            self.iceservice_avaliable = m.get('ICEServiceAvaliable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIceProductStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeIceProductStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIceProductStatusResponse, self).to_map()
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
            temp_model = DescribeIceProductStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRelatedAuthorizationStatusResponseBody(TeaModel):
    def __init__(self, authorized=None, mnsauthorized=None, mtsauthorized=None, ossauthorized=None, request_id=None):
        self.authorized = authorized  # type: bool
        self.mnsauthorized = mnsauthorized  # type: bool
        self.mtsauthorized = mtsauthorized  # type: bool
        self.ossauthorized = ossauthorized  # type: bool
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRelatedAuthorizationStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized is not None:
            result['Authorized'] = self.authorized
        if self.mnsauthorized is not None:
            result['MNSAuthorized'] = self.mnsauthorized
        if self.mtsauthorized is not None:
            result['MTSAuthorized'] = self.mtsauthorized
        if self.ossauthorized is not None:
            result['OSSAuthorized'] = self.ossauthorized
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')
        if m.get('MNSAuthorized') is not None:
            self.mnsauthorized = m.get('MNSAuthorized')
        if m.get('MTSAuthorized') is not None:
            self.mtsauthorized = m.get('MTSAuthorized')
        if m.get('OSSAuthorized') is not None:
            self.ossauthorized = m.get('OSSAuthorized')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRelatedAuthorizationStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRelatedAuthorizationStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRelatedAuthorizationStatusResponse, self).to_map()
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
            temp_model = DescribeRelatedAuthorizationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultStorageLocationResponseBody(TeaModel):
    def __init__(self, bucket=None, path=None, request_id=None, status=None, storage_type=None):
        # oss bucket 名称
        self.bucket = bucket  # type: str
        # 路径
        self.path = path  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 状态
        self.status = status  # type: str
        # 存储类型
        self.storage_type = storage_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDefaultStorageLocationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.path is not None:
            result['Path'] = self.path
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class GetDefaultStorageLocationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDefaultStorageLocationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDefaultStorageLocationResponse, self).to_map()
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
            temp_model = GetDefaultStorageLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEditingProjectRequest(TeaModel):
    def __init__(self, project_id=None):
        # 云剪辑工程ID
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetEditingProjectResponseBodyProject(TeaModel):
    def __init__(self, business_config=None, business_status=None, cover_url=None, create_source=None,
                 create_time=None, description=None, duration=None, modified_source=None, modified_time=None, project_id=None,
                 project_type=None, status=None, template_type=None, timeline=None, title=None):
        self.business_config = business_config  # type: str
        self.business_status = business_status  # type: str
        # 云剪辑工程封面
        self.cover_url = cover_url  # type: str
        # 云剪辑工程创建来源
        self.create_source = create_source  # type: str
        # 云剪辑工程创建时间
        self.create_time = create_time  # type: str
        # 云剪辑工程描述
        self.description = description  # type: str
        # 云剪辑工程总时长
        self.duration = duration  # type: long
        # 云剪辑工程修改来源
        self.modified_source = modified_source  # type: str
        # 云剪辑工程最新修改时间
        self.modified_time = modified_time  # type: str
        # 云剪辑工程ID
        self.project_id = project_id  # type: str
        self.project_type = project_type  # type: str
        # 云剪辑工程状态
        self.status = status  # type: str
        # 云剪辑工程模板类型
        self.template_type = template_type  # type: str
        # 云剪辑工程时间线
        self.timeline = timeline  # type: str
        # 云剪辑工程标题
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectResponseBodyProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_config is not None:
            result['BusinessConfig'] = self.business_config
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        if self.status is not None:
            result['Status'] = self.status
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessConfig') is not None:
            self.business_config = m.get('BusinessConfig')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetEditingProjectResponseBody(TeaModel):
    def __init__(self, project=None, request_id=None):
        self.project = project  # type: GetEditingProjectResponseBodyProject
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super(GetEditingProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = GetEditingProjectResponseBodyProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEditingProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEditingProjectResponse, self).to_map()
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
            temp_model = GetEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEditingProjectMaterialsRequest(TeaModel):
    def __init__(self, project_id=None):
        # 云剪辑工程ID
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectMaterialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetEditingProjectMaterialsResponseBodyLiveMaterials(TeaModel):
    def __init__(self, app_name=None, domain_name=None, live_url=None, stream_name=None):
        self.app_name = app_name  # type: str
        self.domain_name = domain_name  # type: str
        self.live_url = live_url  # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBodyLiveMaterials, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(self, bitrate=None, duration=None, file_name=None, file_size=None, file_status=None, file_type=None,
                 file_url=None, format_name=None, height=None, region=None, width=None):
        # 码率
        self.bitrate = bitrate  # type: str
        # 时长
        self.duration = duration  # type: str
        # 文件名
        self.file_name = file_name  # type: str
        # 文件大小（字节）
        self.file_size = file_size  # type: str
        # 文件状态
        self.file_status = file_status  # type: str
        # 文件类型
        self.file_type = file_type  # type: str
        # 文件oss地址
        self.file_url = file_url  # type: str
        # 封装格式
        self.format_name = format_name  # type: str
        # 高
        self.height = height  # type: str
        # 文件存储区域
        self.region = region  # type: str
        # 宽
        self.width = width  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.height is not None:
            result['Height'] = self.height
        if self.region is not None:
            result['Region'] = self.region
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(self, file_basic_info=None):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info  # type: GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class GetEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(self, business_type=None, category=None, cover_url=None, create_time=None, deleted_time=None,
                 description=None, input_url=None, media_id=None, media_tags=None, media_type=None, modified_time=None,
                 snapshots=None, source=None, sprite_images=None, status=None, title=None, transcode_status=None,
                 user_data=None):
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 分类
        self.category = category  # type: str
        # 封面地址
        self.cover_url = cover_url  # type: str
        # 媒资创建时间
        self.create_time = create_time  # type: str
        # 媒资删除时间
        self.deleted_time = deleted_time  # type: str
        # 内容描述
        self.description = description  # type: str
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url  # type: str
        # MediaId
        self.media_id = media_id  # type: str
        # 标签
        self.media_tags = media_tags  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 媒资修改时间
        self.modified_time = modified_time  # type: str
        # 截图
        self.snapshots = snapshots  # type: str
        # 来源
        self.source = source  # type: str
        # 雪碧图
        self.sprite_images = sprite_images  # type: str
        # 资源状态
        self.status = status  # type: str
        # 标题
        self.title = title  # type: str
        # 转码状态
        self.transcode_status = transcode_status  # type: str
        # 用户数据
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.category is not None:
            result['Category'] = self.category
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.description is not None:
            result['Description'] = self.description
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.source is not None:
            result['Source'] = self.source
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetEditingProjectMaterialsResponseBodyMediaInfos(TeaModel):
    def __init__(self, file_info_list=None, media_basic_info=None, media_id=None):
        # FileInfos
        self.file_info_list = file_info_list  # type: list[GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoList]
        # BasicInfo
        self.media_basic_info = media_basic_info  # type: GetEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo
        # 媒资ID
        self.media_id = media_id  # type: str

    def validate(self):
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()
        if self.media_basic_info:
            self.media_basic_info.validate()

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBodyMediaInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = GetEditingProjectMaterialsResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        if m.get('MediaBasicInfo') is not None:
            temp_model = GetEditingProjectMaterialsResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class GetEditingProjectMaterialsResponseBody(TeaModel):
    def __init__(self, live_materials=None, media_infos=None, project_id=None, project_materials=None,
                 request_id=None):
        self.live_materials = live_materials  # type: list[GetEditingProjectMaterialsResponseBodyLiveMaterials]
        # 符合要求的媒资集合
        self.media_infos = media_infos  # type: list[GetEditingProjectMaterialsResponseBodyMediaInfos]
        self.project_id = project_id  # type: str
        self.project_materials = project_materials  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.live_materials:
            for k in self.live_materials:
                if k:
                    k.validate()
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveMaterials'] = []
        if self.live_materials is not None:
            for k in self.live_materials:
                result['LiveMaterials'].append(k.to_map() if k else None)
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_materials is not None:
            result['ProjectMaterials'] = self.project_materials
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.live_materials = []
        if m.get('LiveMaterials') is not None:
            for k in m.get('LiveMaterials'):
                temp_model = GetEditingProjectMaterialsResponseBodyLiveMaterials()
                self.live_materials.append(temp_model.from_map(k))
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = GetEditingProjectMaterialsResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectMaterials') is not None:
            self.project_materials = m.get('ProjectMaterials')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEditingProjectMaterialsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEditingProjectMaterialsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponse, self).to_map()
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
            temp_model = GetEditingProjectMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventCallbackResponseBody(TeaModel):
    def __init__(self, callback_queue_name=None, event_type_list=None, request_id=None):
        self.callback_queue_name = callback_queue_name  # type: str
        self.event_type_list = event_type_list  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventCallbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_queue_name is not None:
            result['CallbackQueueName'] = self.callback_queue_name
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackQueueName') is not None:
            self.callback_queue_name = m.get('CallbackQueueName')
        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEventCallbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEventCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEventCallbackResponse, self).to_map()
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
            temp_model = GetEventCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveEditingIndexFileRequest(TeaModel):
    def __init__(self, app_name=None, domain_name=None, project_id=None, stream_name=None):
        self.app_name = app_name  # type: str
        self.domain_name = domain_name  # type: str
        self.project_id = project_id  # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveEditingIndexFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class GetLiveEditingIndexFileResponseBody(TeaModel):
    def __init__(self, index_file=None, request_id=None):
        self.index_file = index_file  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveEditingIndexFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_file is not None:
            result['IndexFile'] = self.index_file
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IndexFile') is not None:
            self.index_file = m.get('IndexFile')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLiveEditingIndexFileResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLiveEditingIndexFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLiveEditingIndexFileResponse, self).to_map()
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
            temp_model = GetLiveEditingIndexFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveEditingJobRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveEditingJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetLiveEditingJobResponseBodyLiveEditingJobLiveStreamConfig(TeaModel):
    def __init__(self, app_name=None, domain_name=None, stream_name=None):
        self.app_name = app_name  # type: str
        self.domain_name = domain_name  # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveEditingJobResponseBodyLiveEditingJobLiveStreamConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class GetLiveEditingJobResponseBodyLiveEditingJobMediaProduceConfig(TeaModel):
    def __init__(self, mode=None):
        self.mode = mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveEditingJobResponseBodyLiveEditingJobMediaProduceConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class GetLiveEditingJobResponseBodyLiveEditingJobOutputMediaConfig(TeaModel):
    def __init__(self, bitrate=None, file_name=None, height=None, media_url=None, storage_location=None,
                 vod_template_group_id=None, width=None):
        self.bitrate = bitrate  # type: long
        self.file_name = file_name  # type: str
        self.height = height  # type: int
        self.media_url = media_url  # type: str
        self.storage_location = storage_location  # type: str
        self.vod_template_group_id = vod_template_group_id  # type: str
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLiveEditingJobResponseBodyLiveEditingJobOutputMediaConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.height is not None:
            result['Height'] = self.height
        if self.media_url is not None:
            result['MediaURL'] = self.media_url
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.vod_template_group_id is not None:
            result['VodTemplateGroupId'] = self.vod_template_group_id
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('VodTemplateGroupId') is not None:
            self.vod_template_group_id = m.get('VodTemplateGroupId')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class GetLiveEditingJobResponseBodyLiveEditingJob(TeaModel):
    def __init__(self, clips=None, code=None, complete_time=None, creation_time=None, job_id=None,
                 live_stream_config=None, media_id=None, media_produce_config=None, media_url=None, message=None, modified_time=None,
                 output_media_config=None, project_id=None, status=None, user_data=None):
        self.clips = clips  # type: str
        self.code = code  # type: str
        self.complete_time = complete_time  # type: str
        self.creation_time = creation_time  # type: str
        self.job_id = job_id  # type: str
        self.live_stream_config = live_stream_config  # type: GetLiveEditingJobResponseBodyLiveEditingJobLiveStreamConfig
        self.media_id = media_id  # type: str
        self.media_produce_config = media_produce_config  # type: GetLiveEditingJobResponseBodyLiveEditingJobMediaProduceConfig
        self.media_url = media_url  # type: str
        self.message = message  # type: str
        self.modified_time = modified_time  # type: str
        self.output_media_config = output_media_config  # type: GetLiveEditingJobResponseBodyLiveEditingJobOutputMediaConfig
        self.project_id = project_id  # type: str
        self.status = status  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        if self.live_stream_config:
            self.live_stream_config.validate()
        if self.media_produce_config:
            self.media_produce_config.validate()
        if self.output_media_config:
            self.output_media_config.validate()

    def to_map(self):
        _map = super(GetLiveEditingJobResponseBodyLiveEditingJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clips is not None:
            result['Clips'] = self.clips
        if self.code is not None:
            result['Code'] = self.code
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.live_stream_config is not None:
            result['LiveStreamConfig'] = self.live_stream_config.to_map()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_produce_config is not None:
            result['MediaProduceConfig'] = self.media_produce_config.to_map()
        if self.media_url is not None:
            result['MediaURL'] = self.media_url
        if self.message is not None:
            result['Message'] = self.message
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.output_media_config is not None:
            result['OutputMediaConfig'] = self.output_media_config.to_map()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Clips') is not None:
            self.clips = m.get('Clips')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('LiveStreamConfig') is not None:
            temp_model = GetLiveEditingJobResponseBodyLiveEditingJobLiveStreamConfig()
            self.live_stream_config = temp_model.from_map(m['LiveStreamConfig'])
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaProduceConfig') is not None:
            temp_model = GetLiveEditingJobResponseBodyLiveEditingJobMediaProduceConfig()
            self.media_produce_config = temp_model.from_map(m['MediaProduceConfig'])
        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OutputMediaConfig') is not None:
            temp_model = GetLiveEditingJobResponseBodyLiveEditingJobOutputMediaConfig()
            self.output_media_config = temp_model.from_map(m['OutputMediaConfig'])
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetLiveEditingJobResponseBody(TeaModel):
    def __init__(self, live_editing_job=None, request_id=None):
        self.live_editing_job = live_editing_job  # type: GetLiveEditingJobResponseBodyLiveEditingJob
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.live_editing_job:
            self.live_editing_job.validate()

    def to_map(self):
        _map = super(GetLiveEditingJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_editing_job is not None:
            result['LiveEditingJob'] = self.live_editing_job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveEditingJob') is not None:
            temp_model = GetLiveEditingJobResponseBodyLiveEditingJob()
            self.live_editing_job = temp_model.from_map(m['LiveEditingJob'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLiveEditingJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLiveEditingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLiveEditingJobResponse, self).to_map()
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
            temp_model = GetLiveEditingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaInfoRequest(TeaModel):
    def __init__(self, input_url=None, media_id=None, output_type=None):
        self.input_url = input_url  # type: str
        self.media_id = media_id  # type: str
        self.output_type = output_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        return self


class GetMediaInfoResponseBodyMediaInfoAiRoughDataList(TeaModel):
    def __init__(self, result=None, type=None):
        # AI原始结果
        self.result = result  # type: str
        # AI类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoAiRoughDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetMediaInfoResponseBodyMediaInfoDynamicMetaDataList(TeaModel):
    def __init__(self, data=None, in_=None, out=None, type=None):
        # 元数据json string
        self.data = data  # type: str
        # 开始时间
        self.in_ = in_  # type: float
        # 结束时间
        self.out = out  # type: float
        # 类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoDynamicMetaDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.in_ is not None:
            result['In'] = self.in_
        if self.out is not None:
            result['Out'] = self.out
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('In') is not None:
            self.in_ = m.get('In')
        if m.get('Out') is not None:
            self.out = m.get('Out')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList(TeaModel):
    def __init__(self, bitrate=None, channel_layout=None, channels=None, codec_long_name=None, codec_name=None,
                 codec_tag=None, codec_tag_string=None, codec_time_base=None, duration=None, fps=None, index=None, lang=None,
                 num_frames=None, profile=None, sample_fmt=None, sample_rate=None, start_time=None, timebase=None):
        # 码率
        self.bitrate = bitrate  # type: str
        # 声道输出样式
        self.channel_layout = channel_layout  # type: str
        # 声道数
        self.channels = channels  # type: str
        # 编码格式长述名
        self.codec_long_name = codec_long_name  # type: str
        # 编码格式简述名
        self.codec_name = codec_name  # type: str
        # 编码格式标记
        self.codec_tag = codec_tag  # type: str
        # 编码格式标记文本
        self.codec_tag_string = codec_tag_string  # type: str
        # 编码时基
        self.codec_time_base = codec_time_base  # type: str
        # 时长
        self.duration = duration  # type: str
        # 音频帧率
        self.fps = fps  # type: str
        # 音频流序号
        self.index = index  # type: str
        # 语言
        self.lang = lang  # type: str
        # 总帧数
        self.num_frames = num_frames  # type: str
        # 编码预置
        self.profile = profile  # type: str
        # 采样格式
        self.sample_fmt = sample_fmt  # type: str
        # 采样率
        self.sample_rate = sample_rate  # type: str
        # 起始时间
        self.start_time = start_time  # type: str
        # 时基
        self.timebase = timebase  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.index is not None:
            result['Index'] = self.index
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.sample_fmt is not None:
            result['SampleFmt'] = self.sample_fmt
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.timebase is not None:
            result['Timebase'] = self.timebase
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('SampleFmt') is not None:
            self.sample_fmt = m.get('SampleFmt')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo(TeaModel):
    def __init__(self, bitrate=None, duration=None, file_name=None, file_size=None, file_status=None, file_type=None,
                 file_url=None, format_name=None, height=None, region=None, width=None):
        # 码率
        self.bitrate = bitrate  # type: str
        # 时长
        self.duration = duration  # type: str
        # 文件名
        self.file_name = file_name  # type: str
        # 文件大小（字节）
        self.file_size = file_size  # type: str
        # 文件状态
        self.file_status = file_status  # type: str
        # 文件类型
        self.file_type = file_type  # type: str
        # 文件oss地址
        self.file_url = file_url  # type: str
        # 封装格式
        self.format_name = format_name  # type: str
        # 高
        self.height = height  # type: str
        # 文件存储区域
        self.region = region  # type: str
        # 宽
        self.width = width  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.height is not None:
            result['Height'] = self.height
        if self.region is not None:
            result['Region'] = self.region
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList(TeaModel):
    def __init__(self, codec_long_name=None, codec_name=None, codec_tag=None, codec_tag_string=None,
                 codec_time_base=None, duration=None, index=None, lang=None, start_time=None, timebase=None):
        # 编码格式长述名
        self.codec_long_name = codec_long_name  # type: str
        # 编码格式简述名
        self.codec_name = codec_name  # type: str
        # 编码格式标记
        self.codec_tag = codec_tag  # type: str
        # 编码格式标记文本
        self.codec_tag_string = codec_tag_string  # type: str
        # 编码时基
        self.codec_time_base = codec_time_base  # type: str
        # 时长
        self.duration = duration  # type: str
        # 音频流序号
        self.index = index  # type: str
        # 语言
        self.lang = lang  # type: str
        # 起始时间
        self.start_time = start_time  # type: str
        # 时基
        self.timebase = timebase  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.index is not None:
            result['Index'] = self.index
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.timebase is not None:
            result['Timebase'] = self.timebase
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList(TeaModel):
    def __init__(self, avg_fps=None, bitrate=None, codec_long_name=None, codec_name=None, codec_tag=None,
                 codec_tag_string=None, codec_time_base=None, dar=None, duration=None, fps=None, has_bframes=None, height=None,
                 index=None, lang=None, level=None, nb_frames=None, num_frames=None, pix_fmt=None, profile=None,
                 rotate=None, sar=None, start_time=None, timebase=None, width=None):
        # 平均帧率
        self.avg_fps = avg_fps  # type: str
        # 码率
        self.bitrate = bitrate  # type: str
        # 编码格式长述名
        self.codec_long_name = codec_long_name  # type: str
        # 编码格式简述名
        self.codec_name = codec_name  # type: str
        # 编码格式标记
        self.codec_tag = codec_tag  # type: str
        # 编码格式标记文本
        self.codec_tag_string = codec_tag_string  # type: str
        # 编码时基
        self.codec_time_base = codec_time_base  # type: str
        # 编码显示分辨率比
        self.dar = dar  # type: str
        # 时长
        self.duration = duration  # type: str
        # 视频帧率
        self.fps = fps  # type: str
        # 是否有B帧
        self.has_bframes = has_bframes  # type: str
        # 高
        self.height = height  # type: str
        # 视频流序号
        self.index = index  # type: str
        # 语言
        self.lang = lang  # type: str
        # 编码等级
        self.level = level  # type: str
        # 总帧数
        self.nb_frames = nb_frames  # type: str
        # 总帧数
        self.num_frames = num_frames  # type: str
        # 像素格式
        self.pix_fmt = pix_fmt  # type: str
        # 编码预置
        self.profile = profile  # type: str
        # 旋转
        self.rotate = rotate  # type: str
        # 编码信号分辨率比
        self.sar = sar  # type: str
        # 起始时间
        self.start_time = start_time  # type: str
        # 时基
        self.timebase = timebase  # type: str
        # 宽
        self.width = width  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_fps is not None:
            result['AvgFPS'] = self.avg_fps
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.dar is not None:
            result['Dar'] = self.dar
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes
        if self.height is not None:
            result['Height'] = self.height
        if self.index is not None:
            result['Index'] = self.index
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.level is not None:
            result['Level'] = self.level
        if self.nb_frames is not None:
            result['Nb_frames'] = self.nb_frames
        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames
        if self.pix_fmt is not None:
            result['PixFmt'] = self.pix_fmt
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.sar is not None:
            result['Sar'] = self.sar
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.timebase is not None:
            result['Timebase'] = self.timebase
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvgFPS') is not None:
            self.avg_fps = m.get('AvgFPS')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('Dar') is not None:
            self.dar = m.get('Dar')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Nb_frames') is not None:
            self.nb_frames = m.get('Nb_frames')
        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')
        if m.get('PixFmt') is not None:
            self.pix_fmt = m.get('PixFmt')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('Sar') is not None:
            self.sar = m.get('Sar')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class GetMediaInfoResponseBodyMediaInfoFileInfoList(TeaModel):
    def __init__(self, audio_stream_info_list=None, file_basic_info=None, subtitle_stream_info_list=None,
                 video_stream_info_list=None):
        # 音频流信息，一个媒资可能有多条音频流
        self.audio_stream_info_list = audio_stream_info_list  # type: list[GetMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList]
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info  # type: GetMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo
        # 字幕流信息，一个媒资可能有多条字幕流
        self.subtitle_stream_info_list = subtitle_stream_info_list  # type: list[GetMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList]
        # 视频流信息，一个媒资可能有多条视频流
        self.video_stream_info_list = video_stream_info_list  # type: list[GetMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList]

    def validate(self):
        if self.audio_stream_info_list:
            for k in self.audio_stream_info_list:
                if k:
                    k.validate()
        if self.file_basic_info:
            self.file_basic_info.validate()
        if self.subtitle_stream_info_list:
            for k in self.subtitle_stream_info_list:
                if k:
                    k.validate()
        if self.video_stream_info_list:
            for k in self.video_stream_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoFileInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AudioStreamInfoList'] = []
        if self.audio_stream_info_list is not None:
            for k in self.audio_stream_info_list:
                result['AudioStreamInfoList'].append(k.to_map() if k else None)
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        result['SubtitleStreamInfoList'] = []
        if self.subtitle_stream_info_list is not None:
            for k in self.subtitle_stream_info_list:
                result['SubtitleStreamInfoList'].append(k.to_map() if k else None)
        result['VideoStreamInfoList'] = []
        if self.video_stream_info_list is not None:
            for k in self.video_stream_info_list:
                result['VideoStreamInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.audio_stream_info_list = []
        if m.get('AudioStreamInfoList') is not None:
            for k in m.get('AudioStreamInfoList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList()
                self.audio_stream_info_list.append(temp_model.from_map(k))
        if m.get('FileBasicInfo') is not None:
            temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        self.subtitle_stream_info_list = []
        if m.get('SubtitleStreamInfoList') is not None:
            for k in m.get('SubtitleStreamInfoList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList()
                self.subtitle_stream_info_list.append(temp_model.from_map(k))
        self.video_stream_info_list = []
        if m.get('VideoStreamInfoList') is not None:
            for k in m.get('VideoStreamInfoList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList()
                self.video_stream_info_list.append(temp_model.from_map(k))
        return self


class GetMediaInfoResponseBodyMediaInfoMediaBasicInfo(TeaModel):
    def __init__(self, business_type=None, category=None, cover_url=None, create_time=None, deleted_time=None,
                 description=None, input_url=None, media_id=None, media_tags=None, media_type=None, modified_time=None,
                 source=None, sprite_images=None, status=None, title=None, user_data=None):
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 分类
        self.category = category  # type: str
        # 封面地址
        self.cover_url = cover_url  # type: str
        # 媒资创建时间
        self.create_time = create_time  # type: str
        # 媒资删除时间
        self.deleted_time = deleted_time  # type: str
        # 内容描述
        self.description = description  # type: str
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url  # type: str
        # MediaId
        self.media_id = media_id  # type: str
        # 标签
        self.media_tags = media_tags  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 媒资修改时间
        self.modified_time = modified_time  # type: str
        # 来源
        self.source = source  # type: str
        # 雪碧图
        self.sprite_images = sprite_images  # type: str
        # 资源状态
        self.status = status  # type: str
        # 标题
        self.title = title  # type: str
        # 用户数据
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfoMediaBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.category is not None:
            result['Category'] = self.category
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.description is not None:
            result['Description'] = self.description
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetMediaInfoResponseBodyMediaInfo(TeaModel):
    def __init__(self, ai_rough_data_list=None, dynamic_meta_data_list=None, file_info_list=None,
                 media_basic_info=None, media_id=None):
        # AIMetadata
        self.ai_rough_data_list = ai_rough_data_list  # type: list[GetMediaInfoResponseBodyMediaInfoAiRoughDataList]
        # 其他元数据
        self.dynamic_meta_data_list = dynamic_meta_data_list  # type: list[GetMediaInfoResponseBodyMediaInfoDynamicMetaDataList]
        # FileInfos
        self.file_info_list = file_info_list  # type: list[GetMediaInfoResponseBodyMediaInfoFileInfoList]
        # BasicInfo
        self.media_basic_info = media_basic_info  # type: GetMediaInfoResponseBodyMediaInfoMediaBasicInfo
        # 媒资ID
        self.media_id = media_id  # type: str

    def validate(self):
        if self.ai_rough_data_list:
            for k in self.ai_rough_data_list:
                if k:
                    k.validate()
        if self.dynamic_meta_data_list:
            for k in self.dynamic_meta_data_list:
                if k:
                    k.validate()
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()
        if self.media_basic_info:
            self.media_basic_info.validate()

    def to_map(self):
        _map = super(GetMediaInfoResponseBodyMediaInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AiRoughDataList'] = []
        if self.ai_rough_data_list is not None:
            for k in self.ai_rough_data_list:
                result['AiRoughDataList'].append(k.to_map() if k else None)
        result['DynamicMetaDataList'] = []
        if self.dynamic_meta_data_list is not None:
            for k in self.dynamic_meta_data_list:
                result['DynamicMetaDataList'].append(k.to_map() if k else None)
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ai_rough_data_list = []
        if m.get('AiRoughDataList') is not None:
            for k in m.get('AiRoughDataList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoAiRoughDataList()
                self.ai_rough_data_list.append(temp_model.from_map(k))
        self.dynamic_meta_data_list = []
        if m.get('DynamicMetaDataList') is not None:
            for k in m.get('DynamicMetaDataList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoDynamicMetaDataList()
                self.dynamic_meta_data_list.append(temp_model.from_map(k))
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = GetMediaInfoResponseBodyMediaInfoFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        if m.get('MediaBasicInfo') is not None:
            temp_model = GetMediaInfoResponseBodyMediaInfoMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class GetMediaInfoResponseBody(TeaModel):
    def __init__(self, media_info=None, request_id=None):
        self.media_info = media_info  # type: GetMediaInfoResponseBodyMediaInfo
        # RequestId
        self.request_id = request_id  # type: str

    def validate(self):
        if self.media_info:
            self.media_info.validate()

    def to_map(self):
        _map = super(GetMediaInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_info is not None:
            result['MediaInfo'] = self.media_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaInfo') is not None:
            temp_model = GetMediaInfoResponseBodyMediaInfo()
            self.media_info = temp_model.from_map(m['MediaInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMediaInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMediaInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMediaInfoResponse, self).to_map()
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
            temp_model = GetMediaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaProducingJobRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaProducingJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetMediaProducingJobResponseBodyMediaProducingJob(TeaModel):
    def __init__(self, clips_param=None, code=None, complete_time=None, create_time=None, duration=None, job_id=None,
                 media_id=None, media_url=None, message=None, modified_time=None, project_id=None, status=None,
                 template_id=None, timeline=None):
        self.clips_param = clips_param  # type: str
        self.code = code  # type: str
        self.complete_time = complete_time  # type: str
        self.create_time = create_time  # type: str
        self.duration = duration  # type: float
        self.job_id = job_id  # type: str
        self.media_id = media_id  # type: str
        self.media_url = media_url  # type: str
        self.message = message  # type: str
        self.modified_time = modified_time  # type: str
        self.project_id = project_id  # type: str
        self.status = status  # type: str
        self.template_id = template_id  # type: str
        self.timeline = timeline  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaProducingJobResponseBodyMediaProducingJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        if self.code is not None:
            result['Code'] = self.code
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_url is not None:
            result['MediaURL'] = self.media_url
        if self.message is not None:
            result['Message'] = self.message
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        return self


class GetMediaProducingJobResponseBody(TeaModel):
    def __init__(self, media_producing_job=None, request_id=None):
        self.media_producing_job = media_producing_job  # type: GetMediaProducingJobResponseBodyMediaProducingJob
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.media_producing_job:
            self.media_producing_job.validate()

    def to_map(self):
        _map = super(GetMediaProducingJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_producing_job is not None:
            result['MediaProducingJob'] = self.media_producing_job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaProducingJob') is not None:
            temp_model = GetMediaProducingJobResponseBodyMediaProducingJob()
            self.media_producing_job = temp_model.from_map(m['MediaProducingJob'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMediaProducingJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMediaProducingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMediaProducingJobResponse, self).to_map()
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
            temp_model = GetMediaProducingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSmartHandleJobRequest(TeaModel):
    def __init__(self, job_id=None, with_ai_result=None):
        self.job_id = job_id  # type: str
        self.with_ai_result = with_ai_result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSmartHandleJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.with_ai_result is not None:
            result['WithAiResult'] = self.with_ai_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('WithAiResult') is not None:
            self.with_ai_result = m.get('WithAiResult')
        return self


class GetSmartHandleJobResponseBodySmartJobInfoInputConfig(TeaModel):
    def __init__(self, input_file=None, job_parameters=None):
        self.input_file = input_file  # type: str
        self.job_parameters = job_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSmartHandleJobResponseBodySmartJobInfoInputConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.job_parameters is not None:
            result['JobParameters'] = self.job_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('JobParameters') is not None:
            self.job_parameters = m.get('JobParameters')
        return self


class GetSmartHandleJobResponseBodySmartJobInfoOutputConfig(TeaModel):
    def __init__(self, bucket=None, object=None):
        self.bucket = bucket  # type: str
        self.object = object  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSmartHandleJobResponseBodySmartJobInfoOutputConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.object is not None:
            result['Object'] = self.object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        return self


class GetSmartHandleJobResponseBodySmartJobInfo(TeaModel):
    def __init__(self, create_time=None, description=None, editing_config=None, input_config=None, job_type=None,
                 modified_time=None, output_config=None, title=None, user_id=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.editing_config = editing_config  # type: str
        self.input_config = input_config  # type: GetSmartHandleJobResponseBodySmartJobInfoInputConfig
        self.job_type = job_type  # type: str
        self.modified_time = modified_time  # type: str
        self.output_config = output_config  # type: GetSmartHandleJobResponseBodySmartJobInfoOutputConfig
        self.title = title  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.input_config:
            self.input_config.validate()
        if self.output_config:
            self.output_config.validate()

    def to_map(self):
        _map = super(GetSmartHandleJobResponseBodySmartJobInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config
        if self.input_config is not None:
            result['InputConfig'] = self.input_config.to_map()
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config.to_map()
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')
        if m.get('InputConfig') is not None:
            temp_model = GetSmartHandleJobResponseBodySmartJobInfoInputConfig()
            self.input_config = temp_model.from_map(m['InputConfig'])
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OutputConfig') is not None:
            temp_model = GetSmartHandleJobResponseBodySmartJobInfoOutputConfig()
            self.output_config = temp_model.from_map(m['OutputConfig'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetSmartHandleJobResponseBody(TeaModel):
    def __init__(self, feextend=None, job_id=None, output=None, request_id=None, smart_job_info=None, state=None,
                 user_data=None):
        self.feextend = feextend  # type: str
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.smart_job_info = smart_job_info  # type: GetSmartHandleJobResponseBodySmartJobInfo
        self.state = state  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        if self.smart_job_info:
            self.smart_job_info.validate()

    def to_map(self):
        _map = super(GetSmartHandleJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feextend is not None:
            result['FEExtend'] = self.feextend
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.smart_job_info is not None:
            result['SmartJobInfo'] = self.smart_job_info.to_map()
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FEExtend') is not None:
            self.feextend = m.get('FEExtend')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SmartJobInfo') is not None:
            temp_model = GetSmartHandleJobResponseBodySmartJobInfo()
            self.smart_job_info = temp_model.from_map(m['SmartJobInfo'])
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetSmartHandleJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSmartHandleJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSmartHandleJobResponse, self).to_map()
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
            temp_model = GetSmartHandleJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(self, related_mediaid_flag=None, template_id=None):
        # 是否返回模板关联素材，1返回，默认0，不返回
        self.related_mediaid_flag = related_mediaid_flag  # type: str
        # 模板Id
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.related_mediaid_flag is not None:
            result['RelatedMediaidFlag'] = self.related_mediaid_flag
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RelatedMediaidFlag') is not None:
            self.related_mediaid_flag = m.get('RelatedMediaidFlag')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetTemplateResponseBodyTemplate(TeaModel):
    def __init__(self, clips_param=None, config=None, cover_url=None, create_source=None, creation_time=None,
                 modified_source=None, modified_time=None, name=None, preview_media=None, preview_media_status=None,
                 related_mediaids=None, status=None, template_id=None, type=None):
        # 提交合成任务的ClipsParam参数
        self.clips_param = clips_param  # type: str
        # 模板配置
        self.config = config  # type: str
        # 封面URL
        self.cover_url = cover_url  # type: str
        # 创建来源
        self.create_source = create_source  # type: str
        # 创建时间
        self.creation_time = creation_time  # type: str
        # 修改来源
        self.modified_source = modified_source  # type: str
        # 修改时间
        self.modified_time = modified_time  # type: str
        # 模板名称
        self.name = name  # type: str
        # 预览素材
        self.preview_media = preview_media  # type: str
        # 预览素材状态
        self.preview_media_status = preview_media_status  # type: str
        # 模板关联素材
        self.related_mediaids = related_mediaids  # type: str
        # 模板状态
        self.status = status  # type: str
        # 模板ID
        self.template_id = template_id  # type: str
        # 模板类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTemplateResponseBodyTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        if self.config is not None:
            result['Config'] = self.config
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.preview_media_status is not None:
            result['PreviewMediaStatus'] = self.preview_media_status
        if self.related_mediaids is not None:
            result['RelatedMediaids'] = self.related_mediaids
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('PreviewMediaStatus') is not None:
            self.preview_media_status = m.get('PreviewMediaStatus')
        if m.get('RelatedMediaids') is not None:
            self.related_mediaids = m.get('RelatedMediaids')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.template = template  # type: GetTemplateResponseBodyTemplate

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(GetTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = GetTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class GetTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAllPublicMediaTagsRequest(TeaModel):
    def __init__(self, business_type=None):
        # 媒资业务类型
        self.business_type = business_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAllPublicMediaTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        return self


class ListAllPublicMediaTagsResponseBodyMediaTagList(TeaModel):
    def __init__(self, media_tag_id=None, media_tag_name_chinese=None, media_tag_name_english=None):
        # 素材标签id
        self.media_tag_id = media_tag_id  # type: str
        # 素材标签中文名
        self.media_tag_name_chinese = media_tag_name_chinese  # type: str
        # 素材标签英文名
        self.media_tag_name_english = media_tag_name_english  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAllPublicMediaTagsResponseBodyMediaTagList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_tag_id is not None:
            result['MediaTagId'] = self.media_tag_id
        if self.media_tag_name_chinese is not None:
            result['MediaTagNameChinese'] = self.media_tag_name_chinese
        if self.media_tag_name_english is not None:
            result['MediaTagNameEnglish'] = self.media_tag_name_english
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaTagId') is not None:
            self.media_tag_id = m.get('MediaTagId')
        if m.get('MediaTagNameChinese') is not None:
            self.media_tag_name_chinese = m.get('MediaTagNameChinese')
        if m.get('MediaTagNameEnglish') is not None:
            self.media_tag_name_english = m.get('MediaTagNameEnglish')
        return self


class ListAllPublicMediaTagsResponseBody(TeaModel):
    def __init__(self, media_tag_list=None, request_id=None):
        # 公共素材库标签列表
        self.media_tag_list = media_tag_list  # type: list[ListAllPublicMediaTagsResponseBodyMediaTagList]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.media_tag_list:
            for k in self.media_tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAllPublicMediaTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MediaTagList'] = []
        if self.media_tag_list is not None:
            for k in self.media_tag_list:
                result['MediaTagList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.media_tag_list = []
        if m.get('MediaTagList') is not None:
            for k in m.get('MediaTagList'):
                temp_model = ListAllPublicMediaTagsResponseBodyMediaTagList()
                self.media_tag_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAllPublicMediaTagsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAllPublicMediaTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAllPublicMediaTagsResponse, self).to_map()
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
            temp_model = ListAllPublicMediaTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMediaBasicInfosRequest(TeaModel):
    def __init__(self, business_type=None, category=None, end_time=None, include_file_basic_info=None,
                 max_results=None, media_type=None, next_token=None, sort_by=None, source=None, start_time=None, status=None):
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 分类
        self.category = category  # type: str
        # 结束时间
        self.end_time = end_time  # type: str
        # 返回值中是否包含文件基础信息
        self.include_file_basic_info = include_file_basic_info  # type: bool
        # 分页大小
        self.max_results = max_results  # type: int
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 页号
        self.next_token = next_token  # type: str
        # 排序
        self.sort_by = sort_by  # type: str
        # 来源
        self.source = source  # type: str
        # 创建时间
        self.start_time = start_time  # type: str
        # 资源状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMediaBasicInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.category is not None:
            result['Category'] = self.category
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.include_file_basic_info is not None:
            result['IncludeFileBasicInfo'] = self.include_file_basic_info
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.source is not None:
            result['Source'] = self.source
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IncludeFileBasicInfo') is not None:
            self.include_file_basic_info = m.get('IncludeFileBasicInfo')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(self, bitrate=None, duration=None, file_name=None, file_size=None, file_status=None, file_type=None,
                 file_url=None, format_name=None, height=None, region=None, width=None):
        # 码率
        self.bitrate = bitrate  # type: str
        # 时长
        self.duration = duration  # type: str
        # 文件名
        self.file_name = file_name  # type: str
        # 文件大小（字节）
        self.file_size = file_size  # type: str
        # 文件状态
        self.file_status = file_status  # type: str
        # 文件类型
        self.file_type = file_type  # type: str
        # 文件oss地址
        self.file_url = file_url  # type: str
        # 封装格式
        self.format_name = format_name  # type: str
        # 高
        self.height = height  # type: str
        # 文件存储区域
        self.region = region  # type: str
        # 宽
        self.width = width  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.height is not None:
            result['Height'] = self.height
        if self.region is not None:
            result['Region'] = self.region
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class ListMediaBasicInfosResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(self, file_basic_info=None):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info  # type: ListMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super(ListMediaBasicInfosResponseBodyMediaInfosFileInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = ListMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class ListMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(self, business_type=None, category=None, cover_url=None, create_time=None, deleted_time=None,
                 description=None, input_url=None, media_id=None, media_tags=None, media_type=None, modified_time=None,
                 snapshots=None, source=None, sprite_images=None, status=None, title=None, transcode_status=None,
                 user_data=None):
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 分类
        self.category = category  # type: str
        # 封面地址
        self.cover_url = cover_url  # type: str
        # 媒资创建时间
        self.create_time = create_time  # type: str
        # 媒资删除时间
        self.deleted_time = deleted_time  # type: str
        # 内容描述
        self.description = description  # type: str
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url  # type: str
        # MediaId
        self.media_id = media_id  # type: str
        # 标签
        self.media_tags = media_tags  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 媒资修改时间
        self.modified_time = modified_time  # type: str
        # 截图
        self.snapshots = snapshots  # type: str
        # 来源
        self.source = source  # type: str
        # 雪碧图
        self.sprite_images = sprite_images  # type: str
        # 资源状态
        self.status = status  # type: str
        # 标题
        self.title = title  # type: str
        # 转码状态
        self.transcode_status = transcode_status  # type: str
        # 用户数据
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.category is not None:
            result['Category'] = self.category
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.description is not None:
            result['Description'] = self.description
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.source is not None:
            result['Source'] = self.source
        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class ListMediaBasicInfosResponseBodyMediaInfos(TeaModel):
    def __init__(self, file_info_list=None, media_basic_info=None, media_id=None):
        # FileInfos
        self.file_info_list = file_info_list  # type: list[ListMediaBasicInfosResponseBodyMediaInfosFileInfoList]
        # BasicInfo
        self.media_basic_info = media_basic_info  # type: ListMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo
        # 媒资ID
        self.media_id = media_id  # type: str

    def validate(self):
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()
        if self.media_basic_info:
            self.media_basic_info.validate()

    def to_map(self):
        _map = super(ListMediaBasicInfosResponseBodyMediaInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = ListMediaBasicInfosResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        if m.get('MediaBasicInfo') is not None:
            temp_model = ListMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class ListMediaBasicInfosResponseBody(TeaModel):
    def __init__(self, max_results=None, media_infos=None, next_token=None, request_id=None, total_count=None):
        self.max_results = max_results  # type: int
        # 符合要求的媒资集合
        self.media_infos = media_infos  # type: list[ListMediaBasicInfosResponseBodyMediaInfos]
        self.next_token = next_token  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 符合要求的媒资总数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMediaBasicInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = ListMediaBasicInfosResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMediaBasicInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListMediaBasicInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMediaBasicInfosResponse, self).to_map()
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
            temp_model = ListMediaBasicInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMediaProducingJobsRequest(TeaModel):
    def __init__(self, status=None):
        # 查询以下状态的合成任务，支持多值，以英文逗号分隔
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMediaProducingJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListMediaProducingJobsResponseBodyMediaProducingJobList(TeaModel):
    def __init__(self, clips_param=None, code=None, complete_time=None, create_time=None, duration=None, job_id=None,
                 media_id=None, media_url=None, message=None, modified_time=None, project_id=None, status=None,
                 template_id=None):
        self.clips_param = clips_param  # type: str
        self.code = code  # type: str
        self.complete_time = complete_time  # type: str
        self.create_time = create_time  # type: str
        self.duration = duration  # type: float
        self.job_id = job_id  # type: str
        self.media_id = media_id  # type: str
        self.media_url = media_url  # type: str
        self.message = message  # type: str
        self.modified_time = modified_time  # type: str
        self.project_id = project_id  # type: str
        self.status = status  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMediaProducingJobsResponseBodyMediaProducingJobList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        if self.code is not None:
            result['Code'] = self.code
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_url is not None:
            result['MediaURL'] = self.media_url
        if self.message is not None:
            result['Message'] = self.message
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ListMediaProducingJobsResponseBody(TeaModel):
    def __init__(self, media_producing_job_list=None, request_id=None):
        self.media_producing_job_list = media_producing_job_list  # type: list[ListMediaProducingJobsResponseBodyMediaProducingJobList]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.media_producing_job_list:
            for k in self.media_producing_job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMediaProducingJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MediaProducingJobList'] = []
        if self.media_producing_job_list is not None:
            for k in self.media_producing_job_list:
                result['MediaProducingJobList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.media_producing_job_list = []
        if m.get('MediaProducingJobList') is not None:
            for k in m.get('MediaProducingJobList'):
                temp_model = ListMediaProducingJobsResponseBodyMediaProducingJobList()
                self.media_producing_job_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListMediaProducingJobsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListMediaProducingJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMediaProducingJobsResponse, self).to_map()
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
            temp_model = ListMediaProducingJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicMediaBasicInfosRequest(TeaModel):
    def __init__(self, include_file_basic_info=None, max_results=None, media_tag_id=None, next_token=None):
        # 返回值中是否包含文件基础信息
        self.include_file_basic_info = include_file_basic_info  # type: bool
        # 分页大小
        self.max_results = max_results  # type: int
        # 标签
        self.media_tag_id = media_tag_id  # type: str
        # 下一次读取的位置
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublicMediaBasicInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_file_basic_info is not None:
            result['IncludeFileBasicInfo'] = self.include_file_basic_info
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.media_tag_id is not None:
            result['MediaTagId'] = self.media_tag_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IncludeFileBasicInfo') is not None:
            self.include_file_basic_info = m.get('IncludeFileBasicInfo')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('MediaTagId') is not None:
            self.media_tag_id = m.get('MediaTagId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo(TeaModel):
    def __init__(self, bitrate=None, duration=None, file_name=None, file_size=None, file_status=None, file_type=None,
                 file_url=None, format_name=None, height=None, region=None, width=None):
        # 码率
        self.bitrate = bitrate  # type: str
        # 时长
        self.duration = duration  # type: str
        # 文件名
        self.file_name = file_name  # type: str
        # 文件大小（字节）
        self.file_size = file_size  # type: str
        # 文件状态
        self.file_status = file_status  # type: str
        # 文件类型
        self.file_type = file_type  # type: str
        # 文件oss地址
        self.file_url = file_url  # type: str
        # 封装格式
        self.format_name = format_name  # type: str
        # 高
        self.height = height  # type: str
        # 文件存储区域
        self.region = region  # type: str
        # 宽
        self.width = width  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_status is not None:
            result['FileStatus'] = self.file_status
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.height is not None:
            result['Height'] = self.height
        if self.region is not None:
            result['Region'] = self.region
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoList(TeaModel):
    def __init__(self, file_basic_info=None):
        # 文件基础信息，包含时长，大小等
        self.file_basic_info = file_basic_info  # type: ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        _map = super(ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m['FileBasicInfo'])
        return self


class ListPublicMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo(TeaModel):
    def __init__(self, business_type=None, category=None, cover_url=None, create_time=None, deleted_time=None,
                 description=None, input_url=None, media_id=None, media_tags=None, media_type=None, modified_time=None,
                 snapshots=None, source=None, status=None, title=None, transcode_status=None, user_data=None):
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 分类
        self.category = category  # type: str
        # 封面地址
        self.cover_url = cover_url  # type: str
        # 媒资创建时间
        self.create_time = create_time  # type: str
        # 媒资删除时间
        self.deleted_time = deleted_time  # type: str
        # 内容描述
        self.description = description  # type: str
        # 待注册的媒资在相应系统中的地址
        self.input_url = input_url  # type: str
        # MediaId
        self.media_id = media_id  # type: str
        # 标签
        self.media_tags = media_tags  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 媒资修改时间
        self.modified_time = modified_time  # type: str
        # 截图
        self.snapshots = snapshots  # type: str
        # 来源
        self.source = source  # type: str
        # 资源状态
        self.status = status  # type: str
        # 标题
        self.title = title  # type: str
        # 转码状态
        self.transcode_status = transcode_status  # type: str
        # 用户数据
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublicMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.category is not None:
            result['Category'] = self.category
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time
        if self.description is not None:
            result['Description'] = self.description
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class ListPublicMediaBasicInfosResponseBodyMediaInfos(TeaModel):
    def __init__(self, file_info_list=None, media_basic_info=None, media_id=None):
        # FileInfos
        self.file_info_list = file_info_list  # type: list[ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoList]
        # BasicInfo
        self.media_basic_info = media_basic_info  # type: ListPublicMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo
        # 媒资ID
        self.media_id = media_id  # type: str

    def validate(self):
        if self.file_info_list:
            for k in self.file_info_list:
                if k:
                    k.validate()
        if self.media_basic_info:
            self.media_basic_info.validate()

    def to_map(self):
        _map = super(ListPublicMediaBasicInfosResponseBodyMediaInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k in self.file_info_list:
                result['FileInfoList'].append(k.to_map() if k else None)
        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k in m.get('FileInfoList'):
                temp_model = ListPublicMediaBasicInfosResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k))
        if m.get('MediaBasicInfo') is not None:
            temp_model = ListPublicMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m['MediaBasicInfo'])
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class ListPublicMediaBasicInfosResponseBody(TeaModel):
    def __init__(self, max_results=None, media_infos=None, next_token=None, request_id=None, total_count=None):
        self.max_results = max_results  # type: int
        # 符合要求的媒资集合
        self.media_infos = media_infos  # type: list[ListPublicMediaBasicInfosResponseBodyMediaInfos]
        self.next_token = next_token  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 符合要求的媒资总数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.media_infos:
            for k in self.media_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPublicMediaBasicInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k in self.media_infos:
                result['MediaInfos'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k in m.get('MediaInfos'):
                temp_model = ListPublicMediaBasicInfosResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPublicMediaBasicInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPublicMediaBasicInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPublicMediaBasicInfosResponse, self).to_map()
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
            temp_model = ListPublicMediaBasicInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSmartJobsRequest(TeaModel):
    def __init__(self, job_state=None, job_type=None, max_results=None, next_token=None, page_no=None,
                 page_size=None, sort_by=None, status=None):
        self.job_state = job_state  # type: str
        self.job_type = job_type  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.sort_by = sort_by  # type: str
        self.status = status  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSmartJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_state is not None:
            result['JobState'] = self.job_state
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobState') is not None:
            self.job_state = m.get('JobState')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSmartJobsResponseBodySmartJobListInputConfig(TeaModel):
    def __init__(self, input_file=None, keyword=None):
        self.input_file = input_file  # type: str
        self.keyword = keyword  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSmartJobsResponseBodySmartJobListInputConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class ListSmartJobsResponseBodySmartJobListOutputConfig(TeaModel):
    def __init__(self, bucket=None, object=None):
        self.bucket = bucket  # type: str
        self.object = object  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSmartJobsResponseBodySmartJobListOutputConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.object is not None:
            result['Object'] = self.object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        return self


class ListSmartJobsResponseBodySmartJobList(TeaModel):
    def __init__(self, create_time=None, description=None, editing_config=None, input_config=None, job_id=None,
                 job_state=None, job_type=None, modified_time=None, output_config=None, title=None, user_data=None,
                 user_id=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.editing_config = editing_config  # type: str
        self.input_config = input_config  # type: ListSmartJobsResponseBodySmartJobListInputConfig
        self.job_id = job_id  # type: str
        self.job_state = job_state  # type: str
        self.job_type = job_type  # type: str
        self.modified_time = modified_time  # type: str
        self.output_config = output_config  # type: ListSmartJobsResponseBodySmartJobListOutputConfig
        self.title = title  # type: str
        self.user_data = user_data  # type: str
        self.user_id = user_id  # type: long

    def validate(self):
        if self.input_config:
            self.input_config.validate()
        if self.output_config:
            self.output_config.validate()

    def to_map(self):
        _map = super(ListSmartJobsResponseBodySmartJobList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config
        if self.input_config is not None:
            result['InputConfig'] = self.input_config.to_map()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_state is not None:
            result['JobState'] = self.job_state
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config.to_map()
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')
        if m.get('InputConfig') is not None:
            temp_model = ListSmartJobsResponseBodySmartJobListInputConfig()
            self.input_config = temp_model.from_map(m['InputConfig'])
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobState') is not None:
            self.job_state = m.get('JobState')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OutputConfig') is not None:
            temp_model = ListSmartJobsResponseBodySmartJobListOutputConfig()
            self.output_config = temp_model.from_map(m['OutputConfig'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListSmartJobsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, smart_job_list=None, total_count=None):
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.smart_job_list = smart_job_list  # type: list[ListSmartJobsResponseBodySmartJobList]
        self.total_count = total_count  # type: str

    def validate(self):
        if self.smart_job_list:
            for k in self.smart_job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSmartJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SmartJobList'] = []
        if self.smart_job_list is not None:
            for k in self.smart_job_list:
                result['SmartJobList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.smart_job_list = []
        if m.get('SmartJobList') is not None:
            for k in m.get('SmartJobList'):
                temp_model = ListSmartJobsResponseBodySmartJobList()
                self.smart_job_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSmartJobsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSmartJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSmartJobsResponse, self).to_map()
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
            temp_model = ListSmartJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSysTemplatesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, type=None):
        # 本次读取的最大数据记录数量
        self.max_results = max_results  # type: int
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSysTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListSysTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, config=None, name=None, template_id=None, type=None):
        self.config = config  # type: str
        self.name = name  # type: str
        self.template_id = template_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSysTemplatesResponseBodyTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListSysTemplatesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, templates=None, total_count=None):
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results  # type: int
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.templates = templates  # type: list[ListSysTemplatesResponseBodyTemplates]
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count  # type: int

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSysTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListSysTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSysTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSysTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSysTemplatesResponse, self).to_map()
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
            temp_model = ListSysTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(self, create_source=None, keyword=None, sort_type=None, status=None, type=None):
        # 创建来源
        self.create_source = create_source  # type: str
        # 搜索关键词，可以根据模板id和title搜索
        self.keyword = keyword  # type: str
        # 排序参数，默认根据创建时间倒序
        self.sort_type = sort_type  # type: str
        # 模板状态
        self.status = status  # type: str
        # 模板类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, clips_param=None, config=None, cover_url=None, create_source=None, creation_time=None,
                 modified_source=None, modified_time=None, name=None, preview_media=None, preview_media_status=None, status=None,
                 template_id=None, type=None):
        # ClipsParam
        self.clips_param = clips_param  # type: str
        # 模板配置
        self.config = config  # type: str
        # 封面URL
        self.cover_url = cover_url  # type: str
        # 创建来源
        self.create_source = create_source  # type: str
        # 创建时间
        self.creation_time = creation_time  # type: str
        # 修改来源
        self.modified_source = modified_source  # type: str
        # 修改时间
        self.modified_time = modified_time  # type: str
        # 模板名称
        self.name = name  # type: str
        # 预览素材
        self.preview_media = preview_media  # type: str
        # 预览素材状态
        self.preview_media_status = preview_media_status  # type: str
        # 模板状态
        self.status = status  # type: str
        # 模板ID
        self.template_id = template_id  # type: str
        # 模板类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesResponseBodyTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        if self.config is not None:
            result['Config'] = self.config
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.preview_media_status is not None:
            result['PreviewMediaStatus'] = self.preview_media_status
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('PreviewMediaStatus') is not None:
            self.preview_media_status = m.get('PreviewMediaStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None, templates=None, total_count=None):
        # 请求ID
        self.request_id = request_id  # type: str
        self.templates = templates  # type: list[ListTemplatesResponseBodyTemplates]
        # 本次请求条件下的数据总量。
        self.total_count = total_count  # type: int

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterMediaInfoRequest(TeaModel):
    def __init__(self, business_type=None, category=None, client_token=None, cover_url=None, description=None,
                 dynamic_meta_data_list=None, input_url=None, media_tags=None, media_type=None, overwrite=None, register_config=None,
                 title=None, user_data=None):
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 分类
        self.category = category  # type: str
        # 客户端token
        self.client_token = client_token  # type: str
        # 封面图，仅视频媒资有效
        self.cover_url = cover_url  # type: str
        # 描述
        self.description = description  # type: str
        # 用户自定义元数据
        self.dynamic_meta_data_list = dynamic_meta_data_list  # type: str
        # 媒资媒体url
        self.input_url = input_url  # type: str
        # 标签,如果有多个标签用逗号隔开
        self.media_tags = media_tags  # type: str
        # 媒资媒体类型
        self.media_type = media_type  # type: str
        # 是否覆盖已有媒资
        self.overwrite = overwrite  # type: bool
        # 注册媒资的配置
        self.register_config = register_config  # type: str
        # 标题
        self.title = title  # type: str
        # 用户数据，最大1024字节
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterMediaInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.category is not None:
            result['Category'] = self.category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.description is not None:
            result['Description'] = self.description
        if self.dynamic_meta_data_list is not None:
            result['DynamicMetaDataList'] = self.dynamic_meta_data_list
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.register_config is not None:
            result['RegisterConfig'] = self.register_config
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DynamicMetaDataList') is not None:
            self.dynamic_meta_data_list = m.get('DynamicMetaDataList')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('RegisterConfig') is not None:
            self.register_config = m.get('RegisterConfig')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class RegisterMediaInfoResponseBody(TeaModel):
    def __init__(self, media_id=None, request_id=None):
        # ICE媒资ID
        self.media_id = media_id  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterMediaInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterMediaInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RegisterMediaInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterMediaInfoResponse, self).to_map()
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
            temp_model = RegisterMediaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchEditingProjectRequest(TeaModel):
    def __init__(self, create_source=None, end_time=None, max_results=None, next_token=None, project_type=None,
                 sort_by=None, start_time=None, status=None, template_type=None):
        # 创建来源
        self.create_source = create_source  # type: str
        # CreationTime（创建时间）的结束时间
        self.end_time = end_time  # type: str
        # 分页参数
        self.max_results = max_results  # type: long
        # 分页参数
        self.next_token = next_token  # type: str
        self.project_type = project_type  # type: str
        # 结果排序方式
        self.sort_by = sort_by  # type: str
        # CreateTime（创建时间）的开始时间
        self.start_time = start_time  # type: str
        # 云剪辑工程状态。多个用逗号分隔
        self.status = status  # type: str
        # 模板类型
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchEditingProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class SearchEditingProjectResponseBodyProjectList(TeaModel):
    def __init__(self, business_config=None, business_status=None, cover_url=None, create_source=None,
                 create_time=None, description=None, duration=None, error_code=None, error_message=None, modified_source=None,
                 modified_time=None, project_id=None, project_type=None, status=None, template_type=None, timeline=None,
                 title=None):
        self.business_config = business_config  # type: str
        self.business_status = business_status  # type: str
        # 云剪辑工程封面
        self.cover_url = cover_url  # type: str
        # 创建来源
        self.create_source = create_source  # type: str
        # 云剪辑工程创建时间
        self.create_time = create_time  # type: str
        # 云剪辑工程描述
        self.description = description  # type: str
        # 云剪辑工程总时长
        self.duration = duration  # type: long
        # 云剪辑工程合成失败的错误码
        self.error_code = error_code  # type: str
        # 云剪辑工程合成失败的消息
        self.error_message = error_message  # type: str
        # 最后一次修改来源
        self.modified_source = modified_source  # type: str
        # 云剪辑工程最新修改时间
        self.modified_time = modified_time  # type: str
        # 云剪辑工程ID
        self.project_id = project_id  # type: str
        self.project_type = project_type  # type: str
        # 云剪辑工程状态
        self.status = status  # type: str
        # 模板类型
        self.template_type = template_type  # type: str
        # 云剪辑工程时间线
        self.timeline = timeline  # type: str
        # 云剪辑工程标题
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchEditingProjectResponseBodyProjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_config is not None:
            result['BusinessConfig'] = self.business_config
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.create_source is not None:
            result['CreateSource'] = self.create_source
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_type is not None:
            result['ProjectType'] = self.project_type
        if self.status is not None:
            result['Status'] = self.status
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessConfig') is not None:
            self.business_config = m.get('BusinessConfig')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SearchEditingProjectResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, project_list=None, request_id=None, total_count=None):
        # 云剪辑工程总数
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        # 云剪辑工程列表
        self.project_list = project_list  # type: list[SearchEditingProjectResponseBodyProjectList]
        # Id of the request
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.project_list:
            for k in self.project_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchEditingProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['ProjectList'] = []
        if self.project_list is not None:
            for k in self.project_list:
                result['ProjectList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.project_list = []
        if m.get('ProjectList') is not None:
            for k in m.get('ProjectList'):
                temp_model = SearchEditingProjectResponseBodyProjectList()
                self.project_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SearchEditingProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchEditingProjectResponse, self).to_map()
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
            temp_model = SearchEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultStorageLocationRequest(TeaModel):
    def __init__(self, bucket=None, path=None, storage_type=None):
        self.bucket = bucket  # type: str
        self.path = path  # type: str
        self.storage_type = storage_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultStorageLocationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.path is not None:
            result['Path'] = self.path
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class SetDefaultStorageLocationResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultStorageLocationResponseBody, self).to_map()
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


class SetDefaultStorageLocationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDefaultStorageLocationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDefaultStorageLocationResponse, self).to_map()
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
            temp_model = SetDefaultStorageLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetEventCallbackRequest(TeaModel):
    def __init__(self, callback_queue_name=None, event_type_list=None):
        self.callback_queue_name = callback_queue_name  # type: str
        self.event_type_list = event_type_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetEventCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_queue_name is not None:
            result['CallbackQueueName'] = self.callback_queue_name
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackQueueName') is not None:
            self.callback_queue_name = m.get('CallbackQueueName')
        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')
        return self


class SetEventCallbackResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否设置成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetEventCallbackResponseBody, self).to_map()
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


class SetEventCallbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetEventCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetEventCallbackResponse, self).to_map()
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
            temp_model = SetEventCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitASRJobRequest(TeaModel):
    def __init__(self, description=None, duration=None, input_file=None, start_time=None, title=None, user_data=None):
        # 任务描述
        self.description = description  # type: str
        # 持续时间
        self.duration = duration  # type: str
        # 输入配置，支持OSS地址和内容库素材ID
        self.input_file = input_file  # type: str
        # 开始时间
        self.start_time = start_time  # type: str
        # 任务标题
        self.title = title  # type: str
        # 自定义设置，为JSON字符串
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitASRJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitASRJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None, state=None):
        # 智能任务Id
        self.job_id = job_id  # type: str
        # 请求Id
        self.request_id = request_id  # type: str
        # 任务状态
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitASRJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class SubmitASRJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitASRJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitASRJobResponse, self).to_map()
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
            temp_model = SubmitASRJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAudioProduceJobRequest(TeaModel):
    def __init__(self, description=None, editing_config=None, input_config=None, output_config=None, overwrite=None,
                 title=None, user_data=None):
        self.description = description  # type: str
        self.editing_config = editing_config  # type: str
        self.input_config = input_config  # type: str
        self.output_config = output_config  # type: str
        self.overwrite = overwrite  # type: bool
        self.title = title  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAudioProduceJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config
        if self.input_config is not None:
            result['InputConfig'] = self.input_config
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')
        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitAudioProduceJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None, state=None):
        # 任务ID
        self.job_id = job_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 任务状态
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAudioProduceJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class SubmitAudioProduceJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitAudioProduceJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitAudioProduceJobResponse, self).to_map()
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
            temp_model = SubmitAudioProduceJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDelogoJobRequest(TeaModel):
    def __init__(self, description=None, input_file=None, input_type=None, output_config=None,
                 output_media_target=None, overwrite=None, title=None, user_data=None):
        self.description = description  # type: str
        # 输入文件
        self.input_file = input_file  # type: str
        # 输入文件类型
        self.input_type = input_type  # type: str
        # 输出bucket
        self.output_config = output_config  # type: str
        # 输出类型
        self.output_media_target = output_media_target  # type: str
        # 是否强制覆盖现有OSS文件
        self.overwrite = overwrite  # type: bool
        self.title = title  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDelogoJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.input_type is not None:
            result['InputType'] = self.input_type
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitDelogoJobResponseBody(TeaModel):
    def __init__(self, job_id=None, output=None, request_id=None, state=None, user_data=None):
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.state = state  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDelogoJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitDelogoJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitDelogoJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitDelogoJobResponse, self).to_map()
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
            temp_model = SubmitDelogoJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitH2VJobRequest(TeaModel):
    def __init__(self, description=None, input_file=None, input_type=None, output_config=None,
                 output_media_target=None, overwrite=None, title=None, user_data=None):
        self.description = description  # type: str
        # 输入文件
        self.input_file = input_file  # type: str
        # 输入文件类型
        self.input_type = input_type  # type: str
        # 输出bucket
        self.output_config = output_config  # type: str
        # 输出类型
        self.output_media_target = output_media_target  # type: str
        # 是否强制覆盖现有OSS文件
        self.overwrite = overwrite  # type: bool
        self.title = title  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitH2VJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.input_type is not None:
            result['InputType'] = self.input_type
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitH2VJobResponseBody(TeaModel):
    def __init__(self, job_id=None, output=None, request_id=None, state=None, user_data=None):
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.state = state  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitH2VJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitH2VJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitH2VJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitH2VJobResponse, self).to_map()
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
            temp_model = SubmitH2VJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitKeyWordCutJobRequest(TeaModel):
    def __init__(self, description=None, input_file=None, keyword=None, title=None, user_data=None):
        self.description = description  # type: str
        self.input_file = input_file  # type: str
        self.keyword = keyword  # type: str
        self.title = title  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitKeyWordCutJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitKeyWordCutJobResponseBody(TeaModel):
    def __init__(self, job_id=None, output=None, request_id=None, state=None, user_data=None):
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.state = state  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitKeyWordCutJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitKeyWordCutJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitKeyWordCutJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitKeyWordCutJobResponse, self).to_map()
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
            temp_model = SubmitKeyWordCutJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitLiveEditingJobRequest(TeaModel):
    def __init__(self, clips=None, live_stream_config=None, media_produce_config=None, output_media_config=None,
                 output_media_target=None, project_id=None, user_data=None):
        self.clips = clips  # type: str
        self.live_stream_config = live_stream_config  # type: str
        self.media_produce_config = media_produce_config  # type: str
        self.output_media_config = output_media_config  # type: str
        self.output_media_target = output_media_target  # type: str
        self.project_id = project_id  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitLiveEditingJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clips is not None:
            result['Clips'] = self.clips
        if self.live_stream_config is not None:
            result['LiveStreamConfig'] = self.live_stream_config
        if self.media_produce_config is not None:
            result['MediaProduceConfig'] = self.media_produce_config
        if self.output_media_config is not None:
            result['OutputMediaConfig'] = self.output_media_config
        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Clips') is not None:
            self.clips = m.get('Clips')
        if m.get('LiveStreamConfig') is not None:
            self.live_stream_config = m.get('LiveStreamConfig')
        if m.get('MediaProduceConfig') is not None:
            self.media_produce_config = m.get('MediaProduceConfig')
        if m.get('OutputMediaConfig') is not None:
            self.output_media_config = m.get('OutputMediaConfig')
        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitLiveEditingJobResponseBody(TeaModel):
    def __init__(self, job_id=None, media_id=None, media_url=None, project_id=None, request_id=None):
        self.job_id = job_id  # type: str
        self.media_id = media_id  # type: str
        self.media_url = media_url  # type: str
        self.project_id = project_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitLiveEditingJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_url is not None:
            result['MediaURL'] = self.media_url
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitLiveEditingJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitLiveEditingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitLiveEditingJobResponse, self).to_map()
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
            temp_model = SubmitLiveEditingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitMattingJobRequest(TeaModel):
    def __init__(self, description=None, input_file=None, input_type=None, output_config=None,
                 output_media_target=None, overwrite=None, title=None, user_data=None):
        self.description = description  # type: str
        # 输入文件
        self.input_file = input_file  # type: str
        # 输入文件类型
        self.input_type = input_type  # type: str
        # 输出bucket
        self.output_config = output_config  # type: str
        # 输出类型
        self.output_media_target = output_media_target  # type: str
        # 是否强制覆盖现有OSS文件
        self.overwrite = overwrite  # type: str
        self.title = title  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitMattingJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.input_type is not None:
            result['InputType'] = self.input_type
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitMattingJobResponseBody(TeaModel):
    def __init__(self, job_id=None, output=None, request_id=None, state=None, user_data=None):
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.state = state  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitMattingJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitMattingJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitMattingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitMattingJobResponse, self).to_map()
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
            temp_model = SubmitMattingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitMediaProducingJobRequest(TeaModel):
    def __init__(self, client_token=None, clips_param=None, output_media_config=None, output_media_target=None,
                 project_id=None, project_metadata=None, source=None, template_id=None, timeline=None, user_data=None):
        self.client_token = client_token  # type: str
        self.clips_param = clips_param  # type: str
        self.output_media_config = output_media_config  # type: str
        self.output_media_target = output_media_target  # type: str
        self.project_id = project_id  # type: str
        self.project_metadata = project_metadata  # type: str
        self.source = source  # type: str
        self.template_id = template_id  # type: str
        self.timeline = timeline  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitMediaProducingJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param
        if self.output_media_config is not None:
            result['OutputMediaConfig'] = self.output_media_config
        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_metadata is not None:
            result['ProjectMetadata'] = self.project_metadata
        if self.source is not None:
            result['Source'] = self.source
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')
        if m.get('OutputMediaConfig') is not None:
            self.output_media_config = m.get('OutputMediaConfig')
        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectMetadata') is not None:
            self.project_metadata = m.get('ProjectMetadata')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitMediaProducingJobResponseBody(TeaModel):
    def __init__(self, job_id=None, media_id=None, project_id=None, request_id=None):
        # 合成作业Id
        self.job_id = job_id  # type: str
        # 合成媒资Id
        self.media_id = media_id  # type: str
        # 剪辑工程Id
        self.project_id = project_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitMediaProducingJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitMediaProducingJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitMediaProducingJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitMediaProducingJobResponse, self).to_map()
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
            temp_model = SubmitMediaProducingJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitPPTCutJobRequest(TeaModel):
    def __init__(self, description=None, input_file=None, title=None, user_data=None):
        self.description = description  # type: str
        self.input_file = input_file  # type: str
        self.title = title  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitPPTCutJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.input_file is not None:
            result['InputFile'] = self.input_file
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitPPTCutJobResponseBody(TeaModel):
    def __init__(self, job_id=None, output=None, request_id=None, state=None, user_data=None):
        self.job_id = job_id  # type: str
        self.output = output  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.state = state  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitPPTCutJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitPPTCutJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitPPTCutJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitPPTCutJobResponse, self).to_map()
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
            temp_model = SubmitPPTCutJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSubtitleProduceJobRequest(TeaModel):
    def __init__(self, description=None, editing_config=None, input_config=None, is_async=None, output_config=None,
                 title=None, type=None, user_data=None):
        self.description = description  # type: str
        self.editing_config = editing_config  # type: str
        self.input_config = input_config  # type: str
        self.is_async = is_async  # type: long
        self.output_config = output_config  # type: str
        self.title = title  # type: str
        self.type = type  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSubtitleProduceJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config
        if self.input_config is not None:
            result['InputConfig'] = self.input_config
        if self.is_async is not None:
            result['IsAsync'] = self.is_async
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')
        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')
        if m.get('IsAsync') is not None:
            self.is_async = m.get('IsAsync')
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitSubtitleProduceJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        self.job_id = job_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSubtitleProduceJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitSubtitleProduceJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitSubtitleProduceJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitSubtitleProduceJobResponse, self).to_map()
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
            temp_model = SubmitSubtitleProduceJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEditingProjectRequest(TeaModel):
    def __init__(self, business_status=None, cover_url=None, description=None, project_id=None, timeline=None,
                 title=None):
        self.business_status = business_status  # type: str
        # 云剪辑工程封面
        self.cover_url = cover_url  # type: str
        # 云剪辑工程描述
        self.description = description  # type: str
        # 云剪辑工程ID
        self.project_id = project_id  # type: str
        # 云剪辑工程时间线，Json格式
        self.timeline = timeline  # type: str
        # 云剪辑工程标题
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEditingProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.description is not None:
            result['Description'] = self.description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateEditingProjectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEditingProjectResponseBody, self).to_map()
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


class UpdateEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEditingProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEditingProjectResponse, self).to_map()
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
            temp_model = UpdateEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMediaInfoRequest(TeaModel):
    def __init__(self, append_dynamic_meta=None, append_tags=None, business_type=None, category=None,
                 cover_url=None, description=None, dynamic_meta_data_list=None, input_url=None, media_id=None,
                 media_tags=None, title=None, user_data=None):
        # 是否以append的形式更新DynamicMetaDataList字段
        self.append_dynamic_meta = append_dynamic_meta  # type: bool
        # 是否以append的形式更新Tags字段
        self.append_tags = append_tags  # type: bool
        # 媒资业务类型
        self.business_type = business_type  # type: str
        # 分类
        self.category = category  # type: str
        # 封面图，仅视频媒资有效
        self.cover_url = cover_url  # type: str
        # 描述
        self.description = description  # type: str
        # 用户自定义元数据
        self.dynamic_meta_data_list = dynamic_meta_data_list  # type: str
        # 媒资媒体类型
        self.input_url = input_url  # type: str
        # 媒资Id
        self.media_id = media_id  # type: str
        # 标签,如果有多个标签用逗号隔开
        self.media_tags = media_tags  # type: str
        # 标题
        self.title = title  # type: str
        # 用户数据，最大1024字节
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMediaInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.append_dynamic_meta is not None:
            result['AppendDynamicMeta'] = self.append_dynamic_meta
        if self.append_tags is not None:
            result['AppendTags'] = self.append_tags
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.category is not None:
            result['Category'] = self.category
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.description is not None:
            result['Description'] = self.description
        if self.dynamic_meta_data_list is not None:
            result['DynamicMetaDataList'] = self.dynamic_meta_data_list
        if self.input_url is not None:
            result['InputURL'] = self.input_url
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppendDynamicMeta') is not None:
            self.append_dynamic_meta = m.get('AppendDynamicMeta')
        if m.get('AppendTags') is not None:
            self.append_tags = m.get('AppendTags')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DynamicMetaDataList') is not None:
            self.dynamic_meta_data_list = m.get('DynamicMetaDataList')
        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class UpdateMediaInfoResponseBody(TeaModel):
    def __init__(self, media_id=None, request_id=None):
        # ICE媒资ID
        self.media_id = media_id  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMediaInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateMediaInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateMediaInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateMediaInfoResponse, self).to_map()
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
            temp_model = UpdateMediaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSmartJobRequest(TeaModel):
    def __init__(self, feextend=None, job_id=None):
        self.feextend = feextend  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSmartJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feextend is not None:
            result['FEExtend'] = self.feextend
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FEExtend') is not None:
            self.feextend = m.get('FEExtend')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class UpdateSmartJobResponseBody(TeaModel):
    def __init__(self, feextend=None, job_id=None, request_id=None):
        self.feextend = feextend  # type: str
        self.job_id = job_id  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSmartJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feextend is not None:
            result['FEExtend'] = self.feextend
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FEExtend') is not None:
            self.feextend = m.get('FEExtend')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSmartJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSmartJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSmartJobResponse, self).to_map()
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
            temp_model = UpdateSmartJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(self, config=None, cover_url=None, name=None, preview_media=None, source=None, status=None,
                 template_id=None):
        # 参见Timeline模板Config文档
        self.config = config  # type: str
        # 模板封面
        self.cover_url = cover_url  # type: str
        # 模板名称
        self.name = name  # type: str
        # 预览视频媒资id
        self.preview_media = preview_media  # type: str
        # 修改来源，默认OpenAPI
        self.source = source  # type: str
        # 模板状态
        self.status = status  # type: str
        # 模板ID
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.name is not None:
            result['Name'] = self.name
        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTemplateResponseBody, self).to_map()
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


class UpdateTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


