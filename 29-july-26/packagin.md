# Python Packaging Notes

## Why package code?

Package code so that others can install it and use it via `pip` **without copying the source files manually.**

A package manager uses your packaged Python source code.

> **`pip` is Python's package manager. It installs packages from package repositories (usually PyPI).**

---

## PyPI

- **PyPI (Python Package Index)** is the official repository where Python packages are published.
- By default, `pip` installs packages from PyPI.

---

## When do we need packages?

- When you want to use the same code in multiple locations (for example, frontend and backend, or across multiple Python projects), it is nice to package it so that it can be be installed and reused easily.
- We use our own package exactly like any other Python package:

```python
import mypackage
```

- Packaging also encourages us to write neat, modular, and independent code, which is generally a good software engineering practice.

---

## setuptools

`setuptools` builds on top of `distutils` (historically) and is used to build and distribute Python packages.

---

## Wheel (`.whl`)

A wheel is a **pre-built installable package**.

- Built distribution format
- Allows much faster installation
- Does not need to rebuild the package during installation

---

## Building a Wheel

```bash
python setup.py bdist_wheel
```

This creates:

```text
build/
dist/
```

Inside `dist/`:

```text
mypackage-1.0.0-py3-none-any.whl
```

---

## Source Distribution (`sdist`)

```bash
python setup.py sdist
```

Creates:

```text
dist/
    mypackage-1.0.0.tar.gz
```

This is the **source distribution**.

It contains the source code, so the package can be rebuilt if necessary.

---

## Overall Workflow

```text
Write Python code
        │
        ▼
Package it using setuptools
        │
        ├── sdist (.tar.gz)
        │      Source distribution
        │
        └── wheel (.whl)
               Built distribution
        │
        ▼
Upload both to PyPI
        │
        ▼
Others install using

pip install your-package
```