# Internet Speed Test

This small Python script measures your internet connection's download speed, upload speed, and ping using the Speedtest.net service.

Files
- `internet_speed.py` — Runs a Speedtest and prints:
  - Download Speed (Mbps)
  - Upload Speed (Mbps)
  - Ping (ms)

How it works
- The script uses the `speedtest` Python module (provided by the `speedtest-cli` package).
- It creates a `Speedtest()` object, calls `download()` and `upload()` which return bits-per-second, converts them to megabits-per-second (Mbps), rounds to 2 decimal places, and prints the results. The ping is read from `test.results.ping`.

Prerequisites
- Python 3.7 or newer installed and on your PATH.
- Internet access (the test contacts Speedtest.net servers).

Install (recommended: virtual environment)
Open PowerShell in the project folder (the folder that contains `internet_speed.py`) and run:

```powershell
# create a virtual environment
python -m venv venv

# (optional) If you get an execution policy error when activating, run the next line first to allow activation for this session
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

# activate the venv (PowerShell)
.\venv\Scripts\Activate.ps1

# install dependency from the included requirements file
pip install -r requirements.txt
```

Alternative without a virtual environment (global install):

```powershell
pip install speedtest-cli
```

Run
From PowerShell in the project folder (with the virtual environment activated if you used one):

```powershell
python .\internet_speed.py
```

Sample output

```
Download Speed in Mbps  123.45
Upload Speed in Mbps  45.67
Ping:  12.34
```

Notes and troubleshooting
- The test can take 20–60 seconds depending on network and chosen server.
- If you see `ModuleNotFoundError: No module named 'speedtest'`, make sure you installed `speedtest-cli` into the active Python environment.
- If activation fails due to execution policy, use the `Set-ExecutionPolicy` line shown above to temporarily bypass it for the session.
- Running as a non-administrator is usually fine; you only need elevated permissions if you modify system-wide Python installs.

License
- This repository contains a tiny utility. Use and modify freely.
