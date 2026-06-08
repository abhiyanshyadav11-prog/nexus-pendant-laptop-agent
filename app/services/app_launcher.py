import subprocess

APPS = {
    "chrome": "start chrome",
    "vscode": "code",
}


def launch_app(app_name: str):
    app_name = app_name.lower()

    if app_name not in APPS:
        return False

    subprocess.Popen(APPS[app_name], shell=True)
    return True