from tempfile import tempdir
from spml2.cli import init_user_files

from pathlib import Path

import subprocess
import sys
import subprocess
import sys
import time
import subprocess
import sys
import time
import os
import signal

import pytest


def test_init_user_files():
    folder = Path(tempdir)
    init_user_files(folder)

    # Check if the user files were created
    assert (folder / "models_user.py").exists()
    assert (folder / "options_user.py").exists()
    assert (folder / "spml2_main.py").exists()


@pytest.mark.skipif(
    sys.platform == "win32",
    reason="Streamlit does not support headless mode on Windows",
)
def test_spml2_web_starts_and_can_be_killed():
    # Start the process in a new process group
    proc = subprocess.Popen(
        [sys.executable, "-m", "spml2.cli", "web", "--server.headless", "true"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        preexec_fn=os.setsid,  # Only works on Unix (macOS/Linux)
    )
    try:
        time.sleep(5)
        assert proc.poll() is None
    finally:
        # Kill the whole process group
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
    outs, errs = proc.communicate()
    assert "Streamlit" in outs or "Streamlit" in errs
