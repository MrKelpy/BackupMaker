# -*- coding: utf-8 -*-
# Created at 28/12/2021
__author__ = "MrKelpy / Alexandre Silva"
__github__ = "github.com/MrKelpy"
__copyright__ = "© Alexandre Silva 2021"
__license__ = "GNU GENERAL PUBLIC LICENSE v3"

# Built-in Imports
import os

# Third Party Imports
import py7zr

# Local Application Imports
from BackupConfigs import BackupConfigs
from BackupLogging import BackupLogging


class BackupCreator(BackupConfigs):
    """
    This class implements the actual program operations that perform the backup.
    """

    def __init__(self, logger: BackupLogging):
        super().__init__()
        self.__settings = self.load_settings()
        self.__logger = logger
        self.__backup_path = os.path.join(self.__settings["backup_path"], self.__logger.session + ".7z")
        os.makedirs(self.__settings["backup_path"], exist_ok=True)


    def start(self):
        """
        Performs a backup of the specified folders, and transfers them to a 7z
        :return:
        """

        with py7zr.SevenZipFile(self.__backup_path, "w") as archive:

            # Adds all the paths in the folders setting to the 7z file.
            for path in self.__settings["backup_folders"]:
                archive.writeall(path)
                self.__logger.log(f"Backed up {path} into {self.__backup_path}.")

        if self.__settings["backup_restart"] == "True":
            os.system("shutdown -s -t 0")