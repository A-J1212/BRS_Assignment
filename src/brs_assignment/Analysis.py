from typing import Any, Optional
import matplotlib.pyplot as plt
import yaml
import requests


class Analysis():

    def __init__(self, analysis_config: str) -> None:
        CONFIG_PATHS = ['configs/system_config.yml', 'configs/user_config.yml']

        # add the analysis config to the list of paths to load
        paths = CONFIG_PATHS + [analysis_config]

        # initialize empty dictionary to hold the configuration
        config = {}

        # load each config file and update the config dictionary
        for path in paths:
            with open(path, 'r') as f:
                this_config = yaml.safe_load(f)
            config.update(this_config)

        self.config = config

    def load_data(self) -> None:
        with open('secrets.yml') as f:
            secrets = yaml.safe_load(f)
        
        # Example API request
        headers = {'Authorization': 'Bearer ' + secrets['key'], 
                    'Accept' : 'application/vnd.github+json'}
        url = 'https://api.github.com/user'
        data = requests.get(url).json()
        self.dataset = data


    def compute_analysis(self) -> Any:
        return self.dataset['public_repos'].count() 
        
    def plot_data(self, save_path: Optional[str] = None) -> plt.Figure:
        pass

    def notify_done(self, message: str) -> None:
        requests.post(f'https://ntfy.sh/{self.config["topicname"]}', data=message)
    

class Ahmad():
    def __init__(self):
        pass