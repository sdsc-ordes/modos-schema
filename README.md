# modos-schema

Metadata schema for the SMOC Multi-Omics Digital Object System.

```mermaid
erDiagram
MODOCollection {

}
MODO {
    datetime creation_date  
    datetime last_update_date  
    uri source_uri  
    uriorcurie id  
    string name  
    string description  
}
Assay {
    OmicsTypeList omics_type  
    uriorcurie id  
    string name  
    string description  
}
DataEntity {
    string data_path  
    DataFormat data_format  
    uriorcurie id  
    string name  
    string description  
}
ReferenceGenome {
    string data_path  
    integerList taxon_id  
    uri source_uri  
    string version  
    uriorcurie id  
    string name  
    string description  
}
ReferenceSequence {
    string sequence_md5  
    uri source_uri  
    string version  
    uriorcurie id  
    string name  
    string description  
}
Sample {
    string cell_type  
    string source_material  
    Sex sex  
    integerList taxon_id  
    stringList collector  
    uriorcurie id  
    string name  
    string description  
}

MODOCollection ||--}o MODO : "entries"
MODO ||--}o Assay : "has_assay"
Assay ||--}o Sample : "has_sample"
Assay ||--}o DataEntity : "has_data"
DataEntity ||--}o Sample : "has_sample"
DataEntity ||--|o ReferenceGenome : "has_reference"
ReferenceGenome ||--}o ReferenceSequence : "has_sequence"

```



## Website

[https://sdsc-ordes.github.io/modos-schema](https://sdsc-ordes.github.io/modos-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [modos_schema](src/modos_schema)
    * [schema](src/modos_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/modos_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).

This project was developed by [SDSC](https://datascience.ch) as part of the [SMOC](http://smoc.ethz.ch) (Swiss Multi-Omics Consortium) and funded by the [PHRT](https://www.sfa-phrt.ch) ETH initiative (Personalized Health and Related technologies).

<img src="http://smoc.ethz.ch/images/smoc_mint.svg" width=100 /> <img src="https://www.sfa-phrt.ch/wp-content/uploads/2022/07/PHRT_Logo_transparent_50px.png" width=200 /> 
