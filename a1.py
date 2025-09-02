from spml2.data_abstract import get_data_abstract_with_options
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
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from spml2.core import assert_numerical_cols
from spml2.data_ import check_data_with_options


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


EXAMPLE_DATA_NAME = "breast_cancer_with_random_cat.dta"
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
        "model": XGBClassifier(random_state=42, n_jobs=1, eval_metric="auc"),
        "params": {
            "model__n_estimators": [10, 50],
            "model__learning_rate": [0.01, 0.1],
        },
    },
}

data, options = check_data_with_options(options.data, options)
options.data = data
d = get_data_abstract_with_options(options, data)
print(d)
print(options.data)
# Run both fresh and cache processes
# Process(options, models)
# Process_cache(options, models)
d = get_data_abstract_with_options(options, data)
print(d)
