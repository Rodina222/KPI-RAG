---
license: cc-by-4.0
task_categories:
- text-retrieval
- text-ranking
- text-generation
- text-classification
- question-answering
language:
- en
tags:
- telecom
- 3gpp
- knowledge_graph
- 6g
- standards
- llm
- rag
- information_extraction
pretty_name: 3GPP Rel-19 Telecom Knowledge Graph
size_categories:
- 100K<n<1M
---


# 3GPP Rel-19 Telecom Knowledge Graph (KG + Chunks)

## Dataset Summary

This dataset, developed by *Khalifa University Research Institute for Digital Future (KU-DF)*, contains a large-scale **telecom-domain knowledge graph** built from **3GPP Release 19 specifications**, together with the underlying text chunks used for extraction and grounding.

It supports research and development in:
- Telecom and networking
- Knowledge graphs
- LLM-based reasoning over standards
- Retrieval-Augmented Generation (RAG)

---

## Dataset Structure

The dataset includes three main components:

- **Knowledge Graph** (`graphml`):
  - Nodes: telecom entities (concepts, parameters, identifiers, protocols, references)
  - Edges: semantic relations with provenance

- **Text Chunks** (`jsonl`):
  - Fine-grained chunks extracted from 3GPP specifications
  - Used as grounding for KG nodes and edges

- **Entity Mapping** (`json`):
  - Maps entities to chunk IDs and source files

---

## Data Statistics

- **Nodes**: 21,540  
- **Edges**: 31,718  
- **Unique entities**: 6,044  
- **Text chunks**: 896,453  

---

## Data Cleaning

Cleaning was limited to structural normalization:
- Removal of NULL-only or empty identifiers
- Removal of isolated nodes with no semantic content
- Exact duplicate node and edge removal
- No semantic pruning of telecom concepts

---

## Intended Uses

- Telecom standards analysis
- Knowledge graph analytics
- LLM-assisted exploration of 3GPP specifications
- RAG systems for telecom documentation
- Research on information extraction from standards

---

## Limitations

- The dataset is limited to **3GPP Release 19**
- Some entities may lack textual descriptions and are intended for later enrichment

---

## License

This dataset is released under the **Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0)** license.

The dataset is derived from publicly available 3GPP specifications.  
Users must provide appropriate attribution and may not use the dataset for commercial purposes.

## Additional Information

For full details on construction and usage, see the accompanying `README.md`.

## Acknowledgement

Compute resources for building and experimenting with the knowledge graph were provided by the ITU AI for Good AWS Sandbox.

---

## Citation

If you use this dataset, please cite the dataset repository

```bibtex
@dataset{kudf_rel19_telecom_kg_2026,
  title     = {3GPP Release 19 Telecom Knowledge Graph},
  author    = {Yang, Yuzhi and Bariah, Lina and Lu, Yuhuan and Debbah, Merouane},
  year      = {2026},
  publisher = {Hugging Face},
  organization = {Khalifa University Research Institute for Digital Future (KU-DF)},
  abstract  = {A large-scale telecom knowledge graph constructed from 3GPP Release 19 specifications, together with text chunks for grounding, provenance, and retrieval-augmented generation (RAG).},
  url       = {https://huggingface.co/datasets/otellm/telecom-kg-rel19},
  note      = {Part of the GSMA Open Telco Assets Initiative.}
}




