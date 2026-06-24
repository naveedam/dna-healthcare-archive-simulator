# Simulation Assumptions

## Purpose

This document defines the assumptions used by the DNA Healthcare Archive Simulator.

All simulation results are dependent on these assumptions and should be treated as scenario-based estimates rather than real-world predictions.

---

# Hospital Profile

## Initial Size

* Hospital Type: Large Multi-Specialty Hospital
* Initial Patients: 100,000
* Annual Patient Growth Rate: 8%
* Simulation Duration: 20 Years

---

# Data Generation Assumptions

## Electronic Health Records (EHR)

* Average Record Size: 2 MB
* New Records Per Patient Per Year: 5

## Medical Imaging

### MRI

* Average Size: 500 MB
* Annual MRI Rate: 15% of Patients

### CT Scan

* Average Size: 1,000 MB
* Annual CT Rate: 10% of Patients

### X-Ray

* Average Size: 50 MB
* Annual X-Ray Rate: 40% of Patients

## Lab Reports

* Average Size: 1 MB
* Annual Lab Reports Per Patient: 8

## Genomic Data

* Average Size: 100 GB
* Genomic Study Participation Rate: 1% of Patients

---

# Storage Tiers

## Tier 1: Active Storage

Purpose:

* Frequently accessed records
* Recent patient activity

Technology Assumption:

* SSD/NVMe

Retention:

* 3 Years

---

## Tier 2: Object Storage

Purpose:

* Historical records
* Infrequently accessed data

Technology Assumption:

* Cloud Object Storage

Retention:

* Until Archive Eligibility

---

## Tier 3: DNA Archive Storage

Purpose:

* Long-Term Preservation
* Compliance Retention
* Historical Access

Technology Assumption:

* DNA-Based Archival Storage

---

# Archive Policies

## EHR

Archive After:

* 7 Years

## MRI

Archive After:

* 3 Years

## CT

Archive After:

* 3 Years

## X-Ray

Archive After:

* 3 Years

## Lab Reports

Archive After:

* 5 Years

## Genomic Data

Archive After:

* 1 Year

---

# DNA Storage Assumptions

## Encoding

Binary to DNA Mapping:

00 → A
01 → C
10 → G
11 → T

## Error Correction

Overhead:

* 15%

## Compression

Assumed Compression:

* 20%

---

# Cost Assumptions

## Active Storage

Cost:

* $120 per TB per Year

## Object Storage

Cost:

* $20 per TB per Year

## DNA Storage

Write Cost:

* $50 per TB

Read Cost:

* $5 per TB

Annual Storage Cost:

* $0.25 per TB

---

# Retrieval Assumptions

Average Retrieval Time:

* 6 Hours

Maximum Retrieval Time:

* 24 Hours

Retrieval Requests:

* 0.5% of Archived Records per Year

---

# Energy Assumptions

## Traditional Archive

Power Consumption:

* 100 Units

## DNA Archive

Power Consumption:

* 5 Units

Estimated Reduction:

* 95%

---

# Success Metrics

The simulator should calculate:

* Total Data Generated
* Active Storage Capacity
* Object Storage Capacity
* DNA Archive Capacity
* Annual Storage Cost
* Cumulative Storage Cost
* Retrieval Cost
* Retrieval Latency
* Energy Consumption
* DNA Archive Growth
* Cost Savings vs Traditional Storage

---

# Future Assumption Categories

Potential future enhancements:

* Multiple Hospitals
* Regional Healthcare Networks
* National Healthcare Systems
* AI-Based Archive Optimization
* Variable DNA Synthesis Costs
* Real DNA Storage Density Models
* Regulatory Policy Variations
