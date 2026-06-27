# DNA Healthcare Archive Simulator

# Simulation Assumptions

Version 0.4.0

---

# Purpose

This document describes the modelling assumptions used by the DNA Healthcare Archive Simulator.

These assumptions are intentionally configurable and should be interpreted as simulation parameters rather than validated real-world characteristics.

Future versions of the simulator will allow most assumptions to be loaded from external configuration files instead of being hard-coded.

---

# Simulation Horizon

Current simulation period:

* 20 Years

Simulation interval:

* Annual

---

# Healthcare Population Model

## Initial Patient Population

Default hospital:

100,000 patients

Healthcare network hospitals:

| Hospital                | Initial Patients |
| ----------------------- | ---------------: |
| Community Hospital      |           75,000 |
| Children's Hospital     |           60,000 |
| Cancer Center           |           45,000 |
| Trauma Center           |           90,000 |
| Academic Medical Center |          250,000 |

---

## Annual Patient Growth

Default simulation:

8%

Healthcare network:

| Hospital                | Annual Growth |
| ----------------------- | ------------: |
| Community Hospital      |            6% |
| Children's Hospital     |            7% |
| Cancer Center           |            5% |
| Trauma Center           |            8% |
| Academic Medical Center |           10% |

Growth rates are deterministic in Version 0.4.0.

Future releases will support probabilistic growth models.

---

# Healthcare Record Model

The simulator currently models five healthcare record categories.

| Record Type                    | Size (MB) | Records per Patient / Year | Active Retention |
| ------------------------------ | --------: | -------------------------: | ---------------: |
| Electronic Health Record (EHR) |         2 |                        5.0 |          7 Years |
| MRI                            |       500 |                       0.15 |          3 Years |
| CT                             |      1000 |                       0.10 |          3 Years |
| X-Ray                          |        50 |                       0.40 |          3 Years |
| Laboratory Report              |         1 |                        8.0 |          5 Years |

After the active retention period expires, records are migrated to the DNA Archive tier.

---

# Storage Architecture

The simulator models two logical storage tiers.

## Active Storage

Contains operational clinical data that remains immediately accessible.

Characteristics:

* High-performance storage
* Frequently accessed
* Operational workload

---

## DNA Archive

Contains historical healthcare records after retention thresholds have been reached.

Characteristics:

* Long-term archival
* Low-access storage
* Capacity optimised

The simulator assumes automatic migration based on record retention policies.

---

# DNA Storage Model

## Compression Ratio

Default:

100:1

Meaning:

100 TB of logical archival data is represented by 1 TB of physical DNA storage.

The compression ratio is configurable.

---

## DNA Media Capacity

Default:

1 TB (physical equivalent)

Future versions may support alternative DNA media assumptions.

---

# Infrastructure Economics

The simulator estimates annual storage costs using configurable cost models.

## Active Storage

Default cost:

USD 220 per TB per year

---

## DNA Archive

Default cost:

USD 35 per TB per year

These values are simulation assumptions and should not be interpreted as market pricing.

---

# Scenario Engine

Version 0.4.0 includes multiple planning scenarios.

Current scenarios:

* Baseline
* Future DNA Technology
* Lower Storage Costs
* High Growth Planning

Each scenario modifies one or more simulation parameters while preserving the underlying simulation model.

---

# Healthcare Network

The healthcare network simulator models independent hospitals operating within a regional healthcare system.

Current assumptions:

* Independent patient growth
* Independent storage generation
* Common DNA storage model
* Common infrastructure cost model

Future releases may introduce hospital-specific storage technologies, policies, and operational characteristics.

---

# Model Limitations

Version 0.4.0 intentionally simplifies several aspects of healthcare operations.

Examples include:

* Constant annual patient growth
* Fixed record generation rates
* Deterministic retention policies
* Uniform storage costs
* No disaster recovery modelling
* No data deduplication
* No compression before DNA archival
* No retrieval latency modelling
* No infrastructure failures

These simplifications are intentional and allow the simulator to remain transparent and easy to extend.

---

# Future Assumptions

Planned releases will introduce configurable assumptions for:

* Hospital definitions
* Record catalogues
* Storage technologies
* DNA media characteristics
* Cost models
* Energy consumption
* Carbon footprint
* Monte Carlo probability distributions
* National healthcare systems

---

# Guiding Principle

Every numerical value documented here represents a configurable modelling assumption.

The purpose of the simulator is not to predict future healthcare infrastructure with certainty, but to provide a transparent framework for exploring alternative scenarios and evaluating long-term archival strategies under different assumptions.
