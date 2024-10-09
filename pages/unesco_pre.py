import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st


logo_path = "pages/gi_logo.png"

# Display the logo
st.logo(logo_path, size="large", link = "https://gi-kace.gov.gh/")

st.markdown("## UNESCO Baseline and Post assesment")
df_1 = pd.read_excel('Book1.xlsx', engine='openpyxl')

st.markdown("### PRE-ASSESMENT DATA")
st.dataframe(df_1.head(), width=2000)

st.markdown("### BELOW ARE THE CHARTS FOR THE BASELINE ASSESMENT")

#Age Distribution
st.markdown("**A bar chart representing the Age Distribution**")
st.image("age.png")
age_counts = df_1["Age"].value_counts()
st.write(age_counts)

#Gender Distribution
st.markdown("**A bar chart representing the Gender Distribution**")
st.image("gender.png")
gender_counts = df_1["Gender"].value_counts()
st.write(gender_counts)


#Region
st.markdown("**A bar chart representing the total number of students per a Region**")
st.image("region_dis.png")
region_counts = df_1["Region of School"].value_counts()
st.write(region_counts)

#Devices
st.markdown("**A bar chart representing the devices used for Online Studies**")
st.image("devices_used.png")
devices_counts = df_1["If yes, what type of device do you use?"].value_counts()
st.write(devices_counts)


#Technology enabled
st.markdown("**A bar chart representing transitioning to technology-enabled learning**")
st.image("tech_enabled.png")
support_needs = df_1["What kind of support would you find most helpful in transitioning to technology-enabled learning?"].value_counts()
st.write(support_needs)

#Learning style
st.markdown("**A histogram chart representing preferred learning styles by gender**")
st.image("learning_style.png")
df_filtered = df_1[df_1['Have you used an online learning platform before?'] == 'Yes']

df_male = df_filtered[df_filtered['Gender'] == 'Male']
df_female = df_filtered[df_filtered['Gender'] == 'Female']

# Count preferred learning styles for males and females
male_counts = df_filtered[df_filtered['Gender'] == 'Male']['What is your preferred learning style?'].value_counts()
female_counts = df_filtered[df_filtered['Gender'] == 'Female']['What is your preferred learning style?'].value_counts()
st.text("Male")
st.write(male_counts)
st.text("Female")
st.write(female_counts)

# Print value counts for both genders
print("**Male Preferred Learning Styles:**")
print(male_counts)

print("\n**Female Preferred Learning Styles:**")
print(female_counts)

#TeOSS 
st.markdown("**A bar chart representing TeOSS awareness**")
st.image("teoss_aware.png")
teoss_awareness = df_1["Have you heard about the TeOSS project before?"]
st.write(teoss_awareness.value_counts())