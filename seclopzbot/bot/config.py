from dataclasses import dataclass
import json
from typing import List


@dataclass
class Config:
    '''Configuration parameters required for a `Bot` to operate.
    '''

    channels: List[str]
    new_hire_links: List[str]


    def load(file_path: str) -> 'Config':
        '''Load a bot configuration from a JSON file.
        '''

        with open(file_path) as cfg_file:
            return Config(**json.load(cfg_file))

