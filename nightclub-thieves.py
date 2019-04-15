import pandas as pd
import numpy as np
import lxml
from bs4 import BeautifulSoup

data = pd.read_table('Raw_Report.html')
table = BeautifulSoup(open('Raw_Report.html','r').read()).find('table')
data = pd.read_html(table)