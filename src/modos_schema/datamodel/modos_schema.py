from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'modos',
     'default_range': 'string',
     'description': 'Metadata schema for the SMOC Multi-Omics Digital Object '
                    'System',
     'id': 'https://w3id.org/sdsc-ordes/modos-schema',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'modos-schema',
     'prefixes': {'CL': {'prefix_prefix': 'CL',
                         'prefix_reference': 'https://bioregistry.io/reference/cl:/'},
                  'EDAM': {'prefix_prefix': 'EDAM',
                           'prefix_reference': 'http://edamontology.org/'},
                  'FG': {'prefix_prefix': 'FG',
                         'prefix_reference': 'https://w3id.org/fair-genomes/ontology/'},
                  'GENO': {'prefix_prefix': 'GENO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/GENO_'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'bioregistry': {'prefix_prefix': 'bioregistry',
                                  'prefix_reference': 'https://bioregistry.io/registry/'},
                  'bioschemas': {'prefix_prefix': 'bioschemas',
                                 'prefix_reference': 'https://bioschemas.org/'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'https://example.org/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'modos': {'prefix_prefix': 'modos',
                            'prefix_reference': 'https://w3id.org/sdsc-ordes/modos-schema/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'sphn': {'prefix_prefix': 'sphn',
                           'prefix_reference': 'https://biomedit.ch/rdf/sphn-schema/sphn#'}},
     'see_also': ['https://sdsc-ordes.github.io/modos-schema'],
     'source_file': 'src/modos_schema/schema/modos_schema.yaml',
     'title': 'modos-schema'} )

class Sex(str, Enum):
    # The male sex.
    Male = "Male"
    # The female sex.
    Female = "Female"


class OmicsType(str, Enum):
    # The study of the structure, function, expression, evolution, mapping and editing of genomes.
    GENOMICS = "GENOMICS"
    # The study of the complete set of RNA transcripts that are produced by the genome.
    TRANSCRIPTOMICS = "TRANSCRIPTOMICS"
    # The study of biological metabolic profiles.
    METABOLOMICS = "METABOLOMICS"
    # The global analysis of cellular proteins.
    PROTEOMICS = "PROTEOMICS"


class DataFormat(str, Enum):
    # Referenced-based compression of alignment format.
    CRAM = "CRAM"
    # FASTQ short read format with sequence and any type of quality scores.
    FASTQ = "FASTQ"
    # Chunked, compressed N-dimensional arrays.
    Zarr = "Zarr"
    # FASTA sequence format including NCBI-style IDs.
    FASTA = "FASTA"
    # Variant call format for sequence variation.
    VCF = "VCF"
    # Binary call format, for efficient storage of sequence variation.
    BCF = "BCF"
    # tab-delimited format for mass spectrometry-based proteomics and metabolomics results.
    mzTab = "mzTab"
    # column-oriented format for efficient storage and retrieval.
    parquet = "parquet"



class NamedThing(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Thing',
         'from_schema': 'https://w3id.org/sdsc-ordes/modos-schema'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })


