# DNA Healthcare Archive Simulator

A simulation platform for modeling long-term healthcare data growth and evaluating the use of DNA-based archival storage.

---

# Overview

Healthcare organizations generate and retain enormous amounts of data:

- Electronic Health Records (EHR)
- MRI scans
- CT scans
- X-Ray images
- Laboratory reports
- Genomics data (future milestone)

As patient populations grow, healthcare providers face increasing challenges related to:

- Storage capacity
- Long-term retention
- Regulatory compliance
- Archival costs
- Infrastructure planning

DNA storage is an emerging technology capable of preserving digital information for decades or even centuries while requiring dramatically less physical space than traditional storage media.

This project simulates how healthcare data could be managed using a tiered storage architecture that automatically migrates aging records from active storage into DNA archives.

---

# Project Goals

The simulator aims to answer questions such as:

- How much healthcare data will be generated over 20 years?
- How quickly does storage growth accelerate?
- Which record types consume the most storage?
- How much data remains active?
- How much data can be moved into DNA archives?
- What percentage of data is suitable for long-term preservation?
- What are the future infrastructure requirements?

---

# Current Simulation Model

The simulator currently models:

## Patient Population Growth

Healthcare data generation is driven by a growing patient population.

Current assumptions:

- Initial patients: 100,000
- Annual growth rate: 8%

---

## Healthcare Record Types

| Record Type | Description |
|------------|-------------|
| EHR | Electronic Health Records |
| MRI | Magnetic Resonance Imaging |
| CT | Computed Tomography |
| XRAY | X-Ray Imaging |
| LAB | Laboratory Reports |

Each record type has:

- Record size
- Annual creation rate
- Retention period

---

## Storage Tiers

### Active Storage

Recently created records remain in operational storage for clinical use.

### DNA Archive

Older records automatically migrate to DNA archival storage once retention thresholds are reached.

---

# Simulation Workflow

Patient Growth
↓
Healthcare Record Generation
↓
Retention Policies
↓
Storage Tier Evaluation
↓
Active Storage
↓
DNA Archive
↓
20-Year Projection

---

# Current Output

The simulator produces annual projections showing:

- Patient population
- Active storage consumption
- DNA archive consumption
- Total storage footprint

Example:

Year    Patients    Active TB    DNA TB    Total TB
--------------------------------------------------
1       100,000     20.31        0.00      20.31
5       136,048     80.49       38.68     119.17
10      199,900    120.76      173.51     294.27
20      431,570    260.72      668.86     929.57

---

# Architecture

Repository Structure

src/
├── models/
│   ├── record.py
│   └── archive.py
│
├── simulation/
│   └── hospital_simulator.py
│
└── main.py

docs/
├── vision.md
└── assumptions.md

---

# Milestone Status

## Milestone 1 - Complete

- Patient growth simulation
- Healthcare data generation
- Annual storage forecasting
- 20-year projection

## Milestone 2 - Complete

- Record type tracking
- Retention policies
- Active storage modeling
- DNA archive modeling
- Automatic archive migration
- Tiered storage reporting

## Milestone 3 - Planned

- DNA compression ratios
- Physical DNA media calculations
- Storage cost analysis
- Cost savings estimation
- Genomics data modeling

## Milestone 4 - Planned

- Multi-hospital simulation
- Regional healthcare networks
- National-scale healthcare systems
- Interactive dashboards
- Scenario analysis

---

# Why DNA Storage?

DNA has the potential to become one of the highest-density archival storage technologies ever developed.

Potential advantages include:

- Extremely high storage density
- Long-term durability
- Reduced physical footprint
- Lower archival infrastructure requirements

This simulator is intended to explore how such technology might be applied within healthcare environments.

---

# Running the Simulator

Requirements:

- Python 3.12+

Run:

python main.py

---

# Future Vision

The long-term goal is to evolve this project into a healthcare archival planning platform capable of modeling:

- Hospital networks
- National healthcare systems
- Genomics repositories
- DNA storage economics
- Capacity planning scenarios
- AI-assisted infrastructure recommendations

