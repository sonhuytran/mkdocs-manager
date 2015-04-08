__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

import sys

from .utils.log import getLogger


def main():
    logger = getLogger()
    logger.info("App Started")

    logger.info("App Exitted")


if __name__ == '__main__':
    sys.exit(main())