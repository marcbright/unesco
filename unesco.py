import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st



unesco_pre_page = st.Page("pages/unesco_pre.py", title="Baseline Assesment", icon=":material/bar_chart:")
unesco_post_page = st.Page("pages/unesco_post.py", title="Post Assesment", icon=":material/bar_chart:")

pg = st.navigation([unesco_pre_page, unesco_post_page])
st.set_page_config(page_title="Unesco & GI-KACE", page_icon=":material/edit:")
pg.run()
