# -*- coding: utf-8 -*-
# Created at 27/12/2021
__author__ = "MrKelpy / Alexandre Silva"
__github__ = "github.com/MrKelpy"
__copyright__ = "© Alexandre Silva 2021"
__license__ = "GNU GENERAL PUBLIC LICENSE v3"

# Built-in Imports
import traceback

# Third Party Imports
# Local Application Imports
from BackupCreator import BackupCreator
from BackupLogging import BackupLogging

if __name__ == "__main__":

    logger = BackupLogging()
    try:
        BackupCreator(logger).start()
    except:
        logger.log(traceback.format_exc(), "ERROR")