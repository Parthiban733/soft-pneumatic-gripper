# Bill of Materials (BOM)

This document lists all components, materials, and hardware required to fabricate, assemble, and operate the **Soft 3-Claw Pneumatic Gripper**.

---

## 1. Raw Materials & Casting Consumables

| Item | Specification / Material | Quantity | Purpose | Supplier / Source |
| :--- | :--- | :--- | :--- | :--- |
| **LSR-105 Silicone Rubber** | 2-part liquid silicone rubber (Part A + B, Shore 05 A) | 500 g | Casting soft pneumatic fingers | Industrial silicone supplier |
| **3D Printing Filament** | PLA or PETG (1.75 mm, Black / Orange) | ~300 g | Printing molds and rigid structural components | Standard 3D printing supplier |
| **Silicone Release Agent** | Mold release spray / petroleum jelly dilution | 1 bottle | Clean mold separation | Hardware supplier |
| **RTV Silicone Sealant** | Room-temperature vulcanizing silicone adhesive | 1 tube | Airtight sealing at inlet fittings | Hardware supplier |

---

## 2. 3D Printed Components

| Part Name | Source File | Qty | Material | Infill % |
| :--- | :--- | :--- | :--- | :--- |
| **Gripper Base Plate** | `cad/step/gripper_base_plate.step` | 1 | PLA / PETG | 40% |
| **Finger Holder Bracket** | `cad/step/finger_holder_bracket.step` | 3 | PLA / PETG | 50% |
| **Air Inlet Adapter** | `cad/step/pneumatic_air_inlet.step` | 3 | PLA / PETG | 100% |
| **Base Mold Bottom** | `cad/stl/base_mold_bottom.stl` | 1 | PLA | 30% |
| **Center Mold Chambers** | `cad/stl/center_mold_chambers.stl` | 1 | PLA | 30% |
| **Outer Mold Top** | `cad/stl/outer_mold_top.stl` | 1 | PLA | 30% |

---

## 3. Pneumatic & Control Components

| Component | Specification | Qty | Function |
| :--- | :--- | :--- | :--- |
| **Mini Diaphragm Pump** | 12V DC, dual-port (positive pressure + vacuum) | 1 | Air pressurization / evacuation |
| **Pneumatic Tubing** | Polyurethane (PU), 4 mm OD x 2.5 mm ID (Blue) | ~2 m | Air routing lines |
| **Push-in Y-Connector** | 4 mm OD push-to-connect 3-way splitter | 2 | Symmetric air distribution to 3 fingers |
| **Straight Quick Fitting** | M5 / 1/8" male to 4 mm push-in | 3 | Secure inlet into finger clamp |
| **Manual / Solenoid Valve** | 2-position 3-way valve or manual pinch valve | 1 | Inflation/deflation control |
| **Power Source** | 12V DC Battery (Lithium-ion / Lead-acid) or Bench PSU | 1 | Powering mini air pump |

---

## 4. Mechanical Fasteners & Hardware

| Item | Specification | Qty | Application |
| :--- | :--- | :--- | :--- |
| **Socket Head Screws** | M3 x 12 mm (Stainless steel) | 6 | Clamping finger holder to soft finger base |
| **Base Mounting Screws** | M3 x 16 mm (Stainless steel) | 6 | Securing finger assemblies to base plate |
| **Hex Nuts** | M3 nylon-lock or standard hex nuts | 12 | Fastener retention |
| **Mold Clamping Hardware** | G-clamps or M4 bolt pairs | 4 | Clamping mold halves during curing |
