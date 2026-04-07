# Bluff Body Flame Holder — CFD Study
A computational investigation of flame stabilization mechanisms in a bluff body combustor using ANSYS Fluent (Student Edition).

## Overview
This project applies an incremental CFD validation methodology to evaluate three bluff body geometries — cylinder (benchmark), diamond, and V-gutter — for use as flame holders in a lean combustor. The study uses dodecane (C₁₂H₂₆) as a Jet-A surrogate fuel at a baseline equivalence ratio of φ = 0.6, with parametric sweeps down to lean blowout.

All simulations are performed in 2D using ANSYS Fluent Student Edition (512k cell limit). Results provide design guidance; 3D LES would be required for final experimental validation.

---

## Objectives

### Objective 1 — Flame Stabilization
Evaluate flame stabilization limits by comparing recirculation residence time to chemical timescale via Damköhler number analysis:

$$Da = \frac{\tau_{residence}}{\tau_{chemical}}$$

- Vary equivalence ratio from φ = 0.6 to lean blowout for each geometry
- Vary blockage ratio (2%–30%) for each geometry
- Map Da vs φ and Da vs blockage ratio
- Identify the optimal geometry and blockage ratio combination that maximizes Da > Da_critical

### Objective 2 — Pressure Loss
Quantify total pressure loss across each bluff body geometry:

- Compare drag coefficient (Cd) as a proxy for total pressure loss
- Evaluated at ideal operating conditions determined from Objective 1
- Directly relevant to combustor thermodynamic efficiency

### Objective 3 — Entropy Production
Quantify and separate irreversibility contributions from:

- **Viscous dissipation due to separation** — extracted from Phase 3 (non-reacting flow)
- **Heat release irreversibility** — extracted from Phase 4 (reactive flow)
- Compare entropy production across geometries at ideal operating conditions

---

## Validation Methodology
Validation follows an incremental confidence-building chain before applying the methodology to geometries without reference data:

| Phase | Re | Geometry | Physics | Purpose |
|-------|----|----------|---------|---------|
| 1 | 200 | Cylinder | Laminar | Validate workflow, mesh, BCs |
| 2 | Operating | Cylinder | Turbulent | Validate turbulence model, wall treatment |
| 3 | Operating | Target shapes | Turbulent | Apply validated methodology |
| 4 | Operating | Target shapes | Reactive | Flame stabilization analysis |

Phases 3 and 4 are repeated for each bluff body geometry.

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
| Baseline equivalence ratio | φ = 0.6 (fuel lean) |
| Equivalence ratio sweep | φ = 0.6 → lean blowout |
| Blockage ratio sweep | 2% – 30% |
| Turbulence model | k-ω SST |
| Combustion model | EDM / Finite Rate |

---

## Current Status
- [x] Phase 1 — Geometry construction (wake zone and no wake zone models)
- [x] Phase 1 — Steady state preliminary run (U99% boundary layer validation)
- [x] Phase 1 — Transient St number validation run
- [x] Phase 2 — Turbulent cylinder validation and mesh independence
- [ ] Phase 3 — Diamond and V-gutter geometry
- [ ] Phase 4 — Reactive flow

---

## References
- Williamson, C.H.K. (1989) — St and Cl reference data for cylinder at Re=200
- Liu et al. (1998) — Cd reference data for cylinder at Re=200
- Achenbach (1968) — Experimental data for cylinder at high Re
