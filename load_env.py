import json
from decouple import config

def update_zappy_settings():

    env_vars = {
        "DB_NAME": config('DB_NAME'),
        "DB_USER": config('DB_USER'),
        "DB_PASSWORD": config('DB_PASSWORD'),
        "DB_HOST": config('DB_HOST'),
        "DB_PORT": config('DB_PORT'),
        "CLOUD_NAME": config('CLOUD_NAME'),
        "API_KEY": config('API_KEY'),
        "API_SECRET": config('API_SECRET'),     
    }

    # load existing settings
    with open('zappa_settings.json', 'r') as file:
        zappa_settings = json.load(file)

    # update settings
    zappa_settings["production"]["environment_variables"] = env_vars

    print(zappa_settings)

    # write settings
    with open("zappa_settings.json", "w") as file:
        json.dump(zappa_settings, file, indent=4)

if __name__ == "__main__":
    update_zappy_settings()