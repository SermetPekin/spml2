Getting Started
===============

This guide will help you quickly set up and run your first classification workflow with **spml2**.

Initialization
--------------

To create example configuration files, run one of the following commands in your project directory:

.. code-block:: bash

   spml2 init
   # or
   spml init

This will generate:

- ``spml2_main.py``
- ``options_user.py``
- ``models_user.py``

You can edit ``options_user.py`` and ``models_user.py`` to customize your settings and models.

Running Classification
----------------------

After editing your configuration files, run the main script to start the classification workflow:

.. code-block:: bash

   python spml2_main.py

This will execute the workflow using your settings and models, and generate outputs (such as Excel files and plots) in the specified output directory.

Web Interface
-------------

You can also launch the Streamlit web interface for interactive use:

.. code-block:: bash

   spml2 web
   # or
   spml web

This provides a user-friendly UI for running and visualizing your ML workflows.

Next Steps
----------
- See the ``options_user.py`` and ``models_user.py`` files for all available options and customization points.
- Refer to the main documentation for advanced usage, feature explanations, and troubleshooting.