class MODO(NamedThing):
    """
    Represents the Multi-Omics Digital Object. It encapsulates omics and other datasets and their metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sdsc-ordes/modos-schema'})

    creation_date: datetime  = Field(..., description="""The date on which something was created.""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['MODO']} })
    has_assay: Optional[List[str]] = Field(None, description="""An assay that was performed as part of a given thing.""", json_schema_extra = { "linkml_meta": {'alias': 'has_assay', 'domain_of': ['MODO'], 'is_a': 'has_part'} })
    last_update_date: datetime  = Field(..., description="""The date on which the thing was last modified.""", json_schema_extra = { "linkml_meta": {'alias': 'last_update_date', 'domain_of': ['MODO']} })
    source_uri: Optional[str] = Field(None, description="""The URI from which a resource or dataset was obtained.""", json_schema_extra = { "linkml_meta": {'alias': 'source_uri',
         'domain_of': ['MODO', 'ReferenceGenome', 'ReferenceSequence']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })


class Assay(NamedThing):
    """
    A coordinated set of actions designed to generate data from samples.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sdsc-ordes/modos-schema',
         'see_also': ['NCIT:C42790', 'sphn:Assay']})

    has_sample: Optional[List[str]] = Field(None, description="""Biological sample included or described by a given thing.""", json_schema_extra = { "linkml_meta": {'alias': 'has_sample',
         'domain_of': ['Assay', 'DataEntity'],
         'is_a': 'has_part'} })
    has_data: Optional[List[str]] = Field(None, description="""Data entity included in a given collection.""", json_schema_extra = { "linkml_meta": {'alias': 'has_data', 'domain_of': ['Assay'], 'is_a': 'has_part'} })
    omics_type: List[OmicsType] = Field(..., description="""The type of omics considered.""", json_schema_extra = { "linkml_meta": {'alias': 'omics_type', 'domain_of': ['Assay']} })
    sample_processing: Optional[List[str]] = Field(None, description="""Codes describing sample processing, preparation or handling steps.
The order of the codes should reflect the order in which the steps were performed.
Should be codes from [MSIO](https://bioregistry.io/registry/msio) or [OBI](https://obofoundry.org/ontology/obi.html)].
""", json_schema_extra = { "linkml_meta": {'alias': 'sample_processing',
         'domain_of': ['Assay'],
         'list_elements_ordered': True} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })


class Sample(NamedThing):
    """
    A biological sample used in assays. Examples include a whole organism, tissue or cell line.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sdsc-ordes/modos-schema',
         'see_also': ['bioschemas:Sample']})

    cell_type: Optional[str] = Field(None, description="""The cell type of the sample, if applicable.
Should be a cell type code URI from the cell ontology.
See: [https://bioregistry.io/registry/cl](https://bioregistry.io/registry/cl)
""", json_schema_extra = { "linkml_meta": {'alias': 'cell_type', 'domain_of': ['Sample']} })
    source_material: Optional[str] = Field(None, description="""The biological source from which the sample was isolated (tissue, organ).
Should be a code URI from the [UBERON](https://bioregistry.io/registry/uberon) ontology or [fairgenomes biospecimen types](https://raw.githubusercontent.com/fairgenomes/fairgenomes-semantic-model/refs/tags/v1.2/generated/ontology/fair-genomes-biospecimentypes.ttl).
""", json_schema_extra = { "linkml_meta": {'alias': 'source_material', 'domain_of': ['Sample']} })
    sex: Optional[Sex] = Field(None, description="""The biological sex of a sample.""", json_schema_extra = { "linkml_meta": {'alias': 'sex', 'domain_of': ['Sample']} })
    taxon_id: Optional[List[str]] = Field(None, description="""The NCBI taxon code from [ncbitaxon](https://obofoundry.org/ontology/ncbitaxon.html) describing the taxonomic range of a sample.
""", json_schema_extra = { "linkml_meta": {'alias': 'taxon_id', 'domain_of': ['Sample', 'ReferenceGenome']} })
    collector: Optional[List[str]] = Field(None, description="""The organization responsible for collecting a given sample.""", json_schema_extra = { "linkml_meta": {'alias': 'collector', 'domain_of': ['Sample']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })


class DataEntity(NamedThing):
    """
    An entity containing data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sdsc-ordes/modos-schema'})

    data_path: str = Field(..., description="""The path to access a resource, on a network or local filesystem. Can be a path relative to the root of the digital object, a URL, or an absolute path.""", json_schema_extra = { "linkml_meta": {'alias': 'data_path',
         'domain_of': ['DataEntity', 'ReferenceGenome'],
         'examples': [{'value': 's3://example-bucket/path/to/data'},
                      {'value': 'relative/file/path'},
                      {'value': 'file:///absolute/file/path'}]} })
    data_format: DataFormat = Field(..., description="""Data/file format associated with a data entity.""", json_schema_extra = { "linkml_meta": {'alias': 'data_format', 'domain_of': ['DataEntity']} })
    derived_from: Optional[List[str]] = Field(None, description="""The source data from which some new data was derived.""", json_schema_extra = { "linkml_meta": {'alias': 'derived_from', 'domain_of': ['DataEntity']} })
    has_sample: Optional[List[str]] = Field(None, description="""Biological sample included or described by a given thing.""", json_schema_extra = { "linkml_meta": {'alias': 'has_sample',
         'domain_of': ['Assay', 'DataEntity'],
         'is_a': 'has_part'} })
    has_reference: Optional[List[str]] = Field(None, description="""Specifies the reference coordinate system used by an omics dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'has_reference', 'domain_of': ['DataEntity'], 'is_a': 'has_part'} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })


