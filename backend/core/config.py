

import os
from dotenv import load_dotenv

load_dotenv()  

DB_USER = os.getenv("DB_USER", "pairuser")
DB_PASS = os.getenv("DB_PASS", "pairpass")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "pair_programming")
DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
