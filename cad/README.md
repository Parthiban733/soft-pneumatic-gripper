# 3D CAD & Manufacturing Files

This directory contains the computer-aided design (CAD) files for the **Soft Multi-Finger Pneumatic Gripper**, designed in **Autodesk Fusion 360**.

---

## Directory Organization

```
cad/
├── stl/                     # 3D Printable Mesh Files (for slicers: Cura, PrusaSlicer, Bambu Studio)
│   ├── base_mold_bottom.stl      # Lower mold forming bottom curvature and sealing rails
│   ├── center_mold_chambers.stl  # Center core mold defining internal chamber ribs
│   └── outer_mold_top.stl        # Upper enclosure mold for outer silicone layer
├── step/                    # Parametric CAD Models (for Fusion 360, SolidWorks, FreeCAD, Onshape)
│   ├── bottom_mold.step          # Parametric bottom mold model
│   ├── middle_mold.step          # Parametric middle chamber mold model
│   ├── top_mold_plate.step       # Parametric top mold plate
│   ├── gripper_base_plate.step   # Symmetric 3-claw mounting plate with tubing guides
│   ├── finger_holder_bracket.step# Rigid clamping bracket securing fingers to base
│   ├── pneumatic_air_inlet.step  # Air inlet connector interface
│   └── finger_insert_core.step   # Internal alignment insert
└── raw/                     # Original source CAD files as exported from Fusion 360
```

---

## 3D Printing Recommendations (Mold Fabrication)

The molds must be printed with high surface finish and dimensional precision to prevent silicone leakage and air pocket formation.

| Parameter | Recommended Setting | Rationale |
| :--- | :--- | :--- |
| **Material** | PLA / PETG | Adequate tensile stiffness, low shrinkage, high detail resolution |
| **Layer Height** | 0.12 mm – 0.16 mm | Ensures smooth surface finish along pneumatic rib chambers |
| **Infill Density** | 25% – 35% | Provides structural rigidity against clamping pressure |
| **Wall / Perimeters** | 3 – 4 perimeters | Ensures mold cavities are airtight and non-porous |
| **Print Speed** | 40 – 50 mm/s | Enhances dimensional accuracy on small internal ribs |
| **Bed Adhesion** | Brim (5 mm) | Prevents corner lifting or warping during printing |

---

## Post-Processing & Surface Preparation

1. **Inspection**: Verify that internal chamber rib slots in `center_mold_chambers.stl` are free of stringing or print artifacts.
2. **Surface Smoothing**: Lightly sand inner mold cavities with 400-grit wet sandpaper if layer lines are prominent.
3. **Mold Release**: Apply a light mist of silicone release agent (or dilute petroleum jelly / mineral oil) prior to casting to ensure clean demolding.

---

## Hardware & Pneumatic Assembly

- **Mounting Screws**: M3 hex socket cap screws (12 mm – 16 mm length) to clamp `finger_holder_bracket` to `gripper_base_plate`.
- **Air Connectors**: Standard push-in pneumatic fittings (M5 male thread to 4 mm / 6 mm OD polyurethane tubing).
- **Sealant**: Room-temperature vulcanizing (RTV) silicone adhesive applied at inlet joints for leak-free operation up to 0.5 bar.
