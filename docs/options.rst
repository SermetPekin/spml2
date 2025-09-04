Options & Configuration
======================

This page documents all available options for configuring your spml2 workflow. You can set these in your ``options_user.py`` file.

Available Options
-----------------

.. list-table:: Main Options
   :header-rows: 1

   * - Option
     - Type
     - Default
     - Description / Possible Values
   * - test_mode
     - bool
     - False
     - Enable test mode for quick runs (uses a small sample)
   * - debug
     - bool
     - False
     - Enable debug mode (extra output, skips some models)
   * - target_name
     - str
     - 'target'
     - Name of the target column in your data
   * - test_df_size
     - int
     - 1000
     - Number of rows for test DataFrame (if test_mode)
   * - test_ratio
     - float
     - 0.20
     - Proportion of the dataset to use as test split
   * - root
     - Path or str
     - './input'
     - Root directory for data files
   * - real_df_filename
     - str
     - 'example.dta'
     - Main data file name (supports .dta, .parquet, .csv, .xlsx)
   * - output_folder
     - Path or str
     - 'Output'
     - Output folder for results
   * - numerical_cols
     - list[str] or None
     - None
     - List of numerical columns (None = infer automatically)
   * - sampling_strategy
     - str or float
     - 'auto'
     - SMOTE sampling strategy (see imbalanced-learn docs)
   * - n_splits
     - int
     - 5
     - Number of cross-validation splits
   * - shap_plots
     - bool
     - False
     - Enable SHAP plots
   * - roc_plots
     - bool
     - True
     - Enable ROC curve plots
   * - shap_sample_size
     - int
     - 100
     - Number of samples for SHAP plots
   * - pipeline
     - ImbPipeline or None
     - None
     - Custom pipeline (advanced users)
   * - search_type
     - str
     - 'random'
     - Hyperparameter search type ('random' or 'grid')
   * - search_kwargs
     - dict or None
     - None
     - Additional kwargs for search (e.g., {'verbose': 1})

Example options_user.py
-----------------------

.. code-block:: python

   from pathlib import Path
   from spml2 import Options
   from models_user import models
   from imblearn.pipeline import Pipeline as ImbPipeline
   from sklearn.preprocessing import StandardScaler
   from imblearn.over_sampling import SMOTE

   user_pipeline = ImbPipeline([
       ("preprocessor", StandardScaler()),
       ("smote", SMOTE(random_state=42)),
       # Add more steps as needed
   ])

   options = Options(
       test_mode=False,
       debug=False,
       target_name="target",
       test_df_size=1000,
       test_ratio=0.20,
       root=Path("./input"),
       real_df_filename="example.dta",
       output_folder="Output",
       numerical_cols=None,
       sampling_strategy="auto",
       n_splits=5,
       shap_plots=False,
       roc_plots=True,
       shap_sample_size=100,
       pipeline=user_pipeline,
       search_type="random",
       search_kwargs={"verbose": 1},
   )

   print(options)

See the comments in ``options_user.py`` for more details and customization tips.
