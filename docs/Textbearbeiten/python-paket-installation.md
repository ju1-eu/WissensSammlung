---
title: "python-paket-installation"
author: "Jan Unger"
date: "2024-11-02"
---

# Installation von Python-Paketen

Letzte Aktualisierung: 2024-11-02


1. Virtuelle Umgebung erstellen und aktivieren
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Abhängigkeiten installieren
```bash
#pip install -r requirements.txt
#pip install -e .

vim requirements.in
matplotlib
numpy
pandas
scipy
seaborn
pillow
PyPDF2
openpyxl
sympy
Pint
pytest
black[jupyter]
flake8
mypy
types-seaborn
scikit-learn

pip install --upgrade pip
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
pip check
```

3. Entwicklungsworkflow 1
```bash
python -m diabvizpro

# Code formatieren
black diabvizpro/

# Linting
#flake8 diabvizpro/
flake8 --max-line-length=100 diabvizpro/

# Typ-Überprüfung: pip install types-seaborn
mypy diabvizpro/

# Tests ausführen
pytest
```

4. Entwicklungsworkflow 2
```bash
# Code formatieren
#pip install "black[jupyter]" # => .py und .ipynb
black .

# Linting
flake8 --max-line-length=100 *.py

# Typ-Überprüfung
mypy diabetes_data_generator.py

# Tests ausführen
pytest
```