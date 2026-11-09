# USD Scene Inspector

**An OpenUSD scene inspection toolkit built with Python and Houdini Solaris.**

USD Scene Inspector is a developer-focused toolkit for inspecting and analysing Universal Scene Description (USD) stages. It provides utilities to examine scene hierarchy, prim types, attributes, relationships, metadata and transformations.

The project is being developed as part of my OpenUSD Developer learning path, following NVIDIA's official Learn OpenUSD curriculum.

## Project Objectives

- Understand and inspect OpenUSD scene structures.
- Develop reusable Python utilities for USD pipeline development.
- Explore USD schemas and composition.
- Integrate OpenUSD Python with Houdini Solaris.
- Generate structured inspection reports for production workflows.

## Current Features

- [x] USD stage initialization through Houdini Solaris
- [x] Prim hierarchy traversal
- [x] Prim type inspection
- [x] Attribute inspection
- [x] Relationship inspection
- [x] Basic prim metadata inspection
- [x] Applied API schema listing
- [x] Direct child count inspection
- [x] Local and world transformation experiments

## Planned Features

- [ ] Standalone USD stage loader
- [ ] Typed schema inspection
- [ ] API schema inspection
- [ ] Transform inspection
- [ ] Time samples and stage timing inspection
- [ ] Layer and composition inspection
- [ ] JSON report export
- [ ] Automated testing
- [ ] Graphical interface

## Technology Stack

- Python
- OpenUSD (`pxr`)
- Houdini 22.0 Apprentice
- Houdini Solaris
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
USD-Scene-Inspector/
├── houdini/
│   ├── usd_prim_inspector.py
│   └── r_and_d/
├── assets/
│   └── test_scenes/
├── reports/
├── tests/
├── docs/
├── examples/
├── README.md
├── requirements.txt
└── .gitignore
```

## Development Environment

The initial inspection scripts use Houdini's Python environment because they depend on the `hou` module and Houdini's USD stage evaluation.

Standalone OpenUSD support will be developed separately.

## Example Usage

Run the inspection script inside Houdini Python Shell:

```python
import hou

lop = hou.node("/obj/usd_stage/cube_lop")
stage = lop.stage()

for prim in stage.Traverse():
    print(prim.GetPath(), prim.GetTypeName())
```

## Learning Resources

- [NVIDIA Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html)
- [NVIDIA Scene Description Blueprints](https://docs.nvidia.com/learn-openusd/latest/scene-description-blueprints/index.html)
- [OpenUSD Documentation](https://openusd.org/)
- [NVIDIA LearnOpenUSD GitHub Repository](https://github.com/NVIDIA-Omniverse/LearnOpenUSD)

## Project Status

**Status: Active Development**

This project is under continuous development. Features, examples and documentation will be added as the learning and implementation progress.

## Author

**Bhanu Pratap Khuntia**

Pipeline Technical Director | Python Developer | OpenUSD Developer

GitHub: [@BhanuPy](https://github.com/BhanuPy)