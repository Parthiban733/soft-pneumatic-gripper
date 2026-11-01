# Finite Element Analysis (FEA) & Kinematic Characterization

This document details the numerical simulation framework, constitutive material modeling, and experimental kinematic validation of the soft pneumatic finger actuators.

---

## 1. Hyperelastic Constitutive Material Formulation

Liquid Silicone Rubber (LSR-105) exhibits strong geometric and material non-linearities under pneumatic inflation. To accurately model this behavior, the elastomer is characterized using a **3rd-order Yeoh strain energy density function** for near-incompressible hyperelasticity:

$$W = C_1 (I_1 - 3) + C_2 (I_1 - 3)^2 + C_3 (I_1 - 3)^3$$

where:
- $W$ is the strain energy per unit reference volume.
- $I_1 = \lambda_1^2 + \lambda_2^2 + \lambda_3^2$ is the first invariant of the right Cauchy-Green deformation tensor.
- $\lambda_1, \lambda_2, \lambda_3$ are the principal stretch ratios.
- $C_1, C_2, C_3$ are hyperelastic material coefficients calibrated via non-linear regression on experimental tensile and compression test data ($R^2 > 0.98$).

Near-incompressibility is enforced by setting Poisson's ratio:
$$\nu = 0.495$$

The initial shear modulus $\mu_0$ relates directly to the first Yeoh parameter:
$$\mu_0 = 2 C_1 = 0.033 \text{ MPa} \implies C_1 = 0.0165 \text{ MPa}$$

Embedded reinforcement elements (e.g., rigid backbones / TPU constraint layers) are represented as linear elastic with:
$$E = 30 \text{ MPa}, \quad \nu = 0.33$$

---

## 2. FEA Numerical Setup & Boundary Conditions

| Analysis Parameter | Implementation Setting |
| :--- | :--- |
| **Solver Type** | Non-linear Implicit Static (Large Deflection / NLGEOM enabled) |
| **Element Type** | 10-node Quadratic Tetrahedral Elements with Hybrid Formulation (C3D10H) |
| **Mesh Density** | Non-uniform: Global size 1.5 mm; locally refined to 0.6 mm at internal ribs and thin bellows walls |
| **Total Elements** | 120,000 – 180,000 elements |
| **Boundary Conditions** | Proximal mounting face fully constrained ($U_x = U_y = U_z = UR_x = UR_y = UR_z = 0$) |
| **Contact Interfaces** | Tied constraints on bonded mold interfaces; frictionless self-contact along bellows fold surfaces |
| **Load Application** | Uniform internal pressure ramped quasi-statically from $0.10 \text{ bar}$ to $0.25 \text{ bar}$ ($\Delta P = 0.05 \text{ bar}$) |

### Mesh Independence & Convergence Study
Mesh sensitivity was evaluated using global element sizes of 2.5 mm, 1.5 mm, and 0.8 mm. The predicted tip displacement deviation between the 1.5 mm and 0.8 mm meshes remained below **1.5%**, validating the computational accuracy of the selected discretization.

---

## 3. Experimental Kinematic & Force Measurements

Experiments were conducted on the fabricated physical prototype using a regulated pressure supply and digital force transducer.

### Table 3.1: Actuation Pressure vs. Kinematic Response
| Actuation Pressure (bar) | Actuation Pressure (kPa) | Bending Angle ($\theta$, deg) | Tip Displacement ($\delta$, mm) |
| :--- | :--- | :--- | :--- |
| **0.10** | 10 | 12.5° | 4.7 mm |
| **0.15** | 15 | 18.6° | 7.1 mm |
| **0.20** | 20 | 24.8° | 9.5 mm |
| **0.25** | 25 | 30.5° | 12.1 mm |

### Table 3.2: Actuation Pressure vs. Gripping Force & Payload Capacity
| Actuation Pressure (bar) | Gripping Force ($F_g$, N) | Maximum Held Payload ($m_{max}$, g) |
| :--- | :--- | :--- |
| **0.10** | 0.39 N | 43 g |
| **0.15** | 0.64 N | 69 g |
| **0.20** | 0.80 N | 86 g |
| **0.25** | 1.03 N | 110 g |

---

## 4. Benchmark Comparison: Current Design vs. Prior Art

| Performance Metric | Prior Art / Conventional Soft Actuator | Current Bio-Inspired Gripper | Improvement / Rationale |
| :--- | :--- | :--- | :--- |
| **Material Model** | $E = 50 \text{ MPa}$ (unrealistic stiffness for soft silicone) | $E = 0.10 \text{ MPa}, \nu = 0.495$ (LSR-105) | High-fidelity hyperelastic representation |
| **Bending Angle** | 50.0° at 60 kPa | **63.8° at 50 kPa** | **+27.6% greater deflection at lower pressure** |
| **Bending Efficiency** | 0.83° / kPa | **1.28° / kPa** | **+54.2% higher actuation efficiency** |
| **Structural Stability** | Excessive uncontrolled bulging | Controlled bellows bending | High lateral stiffness with compliance |

---

## 5. Object Manipulation & Grasping Validation

The assembled 3-finger pneumatic gripper was tested on **20 diverse object types** characterized by varying geometries, fragility, surface textures, and mass:
- **Fragile Objects**: Fresh chicken eggs, lightweight paper cups, light bulbs.
- **Deformable Objects**: Foam balls, fruit, rubber squeeze toys.
- **Rigid & Industrial Items**: Cylindrical water bottles (60–80 g), grease containers (75–80 g), computer mice, electronic PCB modules.

### Outcome
- **Grasping Success Rate**: **> 95% across all 20 test categories**.
- **Damage Assessment**: Zero structural deformation or surface damage observed on fragile test specimens.
- **Fatigue Life**: Actuator returned to baseline shape with **zero residual strain** across **200+ continuous inflation/deflation cycles**.
