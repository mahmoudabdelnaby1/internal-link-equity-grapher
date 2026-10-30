# Internal Link Equity Grapher & Orphan Page Radar

> Visualize internal PageRank distribution and spot orphan pages instantly from your crawl data with zero external dependencies.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CLI_SCRIPT](https://img.shields.io/badge/Format-CLI--SCRIPT-green.svg)](#)
[![Tier: 2](https://img.shields.io/badge/Tier-2-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Create a standalone Python CLI tool that parses standard crawl export CSVs (Screaming Frog or Sitebulb format), builds a directed graph of internal links, computes internal PageRank using iterative power-iteration, identifies orphan pages (0 inlinks), and generates an interactive, standalone HTML topology visualization report.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `LICENSE`
- `README.md`
- `reports/sample_report.html`
- `sample_data/crawl_export.csv`
- `src/pagerank_graph.py`
- `tests/test_graph.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/pagerank_graph.py --help
```

### Interactive Browser Tool
Open `reports/sample_report.html` directly in your web browser (Chrome, Edge, Safari) to use the local interactive calculator or dashboard. Operates 100% client-side with zero external network calls.

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "seo",
  "repository": "internal-link-equity-grapher",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Graph Traversal Scale:** Large enterprise e-commerce catalogs (>50,000 URLs) require directed graph adjacency matrices to compute PageRank without memory exhaustion.
- **Canonical & Noindex Filters:** Orphan page radar must distinguish between intentionally hidden landing pages and accidental orphans missing internal links.
- **Crawl Depth Limits:** Search bots prioritize pages within 3 to 4 click depths from the root domain.

---

## 📚 Primary Documentation & Verifiable References

- [Google Search Central: Internal Linking Guidelines](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) - Official guidelines for search-friendly link structure and crawlability.
- [Stanford University: The PageRank Citation Ranking Architecture](http://ilpubs.stanford.edu:8090/422/) - Original mathematical formulation for link equity and random surfer models.
- [NetworkX Documentation: Graph Analysis Algorithms](https://networkx.org/documentation/stable/) - Open-source network analysis library for directed graphs.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
