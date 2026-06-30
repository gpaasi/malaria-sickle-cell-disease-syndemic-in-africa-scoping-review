Reframing the Malaria and Sickle Cell Disease Relationship in Sub-Saharan Africa as a Bounded Syndemic: A Scoping Review and Evidence Gap Map
![OSF registration](https://img.shields.io/badge/OSF%20registration-10.17605%2FOSF.IO%2F6TVSB-blue)
![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)
![Review type](https://img.shields.io/badge/review-scoping%20review-green)
![Evidence map](https://img.shields.io/badge/output-evidence%20gap%20map-orange)
![Reproducibility](https://img.shields.io/badge/reproducibility-open%20workflow-informational)
Summary
This repository implements the reproducible workflow for the scoping review and evidence gap map, “Reframing the Malaria-Sickle Cell Disease Relationship in Sub-Saharan Africa as a Bounded Syndemic: A Scoping Review and Evidence Gap Map.”
The review maps and integrates evidence on the malaria and sickle cell disease (SCD) relationship in sub-Saharan Africa across biological, spatial, clinical, service, structural, programme, and theoretical domains. The workflow moves from search documentation and source selection to source-level extraction, domain coding, evidence gap mapping, geographic reconciliation, population/system-level mapping, thematic synthesis, and configurative synthesis.
The review is designed to examine how malaria ecology, HbS selection and persistence, inherited sickle cell anaemia (SCA) burden, malaria-HbS/SCD spatial co-risk, severe anaemia, under-recognition, service-mediated visibility, structural vulnerability, and screening-to-care systems are connected in the literature. It uses a bounded syndemic lens, meaning that malaria and SCD are not treated as syndemic solely because they co-occur geographically. Stronger syndemic relevance requires evidence linking biological interaction, spatial co-risk, clinical convergence, service-mediated visibility, structural vulnerability, or programme response.
Key outputs include PRISMA-ScR source selection counts, source characteristics tables, domain coding files, evidence gap matrices, geographic evidence mapping data, population/system-level evidence mapping data, manuscript-ready figure and table files, and synthesis notes.
Protocol registration
The review protocol was registered on the Open Science Framework:
https://doi.org/10.17605/OSF.IO/6TVSB
Associated OSF project:
https://osf.io/8kdp5
Evidence domains
The review is organised around seven evidence domains:
Code	Evidence domain
D1	Biological interaction between malaria and red blood cell polymorphisms
D2	Spatial co-risk and malaria-HbS/SCD geography
D3	Clinical convergence and under-recognition
D4	Service-mediated visibility and routine data
D5	Structural vulnerability and access to essential SCD services
D6	Programme response and screening-to-care systems
D7	Syndemic theory and integration
Folder layout
```text
.
├─ protocol/
│  ├─ osf_registration.md
│  └─ protocol_summary.md
├─ search_strategy/
│  ├─ database_searches/
│  │  └─ README.md
│  ├─ grey_literature_searches/
│  │  └─ README.md
│  ├─ citation_searching.md
│  └─ search_log.csv
├─ screening/
│  ├─ prisma_counts.csv
│  ├─ title_abstract_screening_summary.csv
│  └─ full_text_exclusion_reasons.csv
├─ extraction/
│  ├─ included_sources_characteristics.csv
│  ├─ domain_coding.csv
│  ├─ geographic_reconciliation.csv
│  ├─ population_system_level_coding.csv
│  └─ evidence_gap_priorities.csv
├─ analysis/
│  ├─ generate_prisma_flow.py
│  ├─ generate_summary_tables.py
│  ├─ generate_evidence_gap_matrix.py
│  ├─ generate_geographic_map.py
│  └─ generate_population_system_matrix.py
├─ outputs/
│  ├─ figures/
│  ├─ tables/
│  └─ supplementary_files/
├─ manuscript/
│  ├─ abstract.md
│  ├─ main_manuscript.md
│  ├─ declarations.md
│  └─ cover_letter.md
├─ docs/
│  ├─ data_dictionary.md
│  ├─ coding_rules.md
│  └─ reproducibility_notes.md
├─ .gitignore
├─ CITATION.cff
├─ LICENSE
└─ README.md
```
Required inputs
The workflow uses source-level extraction and coding files rather than full-text PDFs. Full-text articles should not be committed to this repository.
Place or maintain the following files under `extraction/` unless you edit paths in the scripts.
Essential
`included_sources_characteristics.csv`  
Source-level inventory of all included sources, including study ID, source citation, country or region, evidence type or design, population or data source, main concept addressed, domain codes, primary geographic category, and primary population/system-level category.
`domain_coding.csv`  
Binary domain coding file showing whether each source contributes to D1 through D7.
`geographic_reconciliation.csv`  
Source-level geographic reconciliation file used to classify evidence by primary geographic category.
`population_system_level_coding.csv`  
Source-level population/system-level recoding file used to generate the supplementary population/system evidence map.
`evidence_gap_priorities.csv`  
Domain-level evidence gap priority classification used to support interpretation of the evidence gap map and research priorities.
`prisma_counts.csv`  
PRISMA-ScR source selection counts used to generate the source selection summary.
Optional
`full_text_exclusion_reasons.csv`  
Full-text exclusion decisions and reasons.
`title_abstract_screening_summary.csv`  
Title and abstract screening decisions.
`search_log.csv`  
Search dates, databases, search strings, and retrieved records.
Software
The workflow is intentionally lightweight and can be run with either Python or R, depending on the user’s preference. The current scripts are written in Python.
Recommended:
Python 3.10 or newer
pandas
matplotlib
openpyxl, if Excel outputs are needed
Install Python dependencies with:
```bash
pip install pandas matplotlib openpyxl
```
A future R workflow may be added if the figures are regenerated using `ggplot2`, `sf`, or related packages.
Run the workflow
Scripts are intended to be run from the repository root.
Step 1. Generate PRISMA-ScR reporting counts
```bash
python analysis/generate_prisma_flow.py
```
Exports the PRISMA-ScR counts used to report source identification, screening, full-text assessment, and inclusion.
Step 2. Generate summary tables
```bash
python analysis/generate_summary_tables.py
```
Creates domain totals, source-type-by-domain summaries, and geography-by-domain summaries under `outputs/tables/`.
Step 3. Generate the main evidence gap matrix
```bash
python analysis/generate_evidence_gap_matrix.py
```
Generates the source-category-by-domain evidence gap matrix. This supports the main manuscript figure showing how evidence types map onto the seven domains.
Step 4. Generate the geographic evidence map data
```bash
python analysis/generate_geographic_map.py
```
Creates geographic evidence distribution summaries by primary geographic category and evidence domain.
Step 5. Generate the population/system-level matrix
```bash
python analysis/generate_population_system_matrix.py
```
Generates the supplementary population/system-level evidence matrix. This reorganises the same 68 included sources by population or system level while retaining the seven evidence domains.
Key outputs
Typical outputs include:
PRISMA-ScR source selection counts
source characteristics tables
domain coding summaries
evidence gap matrix counts
geographic reconciliation summaries
population/system-level matrix counts
evidence gap priority tables
manuscript-ready figures
manuscript-ready supplementary tables
thematic synthesis notes
configurative synthesis notes
Example output locations:
```text
outputs/figures/
outputs/tables/
outputs/supplementary_files/
```
Manuscript linkage
This repository supports the manuscript:
Reframing the Malaria-Sickle Cell Disease Relationship in Sub-Saharan Africa as a Bounded Syndemic: A Scoping Review and Evidence Gap Map
The intended figure structure is:
Figure	Purpose
Figure 1	PRISMA-ScR source selection flow diagram
Figure 2	Matrix evidence gap map by source category and evidence domain
Figure 3	Geographic evidence map
Figure 4	Configurative synthesis schema of the bounded malaria-SCD evidence pathway
Figure S1	Population/system-level evidence gap map
Main manuscript files are stored in `manuscript/`, and generated tables or figures are stored in `outputs/`.
Reproducibility
The workflow is organised as a transparent scoping review pipeline. The scripts are intended to be run after the extraction and coding files have been finalised.
For reproducibility:
keep source-level extraction files in `extraction/`
keep screening and PRISMA counts in `screening/`
avoid editing generated outputs manually
document any changes to coding rules in `docs/coding_rules.md`
do not upload copyrighted full-text PDFs
preserve study IDs across all extraction and analysis files
rerun the scripts after changing source-level coding files
compare generated domain totals with the expected reconciled values
Expected reconciled totals:
Domain	Expected total
D1	20
D2	10
D3	10
D4	11
D5	20
D6	19
D7	6
Total domain assignments	96
Included sources	68
Bounded syndemic interpretation
The review uses a bounded syndemic lens to avoid overclaiming. Co-occurrence of malaria and SCD in the same setting is not treated as sufficient evidence of syndemic interaction. Syndemic relevance is interpreted as stronger when evidence links one or more of the following:
biological interaction
spatial co-risk
clinical convergence
service-mediated visibility
structural vulnerability
programme response
The configurative synthesis links these domains into an evidence pathway from malaria ecology and HbS selection to HbSS births, SCA burden, severe anaemia, under-recognition, service visibility, structural access to care, and screening-to-care programme response.
Troubleshooting
File or path errors
Check that all required CSV files are present in `extraction/` and `screening/`. Run scripts from the repository root.
Domain totals do not match expected values
Check `domain_coding.csv` and `included_sources_characteristics.csv`. Confirm that domain codes are separated consistently and that all 68 study IDs are present.
Matrix cell counts differ from the manuscript
Check whether the row category being used is source category, geographic category, or population/system level. These are different views of the same source inventory and should not be mixed.
Geographic counts look different from disease burden
The geographic evidence map represents evidence distribution, not malaria or SCD disease burden. Global, foundational, theory, and multicountry sources are coded separately where appropriate.
Missing data in source characteristics
Missing or unclear source-level fields should be coded as `unclear` or `not reported` rather than inferred without support.
Citing
Please cite this repository using `CITATION.cff`, the OSF registration, and the final published article when available.
OSF registration:
https://doi.org/10.17605/OSF.IO/6TVSB
Please also cite the main methodological and substantive sources used in the manuscript, including:
PRISMA-ScR reporting guidance
Joanna Briggs Institute scoping review guidance
malaria-HbS biological interaction studies
malaria and HbS/SCA geospatial mapping studies
severe anaemia and malaria-SCD clinical convergence studies
newborn screening and screening-to-care implementation studies
syndemic theory and methods sources
License
See `LICENSE`.
Recommended approach:
repository documentation, extracted review data, tables, and figures under CC BY 4.0
analysis scripts may be reused with attribution under the repository license
Contact
George Paasi  
Makerere University College of Health Sciences, School of Medicine, Kampala, Uganda  
Mbale Clinical Research Institute, Mbale, Uganda  
Email: georgepaasi8@gmail.com  
ORCID: 0000-0001-6360-0589  
Postal address: P.O. Box 1966, Mbale, Uganda
Co-authors: Grace Ndeezi, Ruth Namazzi, Ezekiel Mupere, Ian Guyton Munabi, Sarah Kiguli, Richard Idro, and Peter Olupot-Olupot.
