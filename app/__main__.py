import sys

# If this script is called without load the bajoo package
if __package__ == '':
    import os

    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

import app

if __name__ == '__main__':
    sys.exit(app.main())
