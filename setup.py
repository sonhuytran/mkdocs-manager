from setuptools import setup, find_packages

setup(
    name="mkdocs_manager",
    version="0.1",
    description="MkDocs Manager",
    packages=find_packages(exclude=[]),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mkman=app:main'
        ]
    },
    windows=[
        {
            'script': "app/__main__.py",
            'dest_base': 'bajoo',
            'icon_resources': [(0, "bajoo/assets/images/bajoo.ico")]
        }
    ],
    # test_suite='tests',
    # tests_require=['mock'],
)
