import subprocess

setup_result = subprocess.run(
    "streamlit run Main.py", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
print(setup_result.stdout.decode())
