import math
import random
import numpy as np
from datetime import datetime
import os
from firebase_admin import credentials, firestore, initialize_app

# 'C:\\example\\cwd\\mydir\\myfile.txt'
notebook_path = os.path.abspath("cluster.ipynb")
cred = credentials.Certificate("fcmav1_key.json")
default_app = initialize_app(cred)
db = firestore.client()