class ReferenceGenome(NamedThing):
    """
    Reference assembly of a given genome, consisting of a collection of congiguous sequences (contigs).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sdsc-ordes/modos-schema',
         'see_also': ['GENO:0000914']})

    data_path: str = Field(..., description="""The path to access a resource, on a network or local filesystem. Can be a path relative to the root of the digital object, a URL, or an absolute path.""", json_schema_extra = { "linkml_meta": {'alias': 'data_path',
         'domain_of': ['DataEntity', 'ReferenceGenome'],
         'examples': [{'value': 's3://example-bucket/path/to/data'},
                      {'value': 'relative/file/path'},
                      {'value': 'file:///absolute/file/path'}]} })
    has_sequence: Optional[List[str]] = Field(None, description="""Denotes that a sequence belongs to a collection (e.g. a reference genome).""", json_schema_extra = { "linkml_meta": {'alias': 'has_sequence', 'domain_of': ['ReferenceGenome'], 'is_a': 'has_part'} })
    taxon_id: Optional[List[str]] = Field(None, description="""The NCBI taxon code from [ncbitaxon](https://obofoundry.org/ontology/ncbitaxon.html) describing the taxonomic range of a sample.
""", json_schema_extra = { "linkml_meta": {'alias': 'taxon_id', 'domain_of': ['Sample', 'ReferenceGenome']} })
    source_uri: Optional[str] = Field(None, description="""The URI from which a resource or dataset was obtained.""", json_schema_extra = { "linkml_meta": {'alias': 'source_uri',
         'domain_of': ['MODO', 'ReferenceGenome', 'ReferenceSequence']} })
    version: Optional[str] = Field(None, description="""A string specifying the release or version of a software or resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['ReferenceGenome', 'ReferenceSequence']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })


class ReferenceSequence(NamedThing):
    """
    A contiguous sequence of DNA part of a reference coordinate system (genome assembly).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sdsc-ordes/modos-schema',
         'see_also': ['GENO:0000017']})

    sequence_md5: Optional[str] = Field(None, description="""The pre-computed hash uniquely representing a biological sequence. Calculated as the MD5 of the upper-case sequence excluding all whitespace characters (this is equivalent to SQ:M5 in SAM).""", json_schema_extra = { "linkml_meta": {'alias': 'sequence_md5', 'domain_of': ['ReferenceSequence']} })
    source_uri: Optional[str] = Field(None, description="""The URI from which a resource or dataset was obtained.""", json_schema_extra = { "linkml_meta": {'alias': 'source_uri',
         'domain_of': ['MODO', 'ReferenceGenome', 'ReferenceSequence']} })
    version: Optional[str] = Field(None, description="""A string specifying the release or version of a software or resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['ReferenceGenome', 'ReferenceSequence']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })

    @field_validator('sequence_md5')
    def pattern_sequence_md5(cls, v):
        pattern=re.compile(r"^[a-f0-9]{32}$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid sequence_md5 format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid sequence_md5 format: {v}")
        return v


