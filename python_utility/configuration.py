from os.path import expanduser, isfile
from typing import Dict, Iterator, Union
from yaml import safe_load_all, dump


class Configuration:
    def __init__(self, path: str = ''):
        self.settings: Dict[str, str] = {}
        self.path = expanduser(path)

        if self.exists():
            input_file = open(self.path, 'r')
            self.add_elements(safe_load_all(input_file))
            input_file.close()

    def add_elements(self, elements: Iterator) -> None:
        for dictionary in elements:
            for key, value in dictionary.items():
                self.settings[key] = value

    def exists(self) -> bool:
        result = False

        if isfile(self.path):
            result = True

        return result

    def contains(self, key: str) -> bool:
        result = False

        if key in self.settings:
            result = True

        return result

    def get(self, key: str) -> str:
        return self.settings.get(key, '')

    def get_nested(self, key: str) -> dict:
        get_result: Union[str, Dict[str, str]] = self.settings.get(key, {})
        result: Dict[str, str]

        if isinstance(get_result, dict):
            result = get_result
        else:
            result = {}

        return result

    def set(self, key: str, value: str) -> None:
        self.settings[key] = value

    def remove(self, key: str) -> str:
        return self.settings.pop(key, '')

    def save(self) -> None:
        output_file = open(self.path, 'w')
        output_file.write(dump(self.settings, default_flow_style=False))
        output_file.close()
