import requests
from bs4 import BeautifulSoup
from typing import Dict, Any

class Email:
    def __init__(self):
        self._base_url = "https://www.invertexto.com/gerador-email-temporario?email="
        self._end_url = "@uorak.com"
