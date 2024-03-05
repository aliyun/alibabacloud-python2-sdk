# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class Address(TeaModel):
    def __init__(self, address_line=None, city=None, country=None, district=None, language=None, province=None,
                 township=None):
        self.address_line = address_line  # type: str
        self.city = city  # type: str
        self.country = country  # type: str
        self.district = district  # type: str
        self.language = language  # type: str
        self.province = province  # type: str
        self.township = township  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Address, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_line is not None:
            result['AddressLine'] = self.address_line
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.district is not None:
            result['District'] = self.district
        if self.language is not None:
            result['Language'] = self.language
        if self.province is not None:
            result['Province'] = self.province
        if self.township is not None:
            result['Township'] = self.township
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressLine') is not None:
            self.address_line = m.get('AddressLine')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Township') is not None:
            self.township = m.get('Township')
        return self


class AddressForStory(TeaModel):
    def __init__(self, city=None, country=None, district=None, province=None, township=None):
        self.city = city  # type: str
        self.country = country  # type: str
        self.district = district  # type: str
        self.province = province  # type: str
        self.township = township  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddressForStory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.district is not None:
            result['District'] = self.district
        if self.province is not None:
            result['Province'] = self.province
        if self.township is not None:
            result['Township'] = self.township
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Township') is not None:
            self.township = m.get('Township')
        return self


