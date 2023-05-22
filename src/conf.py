import os
import configparser
from dataclasses import dataclass
# from typing import AnyStr


@dataclass
class GenConf:
    bot_name: str
    token: str = ''

    def __post_init__(self):
        pars_config = configparser.ConfigParser()
        pars_config.read(os.path.abspath('../bots.ini'))
        self.token = pars_config['Bots'][self.bot_name]