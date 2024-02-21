# Auto generated from modo_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-02-21T16:56:00
# Schema: modo-schema
#
# id: https://w3id.org/sdsc-ordes/modo-schema
# description: Metadata schema for the SMOC Multi-Omics Digital Object
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Datetime, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EDAM = CurieNamespace('EDAM', 'http://edamontology.org/')
FG = CurieNamespace('FG', 'https://w3id.org/fair-genomes/ontology/')
GENO = CurieNamespace('GENO', 'http://purl.obolibrary.org/obo/GENO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
BIOSCHEMAS = CurieNamespace('bioschemas', 'https://bioschemas.org/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MODO = CurieNamespace('modo', 'https://w3id.org/sdsc-ordes/modo-schema/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SPHN = CurieNamespace('sphn', 'https://biomedit.ch/rdf/sphn-schema/sphn#')
DEFAULT_ = MODO


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class MODOId(NamedThingId):
    pass


class AssayId(NamedThingId):
    pass


class SampleId(NamedThingId):
    pass


class DataEntityId(NamedThingId):
    pass


class ReferenceGenomeId(NamedThingId):
    pass


class ReferenceSequenceId(NamedThingId):
    pass


class AlignmentSetId(DataEntityId):
    pass


class VariantSetId(DataEntityId):
    pass


class ArrayId(DataEntityId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MODO.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class MODO(NamedThing):
    """
    Represents the Multi-Omics Digital Object. It encapsulates omics and other datasets and their metadata.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MODO["MODO"]
    class_class_curie: ClassVar[str] = "modo:MODO"
    class_name: ClassVar[str] = "MODO"
    class_model_uri: ClassVar[URIRef] = MODO.MODO

    id: Union[str, MODOId] = None
    creation_date: Union[str, XSDDateTime] = None
    last_update_date: Union[str, XSDDateTime] = None
    has_assay: Optional[Union[Union[str, AssayId], List[Union[str, AssayId]]]] = empty_list()
    source_uri: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MODOId):
            self.id = MODOId(self.id)

        if self._is_empty(self.creation_date):
            self.MissingRequiredField("creation_date")
        if not isinstance(self.creation_date, XSDDateTime):
            self.creation_date = XSDDateTime(self.creation_date)

        if self._is_empty(self.last_update_date):
            self.MissingRequiredField("last_update_date")
        if not isinstance(self.last_update_date, XSDDateTime):
            self.last_update_date = XSDDateTime(self.last_update_date)

        if not isinstance(self.has_assay, list):
            self.has_assay = [self.has_assay] if self.has_assay is not None else []
        self.has_assay = [v if isinstance(v, AssayId) else AssayId(v) for v in self.has_assay]

        if self.source_uri is not None and not isinstance(self.source_uri, URI):
            self.source_uri = URI(self.source_uri)

        super().__post_init__(**kwargs)


@dataclass
class Assay(NamedThing):
    """
    A coordinated set of actions designed to generate data from samples.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MODO["Assay"]
    class_class_curie: ClassVar[str] = "modo:Assay"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = MODO.Assay

    id: Union[str, AssayId] = None
    omics_type: Union[Union[str, "OmicsType"], List[Union[str, "OmicsType"]]] = None
    has_sample: Optional[Union[Union[str, SampleId], List[Union[str, SampleId]]]] = empty_list()
    has_data: Optional[Union[Union[str, DataEntityId], List[Union[str, DataEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssayId):
            self.id = AssayId(self.id)

        if self._is_empty(self.omics_type):
            self.MissingRequiredField("omics_type")
        if not isinstance(self.omics_type, list):
            self.omics_type = [self.omics_type] if self.omics_type is not None else []
        self.omics_type = [v if isinstance(v, OmicsType) else OmicsType(v) for v in self.omics_type]

        if not isinstance(self.has_sample, list):
            self.has_sample = [self.has_sample] if self.has_sample is not None else []
        self.has_sample = [v if isinstance(v, SampleId) else SampleId(v) for v in self.has_sample]

        if not isinstance(self.has_data, list):
            self.has_data = [self.has_data] if self.has_data is not None else []
        self.has_data = [v if isinstance(v, DataEntityId) else DataEntityId(v) for v in self.has_data]

        super().__post_init__(**kwargs)


@dataclass
class Sample(NamedThing):
    """
    A biological sample used in assays. Examples include a whole organism, tissue or cell line.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MODO["Sample"]
    class_class_curie: ClassVar[str] = "modo:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = MODO.Sample

    id: Union[str, SampleId] = None
    cell_type: Optional[str] = None
    source_material: Optional[str] = None
    sex: Optional[Union[str, "Sex"]] = None
    taxon_id: Optional[Union[int, List[int]]] = empty_list()
    collector: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self.cell_type is not None and not isinstance(self.cell_type, str):
            self.cell_type = str(self.cell_type)

        if self.source_material is not None and not isinstance(self.source_material, str):
            self.source_material = str(self.source_material)

        if self.sex is not None and not isinstance(self.sex, Sex):
            self.sex = Sex(self.sex)

        if not isinstance(self.taxon_id, list):
            self.taxon_id = [self.taxon_id] if self.taxon_id is not None else []
        self.taxon_id = [v if isinstance(v, int) else int(v) for v in self.taxon_id]

        if not isinstance(self.collector, list):
            self.collector = [self.collector] if self.collector is not None else []
        self.collector = [v if isinstance(v, str) else str(v) for v in self.collector]

        super().__post_init__(**kwargs)


@dataclass
class DataEntity(NamedThing):
    """
    An entity containing data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MODO["DataEntity"]
    class_class_curie: ClassVar[str] = "modo:DataEntity"
    class_name: ClassVar[str] = "DataEntity"
    class_model_uri: ClassVar[URIRef] = MODO.DataEntity

    id: Union[str, DataEntityId] = None
    data_path: str = None
    data_format: Union[str, "DataFormat"] = None
    has_sample: Optional[Union[Union[str, SampleId], List[Union[str, SampleId]]]] = empty_list()
    has_reference: Optional[Union[Union[str, ReferenceGenomeId], List[Union[str, ReferenceGenomeId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataEntityId):
            self.id = DataEntityId(self.id)

        if self._is_empty(self.data_path):
            self.MissingRequiredField("data_path")
        if not isinstance(self.data_path, str):
            self.data_path = str(self.data_path)

        if self._is_empty(self.data_format):
            self.MissingRequiredField("data_format")
        if not isinstance(self.data_format, DataFormat):
            self.data_format = DataFormat(self.data_format)

        if not isinstance(self.has_sample, list):
            self.has_sample = [self.has_sample] if self.has_sample is not None else []
        self.has_sample = [v if isinstance(v, SampleId) else SampleId(v) for v in self.has_sample]

        if not isinstance(self.has_reference, list):
            self.has_reference = [self.has_reference] if self.has_reference is not None else []
        self.has_reference = [v if isinstance(v, ReferenceGenomeId) else ReferenceGenomeId(v) for v in self.has_reference]

        super().__post_init__(**kwargs)


@dataclass
class ReferenceGenome(NamedThing):
    """
    Reference assembly of a given genome, consisting of a collection of congiguous sequences (contigs).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MODO["ReferenceGenome"]
    class_class_curie: ClassVar[str] = "modo:ReferenceGenome"
    class_name: ClassVar[str] = "ReferenceGenome"
    class_model_uri: ClassVar[URIRef] = MODO.ReferenceGenome

    id: Union[str, ReferenceGenomeId] = None
    data_path: str = None
    has_sequence: Optional[Union[Union[str, ReferenceSequenceId], List[Union[str, ReferenceSequenceId]]]] = empty_list()
    taxon_id: Optional[Union[int, List[int]]] = empty_list()
    source_uri: Optional[Union[str, URI]] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReferenceGenomeId):
            self.id = ReferenceGenomeId(self.id)

        if self._is_empty(self.data_path):
            self.MissingRequiredField("data_path")
        if not isinstance(self.data_path, str):
            self.data_path = str(self.data_path)

        if not isinstance(self.has_sequence, list):
            self.has_sequence = [self.has_sequence] if self.has_sequence is not None else []
        self.has_sequence = [v if isinstance(v, ReferenceSequenceId) else ReferenceSequenceId(v) for v in self.has_sequence]

        if not isinstance(self.taxon_id, list):
            self.taxon_id = [self.taxon_id] if self.taxon_id is not None else []
        self.taxon_id = [v if isinstance(v, int) else int(v) for v in self.taxon_id]

        if self.source_uri is not None and not isinstance(self.source_uri, URI):
            self.source_uri = URI(self.source_uri)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class ReferenceSequence(NamedThing):
    """
    A contiguous sequence of DNA part of a reference coordinate system (genome assembly).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MODO["ReferenceSequence"]
    class_class_curie: ClassVar[str] = "modo:ReferenceSequence"
    class_name: ClassVar[str] = "ReferenceSequence"
    class_model_uri: ClassVar[URIRef] = MODO.ReferenceSequence

    id: Union[str, ReferenceSequenceId] = None
    sequence_md5: Optional[str] = None
    source_uri: Optional[Union[str, URI]] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReferenceSequenceId):
            self.id = ReferenceSequenceId(self.id)

        if self.sequence_md5 is not None and not isinstance(self.sequence_md5, str):
            self.sequence_md5 = str(self.sequence_md5)

        if self.source_uri is not None and not isinstance(self.source_uri, URI):
            self.source_uri = URI(self.source_uri)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class AlignmentSet(DataEntity):
    """
    A data entity consisting of genomic intervals aligned to a reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MODO["AlignmentSet"]
    class_class_curie: ClassVar[str] = "modo:AlignmentSet"
    class_name: ClassVar[str] = "AlignmentSet"
    class_model_uri: ClassVar[URIRef] = MODO.AlignmentSet

    id: Union[str, AlignmentSetId] = None
    data_path: str = None
    data_format: Union[str, "DataFormat"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlignmentSetId):
            self.id = AlignmentSetId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class VariantSet(DataEntity):
    """
    A data entity consisting of genomic variants relative to a reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MODO["VariantSet"]
    class_class_curie: ClassVar[str] = "modo:VariantSet"
    class_name: ClassVar[str] = "VariantSet"
    class_model_uri: ClassVar[URIRef] = MODO.VariantSet

    id: Union[str, VariantSetId] = None
    data_path: str = None
    data_format: Union[str, "DataFormat"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantSetId):
            self.id = VariantSetId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Array(DataEntity):
    """
    Data entity consisting of an N-dimensional array.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MODO["Array"]
    class_class_curie: ClassVar[str] = "modo:Array"
    class_name: ClassVar[str] = "Array"
    class_model_uri: ClassVar[URIRef] = MODO.Array

    id: Union[str, ArrayId] = None
    data_path: str = None
    data_format: Union[str, "DataFormat"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArrayId):
            self.id = ArrayId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MODOCollection(YAMLRoot):
    """
    A holder for Multi-Omics Digital Objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MODO["MODOCollection"]
    class_class_curie: ClassVar[str] = "modo:MODOCollection"
    class_name: ClassVar[str] = "MODOCollection"
    class_model_uri: ClassVar[URIRef] = MODO.MODOCollection

    entries: Optional[Union[Dict[Union[str, MODOId], Union[dict, MODO]], List[Union[dict, MODO]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=MODO, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class Sex(EnumDefinitionImpl):

    Male = PermissibleValue(
        text="Male",
        description="The male sex.")
    Female = PermissibleValue(
        text="Female",
        description="The female sex.")

    _defn = EnumDefinition(
        name="Sex",
    )

class OmicsType(EnumDefinitionImpl):

    GENOMICS = PermissibleValue(
        text="GENOMICS",
        description="The study of the structure, function, expression, evolution, mapping and editing of genomes.",
        meaning=NCIT["C84343"])
    TRANSCRIPTOMICS = PermissibleValue(
        text="TRANSCRIPTOMICS",
        description="The study of the complete set of RNA transcripts that are produced by the genome.",
        meaning=NCIT["C153189"])
    METABOLOMICS = PermissibleValue(
        text="METABOLOMICS",
        description="The study of biological metabolic profiles.",
        meaning=NCIT["C49019"])
    PROTEOMICS = PermissibleValue(
        text="PROTEOMICS",
        description="The global analysis of cellular proteins.",
        meaning=NCIT["C20085"])

    _defn = EnumDefinition(
        name="OmicsType",
    )

class DataFormat(EnumDefinitionImpl):

    CRAM = PermissibleValue(
        text="CRAM",
        description="Referenced-based compression of alignment format.",
        meaning=EDAM["format_3462"])
    FASTQ = PermissibleValue(
        text="FASTQ",
        description="FASTQ short read format with sequence and any type of quality scores.",
        meaning=EDAM["format_1930"])
    Zarr = PermissibleValue(
        text="Zarr",
        description="Chunked, compressed N-dimensional arrays.",
        meaning=EDAM["format_3915"])
    FASTA = PermissibleValue(
        text="FASTA",
        description="FASTA sequence format including NCBI-style IDs.",
        meaning=EDAM["format_1929"])

    _defn = EnumDefinition(
        name="DataFormat",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MODO.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MODO.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MODO.description, domain=None, range=Optional[str])

slots.has_part = Slot(uri=SCHEMA.hasPart, name="has_part", curie=SCHEMA.curie('hasPart'),
                   model_uri=MODO.has_part, domain=None, range=Optional[Union[str, List[str]]])

slots.creation_date = Slot(uri=MODO.creation_date, name="creation_date", curie=MODO.curie('creation_date'),
                   model_uri=MODO.creation_date, domain=None, range=Union[str, XSDDateTime])

slots.last_update_date = Slot(uri=MODO.last_update_date, name="last_update_date", curie=MODO.curie('last_update_date'),
                   model_uri=MODO.last_update_date, domain=None, range=Union[str, XSDDateTime])

slots.omics_type = Slot(uri=MODO.omics_type, name="omics_type", curie=MODO.curie('omics_type'),
                   model_uri=MODO.omics_type, domain=None, range=Union[Union[str, "OmicsType"], List[Union[str, "OmicsType"]]])

slots.has_assay = Slot(uri=MODO.has_assay, name="has_assay", curie=MODO.curie('has_assay'),
                   model_uri=MODO.has_assay, domain=None, range=Optional[Union[Union[str, AssayId], List[Union[str, AssayId]]]])

slots.has_sample = Slot(uri=MODO.has_sample, name="has_sample", curie=MODO.curie('has_sample'),
                   model_uri=MODO.has_sample, domain=None, range=Optional[Union[Union[str, SampleId], List[Union[str, SampleId]]]])

slots.has_data = Slot(uri=MODO.has_data, name="has_data", curie=MODO.curie('has_data'),
                   model_uri=MODO.has_data, domain=None, range=Optional[Union[Union[str, DataEntityId], List[Union[str, DataEntityId]]]])

slots.has_sequence = Slot(uri=MODO.has_sequence, name="has_sequence", curie=MODO.curie('has_sequence'),
                   model_uri=MODO.has_sequence, domain=None, range=Optional[Union[Union[str, ReferenceSequenceId], List[Union[str, ReferenceSequenceId]]]])

slots.has_reference = Slot(uri=MODO.has_reference, name="has_reference", curie=MODO.curie('has_reference'),
                   model_uri=MODO.has_reference, domain=None, range=Optional[Union[Union[str, ReferenceGenomeId], List[Union[str, ReferenceGenomeId]]]])

slots.data_format = Slot(uri=MODO.data_format, name="data_format", curie=MODO.curie('data_format'),
                   model_uri=MODO.data_format, domain=None, range=Union[str, "DataFormat"])

slots.taxon_id = Slot(uri=MODO.taxon_id, name="taxon_id", curie=MODO.curie('taxon_id'),
                   model_uri=MODO.taxon_id, domain=None, range=Optional[Union[int, List[int]]])

slots.collector = Slot(uri=MODO.collector, name="collector", curie=MODO.curie('collector'),
                   model_uri=MODO.collector, domain=None, range=Optional[Union[str, List[str]]])

slots.data_path = Slot(uri=MODO.data_path, name="data_path", curie=MODO.curie('data_path'),
                   model_uri=MODO.data_path, domain=None, range=str)

slots.sequence_md5 = Slot(uri=MODO.sequence_md5, name="sequence_md5", curie=MODO.curie('sequence_md5'),
                   model_uri=MODO.sequence_md5, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{32}$'))

slots.source_uri = Slot(uri=MODO.source_uri, name="source_uri", curie=MODO.curie('source_uri'),
                   model_uri=MODO.source_uri, domain=None, range=Optional[Union[str, URI]])

slots.version = Slot(uri=MODO.version, name="version", curie=MODO.curie('version'),
                   model_uri=MODO.version, domain=None, range=Optional[str])

slots.cell_type = Slot(uri=MODO.cell_type, name="cell_type", curie=MODO.curie('cell_type'),
                   model_uri=MODO.cell_type, domain=None, range=Optional[str])

slots.source_material = Slot(uri=MODO.source_material, name="source_material", curie=MODO.curie('source_material'),
                   model_uri=MODO.source_material, domain=None, range=Optional[str])

slots.sex = Slot(uri=MODO.sex, name="sex", curie=MODO.curie('sex'),
                   model_uri=MODO.sex, domain=None, range=Optional[Union[str, "Sex"]])

slots.mODOCollection__entries = Slot(uri=MODO.entries, name="mODOCollection__entries", curie=MODO.curie('entries'),
                   model_uri=MODO.mODOCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, MODOId], Union[dict, MODO]], List[Union[dict, MODO]]]])