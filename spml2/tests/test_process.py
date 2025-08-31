def test_main():
    assert True


import pandas as pd
import numpy as np
from sklearn.model_selection import (
    train_test_split,
    GridSearchCV,
    StratifiedKFold,
    RandomizedSearchCV,
)
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    roc_auc_score,
    f1_score,
    confusion_matrix,
    classification_report,
)
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
import warnings
import time

warnings.filterwarnings("ignore")
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from sklearn.compose import ColumnTransformer
from pathlib import Path
import os

# 3. Pipeline and parameter grids for all models
models = {
    "XGBoost": {
        "model": XGBClassifier(random_state=42, n_jobs=-1, eval_metric="auc"),
        "params": {
            "model__n_estimators": [10, 50, 100, 200, 400, 750, 1000],
            "model__learning_rate": [0.001, 0.01, 0.1, 1, 10, 100],
            "model__max_depth": [3, 5, 7, 11, 15, 20, 30, 50],
            "model__colsample_bytree": [0.7, 0.9],
            "model__gamma": [0, 0.1],
            "model__reg_alpha": [0, 0.1],
            "model__reg_lambda": [0, 0.1],
            "model__scale_pos_weight": [1, 3],
        },
    },
}
try:
    import pytest
except ImportError:
    pass
import pandas as pd
from spml2.options import Options
from spml2.utils import get_data, local_print, local_print_df
from spml2 import Process, Process_cache
from pathlib import Path
from spml2 import Options
from spml2 import Process, Process_cache
from models_user import models

TEST_MODE = True  # Enable test mode for quick runs
DEBUG = True  # Enable debug mode for extra checks
TARGET_NAME = "target"  # Name of the target column
TEST_DF_SIZE = 1000  # Number of rows for test DataFrame
ROOT = Path("./input")  # Root directory for data
REAL_DF_FILENAME = "example.dta"  # Main data file name (must be .dta)
OUTPUT_FOLDER = "Output"  #  None  # Output folder (None = default root/Output)
NUMERICAL_COLS = None  # List of numerical columns (None = infer from data)
SAMPLING_STRATEGY = "auto"  # SMOTE sampling strategy ('auto' recommended)
N_SPLITS = 5

SHAP_PLOTS = False
ROC_PLOTS = True


options = Options(
    test_mode=TEST_MODE,
    debug=DEBUG,
    target_name=TARGET_NAME,
    test_df_size=TEST_DF_SIZE,
    root=ROOT,
    real_df_filename=REAL_DF_FILENAME,
    output_folder=OUTPUT_FOLDER,
    numerical_cols=NUMERICAL_COLS,
    sampling_strategy=SAMPLING_STRATEGY,
    n_splits=N_SPLITS,
    shap_plots=SHAP_PLOTS,
    roc_plots=ROC_PLOTS,
)


def test_process():
    Process(options, models)
    Process_cache(options, models)
