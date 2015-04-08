__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

import sys
import json
import subprocess
import webbrowser
# python3: import urllib.parse as urlparse
# python3: import urllib.request as urlrequest
import urlparse
import urllib as urlrequest
from os import path

from .utils.log import getLogger, APP_FOLDER


def path2url(file_path):
    return urlparse.urljoin(
        'file:', urlrequest.pathname2url(file_path))


def main():
    logger = getLogger()
    logger.info("App Started")

    # Read config file
    config_path = path.join(APP_FOLDER, "mkdocs-console.json")
    html_path = path.join(APP_FOLDER, "index.html")

    try:
        config_file = open(config_path, "r")
        html_file = open(html_path, "w")
        data = json.load(config_file)
        config_file.close()
        logger.info("Data loaded successfully")

        for doc in data:
            subprocess.Popen(["mkdocs", "serve", "--dev-addr=127.0.0.1:" + str(doc["port"])],
                             cwd=doc["path"], shell=True)
            html_file.write("<a target='_blank' href='http://127.0.0.1:" + str(doc["port"]) + "'>" +
                            doc["path"] + "</a><br/>")

        html_file.close()

        html_url = path2url(path.abspath(html_path))
        webbrowser.open_new_tab(html_url)

    except (IOError, ValueError) as e:
        # file not exists, empty or corrupted file
        data = {}
        logger.error(e)

    logger.info("App Exitted")


if __name__ == '__main__':
    sys.exit(main())