from spml2.options import Options
import subprocess
import sys
import os


def make_debug_true():
    file_name = "options_user.py"
    with open(file_name, "r") as f:
        content = ""
        lines = f.readlines()
        for line in lines:
            if "DEBUG =" not in line:
                content += line
            else:
                content += "DEBUG = True"
    with open(file_name, "w+") as f:
        f.write(content)


def test_process_initial():
    proc = subprocess.Popen(
        [sys.executable, "-m", "spml2.cli", "init", "-f"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    stdout, stderr = proc.communicate()
    print(stdout)
    if stderr:
        print("Error:", stderr)
    assert proc.returncode == 0

    assert os.path.exists("input/example.dta")
    assert os.path.exists("Output")
    assert os.path.exists("input/example.dta")

    make_debug_true()

    proc = subprocess.Popen(
        [sys.executable, "spml2_main.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    stdout, stderr = proc.communicate()
    print(stdout)
    if stderr:
        print("Error:", stderr)
    # assert proc.returncode == 0
