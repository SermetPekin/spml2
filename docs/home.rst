spml2-mltools
=============

.. image:: https://img.shields.io/pypi/v/spml2-mltools.svg
   :target: https://pypi.org/project/spml2-mltools/
   :alt: PyPI version

.. image:: https://img.shields.io/badge/python-3.10+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Supported Python versions

.. image:: https://img.shields.io/github/license/SermetPekin/spml2-mltools.svg
   :target: https://github.com/SermetPekin/spml2/blob/main/LICENSE
   :alt: License

Overview
--------

**spml2-mltools** is a convenient package for applying machine learning workflows with a Streamlit app, generating Excel outputs, and visualizations.

Installation
------------

.. code-block:: bash

   pip install spml2-mltools

Quick Start
-----------

1. **Initialize Example Files**

   .. code-block:: bash

      spml2 init
      # or
      spml init

   This creates:
   - spml2_main.py
   - options_user.py
   - models_user.py

2. **Run Classification**

   .. code-block:: bash

      python spml2_main.py

3. **Launch the Web UI**

   .. code-block:: bash

      spml2 web
      # or
      spml web

Features
--------

- Streamlit-based web runner
- ROC curve visualization
- Feature importances
- SHAP graphs
- Excel output generation

Documentation
-------------

- `Homepage <https://github.com/SermetPekin/spml2>`_
- `Documentation <https://github.com/SermetPekin/spml2>`_
- `Issues <https://github.com/SermetPekin/spml2/issues>`_
- `Changelog <https://github.com/SermetPekin/spml2/releases>`_
