import psutil

PROTECTED_APPS = [
    "Code.exe",
    "python.exe",
    "pythonw.exe",
    "cmd.exe",
    "powershell.exe",
    "explorer.exe"
]


APP_PROCESSES = {
    "chrome": "chrome.exe",
    "edge": "msedge.exe",
    "spotify": "spotify.exe",
    "notepad": "notepad.exe",
    "vscode": "Code.exe",
    "code": "Code.exe",
}


def close_app(app_name: str):
    app_name = app_name.lower()

    if app_name not in APP_PROCESSES:
        return f"{app_name} not found in registry"

    target_process = APP_PROCESSES[app_name]
    closed = False

    for proc in psutil.process_iter(["pid", "name"]):
        try:
            if proc.info["name"] == target_process:
                proc.kill()
                closed = True
        except:
            pass

    if closed:
        return f"Closed {app_name}"

    return f"{app_name} is not running"


def close_all_apps():
    closed_count = 0

    for proc in psutil.process_iter(["pid", "name"]):
        try:
            name = proc.info["name"]

            if not name:
                continue

            if name in PROTECTED_APPS:
                continue

            proc.kill()
            closed_count += 1

        except:
            pass

    return f"Closed {closed_count} processes"