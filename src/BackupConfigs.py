# -*- coding: utf-8 -*-
# Created at 27/12/2021
__author__ = "MrKelpy / Alexandre Silva"
__github__ = "github.com/MrKelpy"
__copyright__ = "© Alexandre Silva 2021"
__license__ = "GNU GENERAL PUBLIC LICENSE v3"

# Built-in Imports
import os
import requests

# Third Party Imports
from bs4 import BeautifulSoup

# Local Application Imports


class BackupConfigs:
    """
    This class implements a way for the program to read the config file and
    for it to be used in the program.
    """

    def __init__(self):
        self.__config_path = fr"./backup.config"


    def load_settings(self):
        """
        Parses the settings config file into a dictionary to be used in the server run.
        :return:
        """
        with open(self.__config_path, "r") as config_file:
            settings = config_file.readlines()

        # Ignores any "#" or "//" starting lines or any empty strings in the lines.
        filtered_settings = [setting.strip() for setting in settings
                             if not setting.startswith("#")
                             and not setting.startswith("//")
                             and setting.strip() != ""]

        # Creates the dictionary by splitting the settings by the "="
        # and assigning the leftmost part to the value, and the rightmost to the key.
        settings_dictionary = dict()
        for setting in filtered_settings:
            key_value_setting = setting.split("=")
            key = key_value_setting[0].lower().strip()
            value = key_value_setting[1].strip()

            # Replaces the value for a list of values if it's separated by semicolons.
            # Validates if the path exists, and if the string isn't empty.
            if ";" in value:
                value = [x.strip() for x in value.split(";") if x and os.path.exists(x)]

            settings_dictionary[key] = value

        return settings_dictionary


    def __ensure_config_existance(self):
        """
        Ensures the existance of a config.mcsm file.
        :return:
        """

        # Checks if the config.mcsm file exists. If not, check the template on GitHub
        # and create the file.
        if not os.path.isfile(self.__config_path):
            config_template = self.__get_config_file()

            with open(self.__config_path, "w") as config_file:
                config_file.write(config_template)


    @staticmethod
    def __get_config_file():
        """
        Gets the config template from github.
        :return:
        """

        config_template_url = "https://github.com/MrKelpy/BackupMaker/blob/master/resources/CFG_TEMPLATE.txt"
        data = requests.get(config_template_url)
        soup = BeautifulSoup(data.text, "html.parser")
        config_template = ""

        for line in soup.find_all("tr"):
            config_template += f"{line.text.strip()}\n"

        return config_template