class AlignmentSet(DataEntity):
    """
    A data entity consisting of genomic intervals aligned to a reference.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sdsc-ordes/modos-schema'})

    data_path: str = Field(..., description="""The path to access a resource, on a network or local filesystem. Can be a path relative to the root of the digital object, a URL, or an absolute path.""", json_schema_extra = { "linkml_meta": {'alias': 'data_path',
         'domain_of': ['DataEntity', 'ReferenceGenome'],
         'examples': [{'value': 's3://example-bucket/path/to/data'},
                      {'value': 'relative/file/path'},
                      {'value': 'file:///absolute/file/path'}]} })
    data_format: DataFormat = Field(..., description="""Data/file format associated with a data entity.""", json_schema_extra = { "linkml_meta": {'alias': 'data_format', 'domain_of': ['DataEntity']} })
    derived_from: Optional[List[str]] = Field(None, description="""The source data from which some new data was derived.""", json_schema_extra = { "linkml_meta": {'alias': 'derived_from', 'domain_of': ['DataEntity']} })
    has_sample: Optional[List[str]] = Field(None, description="""Biological sample included or described by a given thing.""", json_schema_extra = { "linkml_meta": {'alias': 'has_sample',
         'domain_of': ['Assay', 'DataEntity'],
         'is_a': 'has_part'} })
    has_reference: Optional[List[str]] = Field(None, description="""Specifies the reference coordinate system used by an omics dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'has_reference', 'domain_of': ['DataEntity'], 'is_a': 'has_part'} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })


class VariantSet(DataEntity):
    """
    A data entity consisting of genomic variants relative to a reference.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sdsc-ordes/modos-schema'})

    data_path: str = Field(..., description="""The path to access a resource, on a network or local filesystem. Can be a path relative to the root of the digital object, a URL, or an absolute path.""", json_schema_extra = { "linkml_meta": {'alias': 'data_path',
         'domain_of': ['DataEntity', 'ReferenceGenome'],
         'examples': [{'value': 's3://example-bucket/path/to/data'},
                      {'value': 'relative/file/path'},
                      {'value': 'file:///absolute/file/path'}]} })
    data_format: DataFormat = Field(..., description="""Data/file format associated with a data entity.""", json_schema_extra = { "linkml_meta": {'alias': 'data_format', 'domain_of': ['DataEntity']} })
    derived_from: Optional[List[str]] = Field(None, description="""The source data from which some new data was derived.""", json_schema_extra = { "linkml_meta": {'alias': 'derived_from', 'domain_of': ['DataEntity']} })
    has_sample: Optional[List[str]] = Field(None, description="""Biological sample included or described by a given thing.""", json_schema_extra = { "linkml_meta": {'alias': 'has_sample',
         'domain_of': ['Assay', 'DataEntity'],
         'is_a': 'has_part'} })
    has_reference: Optional[List[str]] = Field(None, description="""Specifies the reference coordinate system used by an omics dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'has_reference', 'domain_of': ['DataEntity'], 'is_a': 'has_part'} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })


class MassSpectrometryResults(DataEntity):
    """
    A data entity consisting of quantitative results from a mass spectrometry experiment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sdsc-ordes/modos-schema'})

    data_path: str = Field(..., description="""The path to access a resource, on a network or local filesystem. Can be a path relative to the root of the digital object, a URL, or an absolute path.""", json_schema_extra = { "linkml_meta": {'alias': 'data_path',
         'domain_of': ['DataEntity', 'ReferenceGenome'],
         'examples': [{'value': 's3://example-bucket/path/to/data'},
                      {'value': 'relative/file/path'},
                      {'value': 'file:///absolute/file/path'}]} })
    data_format: DataFormat = Field(..., description="""Data/file format associated with a data entity.""", json_schema_extra = { "linkml_meta": {'alias': 'data_format', 'domain_of': ['DataEntity']} })
    derived_from: Optional[List[str]] = Field(None, description="""The source data from which some new data was derived.""", json_schema_extra = { "linkml_meta": {'alias': 'derived_from', 'domain_of': ['DataEntity']} })
    has_sample: Optional[List[str]] = Field(None, description="""Biological sample included or described by a given thing.""", json_schema_extra = { "linkml_meta": {'alias': 'has_sample',
         'domain_of': ['Assay', 'DataEntity'],
         'is_a': 'has_part'} })
    has_reference: Optional[List[str]] = Field(None, description="""Specifies the reference coordinate system used by an omics dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'has_reference', 'domain_of': ['DataEntity'], 'is_a': 'has_part'} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })


