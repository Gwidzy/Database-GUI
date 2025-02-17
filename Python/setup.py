from setuptools import setup
import os

APP = ['DUI.py']
DATA_FILES = [
    ('scripts', [os.path.join('tools', 'createTable.py'),
               os.path.join('tools', 'populateTable.py'),
               os.path.join('tools', 'renameTable.py'),
               os.path.join('tools', 'renameColumn.py')])
]
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'packages': ['rumps'],
    'plist': {
        'PyRuntimeLocations': [
            '@executable_path/../Frameworks/Python.framework/Versions/3.11/lib/libpython3.11.dylib',
            '/usr/local/Cellar/python@3.11/3.11.3/Frameworks/Python.framework/Versions/3.11/lib/libpython3.11.dylib',
        ],
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
