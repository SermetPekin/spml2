import pytest
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
from spml2.options import Options
from spml2 import Process, Process_cache
from spml2.parque_utils import df_to_stata
from spml2.utils_init import get_example_data2

EXAMPLE_DATA_NAME = "breast_cancer_with_random_cat.dta"


def create_example_data2(force=False):
    df = get_example_data2()
    folder = Path("./input")
    folder.mkdir(parents=True, exist_ok=True)
    file_name = folder / EXAMPLE_DATA_NAME
    if not force and file_name.exists():
        print(f"File {file_name} already exists.")
        return
    df_to_stata(df, file_name)


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


def get_preprocessor(options: Options) -> ColumnTransformer:
    return ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), options.numerical_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), options.categorical_cols),
        ]
    )


def make_test_pipeline(options: Options):
    return ImbPipeline(
        [
            ("preprocessor", get_preprocessor(options)),
            ("smote", SMOTE(random_state=42)),
        ]
    )


@pytest.mark.skip(reason="For manual testing only, not part of CI")
def test_process_with_custom_pipeline_and_search_type():
    options = Options(
        test_mode=True,
        debug=True,
        target_name="target",
        test_df_size=100,
        test_ratio=0.2,
        root=Path("./input"),
        real_df_filename=EXAMPLE_DATA_NAME,
        output_folder="Output",
        numerical_cols=None,
        categorical_cols=["random_cat"],
        sampling_strategy="auto",
        n_splits=3,
        shap_plots=False,
        roc_plots=False,
        shap_sample_size=10,
        pipeline=None,  # Pass custom pipeline
        search_type="random",  # Test grid search
        search_kwargs={"verbose": 0},  # Custom search kwargs
        data=get_example_data2(),
    )
    options.pipeline = make_test_pipeline(options)

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
