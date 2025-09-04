import os
import pytest
import pandas as pd
from spml2.options import Options
from spml2.utils import get_data, local_print, local_print_df
from spml2 import Process, Process_cache

# --- User-editable configuration ---
from pathlib import Path
from spml2 import Options
from spml2 import Process, Process_cache

try:
    from models_user import models
except ImportError:
    models = None
    # Handle missing models_user module
    print("Warning: models_user module not found. Using default models.")
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
)


def test_options_fields():
    opts = Options(
        test_mode=True,
        debug=True,
        target_name="target",
        test_df_size=10,
        root=".",
        real_df_filename="file.dta",
        output_folder=".",
        numerical_cols=None,
        sampling_strategy="auto",
        n_splits=2,
    )
    assert hasattr(opts, "test_mode")
    assert hasattr(opts, "debug")
    assert hasattr(opts, "target_name")
    assert hasattr(opts, "test_df_size")
    assert hasattr(opts, "root")
    assert hasattr(opts, "real_df_path")
    assert hasattr(opts, "output_folder")
    assert hasattr(opts, "numerical_cols")
    assert hasattr(opts, "sampling_strategy")
    assert hasattr(opts, "n_splits")


def test_local_print_and_df(capsys):
    local_print("hello world")
    captured = capsys.readouterr()
    assert "hello world" in captured.out
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    # Should not raise error
    local_print_df(df)


@pytest.mark.skipif(
    "GITHUB_ACTIONS" in os.environ, reason="Skipping test in GitHub workflow"
)
def test_get_data_test_mode(monkeypatch):
    df = pd.DataFrame({"target": [0, 1], "feature": [1.0, 2.0]})
    dummy_path = Path(".") / "dummy.dta"
    df.to_stata(dummy_path)

    class DummyOptions:
        test_mode = True
        test_df_size = 2
        root = "."
        real_df_filename = "file.dta"
        output_folder = "."
        numerical_cols = None
        sampling_strategy = "auto"
        n_splits = 2
        test_file_name = "dummy.parquet"
        real_df_path = Path("dummy.dta")
        data = None

    # Patch get_test_data to return a DataFrame
    monkeypatch.setattr(
        "spml2.utils.get_test_data", lambda options: pd.DataFrame({"x": [1, 2]})
    )
    df = get_data(DummyOptions())
    assert isinstance(df, pd.DataFrame)
    assert "target" in df.columns
