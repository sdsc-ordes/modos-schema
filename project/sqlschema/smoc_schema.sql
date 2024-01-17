

CREATE TABLE "AlignmentSet" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	data_path TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Array" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	data_path TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MODO" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	creation_date DATETIME NOT NULL, 
	last_update_date DATETIME NOT NULL, 
	source_uri TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MODOCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ReferenceGenome" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	data_path TEXT NOT NULL, 
	source_uri TEXT, 
	version TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Sample" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	cell_type TEXT, 
	source_material TEXT, 
	sex VARCHAR(6), 
	PRIMARY KEY (id)
);

CREATE TABLE "VariantSet" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	data_path TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Assay" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_sample TEXT, 
	"MODO_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("MODO_id") REFERENCES "MODO" (id)
);

CREATE TABLE "ReferenceSequence" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	sequence_md5 TEXT, 
	source_uri TEXT, 
	version TEXT, 
	"ReferenceGenome_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ReferenceGenome_id") REFERENCES "ReferenceGenome" (id)
);

CREATE TABLE "ReferenceGenome_taxon_id" (
	backref_id TEXT, 
	taxon_id INTEGER, 
	PRIMARY KEY (backref_id, taxon_id), 
	FOREIGN KEY(backref_id) REFERENCES "ReferenceGenome" (id)
);

CREATE TABLE "Sample_taxon_id" (
	backref_id TEXT, 
	taxon_id INTEGER, 
	PRIMARY KEY (backref_id, taxon_id), 
	FOREIGN KEY(backref_id) REFERENCES "Sample" (id)
);

CREATE TABLE "Sample_collector" (
	backref_id TEXT, 
	collector TEXT, 
	PRIMARY KEY (backref_id, collector), 
	FOREIGN KEY(backref_id) REFERENCES "Sample" (id)
);

CREATE TABLE "DataEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	data_path TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	"Assay_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Assay_id") REFERENCES "Assay" (id)
);

CREATE TABLE "Assay_omics_type" (
	backref_id TEXT, 
	omics_type VARCHAR(15) NOT NULL, 
	PRIMARY KEY (backref_id, omics_type), 
	FOREIGN KEY(backref_id) REFERENCES "Assay" (id)
);
