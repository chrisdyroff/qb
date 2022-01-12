import yaml
import requests
import json

def read_config(file_path="config.yml"):
    with open(file_path) as f:
        return yaml.safe_load(f)


def get_tables(config, app_id):
    headers = {
        'QB-Realm-Hostname': config['realm'],
        'User-Agent': 'python client',
        'Authorization': f"QB-USER-TOKEN {config['user_token']}"
    }
    params = {
        'appId': app_id
    }
    r = requests.get(
    'https://api.quickbase.com/v1/tables', 
    params = params, 
    headers = headers
    )
    print(json.dumps(r.json(),indent=4))


def main():
    print('Getting tables in first configured app.')
    config = read_config()
    fist_app = config['apps'][0]
    get_tables(config, fist_app)

if __name__ == "__main__":
    main()