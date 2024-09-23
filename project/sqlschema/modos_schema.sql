-- # Class: "NamedThing" Description: "A generic grouping for any identifiable entity"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "MODO" Description: "Represents the Multi-Omics Digital Object. It encapsulates omics and other datasets and their metadata."
--     * Slot: creation_date Description: The date on which something was created.
--     * Slot: last_update_date Description: The date on which the thing was last modified.
--     * Slot: source_uri Description: The URI from which a resource or dataset was obtained or derived.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: MODOCollection_id Description: Autocreated FK slot
-- # Class: "Assay" Description: "A coordinated set of actions designed to generate data from samples."
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Sample" Description: "A biological sample used in assays. Examples include a whole organism, tissue or cell line."
--     * Slot: cell_type Description: The cell type name or code, if applicable.
--     * Slot: source_material Description: The biological source from which the sample was isolated (tissue, organ).
--     * Slot: sex Description: The biological sex of a sample.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "DataEntity" Description: "An entity containing data."
--     * Slot: data_path Description: The path to access a resource, on a network or local filesystem. Can be a path relative to the root of the digital object, a URL, or an absolute path.
--     * Slot: data_format Description: Data/file format associated with a data entity.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "ReferenceGenome" Description: "Reference assembly of a given genome, consisting of a collection of congiguous sequences (contigs)."
--     * Slot: data_path Description: The path to access a resource, on a network or local filesystem. Can be a path relative to the root of the digital object, a URL, or an absolute path.
--     * Slot: source_uri Description: The URI from which a resource or dataset was obtained or derived.
--     * Slot: version Description: A string specifying the release or version of a software or resource.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "ReferenceSequence" Description: "A contiguous sequence of DNA part of a reference coordinate system (genome assembly)."
--     * Slot: sequence_md5 Description: The pre-computed hash uniquely representing a biological sequence. Calculated as the MD5 of the upper-case sequence excluding all whitespace characters (this is equivalent to SQ:M5 in SAM).
--     * Slot: source_uri Description: The URI from which a resource or dataset was obtained or derived.
--     * Slot: version Description: A string specifying the release or version of a software or resource.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "AlignmentSet" Description: "A data entity consisting of genomic intervals aligned to a reference."
--     * Slot: data_path Description: The path to access a resource, on a network or local filesystem. Can be a path relative to the root of the digital object, a URL, or an absolute path.
--     * Slot: data_format Description: Data/file format associated with a data entity.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "VariantSet" Description: "A data entity consisting of genomic variants relative to a reference."
--     * Slot: data_path Description: The path to access a resource, on a network or local filesystem. Can be a path relative to the root of the digital object, a URL, or an absolute path.
--     * Slot: data_format Description: Data/file format associated with a data entity.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Array" Description: "Data entity consisting of an N-dimensional array."
--     * Slot: data_path Description: The path to access a resource, on a network or local filesystem. Can be a path relative to the root of the digital object, a URL, or an absolute path.
--     * Slot: data_format Description: Data/file format associated with a data entity.
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "MODOCollection" Description: "A holder for Multi-Omics Digital Objects"
--     * Slot: id Description: 
-- # Class: "MODO_has_assay" Description: ""
--     * Slot: MODO_id Description: Autocreated FK slot
--     * Slot: has_assay_id Description: An assay that was performed as part of a given thing.
-- # Class: "Assay_has_sample" Description: ""
--     * Slot: Assay_id Description: Autocreated FK slot
--     * Slot: has_sample_id Description: Biological sample included or described by a given thing.
-- # Class: "Assay_has_data" Description: ""
--     * Slot: Assay_id Description: Autocreated FK slot
--     * Slot: has_data_id Description: Data entity included in a given collection.
-- # Class: "Assay_omics_type" Description: ""
--     * Slot: Assay_id Description: Autocreated FK slot
--     * Slot: omics_type Description: The type of omics considered.
-- # Class: "Sample_taxon_id" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: taxon_id Description: The taxid number describing the taxonomic range of a sample.
-- # Class: "Sample_collector" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: collector Description: The organization responsible for collecting a given sample.
-- # Class: "DataEntity_has_sample" Description: ""
--     * Slot: DataEntity_id Description: Autocreated FK slot
--     * Slot: has_sample_id Description: Biological sample included or described by a given thing.
-- # Class: "DataEntity_has_reference" Description: ""
--     * Slot: DataEntity_id Description: Autocreated FK slot
--     * Slot: has_reference_id Description: Specifies the reference coordinate system used by an omics dataset.
-- # Class: "ReferenceGenome_has_sequence" Description: ""
--     * Slot: ReferenceGenome_id Description: Autocreated FK slot
--     * Slot: has_sequence_id Description: Denotes that a sequence belongs to a collection (e.g. a reference genome).
-- # Class: "ReferenceGenome_taxon_id" Description: ""
--     * Slot: ReferenceGenome_id Description: Autocreated FK slot
--     * Slot: taxon_id Description: The taxid number describing the taxonomic range of a sample.
-- # Class: "AlignmentSet_has_sample" Description: ""
--     * Slot: AlignmentSet_id Description: Autocreated FK slot
--     * Slot: has_sample_id Description: Biological sample included or described by a given thing.
-- # Class: "AlignmentSet_has_reference" Description: ""
--     * Slot: AlignmentSet_id Description: Autocreated FK slot
--     * Slot: has_reference_id Description: Specifies the reference coordinate system used by an omics dataset.
-- # Class: "VariantSet_has_sample" Description: ""
--     * Slot: VariantSet_id Description: Autocreated FK slot
--     * Slot: has_sample_id Description: Biological sample included or described by a given thing.
-- # Class: "VariantSet_has_reference" Description: ""
--     * Slot: VariantSet_id Description: Autocreated FK slot
--     * Slot: has_reference_id Description: Specifies the reference coordinate system used by an omics dataset.
-- # Class: "Array_has_sample" Description: ""
--     * Slot: Array_id Description: Autocreated FK slot
--     * Slot: has_sample_id Description: Biological sample included or described by a given thing.
-- # Class: "Array_has_reference" Description: ""
--     * Slot: Array_id Description: Autocreated FK slot
--     * Slot: has_reference_id Description: Specifies the reference coordinate system used by an omics dataset.

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Assay" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Sample" (
	cell_type TEXT, 
	source_material TEXT, 
	sex VARCHAR(6), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "DataEntity" (
	data_path TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ReferenceGenome" (
	data_path TEXT NOT NULL, 
	source_uri TEXT, 
	version TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ReferenceSequence" (
	sequence_md5 TEXT, 
	source_uri TEXT, 
	version TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "AlignmentSet" (
	data_path TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "VariantSet" (
	data_path TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Array" (
	data_path TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "MODOCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "MODO" (
	creation_date DATETIME NOT NULL, 
	last_update_date DATETIME NOT NULL, 
	source_uri TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"MODOCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("MODOCollection_id") REFERENCES "MODOCollection" (id)
);
CREATE TABLE "Assay_has_sample" (
	"Assay_id" TEXT, 
	has_sample_id TEXT, 
	PRIMARY KEY ("Assay_id", has_sample_id), 
	FOREIGN KEY("Assay_id") REFERENCES "Assay" (id), 
	FOREIGN KEY(has_sample_id) REFERENCES "Sample" (id)
);
CREATE TABLE "Assay_has_data" (
	"Assay_id" TEXT, 
	has_data_id TEXT, 
	PRIMARY KEY ("Assay_id", has_data_id), 
	FOREIGN KEY("Assay_id") REFERENCES "Assay" (id), 
	FOREIGN KEY(has_data_id) REFERENCES "DataEntity" (id)
);
CREATE TABLE "Assay_omics_type" (
	"Assay_id" TEXT, 
	omics_type VARCHAR(15) NOT NULL, 
	PRIMARY KEY ("Assay_id", omics_type), 
	FOREIGN KEY("Assay_id") REFERENCES "Assay" (id)
);
CREATE TABLE "Sample_taxon_id" (
	"Sample_id" TEXT, 
	taxon_id INTEGER, 
	PRIMARY KEY ("Sample_id", taxon_id), 
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id)
);
CREATE TABLE "Sample_collector" (
	"Sample_id" TEXT, 
	collector TEXT, 
	PRIMARY KEY ("Sample_id", collector), 
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id)
);
CREATE TABLE "DataEntity_has_sample" (
	"DataEntity_id" TEXT, 
	has_sample_id TEXT, 
	PRIMARY KEY ("DataEntity_id", has_sample_id), 
	FOREIGN KEY("DataEntity_id") REFERENCES "DataEntity" (id), 
	FOREIGN KEY(has_sample_id) REFERENCES "Sample" (id)
);
CREATE TABLE "DataEntity_has_reference" (
	"DataEntity_id" TEXT, 
	has_reference_id TEXT, 
	PRIMARY KEY ("DataEntity_id", has_reference_id), 
	FOREIGN KEY("DataEntity_id") REFERENCES "DataEntity" (id), 
	FOREIGN KEY(has_reference_id) REFERENCES "ReferenceGenome" (id)
);
CREATE TABLE "ReferenceGenome_has_sequence" (
	"ReferenceGenome_id" TEXT, 
	has_sequence_id TEXT, 
	PRIMARY KEY ("ReferenceGenome_id", has_sequence_id), 
	FOREIGN KEY("ReferenceGenome_id") REFERENCES "ReferenceGenome" (id), 
	FOREIGN KEY(has_sequence_id) REFERENCES "ReferenceSequence" (id)
);
CREATE TABLE "ReferenceGenome_taxon_id" (
	"ReferenceGenome_id" TEXT, 
	taxon_id INTEGER, 
	PRIMARY KEY ("ReferenceGenome_id", taxon_id), 
	FOREIGN KEY("ReferenceGenome_id") REFERENCES "ReferenceGenome" (id)
);
CREATE TABLE "AlignmentSet_has_sample" (
	"AlignmentSet_id" TEXT, 
	has_sample_id TEXT, 
	PRIMARY KEY ("AlignmentSet_id", has_sample_id), 
	FOREIGN KEY("AlignmentSet_id") REFERENCES "AlignmentSet" (id), 
	FOREIGN KEY(has_sample_id) REFERENCES "Sample" (id)
);
CREATE TABLE "AlignmentSet_has_reference" (
	"AlignmentSet_id" TEXT, 
	has_reference_id TEXT, 
	PRIMARY KEY ("AlignmentSet_id", has_reference_id), 
	FOREIGN KEY("AlignmentSet_id") REFERENCES "AlignmentSet" (id), 
	FOREIGN KEY(has_reference_id) REFERENCES "ReferenceGenome" (id)
);
CREATE TABLE "VariantSet_has_sample" (
	"VariantSet_id" TEXT, 
	has_sample_id TEXT, 
	PRIMARY KEY ("VariantSet_id", has_sample_id), 
	FOREIGN KEY("VariantSet_id") REFERENCES "VariantSet" (id), 
	FOREIGN KEY(has_sample_id) REFERENCES "Sample" (id)
);
CREATE TABLE "VariantSet_has_reference" (
	"VariantSet_id" TEXT, 
	has_reference_id TEXT, 
	PRIMARY KEY ("VariantSet_id", has_reference_id), 
	FOREIGN KEY("VariantSet_id") REFERENCES "VariantSet" (id), 
	FOREIGN KEY(has_reference_id) REFERENCES "ReferenceGenome" (id)
);
CREATE TABLE "Array_has_sample" (
	"Array_id" TEXT, 
	has_sample_id TEXT, 
	PRIMARY KEY ("Array_id", has_sample_id), 
	FOREIGN KEY("Array_id") REFERENCES "Array" (id), 
	FOREIGN KEY(has_sample_id) REFERENCES "Sample" (id)
);
CREATE TABLE "Array_has_reference" (
	"Array_id" TEXT, 
	has_reference_id TEXT, 
	PRIMARY KEY ("Array_id", has_reference_id), 
	FOREIGN KEY("Array_id") REFERENCES "Array" (id), 
	FOREIGN KEY(has_reference_id) REFERENCES "ReferenceGenome" (id)
);
CREATE TABLE "MODO_has_assay" (
	"MODO_id" TEXT, 
	has_assay_id TEXT, 
	PRIMARY KEY ("MODO_id", has_assay_id), 
	FOREIGN KEY("MODO_id") REFERENCES "MODO" (id), 
	FOREIGN KEY(has_assay_id) REFERENCES "Assay" (id)
);