class AlgorithmDefinition(TeaModel):
    def __init__(self, algorithm_definition_id=None, create_time=None, custom_labels=None, description=None,
                 name=None, owner_id=None, project_name=None, training_specification=None, update_time=None):
        self.algorithm_definition_id = algorithm_definition_id  # type: str
        self.create_time = create_time  # type: str
        self.custom_labels = custom_labels  # type: list[dict[str, str]]
        self.description = description  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: str
        self.project_name = project_name  # type: str
        self.training_specification = training_specification  # type: TrainingSpecification
        self.update_time = update_time  # type: str

    def validate(self):
        if self.training_specification:
            self.training_specification.validate()

    def to_map(self):
        _map = super(AlgorithmDefinition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_definition_id is not None:
            result['AlgorithmDefinitionId'] = self.algorithm_definition_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.training_specification is not None:
            result['TrainingSpecification'] = self.training_specification.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmDefinitionId') is not None:
            self.algorithm_definition_id = m.get('AlgorithmDefinitionId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TrainingSpecification') is not None:
            temp_model = TrainingSpecification()
            self.training_specification = temp_model.from_map(m['TrainingSpecification'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class App(TeaModel):
    def __init__(self, app_description=None, app_id=None, app_key=None, app_name=None, app_region=None,
                 app_type=None, english_name=None, owner_id=None, package_name=None):
        self.app_description = app_description  # type: str
        self.app_id = app_id  # type: str
        self.app_key = app_key  # type: str
        self.app_name = app_name  # type: str
        self.app_region = app_region  # type: long
        self.app_type = app_type  # type: long
        self.english_name = english_name  # type: str
        self.owner_id = owner_id  # type: str
        self.package_name = package_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(App, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_region is not None:
            result['AppRegion'] = self.app_region
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.english_name is not None:
            result['EnglishName'] = self.english_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppRegion') is not None:
            self.app_region = m.get('AppRegion')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('EnglishName') is not None:
            self.english_name = m.get('EnglishName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        return self


class AssumeRoleChain(TeaModel):
    def __init__(self, chain=None, policy=None):
        self.chain = chain  # type: list[AssumeRoleChainNode]
        self.policy = policy  # type: str

    def validate(self):
        if self.chain:
            for k in self.chain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AssumeRoleChain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Chain'] = []
        if self.chain is not None:
            for k in self.chain:
                result['Chain'].append(k.to_map() if k else None)
        if self.policy is not None:
            result['Policy'] = self.policy
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.chain = []
        if m.get('Chain') is not None:
            for k in m.get('Chain'):
                temp_model = AssumeRoleChainNode()
                self.chain.append(temp_model.from_map(k))
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        return self


class AssumeRoleChainNode(TeaModel):
    def __init__(self, owner_id=None, role=None, type=None):
        self.owner_id = owner_id  # type: str
        self.role = role  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssumeRoleChainNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.role is not None:
            result['Role'] = self.role
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AudioStream(TeaModel):
    def __init__(self, bitrate=None, channel_layout=None, channels=None, codec_long_name=None, codec_name=None,
                 codec_tag=None, codec_tag_string=None, codec_time_base=None, duration=None, frame_count=None, index=None,
                 language=None, lyric=None, sample_format=None, sample_rate=None, start_time=None, time_base=None):
        self.bitrate = bitrate  # type: long
        self.channel_layout = channel_layout  # type: str
        self.channels = channels  # type: long
        self.codec_long_name = codec_long_name  # type: str
        self.codec_name = codec_name  # type: str
        self.codec_tag = codec_tag  # type: str
        self.codec_tag_string = codec_tag_string  # type: str
        self.codec_time_base = codec_time_base  # type: str
        self.duration = duration  # type: float
        self.frame_count = frame_count  # type: long
        self.index = index  # type: long
        self.language = language  # type: str
        self.lyric = lyric  # type: str
        self.sample_format = sample_format  # type: str
        self.sample_rate = sample_rate  # type: long
        self.start_time = start_time  # type: float
        self.time_base = time_base  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AudioStream, self).to_map()
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
        if self.frame_count is not None:
            result['FrameCount'] = self.frame_count
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        if self.lyric is not None:
            result['Lyric'] = self.lyric
        if self.sample_format is not None:
            result['SampleFormat'] = self.sample_format
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_base is not None:
            result['TimeBase'] = self.time_base
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
        if m.get('FrameCount') is not None:
            self.frame_count = m.get('FrameCount')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Lyric') is not None:
            self.lyric = m.get('Lyric')
        if m.get('SampleFormat') is not None:
            self.sample_format = m.get('SampleFormat')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeBase') is not None:
            self.time_base = m.get('TimeBase')
        return self


class Binding(TeaModel):
    def __init__(self, create_time=None, dataset_name=None, detail=None, phase=None, project_name=None, state=None,
                 uri=None, update_time=None):
        self.create_time = create_time  # type: str
        self.dataset_name = dataset_name  # type: str
        self.detail = detail  # type: str
        self.phase = phase  # type: str
        self.project_name = project_name  # type: str
        self.state = state  # type: str
        self.uri = uri  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Binding, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.state is not None:
            result['State'] = self.state
        if self.uri is not None:
            result['URI'] = self.uri
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class Body(TeaModel):
    def __init__(self, boundary=None, confidence=None):
        self.boundary = boundary  # type: Boundary
        self.confidence = confidence  # type: float

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super(Body, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class Boundary(TeaModel):
    def __init__(self, height=None, left=None, polygon=None, top=None, width=None):
        self.height = height  # type: long
        self.left = left  # type: long
        self.polygon = polygon  # type: list[PointInt64]
        self.top = top  # type: long
        self.width = width  # type: long

    def validate(self):
        if self.polygon:
            for k in self.polygon:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Boundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        result['Polygon'] = []
        if self.polygon is not None:
            for k in self.polygon:
                result['Polygon'].append(k.to_map() if k else None)
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
        self.polygon = []
        if m.get('Polygon') is not None:
            for k in m.get('Polygon'):
                temp_model = PointInt64()
                self.polygon.append(temp_model.from_map(k))
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class Car(TeaModel):
    def __init__(self, boundary=None, car_color=None, car_color_confidence=None, car_type=None,
                 car_type_confidence=None, confidence=None, license_plates=None):
        self.boundary = boundary  # type: Boundary
        self.car_color = car_color  # type: str
        self.car_color_confidence = car_color_confidence  # type: float
        self.car_type = car_type  # type: str
        self.car_type_confidence = car_type_confidence  # type: float
        self.confidence = confidence  # type: float
        self.license_plates = license_plates  # type: list[LicensePlate]

    def validate(self):
        if self.boundary:
            self.boundary.validate()
        if self.license_plates:
            for k in self.license_plates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Car, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.car_color is not None:
            result['CarColor'] = self.car_color
        if self.car_color_confidence is not None:
            result['CarColorConfidence'] = self.car_color_confidence
        if self.car_type is not None:
            result['CarType'] = self.car_type
        if self.car_type_confidence is not None:
            result['CarTypeConfidence'] = self.car_type_confidence
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        result['LicensePlates'] = []
        if self.license_plates is not None:
            for k in self.license_plates:
                result['LicensePlates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('CarColor') is not None:
            self.car_color = m.get('CarColor')
        if m.get('CarColorConfidence') is not None:
            self.car_color_confidence = m.get('CarColorConfidence')
        if m.get('CarType') is not None:
            self.car_type = m.get('CarType')
        if m.get('CarTypeConfidence') is not None:
            self.car_type_confidence = m.get('CarTypeConfidence')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        self.license_plates = []
        if m.get('LicensePlates') is not None:
            for k in m.get('LicensePlates'):
                temp_model = LicensePlate()
                self.license_plates.append(temp_model.from_map(k))
        return self


class ClusterForReqCoverFigures(TeaModel):
    def __init__(self, figure_id=None):
        self.figure_id = figure_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClusterForReqCoverFigures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        return self


class ClusterForReqCover(TeaModel):
    def __init__(self, figures=None):
        self.figures = figures  # type: list[ClusterForReqCoverFigures]

    def validate(self):
        if self.figures:
            for k in self.figures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ClusterForReqCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Figures'] = []
        if self.figures is not None:
            for k in self.figures:
                result['Figures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.figures = []
        if m.get('Figures') is not None:
            for k in m.get('Figures'):
                temp_model = ClusterForReqCoverFigures()
                self.figures.append(temp_model.from_map(k))
        return self


class ClusterForReq(TeaModel):
    def __init__(self, cover=None, custom_id=None, custom_labels=None, name=None, object_id=None):
        self.cover = cover  # type: ClusterForReqCover
        self.custom_id = custom_id  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]
        self.name = name  # type: str
        self.object_id = object_id  # type: str

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(ClusterForReq, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.name is not None:
            result['Name'] = self.name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cover') is not None:
            temp_model = ClusterForReqCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        return self


class Codes(TeaModel):
    def __init__(self, boundary=None, confidence=None, content=None, type=None):
        self.boundary = boundary  # type: Boundary
        self.confidence = confidence  # type: float
        self.content = content  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super(Codes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.content is not None:
            result['Content'] = self.content
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CredentialConfigChain(TeaModel):
    def __init__(self, assume_role_for=None, role=None, role_type=None):
        self.assume_role_for = assume_role_for  # type: str
        self.role = role  # type: str
        self.role_type = role_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CredentialConfigChain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for
        if self.role is not None:
            result['Role'] = self.role
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class CredentialConfig(TeaModel):
    def __init__(self, chain=None, policy=None, service_role=None):
        self.chain = chain  # type: list[CredentialConfigChain]
        self.policy = policy  # type: str
        self.service_role = service_role  # type: str

    def validate(self):
        if self.chain:
            for k in self.chain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CredentialConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Chain'] = []
        if self.chain is not None:
            for k in self.chain:
                result['Chain'].append(k.to_map() if k else None)
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.chain = []
        if m.get('Chain') is not None:
            for k in m.get('Chain'):
                temp_model = CredentialConfigChain()
                self.chain.append(temp_model.from_map(k))
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        return self


class CroppingSuggestion(TeaModel):
    def __init__(self, aspect_ratio=None, boundary=None, confidence=None):
        self.aspect_ratio = aspect_ratio  # type: str
        self.boundary = boundary  # type: Boundary
        self.confidence = confidence  # type: float

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super(CroppingSuggestion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        return self


class CustomParams(TeaModel):
    def __init__(self, name=None, properties=None):
        self.name = name  # type: str
        self.properties = properties  # type: list[Property]

    def validate(self):
        if self.properties:
            for k in self.properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CustomParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['Properties'] = []
        if self.properties is not None:
            for k in self.properties:
                result['Properties'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.properties = []
        if m.get('Properties') is not None:
            for k in m.get('Properties'):
                temp_model = Property()
                self.properties.append(temp_model.from_map(k))
        return self


class DataIngestionActions(TeaModel):
    def __init__(self, fast_fail_policy=None, name=None, parameters=None):
        self.fast_fail_policy = fast_fail_policy  # type: FastFailPolicy
        self.name = name  # type: str
        self.parameters = parameters  # type: list[str]

    def validate(self):
        if self.fast_fail_policy:
            self.fast_fail_policy.validate()

    def to_map(self):
        _map = super(DataIngestionActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fast_fail_policy is not None:
            result['FastFailPolicy'] = self.fast_fail_policy.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FastFailPolicy') is not None:
            temp_model = FastFailPolicy()
            self.fast_fail_policy = temp_model.from_map(m['FastFailPolicy'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class DataIngestionNotification(TeaModel):
    def __init__(self, endpoint=None, mns=None, rocket_mq=None, topic=None):
        self.endpoint = endpoint  # type: str
        self.mns = mns  # type: MNS
        self.rocket_mq = rocket_mq  # type: RocketMQ
        self.topic = topic  # type: str

    def validate(self):
        if self.mns:
            self.mns.validate()
        if self.rocket_mq:
            self.rocket_mq.validate()

    def to_map(self):
        _map = super(DataIngestionNotification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.mns is not None:
            result['MNS'] = self.mns.to_map()
        if self.rocket_mq is not None:
            result['RocketMQ'] = self.rocket_mq.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('MNS') is not None:
            temp_model = MNS()
            self.mns = temp_model.from_map(m['MNS'])
        if m.get('RocketMQ') is not None:
            temp_model = RocketMQ()
            self.rocket_mq = temp_model.from_map(m['RocketMQ'])
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class DataIngestionStatistic(TeaModel):
    def __init__(self, submit_failure=None, submit_success=None):
        self.submit_failure = submit_failure  # type: long
        self.submit_success = submit_success  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataIngestionStatistic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.submit_failure is not None:
            result['SubmitFailure'] = self.submit_failure
        if self.submit_success is not None:
            result['SubmitSuccess'] = self.submit_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubmitFailure') is not None:
            self.submit_failure = m.get('SubmitFailure')
        if m.get('SubmitSuccess') is not None:
            self.submit_success = m.get('SubmitSuccess')
        return self


class DataIngestion(TeaModel):
    def __init__(self, actions=None, create_time=None, error=None, id=None, input=None, marker=None,
                 notification=None, phase=None, state=None, statistic=None, tags=None, update_time=None):
        self.actions = actions  # type: list[DataIngestionActions]
        self.create_time = create_time  # type: str
        self.error = error  # type: str
        self.id = id  # type: str
        self.input = input  # type: Input
        self.marker = marker  # type: str
        self.notification = notification  # type: DataIngestionNotification
        self.phase = phase  # type: str
        self.state = state  # type: str
        self.statistic = statistic  # type: DataIngestionStatistic
        self.tags = tags  # type: dict[str, any]
        self.update_time = update_time  # type: str

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.input:
            self.input.validate()
        if self.notification:
            self.notification.validate()
        if self.statistic:
            self.statistic.validate()

    def to_map(self):
        _map = super(DataIngestion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.state is not None:
            result['State'] = self.state
        if self.statistic is not None:
            result['Statistic'] = self.statistic.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = DataIngestionActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Input') is not None:
            temp_model = Input()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('Notification') is not None:
            temp_model = DataIngestionNotification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Statistic') is not None:
            temp_model = DataIngestionStatistic()
            self.statistic = temp_model.from_map(m['Statistic'])
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class Dataset(TeaModel):
    def __init__(self, bind_count=None, create_time=None, dataset_max_bind_count=None,
                 dataset_max_entity_count=None, dataset_max_file_count=None, dataset_max_relation_count=None,
                 dataset_max_total_file_size=None, dataset_name=None, description=None, file_count=None, project_name=None, template_id=None,
                 total_file_size=None, update_time=None):
        self.bind_count = bind_count  # type: long
        self.create_time = create_time  # type: str
        self.dataset_max_bind_count = dataset_max_bind_count  # type: long
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        self.dataset_max_total_file_size = dataset_max_total_file_size  # type: long
        self.dataset_name = dataset_name  # type: str
        self.description = description  # type: str
        self.file_count = file_count  # type: long
        self.project_name = project_name  # type: str
        self.template_id = template_id  # type: str
        self.total_file_size = total_file_size  # type: long
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Dataset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_count is not None:
            result['BindCount'] = self.bind_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.file_count is not None:
            result['FileCount'] = self.file_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.total_file_size is not None:
            result['TotalFileSize'] = self.total_file_size
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TotalFileSize') is not None:
            self.total_file_size = m.get('TotalFileSize')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class Element(TeaModel):
    def __init__(self, element_contents=None):
        self.element_contents = element_contents  # type: list[ElementContent]

    def validate(self):
        if self.element_contents:
            for k in self.element_contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Element, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ElementContents'] = []
        if self.element_contents is not None:
            for k in self.element_contents:
                result['ElementContents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.element_contents = []
        if m.get('ElementContents') is not None:
            for k in m.get('ElementContents'):
                temp_model = ElementContent()
                self.element_contents.append(temp_model.from_map(k))
        return self


class ElementContent(TeaModel):
    def __init__(self, content=None, type=None, url=None):
        self.content = content  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ElementContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class FastFailPolicy(TeaModel):
    def __init__(self, action=None):
        self.action = action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FastFailPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        return self


class Figure(TeaModel):
    def __init__(self, age=None, age_sd=None, attractive=None, beard=None, beard_confidence=None, boundary=None,
                 emotion=None, emotion_confidence=None, face_quality=None, figure_cluster_confidence=None,
                 figure_cluster_id=None, figure_confidence=None, figure_id=None, figure_type=None, gender=None,
                 gender_confidence=None, glasses=None, glasses_confidence=None, hat=None, hat_confidence=None, head_pose=None,
                 mask=None, mask_confidence=None, mouth=None, mouth_confidence=None, sharpness=None):
        self.age = age  # type: long
        self.age_sd = age_sd  # type: float
        self.attractive = attractive  # type: float
        self.beard = beard  # type: str
        self.beard_confidence = beard_confidence  # type: float
        self.boundary = boundary  # type: Boundary
        self.emotion = emotion  # type: str
        self.emotion_confidence = emotion_confidence  # type: float
        self.face_quality = face_quality  # type: float
        self.figure_cluster_confidence = figure_cluster_confidence  # type: float
        self.figure_cluster_id = figure_cluster_id  # type: str
        self.figure_confidence = figure_confidence  # type: float
        self.figure_id = figure_id  # type: str
        self.figure_type = figure_type  # type: str
        self.gender = gender  # type: str
        self.gender_confidence = gender_confidence  # type: float
        self.glasses = glasses  # type: str
        self.glasses_confidence = glasses_confidence  # type: float
        self.hat = hat  # type: str
        self.hat_confidence = hat_confidence  # type: float
        self.head_pose = head_pose  # type: HeadPose
        self.mask = mask  # type: str
        self.mask_confidence = mask_confidence  # type: float
        self.mouth = mouth  # type: str
        self.mouth_confidence = mouth_confidence  # type: float
        self.sharpness = sharpness  # type: float

    def validate(self):
        if self.boundary:
            self.boundary.validate()
        if self.head_pose:
            self.head_pose.validate()

    def to_map(self):
        _map = super(Figure, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age is not None:
            result['Age'] = self.age
        if self.age_sd is not None:
            result['AgeSD'] = self.age_sd
        if self.attractive is not None:
            result['Attractive'] = self.attractive
        if self.beard is not None:
            result['Beard'] = self.beard
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.figure_cluster_confidence is not None:
            result['FigureClusterConfidence'] = self.figure_cluster_confidence
        if self.figure_cluster_id is not None:
            result['FigureClusterId'] = self.figure_cluster_id
        if self.figure_confidence is not None:
            result['FigureConfidence'] = self.figure_confidence
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        if self.figure_type is not None:
            result['FigureType'] = self.figure_type
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence
        if self.hat is not None:
            result['Hat'] = self.hat
        if self.hat_confidence is not None:
            result['HatConfidence'] = self.hat_confidence
        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.mouth is not None:
            result['Mouth'] = self.mouth
        if self.mouth_confidence is not None:
            result['MouthConfidence'] = self.mouth_confidence
        if self.sharpness is not None:
            result['Sharpness'] = self.sharpness
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('AgeSD') is not None:
            self.age_sd = m.get('AgeSD')
        if m.get('Attractive') is not None:
            self.attractive = m.get('Attractive')
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('FigureClusterConfidence') is not None:
            self.figure_cluster_confidence = m.get('FigureClusterConfidence')
        if m.get('FigureClusterId') is not None:
            self.figure_cluster_id = m.get('FigureClusterId')
        if m.get('FigureConfidence') is not None:
            self.figure_confidence = m.get('FigureConfidence')
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        if m.get('FigureType') is not None:
            self.figure_type = m.get('FigureType')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')
        if m.get('Hat') is not None:
            self.hat = m.get('Hat')
        if m.get('HatConfidence') is not None:
            self.hat_confidence = m.get('HatConfidence')
        if m.get('HeadPose') is not None:
            temp_model = HeadPose()
            self.head_pose = temp_model.from_map(m['HeadPose'])
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('Mouth') is not None:
            self.mouth = m.get('Mouth')
        if m.get('MouthConfidence') is not None:
            self.mouth_confidence = m.get('MouthConfidence')
        if m.get('Sharpness') is not None:
            self.sharpness = m.get('Sharpness')
        return self


class FigureCluster(TeaModel):
    def __init__(self, average_age=None, cover=None, create_time=None, custom_id=None, custom_labels=None,
                 dataset_name=None, face_count=None, gender=None, image_count=None, max_age=None, meta_lock_version=None,
                 min_age=None, name=None, object_id=None, object_type=None, owner_id=None, project_name=None,
                 update_time=None, video_count=None):
        self.average_age = average_age  # type: float
        self.cover = cover  # type: File
        self.create_time = create_time  # type: str
        self.custom_id = custom_id  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]
        self.dataset_name = dataset_name  # type: str
        self.face_count = face_count  # type: long
        self.gender = gender  # type: str
        self.image_count = image_count  # type: long
        self.max_age = max_age  # type: float
        self.meta_lock_version = meta_lock_version  # type: long
        self.min_age = min_age  # type: float
        self.name = name  # type: str
        self.object_id = object_id  # type: str
        self.object_type = object_type  # type: str
        self.owner_id = owner_id  # type: str
        self.project_name = project_name  # type: str
        self.update_time = update_time  # type: str
        self.video_count = video_count  # type: long

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(FigureCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_age is not None:
            result['AverageAge'] = self.average_age
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.max_age is not None:
            result['MaxAge'] = self.max_age
        if self.meta_lock_version is not None:
            result['MetaLockVersion'] = self.meta_lock_version
        if self.min_age is not None:
            result['MinAge'] = self.min_age
        if self.name is not None:
            result['Name'] = self.name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.video_count is not None:
            result['VideoCount'] = self.video_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AverageAge') is not None:
            self.average_age = m.get('AverageAge')
        if m.get('Cover') is not None:
            temp_model = File()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('MaxAge') is not None:
            self.max_age = m.get('MaxAge')
        if m.get('MetaLockVersion') is not None:
            self.meta_lock_version = m.get('MetaLockVersion')
        if m.get('MinAge') is not None:
            self.min_age = m.get('MinAge')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VideoCount') is not None:
            self.video_count = m.get('VideoCount')
        return self


class FigureClusterForReqCoverFigures(TeaModel):
    def __init__(self, figure_id=None):
        self.figure_id = figure_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FigureClusterForReqCoverFigures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        return self


class FigureClusterForReqCover(TeaModel):
    def __init__(self, figures=None):
        self.figures = figures  # type: list[FigureClusterForReqCoverFigures]

    def validate(self):
        if self.figures:
            for k in self.figures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FigureClusterForReqCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Figures'] = []
        if self.figures is not None:
            for k in self.figures:
                result['Figures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.figures = []
        if m.get('Figures') is not None:
            for k in m.get('Figures'):
                temp_model = FigureClusterForReqCoverFigures()
                self.figures.append(temp_model.from_map(k))
        return self


class FigureClusterForReq(TeaModel):
    def __init__(self, cover=None, custom_id=None, custom_labels=None, meta_lock_version=None, name=None,
                 object_id=None):
        self.cover = cover  # type: FigureClusterForReqCover
        self.custom_id = custom_id  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]
        self.meta_lock_version = meta_lock_version  # type: long
        self.name = name  # type: str
        self.object_id = object_id  # type: str

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(FigureClusterForReq, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.meta_lock_version is not None:
            result['MetaLockVersion'] = self.meta_lock_version
        if self.name is not None:
            result['Name'] = self.name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cover') is not None:
            temp_model = FigureClusterForReqCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('MetaLockVersion') is not None:
            self.meta_lock_version = m.get('MetaLockVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        return self


class File(TeaModel):
    def __init__(self, access_control_allow_origin=None, access_control_request_method=None, addresses=None,
                 album=None, album_artist=None, artist=None, audio_covers=None, audio_streams=None, bitrate=None,
                 cache_control=None, composer=None, content_disposition=None, content_encoding=None, content_language=None,
                 content_md_5=None, content_type=None, create_time=None, cropping_suggestions=None, custom_id=None,
                 custom_labels=None, dataset_name=None, duration=None, etag=None, exif=None, elements=None, figure_count=None,
                 figures=None, file_access_time=None, file_create_time=None, file_hash=None, file_modified_time=None,
                 filename=None, format_long_name=None, format_name=None, image_height=None, image_score=None,
                 image_width=None, labels=None, language=None, lat_long=None, media_type=None, ocrcontents=None, ocrtexts=None,
                 osscrc64=None, ossdelete_marker=None, ossexpiration=None, ossobject_type=None, ossstorage_class=None,
                 osstagging=None, osstagging_count=None, ossuri=None, ossuser_meta=None, ossversion_id=None, object_acl=None,
                 object_id=None, object_type=None, orientation=None, owner_id=None, page_count=None, performer=None,
                 produce_time=None, program_count=None, project_name=None, semantic_types=None,
                 server_side_data_encryption=None, server_side_encryption=None, server_side_encryption_customer_algorithm=None,
                 server_side_encryption_key_id=None, size=None, start_time=None, stream_count=None, subtitles=None, timezone=None, title=None,
                 travel_cluster_id=None, uri=None, update_time=None, video_height=None, video_streams=None, video_width=None):
        self.access_control_allow_origin = access_control_allow_origin  # type: str
        self.access_control_request_method = access_control_request_method  # type: str
        self.addresses = addresses  # type: list[Address]
        self.album = album  # type: str
        self.album_artist = album_artist  # type: str
        self.artist = artist  # type: str
        self.audio_covers = audio_covers  # type: list[Image]
        self.audio_streams = audio_streams  # type: list[AudioStream]
        self.bitrate = bitrate  # type: long
        self.cache_control = cache_control  # type: str
        self.composer = composer  # type: str
        self.content_disposition = content_disposition  # type: str
        self.content_encoding = content_encoding  # type: str
        self.content_language = content_language  # type: str
        self.content_md_5 = content_md_5  # type: str
        self.content_type = content_type  # type: str
        self.create_time = create_time  # type: str
        self.cropping_suggestions = cropping_suggestions  # type: list[CroppingSuggestion]
        self.custom_id = custom_id  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]
        self.dataset_name = dataset_name  # type: str
        self.duration = duration  # type: float
        self.etag = etag  # type: str
        self.exif = exif  # type: str
        self.elements = elements  # type: list[Element]
        self.figure_count = figure_count  # type: long
        self.figures = figures  # type: list[Figure]
        self.file_access_time = file_access_time  # type: str
        self.file_create_time = file_create_time  # type: str
        self.file_hash = file_hash  # type: str
        self.file_modified_time = file_modified_time  # type: str
        self.filename = filename  # type: str
        self.format_long_name = format_long_name  # type: str
        self.format_name = format_name  # type: str
        self.image_height = image_height  # type: long
        self.image_score = image_score  # type: ImageScore
        self.image_width = image_width  # type: long
        self.labels = labels  # type: list[Label]
        self.language = language  # type: str
        self.lat_long = lat_long  # type: str
        self.media_type = media_type  # type: str
        self.ocrcontents = ocrcontents  # type: list[OCRContents]
        self.ocrtexts = ocrtexts  # type: str
        self.osscrc64 = osscrc64  # type: str
        self.ossdelete_marker = ossdelete_marker  # type: str
        self.ossexpiration = ossexpiration  # type: str
        self.ossobject_type = ossobject_type  # type: str
        self.ossstorage_class = ossstorage_class  # type: str
        self.osstagging = osstagging  # type: dict[str, any]
        self.osstagging_count = osstagging_count  # type: long
        self.ossuri = ossuri  # type: str
        self.ossuser_meta = ossuser_meta  # type: dict[str, any]
        self.ossversion_id = ossversion_id  # type: str
        self.object_acl = object_acl  # type: str
        self.object_id = object_id  # type: str
        self.object_type = object_type  # type: str
        self.orientation = orientation  # type: long
        self.owner_id = owner_id  # type: str
        self.page_count = page_count  # type: long
        self.performer = performer  # type: str
        self.produce_time = produce_time  # type: str
        self.program_count = program_count  # type: long
        self.project_name = project_name  # type: str
        self.semantic_types = semantic_types  # type: list[str]
        self.server_side_data_encryption = server_side_data_encryption  # type: str
        self.server_side_encryption = server_side_encryption  # type: str
        self.server_side_encryption_customer_algorithm = server_side_encryption_customer_algorithm  # type: str
        self.server_side_encryption_key_id = server_side_encryption_key_id  # type: str
        self.size = size  # type: long
        self.start_time = start_time  # type: float
        self.stream_count = stream_count  # type: long
        self.subtitles = subtitles  # type: list[SubtitleStream]
        self.timezone = timezone  # type: str
        self.title = title  # type: str
        self.travel_cluster_id = travel_cluster_id  # type: str
        self.uri = uri  # type: str
        self.update_time = update_time  # type: str
        self.video_height = video_height  # type: long
        self.video_streams = video_streams  # type: list[VideoStream]
        self.video_width = video_width  # type: long

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()
        if self.audio_covers:
            for k in self.audio_covers:
                if k:
                    k.validate()
        if self.audio_streams:
            for k in self.audio_streams:
                if k:
                    k.validate()
        if self.cropping_suggestions:
            for k in self.cropping_suggestions:
                if k:
                    k.validate()
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()
        if self.figures:
            for k in self.figures:
                if k:
                    k.validate()
        if self.image_score:
            self.image_score.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.ocrcontents:
            for k in self.ocrcontents:
                if k:
                    k.validate()
        if self.subtitles:
            for k in self.subtitles:
                if k:
                    k.validate()
        if self.video_streams:
            for k in self.video_streams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(File, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_allow_origin is not None:
            result['AccessControlAllowOrigin'] = self.access_control_allow_origin
        if self.access_control_request_method is not None:
            result['AccessControlRequestMethod'] = self.access_control_request_method
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.album is not None:
            result['Album'] = self.album
        if self.album_artist is not None:
            result['AlbumArtist'] = self.album_artist
        if self.artist is not None:
            result['Artist'] = self.artist
        result['AudioCovers'] = []
        if self.audio_covers is not None:
            for k in self.audio_covers:
                result['AudioCovers'].append(k.to_map() if k else None)
        result['AudioStreams'] = []
        if self.audio_streams is not None:
            for k in self.audio_streams:
                result['AudioStreams'].append(k.to_map() if k else None)
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.cache_control is not None:
            result['CacheControl'] = self.cache_control
        if self.composer is not None:
            result['Composer'] = self.composer
        if self.content_disposition is not None:
            result['ContentDisposition'] = self.content_disposition
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.content_language is not None:
            result['ContentLanguage'] = self.content_language
        if self.content_md_5 is not None:
            result['ContentMd5'] = self.content_md_5
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['CroppingSuggestions'] = []
        if self.cropping_suggestions is not None:
            for k in self.cropping_suggestions:
                result['CroppingSuggestions'].append(k.to_map() if k else None)
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.exif is not None:
            result['EXIF'] = self.exif
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        if self.figure_count is not None:
            result['FigureCount'] = self.figure_count
        result['Figures'] = []
        if self.figures is not None:
            for k in self.figures:
                result['Figures'].append(k.to_map() if k else None)
        if self.file_access_time is not None:
            result['FileAccessTime'] = self.file_access_time
        if self.file_create_time is not None:
            result['FileCreateTime'] = self.file_create_time
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.file_modified_time is not None:
            result['FileModifiedTime'] = self.file_modified_time
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.format_long_name is not None:
            result['FormatLongName'] = self.format_long_name
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.image_score is not None:
            result['ImageScore'] = self.image_score.to_map()
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.language is not None:
            result['Language'] = self.language
        if self.lat_long is not None:
            result['LatLong'] = self.lat_long
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        result['OCRContents'] = []
        if self.ocrcontents is not None:
            for k in self.ocrcontents:
                result['OCRContents'].append(k.to_map() if k else None)
        if self.ocrtexts is not None:
            result['OCRTexts'] = self.ocrtexts
        if self.osscrc64 is not None:
            result['OSSCRC64'] = self.osscrc64
        if self.ossdelete_marker is not None:
            result['OSSDeleteMarker'] = self.ossdelete_marker
        if self.ossexpiration is not None:
            result['OSSExpiration'] = self.ossexpiration
        if self.ossobject_type is not None:
            result['OSSObjectType'] = self.ossobject_type
        if self.ossstorage_class is not None:
            result['OSSStorageClass'] = self.ossstorage_class
        if self.osstagging is not None:
            result['OSSTagging'] = self.osstagging
        if self.osstagging_count is not None:
            result['OSSTaggingCount'] = self.osstagging_count
        if self.ossuri is not None:
            result['OSSURI'] = self.ossuri
        if self.ossuser_meta is not None:
            result['OSSUserMeta'] = self.ossuser_meta
        if self.ossversion_id is not None:
            result['OSSVersionId'] = self.ossversion_id
        if self.object_acl is not None:
            result['ObjectACL'] = self.object_acl
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.performer is not None:
            result['Performer'] = self.performer
        if self.produce_time is not None:
            result['ProduceTime'] = self.produce_time
        if self.program_count is not None:
            result['ProgramCount'] = self.program_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.semantic_types is not None:
            result['SemanticTypes'] = self.semantic_types
        if self.server_side_data_encryption is not None:
            result['ServerSideDataEncryption'] = self.server_side_data_encryption
        if self.server_side_encryption is not None:
            result['ServerSideEncryption'] = self.server_side_encryption
        if self.server_side_encryption_customer_algorithm is not None:
            result['ServerSideEncryptionCustomerAlgorithm'] = self.server_side_encryption_customer_algorithm
        if self.server_side_encryption_key_id is not None:
            result['ServerSideEncryptionKeyId'] = self.server_side_encryption_key_id
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_count is not None:
            result['StreamCount'] = self.stream_count
        result['Subtitles'] = []
        if self.subtitles is not None:
            for k in self.subtitles:
                result['Subtitles'].append(k.to_map() if k else None)
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.title is not None:
            result['Title'] = self.title
        if self.travel_cluster_id is not None:
            result['TravelClusterId'] = self.travel_cluster_id
        if self.uri is not None:
            result['URI'] = self.uri
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.video_height is not None:
            result['VideoHeight'] = self.video_height
        result['VideoStreams'] = []
        if self.video_streams is not None:
            for k in self.video_streams:
                result['VideoStreams'].append(k.to_map() if k else None)
        if self.video_width is not None:
            result['VideoWidth'] = self.video_width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessControlAllowOrigin') is not None:
            self.access_control_allow_origin = m.get('AccessControlAllowOrigin')
        if m.get('AccessControlRequestMethod') is not None:
            self.access_control_request_method = m.get('AccessControlRequestMethod')
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = Address()
                self.addresses.append(temp_model.from_map(k))
        if m.get('Album') is not None:
            self.album = m.get('Album')
        if m.get('AlbumArtist') is not None:
            self.album_artist = m.get('AlbumArtist')
        if m.get('Artist') is not None:
            self.artist = m.get('Artist')
        self.audio_covers = []
        if m.get('AudioCovers') is not None:
            for k in m.get('AudioCovers'):
                temp_model = Image()
                self.audio_covers.append(temp_model.from_map(k))
        self.audio_streams = []
        if m.get('AudioStreams') is not None:
            for k in m.get('AudioStreams'):
                temp_model = AudioStream()
                self.audio_streams.append(temp_model.from_map(k))
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CacheControl') is not None:
            self.cache_control = m.get('CacheControl')
        if m.get('Composer') is not None:
            self.composer = m.get('Composer')
        if m.get('ContentDisposition') is not None:
            self.content_disposition = m.get('ContentDisposition')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('ContentLanguage') is not None:
            self.content_language = m.get('ContentLanguage')
        if m.get('ContentMd5') is not None:
            self.content_md_5 = m.get('ContentMd5')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.cropping_suggestions = []
        if m.get('CroppingSuggestions') is not None:
            for k in m.get('CroppingSuggestions'):
                temp_model = CroppingSuggestion()
                self.cropping_suggestions.append(temp_model.from_map(k))
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('EXIF') is not None:
            self.exif = m.get('EXIF')
        self.elements = []
        if m.get('Elements') is not None:
            for k in m.get('Elements'):
                temp_model = Element()
                self.elements.append(temp_model.from_map(k))
        if m.get('FigureCount') is not None:
            self.figure_count = m.get('FigureCount')
        self.figures = []
        if m.get('Figures') is not None:
            for k in m.get('Figures'):
                temp_model = Figure()
                self.figures.append(temp_model.from_map(k))
        if m.get('FileAccessTime') is not None:
            self.file_access_time = m.get('FileAccessTime')
        if m.get('FileCreateTime') is not None:
            self.file_create_time = m.get('FileCreateTime')
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        if m.get('FileModifiedTime') is not None:
            self.file_modified_time = m.get('FileModifiedTime')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('FormatLongName') is not None:
            self.format_long_name = m.get('FormatLongName')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ImageScore') is not None:
            temp_model = ImageScore()
            self.image_score = temp_model.from_map(m['ImageScore'])
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LatLong') is not None:
            self.lat_long = m.get('LatLong')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        self.ocrcontents = []
        if m.get('OCRContents') is not None:
            for k in m.get('OCRContents'):
                temp_model = OCRContents()
                self.ocrcontents.append(temp_model.from_map(k))
        if m.get('OCRTexts') is not None:
            self.ocrtexts = m.get('OCRTexts')
        if m.get('OSSCRC64') is not None:
            self.osscrc64 = m.get('OSSCRC64')
        if m.get('OSSDeleteMarker') is not None:
            self.ossdelete_marker = m.get('OSSDeleteMarker')
        if m.get('OSSExpiration') is not None:
            self.ossexpiration = m.get('OSSExpiration')
        if m.get('OSSObjectType') is not None:
            self.ossobject_type = m.get('OSSObjectType')
        if m.get('OSSStorageClass') is not None:
            self.ossstorage_class = m.get('OSSStorageClass')
        if m.get('OSSTagging') is not None:
            self.osstagging = m.get('OSSTagging')
        if m.get('OSSTaggingCount') is not None:
            self.osstagging_count = m.get('OSSTaggingCount')
        if m.get('OSSURI') is not None:
            self.ossuri = m.get('OSSURI')
        if m.get('OSSUserMeta') is not None:
            self.ossuser_meta = m.get('OSSUserMeta')
        if m.get('OSSVersionId') is not None:
            self.ossversion_id = m.get('OSSVersionId')
        if m.get('ObjectACL') is not None:
            self.object_acl = m.get('ObjectACL')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('Performer') is not None:
            self.performer = m.get('Performer')
        if m.get('ProduceTime') is not None:
            self.produce_time = m.get('ProduceTime')
        if m.get('ProgramCount') is not None:
            self.program_count = m.get('ProgramCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SemanticTypes') is not None:
            self.semantic_types = m.get('SemanticTypes')
        if m.get('ServerSideDataEncryption') is not None:
            self.server_side_data_encryption = m.get('ServerSideDataEncryption')
        if m.get('ServerSideEncryption') is not None:
            self.server_side_encryption = m.get('ServerSideEncryption')
        if m.get('ServerSideEncryptionCustomerAlgorithm') is not None:
            self.server_side_encryption_customer_algorithm = m.get('ServerSideEncryptionCustomerAlgorithm')
        if m.get('ServerSideEncryptionKeyId') is not None:
            self.server_side_encryption_key_id = m.get('ServerSideEncryptionKeyId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamCount') is not None:
            self.stream_count = m.get('StreamCount')
        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k in m.get('Subtitles'):
                temp_model = SubtitleStream()
                self.subtitles.append(temp_model.from_map(k))
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TravelClusterId') is not None:
            self.travel_cluster_id = m.get('TravelClusterId')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VideoHeight') is not None:
            self.video_height = m.get('VideoHeight')
        self.video_streams = []
        if m.get('VideoStreams') is not None:
            for k in m.get('VideoStreams'):
                temp_model = VideoStream()
                self.video_streams.append(temp_model.from_map(k))
        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')
        return self


class HeadPose(TeaModel):
    def __init__(self, pitch=None, roll=None, yaw=None):
        self.pitch = pitch  # type: float
        self.roll = roll  # type: float
        self.yaw = yaw  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(HeadPose, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class Hyperparameters(TeaModel):
    def __init__(self, backup_interval=None, batch_size=None, data_loader_workers=None, evaluator=None,
                 input_size=None, max_epoch=None, optimization=None, schedule=None):
        self.backup_interval = backup_interval  # type: long
        self.batch_size = batch_size  # type: long
        self.data_loader_workers = data_loader_workers  # type: long
        self.evaluator = evaluator  # type: CustomParams
        self.input_size = input_size  # type: list[long]
        self.max_epoch = max_epoch  # type: long
        self.optimization = optimization  # type: Optimization
        self.schedule = schedule  # type: Schedule

    def validate(self):
        if self.evaluator:
            self.evaluator.validate()
        if self.optimization:
            self.optimization.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        _map = super(Hyperparameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_interval is not None:
            result['BackupInterval'] = self.backup_interval
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.data_loader_workers is not None:
            result['DataLoaderWorkers'] = self.data_loader_workers
        if self.evaluator is not None:
            result['Evaluator'] = self.evaluator.to_map()
        if self.input_size is not None:
            result['InputSize'] = self.input_size
        if self.max_epoch is not None:
            result['MaxEpoch'] = self.max_epoch
        if self.optimization is not None:
            result['Optimization'] = self.optimization.to_map()
        if self.schedule is not None:
            result['Schedule'] = self.schedule.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupInterval') is not None:
            self.backup_interval = m.get('BackupInterval')
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('DataLoaderWorkers') is not None:
            self.data_loader_workers = m.get('DataLoaderWorkers')
        if m.get('Evaluator') is not None:
            temp_model = CustomParams()
            self.evaluator = temp_model.from_map(m['Evaluator'])
        if m.get('InputSize') is not None:
            self.input_size = m.get('InputSize')
        if m.get('MaxEpoch') is not None:
            self.max_epoch = m.get('MaxEpoch')
        if m.get('Optimization') is not None:
            temp_model = Optimization()
            self.optimization = temp_model.from_map(m['Optimization'])
        if m.get('Schedule') is not None:
            temp_model = Schedule()
            self.schedule = temp_model.from_map(m['Schedule'])
        return self


class Image(TeaModel):
    def __init__(self, cropping_suggestions=None, exif=None, image_height=None, image_score=None, image_width=None,
                 ocrcontents=None):
        self.cropping_suggestions = cropping_suggestions  # type: list[CroppingSuggestion]
        self.exif = exif  # type: str
        self.image_height = image_height  # type: long
        self.image_score = image_score  # type: ImageScore
        self.image_width = image_width  # type: long
        self.ocrcontents = ocrcontents  # type: list[OCRContents]

    def validate(self):
        if self.cropping_suggestions:
            for k in self.cropping_suggestions:
                if k:
                    k.validate()
        if self.image_score:
            self.image_score.validate()
        if self.ocrcontents:
            for k in self.ocrcontents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Image, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CroppingSuggestions'] = []
        if self.cropping_suggestions is not None:
            for k in self.cropping_suggestions:
                result['CroppingSuggestions'].append(k.to_map() if k else None)
        if self.exif is not None:
            result['EXIF'] = self.exif
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.image_score is not None:
            result['ImageScore'] = self.image_score.to_map()
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        result['OCRContents'] = []
        if self.ocrcontents is not None:
            for k in self.ocrcontents:
                result['OCRContents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cropping_suggestions = []
        if m.get('CroppingSuggestions') is not None:
            for k in m.get('CroppingSuggestions'):
                temp_model = CroppingSuggestion()
                self.cropping_suggestions.append(temp_model.from_map(k))
        if m.get('EXIF') is not None:
            self.exif = m.get('EXIF')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ImageScore') is not None:
            temp_model = ImageScore()
            self.image_score = temp_model.from_map(m['ImageScore'])
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        self.ocrcontents = []
        if m.get('OCRContents') is not None:
            for k in m.get('OCRContents'):
                temp_model = OCRContents()
                self.ocrcontents.append(temp_model.from_map(k))
        return self


class ImageScore(TeaModel):
    def __init__(self, overall_quality_score=None):
        self.overall_quality_score = overall_quality_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageScore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_quality_score is not None:
            result['OverallQualityScore'] = self.overall_quality_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OverallQualityScore') is not None:
            self.overall_quality_score = m.get('OverallQualityScore')
        return self


class Input(TeaModel):
    def __init__(self, oss=None):
        self.oss = oss  # type: InputOSS

    def validate(self):
        if self.oss:
            self.oss.validate()

    def to_map(self):
        _map = super(Input, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss is not None:
            result['OSS'] = self.oss.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OSS') is not None:
            temp_model = InputOSS()
            self.oss = temp_model.from_map(m['OSS'])
        return self


class InputFileFigures(TeaModel):
    def __init__(self, figure_cluster_id=None, figure_id=None, figure_type=None):
        self.figure_cluster_id = figure_cluster_id  # type: str
        self.figure_id = figure_id  # type: str
        self.figure_type = figure_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InputFileFigures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_cluster_id is not None:
            result['FigureClusterId'] = self.figure_cluster_id
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        if self.figure_type is not None:
            result['FigureType'] = self.figure_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FigureClusterId') is not None:
            self.figure_cluster_id = m.get('FigureClusterId')
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        if m.get('FigureType') is not None:
            self.figure_type = m.get('FigureType')
        return self


class InputFile(TeaModel):
    def __init__(self, content_type=None, custom_id=None, custom_labels=None, figures=None, file_hash=None,
                 lat_long=None, media_type=None, ossuri=None, produce_time=None, uri=None):
        self.content_type = content_type  # type: str
        self.custom_id = custom_id  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]
        self.figures = figures  # type: list[InputFileFigures]
        self.file_hash = file_hash  # type: str
        self.lat_long = lat_long  # type: str
        self.media_type = media_type  # type: str
        self.ossuri = ossuri  # type: str
        self.produce_time = produce_time  # type: str
        self.uri = uri  # type: str

    def validate(self):
        if self.figures:
            for k in self.figures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InputFile, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        result['Figures'] = []
        if self.figures is not None:
            for k in self.figures:
                result['Figures'].append(k.to_map() if k else None)
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.lat_long is not None:
            result['LatLong'] = self.lat_long
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.ossuri is not None:
            result['OSSURI'] = self.ossuri
        if self.produce_time is not None:
            result['ProduceTime'] = self.produce_time
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        self.figures = []
        if m.get('Figures') is not None:
            for k in m.get('Figures'):
                temp_model = InputFileFigures()
                self.figures.append(temp_model.from_map(k))
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        if m.get('LatLong') is not None:
            self.lat_long = m.get('LatLong')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('OSSURI') is not None:
            self.ossuri = m.get('OSSURI')
        if m.get('ProduceTime') is not None:
            self.produce_time = m.get('ProduceTime')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class InputOSS(TeaModel):
    def __init__(self, bucket=None, match_expressions=None, prefix=None):
        self.bucket = bucket  # type: str
        self.match_expressions = match_expressions  # type: list[str]
        self.prefix = prefix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InputOSS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.match_expressions is not None:
            result['MatchExpressions'] = self.match_expressions
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('MatchExpressions') is not None:
            self.match_expressions = m.get('MatchExpressions')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class KdtreeOption(TeaModel):
    def __init__(self, compression_level=None, library_name=None, quantization_bits=None):
        self.compression_level = compression_level  # type: int
        self.library_name = library_name  # type: str
        self.quantization_bits = quantization_bits  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(KdtreeOption, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compression_level is not None:
            result['CompressionLevel'] = self.compression_level
        if self.library_name is not None:
            result['LibraryName'] = self.library_name
        if self.quantization_bits is not None:
            result['QuantizationBits'] = self.quantization_bits
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompressionLevel') is not None:
            self.compression_level = m.get('CompressionLevel')
        if m.get('LibraryName') is not None:
            self.library_name = m.get('LibraryName')
        if m.get('QuantizationBits') is not None:
            self.quantization_bits = m.get('QuantizationBits')
        return self


class KeyValuePair(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KeyValuePair, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class Label(TeaModel):
    def __init__(self, centric_score=None, label_confidence=None, label_level=None, label_name=None, language=None,
                 parent_label_name=None):
        self.centric_score = centric_score  # type: float
        self.label_confidence = label_confidence  # type: float
        self.label_level = label_level  # type: long
        self.label_name = label_name  # type: str
        self.language = language  # type: str
        self.parent_label_name = parent_label_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Label, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.centric_score is not None:
            result['CentricScore'] = self.centric_score
        if self.label_confidence is not None:
            result['LabelConfidence'] = self.label_confidence
        if self.label_level is not None:
            result['LabelLevel'] = self.label_level
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.language is not None:
            result['Language'] = self.language
        if self.parent_label_name is not None:
            result['ParentLabelName'] = self.parent_label_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CentricScore') is not None:
            self.centric_score = m.get('CentricScore')
        if m.get('LabelConfidence') is not None:
            self.label_confidence = m.get('LabelConfidence')
        if m.get('LabelLevel') is not None:
            self.label_level = m.get('LabelLevel')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ParentLabelName') is not None:
            self.parent_label_name = m.get('ParentLabelName')
        return self


class LicensePlate(TeaModel):
    def __init__(self, boundary=None, confidence=None, content=None):
        self.boundary = boundary  # type: Boundary
        self.confidence = confidence  # type: float
        self.content = content  # type: str

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super(LicensePlate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class LocationDateCluster(TeaModel):
    def __init__(self, addresses=None, create_time=None, custom_id=None, custom_labels=None,
                 location_date_cluster_end_time=None, location_date_cluster_level=None, location_date_cluster_start_time=None, object_id=None,
                 title=None, update_time=None):
        self.addresses = addresses  # type: list[Address]
        self.create_time = create_time  # type: str
        self.custom_id = custom_id  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]
        self.location_date_cluster_end_time = location_date_cluster_end_time  # type: str
        self.location_date_cluster_level = location_date_cluster_level  # type: str
        self.location_date_cluster_start_time = location_date_cluster_start_time  # type: str
        self.object_id = object_id  # type: str
        self.title = title  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(LocationDateCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.location_date_cluster_end_time is not None:
            result['LocationDateClusterEndTime'] = self.location_date_cluster_end_time
        if self.location_date_cluster_level is not None:
            result['LocationDateClusterLevel'] = self.location_date_cluster_level
        if self.location_date_cluster_start_time is not None:
            result['LocationDateClusterStartTime'] = self.location_date_cluster_start_time
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = Address()
                self.addresses.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('LocationDateClusterEndTime') is not None:
            self.location_date_cluster_end_time = m.get('LocationDateClusterEndTime')
        if m.get('LocationDateClusterLevel') is not None:
            self.location_date_cluster_level = m.get('LocationDateClusterLevel')
        if m.get('LocationDateClusterStartTime') is not None:
            self.location_date_cluster_start_time = m.get('LocationDateClusterStartTime')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class MNS(TeaModel):
    def __init__(self, topic_name=None):
        self.topic_name = topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MNS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class MetaData(TeaModel):
    def __init__(self, identifier=None, provider=None, version=None):
        self.identifier = identifier  # type: str
        self.provider = provider  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MetaData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ModelSpecification(TeaModel):
    def __init__(self, meta_data=None, spec=None):
        self.meta_data = meta_data  # type: MetaData
        self.spec = spec  # type: Spec

    def validate(self):
        if self.meta_data:
            self.meta_data.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super(ModelSpecification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_data is not None:
            result['MetaData'] = self.meta_data.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MetaData') is not None:
            temp_model = MetaData()
            self.meta_data = temp_model.from_map(m['MetaData'])
        if m.get('Spec') is not None:
            temp_model = Spec()
            self.spec = temp_model.from_map(m['Spec'])
        return self


class Notification(TeaModel):
    def __init__(self, extended_message_uri=None, mns=None, rocket_mq=None):
        self.extended_message_uri = extended_message_uri  # type: str
        self.mns = mns  # type: MNS
        self.rocket_mq = rocket_mq  # type: RocketMQ

    def validate(self):
        if self.mns:
            self.mns.validate()
        if self.rocket_mq:
            self.rocket_mq.validate()

    def to_map(self):
        _map = super(Notification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extended_message_uri is not None:
            result['ExtendedMessageURI'] = self.extended_message_uri
        if self.mns is not None:
            result['MNS'] = self.mns.to_map()
        if self.rocket_mq is not None:
            result['RocketMQ'] = self.rocket_mq.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtendedMessageURI') is not None:
            self.extended_message_uri = m.get('ExtendedMessageURI')
        if m.get('MNS') is not None:
            temp_model = MNS()
            self.mns = temp_model.from_map(m['MNS'])
        if m.get('RocketMQ') is not None:
            temp_model = RocketMQ()
            self.rocket_mq = temp_model.from_map(m['RocketMQ'])
        return self


class OCRContents(TeaModel):
    def __init__(self, boundary=None, confidence=None, contents=None, language=None):
        self.boundary = boundary  # type: Boundary
        self.confidence = confidence  # type: float
        self.contents = contents  # type: str
        self.language = language  # type: str

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super(OCRContents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.contents is not None:
            result['Contents'] = self.contents
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class OctreeOption(TeaModel):
    def __init__(self, do_voxel_grid_down_down_sampling=None, library_name=None, octree_resolution=None,
                 point_resolution=None):
        self.do_voxel_grid_down_down_sampling = do_voxel_grid_down_down_sampling  # type: bool
        self.library_name = library_name  # type: str
        self.octree_resolution = octree_resolution  # type: float
        self.point_resolution = point_resolution  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(OctreeOption, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.do_voxel_grid_down_down_sampling is not None:
            result['DoVoxelGridDownDownSampling'] = self.do_voxel_grid_down_down_sampling
        if self.library_name is not None:
            result['LibraryName'] = self.library_name
        if self.octree_resolution is not None:
            result['OctreeResolution'] = self.octree_resolution
        if self.point_resolution is not None:
            result['PointResolution'] = self.point_resolution
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DoVoxelGridDownDownSampling') is not None:
            self.do_voxel_grid_down_down_sampling = m.get('DoVoxelGridDownDownSampling')
        if m.get('LibraryName') is not None:
            self.library_name = m.get('LibraryName')
        if m.get('OctreeResolution') is not None:
            self.octree_resolution = m.get('OctreeResolution')
        if m.get('PointResolution') is not None:
            self.point_resolution = m.get('PointResolution')
        return self


class Optimization(TeaModel):
    def __init__(self, learning_rate=None, optimizer=None):
        self.learning_rate = learning_rate  # type: float
        self.optimizer = optimizer  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Optimization, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.learning_rate is not None:
            result['LearningRate'] = self.learning_rate
        if self.optimizer is not None:
            result['Optimizer'] = self.optimizer
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LearningRate') is not None:
            self.learning_rate = m.get('LearningRate')
        if m.get('Optimizer') is not None:
            self.optimizer = m.get('Optimizer')
        return self


class PointInt64(TeaModel):
    def __init__(self, x=None, y=None):
        self.x = x  # type: long
        self.y = y  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PointInt64, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class PresetReference(TeaModel):
    def __init__(self, name=None, type=None):
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PresetReference, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class Project(TeaModel):
    def __init__(self, create_time=None, dataset_count=None, dataset_max_bind_count=None,
                 dataset_max_entity_count=None, dataset_max_file_count=None, dataset_max_relation_count=None,
                 dataset_max_total_file_size=None, description=None, engine_concurrency=None, file_count=None, project_max_dataset_count=None,
                 project_name=None, project_queries_per_second=None, service_role=None, template_id=None, total_file_size=None,
                 update_time=None):
        self.create_time = create_time  # type: str
        self.dataset_count = dataset_count  # type: long
        self.dataset_max_bind_count = dataset_max_bind_count  # type: long
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        self.dataset_max_total_file_size = dataset_max_total_file_size  # type: long
        self.description = description  # type: str
        self.engine_concurrency = engine_concurrency  # type: long
        self.file_count = file_count  # type: long
        self.project_max_dataset_count = project_max_dataset_count  # type: long
        self.project_name = project_name  # type: str
        self.project_queries_per_second = project_queries_per_second  # type: long
        self.service_role = service_role  # type: str
        self.template_id = template_id  # type: str
        self.total_file_size = total_file_size  # type: long
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Project, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dataset_count is not None:
            result['DatasetCount'] = self.dataset_count
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.description is not None:
            result['Description'] = self.description
        if self.engine_concurrency is not None:
            result['EngineConcurrency'] = self.engine_concurrency
        if self.file_count is not None:
            result['FileCount'] = self.file_count
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_queries_per_second is not None:
            result['ProjectQueriesPerSecond'] = self.project_queries_per_second
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.total_file_size is not None:
            result['TotalFileSize'] = self.total_file_size
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatasetCount') is not None:
            self.dataset_count = m.get('DatasetCount')
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EngineConcurrency') is not None:
            self.engine_concurrency = m.get('EngineConcurrency')
        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQueriesPerSecond') is not None:
            self.project_queries_per_second = m.get('ProjectQueriesPerSecond')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TotalFileSize') is not None:
            self.total_file_size = m.get('TotalFileSize')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class Property(TeaModel):
    def __init__(self, items_type=None, name=None, value=None, value_type=None):
        self.items_type = items_type  # type: str
        self.name = name  # type: str
        self.value = value  # type: str
        self.value_type = value_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Property, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items_type is not None:
            result['ItemsType'] = self.items_type
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemsType') is not None:
            self.items_type = m.get('ItemsType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class RegionType(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegionType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class Resource(TeaModel):
    def __init__(self, cpu=None, ecsinstance=None, gpumodel=None, gpunum=None, name=None, ram=None):
        self.cpu = cpu  # type: long
        self.ecsinstance = ecsinstance  # type: str
        self.gpumodel = gpumodel  # type: str
        self.gpunum = gpunum  # type: long
        self.name = name  # type: str
        self.ram = ram  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(Resource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['CPU'] = self.cpu
        if self.ecsinstance is not None:
            result['ECSInstance'] = self.ecsinstance
        if self.gpumodel is not None:
            result['GPUModel'] = self.gpumodel
        if self.gpunum is not None:
            result['GPUNum'] = self.gpunum
        if self.name is not None:
            result['Name'] = self.name
        if self.ram is not None:
            result['RAM'] = self.ram
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')
        if m.get('ECSInstance') is not None:
            self.ecsinstance = m.get('ECSInstance')
        if m.get('GPUModel') is not None:
            self.gpumodel = m.get('GPUModel')
        if m.get('GPUNum') is not None:
            self.gpunum = m.get('GPUNum')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RAM') is not None:
            self.ram = m.get('RAM')
        return self


class RocketMQ(TeaModel):
    def __init__(self, instance_id=None, topic_name=None):
        self.instance_id = instance_id  # type: str
        self.topic_name = topic_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RocketMQ, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class Row(TeaModel):
    def __init__(self, custom_labels=None, uri=None):
        self.custom_labels = custom_labels  # type: list[KeyValuePair]
        self.uri = uri  # type: str

    def validate(self):
        if self.custom_labels:
            for k in self.custom_labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Row, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomLabels'] = []
        if self.custom_labels is not None:
            for k in self.custom_labels:
                result['CustomLabels'].append(k.to_map() if k else None)
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_labels = []
        if m.get('CustomLabels') is not None:
            for k in m.get('CustomLabels'):
                temp_model = KeyValuePair()
                self.custom_labels.append(temp_model.from_map(k))
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class Runtime(TeaModel):
    def __init__(self, hyperparameters=None, resource=None):
        self.hyperparameters = hyperparameters  # type: Hyperparameters
        self.resource = resource  # type: Resource

    def validate(self):
        if self.hyperparameters:
            self.hyperparameters.validate()
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super(Runtime, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hyperparameters is not None:
            result['Hyperparameters'] = self.hyperparameters.to_map()
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hyperparameters') is not None:
            temp_model = Hyperparameters()
            self.hyperparameters = temp_model.from_map(m['Hyperparameters'])
        if m.get('Resource') is not None:
            temp_model = Resource()
            self.resource = temp_model.from_map(m['Resource'])
        return self


class Schedule(TeaModel):
    def __init__(self, gamma=None, lrscheduler=None, step_size=None):
        self.gamma = gamma  # type: float
        self.lrscheduler = lrscheduler  # type: str
        self.step_size = step_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(Schedule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gamma is not None:
            result['Gamma'] = self.gamma
        if self.lrscheduler is not None:
            result['LRScheduler'] = self.lrscheduler
        if self.step_size is not None:
            result['StepSize'] = self.step_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Gamma') is not None:
            self.gamma = m.get('Gamma')
        if m.get('LRScheduler') is not None:
            self.lrscheduler = m.get('LRScheduler')
        if m.get('StepSize') is not None:
            self.step_size = m.get('StepSize')
        return self


class SimilarImage(TeaModel):
    def __init__(self, image_score=None, uri=None):
        self.image_score = image_score  # type: float
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SimilarImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_score is not None:
            result['ImageScore'] = self.image_score
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageScore') is not None:
            self.image_score = m.get('ImageScore')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class SimilarImageCluster(TeaModel):
    def __init__(self, create_time=None, custom_labels=None, files=None, object_id=None, update_time=None):
        self.create_time = create_time  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]
        self.files = files  # type: list[SimilarImage]
        self.object_id = object_id  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SimilarImageCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = SimilarImage()
                self.files.append(temp_model.from_map(k))
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class SimpleQuery(TeaModel):
    def __init__(self, field=None, operation=None, sub_queries=None, value=None):
        self.field = field  # type: str
        self.operation = operation  # type: str
        self.sub_queries = sub_queries  # type: list[SimpleQuery]
        self.value = value  # type: str

    def validate(self):
        if self.sub_queries:
            for k in self.sub_queries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SimpleQuery, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.operation is not None:
            result['Operation'] = self.operation
        result['SubQueries'] = []
        if self.sub_queries is not None:
            for k in self.sub_queries:
                result['SubQueries'].append(k.to_map() if k else None)
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        self.sub_queries = []
        if m.get('SubQueries') is not None:
            for k in m.get('SubQueries'):
                temp_model = SimpleQuery()
                self.sub_queries.append(temp_model.from_map(k))
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class Spec(TeaModel):
    def __init__(self, backbone=None, class_num=None, head=None, input_channel=None, loss=None, name=None, neck=None,
                 num_landmarks=None, pretrained_path=None):
        self.backbone = backbone  # type: CustomParams
        self.class_num = class_num  # type: long
        self.head = head  # type: CustomParams
        self.input_channel = input_channel  # type: long
        self.loss = loss  # type: CustomParams
        self.name = name  # type: str
        self.neck = neck  # type: CustomParams
        self.num_landmarks = num_landmarks  # type: long
        self.pretrained_path = pretrained_path  # type: str

    def validate(self):
        if self.backbone:
            self.backbone.validate()
        if self.head:
            self.head.validate()
        if self.loss:
            self.loss.validate()
        if self.neck:
            self.neck.validate()

    def to_map(self):
        _map = super(Spec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backbone is not None:
            result['Backbone'] = self.backbone.to_map()
        if self.class_num is not None:
            result['ClassNum'] = self.class_num
        if self.head is not None:
            result['Head'] = self.head.to_map()
        if self.input_channel is not None:
            result['InputChannel'] = self.input_channel
        if self.loss is not None:
            result['Loss'] = self.loss.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.neck is not None:
            result['Neck'] = self.neck.to_map()
        if self.num_landmarks is not None:
            result['NumLandmarks'] = self.num_landmarks
        if self.pretrained_path is not None:
            result['PretrainedPath'] = self.pretrained_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Backbone') is not None:
            temp_model = CustomParams()
            self.backbone = temp_model.from_map(m['Backbone'])
        if m.get('ClassNum') is not None:
            self.class_num = m.get('ClassNum')
        if m.get('Head') is not None:
            temp_model = CustomParams()
            self.head = temp_model.from_map(m['Head'])
        if m.get('InputChannel') is not None:
            self.input_channel = m.get('InputChannel')
        if m.get('Loss') is not None:
            temp_model = CustomParams()
            self.loss = temp_model.from_map(m['Loss'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Neck') is not None:
            temp_model = CustomParams()
            self.neck = temp_model.from_map(m['Neck'])
        if m.get('NumLandmarks') is not None:
            self.num_landmarks = m.get('NumLandmarks')
        if m.get('PretrainedPath') is not None:
            self.pretrained_path = m.get('PretrainedPath')
        return self


class Story(TeaModel):
    def __init__(self, addresses=None, cover=None, create_time=None, custom_id=None, custom_labels=None,
                 dataset_name=None, figure_cluster_ids=None, files=None, object_id=None, object_type=None, owner_id=None,
                 project_name=None, story_end_time=None, story_name=None, story_start_time=None, story_sub_type=None,
                 story_type=None, update_time=None):
        self.addresses = addresses  # type: list[Address]
        self.cover = cover  # type: File
        self.create_time = create_time  # type: str
        self.custom_id = custom_id  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]
        self.dataset_name = dataset_name  # type: str
        self.figure_cluster_ids = figure_cluster_ids  # type: list[str]
        self.files = files  # type: list[File]
        self.object_id = object_id  # type: str
        self.object_type = object_type  # type: str
        self.owner_id = owner_id  # type: str
        self.project_name = project_name  # type: str
        self.story_end_time = story_end_time  # type: str
        self.story_name = story_name  # type: str
        self.story_start_time = story_start_time  # type: str
        self.story_sub_type = story_sub_type  # type: str
        self.story_type = story_type  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(Story, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster_ids is not None:
            result['FigureClusterIds'] = self.figure_cluster_ids
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_end_time is not None:
            result['StoryEndTime'] = self.story_end_time
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time is not None:
            result['StoryStartTime'] = self.story_start_time
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = Address()
                self.addresses.append(temp_model.from_map(k))
        if m.get('Cover') is not None:
            temp_model = File()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureClusterIds') is not None:
            self.figure_cluster_ids = m.get('FigureClusterIds')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryEndTime') is not None:
            self.story_end_time = m.get('StoryEndTime')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTime') is not None:
            self.story_start_time = m.get('StoryStartTime')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class SubtitleStream(TeaModel):
    def __init__(self, bitrate=None, codec_long_name=None, codec_name=None, codec_tag=None, codec_tag_string=None,
                 content=None, duration=None, height=None, index=None, language=None, start_time=None, width=None):
        self.bitrate = bitrate  # type: long
        self.codec_long_name = codec_long_name  # type: str
        self.codec_name = codec_name  # type: str
        self.codec_tag = codec_tag  # type: str
        self.codec_tag_string = codec_tag_string  # type: str
        self.content = content  # type: str
        self.duration = duration  # type: float
        self.height = height  # type: long
        self.index = index  # type: long
        self.language = language  # type: str
        self.start_time = start_time  # type: float
        self.width = width  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubtitleStream, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.content is not None:
            result['Content'] = self.content
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.height is not None:
            result['Height'] = self.height
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class TargetAudioFilterAudio(TeaModel):
    def __init__(self, mixing=None):
        self.mixing = mixing  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TargetAudioFilterAudio, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mixing is not None:
            result['Mixing'] = self.mixing
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mixing') is not None:
            self.mixing = m.get('Mixing')
        return self


class TargetAudioTranscodeAudio(TeaModel):
    def __init__(self, bitrate=None, bitrate_option=None, channel=None, codec=None, quality=None, sample_rate=None,
                 sample_rate_option=None):
        self.bitrate = bitrate  # type: int
        self.bitrate_option = bitrate_option  # type: str
        self.channel = channel  # type: int
        self.codec = codec  # type: str
        self.quality = quality  # type: int
        self.sample_rate = sample_rate  # type: int
        self.sample_rate_option = sample_rate_option  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TargetAudioTranscodeAudio, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.bitrate_option is not None:
            result['BitrateOption'] = self.bitrate_option
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.codec is not None:
            result['Codec'] = self.codec
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.sample_rate_option is not None:
            result['SampleRateOption'] = self.sample_rate_option
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('BitrateOption') is not None:
            self.bitrate_option = m.get('BitrateOption')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Codec') is not None:
            self.codec = m.get('Codec')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SampleRateOption') is not None:
            self.sample_rate_option = m.get('SampleRateOption')
        return self


class TargetAudio(TeaModel):
    def __init__(self, disable_audio=None, filter_audio=None, stream=None, transcode_audio=None):
        self.disable_audio = disable_audio  # type: bool
        self.filter_audio = filter_audio  # type: TargetAudioFilterAudio
        self.stream = stream  # type: list[long]
        self.transcode_audio = transcode_audio  # type: TargetAudioTranscodeAudio

    def validate(self):
        if self.filter_audio:
            self.filter_audio.validate()
        if self.transcode_audio:
            self.transcode_audio.validate()

    def to_map(self):
        _map = super(TargetAudio, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_audio is not None:
            result['DisableAudio'] = self.disable_audio
        if self.filter_audio is not None:
            result['FilterAudio'] = self.filter_audio.to_map()
        if self.stream is not None:
            result['Stream'] = self.stream
        if self.transcode_audio is not None:
            result['TranscodeAudio'] = self.transcode_audio.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisableAudio') is not None:
            self.disable_audio = m.get('DisableAudio')
        if m.get('FilterAudio') is not None:
            temp_model = TargetAudioFilterAudio()
            self.filter_audio = temp_model.from_map(m['FilterAudio'])
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        if m.get('TranscodeAudio') is not None:
            temp_model = TargetAudioTranscodeAudio()
            self.transcode_audio = temp_model.from_map(m['TranscodeAudio'])
        return self


class TargetImageAnimations(TeaModel):
    def __init__(self, format=None, frame_rate=None, height=None, interval=None, number=None, scale_type=None,
                 start_time=None, uri=None, width=None):
        self.format = format  # type: str
        self.frame_rate = frame_rate  # type: float
        self.height = height  # type: float
        self.interval = interval  # type: float
        self.number = number  # type: int
        self.scale_type = scale_type  # type: str
        self.start_time = start_time  # type: float
        self.uri = uri  # type: str
        self.width = width  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(TargetImageAnimations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.height is not None:
            result['Height'] = self.height
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.number is not None:
            result['Number'] = self.number
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uri is not None:
            result['URI'] = self.uri
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class TargetImageSnapshots(TeaModel):
    def __init__(self, format=None, height=None, interval=None, number=None, scale_type=None, start_time=None,
                 uri=None, width=None):
        self.format = format  # type: str
        self.height = height  # type: float
        self.interval = interval  # type: float
        self.number = number  # type: int
        self.scale_type = scale_type  # type: str
        self.start_time = start_time  # type: float
        self.uri = uri  # type: str
        self.width = width  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(TargetImageSnapshots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.height is not None:
            result['Height'] = self.height
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.number is not None:
            result['Number'] = self.number
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uri is not None:
            result['URI'] = self.uri
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class TargetImageSprites(TeaModel):
    def __init__(self, format=None, interval=None, margin=None, number=None, pad=None, scale_height=None,
                 scale_type=None, scale_width=None, start_time=None, tile_height=None, tile_width=None, uri=None):
        self.format = format  # type: str
        self.interval = interval  # type: float
        self.margin = margin  # type: int
        self.number = number  # type: int
        self.pad = pad  # type: int
        self.scale_height = scale_height  # type: float
        self.scale_type = scale_type  # type: str
        self.scale_width = scale_width  # type: float
        self.start_time = start_time  # type: float
        self.tile_height = tile_height  # type: int
        self.tile_width = tile_width  # type: int
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TargetImageSprites, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.margin is not None:
            result['Margin'] = self.margin
        if self.number is not None:
            result['Number'] = self.number
        if self.pad is not None:
            result['Pad'] = self.pad
        if self.scale_height is not None:
            result['ScaleHeight'] = self.scale_height
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.scale_width is not None:
            result['ScaleWidth'] = self.scale_width
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tile_height is not None:
            result['TileHeight'] = self.tile_height
        if self.tile_width is not None:
            result['TileWidth'] = self.tile_width
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Margin') is not None:
            self.margin = m.get('Margin')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Pad') is not None:
            self.pad = m.get('Pad')
        if m.get('ScaleHeight') is not None:
            self.scale_height = m.get('ScaleHeight')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('ScaleWidth') is not None:
            self.scale_width = m.get('ScaleWidth')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TileHeight') is not None:
            self.tile_height = m.get('TileHeight')
        if m.get('TileWidth') is not None:
            self.tile_width = m.get('TileWidth')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class TargetImage(TeaModel):
    def __init__(self, animations=None, snapshots=None, sprites=None):
        self.animations = animations  # type: list[TargetImageAnimations]
        self.snapshots = snapshots  # type: list[TargetImageSnapshots]
        self.sprites = sprites  # type: list[TargetImageSprites]

    def validate(self):
        if self.animations:
            for k in self.animations:
                if k:
                    k.validate()
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()
        if self.sprites:
            for k in self.sprites:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TargetImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Animations'] = []
        if self.animations is not None:
            for k in self.animations:
                result['Animations'].append(k.to_map() if k else None)
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        result['Sprites'] = []
        if self.sprites is not None:
            for k in self.sprites:
                result['Sprites'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.animations = []
        if m.get('Animations') is not None:
            for k in m.get('Animations'):
                temp_model = TargetImageAnimations()
                self.animations.append(temp_model.from_map(k))
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = TargetImageSnapshots()
                self.snapshots.append(temp_model.from_map(k))
        self.sprites = []
        if m.get('Sprites') is not None:
            for k in m.get('Sprites'):
                temp_model = TargetImageSprites()
                self.sprites.append(temp_model.from_map(k))
        return self


class TargetSubtitleExtractSubtitle(TeaModel):
    def __init__(self, format=None, uri=None):
        self.format = format  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TargetSubtitleExtractSubtitle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class TargetSubtitle(TeaModel):
    def __init__(self, disable_subtitle=None, extract_subtitle=None, stream=None):
        self.disable_subtitle = disable_subtitle  # type: bool
        self.extract_subtitle = extract_subtitle  # type: TargetSubtitleExtractSubtitle
        self.stream = stream  # type: list[int]

    def validate(self):
        if self.extract_subtitle:
            self.extract_subtitle.validate()

    def to_map(self):
        _map = super(TargetSubtitle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_subtitle is not None:
            result['DisableSubtitle'] = self.disable_subtitle
        if self.extract_subtitle is not None:
            result['ExtractSubtitle'] = self.extract_subtitle.to_map()
        if self.stream is not None:
            result['Stream'] = self.stream
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisableSubtitle') is not None:
            self.disable_subtitle = m.get('DisableSubtitle')
        if m.get('ExtractSubtitle') is not None:
            temp_model = TargetSubtitleExtractSubtitle()
            self.extract_subtitle = temp_model.from_map(m['ExtractSubtitle'])
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        return self


class TargetVideoFilterVideoDelogos(TeaModel):
    def __init__(self, duration=None, dx=None, dy=None, height=None, refer_pos=None, start_time=None, width=None):
        self.duration = duration  # type: float
        self.dx = dx  # type: float
        self.dy = dy  # type: float
        self.height = height  # type: float
        self.refer_pos = refer_pos  # type: str
        self.start_time = start_time  # type: float
        self.width = width  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(TargetVideoFilterVideoDelogos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.dx is not None:
            result['Dx'] = self.dx
        if self.dy is not None:
            result['Dy'] = self.dy
        if self.height is not None:
            result['Height'] = self.height
        if self.refer_pos is not None:
            result['ReferPos'] = self.refer_pos
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Dx') is not None:
            self.dx = m.get('Dx')
        if m.get('Dy') is not None:
            self.dy = m.get('Dy')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class TargetVideoFilterVideoWatermarks(TeaModel):
    def __init__(self, border_color=None, border_width=None, content=None, duration=None, dx=None, dy=None,
                 font_apha=None, font_color=None, font_name=None, font_size=None, height=None, refer_pos=None, start_time=None,
                 type=None, uri=None, width=None):
        self.border_color = border_color  # type: str
        self.border_width = border_width  # type: int
        self.content = content  # type: str
        self.duration = duration  # type: float
        self.dx = dx  # type: float
        self.dy = dy  # type: float
        self.font_apha = font_apha  # type: float
        self.font_color = font_color  # type: str
        self.font_name = font_name  # type: str
        self.font_size = font_size  # type: int
        self.height = height  # type: float
        self.refer_pos = refer_pos  # type: str
        self.start_time = start_time  # type: float
        self.type = type  # type: str
        self.uri = uri  # type: str
        self.width = width  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(TargetVideoFilterVideoWatermarks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.border_color is not None:
            result['BorderColor'] = self.border_color
        if self.border_width is not None:
            result['BorderWidth'] = self.border_width
        if self.content is not None:
            result['Content'] = self.content
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.dx is not None:
            result['Dx'] = self.dx
        if self.dy is not None:
            result['Dy'] = self.dy
        if self.font_apha is not None:
            result['FontApha'] = self.font_apha
        if self.font_color is not None:
            result['FontColor'] = self.font_color
        if self.font_name is not None:
            result['FontName'] = self.font_name
        if self.font_size is not None:
            result['FontSize'] = self.font_size
        if self.height is not None:
            result['Height'] = self.height
        if self.refer_pos is not None:
            result['ReferPos'] = self.refer_pos
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['URI'] = self.uri
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')
        if m.get('BorderWidth') is not None:
            self.border_width = m.get('BorderWidth')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Dx') is not None:
            self.dx = m.get('Dx')
        if m.get('Dy') is not None:
            self.dy = m.get('Dy')
        if m.get('FontApha') is not None:
            self.font_apha = m.get('FontApha')
        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')
        if m.get('FontName') is not None:
            self.font_name = m.get('FontName')
        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class TargetVideoFilterVideo(TeaModel):
    def __init__(self, delogos=None, watermarks=None):
        self.delogos = delogos  # type: list[TargetVideoFilterVideoDelogos]
        self.watermarks = watermarks  # type: list[TargetVideoFilterVideoWatermarks]

    def validate(self):
        if self.delogos:
            for k in self.delogos:
                if k:
                    k.validate()
        if self.watermarks:
            for k in self.watermarks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TargetVideoFilterVideo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Delogos'] = []
        if self.delogos is not None:
            for k in self.delogos:
                result['Delogos'].append(k.to_map() if k else None)
        result['Watermarks'] = []
        if self.watermarks is not None:
            for k in self.watermarks:
                result['Watermarks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.delogos = []
        if m.get('Delogos') is not None:
            for k in m.get('Delogos'):
                temp_model = TargetVideoFilterVideoDelogos()
                self.delogos.append(temp_model.from_map(k))
        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k in m.get('Watermarks'):
                temp_model = TargetVideoFilterVideoWatermarks()
                self.watermarks.append(temp_model.from_map(k))
        return self


class TargetVideoTranscodeVideo(TeaModel):
    def __init__(self, adaptive_resolution_direction=None, bframes=None, bitrate=None, bitrate_option=None,
                 buffer_size=None, crf=None, codec=None, frame_rate=None, frame_rate_option=None, gopsize=None, max_bitrate=None,
                 pixel_format=None, refs=None, resolution=None, resolution_option=None, rotation=None, scale_type=None):
        self.adaptive_resolution_direction = adaptive_resolution_direction  # type: bool
        self.bframes = bframes  # type: int
        self.bitrate = bitrate  # type: int
        self.bitrate_option = bitrate_option  # type: str
        self.buffer_size = buffer_size  # type: int
        self.crf = crf  # type: float
        self.codec = codec  # type: str
        self.frame_rate = frame_rate  # type: float
        self.frame_rate_option = frame_rate_option  # type: str
        self.gopsize = gopsize  # type: int
        self.max_bitrate = max_bitrate  # type: int
        self.pixel_format = pixel_format  # type: str
        self.refs = refs  # type: int
        self.resolution = resolution  # type: str
        self.resolution_option = resolution_option  # type: str
        self.rotation = rotation  # type: int
        self.scale_type = scale_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TargetVideoTranscodeVideo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adaptive_resolution_direction is not None:
            result['AdaptiveResolutionDirection'] = self.adaptive_resolution_direction
        if self.bframes is not None:
            result['BFrames'] = self.bframes
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.bitrate_option is not None:
            result['BitrateOption'] = self.bitrate_option
        if self.buffer_size is not None:
            result['BufferSize'] = self.buffer_size
        if self.crf is not None:
            result['CRF'] = self.crf
        if self.codec is not None:
            result['Codec'] = self.codec
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.frame_rate_option is not None:
            result['FrameRateOption'] = self.frame_rate_option
        if self.gopsize is not None:
            result['GOPSize'] = self.gopsize
        if self.max_bitrate is not None:
            result['MaxBitrate'] = self.max_bitrate
        if self.pixel_format is not None:
            result['PixelFormat'] = self.pixel_format
        if self.refs is not None:
            result['Refs'] = self.refs
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.resolution_option is not None:
            result['ResolutionOption'] = self.resolution_option
        if self.rotation is not None:
            result['Rotation'] = self.rotation
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdaptiveResolutionDirection') is not None:
            self.adaptive_resolution_direction = m.get('AdaptiveResolutionDirection')
        if m.get('BFrames') is not None:
            self.bframes = m.get('BFrames')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('BitrateOption') is not None:
            self.bitrate_option = m.get('BitrateOption')
        if m.get('BufferSize') is not None:
            self.buffer_size = m.get('BufferSize')
        if m.get('CRF') is not None:
            self.crf = m.get('CRF')
        if m.get('Codec') is not None:
            self.codec = m.get('Codec')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('FrameRateOption') is not None:
            self.frame_rate_option = m.get('FrameRateOption')
        if m.get('GOPSize') is not None:
            self.gopsize = m.get('GOPSize')
        if m.get('MaxBitrate') is not None:
            self.max_bitrate = m.get('MaxBitrate')
        if m.get('PixelFormat') is not None:
            self.pixel_format = m.get('PixelFormat')
        if m.get('Refs') is not None:
            self.refs = m.get('Refs')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('ResolutionOption') is not None:
            self.resolution_option = m.get('ResolutionOption')
        if m.get('Rotation') is not None:
            self.rotation = m.get('Rotation')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        return self


class TargetVideo(TeaModel):
    def __init__(self, disable_video=None, filter_video=None, stream=None, transcode_video=None):
        self.disable_video = disable_video  # type: bool
        self.filter_video = filter_video  # type: TargetVideoFilterVideo
        self.stream = stream  # type: list[int]
        self.transcode_video = transcode_video  # type: TargetVideoTranscodeVideo

    def validate(self):
        if self.filter_video:
            self.filter_video.validate()
        if self.transcode_video:
            self.transcode_video.validate()

    def to_map(self):
        _map = super(TargetVideo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_video is not None:
            result['DisableVideo'] = self.disable_video
        if self.filter_video is not None:
            result['FilterVideo'] = self.filter_video.to_map()
        if self.stream is not None:
            result['Stream'] = self.stream
        if self.transcode_video is not None:
            result['TranscodeVideo'] = self.transcode_video.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisableVideo') is not None:
            self.disable_video = m.get('DisableVideo')
        if m.get('FilterVideo') is not None:
            temp_model = TargetVideoFilterVideo()
            self.filter_video = temp_model.from_map(m['FilterVideo'])
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        if m.get('TranscodeVideo') is not None:
            temp_model = TargetVideoTranscodeVideo()
            self.transcode_video = temp_model.from_map(m['TranscodeVideo'])
        return self


class TaskInfo(TeaModel):
    def __init__(self, code=None, end_time=None, message=None, progress=None, start_time=None, status=None, tags=None,
                 task_id=None, task_request_definition=None, task_type=None, user_data=None):
        self.code = code  # type: str
        self.end_time = end_time  # type: str
        self.message = message  # type: str
        self.progress = progress  # type: int
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: dict[str, any]
        self.task_id = task_id  # type: str
        self.task_request_definition = task_request_definition  # type: str
        self.task_type = task_type  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.message is not None:
            result['Message'] = self.message
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_request_definition is not None:
            result['TaskRequestDefinition'] = self.task_request_definition
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskRequestDefinition') is not None:
            self.task_request_definition = m.get('TaskRequestDefinition')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class TimeRange(TeaModel):
    def __init__(self, end=None, start=None):
        self.end = end  # type: str
        self.start = start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TimeRange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class TrainingSpecification(TeaModel):
    def __init__(self, dataset_name=None, endpoint=None, model_specification=None, runtime=None, source_uri=None,
                 target_uri=None, transforms=None, validation_source_uri=None, validation_split=None):
        self.dataset_name = dataset_name  # type: str
        self.endpoint = endpoint  # type: str
        self.model_specification = model_specification  # type: ModelSpecification
        self.runtime = runtime  # type: Runtime
        self.source_uri = source_uri  # type: str
        self.target_uri = target_uri  # type: str
        self.transforms = transforms  # type: list[CustomParams]
        self.validation_source_uri = validation_source_uri  # type: str
        self.validation_split = validation_split  # type: float

    def validate(self):
        if self.model_specification:
            self.model_specification.validate()
        if self.runtime:
            self.runtime.validate()
        if self.transforms:
            for k in self.transforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TrainingSpecification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.model_specification is not None:
            result['ModelSpecification'] = self.model_specification.to_map()
        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        result['Transforms'] = []
        if self.transforms is not None:
            for k in self.transforms:
                result['Transforms'].append(k.to_map() if k else None)
        if self.validation_source_uri is not None:
            result['ValidationSourceURI'] = self.validation_source_uri
        if self.validation_split is not None:
            result['ValidationSplit'] = self.validation_split
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ModelSpecification') is not None:
            temp_model = ModelSpecification()
            self.model_specification = temp_model.from_map(m['ModelSpecification'])
        if m.get('Runtime') is not None:
            temp_model = Runtime()
            self.runtime = temp_model.from_map(m['Runtime'])
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        self.transforms = []
        if m.get('Transforms') is not None:
            for k in m.get('Transforms'):
                temp_model = CustomParams()
                self.transforms.append(temp_model.from_map(k))
        if m.get('ValidationSourceURI') is not None:
            self.validation_source_uri = m.get('ValidationSourceURI')
        if m.get('ValidationSplit') is not None:
            self.validation_split = m.get('ValidationSplit')
        return self


class TrimPolicy(TeaModel):
    def __init__(self, disable_delete_empty_cell=None, disable_delete_repeated_style=None,
                 disable_delete_unused_picture=None, disable_delete_unused_shape=None):
        self.disable_delete_empty_cell = disable_delete_empty_cell  # type: bool
        self.disable_delete_repeated_style = disable_delete_repeated_style  # type: bool
        self.disable_delete_unused_picture = disable_delete_unused_picture  # type: bool
        self.disable_delete_unused_shape = disable_delete_unused_shape  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TrimPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_delete_empty_cell is not None:
            result['DisableDeleteEmptyCell'] = self.disable_delete_empty_cell
        if self.disable_delete_repeated_style is not None:
            result['DisableDeleteRepeatedStyle'] = self.disable_delete_repeated_style
        if self.disable_delete_unused_picture is not None:
            result['DisableDeleteUnusedPicture'] = self.disable_delete_unused_picture
        if self.disable_delete_unused_shape is not None:
            result['DisableDeleteUnusedShape'] = self.disable_delete_unused_shape
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisableDeleteEmptyCell') is not None:
            self.disable_delete_empty_cell = m.get('DisableDeleteEmptyCell')
        if m.get('DisableDeleteRepeatedStyle') is not None:
            self.disable_delete_repeated_style = m.get('DisableDeleteRepeatedStyle')
        if m.get('DisableDeleteUnusedPicture') is not None:
            self.disable_delete_unused_picture = m.get('DisableDeleteUnusedPicture')
        if m.get('DisableDeleteUnusedShape') is not None:
            self.disable_delete_unused_shape = m.get('DisableDeleteUnusedShape')
        return self


class VideoStream(TeaModel):
    def __init__(self, average_frame_rate=None, bit_depth=None, bitrate=None, codec_long_name=None, codec_name=None,
                 codec_tag=None, codec_tag_string=None, codec_time_base=None, color_primaries=None, color_range=None,
                 color_space=None, color_transfer=None, display_aspect_ratio=None, duration=None, frame_count=None,
                 frame_rate=None, has_bframes=None, height=None, index=None, language=None, level=None, pixel_format=None,
                 profile=None, rotate=None, sample_aspect_ratio=None, start_time=None, time_base=None, width=None):
        self.average_frame_rate = average_frame_rate  # type: str
        self.bit_depth = bit_depth  # type: long
        self.bitrate = bitrate  # type: long
        self.codec_long_name = codec_long_name  # type: str
        self.codec_name = codec_name  # type: str
        self.codec_tag = codec_tag  # type: str
        self.codec_tag_string = codec_tag_string  # type: str
        self.codec_time_base = codec_time_base  # type: str
        self.color_primaries = color_primaries  # type: str
        self.color_range = color_range  # type: str
        self.color_space = color_space  # type: str
        self.color_transfer = color_transfer  # type: str
        self.display_aspect_ratio = display_aspect_ratio  # type: str
        self.duration = duration  # type: float
        self.frame_count = frame_count  # type: long
        self.frame_rate = frame_rate  # type: str
        self.has_bframes = has_bframes  # type: long
        self.height = height  # type: long
        self.index = index  # type: long
        self.language = language  # type: str
        self.level = level  # type: long
        self.pixel_format = pixel_format  # type: str
        self.profile = profile  # type: str
        self.rotate = rotate  # type: str
        self.sample_aspect_ratio = sample_aspect_ratio  # type: str
        self.start_time = start_time  # type: float
        self.time_base = time_base  # type: str
        self.width = width  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoStream, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average_frame_rate is not None:
            result['AverageFrameRate'] = self.average_frame_rate
        if self.bit_depth is not None:
            result['BitDepth'] = self.bit_depth
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
        if self.color_primaries is not None:
            result['ColorPrimaries'] = self.color_primaries
        if self.color_range is not None:
            result['ColorRange'] = self.color_range
        if self.color_space is not None:
            result['ColorSpace'] = self.color_space
        if self.color_transfer is not None:
            result['ColorTransfer'] = self.color_transfer
        if self.display_aspect_ratio is not None:
            result['DisplayAspectRatio'] = self.display_aspect_ratio
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.frame_count is not None:
            result['FrameCount'] = self.frame_count
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes
        if self.height is not None:
            result['Height'] = self.height
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        if self.level is not None:
            result['Level'] = self.level
        if self.pixel_format is not None:
            result['PixelFormat'] = self.pixel_format
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.sample_aspect_ratio is not None:
            result['SampleAspectRatio'] = self.sample_aspect_ratio
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_base is not None:
            result['TimeBase'] = self.time_base
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AverageFrameRate') is not None:
            self.average_frame_rate = m.get('AverageFrameRate')
        if m.get('BitDepth') is not None:
            self.bit_depth = m.get('BitDepth')
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
        if m.get('ColorPrimaries') is not None:
            self.color_primaries = m.get('ColorPrimaries')
        if m.get('ColorRange') is not None:
            self.color_range = m.get('ColorRange')
        if m.get('ColorSpace') is not None:
            self.color_space = m.get('ColorSpace')
        if m.get('ColorTransfer') is not None:
            self.color_transfer = m.get('ColorTransfer')
        if m.get('DisplayAspectRatio') is not None:
            self.display_aspect_ratio = m.get('DisplayAspectRatio')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FrameCount') is not None:
            self.frame_count = m.get('FrameCount')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PixelFormat') is not None:
            self.pixel_format = m.get('PixelFormat')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('SampleAspectRatio') is not None:
            self.sample_aspect_ratio = m.get('SampleAspectRatio')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeBase') is not None:
            self.time_base = m.get('TimeBase')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class WebofficePermission(TeaModel):
    def __init__(self, copy=None, export=None, history=None, print_=None, readonly=None, rename=None):
        self.copy = copy  # type: bool
        self.export = export  # type: bool
        self.history = history  # type: bool
        self.print_ = print_  # type: bool
        self.readonly = readonly  # type: bool
        self.rename = rename  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(WebofficePermission, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.copy is not None:
            result['Copy'] = self.copy
        if self.export is not None:
            result['Export'] = self.export
        if self.history is not None:
            result['History'] = self.history
        if self.print_ is not None:
            result['Print'] = self.print_
        if self.readonly is not None:
            result['Readonly'] = self.readonly
        if self.rename is not None:
            result['Rename'] = self.rename
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Copy') is not None:
            self.copy = m.get('Copy')
        if m.get('Export') is not None:
            self.export = m.get('Export')
        if m.get('History') is not None:
            self.history = m.get('History')
        if m.get('Print') is not None:
            self.print_ = m.get('Print')
        if m.get('Readonly') is not None:
            self.readonly = m.get('Readonly')
        if m.get('Rename') is not None:
            self.rename = m.get('Rename')
        return self


class WebofficeUser(TeaModel):
    def __init__(self, avatar=None, id=None, name=None):
        self.avatar = avatar  # type: str
        self.id = id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WebofficeUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class WebofficeWatermark(TeaModel):
    def __init__(self, fill_style=None, font=None, horizontal=None, rotate=None, type=None, value=None, vertical=None):
        self.fill_style = fill_style  # type: str
        self.font = font  # type: str
        self.horizontal = horizontal  # type: long
        self.rotate = rotate  # type: float
        self.type = type  # type: long
        self.value = value  # type: str
        self.vertical = vertical  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(WebofficeWatermark, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fill_style is not None:
            result['FillStyle'] = self.fill_style
        if self.font is not None:
            result['Font'] = self.font
        if self.horizontal is not None:
            result['Horizontal'] = self.horizontal
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.vertical is not None:
            result['Vertical'] = self.vertical
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FillStyle') is not None:
            self.fill_style = m.get('FillStyle')
        if m.get('Font') is not None:
            self.font = m.get('Font')
        if m.get('Horizontal') is not None:
            self.horizontal = m.get('Horizontal')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')
        return self


class AddImageMosaicRequestTargetsBoundary(TeaModel):
    def __init__(self, height=None, refer_pos=None, width=None, x=None, y=None):
        self.height = height  # type: float
        self.refer_pos = refer_pos  # type: str
        self.width = width  # type: float
        self.x = x  # type: float
        self.y = y  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageMosaicRequestTargetsBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.refer_pos is not None:
            result['ReferPos'] = self.refer_pos
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class AddImageMosaicRequestTargets(TeaModel):
    def __init__(self, blur_radius=None, boundary=None, color=None, mosaic_radius=None, sigma=None, type=None):
        self.blur_radius = blur_radius  # type: int
        self.boundary = boundary  # type: AddImageMosaicRequestTargetsBoundary
        self.color = color  # type: str
        self.mosaic_radius = mosaic_radius  # type: int
        self.sigma = sigma  # type: int
        self.type = type  # type: str

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super(AddImageMosaicRequestTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blur_radius is not None:
            result['BlurRadius'] = self.blur_radius
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.color is not None:
            result['Color'] = self.color
        if self.mosaic_radius is not None:
            result['MosaicRadius'] = self.mosaic_radius
        if self.sigma is not None:
            result['Sigma'] = self.sigma
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlurRadius') is not None:
            self.blur_radius = m.get('BlurRadius')
        if m.get('Boundary') is not None:
            temp_model = AddImageMosaicRequestTargetsBoundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('MosaicRadius') is not None:
            self.mosaic_radius = m.get('MosaicRadius')
        if m.get('Sigma') is not None:
            self.sigma = m.get('Sigma')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddImageMosaicRequest(TeaModel):
    def __init__(self, credential_config=None, image_format=None, project_name=None, quality=None, source_uri=None,
                 target_uri=None, targets=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.image_format = image_format  # type: str
        self.project_name = project_name  # type: str
        self.quality = quality  # type: int
        self.source_uri = source_uri  # type: str
        self.target_uri = target_uri  # type: str
        self.targets = targets  # type: list[AddImageMosaicRequestTargets]

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddImageMosaicRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = AddImageMosaicRequestTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class AddImageMosaicShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, image_format=None, project_name=None, quality=None,
                 source_uri=None, target_uri=None, targets_shrink=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.image_format = image_format  # type: str
        self.project_name = project_name  # type: str
        self.quality = quality  # type: int
        self.source_uri = source_uri  # type: str
        self.target_uri = target_uri  # type: str
        self.targets_shrink = targets_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageMosaicShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')
        return self


class AddImageMosaicResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddImageMosaicResponseBody, self).to_map()
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


class AddImageMosaicResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddImageMosaicResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddImageMosaicResponse, self).to_map()
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
            temp_model = AddImageMosaicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddStoryFilesRequestFiles(TeaModel):
    def __init__(self, uri=None):
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddStoryFilesRequestFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class AddStoryFilesRequest(TeaModel):
    def __init__(self, dataset_name=None, files=None, object_id=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.files = files  # type: list[AddStoryFilesRequestFiles]
        self.object_id = object_id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddStoryFilesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = AddStoryFilesRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class AddStoryFilesShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, files_shrink=None, object_id=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.files_shrink = files_shrink  # type: str
        self.object_id = object_id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddStoryFilesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class AddStoryFilesResponseBodyFiles(TeaModel):
    def __init__(self, error_code=None, error_message=None, uri=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddStoryFilesResponseBodyFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class AddStoryFilesResponseBody(TeaModel):
    def __init__(self, files=None, request_id=None):
        self.files = files  # type: list[AddStoryFilesResponseBodyFiles]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddStoryFilesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = AddStoryFilesResponseBodyFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddStoryFilesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddStoryFilesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddStoryFilesResponse, self).to_map()
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
            temp_model = AddStoryFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachOSSBucketRequest(TeaModel):
    def __init__(self, description=None, ossbucket=None, project_name=None):
        self.description = description  # type: str
        self.ossbucket = ossbucket  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachOSSBucketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class AttachOSSBucketResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachOSSBucketResponseBody, self).to_map()
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


class AttachOSSBucketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachOSSBucketResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachOSSBucketResponse, self).to_map()
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
            temp_model = AttachOSSBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteFileMetaRequest(TeaModel):
    def __init__(self, dataset_name=None, project_name=None, uris=None):
        self.dataset_name = dataset_name  # type: str
        self.project_name = project_name  # type: str
        self.uris = uris  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uris is not None:
            result['URIs'] = self.uris
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URIs') is not None:
            self.uris = m.get('URIs')
        return self


class BatchDeleteFileMetaShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, project_name=None, uris_shrink=None):
        self.dataset_name = dataset_name  # type: str
        self.project_name = project_name  # type: str
        self.uris_shrink = uris_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteFileMetaShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uris_shrink is not None:
            result['URIs'] = self.uris_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URIs') is not None:
            self.uris_shrink = m.get('URIs')
        return self


class BatchDeleteFileMetaResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteFileMetaResponseBody, self).to_map()
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


class BatchDeleteFileMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchDeleteFileMetaResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchDeleteFileMetaResponse, self).to_map()
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
            temp_model = BatchDeleteFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetFigureClusterRequest(TeaModel):
    def __init__(self, dataset_name=None, object_ids=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.object_ids = object_ids  # type: list[str]
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetFigureClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_ids is not None:
            result['ObjectIds'] = self.object_ids
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectIds') is not None:
            self.object_ids = m.get('ObjectIds')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class BatchGetFigureClusterShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, object_ids_shrink=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.object_ids_shrink = object_ids_shrink  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetFigureClusterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_ids_shrink is not None:
            result['ObjectIds'] = self.object_ids_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectIds') is not None:
            self.object_ids_shrink = m.get('ObjectIds')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class BatchGetFigureClusterResponseBody(TeaModel):
    def __init__(self, figure_clusters=None, request_id=None):
        self.figure_clusters = figure_clusters  # type: list[FigureCluster]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.figure_clusters:
            for k in self.figure_clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchGetFigureClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FigureClusters'] = []
        if self.figure_clusters is not None:
            for k in self.figure_clusters:
                result['FigureClusters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.figure_clusters = []
        if m.get('FigureClusters') is not None:
            for k in m.get('FigureClusters'):
                temp_model = FigureCluster()
                self.figure_clusters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchGetFigureClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchGetFigureClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchGetFigureClusterResponse, self).to_map()
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
            temp_model = BatchGetFigureClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetFileMetaRequest(TeaModel):
    def __init__(self, dataset_name=None, project_name=None, uris=None):
        self.dataset_name = dataset_name  # type: str
        self.project_name = project_name  # type: str
        self.uris = uris  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uris is not None:
            result['URIs'] = self.uris
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URIs') is not None:
            self.uris = m.get('URIs')
        return self


class BatchGetFileMetaShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, project_name=None, uris_shrink=None):
        self.dataset_name = dataset_name  # type: str
        self.project_name = project_name  # type: str
        self.uris_shrink = uris_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetFileMetaShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uris_shrink is not None:
            result['URIs'] = self.uris_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URIs') is not None:
            self.uris_shrink = m.get('URIs')
        return self


class BatchGetFileMetaResponseBody(TeaModel):
    def __init__(self, files=None, request_id=None):
        self.files = files  # type: list[File]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchGetFileMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchGetFileMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchGetFileMetaResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchGetFileMetaResponse, self).to_map()
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
            temp_model = BatchGetFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchIndexFileMetaRequest(TeaModel):
    def __init__(self, dataset_name=None, files=None, notification=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.files = files  # type: list[InputFile]
        self.notification = notification  # type: Notification
        self.project_name = project_name  # type: str

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super(BatchIndexFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = InputFile()
                self.files.append(temp_model.from_map(k))
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class BatchIndexFileMetaShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, files_shrink=None, notification_shrink=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.files_shrink = files_shrink  # type: str
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchIndexFileMetaShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class BatchIndexFileMetaResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchIndexFileMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchIndexFileMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchIndexFileMetaResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchIndexFileMetaResponse, self).to_map()
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
            temp_model = BatchIndexFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateFileMetaRequest(TeaModel):
    def __init__(self, dataset_name=None, files=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.files = files  # type: list[InputFile]
        self.project_name = project_name  # type: str

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchUpdateFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = InputFile()
                self.files.append(temp_model.from_map(k))
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class BatchUpdateFileMetaShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, files_shrink=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.files_shrink = files_shrink  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUpdateFileMetaShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class BatchUpdateFileMetaResponseBodyFiles(TeaModel):
    def __init__(self, message=None, success=None, uri=None):
        self.message = message  # type: str
        self.success = success  # type: bool
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUpdateFileMetaResponseBodyFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class BatchUpdateFileMetaResponseBody(TeaModel):
    def __init__(self, files=None, request_id=None):
        self.files = files  # type: list[BatchUpdateFileMetaResponseBodyFiles]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchUpdateFileMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = BatchUpdateFileMetaResponseBodyFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchUpdateFileMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchUpdateFileMetaResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchUpdateFileMetaResponse, self).to_map()
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
            temp_model = BatchUpdateFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompareImageFacesRequestSource(TeaModel):
    def __init__(self, uri1=None, uri2=None):
        self.uri1 = uri1  # type: str
        self.uri2 = uri2  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompareImageFacesRequestSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri1 is not None:
            result['URI1'] = self.uri1
        if self.uri2 is not None:
            result['URI2'] = self.uri2
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('URI1') is not None:
            self.uri1 = m.get('URI1')
        if m.get('URI2') is not None:
            self.uri2 = m.get('URI2')
        return self


class CompareImageFacesRequest(TeaModel):
    def __init__(self, credential_config=None, project_name=None, source=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.project_name = project_name  # type: str
        self.source = source  # type: CompareImageFacesRequestSource

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        _map = super(CompareImageFacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source is not None:
            result['Source'] = self.source.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Source') is not None:
            temp_model = CompareImageFacesRequestSource()
            self.source = temp_model.from_map(m['Source'])
        return self


class CompareImageFacesShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, project_name=None, source_shrink=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.project_name = project_name  # type: str
        self.source_shrink = source_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompareImageFacesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_shrink is not None:
            result['Source'] = self.source_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Source') is not None:
            self.source_shrink = m.get('Source')
        return self


class CompareImageFacesResponseBody(TeaModel):
    def __init__(self, request_id=None, similarity=None):
        self.request_id = request_id  # type: str
        self.similarity = similarity  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompareImageFacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        return self


class CompareImageFacesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CompareImageFacesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CompareImageFacesResponse, self).to_map()
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
            temp_model = CompareImageFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateArchiveFileInspectionTaskRequest(TeaModel):
    def __init__(self, credential_config=None, notification=None, password=None, project_name=None, source_uri=None,
                 user_data=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.notification = notification  # type: Notification
        self.password = password  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super(CreateArchiveFileInspectionTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateArchiveFileInspectionTaskShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, notification_shrink=None, password=None, project_name=None,
                 source_uri=None, user_data=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.notification_shrink = notification_shrink  # type: str
        self.password = password  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateArchiveFileInspectionTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateArchiveFileInspectionTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateArchiveFileInspectionTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateArchiveFileInspectionTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateArchiveFileInspectionTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateArchiveFileInspectionTaskResponse, self).to_map()
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
            temp_model = CreateArchiveFileInspectionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBatchRequestActions(TeaModel):
    def __init__(self, fast_fail_policy=None, name=None, parameters=None):
        self.fast_fail_policy = fast_fail_policy  # type: FastFailPolicy
        self.name = name  # type: str
        self.parameters = parameters  # type: list[str]

    def validate(self):
        if self.fast_fail_policy:
            self.fast_fail_policy.validate()

    def to_map(self):
        _map = super(CreateBatchRequestActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fast_fail_policy is not None:
            result['FastFailPolicy'] = self.fast_fail_policy.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FastFailPolicy') is not None:
            temp_model = FastFailPolicy()
            self.fast_fail_policy = temp_model.from_map(m['FastFailPolicy'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class CreateBatchRequestNotification(TeaModel):
    def __init__(self, mns=None):
        self.mns = mns  # type: MNS

    def validate(self):
        if self.mns:
            self.mns.validate()

    def to_map(self):
        _map = super(CreateBatchRequestNotification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mns is not None:
            result['MNS'] = self.mns.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MNS') is not None:
            temp_model = MNS()
            self.mns = temp_model.from_map(m['MNS'])
        return self


class CreateBatchRequest(TeaModel):
    def __init__(self, actions=None, input=None, notification=None, project_name=None, service_role=None, tags=None):
        self.actions = actions  # type: list[CreateBatchRequestActions]
        self.input = input  # type: Input
        self.notification = notification  # type: CreateBatchRequestNotification
        self.project_name = project_name  # type: str
        self.service_role = service_role  # type: str
        self.tags = tags  # type: dict[str, any]

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.input:
            self.input.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super(CreateBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = CreateBatchRequestActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('Input') is not None:
            temp_model = Input()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Notification') is not None:
            temp_model = CreateBatchRequestNotification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class CreateBatchShrinkRequest(TeaModel):
    def __init__(self, actions_shrink=None, input_shrink=None, notification_shrink=None, project_name=None,
                 service_role=None, tags_shrink=None):
        self.actions_shrink = actions_shrink  # type: str
        self.input_shrink = input_shrink  # type: str
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str
        self.service_role = service_role  # type: str
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBatchShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions_shrink is not None:
            result['Actions'] = self.actions_shrink
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions_shrink = m.get('Actions')
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class CreateBatchResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBatchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBatchResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBatchResponse, self).to_map()
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
            temp_model = CreateBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBindingRequest(TeaModel):
    def __init__(self, dataset_name=None, project_name=None, uri=None):
        self.dataset_name = dataset_name  # type: str
        self.project_name = project_name  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBindingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateBindingResponseBody(TeaModel):
    def __init__(self, binding=None, request_id=None):
        self.binding = binding  # type: Binding
        self.request_id = request_id  # type: str

    def validate(self):
        if self.binding:
            self.binding.validate()

    def to_map(self):
        _map = super(CreateBindingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding is not None:
            result['Binding'] = self.binding.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Binding') is not None:
            temp_model = Binding()
            self.binding = temp_model.from_map(m['Binding'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBindingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBindingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBindingResponse, self).to_map()
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
            temp_model = CreateBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCompressPointCloudTaskRequest(TeaModel):
    def __init__(self, compress_method=None, credential_config=None, kdtree_option=None, notification=None,
                 octree_option=None, point_cloud_fields=None, point_cloud_file_format=None, project_name=None, source_uri=None,
                 tags=None, target_uri=None, user_data=None):
        self.compress_method = compress_method  # type: str
        self.credential_config = credential_config  # type: CredentialConfig
        self.kdtree_option = kdtree_option  # type: KdtreeOption
        self.notification = notification  # type: Notification
        self.octree_option = octree_option  # type: OctreeOption
        self.point_cloud_fields = point_cloud_fields  # type: list[str]
        self.point_cloud_file_format = point_cloud_file_format  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str
        self.tags = tags  # type: dict[str, any]
        self.target_uri = target_uri  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.kdtree_option:
            self.kdtree_option.validate()
        if self.notification:
            self.notification.validate()
        if self.octree_option:
            self.octree_option.validate()

    def to_map(self):
        _map = super(CreateCompressPointCloudTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compress_method is not None:
            result['CompressMethod'] = self.compress_method
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.kdtree_option is not None:
            result['KdtreeOption'] = self.kdtree_option.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.octree_option is not None:
            result['OctreeOption'] = self.octree_option.to_map()
        if self.point_cloud_fields is not None:
            result['PointCloudFields'] = self.point_cloud_fields
        if self.point_cloud_file_format is not None:
            result['PointCloudFileFormat'] = self.point_cloud_file_format
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompressMethod') is not None:
            self.compress_method = m.get('CompressMethod')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('KdtreeOption') is not None:
            temp_model = KdtreeOption()
            self.kdtree_option = temp_model.from_map(m['KdtreeOption'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('OctreeOption') is not None:
            temp_model = OctreeOption()
            self.octree_option = temp_model.from_map(m['OctreeOption'])
        if m.get('PointCloudFields') is not None:
            self.point_cloud_fields = m.get('PointCloudFields')
        if m.get('PointCloudFileFormat') is not None:
            self.point_cloud_file_format = m.get('PointCloudFileFormat')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateCompressPointCloudTaskShrinkRequest(TeaModel):
    def __init__(self, compress_method=None, credential_config_shrink=None, kdtree_option_shrink=None,
                 notification_shrink=None, octree_option_shrink=None, point_cloud_fields_shrink=None, point_cloud_file_format=None,
                 project_name=None, source_uri=None, tags_shrink=None, target_uri=None, user_data=None):
        self.compress_method = compress_method  # type: str
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.kdtree_option_shrink = kdtree_option_shrink  # type: str
        self.notification_shrink = notification_shrink  # type: str
        self.octree_option_shrink = octree_option_shrink  # type: str
        self.point_cloud_fields_shrink = point_cloud_fields_shrink  # type: str
        self.point_cloud_file_format = point_cloud_file_format  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.target_uri = target_uri  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCompressPointCloudTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compress_method is not None:
            result['CompressMethod'] = self.compress_method
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.kdtree_option_shrink is not None:
            result['KdtreeOption'] = self.kdtree_option_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.octree_option_shrink is not None:
            result['OctreeOption'] = self.octree_option_shrink
        if self.point_cloud_fields_shrink is not None:
            result['PointCloudFields'] = self.point_cloud_fields_shrink
        if self.point_cloud_file_format is not None:
            result['PointCloudFileFormat'] = self.point_cloud_file_format
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompressMethod') is not None:
            self.compress_method = m.get('CompressMethod')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('KdtreeOption') is not None:
            self.kdtree_option_shrink = m.get('KdtreeOption')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('OctreeOption') is not None:
            self.octree_option_shrink = m.get('OctreeOption')
        if m.get('PointCloudFields') is not None:
            self.point_cloud_fields_shrink = m.get('PointCloudFields')
        if m.get('PointCloudFileFormat') is not None:
            self.point_cloud_file_format = m.get('PointCloudFileFormat')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateCompressPointCloudTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCompressPointCloudTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateCompressPointCloudTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCompressPointCloudTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCompressPointCloudTaskResponse, self).to_map()
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
            temp_model = CreateCompressPointCloudTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomizedStoryRequestCover(TeaModel):
    def __init__(self, uri=None):
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomizedStoryRequestCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateCustomizedStoryRequestFiles(TeaModel):
    def __init__(self, uri=None):
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomizedStoryRequestFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateCustomizedStoryRequest(TeaModel):
    def __init__(self, cover=None, custom_labels=None, dataset_name=None, files=None, project_name=None,
                 story_name=None, story_sub_type=None, story_type=None):
        self.cover = cover  # type: CreateCustomizedStoryRequestCover
        self.custom_labels = custom_labels  # type: dict[str, any]
        self.dataset_name = dataset_name  # type: str
        self.files = files  # type: list[CreateCustomizedStoryRequestFiles]
        self.project_name = project_name  # type: str
        self.story_name = story_name  # type: str
        self.story_sub_type = story_sub_type  # type: str
        self.story_type = story_type  # type: str

    def validate(self):
        if self.cover:
            self.cover.validate()
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateCustomizedStoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cover') is not None:
            temp_model = CreateCustomizedStoryRequestCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = CreateCustomizedStoryRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        return self


class CreateCustomizedStoryShrinkRequest(TeaModel):
    def __init__(self, cover_shrink=None, custom_labels_shrink=None, dataset_name=None, files_shrink=None,
                 project_name=None, story_name=None, story_sub_type=None, story_type=None):
        self.cover_shrink = cover_shrink  # type: str
        self.custom_labels_shrink = custom_labels_shrink  # type: str
        self.dataset_name = dataset_name  # type: str
        self.files_shrink = files_shrink  # type: str
        self.project_name = project_name  # type: str
        self.story_name = story_name  # type: str
        self.story_sub_type = story_sub_type  # type: str
        self.story_type = story_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomizedStoryShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_shrink is not None:
            result['Cover'] = self.cover_shrink
        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cover') is not None:
            self.cover_shrink = m.get('Cover')
        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        return self


class CreateCustomizedStoryResponseBody(TeaModel):
    def __init__(self, object_id=None, request_id=None):
        self.object_id = object_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomizedStoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCustomizedStoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCustomizedStoryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCustomizedStoryResponse, self).to_map()
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
            temp_model = CreateCustomizedStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasetRequest(TeaModel):
    def __init__(self, dataset_max_bind_count=None, dataset_max_entity_count=None, dataset_max_file_count=None,
                 dataset_max_relation_count=None, dataset_max_total_file_size=None, dataset_name=None, description=None, project_name=None,
                 template_id=None):
        self.dataset_max_bind_count = dataset_max_bind_count  # type: long
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        self.dataset_max_total_file_size = dataset_max_total_file_size  # type: long
        self.dataset_name = dataset_name  # type: str
        self.description = description  # type: str
        self.project_name = project_name  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDatasetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateDatasetResponseBody(TeaModel):
    def __init__(self, dataset=None, request_id=None):
        self.dataset = dataset  # type: Dataset
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super(CreateDatasetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dataset') is not None:
            temp_model = Dataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatasetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDatasetResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDatasetResponse, self).to_map()
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
            temp_model = CreateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFacesSearchingTaskRequestSources(TeaModel):
    def __init__(self, uri=None):
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFacesSearchingTaskRequestSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateFacesSearchingTaskRequest(TeaModel):
    def __init__(self, dataset_name=None, max_result=None, notification=None, project_name=None, sources=None,
                 user_data=None):
        self.dataset_name = dataset_name  # type: str
        self.max_result = max_result  # type: long
        self.notification = notification  # type: Notification
        self.project_name = project_name  # type: str
        self.sources = sources  # type: list[CreateFacesSearchingTaskRequestSources]
        self.user_data = user_data  # type: str

    def validate(self):
        if self.notification:
            self.notification.validate()
        if self.sources:
            for k in self.sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateFacesSearchingTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        result['Sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['Sources'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        self.sources = []
        if m.get('Sources') is not None:
            for k in m.get('Sources'):
                temp_model = CreateFacesSearchingTaskRequestSources()
                self.sources.append(temp_model.from_map(k))
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFacesSearchingTaskShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, max_result=None, notification_shrink=None, project_name=None,
                 sources_shrink=None, user_data=None):
        self.dataset_name = dataset_name  # type: str
        self.max_result = max_result  # type: long
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str
        self.sources_shrink = sources_shrink  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFacesSearchingTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFacesSearchingTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFacesSearchingTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateFacesSearchingTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFacesSearchingTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFacesSearchingTaskResponse, self).to_map()
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
            temp_model = CreateFacesSearchingTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFigureClusteringTaskRequest(TeaModel):
    def __init__(self, dataset_name=None, notification=None, project_name=None, tags=None, user_data=None):
        self.dataset_name = dataset_name  # type: str
        self.notification = notification  # type: Notification
        self.project_name = project_name  # type: str
        self.tags = tags  # type: dict[str, any]
        self.user_data = user_data  # type: str

    def validate(self):
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super(CreateFigureClusteringTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFigureClusteringTaskShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, notification_shrink=None, project_name=None, tags_shrink=None,
                 user_data=None):
        self.dataset_name = dataset_name  # type: str
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFigureClusteringTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFigureClusteringTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFigureClusteringTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateFigureClusteringTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFigureClusteringTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFigureClusteringTaskResponse, self).to_map()
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
            temp_model = CreateFigureClusteringTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFigureClustersMergingTaskRequest(TeaModel):
    def __init__(self, dataset_name=None, from_=None, froms=None, notification=None, project_name=None, tags=None,
                 to=None, user_data=None):
        self.dataset_name = dataset_name  # type: str
        self.from_ = from_  # type: str
        self.froms = froms  # type: list[str]
        self.notification = notification  # type: Notification
        self.project_name = project_name  # type: str
        self.tags = tags  # type: dict[str, any]
        self.to = to  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super(CreateFigureClustersMergingTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.from_ is not None:
            result['From'] = self.from_
        if self.froms is not None:
            result['Froms'] = self.froms
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.to is not None:
            result['To'] = self.to
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Froms') is not None:
            self.froms = m.get('Froms')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFigureClustersMergingTaskShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, from_=None, froms_shrink=None, notification_shrink=None,
                 project_name=None, tags_shrink=None, to=None, user_data=None):
        self.dataset_name = dataset_name  # type: str
        self.from_ = from_  # type: str
        self.froms_shrink = froms_shrink  # type: str
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.to = to  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFigureClustersMergingTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.from_ is not None:
            result['From'] = self.from_
        if self.froms_shrink is not None:
            result['Froms'] = self.froms_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.to is not None:
            result['To'] = self.to
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Froms') is not None:
            self.froms_shrink = m.get('Froms')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFigureClustersMergingTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFigureClustersMergingTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateFigureClustersMergingTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFigureClustersMergingTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFigureClustersMergingTaskResponse, self).to_map()
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
            temp_model = CreateFigureClustersMergingTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileCompressionTaskRequestSources(TeaModel):
    def __init__(self, alias=None, mode=None, uri=None):
        self.alias = alias  # type: str
        self.mode = mode  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileCompressionTaskRequestSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateFileCompressionTaskRequest(TeaModel):
    def __init__(self, compressed_format=None, credential_config=None, notification=None, project_name=None,
                 source_manifest_uri=None, sources=None, target_uri=None, user_data=None):
        self.compressed_format = compressed_format  # type: str
        self.credential_config = credential_config  # type: CredentialConfig
        self.notification = notification  # type: Notification
        self.project_name = project_name  # type: str
        self.source_manifest_uri = source_manifest_uri  # type: str
        self.sources = sources  # type: list[CreateFileCompressionTaskRequestSources]
        self.target_uri = target_uri  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.sources:
            for k in self.sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateFileCompressionTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compressed_format is not None:
            result['CompressedFormat'] = self.compressed_format
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_manifest_uri is not None:
            result['SourceManifestURI'] = self.source_manifest_uri
        result['Sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['Sources'].append(k.to_map() if k else None)
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompressedFormat') is not None:
            self.compressed_format = m.get('CompressedFormat')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceManifestURI') is not None:
            self.source_manifest_uri = m.get('SourceManifestURI')
        self.sources = []
        if m.get('Sources') is not None:
            for k in m.get('Sources'):
                temp_model = CreateFileCompressionTaskRequestSources()
                self.sources.append(temp_model.from_map(k))
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFileCompressionTaskShrinkRequest(TeaModel):
    def __init__(self, compressed_format=None, credential_config_shrink=None, notification_shrink=None,
                 project_name=None, source_manifest_uri=None, sources_shrink=None, target_uri=None, user_data=None):
        self.compressed_format = compressed_format  # type: str
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str
        self.source_manifest_uri = source_manifest_uri  # type: str
        self.sources_shrink = sources_shrink  # type: str
        self.target_uri = target_uri  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileCompressionTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compressed_format is not None:
            result['CompressedFormat'] = self.compressed_format
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_manifest_uri is not None:
            result['SourceManifestURI'] = self.source_manifest_uri
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompressedFormat') is not None:
            self.compressed_format = m.get('CompressedFormat')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceManifestURI') is not None:
            self.source_manifest_uri = m.get('SourceManifestURI')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFileCompressionTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileCompressionTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateFileCompressionTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFileCompressionTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFileCompressionTaskResponse, self).to_map()
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
            temp_model = CreateFileCompressionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileUncompressionTaskRequest(TeaModel):
    def __init__(self, credential_config=None, notification=None, password=None, project_name=None,
                 selected_files=None, source_uri=None, target_uri=None, user_data=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.notification = notification  # type: Notification
        self.password = password  # type: str
        self.project_name = project_name  # type: str
        self.selected_files = selected_files  # type: list[str]
        self.source_uri = source_uri  # type: str
        self.target_uri = target_uri  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super(CreateFileUncompressionTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.selected_files is not None:
            result['SelectedFiles'] = self.selected_files
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SelectedFiles') is not None:
            self.selected_files = m.get('SelectedFiles')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFileUncompressionTaskShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, notification_shrink=None, password=None, project_name=None,
                 selected_files_shrink=None, source_uri=None, target_uri=None, user_data=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.notification_shrink = notification_shrink  # type: str
        self.password = password  # type: str
        self.project_name = project_name  # type: str
        self.selected_files_shrink = selected_files_shrink  # type: str
        self.source_uri = source_uri  # type: str
        self.target_uri = target_uri  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileUncompressionTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.selected_files_shrink is not None:
            result['SelectedFiles'] = self.selected_files_shrink
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SelectedFiles') is not None:
            self.selected_files_shrink = m.get('SelectedFiles')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateFileUncompressionTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileUncompressionTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateFileUncompressionTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFileUncompressionTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFileUncompressionTaskResponse, self).to_map()
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
            temp_model = CreateFileUncompressionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageModerationTaskRequest(TeaModel):
    def __init__(self, credential_config=None, interval=None, max_frames=None, notification=None, project_name=None,
                 scenes=None, source_uri=None, tags=None, user_data=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.interval = interval  # type: long
        self.max_frames = max_frames  # type: long
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification = notification  # type: Notification
        self.project_name = project_name  # type: str
        self.scenes = scenes  # type: list[str]
        self.source_uri = source_uri  # type: str
        self.tags = tags  # type: dict[str, any]
        self.user_data = user_data  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super(CreateImageModerationTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.scenes is not None:
            result['Scenes'] = self.scenes
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Scenes') is not None:
            self.scenes = m.get('Scenes')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageModerationTaskShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, interval=None, max_frames=None, notification_shrink=None,
                 project_name=None, scenes_shrink=None, source_uri=None, tags_shrink=None, user_data=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.interval = interval  # type: long
        self.max_frames = max_frames  # type: long
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str
        self.scenes_shrink = scenes_shrink  # type: str
        self.source_uri = source_uri  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageModerationTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.scenes_shrink is not None:
            result['Scenes'] = self.scenes_shrink
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Scenes') is not None:
            self.scenes_shrink = m.get('Scenes')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageModerationTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageModerationTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateImageModerationTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateImageModerationTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateImageModerationTaskResponse, self).to_map()
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
            temp_model = CreateImageModerationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageSplicingTaskRequestSources(TeaModel):
    def __init__(self, rotate=None, uri=None):
        self.rotate = rotate  # type: long
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageSplicingTaskRequestSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateImageSplicingTaskRequest(TeaModel):
    def __init__(self, align=None, background_color=None, credential_config=None, direction=None, image_format=None,
                 margin=None, notification=None, padding=None, project_name=None, quality=None, scale_type=None,
                 sources=None, tags=None, target_uri=None, user_data=None):
        self.align = align  # type: long
        self.background_color = background_color  # type: str
        self.credential_config = credential_config  # type: CredentialConfig
        self.direction = direction  # type: str
        self.image_format = image_format  # type: str
        self.margin = margin  # type: long
        self.notification = notification  # type: Notification
        self.padding = padding  # type: long
        self.project_name = project_name  # type: str
        self.quality = quality  # type: long
        self.scale_type = scale_type  # type: str
        self.sources = sources  # type: list[CreateImageSplicingTaskRequestSources]
        self.tags = tags  # type: dict[str, any]
        self.target_uri = target_uri  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.sources:
            for k in self.sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateImageSplicingTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align is not None:
            result['Align'] = self.align
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.margin is not None:
            result['Margin'] = self.margin
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.padding is not None:
            result['Padding'] = self.padding
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        result['Sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['Sources'].append(k.to_map() if k else None)
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Align') is not None:
            self.align = m.get('Align')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('Margin') is not None:
            self.margin = m.get('Margin')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('Padding') is not None:
            self.padding = m.get('Padding')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        self.sources = []
        if m.get('Sources') is not None:
            for k in m.get('Sources'):
                temp_model = CreateImageSplicingTaskRequestSources()
                self.sources.append(temp_model.from_map(k))
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageSplicingTaskShrinkRequest(TeaModel):
    def __init__(self, align=None, background_color=None, credential_config_shrink=None, direction=None,
                 image_format=None, margin=None, notification_shrink=None, padding=None, project_name=None, quality=None,
                 scale_type=None, sources_shrink=None, tags_shrink=None, target_uri=None, user_data=None):
        self.align = align  # type: long
        self.background_color = background_color  # type: str
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.direction = direction  # type: str
        self.image_format = image_format  # type: str
        self.margin = margin  # type: long
        self.notification_shrink = notification_shrink  # type: str
        self.padding = padding  # type: long
        self.project_name = project_name  # type: str
        self.quality = quality  # type: long
        self.scale_type = scale_type  # type: str
        self.sources_shrink = sources_shrink  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.target_uri = target_uri  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageSplicingTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.align is not None:
            result['Align'] = self.align
        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.margin is not None:
            result['Margin'] = self.margin
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.padding is not None:
            result['Padding'] = self.padding
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Align') is not None:
            self.align = m.get('Align')
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('Margin') is not None:
            self.margin = m.get('Margin')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('Padding') is not None:
            self.padding = m.get('Padding')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageSplicingTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageSplicingTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateImageSplicingTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateImageSplicingTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateImageSplicingTaskResponse, self).to_map()
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
            temp_model = CreateImageSplicingTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageToPDFTaskRequestSources(TeaModel):
    def __init__(self, rotate=None, uri=None):
        self.rotate = rotate  # type: long
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageToPDFTaskRequestSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateImageToPDFTaskRequest(TeaModel):
    def __init__(self, credential_config=None, notification=None, project_name=None, sources=None, tags=None,
                 target_uri=None, user_data=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.notification = notification  # type: Notification
        self.project_name = project_name  # type: str
        self.sources = sources  # type: list[CreateImageToPDFTaskRequestSources]
        self.tags = tags  # type: dict[str, any]
        self.target_uri = target_uri  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.sources:
            for k in self.sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateImageToPDFTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        result['Sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['Sources'].append(k.to_map() if k else None)
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        self.sources = []
        if m.get('Sources') is not None:
            for k in m.get('Sources'):
                temp_model = CreateImageToPDFTaskRequestSources()
                self.sources.append(temp_model.from_map(k))
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageToPDFTaskShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, notification_shrink=None, project_name=None,
                 sources_shrink=None, tags_shrink=None, target_uri=None, user_data=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str
        self.sources_shrink = sources_shrink  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.target_uri = target_uri  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageToPDFTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateImageToPDFTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageToPDFTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateImageToPDFTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateImageToPDFTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateImageToPDFTaskResponse, self).to_map()
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
            temp_model = CreateImageToPDFTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLocationDateClusteringTaskRequestDateOptions(TeaModel):
    def __init__(self, gap_days=None, max_days=None, min_days=None):
        self.gap_days = gap_days  # type: long
        self.max_days = max_days  # type: long
        self.min_days = min_days  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLocationDateClusteringTaskRequestDateOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gap_days is not None:
            result['GapDays'] = self.gap_days
        if self.max_days is not None:
            result['MaxDays'] = self.max_days
        if self.min_days is not None:
            result['MinDays'] = self.min_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GapDays') is not None:
            self.gap_days = m.get('GapDays')
        if m.get('MaxDays') is not None:
            self.max_days = m.get('MaxDays')
        if m.get('MinDays') is not None:
            self.min_days = m.get('MinDays')
        return self


class CreateLocationDateClusteringTaskRequestLocationOptions(TeaModel):
    def __init__(self, location_date_cluster_levels=None):
        self.location_date_cluster_levels = location_date_cluster_levels  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLocationDateClusteringTaskRequestLocationOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location_date_cluster_levels is not None:
            result['LocationDateClusterLevels'] = self.location_date_cluster_levels
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocationDateClusterLevels') is not None:
            self.location_date_cluster_levels = m.get('LocationDateClusterLevels')
        return self


class CreateLocationDateClusteringTaskRequest(TeaModel):
    def __init__(self, dataset_name=None, date_options=None, location_options=None, notification=None,
                 project_name=None, tags=None, user_data=None):
        self.dataset_name = dataset_name  # type: str
        self.date_options = date_options  # type: CreateLocationDateClusteringTaskRequestDateOptions
        self.location_options = location_options  # type: CreateLocationDateClusteringTaskRequestLocationOptions
        self.notification = notification  # type: Notification
        self.project_name = project_name  # type: str
        self.tags = tags  # type: dict[str, any]
        self.user_data = user_data  # type: str

    def validate(self):
        if self.date_options:
            self.date_options.validate()
        if self.location_options:
            self.location_options.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super(CreateLocationDateClusteringTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.date_options is not None:
            result['DateOptions'] = self.date_options.to_map()
        if self.location_options is not None:
            result['LocationOptions'] = self.location_options.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('DateOptions') is not None:
            temp_model = CreateLocationDateClusteringTaskRequestDateOptions()
            self.date_options = temp_model.from_map(m['DateOptions'])
        if m.get('LocationOptions') is not None:
            temp_model = CreateLocationDateClusteringTaskRequestLocationOptions()
            self.location_options = temp_model.from_map(m['LocationOptions'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateLocationDateClusteringTaskShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, date_options_shrink=None, location_options_shrink=None,
                 notification_shrink=None, project_name=None, tags_shrink=None, user_data=None):
        self.dataset_name = dataset_name  # type: str
        self.date_options_shrink = date_options_shrink  # type: str
        self.location_options_shrink = location_options_shrink  # type: str
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLocationDateClusteringTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.date_options_shrink is not None:
            result['DateOptions'] = self.date_options_shrink
        if self.location_options_shrink is not None:
            result['LocationOptions'] = self.location_options_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('DateOptions') is not None:
            self.date_options_shrink = m.get('DateOptions')
        if m.get('LocationOptions') is not None:
            self.location_options_shrink = m.get('LocationOptions')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateLocationDateClusteringTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLocationDateClusteringTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateLocationDateClusteringTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLocationDateClusteringTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLocationDateClusteringTaskResponse, self).to_map()
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
            temp_model = CreateLocationDateClusteringTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMediaConvertTaskRequestSourcesSubtitles(TeaModel):
    def __init__(self, language=None, time_offset=None, uri=None):
        self.language = language  # type: str
        self.time_offset = time_offset  # type: float
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMediaConvertTaskRequestSourcesSubtitles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.time_offset is not None:
            result['TimeOffset'] = self.time_offset
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('TimeOffset') is not None:
            self.time_offset = m.get('TimeOffset')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateMediaConvertTaskRequestSources(TeaModel):
    def __init__(self, duration=None, start_time=None, subtitles=None, uri=None):
        self.duration = duration  # type: float
        self.start_time = start_time  # type: float
        self.subtitles = subtitles  # type: list[CreateMediaConvertTaskRequestSourcesSubtitles]
        self.uri = uri  # type: str

    def validate(self):
        if self.subtitles:
            for k in self.subtitles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateMediaConvertTaskRequestSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['Subtitles'] = []
        if self.subtitles is not None:
            for k in self.subtitles:
                result['Subtitles'].append(k.to_map() if k else None)
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k in m.get('Subtitles'):
                temp_model = CreateMediaConvertTaskRequestSourcesSubtitles()
                self.subtitles.append(temp_model.from_map(k))
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateMediaConvertTaskRequestTargetsSegment(TeaModel):
    def __init__(self, duration=None, format=None, start_number=None):
        self.duration = duration  # type: float
        self.format = format  # type: str
        self.start_number = start_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMediaConvertTaskRequestTargetsSegment, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.format is not None:
            result['Format'] = self.format
        if self.start_number is not None:
            result['StartNumber'] = self.start_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('StartNumber') is not None:
            self.start_number = m.get('StartNumber')
        return self


class CreateMediaConvertTaskRequestTargets(TeaModel):
    def __init__(self, audio=None, container=None, image=None, segment=None, speed=None, strip_metadata=None,
                 subtitle=None, uri=None, video=None):
        self.audio = audio  # type: TargetAudio
        self.container = container  # type: str
        self.image = image  # type: TargetImage
        self.segment = segment  # type: CreateMediaConvertTaskRequestTargetsSegment
        self.speed = speed  # type: float
        self.strip_metadata = strip_metadata  # type: bool
        self.subtitle = subtitle  # type: TargetSubtitle
        self.uri = uri  # type: str
        self.video = video  # type: TargetVideo

    def validate(self):
        if self.audio:
            self.audio.validate()
        if self.image:
            self.image.validate()
        if self.segment:
            self.segment.validate()
        if self.subtitle:
            self.subtitle.validate()
        if self.video:
            self.video.validate()

    def to_map(self):
        _map = super(CreateMediaConvertTaskRequestTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio is not None:
            result['Audio'] = self.audio.to_map()
        if self.container is not None:
            result['Container'] = self.container
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.segment is not None:
            result['Segment'] = self.segment.to_map()
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.strip_metadata is not None:
            result['StripMetadata'] = self.strip_metadata
        if self.subtitle is not None:
            result['Subtitle'] = self.subtitle.to_map()
        if self.uri is not None:
            result['URI'] = self.uri
        if self.video is not None:
            result['Video'] = self.video.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Audio') is not None:
            temp_model = TargetAudio()
            self.audio = temp_model.from_map(m['Audio'])
        if m.get('Container') is not None:
            self.container = m.get('Container')
        if m.get('Image') is not None:
            temp_model = TargetImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('Segment') is not None:
            temp_model = CreateMediaConvertTaskRequestTargetsSegment()
            self.segment = temp_model.from_map(m['Segment'])
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('StripMetadata') is not None:
            self.strip_metadata = m.get('StripMetadata')
        if m.get('Subtitle') is not None:
            temp_model = TargetSubtitle()
            self.subtitle = temp_model.from_map(m['Subtitle'])
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Video') is not None:
            temp_model = TargetVideo()
            self.video = temp_model.from_map(m['Video'])
        return self


class CreateMediaConvertTaskRequest(TeaModel):
    def __init__(self, alignment_index=None, credential_config=None, notification=None, project_name=None,
                 sources=None, tags=None, targets=None, user_data=None):
        self.alignment_index = alignment_index  # type: int
        self.credential_config = credential_config  # type: CredentialConfig
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification = notification  # type: Notification
        self.project_name = project_name  # type: str
        self.sources = sources  # type: list[CreateMediaConvertTaskRequestSources]
        self.tags = tags  # type: dict[str, any]
        self.targets = targets  # type: list[CreateMediaConvertTaskRequestTargets]
        self.user_data = user_data  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.sources:
            for k in self.sources:
                if k:
                    k.validate()
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateMediaConvertTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alignment_index is not None:
            result['AlignmentIndex'] = self.alignment_index
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        result['Sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['Sources'].append(k.to_map() if k else None)
        if self.tags is not None:
            result['Tags'] = self.tags
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlignmentIndex') is not None:
            self.alignment_index = m.get('AlignmentIndex')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        self.sources = []
        if m.get('Sources') is not None:
            for k in m.get('Sources'):
                temp_model = CreateMediaConvertTaskRequestSources()
                self.sources.append(temp_model.from_map(k))
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = CreateMediaConvertTaskRequestTargets()
                self.targets.append(temp_model.from_map(k))
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateMediaConvertTaskShrinkRequest(TeaModel):
    def __init__(self, alignment_index=None, credential_config_shrink=None, notification_shrink=None,
                 project_name=None, sources_shrink=None, tags_shrink=None, targets_shrink=None, user_data=None):
        self.alignment_index = alignment_index  # type: int
        self.credential_config_shrink = credential_config_shrink  # type: str
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str
        self.sources_shrink = sources_shrink  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.targets_shrink = targets_shrink  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMediaConvertTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alignment_index is not None:
            result['AlignmentIndex'] = self.alignment_index
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlignmentIndex') is not None:
            self.alignment_index = m.get('AlignmentIndex')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateMediaConvertTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMediaConvertTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateMediaConvertTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateMediaConvertTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMediaConvertTaskResponse, self).to_map()
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
            temp_model = CreateMediaConvertTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOfficeConversionTaskRequest(TeaModel):
    def __init__(self, credential_config=None, end_page=None, first_page=None, fit_to_height=None,
                 fit_to_width=None, hold_line_feed=None, image_dpi=None, long_picture=None, long_text=None,
                 max_sheet_column=None, max_sheet_row=None, notification=None, pages=None, paper_horizontal=None, paper_size=None,
                 password=None, project_name=None, quality=None, scale_percentage=None, sheet_count=None, sheet_index=None,
                 show_comments=None, source_type=None, source_uri=None, start_page=None, tags=None, target_type=None,
                 target_uri=None, target_uriprefix=None, trim_policy=None, user_data=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.end_page = end_page  # type: long
        self.first_page = first_page  # type: bool
        self.fit_to_height = fit_to_height  # type: bool
        self.fit_to_width = fit_to_width  # type: bool
        self.hold_line_feed = hold_line_feed  # type: bool
        self.image_dpi = image_dpi  # type: long
        self.long_picture = long_picture  # type: bool
        self.long_text = long_text  # type: bool
        self.max_sheet_column = max_sheet_column  # type: long
        self.max_sheet_row = max_sheet_row  # type: long
        self.notification = notification  # type: Notification
        self.pages = pages  # type: str
        self.paper_horizontal = paper_horizontal  # type: bool
        self.paper_size = paper_size  # type: str
        self.password = password  # type: str
        self.project_name = project_name  # type: str
        self.quality = quality  # type: long
        self.scale_percentage = scale_percentage  # type: long
        self.sheet_count = sheet_count  # type: long
        self.sheet_index = sheet_index  # type: long
        self.show_comments = show_comments  # type: bool
        self.source_type = source_type  # type: str
        self.source_uri = source_uri  # type: str
        self.start_page = start_page  # type: long
        self.tags = tags  # type: dict[str, any]
        self.target_type = target_type  # type: str
        self.target_uri = target_uri  # type: str
        self.target_uriprefix = target_uriprefix  # type: str
        self.trim_policy = trim_policy  # type: TrimPolicy
        self.user_data = user_data  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.trim_policy:
            self.trim_policy.validate()

    def to_map(self):
        _map = super(CreateOfficeConversionTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.end_page is not None:
            result['EndPage'] = self.end_page
        if self.first_page is not None:
            result['FirstPage'] = self.first_page
        if self.fit_to_height is not None:
            result['FitToHeight'] = self.fit_to_height
        if self.fit_to_width is not None:
            result['FitToWidth'] = self.fit_to_width
        if self.hold_line_feed is not None:
            result['HoldLineFeed'] = self.hold_line_feed
        if self.image_dpi is not None:
            result['ImageDPI'] = self.image_dpi
        if self.long_picture is not None:
            result['LongPicture'] = self.long_picture
        if self.long_text is not None:
            result['LongText'] = self.long_text
        if self.max_sheet_column is not None:
            result['MaxSheetColumn'] = self.max_sheet_column
        if self.max_sheet_row is not None:
            result['MaxSheetRow'] = self.max_sheet_row
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.paper_horizontal is not None:
            result['PaperHorizontal'] = self.paper_horizontal
        if self.paper_size is not None:
            result['PaperSize'] = self.paper_size
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.scale_percentage is not None:
            result['ScalePercentage'] = self.scale_percentage
        if self.sheet_count is not None:
            result['SheetCount'] = self.sheet_count
        if self.sheet_index is not None:
            result['SheetIndex'] = self.sheet_index
        if self.show_comments is not None:
            result['ShowComments'] = self.show_comments
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.start_page is not None:
            result['StartPage'] = self.start_page
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.target_uriprefix is not None:
            result['TargetURIPrefix'] = self.target_uriprefix
        if self.trim_policy is not None:
            result['TrimPolicy'] = self.trim_policy.to_map()
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('EndPage') is not None:
            self.end_page = m.get('EndPage')
        if m.get('FirstPage') is not None:
            self.first_page = m.get('FirstPage')
        if m.get('FitToHeight') is not None:
            self.fit_to_height = m.get('FitToHeight')
        if m.get('FitToWidth') is not None:
            self.fit_to_width = m.get('FitToWidth')
        if m.get('HoldLineFeed') is not None:
            self.hold_line_feed = m.get('HoldLineFeed')
        if m.get('ImageDPI') is not None:
            self.image_dpi = m.get('ImageDPI')
        if m.get('LongPicture') is not None:
            self.long_picture = m.get('LongPicture')
        if m.get('LongText') is not None:
            self.long_text = m.get('LongText')
        if m.get('MaxSheetColumn') is not None:
            self.max_sheet_column = m.get('MaxSheetColumn')
        if m.get('MaxSheetRow') is not None:
            self.max_sheet_row = m.get('MaxSheetRow')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('PaperHorizontal') is not None:
            self.paper_horizontal = m.get('PaperHorizontal')
        if m.get('PaperSize') is not None:
            self.paper_size = m.get('PaperSize')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('ScalePercentage') is not None:
            self.scale_percentage = m.get('ScalePercentage')
        if m.get('SheetCount') is not None:
            self.sheet_count = m.get('SheetCount')
        if m.get('SheetIndex') is not None:
            self.sheet_index = m.get('SheetIndex')
        if m.get('ShowComments') is not None:
            self.show_comments = m.get('ShowComments')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('StartPage') is not None:
            self.start_page = m.get('StartPage')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('TargetURIPrefix') is not None:
            self.target_uriprefix = m.get('TargetURIPrefix')
        if m.get('TrimPolicy') is not None:
            temp_model = TrimPolicy()
            self.trim_policy = temp_model.from_map(m['TrimPolicy'])
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateOfficeConversionTaskShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, end_page=None, first_page=None, fit_to_height=None,
                 fit_to_width=None, hold_line_feed=None, image_dpi=None, long_picture=None, long_text=None,
                 max_sheet_column=None, max_sheet_row=None, notification_shrink=None, pages=None, paper_horizontal=None,
                 paper_size=None, password=None, project_name=None, quality=None, scale_percentage=None, sheet_count=None,
                 sheet_index=None, show_comments=None, source_type=None, source_uri=None, start_page=None, tags_shrink=None,
                 target_type=None, target_uri=None, target_uriprefix=None, trim_policy_shrink=None, user_data=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.end_page = end_page  # type: long
        self.first_page = first_page  # type: bool
        self.fit_to_height = fit_to_height  # type: bool
        self.fit_to_width = fit_to_width  # type: bool
        self.hold_line_feed = hold_line_feed  # type: bool
        self.image_dpi = image_dpi  # type: long
        self.long_picture = long_picture  # type: bool
        self.long_text = long_text  # type: bool
        self.max_sheet_column = max_sheet_column  # type: long
        self.max_sheet_row = max_sheet_row  # type: long
        self.notification_shrink = notification_shrink  # type: str
        self.pages = pages  # type: str
        self.paper_horizontal = paper_horizontal  # type: bool
        self.paper_size = paper_size  # type: str
        self.password = password  # type: str
        self.project_name = project_name  # type: str
        self.quality = quality  # type: long
        self.scale_percentage = scale_percentage  # type: long
        self.sheet_count = sheet_count  # type: long
        self.sheet_index = sheet_index  # type: long
        self.show_comments = show_comments  # type: bool
        self.source_type = source_type  # type: str
        self.source_uri = source_uri  # type: str
        self.start_page = start_page  # type: long
        self.tags_shrink = tags_shrink  # type: str
        self.target_type = target_type  # type: str
        self.target_uri = target_uri  # type: str
        self.target_uriprefix = target_uriprefix  # type: str
        self.trim_policy_shrink = trim_policy_shrink  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOfficeConversionTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.end_page is not None:
            result['EndPage'] = self.end_page
        if self.first_page is not None:
            result['FirstPage'] = self.first_page
        if self.fit_to_height is not None:
            result['FitToHeight'] = self.fit_to_height
        if self.fit_to_width is not None:
            result['FitToWidth'] = self.fit_to_width
        if self.hold_line_feed is not None:
            result['HoldLineFeed'] = self.hold_line_feed
        if self.image_dpi is not None:
            result['ImageDPI'] = self.image_dpi
        if self.long_picture is not None:
            result['LongPicture'] = self.long_picture
        if self.long_text is not None:
            result['LongText'] = self.long_text
        if self.max_sheet_column is not None:
            result['MaxSheetColumn'] = self.max_sheet_column
        if self.max_sheet_row is not None:
            result['MaxSheetRow'] = self.max_sheet_row
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.paper_horizontal is not None:
            result['PaperHorizontal'] = self.paper_horizontal
        if self.paper_size is not None:
            result['PaperSize'] = self.paper_size
        if self.password is not None:
            result['Password'] = self.password
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.quality is not None:
            result['Quality'] = self.quality
        if self.scale_percentage is not None:
            result['ScalePercentage'] = self.scale_percentage
        if self.sheet_count is not None:
            result['SheetCount'] = self.sheet_count
        if self.sheet_index is not None:
            result['SheetIndex'] = self.sheet_index
        if self.show_comments is not None:
            result['ShowComments'] = self.show_comments
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.start_page is not None:
            result['StartPage'] = self.start_page
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri
        if self.target_uriprefix is not None:
            result['TargetURIPrefix'] = self.target_uriprefix
        if self.trim_policy_shrink is not None:
            result['TrimPolicy'] = self.trim_policy_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('EndPage') is not None:
            self.end_page = m.get('EndPage')
        if m.get('FirstPage') is not None:
            self.first_page = m.get('FirstPage')
        if m.get('FitToHeight') is not None:
            self.fit_to_height = m.get('FitToHeight')
        if m.get('FitToWidth') is not None:
            self.fit_to_width = m.get('FitToWidth')
        if m.get('HoldLineFeed') is not None:
            self.hold_line_feed = m.get('HoldLineFeed')
        if m.get('ImageDPI') is not None:
            self.image_dpi = m.get('ImageDPI')
        if m.get('LongPicture') is not None:
            self.long_picture = m.get('LongPicture')
        if m.get('LongText') is not None:
            self.long_text = m.get('LongText')
        if m.get('MaxSheetColumn') is not None:
            self.max_sheet_column = m.get('MaxSheetColumn')
        if m.get('MaxSheetRow') is not None:
            self.max_sheet_row = m.get('MaxSheetRow')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('PaperHorizontal') is not None:
            self.paper_horizontal = m.get('PaperHorizontal')
        if m.get('PaperSize') is not None:
            self.paper_size = m.get('PaperSize')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')
        if m.get('ScalePercentage') is not None:
            self.scale_percentage = m.get('ScalePercentage')
        if m.get('SheetCount') is not None:
            self.sheet_count = m.get('SheetCount')
        if m.get('SheetIndex') is not None:
            self.sheet_index = m.get('SheetIndex')
        if m.get('ShowComments') is not None:
            self.show_comments = m.get('ShowComments')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('StartPage') is not None:
            self.start_page = m.get('StartPage')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')
        if m.get('TargetURIPrefix') is not None:
            self.target_uriprefix = m.get('TargetURIPrefix')
        if m.get('TrimPolicy') is not None:
            self.trim_policy_shrink = m.get('TrimPolicy')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateOfficeConversionTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOfficeConversionTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateOfficeConversionTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOfficeConversionTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOfficeConversionTaskResponse, self).to_map()
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
            temp_model = CreateOfficeConversionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(self, dataset_max_bind_count=None, dataset_max_entity_count=None, dataset_max_file_count=None,
                 dataset_max_relation_count=None, dataset_max_total_file_size=None, description=None, project_max_dataset_count=None,
                 project_name=None, service_role=None, template_id=None):
        self.dataset_max_bind_count = dataset_max_bind_count  # type: long
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        self.dataset_max_total_file_size = dataset_max_total_file_size  # type: long
        self.description = description  # type: str
        self.project_max_dataset_count = project_max_dataset_count  # type: long
        self.project_name = project_name  # type: str
        self.service_role = service_role  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.description is not None:
            result['Description'] = self.description
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(self, project=None, request_id=None):
        self.project = project  # type: Project
        self.request_id = request_id  # type: str

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super(CreateProjectResponseBody, self).to_map()
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
            temp_model = Project()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateProjectResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProjectResponse, self).to_map()
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSimilarImageClusteringTaskRequest(TeaModel):
    def __init__(self, dataset_name=None, notification=None, project_name=None, tags=None, user_data=None):
        self.dataset_name = dataset_name  # type: str
        self.notification = notification  # type: Notification
        self.project_name = project_name  # type: str
        self.tags = tags  # type: dict[str, any]
        self.user_data = user_data  # type: str

    def validate(self):
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super(CreateSimilarImageClusteringTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateSimilarImageClusteringTaskShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, notification_shrink=None, project_name=None, tags_shrink=None,
                 user_data=None):
        self.dataset_name = dataset_name  # type: str
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSimilarImageClusteringTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateSimilarImageClusteringTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSimilarImageClusteringTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateSimilarImageClusteringTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSimilarImageClusteringTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSimilarImageClusteringTaskResponse, self).to_map()
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
            temp_model = CreateSimilarImageClusteringTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStoryRequest(TeaModel):
    def __init__(self, address=None, custom_id=None, custom_labels=None, dataset_name=None, max_file_count=None,
                 min_file_count=None, notification=None, notify_topic_name=None, object_id=None, project_name=None,
                 story_end_time=None, story_name=None, story_start_time=None, story_sub_type=None, story_type=None, tags=None,
                 user_data=None):
        self.address = address  # type: AddressForStory
        self.custom_id = custom_id  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]
        self.dataset_name = dataset_name  # type: str
        self.max_file_count = max_file_count  # type: long
        self.min_file_count = min_file_count  # type: long
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification = notification  # type: Notification
        self.notify_topic_name = notify_topic_name  # type: str
        self.object_id = object_id  # type: str
        self.project_name = project_name  # type: str
        self.story_end_time = story_end_time  # type: str
        self.story_name = story_name  # type: str
        self.story_start_time = story_start_time  # type: str
        self.story_sub_type = story_sub_type  # type: str
        self.story_type = story_type  # type: str
        self.tags = tags  # type: dict[str, any]
        self.user_data = user_data  # type: str

    def validate(self):
        if self.address:
            self.address.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super(CreateStoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_file_count is not None:
            result['MaxFileCount'] = self.max_file_count
        if self.min_file_count is not None:
            result['MinFileCount'] = self.min_file_count
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_end_time is not None:
            result['StoryEndTime'] = self.story_end_time
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time is not None:
            result['StoryStartTime'] = self.story_start_time
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = AddressForStory()
            self.address = temp_model.from_map(m['Address'])
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxFileCount') is not None:
            self.max_file_count = m.get('MaxFileCount')
        if m.get('MinFileCount') is not None:
            self.min_file_count = m.get('MinFileCount')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryEndTime') is not None:
            self.story_end_time = m.get('StoryEndTime')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTime') is not None:
            self.story_start_time = m.get('StoryStartTime')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateStoryShrinkRequest(TeaModel):
    def __init__(self, address_shrink=None, custom_id=None, custom_labels_shrink=None, dataset_name=None,
                 max_file_count=None, min_file_count=None, notification_shrink=None, notify_topic_name=None, object_id=None,
                 project_name=None, story_end_time=None, story_name=None, story_start_time=None, story_sub_type=None,
                 story_type=None, tags_shrink=None, user_data=None):
        self.address_shrink = address_shrink  # type: str
        self.custom_id = custom_id  # type: str
        self.custom_labels_shrink = custom_labels_shrink  # type: str
        self.dataset_name = dataset_name  # type: str
        self.max_file_count = max_file_count  # type: long
        self.min_file_count = min_file_count  # type: long
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification_shrink = notification_shrink  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.object_id = object_id  # type: str
        self.project_name = project_name  # type: str
        self.story_end_time = story_end_time  # type: str
        self.story_name = story_name  # type: str
        self.story_start_time = story_start_time  # type: str
        self.story_sub_type = story_sub_type  # type: str
        self.story_type = story_type  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStoryShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_shrink is not None:
            result['Address'] = self.address_shrink
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_file_count is not None:
            result['MaxFileCount'] = self.max_file_count
        if self.min_file_count is not None:
            result['MinFileCount'] = self.min_file_count
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_end_time is not None:
            result['StoryEndTime'] = self.story_end_time
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time is not None:
            result['StoryStartTime'] = self.story_start_time
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address_shrink = m.get('Address')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxFileCount') is not None:
            self.max_file_count = m.get('MaxFileCount')
        if m.get('MinFileCount') is not None:
            self.min_file_count = m.get('MinFileCount')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryEndTime') is not None:
            self.story_end_time = m.get('StoryEndTime')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTime') is not None:
            self.story_start_time = m.get('StoryStartTime')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateStoryResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateStoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateStoryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateStoryResponse, self).to_map()
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
            temp_model = CreateStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTriggerRequestActions(TeaModel):
    def __init__(self, fast_fail_policy=None, name=None, parameters=None):
        self.fast_fail_policy = fast_fail_policy  # type: FastFailPolicy
        self.name = name  # type: str
        self.parameters = parameters  # type: list[str]

    def validate(self):
        if self.fast_fail_policy:
            self.fast_fail_policy.validate()

    def to_map(self):
        _map = super(CreateTriggerRequestActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fast_fail_policy is not None:
            result['FastFailPolicy'] = self.fast_fail_policy.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FastFailPolicy') is not None:
            temp_model = FastFailPolicy()
            self.fast_fail_policy = temp_model.from_map(m['FastFailPolicy'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class CreateTriggerRequestNotification(TeaModel):
    def __init__(self, mns=None):
        self.mns = mns  # type: MNS

    def validate(self):
        if self.mns:
            self.mns.validate()

    def to_map(self):
        _map = super(CreateTriggerRequestNotification, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mns is not None:
            result['MNS'] = self.mns.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MNS') is not None:
            temp_model = MNS()
            self.mns = temp_model.from_map(m['MNS'])
        return self


class CreateTriggerRequest(TeaModel):
    def __init__(self, actions=None, input=None, notification=None, project_name=None, service_role=None, tags=None):
        self.actions = actions  # type: list[CreateTriggerRequestActions]
        self.input = input  # type: Input
        self.notification = notification  # type: CreateTriggerRequestNotification
        self.project_name = project_name  # type: str
        self.service_role = service_role  # type: str
        self.tags = tags  # type: dict[str, any]

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.input:
            self.input.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super(CreateTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = CreateTriggerRequestActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('Input') is not None:
            temp_model = Input()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Notification') is not None:
            temp_model = CreateTriggerRequestNotification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class CreateTriggerShrinkRequest(TeaModel):
    def __init__(self, actions_shrink=None, input_shrink=None, notification_shrink=None, project_name=None,
                 service_role=None, tags_shrink=None):
        self.actions_shrink = actions_shrink  # type: str
        self.input_shrink = input_shrink  # type: str
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str
        self.service_role = service_role  # type: str
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTriggerShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions_shrink is not None:
            result['Actions'] = self.actions_shrink
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions_shrink = m.get('Actions')
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class CreateTriggerResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTriggerResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTriggerResponse, self).to_map()
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
            temp_model = CreateTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoLabelClassificationTaskRequest(TeaModel):
    def __init__(self, credential_config=None, notification=None, project_name=None, source_uri=None, tags=None,
                 user_data=None):
        self.credential_config = credential_config  # type: CredentialConfig
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification = notification  # type: Notification
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str
        self.tags = tags  # type: dict[str, any]
        self.user_data = user_data  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super(CreateVideoLabelClassificationTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateVideoLabelClassificationTaskShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, notification_shrink=None, project_name=None, source_uri=None,
                 tags_shrink=None, user_data=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVideoLabelClassificationTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateVideoLabelClassificationTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVideoLabelClassificationTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateVideoLabelClassificationTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVideoLabelClassificationTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVideoLabelClassificationTaskResponse, self).to_map()
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
            temp_model = CreateVideoLabelClassificationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoModerationTaskRequest(TeaModel):
    def __init__(self, credential_config=None, interval=None, max_frames=None, notification=None, project_name=None,
                 scenes=None, source_uri=None, tags=None, user_data=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.interval = interval  # type: long
        self.max_frames = max_frames  # type: long
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification = notification  # type: Notification
        self.project_name = project_name  # type: str
        self.scenes = scenes  # type: list[str]
        self.source_uri = source_uri  # type: str
        self.tags = tags  # type: dict[str, any]
        self.user_data = user_data  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super(CreateVideoModerationTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.scenes is not None:
            result['Scenes'] = self.scenes
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Scenes') is not None:
            self.scenes = m.get('Scenes')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateVideoModerationTaskShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, interval=None, max_frames=None, notification_shrink=None,
                 project_name=None, scenes_shrink=None, source_uri=None, tags_shrink=None, user_data=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.interval = interval  # type: long
        self.max_frames = max_frames  # type: long
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str
        self.scenes_shrink = scenes_shrink  # type: str
        self.source_uri = source_uri  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVideoModerationTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.scenes_shrink is not None:
            result['Scenes'] = self.scenes_shrink
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Scenes') is not None:
            self.scenes_shrink = m.get('Scenes')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateVideoModerationTaskResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None, task_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVideoModerationTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateVideoModerationTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVideoModerationTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVideoModerationTaskResponse, self).to_map()
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
            temp_model = CreateVideoModerationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBatchRequest(TeaModel):
    def __init__(self, id=None, project_name=None):
        self.id = id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteBatchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBatchResponseBody, self).to_map()
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


class DeleteBatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBatchResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBatchResponse, self).to_map()
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
            temp_model = DeleteBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBindingRequest(TeaModel):
    def __init__(self, dataset_name=None, project_name=None, uri=None):
        self.dataset_name = dataset_name  # type: str
        self.project_name = project_name  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBindingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class DeleteBindingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBindingResponseBody, self).to_map()
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


class DeleteBindingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBindingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBindingResponse, self).to_map()
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
            temp_model = DeleteBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatasetRequest(TeaModel):
    def __init__(self, dataset_name=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDatasetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteDatasetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDatasetResponseBody, self).to_map()
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


class DeleteDatasetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDatasetResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDatasetResponse, self).to_map()
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
            temp_model = DeleteDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileMetaRequest(TeaModel):
    def __init__(self, dataset_name=None, project_name=None, uri=None):
        self.dataset_name = dataset_name  # type: str
        self.project_name = project_name  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class DeleteFileMetaResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileMetaResponseBody, self).to_map()
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


class DeleteFileMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFileMetaResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFileMetaResponse, self).to_map()
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
            temp_model = DeleteFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLocationDateClusterRequest(TeaModel):
    def __init__(self, dataset_name=None, object_id=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.object_id = object_id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLocationDateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteLocationDateClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLocationDateClusterResponseBody, self).to_map()
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


class DeleteLocationDateClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLocationDateClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLocationDateClusterResponse, self).to_map()
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
            temp_model = DeleteLocationDateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(self, project_name=None):
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectResponseBody, self).to_map()
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


class DeleteProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteProjectResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProjectResponse, self).to_map()
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStoryRequest(TeaModel):
    def __init__(self, dataset_name=None, object_id=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.object_id = object_id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteStoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStoryResponseBody, self).to_map()
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


class DeleteStoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteStoryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteStoryResponse, self).to_map()
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
            temp_model = DeleteStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTriggerRequest(TeaModel):
    def __init__(self, id=None, project_name=None):
        self.id = id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DeleteTriggerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTriggerResponseBody, self).to_map()
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


class DeleteTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTriggerResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTriggerResponse, self).to_map()
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
            temp_model = DeleteTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachOSSBucketRequest(TeaModel):
    def __init__(self, ossbucket=None):
        self.ossbucket = ossbucket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachOSSBucketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')
        return self


class DetachOSSBucketResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachOSSBucketResponseBody, self).to_map()
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


class DetachOSSBucketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachOSSBucketResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachOSSBucketResponse, self).to_map()
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
            temp_model = DetachOSSBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageBodiesRequest(TeaModel):
    def __init__(self, credential_config=None, project_name=None, sensitivity=None, source_uri=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.project_name = project_name  # type: str
        self.sensitivity = sensitivity  # type: float
        self.source_uri = source_uri  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super(DetectImageBodiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sensitivity is not None:
            result['Sensitivity'] = self.sensitivity
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sensitivity') is not None:
            self.sensitivity = m.get('Sensitivity')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageBodiesShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, project_name=None, sensitivity=None, source_uri=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.project_name = project_name  # type: str
        self.sensitivity = sensitivity  # type: float
        self.source_uri = source_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageBodiesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sensitivity is not None:
            result['Sensitivity'] = self.sensitivity
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sensitivity') is not None:
            self.sensitivity = m.get('Sensitivity')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageBodiesResponseBody(TeaModel):
    def __init__(self, bodies=None, request_id=None):
        self.bodies = bodies  # type: list[Body]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.bodies:
            for k in self.bodies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectImageBodiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bodies'] = []
        if self.bodies is not None:
            for k in self.bodies:
                result['Bodies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bodies = []
        if m.get('Bodies') is not None:
            for k in m.get('Bodies'):
                temp_model = Body()
                self.bodies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageBodiesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetectImageBodiesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectImageBodiesResponse, self).to_map()
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
            temp_model = DetectImageBodiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageCarsRequest(TeaModel):
    def __init__(self, credential_config=None, project_name=None, source_uri=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super(DetectImageCarsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCarsShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, project_name=None, source_uri=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageCarsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCarsResponseBody(TeaModel):
    def __init__(self, cars=None, request_id=None):
        self.cars = cars  # type: list[Car]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cars:
            for k in self.cars:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectImageCarsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cars'] = []
        if self.cars is not None:
            for k in self.cars:
                result['Cars'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cars = []
        if m.get('Cars') is not None:
            for k in m.get('Cars'):
                temp_model = Car()
                self.cars.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageCarsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetectImageCarsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectImageCarsResponse, self).to_map()
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
            temp_model = DetectImageCarsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageCodesRequest(TeaModel):
    def __init__(self, credential_config=None, project_name=None, source_uri=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super(DetectImageCodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCodesShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, project_name=None, source_uri=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageCodesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCodesResponseBody(TeaModel):
    def __init__(self, codes=None, request_id=None):
        self.codes = codes  # type: list[Codes]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.codes:
            for k in self.codes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectImageCodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Codes'] = []
        if self.codes is not None:
            for k in self.codes:
                result['Codes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.codes = []
        if m.get('Codes') is not None:
            for k in m.get('Codes'):
                temp_model = Codes()
                self.codes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageCodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetectImageCodesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectImageCodesResponse, self).to_map()
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
            temp_model = DetectImageCodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageCroppingRequest(TeaModel):
    def __init__(self, aspect_ratios=None, credential_config=None, project_name=None, source_uri=None):
        self.aspect_ratios = aspect_ratios  # type: str
        self.credential_config = credential_config  # type: CredentialConfig
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super(DetectImageCroppingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aspect_ratios is not None:
            result['AspectRatios'] = self.aspect_ratios
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AspectRatios') is not None:
            self.aspect_ratios = m.get('AspectRatios')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCroppingShrinkRequest(TeaModel):
    def __init__(self, aspect_ratios=None, credential_config_shrink=None, project_name=None, source_uri=None):
        self.aspect_ratios = aspect_ratios  # type: str
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageCroppingShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aspect_ratios is not None:
            result['AspectRatios'] = self.aspect_ratios
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AspectRatios') is not None:
            self.aspect_ratios = m.get('AspectRatios')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageCroppingResponseBody(TeaModel):
    def __init__(self, croppings=None, request_id=None):
        self.croppings = croppings  # type: list[CroppingSuggestion]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.croppings:
            for k in self.croppings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectImageCroppingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Croppings'] = []
        if self.croppings is not None:
            for k in self.croppings:
                result['Croppings'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.croppings = []
        if m.get('Croppings') is not None:
            for k in m.get('Croppings'):
                temp_model = CroppingSuggestion()
                self.croppings.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageCroppingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetectImageCroppingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectImageCroppingResponse, self).to_map()
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
            temp_model = DetectImageCroppingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageFacesRequest(TeaModel):
    def __init__(self, credential_config=None, project_name=None, source_uri=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super(DetectImageFacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageFacesShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, project_name=None, source_uri=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageFacesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageFacesResponseBody(TeaModel):
    def __init__(self, faces=None, request_id=None):
        self.faces = faces  # type: list[Figure]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectImageFacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = Figure()
                self.faces.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageFacesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetectImageFacesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectImageFacesResponse, self).to_map()
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
            temp_model = DetectImageFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageLabelsRequest(TeaModel):
    def __init__(self, credential_config=None, project_name=None, source_uri=None, threshold=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str
        self.threshold = threshold  # type: float

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super(DetectImageLabelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DetectImageLabelsShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, project_name=None, source_uri=None, threshold=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str
        self.threshold = threshold  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageLabelsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DetectImageLabelsResponseBody(TeaModel):
    def __init__(self, labels=None, request_id=None):
        self.labels = labels  # type: list[Label]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectImageLabelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageLabelsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetectImageLabelsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectImageLabelsResponse, self).to_map()
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
            temp_model = DetectImageLabelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageScoreRequest(TeaModel):
    def __init__(self, credential_config=None, project_name=None, source_uri=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super(DetectImageScoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageScoreShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, project_name=None, source_uri=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageScoreShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageScoreResponseBodyImageScore(TeaModel):
    def __init__(self, overall_quality_score=None):
        self.overall_quality_score = overall_quality_score  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageScoreResponseBodyImageScore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_quality_score is not None:
            result['OverallQualityScore'] = self.overall_quality_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OverallQualityScore') is not None:
            self.overall_quality_score = m.get('OverallQualityScore')
        return self


class DetectImageScoreResponseBody(TeaModel):
    def __init__(self, image_score=None, request_id=None):
        self.image_score = image_score  # type: DetectImageScoreResponseBodyImageScore
        self.request_id = request_id  # type: str

    def validate(self):
        if self.image_score:
            self.image_score.validate()

    def to_map(self):
        _map = super(DetectImageScoreResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_score is not None:
            result['ImageScore'] = self.image_score.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageScore') is not None:
            temp_model = DetectImageScoreResponseBodyImageScore()
            self.image_score = temp_model.from_map(m['ImageScore'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageScoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetectImageScoreResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectImageScoreResponse, self).to_map()
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
            temp_model = DetectImageScoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageTextsRequest(TeaModel):
    def __init__(self, credential_config=None, project_name=None, source_uri=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super(DetectImageTextsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageTextsShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, project_name=None, source_uri=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectImageTextsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectImageTextsResponseBody(TeaModel):
    def __init__(self, ocrcontents=None, ocrtexts=None, request_id=None):
        self.ocrcontents = ocrcontents  # type: list[OCRContents]
        self.ocrtexts = ocrtexts  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ocrcontents:
            for k in self.ocrcontents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectImageTextsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OCRContents'] = []
        if self.ocrcontents is not None:
            for k in self.ocrcontents:
                result['OCRContents'].append(k.to_map() if k else None)
        if self.ocrtexts is not None:
            result['OCRTexts'] = self.ocrtexts
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ocrcontents = []
        if m.get('OCRContents') is not None:
            for k in m.get('OCRContents'):
                temp_model = OCRContents()
                self.ocrcontents.append(temp_model.from_map(k))
        if m.get('OCRTexts') is not None:
            self.ocrtexts = m.get('OCRTexts')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectImageTextsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetectImageTextsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectImageTextsResponse, self).to_map()
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
            temp_model = DetectImageTextsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectMediaMetaRequest(TeaModel):
    def __init__(self, credential_config=None, project_name=None, source_uri=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super(DetectMediaMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectMediaMetaShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, project_name=None, source_uri=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectMediaMetaShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class DetectMediaMetaResponseBody(TeaModel):
    def __init__(self, addresses=None, album=None, album_artist=None, artist=None, audio_streams=None, bitrate=None,
                 composer=None, duration=None, format_long_name=None, format_name=None, language=None, lat_long=None,
                 performer=None, produce_time=None, program_count=None, request_id=None, size=None, start_time=None,
                 stream_count=None, subtitles=None, title=None, video_height=None, video_streams=None, video_width=None):
        self.addresses = addresses  # type: list[Address]
        self.album = album  # type: str
        self.album_artist = album_artist  # type: str
        self.artist = artist  # type: str
        self.audio_streams = audio_streams  # type: list[AudioStream]
        self.bitrate = bitrate  # type: long
        self.composer = composer  # type: str
        self.duration = duration  # type: float
        self.format_long_name = format_long_name  # type: str
        self.format_name = format_name  # type: str
        self.language = language  # type: str
        self.lat_long = lat_long  # type: str
        self.performer = performer  # type: str
        self.produce_time = produce_time  # type: str
        self.program_count = program_count  # type: long
        self.request_id = request_id  # type: str
        self.size = size  # type: long
        self.start_time = start_time  # type: float
        self.stream_count = stream_count  # type: long
        self.subtitles = subtitles  # type: list[SubtitleStream]
        self.title = title  # type: str
        self.video_height = video_height  # type: long
        self.video_streams = video_streams  # type: list[VideoStream]
        self.video_width = video_width  # type: long

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()
        if self.audio_streams:
            for k in self.audio_streams:
                if k:
                    k.validate()
        if self.subtitles:
            for k in self.subtitles:
                if k:
                    k.validate()
        if self.video_streams:
            for k in self.video_streams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectMediaMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.album is not None:
            result['Album'] = self.album
        if self.album_artist is not None:
            result['AlbumArtist'] = self.album_artist
        if self.artist is not None:
            result['Artist'] = self.artist
        result['AudioStreams'] = []
        if self.audio_streams is not None:
            for k in self.audio_streams:
                result['AudioStreams'].append(k.to_map() if k else None)
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.composer is not None:
            result['Composer'] = self.composer
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.format_long_name is not None:
            result['FormatLongName'] = self.format_long_name
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.language is not None:
            result['Language'] = self.language
        if self.lat_long is not None:
            result['LatLong'] = self.lat_long
        if self.performer is not None:
            result['Performer'] = self.performer
        if self.produce_time is not None:
            result['ProduceTime'] = self.produce_time
        if self.program_count is not None:
            result['ProgramCount'] = self.program_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_count is not None:
            result['StreamCount'] = self.stream_count
        result['Subtitles'] = []
        if self.subtitles is not None:
            for k in self.subtitles:
                result['Subtitles'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        if self.video_height is not None:
            result['VideoHeight'] = self.video_height
        result['VideoStreams'] = []
        if self.video_streams is not None:
            for k in self.video_streams:
                result['VideoStreams'].append(k.to_map() if k else None)
        if self.video_width is not None:
            result['VideoWidth'] = self.video_width
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = Address()
                self.addresses.append(temp_model.from_map(k))
        if m.get('Album') is not None:
            self.album = m.get('Album')
        if m.get('AlbumArtist') is not None:
            self.album_artist = m.get('AlbumArtist')
        if m.get('Artist') is not None:
            self.artist = m.get('Artist')
        self.audio_streams = []
        if m.get('AudioStreams') is not None:
            for k in m.get('AudioStreams'):
                temp_model = AudioStream()
                self.audio_streams.append(temp_model.from_map(k))
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Composer') is not None:
            self.composer = m.get('Composer')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FormatLongName') is not None:
            self.format_long_name = m.get('FormatLongName')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LatLong') is not None:
            self.lat_long = m.get('LatLong')
        if m.get('Performer') is not None:
            self.performer = m.get('Performer')
        if m.get('ProduceTime') is not None:
            self.produce_time = m.get('ProduceTime')
        if m.get('ProgramCount') is not None:
            self.program_count = m.get('ProgramCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamCount') is not None:
            self.stream_count = m.get('StreamCount')
        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k in m.get('Subtitles'):
                temp_model = SubtitleStream()
                self.subtitles.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoHeight') is not None:
            self.video_height = m.get('VideoHeight')
        self.video_streams = []
        if m.get('VideoStreams') is not None:
            for k in m.get('VideoStreams'):
                temp_model = VideoStream()
                self.video_streams.append(temp_model.from_map(k))
        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')
        return self


class DetectMediaMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetectMediaMetaResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectMediaMetaResponse, self).to_map()
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
            temp_model = DetectMediaMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectTextAnomalyRequest(TeaModel):
    def __init__(self, content=None, project_name=None):
        self.content = content  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectTextAnomalyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DetectTextAnomalyResponseBody(TeaModel):
    def __init__(self, request_id=None, suggestion=None):
        self.request_id = request_id  # type: str
        self.suggestion = suggestion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectTextAnomalyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class DetectTextAnomalyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetectTextAnomalyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectTextAnomalyResponse, self).to_map()
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
            temp_model = DetectTextAnomalyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtractDocumentTextRequest(TeaModel):
    def __init__(self, credential_config=None, project_name=None, source_type=None, source_uri=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.project_name = project_name  # type: str
        self.source_type = source_type  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super(ExtractDocumentTextRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class ExtractDocumentTextShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, project_name=None, source_type=None, source_uri=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.project_name = project_name  # type: str
        self.source_type = source_type  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractDocumentTextShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class ExtractDocumentTextResponseBody(TeaModel):
    def __init__(self, document_text=None, request_id=None):
        self.document_text = document_text  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractDocumentTextResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_text is not None:
            result['DocumentText'] = self.document_text
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DocumentText') is not None:
            self.document_text = m.get('DocumentText')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExtractDocumentTextResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExtractDocumentTextResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExtractDocumentTextResponse, self).to_map()
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
            temp_model = ExtractDocumentTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FuzzyQueryRequest(TeaModel):
    def __init__(self, dataset_name=None, max_results=None, next_token=None, order=None, project_name=None,
                 query=None, sort=None, with_fields=None):
        self.dataset_name = dataset_name  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.query = query  # type: str
        self.sort = sort  # type: str
        self.with_fields = with_fields  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(FuzzyQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query is not None:
            result['Query'] = self.query
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.with_fields is not None:
            result['WithFields'] = self.with_fields
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('WithFields') is not None:
            self.with_fields = m.get('WithFields')
        return self


class FuzzyQueryShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, max_results=None, next_token=None, order=None, project_name=None,
                 query=None, sort=None, with_fields_shrink=None):
        self.dataset_name = dataset_name  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.query = query  # type: str
        self.sort = sort  # type: str
        self.with_fields_shrink = with_fields_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FuzzyQueryShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query is not None:
            result['Query'] = self.query
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.with_fields_shrink is not None:
            result['WithFields'] = self.with_fields_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('WithFields') is not None:
            self.with_fields_shrink = m.get('WithFields')
        return self


class FuzzyQueryResponseBody(TeaModel):
    def __init__(self, files=None, next_token=None, request_id=None, total_hits=None):
        self.files = files  # type: list[File]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_hits = total_hits  # type: long

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FuzzyQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_hits is not None:
            result['TotalHits'] = self.total_hits
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalHits') is not None:
            self.total_hits = m.get('TotalHits')
        return self


class FuzzyQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FuzzyQueryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FuzzyQueryResponse, self).to_map()
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
            temp_model = FuzzyQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateVideoPlaylistRequestSourceSubtitles(TeaModel):
    def __init__(self, language=None, uri=None):
        self.language = language  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateVideoPlaylistRequestSourceSubtitles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GenerateVideoPlaylistRequestTargets(TeaModel):
    def __init__(self, audio=None, duration=None, initial_segments=None, initial_transcode=None, subtitle=None,
                 tags=None, transcode_ahead=None, uri=None, video=None):
        self.audio = audio  # type: TargetAudio
        self.duration = duration  # type: float
        self.initial_segments = initial_segments  # type: list[float]
        self.initial_transcode = initial_transcode  # type: float
        self.subtitle = subtitle  # type: TargetSubtitle
        self.tags = tags  # type: dict[str, str]
        self.transcode_ahead = transcode_ahead  # type: int
        self.uri = uri  # type: str
        self.video = video  # type: TargetVideo

    def validate(self):
        if self.audio:
            self.audio.validate()
        if self.subtitle:
            self.subtitle.validate()
        if self.video:
            self.video.validate()

    def to_map(self):
        _map = super(GenerateVideoPlaylistRequestTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio is not None:
            result['Audio'] = self.audio.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.initial_segments is not None:
            result['InitialSegments'] = self.initial_segments
        if self.initial_transcode is not None:
            result['InitialTranscode'] = self.initial_transcode
        if self.subtitle is not None:
            result['Subtitle'] = self.subtitle.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.transcode_ahead is not None:
            result['TranscodeAhead'] = self.transcode_ahead
        if self.uri is not None:
            result['URI'] = self.uri
        if self.video is not None:
            result['Video'] = self.video.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Audio') is not None:
            temp_model = TargetAudio()
            self.audio = temp_model.from_map(m['Audio'])
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InitialSegments') is not None:
            self.initial_segments = m.get('InitialSegments')
        if m.get('InitialTranscode') is not None:
            self.initial_transcode = m.get('InitialTranscode')
        if m.get('Subtitle') is not None:
            temp_model = TargetSubtitle()
            self.subtitle = temp_model.from_map(m['Subtitle'])
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TranscodeAhead') is not None:
            self.transcode_ahead = m.get('TranscodeAhead')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        if m.get('Video') is not None:
            temp_model = TargetVideo()
            self.video = temp_model.from_map(m['Video'])
        return self


class GenerateVideoPlaylistRequest(TeaModel):
    def __init__(self, credential_config=None, master_uri=None, notification=None, overwrite_policy=None,
                 project_name=None, source_duration=None, source_start_time=None, source_subtitles=None, source_uri=None,
                 tags=None, targets=None, user_data=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.master_uri = master_uri  # type: str
        self.notification = notification  # type: Notification
        self.overwrite_policy = overwrite_policy  # type: str
        self.project_name = project_name  # type: str
        self.source_duration = source_duration  # type: float
        self.source_start_time = source_start_time  # type: float
        self.source_subtitles = source_subtitles  # type: list[GenerateVideoPlaylistRequestSourceSubtitles]
        self.source_uri = source_uri  # type: str
        self.tags = tags  # type: dict[str, str]
        self.targets = targets  # type: list[GenerateVideoPlaylistRequestTargets]
        self.user_data = user_data  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.source_subtitles:
            for k in self.source_subtitles:
                if k:
                    k.validate()
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GenerateVideoPlaylistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.master_uri is not None:
            result['MasterURI'] = self.master_uri
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.overwrite_policy is not None:
            result['OverwritePolicy'] = self.overwrite_policy
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_duration is not None:
            result['SourceDuration'] = self.source_duration
        if self.source_start_time is not None:
            result['SourceStartTime'] = self.source_start_time
        result['SourceSubtitles'] = []
        if self.source_subtitles is not None:
            for k in self.source_subtitles:
                result['SourceSubtitles'].append(k.to_map() if k else None)
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags is not None:
            result['Tags'] = self.tags
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('MasterURI') is not None:
            self.master_uri = m.get('MasterURI')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('OverwritePolicy') is not None:
            self.overwrite_policy = m.get('OverwritePolicy')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceDuration') is not None:
            self.source_duration = m.get('SourceDuration')
        if m.get('SourceStartTime') is not None:
            self.source_start_time = m.get('SourceStartTime')
        self.source_subtitles = []
        if m.get('SourceSubtitles') is not None:
            for k in m.get('SourceSubtitles'):
                temp_model = GenerateVideoPlaylistRequestSourceSubtitles()
                self.source_subtitles.append(temp_model.from_map(k))
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = GenerateVideoPlaylistRequestTargets()
                self.targets.append(temp_model.from_map(k))
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GenerateVideoPlaylistShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, master_uri=None, notification_shrink=None,
                 overwrite_policy=None, project_name=None, source_duration=None, source_start_time=None,
                 source_subtitles_shrink=None, source_uri=None, tags_shrink=None, targets_shrink=None, user_data=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.master_uri = master_uri  # type: str
        self.notification_shrink = notification_shrink  # type: str
        self.overwrite_policy = overwrite_policy  # type: str
        self.project_name = project_name  # type: str
        self.source_duration = source_duration  # type: float
        self.source_start_time = source_start_time  # type: float
        self.source_subtitles_shrink = source_subtitles_shrink  # type: str
        self.source_uri = source_uri  # type: str
        self.tags_shrink = tags_shrink  # type: str
        self.targets_shrink = targets_shrink  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateVideoPlaylistShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.master_uri is not None:
            result['MasterURI'] = self.master_uri
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.overwrite_policy is not None:
            result['OverwritePolicy'] = self.overwrite_policy
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_duration is not None:
            result['SourceDuration'] = self.source_duration
        if self.source_start_time is not None:
            result['SourceStartTime'] = self.source_start_time
        if self.source_subtitles_shrink is not None:
            result['SourceSubtitles'] = self.source_subtitles_shrink
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('MasterURI') is not None:
            self.master_uri = m.get('MasterURI')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('OverwritePolicy') is not None:
            self.overwrite_policy = m.get('OverwritePolicy')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceDuration') is not None:
            self.source_duration = m.get('SourceDuration')
        if m.get('SourceStartTime') is not None:
            self.source_start_time = m.get('SourceStartTime')
        if m.get('SourceSubtitles') is not None:
            self.source_subtitles_shrink = m.get('SourceSubtitles')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GenerateVideoPlaylistResponseBodyAudioPlaylist(TeaModel):
    def __init__(self, channels=None, token=None, uri=None):
        self.channels = channels  # type: int
        # 转码生成的Token。用于LiveTranscoding访问的参数。
        self.token = token  # type: str
        # 输出m3u8的OSS地址。地址规则为 Target.URI + ".m3u8“， 其中Target.URI为输入参数中视频转码输出地址前缀。
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateVideoPlaylistResponseBodyAudioPlaylist, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.token is not None:
            result['Token'] = self.token
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GenerateVideoPlaylistResponseBodySubtitlePlaylist(TeaModel):
    def __init__(self, index=None, language=None, token=None, uri=None):
        # 字幕流编号，从0开始。
        self.index = index  # type: int
        # 视频源中字幕流的语言。
        self.language = language  # type: str
        # 转码生成的Token。用于LiveTranscoding访问的参数。
        self.token = token  # type: str
        # 输出m3u8的OSS地址。地址规则为 Target.URI + “_” + Index + ".m3u8“， 其中Target.URI为输入参数中视频转码输出地址前缀。
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateVideoPlaylistResponseBodySubtitlePlaylist, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        if self.token is not None:
            result['Token'] = self.token
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GenerateVideoPlaylistResponseBodyVideoPlaylist(TeaModel):
    def __init__(self, frame_rate=None, resolution=None, token=None, uri=None):
        self.frame_rate = frame_rate  # type: str
        self.resolution = resolution  # type: str
        # 转码生成的Token。用于LiveTranscoding访问的参数。
        self.token = token  # type: str
        # 输出m3u8的OSS地址。地址规则为 Target.URI + ".m3u8“， 其中Target.URI为输入参数中视频转码输出地址前缀。
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateVideoPlaylistResponseBodyVideoPlaylist, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.token is not None:
            result['Token'] = self.token
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GenerateVideoPlaylistResponseBody(TeaModel):
    def __init__(self, audio_playlist=None, duration=None, master_uri=None, request_id=None, subtitle_playlist=None,
                 token=None, uri=None, video_playlist=None):
        # 转码文件列表。
        self.audio_playlist = audio_playlist  # type: list[GenerateVideoPlaylistResponseBodyAudioPlaylist]
        self.duration = duration  # type: float
        self.master_uri = master_uri  # type: str
        self.request_id = request_id  # type: str
        # 转码文件列表。
        self.subtitle_playlist = subtitle_playlist  # type: list[GenerateVideoPlaylistResponseBodySubtitlePlaylist]
        self.token = token  # type: str
        self.uri = uri  # type: str
        # 转码文件列表。
        self.video_playlist = video_playlist  # type: list[GenerateVideoPlaylistResponseBodyVideoPlaylist]

    def validate(self):
        if self.audio_playlist:
            for k in self.audio_playlist:
                if k:
                    k.validate()
        if self.subtitle_playlist:
            for k in self.subtitle_playlist:
                if k:
                    k.validate()
        if self.video_playlist:
            for k in self.video_playlist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GenerateVideoPlaylistResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AudioPlaylist'] = []
        if self.audio_playlist is not None:
            for k in self.audio_playlist:
                result['AudioPlaylist'].append(k.to_map() if k else None)
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.master_uri is not None:
            result['MasterURI'] = self.master_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SubtitlePlaylist'] = []
        if self.subtitle_playlist is not None:
            for k in self.subtitle_playlist:
                result['SubtitlePlaylist'].append(k.to_map() if k else None)
        if self.token is not None:
            result['Token'] = self.token
        if self.uri is not None:
            result['URI'] = self.uri
        result['VideoPlaylist'] = []
        if self.video_playlist is not None:
            for k in self.video_playlist:
                result['VideoPlaylist'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.audio_playlist = []
        if m.get('AudioPlaylist') is not None:
            for k in m.get('AudioPlaylist'):
                temp_model = GenerateVideoPlaylistResponseBodyAudioPlaylist()
                self.audio_playlist.append(temp_model.from_map(k))
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('MasterURI') is not None:
            self.master_uri = m.get('MasterURI')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.subtitle_playlist = []
        if m.get('SubtitlePlaylist') is not None:
            for k in m.get('SubtitlePlaylist'):
                temp_model = GenerateVideoPlaylistResponseBodySubtitlePlaylist()
                self.subtitle_playlist.append(temp_model.from_map(k))
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        self.video_playlist = []
        if m.get('VideoPlaylist') is not None:
            for k in m.get('VideoPlaylist'):
                temp_model = GenerateVideoPlaylistResponseBodyVideoPlaylist()
                self.video_playlist.append(temp_model.from_map(k))
        return self


class GenerateVideoPlaylistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateVideoPlaylistResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateVideoPlaylistResponse, self).to_map()
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
            temp_model = GenerateVideoPlaylistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateWebofficeTokenRequest(TeaModel):
    def __init__(self, cache_preview=None, credential_config=None, external_uploaded=None, filename=None,
                 hidecmb=None, notification=None, notify_topic_name=None, password=None, permission=None,
                 preview_pages=None, project_name=None, referer=None, source_uri=None, user=None, user_data=None, watermark=None):
        self.cache_preview = cache_preview  # type: bool
        self.credential_config = credential_config  # type: CredentialConfig
        self.external_uploaded = external_uploaded  # type: bool
        self.filename = filename  # type: str
        self.hidecmb = hidecmb  # type: bool
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification = notification  # type: Notification
        self.notify_topic_name = notify_topic_name  # type: str
        self.password = password  # type: str
        self.permission = permission  # type: WebofficePermission
        self.preview_pages = preview_pages  # type: long
        self.project_name = project_name  # type: str
        self.referer = referer  # type: str
        self.source_uri = source_uri  # type: str
        self.user = user  # type: WebofficeUser
        self.user_data = user_data  # type: str
        self.watermark = watermark  # type: WebofficeWatermark

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.permission:
            self.permission.validate()
        if self.user:
            self.user.validate()
        if self.watermark:
            self.watermark.validate()

    def to_map(self):
        _map = super(GenerateWebofficeTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_preview is not None:
            result['CachePreview'] = self.cache_preview
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.external_uploaded is not None:
            result['ExternalUploaded'] = self.external_uploaded
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.hidecmb is not None:
            result['Hidecmb'] = self.hidecmb
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.password is not None:
            result['Password'] = self.password
        if self.permission is not None:
            result['Permission'] = self.permission.to_map()
        if self.preview_pages is not None:
            result['PreviewPages'] = self.preview_pages
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.referer is not None:
            result['Referer'] = self.referer
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.user is not None:
            result['User'] = self.user.to_map()
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.watermark is not None:
            result['Watermark'] = self.watermark.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CachePreview') is not None:
            self.cache_preview = m.get('CachePreview')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ExternalUploaded') is not None:
            self.external_uploaded = m.get('ExternalUploaded')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('Hidecmb') is not None:
            self.hidecmb = m.get('Hidecmb')
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Permission') is not None:
            temp_model = WebofficePermission()
            self.permission = temp_model.from_map(m['Permission'])
        if m.get('PreviewPages') is not None:
            self.preview_pages = m.get('PreviewPages')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Referer') is not None:
            self.referer = m.get('Referer')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('User') is not None:
            temp_model = WebofficeUser()
            self.user = temp_model.from_map(m['User'])
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Watermark') is not None:
            temp_model = WebofficeWatermark()
            self.watermark = temp_model.from_map(m['Watermark'])
        return self


class GenerateWebofficeTokenShrinkRequest(TeaModel):
    def __init__(self, cache_preview=None, credential_config_shrink=None, external_uploaded=None, filename=None,
                 hidecmb=None, notification_shrink=None, notify_topic_name=None, password=None, permission_shrink=None,
                 preview_pages=None, project_name=None, referer=None, source_uri=None, user_shrink=None, user_data=None,
                 watermark_shrink=None):
        self.cache_preview = cache_preview  # type: bool
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.external_uploaded = external_uploaded  # type: bool
        self.filename = filename  # type: str
        self.hidecmb = hidecmb  # type: bool
        # 消息通知配置，支持使用MNS、RocketMQ接收异步消息通知。
        self.notification_shrink = notification_shrink  # type: str
        self.notify_topic_name = notify_topic_name  # type: str
        self.password = password  # type: str
        self.permission_shrink = permission_shrink  # type: str
        self.preview_pages = preview_pages  # type: long
        self.project_name = project_name  # type: str
        self.referer = referer  # type: str
        self.source_uri = source_uri  # type: str
        self.user_shrink = user_shrink  # type: str
        self.user_data = user_data  # type: str
        self.watermark_shrink = watermark_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateWebofficeTokenShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_preview is not None:
            result['CachePreview'] = self.cache_preview
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.external_uploaded is not None:
            result['ExternalUploaded'] = self.external_uploaded
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.hidecmb is not None:
            result['Hidecmb'] = self.hidecmb
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.password is not None:
            result['Password'] = self.password
        if self.permission_shrink is not None:
            result['Permission'] = self.permission_shrink
        if self.preview_pages is not None:
            result['PreviewPages'] = self.preview_pages
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.referer is not None:
            result['Referer'] = self.referer
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        if self.user_shrink is not None:
            result['User'] = self.user_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.watermark_shrink is not None:
            result['Watermark'] = self.watermark_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CachePreview') is not None:
            self.cache_preview = m.get('CachePreview')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ExternalUploaded') is not None:
            self.external_uploaded = m.get('ExternalUploaded')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('Hidecmb') is not None:
            self.hidecmb = m.get('Hidecmb')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Permission') is not None:
            self.permission_shrink = m.get('Permission')
        if m.get('PreviewPages') is not None:
            self.preview_pages = m.get('PreviewPages')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Referer') is not None:
            self.referer = m.get('Referer')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        if m.get('User') is not None:
            self.user_shrink = m.get('User')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Watermark') is not None:
            self.watermark_shrink = m.get('Watermark')
        return self


class GenerateWebofficeTokenResponseBody(TeaModel):
    def __init__(self, access_token=None, access_token_expired_time=None, refresh_token=None,
                 refresh_token_expired_time=None, request_id=None, weboffice_url=None):
        self.access_token = access_token  # type: str
        self.access_token_expired_time = access_token_expired_time  # type: str
        self.refresh_token = refresh_token  # type: str
        self.refresh_token_expired_time = refresh_token_expired_time  # type: str
        self.request_id = request_id  # type: str
        self.weboffice_url = weboffice_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateWebofficeTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.weboffice_url is not None:
            result['WebofficeURL'] = self.weboffice_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WebofficeURL') is not None:
            self.weboffice_url = m.get('WebofficeURL')
        return self


class GenerateWebofficeTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateWebofficeTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateWebofficeTokenResponse, self).to_map()
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
            temp_model = GenerateWebofficeTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBatchRequest(TeaModel):
    def __init__(self, id=None, project_name=None):
        self.id = id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GetBatchResponseBody(TeaModel):
    def __init__(self, batch=None, request_id=None):
        self.batch = batch  # type: DataIngestion
        self.request_id = request_id  # type: str

    def validate(self):
        if self.batch:
            self.batch.validate()

    def to_map(self):
        _map = super(GetBatchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch is not None:
            result['Batch'] = self.batch.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Batch') is not None:
            temp_model = DataIngestion()
            self.batch = temp_model.from_map(m['Batch'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetBatchResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBatchResponse, self).to_map()
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
            temp_model = GetBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBindingRequest(TeaModel):
    def __init__(self, dataset_name=None, project_name=None, uri=None):
        self.dataset_name = dataset_name  # type: str
        self.project_name = project_name  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBindingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetBindingResponseBody(TeaModel):
    def __init__(self, binding=None, request_id=None):
        self.binding = binding  # type: Binding
        self.request_id = request_id  # type: str

    def validate(self):
        if self.binding:
            self.binding.validate()

    def to_map(self):
        _map = super(GetBindingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding is not None:
            result['Binding'] = self.binding.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Binding') is not None:
            temp_model = Binding()
            self.binding = temp_model.from_map(m['Binding'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBindingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetBindingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBindingResponse, self).to_map()
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
            temp_model = GetBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatasetRequest(TeaModel):
    def __init__(self, dataset_name=None, project_name=None, with_statistics=None):
        self.dataset_name = dataset_name  # type: str
        self.project_name = project_name  # type: str
        self.with_statistics = with_statistics  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDatasetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.with_statistics is not None:
            result['WithStatistics'] = self.with_statistics
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('WithStatistics') is not None:
            self.with_statistics = m.get('WithStatistics')
        return self


class GetDatasetResponseBody(TeaModel):
    def __init__(self, dataset=None, request_id=None):
        self.dataset = dataset  # type: Dataset
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super(GetDatasetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dataset') is not None:
            temp_model = Dataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDatasetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDatasetResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDatasetResponse, self).to_map()
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
            temp_model = GetDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFigureClusterRequest(TeaModel):
    def __init__(self, dataset_name=None, object_id=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.object_id = object_id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFigureClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GetFigureClusterResponseBody(TeaModel):
    def __init__(self, figure_cluster=None, request_id=None):
        self.figure_cluster = figure_cluster  # type: FigureCluster
        self.request_id = request_id  # type: str

    def validate(self):
        if self.figure_cluster:
            self.figure_cluster.validate()

    def to_map(self):
        _map = super(GetFigureClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_cluster is not None:
            result['FigureCluster'] = self.figure_cluster.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FigureCluster') is not None:
            temp_model = FigureCluster()
            self.figure_cluster = temp_model.from_map(m['FigureCluster'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFigureClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFigureClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFigureClusterResponse, self).to_map()
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
            temp_model = GetFigureClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileMetaRequest(TeaModel):
    def __init__(self, dataset_name=None, project_name=None, uri=None):
        self.dataset_name = dataset_name  # type: str
        self.project_name = project_name  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetFileMetaResponseBody(TeaModel):
    def __init__(self, files=None, request_id=None):
        self.files = files  # type: list[File]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFileMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFileMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFileMetaResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFileMetaResponse, self).to_map()
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
            temp_model = GetFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageModerationResultRequest(TeaModel):
    def __init__(self, project_name=None, task_id=None, task_type=None):
        self.project_name = project_name  # type: str
        self.task_id = task_id  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageModerationResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetImageModerationResultResponseBodyModerationResultFramesBlockFrames(TeaModel):
    def __init__(self, label=None, offset=None, rate=None):
        self.label = label  # type: str
        self.offset = offset  # type: int
        self.rate = rate  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageModerationResultResponseBodyModerationResultFramesBlockFrames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.rate is not None:
            result['Rate'] = self.rate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        return self


class GetImageModerationResultResponseBodyModerationResultFrames(TeaModel):
    def __init__(self, block_frames=None, total_count=None):
        self.block_frames = block_frames  # type: list[GetImageModerationResultResponseBodyModerationResultFramesBlockFrames]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.block_frames:
            for k in self.block_frames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetImageModerationResultResponseBodyModerationResultFrames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockFrames'] = []
        if self.block_frames is not None:
            for k in self.block_frames:
                result['BlockFrames'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.block_frames = []
        if m.get('BlockFrames') is not None:
            for k in m.get('BlockFrames'):
                temp_model = GetImageModerationResultResponseBodyModerationResultFramesBlockFrames()
                self.block_frames.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetImageModerationResultResponseBodyModerationResult(TeaModel):
    def __init__(self, categories=None, frames=None, suggestion=None, uri=None):
        self.categories = categories  # type: list[str]
        self.frames = frames  # type: GetImageModerationResultResponseBodyModerationResultFrames
        self.suggestion = suggestion  # type: str
        self.uri = uri  # type: str

    def validate(self):
        if self.frames:
            self.frames.validate()

    def to_map(self):
        _map = super(GetImageModerationResultResponseBodyModerationResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.frames is not None:
            result['Frames'] = self.frames.to_map()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Frames') is not None:
            temp_model = GetImageModerationResultResponseBodyModerationResultFrames()
            self.frames = temp_model.from_map(m['Frames'])
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetImageModerationResultResponseBody(TeaModel):
    def __init__(self, code=None, end_time=None, event_id=None, message=None, moderation_result=None,
                 project_name=None, request_id=None, start_time=None, status=None, task_id=None, task_type=None, user_data=None):
        self.code = code  # type: str
        self.end_time = end_time  # type: str
        self.event_id = event_id  # type: str
        self.message = message  # type: str
        self.moderation_result = moderation_result  # type: GetImageModerationResultResponseBodyModerationResult
        self.project_name = project_name  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str
        self.task_type = task_type  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        if self.moderation_result:
            self.moderation_result.validate()

    def to_map(self):
        _map = super(GetImageModerationResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.message is not None:
            result['Message'] = self.message
        if self.moderation_result is not None:
            result['ModerationResult'] = self.moderation_result.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModerationResult') is not None:
            temp_model = GetImageModerationResultResponseBodyModerationResult()
            self.moderation_result = temp_model.from_map(m['ModerationResult'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetImageModerationResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetImageModerationResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageModerationResultResponse, self).to_map()
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
            temp_model = GetImageModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOSSBucketAttachmentRequest(TeaModel):
    def __init__(self, ossbucket=None):
        self.ossbucket = ossbucket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOSSBucketAttachmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')
        return self


class GetOSSBucketAttachmentResponseBody(TeaModel):
    def __init__(self, create_time=None, description=None, project_name=None, request_id=None, update_time=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.project_name = project_name  # type: str
        self.request_id = request_id  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOSSBucketAttachmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetOSSBucketAttachmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOSSBucketAttachmentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOSSBucketAttachmentResponse, self).to_map()
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
            temp_model = GetOSSBucketAttachmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectRequest(TeaModel):
    def __init__(self, project_name=None, with_statistics=None):
        self.project_name = project_name  # type: str
        self.with_statistics = with_statistics  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.with_statistics is not None:
            result['WithStatistics'] = self.with_statistics
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('WithStatistics') is not None:
            self.with_statistics = m.get('WithStatistics')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(self, project=None, request_id=None):
        self.project = project  # type: Project
        self.request_id = request_id  # type: str

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super(GetProjectResponseBody, self).to_map()
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
            temp_model = Project()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProjectResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectResponse, self).to_map()
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
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStoryRequest(TeaModel):
    def __init__(self, dataset_name=None, object_id=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.object_id = object_id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GetStoryResponseBody(TeaModel):
    def __init__(self, request_id=None, story=None):
        self.request_id = request_id  # type: str
        self.story = story  # type: Story

    def validate(self):
        if self.story:
            self.story.validate()

    def to_map(self):
        _map = super(GetStoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.story is not None:
            result['Story'] = self.story.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Story') is not None:
            temp_model = Story()
            self.story = temp_model.from_map(m['Story'])
        return self


class GetStoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetStoryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStoryResponse, self).to_map()
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
            temp_model = GetStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskRequest(TeaModel):
    def __init__(self, project_name=None, request_definition=None, task_id=None, task_type=None):
        self.project_name = project_name  # type: str
        self.request_definition = request_definition  # type: bool
        self.task_id = task_id  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_definition is not None:
            result['RequestDefinition'] = self.request_definition
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestDefinition') is not None:
            self.request_definition = m.get('RequestDefinition')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(self, code=None, end_time=None, event_id=None, message=None, progress=None, project_name=None,
                 request_id=None, start_time=None, status=None, tags=None, task_id=None, task_request_definition=None,
                 task_type=None, user_data=None):
        self.code = code  # type: str
        self.end_time = end_time  # type: str
        self.event_id = event_id  # type: str
        self.message = message  # type: str
        self.progress = progress  # type: int
        self.project_name = project_name  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: dict[str, any]
        self.task_id = task_id  # type: str
        self.task_request_definition = task_request_definition  # type: str
        self.task_type = task_type  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.message is not None:
            result['Message'] = self.message
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_request_definition is not None:
            result['TaskRequestDefinition'] = self.task_request_definition
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskRequestDefinition') is not None:
            self.task_request_definition = m.get('TaskRequestDefinition')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTaskResponseBody

    def validate(self):
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


class GetTriggerRequest(TeaModel):
    def __init__(self, id=None, project_name=None):
        self.id = id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GetTriggerResponseBody(TeaModel):
    def __init__(self, request_id=None, trigger=None):
        self.request_id = request_id  # type: str
        self.trigger = trigger  # type: DataIngestion

    def validate(self):
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        _map = super(GetTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Trigger') is not None:
            temp_model = DataIngestion()
            self.trigger = temp_model.from_map(m['Trigger'])
        return self


class GetTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTriggerResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTriggerResponse, self).to_map()
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
            temp_model = GetTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoLabelClassificationResultRequest(TeaModel):
    def __init__(self, project_name=None, task_id=None, task_type=None):
        self.project_name = project_name  # type: str
        self.task_id = task_id  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoLabelClassificationResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetVideoLabelClassificationResultResponseBody(TeaModel):
    def __init__(self, code=None, end_time=None, event_id=None, labels=None, message=None, project_name=None,
                 request_id=None, start_time=None, status=None, task_id=None, task_type=None, user_data=None):
        self.code = code  # type: str
        self.end_time = end_time  # type: str
        self.event_id = event_id  # type: str
        self.labels = labels  # type: list[Label]
        self.message = message  # type: str
        self.project_name = project_name  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str
        self.task_type = task_type  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetVideoLabelClassificationResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_id is not None:
            result['EventId'] = self.event_id
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = Label()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetVideoLabelClassificationResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVideoLabelClassificationResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoLabelClassificationResultResponse, self).to_map()
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
            temp_model = GetVideoLabelClassificationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoModerationResultRequest(TeaModel):
    def __init__(self, project_name=None, task_id=None, task_type=None):
        self.project_name = project_name  # type: str
        self.task_id = task_id  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoModerationResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetVideoModerationResultResponseBodyModerationResultFramesBlockFrames(TeaModel):
    def __init__(self, label=None, offset=None, rate=None):
        self.label = label  # type: str
        self.offset = offset  # type: int
        self.rate = rate  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoModerationResultResponseBodyModerationResultFramesBlockFrames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.rate is not None:
            result['Rate'] = self.rate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        return self


class GetVideoModerationResultResponseBodyModerationResultFrames(TeaModel):
    def __init__(self, block_frames=None, total_count=None):
        self.block_frames = block_frames  # type: list[GetVideoModerationResultResponseBodyModerationResultFramesBlockFrames]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.block_frames:
            for k in self.block_frames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetVideoModerationResultResponseBodyModerationResultFrames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockFrames'] = []
        if self.block_frames is not None:
            for k in self.block_frames:
                result['BlockFrames'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.block_frames = []
        if m.get('BlockFrames') is not None:
            for k in m.get('BlockFrames'):
                temp_model = GetVideoModerationResultResponseBodyModerationResultFramesBlockFrames()
                self.block_frames.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetVideoModerationResultResponseBodyModerationResult(TeaModel):
    def __init__(self, categories=None, frames=None, suggestion=None, uri=None):
        self.categories = categories  # type: list[str]
        self.frames = frames  # type: GetVideoModerationResultResponseBodyModerationResultFrames
        self.suggestion = suggestion  # type: str
        self.uri = uri  # type: str

    def validate(self):
        if self.frames:
            self.frames.validate()

    def to_map(self):
        _map = super(GetVideoModerationResultResponseBodyModerationResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.frames is not None:
            result['Frames'] = self.frames.to_map()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Frames') is not None:
            temp_model = GetVideoModerationResultResponseBodyModerationResultFrames()
            self.frames = temp_model.from_map(m['Frames'])
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class GetVideoModerationResultResponseBody(TeaModel):
    def __init__(self, code=None, end_time=None, event_id=None, message=None, moderation_result=None,
                 project_name=None, request_id=None, start_time=None, status=None, task_id=None, task_type=None, user_data=None):
        self.code = code  # type: str
        self.end_time = end_time  # type: str
        self.event_id = event_id  # type: str
        self.message = message  # type: str
        self.moderation_result = moderation_result  # type: GetVideoModerationResultResponseBodyModerationResult
        self.project_name = project_name  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str
        self.task_type = task_type  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        if self.moderation_result:
            self.moderation_result.validate()

    def to_map(self):
        _map = super(GetVideoModerationResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.message is not None:
            result['Message'] = self.message
        if self.moderation_result is not None:
            result['ModerationResult'] = self.moderation_result.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModerationResult') is not None:
            temp_model = GetVideoModerationResultResponseBodyModerationResult()
            self.moderation_result = temp_model.from_map(m['ModerationResult'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetVideoModerationResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVideoModerationResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoModerationResultResponse, self).to_map()
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
            temp_model = GetVideoModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IndexFileMetaRequest(TeaModel):
    def __init__(self, dataset_name=None, file=None, notification=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.file = file  # type: InputFile
        self.notification = notification  # type: Notification
        self.project_name = project_name  # type: str

    def validate(self):
        if self.file:
            self.file.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super(IndexFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.file is not None:
            result['File'] = self.file.to_map()
        if self.notification is not None:
            result['Notification'] = self.notification.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('File') is not None:
            temp_model = InputFile()
            self.file = temp_model.from_map(m['File'])
        if m.get('Notification') is not None:
            temp_model = Notification()
            self.notification = temp_model.from_map(m['Notification'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class IndexFileMetaShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, file_shrink=None, notification_shrink=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.file_shrink = file_shrink  # type: str
        self.notification_shrink = notification_shrink  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexFileMetaShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.file_shrink is not None:
            result['File'] = self.file_shrink
        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('File') is not None:
            self.file_shrink = m.get('File')
        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class IndexFileMetaResponseBody(TeaModel):
    def __init__(self, event_id=None, request_id=None):
        self.event_id = event_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IndexFileMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IndexFileMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: IndexFileMetaResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IndexFileMetaResponse, self).to_map()
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
            temp_model = IndexFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBatchesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, order=None, project_name=None, sort=None, state=None,
                 tag_selector=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.sort = sort  # type: str
        self.state = state  # type: str
        self.tag_selector = tag_selector  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBatchesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.state is not None:
            result['State'] = self.state
        if self.tag_selector is not None:
            result['TagSelector'] = self.tag_selector
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TagSelector') is not None:
            self.tag_selector = m.get('TagSelector')
        return self


class ListBatchesResponseBody(TeaModel):
    def __init__(self, batches=None, next_token=None, request_id=None):
        self.batches = batches  # type: list[DataIngestion]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.batches:
            for k in self.batches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBatchesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Batches'] = []
        if self.batches is not None:
            for k in self.batches:
                result['Batches'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.batches = []
        if m.get('Batches') is not None:
            for k in m.get('Batches'):
                temp_model = DataIngestion()
                self.batches.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBatchesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBatchesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBatchesResponse, self).to_map()
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
            temp_model = ListBatchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindingsRequest(TeaModel):
    def __init__(self, dataset_name=None, max_results=None, next_token=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBindingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListBindingsResponseBody(TeaModel):
    def __init__(self, bindings=None, next_token=None, request_id=None):
        self.bindings = bindings  # type: list[Binding]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBindingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = Binding()
                self.bindings.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBindingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBindingsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBindingsResponse, self).to_map()
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
            temp_model = ListBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasetsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, prefix=None, project_name=None):
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.prefix = prefix  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDatasetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListDatasetsResponseBody(TeaModel):
    def __init__(self, datasets=None, next_token=None, request_id=None):
        self.datasets = datasets  # type: list[Dataset]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.datasets:
            for k in self.datasets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDatasetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Datasets'] = []
        if self.datasets is not None:
            for k in self.datasets:
                result['Datasets'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.datasets = []
        if m.get('Datasets') is not None:
            for k in m.get('Datasets'):
                temp_model = Dataset()
                self.datasets.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDatasetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDatasetsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDatasetsResponse, self).to_map()
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
            temp_model = ListDatasetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, prefix=None):
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.prefix = prefix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(self, next_token=None, projects=None, request_id=None):
        self.next_token = next_token  # type: str
        self.projects = projects  # type: list[Project]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['Projects'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.projects = []
        if m.get('Projects') is not None:
            for k in m.get('Projects'):
                temp_model = Project()
                self.projects.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectsResponse, self).to_map()
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
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: list[RegionType]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = RegionType()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRegionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRegionsResponse, self).to_map()
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(self, end_time_range=None, max_results=None, next_token=None, order=None, project_name=None,
                 request_definition=None, sort=None, start_time_range=None, status=None, tag_selector=None, task_types=None):
        self.end_time_range = end_time_range  # type: TimeRange
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.request_definition = request_definition  # type: bool
        self.sort = sort  # type: str
        self.start_time_range = start_time_range  # type: TimeRange
        self.status = status  # type: str
        self.tag_selector = tag_selector  # type: str
        self.task_types = task_types  # type: list[str]

    def validate(self):
        if self.end_time_range:
            self.end_time_range.validate()
        if self.start_time_range:
            self.start_time_range.validate()

    def to_map(self):
        _map = super(ListTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time_range is not None:
            result['EndTimeRange'] = self.end_time_range.to_map()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_definition is not None:
            result['RequestDefinition'] = self.request_definition
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_time_range is not None:
            result['StartTimeRange'] = self.start_time_range.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_selector is not None:
            result['TagSelector'] = self.tag_selector
        if self.task_types is not None:
            result['TaskTypes'] = self.task_types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimeRange') is not None:
            temp_model = TimeRange()
            self.end_time_range = temp_model.from_map(m['EndTimeRange'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestDefinition') is not None:
            self.request_definition = m.get('RequestDefinition')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartTimeRange') is not None:
            temp_model = TimeRange()
            self.start_time_range = temp_model.from_map(m['StartTimeRange'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagSelector') is not None:
            self.tag_selector = m.get('TagSelector')
        if m.get('TaskTypes') is not None:
            self.task_types = m.get('TaskTypes')
        return self


class ListTasksShrinkRequest(TeaModel):
    def __init__(self, end_time_range_shrink=None, max_results=None, next_token=None, order=None, project_name=None,
                 request_definition=None, sort=None, start_time_range_shrink=None, status=None, tag_selector=None,
                 task_types_shrink=None):
        self.end_time_range_shrink = end_time_range_shrink  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.request_definition = request_definition  # type: bool
        self.sort = sort  # type: str
        self.start_time_range_shrink = start_time_range_shrink  # type: str
        self.status = status  # type: str
        self.tag_selector = tag_selector  # type: str
        self.task_types_shrink = task_types_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time_range_shrink is not None:
            result['EndTimeRange'] = self.end_time_range_shrink
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_definition is not None:
            result['RequestDefinition'] = self.request_definition
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_time_range_shrink is not None:
            result['StartTimeRange'] = self.start_time_range_shrink
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_selector is not None:
            result['TagSelector'] = self.tag_selector
        if self.task_types_shrink is not None:
            result['TaskTypes'] = self.task_types_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimeRange') is not None:
            self.end_time_range_shrink = m.get('EndTimeRange')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestDefinition') is not None:
            self.request_definition = m.get('RequestDefinition')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartTimeRange') is not None:
            self.start_time_range_shrink = m.get('StartTimeRange')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagSelector') is not None:
            self.tag_selector = m.get('TagSelector')
        if m.get('TaskTypes') is not None:
            self.task_types_shrink = m.get('TaskTypes')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, project_name=None, request_id=None, tasks=None):
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        self.project_name = project_name  # type: str
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: list[TaskInfo]

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = TaskInfo()
                self.tasks.append(temp_model.from_map(k))
        return self


class ListTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTasksResponseBody

    def validate(self):
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


class ListTriggersRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, order=None, project_name=None, sort=None, state=None,
                 tag_selector=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.sort = sort  # type: str
        self.state = state  # type: str
        self.tag_selector = tag_selector  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTriggersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.state is not None:
            result['State'] = self.state
        if self.tag_selector is not None:
            result['TagSelector'] = self.tag_selector
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TagSelector') is not None:
            self.tag_selector = m.get('TagSelector')
        return self


class ListTriggersResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, triggers=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.triggers = triggers  # type: list[DataIngestion]

    def validate(self):
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTriggersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Triggers'] = []
        if self.triggers is not None:
            for k in self.triggers:
                result['Triggers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.triggers = []
        if m.get('Triggers') is not None:
            for k in m.get('Triggers'):
                temp_model = DataIngestion()
                self.triggers.append(temp_model.from_map(k))
        return self


class ListTriggersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTriggersResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTriggersResponse, self).to_map()
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
            temp_model = ListTriggersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFigureClustersRequest(TeaModel):
    def __init__(self, create_time_range=None, custom_labels=None, dataset_name=None, max_results=None,
                 next_token=None, order=None, project_name=None, sort=None, update_time_range=None, with_total_count=None):
        self.create_time_range = create_time_range  # type: TimeRange
        self.custom_labels = custom_labels  # type: str
        self.dataset_name = dataset_name  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.sort = sort  # type: str
        self.update_time_range = update_time_range  # type: TimeRange
        self.with_total_count = with_total_count  # type: bool

    def validate(self):
        if self.create_time_range:
            self.create_time_range.validate()
        if self.update_time_range:
            self.update_time_range.validate()

    def to_map(self):
        _map = super(QueryFigureClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_range is not None:
            result['CreateTimeRange'] = self.create_time_range.to_map()
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.update_time_range is not None:
            result['UpdateTimeRange'] = self.update_time_range.to_map()
        if self.with_total_count is not None:
            result['WithTotalCount'] = self.with_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTimeRange') is not None:
            temp_model = TimeRange()
            self.create_time_range = temp_model.from_map(m['CreateTimeRange'])
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('UpdateTimeRange') is not None:
            temp_model = TimeRange()
            self.update_time_range = temp_model.from_map(m['UpdateTimeRange'])
        if m.get('WithTotalCount') is not None:
            self.with_total_count = m.get('WithTotalCount')
        return self


class QueryFigureClustersShrinkRequest(TeaModel):
    def __init__(self, create_time_range_shrink=None, custom_labels=None, dataset_name=None, max_results=None,
                 next_token=None, order=None, project_name=None, sort=None, update_time_range_shrink=None,
                 with_total_count=None):
        self.create_time_range_shrink = create_time_range_shrink  # type: str
        self.custom_labels = custom_labels  # type: str
        self.dataset_name = dataset_name  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.sort = sort  # type: str
        self.update_time_range_shrink = update_time_range_shrink  # type: str
        self.with_total_count = with_total_count  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFigureClustersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_range_shrink is not None:
            result['CreateTimeRange'] = self.create_time_range_shrink
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.update_time_range_shrink is not None:
            result['UpdateTimeRange'] = self.update_time_range_shrink
        if self.with_total_count is not None:
            result['WithTotalCount'] = self.with_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTimeRange') is not None:
            self.create_time_range_shrink = m.get('CreateTimeRange')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('UpdateTimeRange') is not None:
            self.update_time_range_shrink = m.get('UpdateTimeRange')
        if m.get('WithTotalCount') is not None:
            self.with_total_count = m.get('WithTotalCount')
        return self


class QueryFigureClustersResponseBody(TeaModel):
    def __init__(self, figure_clusters=None, next_token=None, request_id=None, total_count=None):
        self.figure_clusters = figure_clusters  # type: list[FigureCluster]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.figure_clusters:
            for k in self.figure_clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFigureClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FigureClusters'] = []
        if self.figure_clusters is not None:
            for k in self.figure_clusters:
                result['FigureClusters'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.figure_clusters = []
        if m.get('FigureClusters') is not None:
            for k in m.get('FigureClusters'):
                temp_model = FigureCluster()
                self.figure_clusters.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryFigureClustersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFigureClustersResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFigureClustersResponse, self).to_map()
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
            temp_model = QueryFigureClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLocationDateClustersRequest(TeaModel):
    def __init__(self, address=None, create_time_range=None, custom_labels=None, dataset_name=None,
                 location_date_cluster_end_time_range=None, location_date_cluster_levels=None, location_date_cluster_start_time_range=None,
                 max_results=None, next_token=None, object_id=None, order=None, project_name=None, sort=None, title=None,
                 update_time_range=None):
        self.address = address  # type: Address
        self.create_time_range = create_time_range  # type: TimeRange
        self.custom_labels = custom_labels  # type: str
        self.dataset_name = dataset_name  # type: str
        self.location_date_cluster_end_time_range = location_date_cluster_end_time_range  # type: TimeRange
        self.location_date_cluster_levels = location_date_cluster_levels  # type: list[str]
        self.location_date_cluster_start_time_range = location_date_cluster_start_time_range  # type: TimeRange
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.object_id = object_id  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.sort = sort  # type: str
        self.title = title  # type: str
        self.update_time_range = update_time_range  # type: TimeRange

    def validate(self):
        if self.address:
            self.address.validate()
        if self.create_time_range:
            self.create_time_range.validate()
        if self.location_date_cluster_end_time_range:
            self.location_date_cluster_end_time_range.validate()
        if self.location_date_cluster_start_time_range:
            self.location_date_cluster_start_time_range.validate()
        if self.update_time_range:
            self.update_time_range.validate()

    def to_map(self):
        _map = super(QueryLocationDateClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        if self.create_time_range is not None:
            result['CreateTimeRange'] = self.create_time_range.to_map()
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.location_date_cluster_end_time_range is not None:
            result['LocationDateClusterEndTimeRange'] = self.location_date_cluster_end_time_range.to_map()
        if self.location_date_cluster_levels is not None:
            result['LocationDateClusterLevels'] = self.location_date_cluster_levels
        if self.location_date_cluster_start_time_range is not None:
            result['LocationDateClusterStartTimeRange'] = self.location_date_cluster_start_time_range.to_map()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time_range is not None:
            result['UpdateTimeRange'] = self.update_time_range.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = Address()
            self.address = temp_model.from_map(m['Address'])
        if m.get('CreateTimeRange') is not None:
            temp_model = TimeRange()
            self.create_time_range = temp_model.from_map(m['CreateTimeRange'])
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('LocationDateClusterEndTimeRange') is not None:
            temp_model = TimeRange()
            self.location_date_cluster_end_time_range = temp_model.from_map(m['LocationDateClusterEndTimeRange'])
        if m.get('LocationDateClusterLevels') is not None:
            self.location_date_cluster_levels = m.get('LocationDateClusterLevels')
        if m.get('LocationDateClusterStartTimeRange') is not None:
            temp_model = TimeRange()
            self.location_date_cluster_start_time_range = temp_model.from_map(m['LocationDateClusterStartTimeRange'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTimeRange') is not None:
            temp_model = TimeRange()
            self.update_time_range = temp_model.from_map(m['UpdateTimeRange'])
        return self


class QueryLocationDateClustersShrinkRequest(TeaModel):
    def __init__(self, address_shrink=None, create_time_range_shrink=None, custom_labels=None, dataset_name=None,
                 location_date_cluster_end_time_range_shrink=None, location_date_cluster_levels_shrink=None,
                 location_date_cluster_start_time_range_shrink=None, max_results=None, next_token=None, object_id=None, order=None, project_name=None, sort=None,
                 title=None, update_time_range_shrink=None):
        self.address_shrink = address_shrink  # type: str
        self.create_time_range_shrink = create_time_range_shrink  # type: str
        self.custom_labels = custom_labels  # type: str
        self.dataset_name = dataset_name  # type: str
        self.location_date_cluster_end_time_range_shrink = location_date_cluster_end_time_range_shrink  # type: str
        self.location_date_cluster_levels_shrink = location_date_cluster_levels_shrink  # type: str
        self.location_date_cluster_start_time_range_shrink = location_date_cluster_start_time_range_shrink  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.object_id = object_id  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.sort = sort  # type: str
        self.title = title  # type: str
        self.update_time_range_shrink = update_time_range_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryLocationDateClustersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_shrink is not None:
            result['Address'] = self.address_shrink
        if self.create_time_range_shrink is not None:
            result['CreateTimeRange'] = self.create_time_range_shrink
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.location_date_cluster_end_time_range_shrink is not None:
            result['LocationDateClusterEndTimeRange'] = self.location_date_cluster_end_time_range_shrink
        if self.location_date_cluster_levels_shrink is not None:
            result['LocationDateClusterLevels'] = self.location_date_cluster_levels_shrink
        if self.location_date_cluster_start_time_range_shrink is not None:
            result['LocationDateClusterStartTimeRange'] = self.location_date_cluster_start_time_range_shrink
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time_range_shrink is not None:
            result['UpdateTimeRange'] = self.update_time_range_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address_shrink = m.get('Address')
        if m.get('CreateTimeRange') is not None:
            self.create_time_range_shrink = m.get('CreateTimeRange')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('LocationDateClusterEndTimeRange') is not None:
            self.location_date_cluster_end_time_range_shrink = m.get('LocationDateClusterEndTimeRange')
        if m.get('LocationDateClusterLevels') is not None:
            self.location_date_cluster_levels_shrink = m.get('LocationDateClusterLevels')
        if m.get('LocationDateClusterStartTimeRange') is not None:
            self.location_date_cluster_start_time_range_shrink = m.get('LocationDateClusterStartTimeRange')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTimeRange') is not None:
            self.update_time_range_shrink = m.get('UpdateTimeRange')
        return self


class QueryLocationDateClustersResponseBody(TeaModel):
    def __init__(self, location_date_clusters=None, next_token=None, request_id=None):
        self.location_date_clusters = location_date_clusters  # type: list[LocationDateCluster]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.location_date_clusters:
            for k in self.location_date_clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryLocationDateClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LocationDateClusters'] = []
        if self.location_date_clusters is not None:
            for k in self.location_date_clusters:
                result['LocationDateClusters'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.location_date_clusters = []
        if m.get('LocationDateClusters') is not None:
            for k in m.get('LocationDateClusters'):
                temp_model = LocationDateCluster()
                self.location_date_clusters.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryLocationDateClustersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryLocationDateClustersResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryLocationDateClustersResponse, self).to_map()
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
            temp_model = QueryLocationDateClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySimilarImageClustersRequest(TeaModel):
    def __init__(self, custom_labels=None, dataset_name=None, max_results=None, next_token=None, order=None,
                 project_name=None, sort=None):
        self.custom_labels = custom_labels  # type: str
        self.dataset_name = dataset_name  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.sort = sort  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySimilarImageClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class QuerySimilarImageClustersResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, similar_image_clusters=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.similar_image_clusters = similar_image_clusters  # type: list[SimilarImageCluster]

    def validate(self):
        if self.similar_image_clusters:
            for k in self.similar_image_clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySimilarImageClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SimilarImageClusters'] = []
        if self.similar_image_clusters is not None:
            for k in self.similar_image_clusters:
                result['SimilarImageClusters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.similar_image_clusters = []
        if m.get('SimilarImageClusters') is not None:
            for k in m.get('SimilarImageClusters'):
                temp_model = SimilarImageCluster()
                self.similar_image_clusters.append(temp_model.from_map(k))
        return self


class QuerySimilarImageClustersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySimilarImageClustersResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySimilarImageClustersResponse, self).to_map()
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
            temp_model = QuerySimilarImageClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStoriesRequest(TeaModel):
    def __init__(self, create_time_range=None, custom_labels=None, dataset_name=None, figure_cluster_ids=None,
                 max_results=None, next_token=None, object_id=None, order=None, project_name=None, sort=None,
                 story_end_time_range=None, story_name=None, story_start_time_range=None, story_sub_type=None, story_type=None,
                 with_empty_stories=None):
        self.create_time_range = create_time_range  # type: TimeRange
        self.custom_labels = custom_labels  # type: str
        self.dataset_name = dataset_name  # type: str
        self.figure_cluster_ids = figure_cluster_ids  # type: list[str]
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.object_id = object_id  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.sort = sort  # type: str
        self.story_end_time_range = story_end_time_range  # type: TimeRange
        self.story_name = story_name  # type: str
        self.story_start_time_range = story_start_time_range  # type: TimeRange
        self.story_sub_type = story_sub_type  # type: str
        self.story_type = story_type  # type: str
        self.with_empty_stories = with_empty_stories  # type: bool

    def validate(self):
        if self.create_time_range:
            self.create_time_range.validate()
        if self.story_end_time_range:
            self.story_end_time_range.validate()
        if self.story_start_time_range:
            self.story_start_time_range.validate()

    def to_map(self):
        _map = super(QueryStoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_range is not None:
            result['CreateTimeRange'] = self.create_time_range.to_map()
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster_ids is not None:
            result['FigureClusterIds'] = self.figure_cluster_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.story_end_time_range is not None:
            result['StoryEndTimeRange'] = self.story_end_time_range.to_map()
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time_range is not None:
            result['StoryStartTimeRange'] = self.story_start_time_range.to_map()
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.with_empty_stories is not None:
            result['WithEmptyStories'] = self.with_empty_stories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTimeRange') is not None:
            temp_model = TimeRange()
            self.create_time_range = temp_model.from_map(m['CreateTimeRange'])
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureClusterIds') is not None:
            self.figure_cluster_ids = m.get('FigureClusterIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StoryEndTimeRange') is not None:
            temp_model = TimeRange()
            self.story_end_time_range = temp_model.from_map(m['StoryEndTimeRange'])
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTimeRange') is not None:
            temp_model = TimeRange()
            self.story_start_time_range = temp_model.from_map(m['StoryStartTimeRange'])
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('WithEmptyStories') is not None:
            self.with_empty_stories = m.get('WithEmptyStories')
        return self


class QueryStoriesShrinkRequest(TeaModel):
    def __init__(self, create_time_range_shrink=None, custom_labels=None, dataset_name=None,
                 figure_cluster_ids_shrink=None, max_results=None, next_token=None, object_id=None, order=None, project_name=None, sort=None,
                 story_end_time_range_shrink=None, story_name=None, story_start_time_range_shrink=None, story_sub_type=None, story_type=None,
                 with_empty_stories=None):
        self.create_time_range_shrink = create_time_range_shrink  # type: str
        self.custom_labels = custom_labels  # type: str
        self.dataset_name = dataset_name  # type: str
        self.figure_cluster_ids_shrink = figure_cluster_ids_shrink  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.object_id = object_id  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.sort = sort  # type: str
        self.story_end_time_range_shrink = story_end_time_range_shrink  # type: str
        self.story_name = story_name  # type: str
        self.story_start_time_range_shrink = story_start_time_range_shrink  # type: str
        self.story_sub_type = story_sub_type  # type: str
        self.story_type = story_type  # type: str
        self.with_empty_stories = with_empty_stories  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStoriesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_range_shrink is not None:
            result['CreateTimeRange'] = self.create_time_range_shrink
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster_ids_shrink is not None:
            result['FigureClusterIds'] = self.figure_cluster_ids_shrink
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.story_end_time_range_shrink is not None:
            result['StoryEndTimeRange'] = self.story_end_time_range_shrink
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        if self.story_start_time_range_shrink is not None:
            result['StoryStartTimeRange'] = self.story_start_time_range_shrink
        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type
        if self.story_type is not None:
            result['StoryType'] = self.story_type
        if self.with_empty_stories is not None:
            result['WithEmptyStories'] = self.with_empty_stories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTimeRange') is not None:
            self.create_time_range_shrink = m.get('CreateTimeRange')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureClusterIds') is not None:
            self.figure_cluster_ids_shrink = m.get('FigureClusterIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StoryEndTimeRange') is not None:
            self.story_end_time_range_shrink = m.get('StoryEndTimeRange')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        if m.get('StoryStartTimeRange') is not None:
            self.story_start_time_range_shrink = m.get('StoryStartTimeRange')
        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')
        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')
        if m.get('WithEmptyStories') is not None:
            self.with_empty_stories = m.get('WithEmptyStories')
        return self


class QueryStoriesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, stories=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.stories = stories  # type: list[Story]

    def validate(self):
        if self.stories:
            for k in self.stories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryStoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Stories'] = []
        if self.stories is not None:
            for k in self.stories:
                result['Stories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stories = []
        if m.get('Stories') is not None:
            for k in m.get('Stories'):
                temp_model = Story()
                self.stories.append(temp_model.from_map(k))
        return self


class QueryStoriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryStoriesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryStoriesResponse, self).to_map()
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
            temp_model = QueryStoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshWebofficeTokenRequest(TeaModel):
    def __init__(self, access_token=None, credential_config=None, project_name=None, refresh_token=None):
        self.access_token = access_token  # type: str
        self.credential_config = credential_config  # type: CredentialConfig
        self.project_name = project_name  # type: str
        self.refresh_token = refresh_token  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super(RefreshWebofficeTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class RefreshWebofficeTokenShrinkRequest(TeaModel):
    def __init__(self, access_token=None, credential_config_shrink=None, project_name=None, refresh_token=None):
        self.access_token = access_token  # type: str
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.project_name = project_name  # type: str
        self.refresh_token = refresh_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshWebofficeTokenShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class RefreshWebofficeTokenResponseBody(TeaModel):
    def __init__(self, access_token=None, access_token_expired_time=None, refresh_token=None,
                 refresh_token_expired_time=None, request_id=None):
        self.access_token = access_token  # type: str
        self.access_token_expired_time = access_token_expired_time  # type: str
        self.refresh_token = refresh_token  # type: str
        self.refresh_token_expired_time = refresh_token_expired_time  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshWebofficeTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshWebofficeTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefreshWebofficeTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshWebofficeTokenResponse, self).to_map()
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
            temp_model = RefreshWebofficeTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveStoryFilesRequestFiles(TeaModel):
    def __init__(self, uri=None):
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveStoryFilesRequestFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class RemoveStoryFilesRequest(TeaModel):
    def __init__(self, dataset_name=None, files=None, object_id=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.files = files  # type: list[RemoveStoryFilesRequestFiles]
        self.object_id = object_id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RemoveStoryFilesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = RemoveStoryFilesRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class RemoveStoryFilesShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, files_shrink=None, object_id=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.files_shrink = files_shrink  # type: str
        self.object_id = object_id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveStoryFilesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class RemoveStoryFilesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveStoryFilesResponseBody, self).to_map()
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


class RemoveStoryFilesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveStoryFilesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveStoryFilesResponse, self).to_map()
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
            temp_model = RemoveStoryFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeBatchRequest(TeaModel):
    def __init__(self, id=None, project_name=None):
        self.id = id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ResumeBatchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeBatchResponseBody, self).to_map()
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


class ResumeBatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResumeBatchResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeBatchResponse, self).to_map()
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
            temp_model = ResumeBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeTriggerRequest(TeaModel):
    def __init__(self, id=None, project_name=None):
        self.id = id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ResumeTriggerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeTriggerResponseBody, self).to_map()
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


class ResumeTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResumeTriggerResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeTriggerResponse, self).to_map()
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
            temp_model = ResumeTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageFigureClusterRequest(TeaModel):
    def __init__(self, credential_config=None, dataset_name=None, project_name=None, source_uri=None):
        self.credential_config = credential_config  # type: CredentialConfig
        self.dataset_name = dataset_name  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()

    def to_map(self):
        _map = super(SearchImageFigureClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = CredentialConfig()
            self.credential_config = temp_model.from_map(m['CredentialConfig'])
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class SearchImageFigureClusterShrinkRequest(TeaModel):
    def __init__(self, credential_config_shrink=None, dataset_name=None, project_name=None, source_uri=None):
        self.credential_config_shrink = credential_config_shrink  # type: str
        self.dataset_name = dataset_name  # type: str
        self.project_name = project_name  # type: str
        self.source_uri = source_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchImageFigureClusterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')
        return self


class SearchImageFigureClusterResponseBodyClusters(TeaModel):
    def __init__(self, boundary=None, cluster_id=None, similarity=None):
        self.boundary = boundary  # type: Boundary
        self.cluster_id = cluster_id  # type: str
        self.similarity = similarity  # type: float

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        _map = super(SearchImageFigureClusterResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = Boundary()
            self.boundary = temp_model.from_map(m['Boundary'])
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        return self


class SearchImageFigureClusterResponseBody(TeaModel):
    def __init__(self, clusters=None, request_id=None):
        self.clusters = clusters  # type: list[SearchImageFigureClusterResponseBodyClusters]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchImageFigureClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = SearchImageFigureClusterResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchImageFigureClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchImageFigureClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchImageFigureClusterResponse, self).to_map()
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
            temp_model = SearchImageFigureClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SemanticQueryRequest(TeaModel):
    def __init__(self, dataset_name=None, max_results=None, media_types=None, next_token=None, project_name=None,
                 query=None, with_fields=None):
        self.dataset_name = dataset_name  # type: str
        self.max_results = max_results  # type: int
        self.media_types = media_types  # type: list[str]
        self.next_token = next_token  # type: str
        self.project_name = project_name  # type: str
        self.query = query  # type: str
        self.with_fields = with_fields  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SemanticQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.media_types is not None:
            result['MediaTypes'] = self.media_types
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query is not None:
            result['Query'] = self.query
        if self.with_fields is not None:
            result['WithFields'] = self.with_fields
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('MediaTypes') is not None:
            self.media_types = m.get('MediaTypes')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('WithFields') is not None:
            self.with_fields = m.get('WithFields')
        return self


class SemanticQueryShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, max_results=None, media_types_shrink=None, next_token=None,
                 project_name=None, query=None, with_fields_shrink=None):
        self.dataset_name = dataset_name  # type: str
        self.max_results = max_results  # type: int
        self.media_types_shrink = media_types_shrink  # type: str
        self.next_token = next_token  # type: str
        self.project_name = project_name  # type: str
        self.query = query  # type: str
        self.with_fields_shrink = with_fields_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SemanticQueryShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.media_types_shrink is not None:
            result['MediaTypes'] = self.media_types_shrink
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query is not None:
            result['Query'] = self.query
        if self.with_fields_shrink is not None:
            result['WithFields'] = self.with_fields_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('MediaTypes') is not None:
            self.media_types_shrink = m.get('MediaTypes')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('WithFields') is not None:
            self.with_fields_shrink = m.get('WithFields')
        return self


class SemanticQueryResponseBody(TeaModel):
    def __init__(self, files=None, request_id=None):
        self.files = files  # type: list[File]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SemanticQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SemanticQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SemanticQueryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SemanticQueryResponse, self).to_map()
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
            temp_model = SemanticQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SimpleQueryRequestAggregations(TeaModel):
    def __init__(self, field=None, operation=None):
        self.field = field  # type: str
        self.operation = operation  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SimpleQueryRequestAggregations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class SimpleQueryRequest(TeaModel):
    def __init__(self, aggregations=None, dataset_name=None, max_results=None, next_token=None, order=None,
                 project_name=None, query=None, sort=None, with_fields=None, without_total_hits=None):
        self.aggregations = aggregations  # type: list[SimpleQueryRequestAggregations]
        self.dataset_name = dataset_name  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.query = query  # type: SimpleQuery
        self.sort = sort  # type: str
        self.with_fields = with_fields  # type: list[str]
        self.without_total_hits = without_total_hits  # type: bool

    def validate(self):
        if self.aggregations:
            for k in self.aggregations:
                if k:
                    k.validate()
        if self.query:
            self.query.validate()

    def to_map(self):
        _map = super(SimpleQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Aggregations'] = []
        if self.aggregations is not None:
            for k in self.aggregations:
                result['Aggregations'].append(k.to_map() if k else None)
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query is not None:
            result['Query'] = self.query.to_map()
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.with_fields is not None:
            result['WithFields'] = self.with_fields
        if self.without_total_hits is not None:
            result['WithoutTotalHits'] = self.without_total_hits
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.aggregations = []
        if m.get('Aggregations') is not None:
            for k in m.get('Aggregations'):
                temp_model = SimpleQueryRequestAggregations()
                self.aggregations.append(temp_model.from_map(k))
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            temp_model = SimpleQuery()
            self.query = temp_model.from_map(m['Query'])
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('WithFields') is not None:
            self.with_fields = m.get('WithFields')
        if m.get('WithoutTotalHits') is not None:
            self.without_total_hits = m.get('WithoutTotalHits')
        return self


class SimpleQueryShrinkRequest(TeaModel):
    def __init__(self, aggregations_shrink=None, dataset_name=None, max_results=None, next_token=None, order=None,
                 project_name=None, query_shrink=None, sort=None, with_fields_shrink=None, without_total_hits=None):
        self.aggregations_shrink = aggregations_shrink  # type: str
        self.dataset_name = dataset_name  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.order = order  # type: str
        self.project_name = project_name  # type: str
        self.query_shrink = query_shrink  # type: str
        self.sort = sort  # type: str
        self.with_fields_shrink = with_fields_shrink  # type: str
        self.without_total_hits = without_total_hits  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SimpleQueryShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregations_shrink is not None:
            result['Aggregations'] = self.aggregations_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order is not None:
            result['Order'] = self.order
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.query_shrink is not None:
            result['Query'] = self.query_shrink
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.with_fields_shrink is not None:
            result['WithFields'] = self.with_fields_shrink
        if self.without_total_hits is not None:
            result['WithoutTotalHits'] = self.without_total_hits
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aggregations') is not None:
            self.aggregations_shrink = m.get('Aggregations')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Query') is not None:
            self.query_shrink = m.get('Query')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('WithFields') is not None:
            self.with_fields_shrink = m.get('WithFields')
        if m.get('WithoutTotalHits') is not None:
            self.without_total_hits = m.get('WithoutTotalHits')
        return self


class SimpleQueryResponseBodyAggregationsGroups(TeaModel):
    def __init__(self, count=None, value=None):
        self.count = count  # type: long
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SimpleQueryResponseBodyAggregationsGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SimpleQueryResponseBodyAggregations(TeaModel):
    def __init__(self, field=None, groups=None, operation=None, value=None):
        self.field = field  # type: str
        self.groups = groups  # type: list[SimpleQueryResponseBodyAggregationsGroups]
        self.operation = operation  # type: str
        self.value = value  # type: float

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SimpleQueryResponseBodyAggregations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['Field'] = self.field
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = SimpleQueryResponseBodyAggregationsGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SimpleQueryResponseBody(TeaModel):
    def __init__(self, aggregations=None, files=None, next_token=None, request_id=None, total_hits=None):
        self.aggregations = aggregations  # type: list[SimpleQueryResponseBodyAggregations]
        self.files = files  # type: list[File]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_hits = total_hits  # type: long

    def validate(self):
        if self.aggregations:
            for k in self.aggregations:
                if k:
                    k.validate()
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SimpleQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Aggregations'] = []
        if self.aggregations is not None:
            for k in self.aggregations:
                result['Aggregations'].append(k.to_map() if k else None)
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_hits is not None:
            result['TotalHits'] = self.total_hits
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.aggregations = []
        if m.get('Aggregations') is not None:
            for k in m.get('Aggregations'):
                temp_model = SimpleQueryResponseBodyAggregations()
                self.aggregations.append(temp_model.from_map(k))
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalHits') is not None:
            self.total_hits = m.get('TotalHits')
        return self


class SimpleQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SimpleQueryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SimpleQueryResponse, self).to_map()
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
            temp_model = SimpleQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendBatchRequest(TeaModel):
    def __init__(self, id=None, project_name=None):
        self.id = id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuspendBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class SuspendBatchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuspendBatchResponseBody, self).to_map()
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


class SuspendBatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SuspendBatchResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SuspendBatchResponse, self).to_map()
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
            temp_model = SuspendBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendTriggerRequest(TeaModel):
    def __init__(self, id=None, project_name=None):
        self.id = id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuspendTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class SuspendTriggerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuspendTriggerResponseBody, self).to_map()
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


class SuspendTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SuspendTriggerResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SuspendTriggerResponse, self).to_map()
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
            temp_model = SuspendTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBatchRequestActions(TeaModel):
    def __init__(self, name=None, parameters=None):
        self.name = name  # type: str
        self.parameters = parameters  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBatchRequestActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class UpdateBatchRequest(TeaModel):
    def __init__(self, actions=None, id=None, input=None, project_name=None, tags=None):
        self.actions = actions  # type: list[UpdateBatchRequestActions]
        self.id = id  # type: str
        self.input = input  # type: Input
        self.project_name = project_name  # type: str
        self.tags = tags  # type: dict[str, any]

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.input:
            self.input.validate()

    def to_map(self):
        _map = super(UpdateBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = UpdateBatchRequestActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Input') is not None:
            temp_model = Input()
            self.input = temp_model.from_map(m['Input'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class UpdateBatchShrinkRequest(TeaModel):
    def __init__(self, actions_shrink=None, id=None, input_shrink=None, project_name=None, tags_shrink=None):
        self.actions_shrink = actions_shrink  # type: str
        self.id = id  # type: str
        self.input_shrink = input_shrink  # type: str
        self.project_name = project_name  # type: str
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBatchShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions_shrink is not None:
            result['Actions'] = self.actions_shrink
        if self.id is not None:
            result['Id'] = self.id
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions_shrink = m.get('Actions')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class UpdateBatchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBatchResponseBody, self).to_map()
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


class UpdateBatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateBatchResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBatchResponse, self).to_map()
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
            temp_model = UpdateBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDatasetRequest(TeaModel):
    def __init__(self, dataset_max_bind_count=None, dataset_max_entity_count=None, dataset_max_file_count=None,
                 dataset_max_relation_count=None, dataset_max_total_file_size=None, dataset_name=None, description=None, project_name=None,
                 template_id=None):
        self.dataset_max_bind_count = dataset_max_bind_count  # type: long
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        self.dataset_max_total_file_size = dataset_max_total_file_size  # type: long
        self.dataset_name = dataset_name  # type: str
        self.description = description  # type: str
        self.project_name = project_name  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDatasetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateDatasetResponseBody(TeaModel):
    def __init__(self, dataset=None, request_id=None):
        self.dataset = dataset  # type: Dataset
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        _map = super(UpdateDatasetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dataset') is not None:
            temp_model = Dataset()
            self.dataset = temp_model.from_map(m['Dataset'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDatasetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDatasetResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDatasetResponse, self).to_map()
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
            temp_model = UpdateDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFigureClusterRequest(TeaModel):
    def __init__(self, dataset_name=None, figure_cluster=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.figure_cluster = figure_cluster  # type: FigureClusterForReq
        self.project_name = project_name  # type: str

    def validate(self):
        if self.figure_cluster:
            self.figure_cluster.validate()

    def to_map(self):
        _map = super(UpdateFigureClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster is not None:
            result['FigureCluster'] = self.figure_cluster.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureCluster') is not None:
            temp_model = FigureClusterForReq()
            self.figure_cluster = temp_model.from_map(m['FigureCluster'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class UpdateFigureClusterShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, figure_cluster_shrink=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.figure_cluster_shrink = figure_cluster_shrink  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFigureClusterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.figure_cluster_shrink is not None:
            result['FigureCluster'] = self.figure_cluster_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('FigureCluster') is not None:
            self.figure_cluster_shrink = m.get('FigureCluster')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class UpdateFigureClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFigureClusterResponseBody, self).to_map()
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


class UpdateFigureClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFigureClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFigureClusterResponse, self).to_map()
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
            temp_model = UpdateFigureClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFileMetaRequest(TeaModel):
    def __init__(self, dataset_name=None, file=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.file = file  # type: InputFile
        self.project_name = project_name  # type: str

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        _map = super(UpdateFileMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.file is not None:
            result['File'] = self.file.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('File') is not None:
            temp_model = InputFile()
            self.file = temp_model.from_map(m['File'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class UpdateFileMetaShrinkRequest(TeaModel):
    def __init__(self, dataset_name=None, file_shrink=None, project_name=None):
        self.dataset_name = dataset_name  # type: str
        self.file_shrink = file_shrink  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFileMetaShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.file_shrink is not None:
            result['File'] = self.file_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('File') is not None:
            self.file_shrink = m.get('File')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class UpdateFileMetaResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFileMetaResponseBody, self).to_map()
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


class UpdateFileMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFileMetaResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFileMetaResponse, self).to_map()
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
            temp_model = UpdateFileMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLocationDateClusterRequest(TeaModel):
    def __init__(self, custom_id=None, custom_labels=None, dataset_name=None, object_id=None, project_name=None,
                 title=None):
        self.custom_id = custom_id  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]
        self.dataset_name = dataset_name  # type: str
        self.object_id = object_id  # type: str
        self.project_name = project_name  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLocationDateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateLocationDateClusterShrinkRequest(TeaModel):
    def __init__(self, custom_id=None, custom_labels_shrink=None, dataset_name=None, object_id=None,
                 project_name=None, title=None):
        self.custom_id = custom_id  # type: str
        self.custom_labels_shrink = custom_labels_shrink  # type: str
        self.dataset_name = dataset_name  # type: str
        self.object_id = object_id  # type: str
        self.project_name = project_name  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLocationDateClusterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateLocationDateClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLocationDateClusterResponseBody, self).to_map()
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


class UpdateLocationDateClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLocationDateClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLocationDateClusterResponse, self).to_map()
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
            temp_model = UpdateLocationDateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(self, dataset_max_bind_count=None, dataset_max_entity_count=None, dataset_max_file_count=None,
                 dataset_max_relation_count=None, dataset_max_total_file_size=None, description=None, project_max_dataset_count=None,
                 project_name=None, service_role=None, template_id=None):
        self.dataset_max_bind_count = dataset_max_bind_count  # type: long
        self.dataset_max_entity_count = dataset_max_entity_count  # type: long
        self.dataset_max_file_count = dataset_max_file_count  # type: long
        self.dataset_max_relation_count = dataset_max_relation_count  # type: long
        self.dataset_max_total_file_size = dataset_max_total_file_size  # type: long
        self.description = description  # type: str
        self.project_max_dataset_count = project_max_dataset_count  # type: long
        self.project_name = project_name  # type: str
        self.service_role = service_role  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_max_bind_count is not None:
            result['DatasetMaxBindCount'] = self.dataset_max_bind_count
        if self.dataset_max_entity_count is not None:
            result['DatasetMaxEntityCount'] = self.dataset_max_entity_count
        if self.dataset_max_file_count is not None:
            result['DatasetMaxFileCount'] = self.dataset_max_file_count
        if self.dataset_max_relation_count is not None:
            result['DatasetMaxRelationCount'] = self.dataset_max_relation_count
        if self.dataset_max_total_file_size is not None:
            result['DatasetMaxTotalFileSize'] = self.dataset_max_total_file_size
        if self.description is not None:
            result['Description'] = self.description
        if self.project_max_dataset_count is not None:
            result['ProjectMaxDatasetCount'] = self.project_max_dataset_count
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetMaxBindCount') is not None:
            self.dataset_max_bind_count = m.get('DatasetMaxBindCount')
        if m.get('DatasetMaxEntityCount') is not None:
            self.dataset_max_entity_count = m.get('DatasetMaxEntityCount')
        if m.get('DatasetMaxFileCount') is not None:
            self.dataset_max_file_count = m.get('DatasetMaxFileCount')
        if m.get('DatasetMaxRelationCount') is not None:
            self.dataset_max_relation_count = m.get('DatasetMaxRelationCount')
        if m.get('DatasetMaxTotalFileSize') is not None:
            self.dataset_max_total_file_size = m.get('DatasetMaxTotalFileSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectMaxDatasetCount') is not None:
            self.project_max_dataset_count = m.get('ProjectMaxDatasetCount')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(self, project=None, request_id=None):
        self.project = project  # type: Project
        self.request_id = request_id  # type: str

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super(UpdateProjectResponseBody, self).to_map()
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
            temp_model = Project()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateProjectResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProjectResponse, self).to_map()
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
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStoryRequestCover(TeaModel):
    def __init__(self, uri=None):
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStoryRequestCover, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class UpdateStoryRequest(TeaModel):
    def __init__(self, cover=None, custom_id=None, custom_labels=None, dataset_name=None, object_id=None,
                 project_name=None, story_name=None):
        self.cover = cover  # type: UpdateStoryRequestCover
        self.custom_id = custom_id  # type: str
        self.custom_labels = custom_labels  # type: dict[str, any]
        self.dataset_name = dataset_name  # type: str
        self.object_id = object_id  # type: str
        self.project_name = project_name  # type: str
        self.story_name = story_name  # type: str

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super(UpdateStoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cover') is not None:
            temp_model = UpdateStoryRequestCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        return self


class UpdateStoryShrinkRequest(TeaModel):
    def __init__(self, cover_shrink=None, custom_id=None, custom_labels_shrink=None, dataset_name=None,
                 object_id=None, project_name=None, story_name=None):
        self.cover_shrink = cover_shrink  # type: str
        self.custom_id = custom_id  # type: str
        self.custom_labels_shrink = custom_labels_shrink  # type: str
        self.dataset_name = dataset_name  # type: str
        self.object_id = object_id  # type: str
        self.project_name = project_name  # type: str
        self.story_name = story_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStoryShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_shrink is not None:
            result['Cover'] = self.cover_shrink
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id
        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.story_name is not None:
            result['StoryName'] = self.story_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cover') is not None:
            self.cover_shrink = m.get('Cover')
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')
        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')
        return self


class UpdateStoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateStoryResponseBody, self).to_map()
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


class UpdateStoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateStoryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateStoryResponse, self).to_map()
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
            temp_model = UpdateStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTriggerRequestActions(TeaModel):
    def __init__(self, name=None, parameters=None):
        self.name = name  # type: str
        self.parameters = parameters  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTriggerRequestActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class UpdateTriggerRequest(TeaModel):
    def __init__(self, actions=None, id=None, input=None, project_name=None, tags=None):
        self.actions = actions  # type: list[UpdateTriggerRequestActions]
        self.id = id  # type: str
        self.input = input  # type: Input
        self.project_name = project_name  # type: str
        self.tags = tags  # type: dict[str, any]

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.input:
            self.input.validate()

    def to_map(self):
        _map = super(UpdateTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = UpdateTriggerRequestActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Input') is not None:
            temp_model = Input()
            self.input = temp_model.from_map(m['Input'])
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class UpdateTriggerShrinkRequest(TeaModel):
    def __init__(self, actions_shrink=None, id=None, input_shrink=None, project_name=None, tags_shrink=None):
        self.actions_shrink = actions_shrink  # type: str
        self.id = id  # type: str
        self.input_shrink = input_shrink  # type: str
        self.project_name = project_name  # type: str
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTriggerShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions_shrink is not None:
            result['Actions'] = self.actions_shrink
        if self.id is not None:
            result['Id'] = self.id
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions_shrink = m.get('Actions')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class UpdateTriggerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTriggerResponseBody, self).to_map()
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


class UpdateTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTriggerResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTriggerResponse, self).to_map()
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
            temp_model = UpdateTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


