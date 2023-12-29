from os import path, listdir
import streamlit as st
from streamlit_embedcode import github_gist
import streamlit.components.v1 as com
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pdfplumber
import streamlit as st
import pandas as pd
import numpy as np
import re
import string
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords 
from string import punctuation
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
from nltk.collocations import *
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from streamlit_option_menu import option_menu
from os import path, listdir
import glob
import pickle
from pathlib import Path
from plotly import graph_objs as go
from collections import Counter
from sklearn.metrics.pairwise import linear_kernel
from st_material_table import st_material_table
import streamlit as st
import pandas as pd
import pickle
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import streamlit.components.v1 as components

# page title
if (selected == 'Prediction Penyakit Diabetes'):
            with open('style.css') as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
            st.title('Prediction Penyakit Jantung')
            col1, col2, col3 = st.columns(3)
            with col1:
                age = st.number_input('Umur')
            with col2: 
                sex = st.number_input('Jenis Kelamin (1 = laki-laki; 0 = perempuan)')
            with col3:
                cp = st.number_input('Chest Pain types (0 = typical, 1 = asymptotic, 2 = nonanginal, 3 = nontypical)')
            with col1:
                trestbps = st.number_input('Resting Blood Pressure')
            with col2:
                chol = st.number_input('Serum Cholestoral in mg/dl')
            with col3:
                fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = benar; 0 = salah)')
            with col1:
                restecg = st.number_input('Resting Electrocardiographic results')
        
            with col2:
                thalach = st.number_input('Maximum Heart Rate achieved')
            with col3:
                exang = st.number_input('Exercise Induced Angina (1 = ya; 0 = tidak)')  
            with col1:
                oldpeak = st.number_input('ST depression induced by exercise')
            with col2:
                slope = st.number_input('Slope of the peak exercise ST segment')
            with col3:
                ca = st.number_input('Major vessels colored by flourosopy (0 - 3)')
            with col1:
                thal = st.number_input('thal: 1 = normal; 2 = fixed defect; 3 = reversable defect')
