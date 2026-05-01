# Bluff Body Flame Holder — CFD Study
A computational investigation of flame stabilization mechanisms in a bluff body combustor using ANSYS(Student Edition).

## Overview
This project applies an incremental CFD validation methodology to evaluate three bluff body geometries — cylinder (benchmark), diamond, and V-gutter — for use as flame holders in a lean combustor. The study progresses from laminar benchmark validation 
at Re=200 to turbulent operating conditions at Re=10^5,characterizing each geometry's wake structure, recirculation length and strength, and aerodynamic coefficients to identify the most 
effective flame holder candidate. The best performing geometry is then subjected to a single reacting flow simulation to assess flame stabilization characteristics.

All simulations are performed in 2D using ANSYS Fluent Student Edition (512k cell limit). Results provide design guidance; 3D LES would be required for final experimental validation.

---

## Objectives

### Objective 1 — Flame Stabilization
Assess flame stabilization characteristics for each bluff body 
geometry through wake structure analysis and a single reactive 
flow simulation on the best-performing geometry:

- Characterize recirculation length (Lr), peak negative velocity, 
  and base pressure coefficient (Cpb) from non-reacting flow
- Identify geometry with strongest recirculation zone for 
  flame anchoring
- Apply reactive flow simulation to validated candidate
- Evaluate Damköhler number from recirculation residence time 
  and chemical timescale to confirm flame stability:

### Objective 2 — Pressure Loss
Characterize pressure loss across each bluff body to inform thermodynmaic efficency:

- Compare drag coefficient (Cd) as a proxy for total pressure loss at outlet
- Compare base pressure coeffcient (Cpb) for flame anchoring and combustion effcieny tradeoffs in the recircualtion zone
- Directly relevant to combustor thermodynamic efficiency


---

## Validation Methodology
Validation follows an incremental confidence-building chain before applying the methodology to geometries without reference data:

| Phase | Re | Geometry | Physics | Purpose |
|-------|----|----------|---------|---------|
| 1 | 200 | Cylinder | Laminar | Validate workflow, BCs |
| 2 | Operating | Cylinder | Turbulent | Validate turbulence model, mesh, wall treatment |
| 3 | Operating | Target shapes | Turbulent | Apply validated methodology |
| 4 | Operating | Target shape | Reactive | Flame stabilization analysis |

Phases 4 is conducted for the best preforming geometry in phase 3.

---

## Geometries Studied
- **Cylinder** — benchmark only, used for Phase 1 and 2 validation
- **Diamond** — fixed separation points, intermediate aerodynamic complexity
- **V-gutter** — industrially relevant flame holder used in afterburners and ramjets

---

## Fuel & Operating Conditions
| Parameter | Value |
|-----------|-------|
| Fuel | Dodecane (C₁₂H₂₆) — Jet-A surrogate |
| Equivalence ratio | φ = 0.6 (fuel lean) |
| Turbulence model | k-ω SST |
| Combustion model | EDM / Finite Rate |

---

## Current Status
- [x] Phase 1 — Geometry construction (wake zone and no wake zone models)
- [x] Phase 1 — Steady state preliminary run (U99% boundary layer validation)
- [x] Phase 1 — Transient St number validation run
- [x] Phase 2 — Turbulent cylinder validation
- [ ] Phase 3 — Diamond and V-gutter geometry
- [ ] Phase 4 — Reactive flow

---

## Reference
- Cox, J. S., Rumsey, C. L., Brentner, K. S., & Younis, B. A. 
  "Computation of Vortex Shedding and Radiated Sound for a 
  Circular Cylinder." NASA Langley Research Center.
  → Validation reference for cylinder Cd, St, Cl across Re ranges