# Soft Gripper Fabrication & Two-Stage Casting Protocol

This guide describes the complete manufacturing workflow for fabricating the soft pneumatic fingers and assembling the 3-claw gripper, based on research developed at the **Department of Robotics and Automation Engineering, PSG College of Technology**.

---

## 1. Material Specifications (LSR-105)

The soft actuator fingers are fabricated using **Liquid Silicone Rubber (LSR-105)**, a two-component addition-cure platinum/tin silicone elastomer selected for its ultra-low Shore hardness, high elongation at break, and non-linear hyperelastic resilience.

| Parameter | Value | Standard / Condition |
| :--- | :--- | :--- |
| **Shore Hardness** | 05 A | Room temperature cured |
| **Density** | 1100 kg/m³ (1.10 g/cm³) | DIN 53479 |
| **Viscosity (mixed)** | 3000 cps | At 25 °C |
| **Tensile Strength** | ≥ 35 kgf/cm² (~3.43 MPa) | ASTM D412 |
| **Modulus of Elasticity ($E$)**| 0.10 MPa | Initial linear regime |
| **Poisson's Ratio ($\nu$)** | 0.495 | Near-incompressible |
| **Shear Modulus ($G$)** | 0.033 MPa | Calculated ($G = E / [2(1+\nu)]$) |
| **Bulk Modulus ($K$)** | 150 MPa | Calculated ($K = E / [3(1-2\nu)]$) |
| **Mixing Ratio** | 1:1 by volume | Part A : Part B |
| **Working Time (Pot Life)** | 25 – 30 minutes | At 25 °C |
| **Demold Time** | 6 – 8 hours | Room temperature cure |

---

## 2. Equipment & Tools Required

- **3D Printed Molds**: Bottom mold (`base_mold_bottom.stl`), center core mold (`center_mold_chambers.stl`), and upper mold (`outer_mold_top.stl`).
- **LSR-105 Silicone**: Part A and Part B liquid silicone rubber.
- **Precision Scale or Graduated Cylinders**: For accurate 1:1 volume/mass measurement.
- **Vacuum Degassing Chamber**: Capable of achieving ≥ -0.09 MPa (or 1-hour ambient resting).
- **Mold Clamps / G-clamps / Tape**: For leak-tight mold sealing.
- **Silicone Release Agent**: Mild lubricant / demolding spray.
- **Pneumatic Fittings**: Push-in connectors (M5 / 4 mm OD), Y/T-connectors, PU tubing (4 mm OD / 2.5 mm ID).
- **RTV Silicone Adhesive**: For bonding pneumatic connectors and sealing air lines.

---

## 3. Step-by-Step Casting Procedure

### Step 3.1: Mold Preparation
1. Clean the 3D-printed PLA mold parts with isopropyl alcohol.
2. Ensure mold cavities are clean and devoid of debris or support material.
3. Lightly apply a silicone mold release agent to all internal contact surfaces.

### Step 3.2: Silicone Compounding & Mixing
1. Dispense equal parts (1:1 by volume or mass) of **LSR-105 Part A** and **Part B** into a clean mixing container.
2. Stir continuously for **4 minutes** using a flat spatula. Ensure thorough mixing along the bottom and side walls of the container to achieve a homogeneous compound.

### Step 3.3: Degassing
- **Method A (Preferred - Vacuum Chamber)**: Place the mixed silicone in a vacuum chamber. Evacuate to -0.09 MPa for **3 to 5 minutes**. The silicone will rise, foam, and collapse as trapped micro-bubbles are extracted.
- **Method B (Alternative - Ambient Resting)**: If a vacuum chamber is unavailable, allow the mixed silicone to rest at ambient temperature for **45 to 60 minutes**, letting air bubbles rise and burst naturally before pouring.

### Step 3.4: Stage 1 Casting (Internal Chamber Core)
1. Assemble the base mold and center chamber mold.
2. Slowly pour the degassed silicone blend into the internal chamber mold cavity in a continuous, thin stream to prevent introducing air.
3. Securely clamp the mold halves to maintain dimensional fidelity and prevent flashing.
4. Allow the silicone to cure at room temperature (25 °C) for **6 to 8 hours**.
5. Carefully open the mold to expose the partially formed inner actuator core with embedded bellow cavities.

### Step 3.5: Stage 2 Casting (Outer Encapsulation)
1. Align the cured inner core into the outer enclosure mold.
2. Position the pneumatic air inlet adapter (`pneumatic_air_inlet.step`) at the proximal end of the finger.
3. Prepare a fresh batch of LSR-105 silicone (1:1 ratio, mixed and degassed).
4. Pour the second batch over the internal core to cast the outer layer, encapsulating the internal chambers.
5. Seal the outer mold with clamps and cure for another **6 to 8 hours** at room temperature.
6. Gently demold the fully cured soft robotic finger.

---

## 4. Gripper Assembly & System Integration

```
[ Air Source: Compressor / 12V Diaphragm Pump ]
                     │
                     ▼
             [ Air Tubing 4mm OD ]
                     │
                     ▼
           [ 1-to-3 Y / T Manifold ]
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   [ Finger 1 ] [ Finger 2 ] [ Finger 3 ]
        └────────────┴────────────┘
                     │
      Mounted to 3-Claw Base Plate (120° Offset)
```

1. **Air Inlet Installation**: Insert push-in pneumatic fittings into the molded inlet channels of each finger. Apply a thin layer of RTV silicone sealant at the interface to guarantee airtight sealing up to 0.5 bar.
2. **Mounting to Base**: Fasten each soft finger to the 3D-printed circular base plate (`gripper_base_plate.step`) using the rigid finger clamps (`finger_holder_bracket.step`) and M3 screws. The fingers are arranged at **120° radial symmetry**.
3. **Pneumatic Circuit Setup**: Connect the three fingers in parallel to a central air line using push-in Y-connectors. Connect the feed line to a 12V DC mini diaphragm vacuum/air pump and pressure regulator.
4. **Leak Testing**: Pressurize the assembly to 0.10 bar. Inspect all joints for air leakage. Ensure all three fingers deform uniformly and symmetrically.
