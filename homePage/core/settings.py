import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
LIB_DIR = os.path.join(BASE_DIR, 'example', 'lib')