class Array(DataEntity):
    """
    Data entity consisting of an N-dimensional array.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sdsc-ordes/modos-schema'})

    data_path: str = Field(..., description="""The path to access a resource, on a network or local filesystem. Can be a path relative to the root of the digital object, a URL, or an absolute path.""", json_schema_extra = { "linkml_meta": {'alias': 'data_path',
         'domain_of': ['DataEntity', 'ReferenceGenome'],
         'examples': [{'value': 's3://example-bucket/path/to/data'},
                      {'value': 'relative/file/path'},
                      {'value': 'file:///absolute/file/path'}]} })
    data_format: DataFormat = Field(..., description="""Data/file format associated with a data entity.""", json_schema_extra = { "linkml_meta": {'alias': 'data_format', 'domain_of': ['DataEntity']} })
    derived_from: Optional[List[str]] = Field(None, description="""The source data from which some new data was derived.""", json_schema_extra = { "linkml_meta": {'alias': 'derived_from', 'domain_of': ['DataEntity']} })
    has_sample: Optional[List[str]] = Field(None, description="""Biological sample included or described by a given thing.""", json_schema_extra = { "linkml_meta": {'alias': 'has_sample',
         'domain_of': ['Assay', 'DataEntity'],
         'is_a': 'has_part'} })
    has_reference: Optional[List[str]] = Field(None, description="""Specifies the reference coordinate system used by an omics dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'has_reference', 'domain_of': ['DataEntity'], 'is_a': 'has_part'} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })


class Table(DataEntity):
    """
    Data entity organized in a tabular structure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sdsc-ordes/modos-schema'})

    data_path: str = Field(..., description="""The path to access a resource, on a network or local filesystem. Can be a path relative to the root of the digital object, a URL, or an absolute path.""", json_schema_extra = { "linkml_meta": {'alias': 'data_path',
         'domain_of': ['DataEntity', 'ReferenceGenome'],
         'examples': [{'value': 's3://example-bucket/path/to/data'},
                      {'value': 'relative/file/path'},
                      {'value': 'file:///absolute/file/path'}]} })
    data_format: DataFormat = Field(..., description="""Data/file format associated with a data entity.""", json_schema_extra = { "linkml_meta": {'alias': 'data_format', 'domain_of': ['DataEntity']} })
    derived_from: Optional[List[str]] = Field(None, description="""The source data from which some new data was derived.""", json_schema_extra = { "linkml_meta": {'alias': 'derived_from', 'domain_of': ['DataEntity']} })
    has_sample: Optional[List[str]] = Field(None, description="""Biological sample included or described by a given thing.""", json_schema_extra = { "linkml_meta": {'alias': 'has_sample',
         'domain_of': ['Assay', 'DataEntity'],
         'is_a': 'has_part'} })
    has_reference: Optional[List[str]] = Field(None, description="""Specifies the reference coordinate system used by an omics dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'has_reference', 'domain_of': ['DataEntity'], 'is_a': 'has_part'} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing'],
         'slot_uri': 'schema:description'} })


class MODOCollection(ConfiguredBaseModel):
    """
    A holder for Multi-Omics Digital Objects
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sdsc-ordes/modos-schema', 'tree_root': True})

    entries: Optional[Dict[str, MODO]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'entries', 'domain_of': ['MODOCollection']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
MODO.model_rebuild()
Assay.model_rebuild()
Sample.model_rebuild()
DataEntity.model_rebuild()
ReferenceGenome.model_rebuild()
ReferenceSequence.model_rebuild()
AlignmentSet.model_rebuild()
VariantSet.model_rebuild()
MassSpectrometryResults.model_rebuild()
Array.model_rebuild()
Table.model_rebuild()
MODOCollection.model_rebuild()

