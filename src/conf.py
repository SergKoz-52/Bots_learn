import os
import configparser

init_file = os.path.abspath('../bots.ini')
pars_config = configparser.ConfigParser()
pars_config.read(init_file)

print(pars_config['Bots']['spk1bot'])

