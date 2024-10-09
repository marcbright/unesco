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
df_1 = pd.read_excel('UNESCO Technology Baseline Assesment.xlsx', engine='openpyxl')

st.markdown("### PRE-ASSESMENT DATA")
st.dataframe(df_1.head(), width=2000)

st.markdown("### BELOW ARE THE CHARTS FOR THE BASELINE ASSESMENT")

#Age Distribution
st.markdown("**A bar chart representing the Age Distribution**")
st.image("age.png")
age_counts = df_1["2. Age"].value_counts()
st.write(age_counts)

#Gender Distribution
st.markdown("**A bar chart representing the Gender Distribution**")
st.image("gender.png")
gender_counts = df_1["3. Gender"].value_counts()
st.write(gender_counts)


#Region of school
st.markdown("**A bar chart representing the total number of students per a Region**")
st.image("regionschool.png")
region_counts = df_1["7. Region of School"].value_counts()
st.write(region_counts)


st.markdown("**A bar chart representing the Current Grade Distribution**")
st.image("current_grade.png")
current_grade = df_1["6. Current Grade Level"].value_counts()
st.write(current_grade)


st.markdown("**A bar chart representing Devices Used for Online Studie**")
st.image("devices_used_online_studies.png")
devices_used_online_studies = df_1["If yes, what type of device do you use?"].value_counts()
st.write(devices_used_online_studies)


st.markdown("**A bar chart representing How Comfortable Are You With Using Digital Devices For Learning**")
st.image("confi_devices.png")
confi_devices = df_1["9. How comfortable are you with using digital devices for Learning?"].value_counts()
st.write(confi_devices)


st.markdown("**A bar chart representing Do You Have Internet Access?**")
st.image("internet_access.png")
internet_access = df_1["10. Do you have internet access?"].value_counts()
st.write(internet_access)

st.markdown("**A bar chart representing What Type Of Internet Access Do You Use?**")
st.image("if_yes_internet_access.png")
if_yes_internet_access = df_1[" If yes, what type of internet access do you use?"].value_counts()
st.write(if_yes_internet_access)


st.markdown("**A bar chart representing How Comfortable Are You Using The Internet To Access Information**")
st.image("internet_to_access_information.png")
internet_to_access_information = df_1["11. How comfortable are you using the internet to access information?"].value_counts()
st.write(internet_to_access_information)



st.markdown("**A bar chart representing What Is Your Preferred Learning Style**")
st.image("preferred_learning_style.png")
preferred_learning_style = df_1["12.What is your preferred learning style?"].value_counts()
st.write(preferred_learning_style)


st.markdown("**A bar chart representing Have You Used An Online Learning Platform Before**")
st.image("learning_platform_before.png")
learning_platform_before = df_1["13. Have you used an online learning platform before? "].value_counts()
st.write(learning_platform_before)


st.markdown("**A bar chart representing What Is Your Level Of Experience With Online Remote Learning Platforms**")
st.image("experience_with_online.png")
experience_with_online = df_1["14. What is your level of experience with online/remote learning platforms?"].value_counts()
st.write(experience_with_online)

#st.markdown("**A bar chart representing What are the main challenges you have faced or expect to face with online learning**")
#st.image("main_challenges.png")
#main_challenges = df_1["15. What are the main challenges you have faced (or expect to face) with online learning?"].value_counts()
#st.write(main_challenges)



st.markdown("**A bar chart representing Have you heard about the TeOSS project before?**")
st.image("teOSS_project_before.png")
teOSS_project_before = df_1["17. Have you heard about the TeOSS project before?"].value_counts()
st.write(teOSS_project_before)

st.markdown("**A bar chart representing What are your expectations for the TeOSS Learners Training Program?**")
st.image("your_expectations.png")
your_expectations = df_1["18. What are your expectations for the TeOSS Learners Training Program?"]
st.write(your_expectations)