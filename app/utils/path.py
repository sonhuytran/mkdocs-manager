import os
from os import path
import sys

# region PATH CONSTANTS
CURRENT_PATH = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
APP_FOLDER = ""

if getattr(sys, 'frozen', None):
    APP_FOLDER = os.path.join(CURRENT_PATH, '..', '..', '..', 'app')
else:
    APP_FOLDER = os.path.join(CURRENT_PATH, '..')
PATH_ASSETS = os.path.join(APP_FOLDER, "assets")
PATH_IMAGES = os.path.join(PATH_ASSETS, "images")
PATH_LOCATE = os.path.join(APP_FOLDER, 'locale')
# endregion


# def get_icon(name, image_type):
#     file_name = os.path.join(PATH_IMAGES, name)
#     return wx.Icon(file_name, image_type)
#
#
# def get_image_path(name):
#     """Return the path of images and icons."""
#     return path.join(PATH_IMAGES, name)
#
#
# def get_app_icon_path():
#     """Return the path of the Bajoo .ico file."""
#     return get_image_path("bajoo.ico")
#
#
# def get_config_folder():
#     """Return the path of the Bajoo config folder.
#     The path differs between the different platforms.
#     """
#     if sys.platform.startswith('win'):
#         return appdirs.user_config_dir(appname='conf', appauthor='Bajoo2',
#                                        roaming=True)
#     else:
#         return appdirs.user_config_dir(appname='Bajoo2', appauthor='Bajoo2',
#                                        roaming=True)
#
#
#
# def get_image(name, image_type):
#     file_name = os.path.join(PATH_IMAGES, name)
#     return wx.Image(file_name, image_type)
#
#
# def get_bitmap_from_image(name, image_type):
#     file_name = os.path.join(PATH_IMAGES, name)
#     image = wx.Image(file_name, image_type)
#     return image.ConvertToBitmap()
#
#
# def application_icon_bw():
#     return get_icon("bajoo32_bw.png", wx.BITMAP_TYPE_PNG)
#
#
# def application_icon():
#     return get_icon("bajoo.ico", wx.BITMAP_TYPE_ICO)
#
#
# def create_dir_if_needed(directory):
#     """
#
#     :param directory:
#     :return: True if the directory exists or created successfully,
#     False if invalid path or system error.
#     """
#     try:
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#         return True
#     except OSError:
#         return False
#
#
# def get_config_file(name):
#     """Return the path of a config file"""
#     return path.join(get_config_folder(), name)
#
#
# def get_storage_config_file():
#     """Return the path of the storage config file"""
#     return path.join(get_config_folder(), "storage")
#
#
# def get_default_gpg_folder():
#     """returns the default path of the GPG folder."""
#     return path.join(get_config_folder(), 'gpg')
