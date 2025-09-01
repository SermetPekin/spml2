import pytest
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
from spml2.options import Options
from spml2 import Process, Process_cache


def make_test_pipeline():
    # Example custom pipeline for testing
    return ImbPipeline(
        [
            ("preprocessor", StandardScaler()),
            ("smote", SMOTE(random_state=42)),
            # Model step will be set by core logic
        ]
    )


def test_process_with_custom_pipeline_and_search_type():
    options = Options(
        test_mode=True,
        debug=True,
        target_name="target",
        test_df_size=100,
        test_ratio=0.2,
        root=Path("./input"),
        real_df_filename="example.dta",
        output_folder="Output",
        numerical_cols=None,
        sampling_strategy="auto",
        n_splits=3,
        shap_plots=False,
        roc_plots=False,
        shap_sample_size=10,
        pipeline=make_test_pipeline(),  # Pass custom pipeline
        search_type="random",  # Test grid search
        search_kwargs={"verbose": 0},  # Custom search kwargs
    )
    models = {
        "XGBoost": {
            "model": XGBClassifier(random_state=42, n_jobs=-1, eval_metric="auc"),
            "params": {
                "model__n_estimators": [10, 50],
                "model__learning_rate": [0.01, 0.1],
            },
        },
    }
    # Run both fresh and cache processes
    Process(options, models)
    Process_cache(options, models)


def test_process_default_pipeline():
    options = Options(
        test_mode=True,
        debug=True,
        target_name="target",
        test_df_size=100,
        test_ratio=0.2,
        root=Path("./input"),
        real_df_filename="example.dta",
        output_folder="Output",
        numerical_cols=None,
        sampling_strategy="auto",
        n_splits=3,
        shap_plots=False,
        roc_plots=False,
        shap_sample_size=10,
        # No pipeline, should use default
    )
    models = {
        "XGBoost": {
            "model": XGBClassifier(random_state=42, n_jobs=-1, eval_metric="auc"),
            "params": {
                "model__n_estimators": [10, 50],
                "model__learning_rate": [0.01, 0.1],
            },
        },
    }
    Process(options, models)
    Process_cache(options, models)
