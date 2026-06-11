from app.services.app_launcher import launch_app
from app.services.website_launcher import open_website
from app.services.system_control import lock_pc
from app.services.file_search import search_files
from app.services.file_opener import open_file
from app.services.command_parser import normalize_command
from app.services.search_memory import LAST_RESULTS
from app.services.volume_control import set_volume
from app.services.app_closer import close_all_apps,close_app

COMMANDS = {
    "open youtube": lambda: open_website("https://youtube.com"),
    "open github": lambda: open_website("https://github.com"),
    "lock pc": lambda: lock_pc(),
    "close all": lambda: close_all_apps(),
}


def execute_command(command: str):

    command = normalize_command(command)

    if command.startswith("find "):
        query = command.replace("find ", "")
        results = search_files(query)
        return results

    if command.startswith("open result "):

        try:
            index = int(command.replace("open result ", "")) - 1

            if index < 0 or index >= len(LAST_RESULTS):
                return "Invalid result number"

            return open_file(LAST_RESULTS[index])

        except:
            return "Invalid result number"

    if command.startswith("open file "):
        file_path = command.replace("open file ", "")
        return open_file(file_path)

    if command.startswith("open "):
        app_name = command.replace("open ", "")

        success = launch_app(app_name)

        if success:
            return f"Opened {app_name}"

        return f"Could not open {app_name}"

    if command in COMMANDS:
        COMMANDS[command]()
        return f"Executed: {command}"
    
    if command.startswith("volume "):

     try:

        percent = int(
            command.replace("volume ", "")
        )

        return set_volume(percent)

     except Exception as e:

        return str(e)
    

    if command == "close all":
      return close_all_apps()

    if command.startswith("close "):

       app_name = command.replace("close ", "").strip()

       return close_app(app_name)

    return "Unknown command"