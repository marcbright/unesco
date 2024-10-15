import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
import csv


logo_path = "pages/gi_logo.png"

# Display the logo
st.logo(logo_path, size="large", link = "https://gi-kace.gov.gh/")

#st.markdown("## UNESCO Baseline and Post assesment")
#df_1 = pd.read_excel('UNESCO Technology Baseline Assesment.xlsx', engine='openpyxl')


df_1 = pd.read_csv('unesco_cleaned_data.csv')
st.dataframe(df_1)

#st.markdown("### PRE-ASSESMENT DATA")
#st.dataframe(df_1.head(), width=2000)

st.markdown("### BELOW ARE THE CHARTS FOR THE BASELINE ASSESMENT")

#Age Distribution
st.markdown("**A bar chart representing the Age Distribution**")
st.image("age.png")
age_counts = df_1["age"].value_counts()
st.write(age_counts)

#Gender Distribution
st.markdown("**A bar chart representing the Gender Distribution**")
st.image("gender.png")
gender_counts = df_1["gender"].value_counts()
st.write(gender_counts)


#Region of school
st.markdown("**A bar chart representing the total number of students per a Region**")
st.image("regionschool.png")
region_counts = df_1["region_of_School"].value_counts()
st.write(region_counts)


st.markdown("**A bar chart representing the Current Grade Distribution**")
st.image("current_grade.png")
current_grade = df_1["current_grade_level"].value_counts()
st.write(current_grade)


st.markdown("**A bar chart representing Devices Used for Online Studie**")
st.image("devices_used_online_studies.png")
devices_used_online_studies = df_1["if_yes_what_type_of_device_do_you_use?"].value_counts()
st.write(devices_used_online_studies)


st.markdown("**A bar chart representing How Comfortable Are You With Using Digital Devices For Learning**")
st.image("confi_devices.png")
confi_devices = df_1["how_comfortable_are_you_with_using_digital_devices_for_Learning?"].value_counts()
st.write(confi_devices)


st.markdown("**A bar chart representing Do You Have Internet Access?**")
st.image("internet_access.png")
internet_access = df_1["do_you_have_internet_access?"].value_counts()
st.write(internet_access)

st.markdown("**A bar chart representing What Type Of Internet Access Do You Use?**")
st.image("if_yes_internet_access.png")
if_yes_internet_access = df_1["if_yes_what_type_of_internet_access_do_you_use?"].value_counts()
st.write(if_yes_internet_access)


st.markdown("**A bar chart representing How Comfortable Are You Using The Internet To Access Information**")
st.image("internet_to_access_information.png")
internet_to_access_information = df_1["how_comfortable_are_you_using_the_internet_to_access_information?"].value_counts()
st.write(internet_to_access_information)



st.markdown("**A bar chart representing What Is Your Preferred Learning Style**")
st.image("preferred_learning_style.png")
preferred_learning_style = df_1["what_is_your_preferred_learning_style?"].value_counts()
st.write(preferred_learning_style)


st.markdown("**A bar chart representing Have You Used An Online Learning Platform Before**")
st.image("learning_platform_before.png")
learning_platform_before = df_1["have_you_used_an_online_learning_platform_before?"].value_counts()
st.write(learning_platform_before)


st.markdown("**A bar chart representing What Is Your Level Of Experience With Online Remote Learning Platforms**")
st.image("experience_with_online.png")
experience_with_online = df_1["what_is_your_level_of_experience_with_online_remote_learning_platforms?"].value_counts()
st.write(experience_with_online)

#st.markdown("**A bar chart representing What are the main challenges you have faced or expect to face with online learning**")
#st.image("main_challenges.png")
#main_challenges = df_1["15. What are the main challenges you have faced (or expect to face) with online learning?"].value_counts()
#st.write(main_challenges)



st.markdown("**A bar chart representing Have you heard about the TeOSS project before?**")
st.image("teOSS_project_before.png")
teOSS_project_before = df_1["have_you_heard_about_the_TeOSS_project_before?"].value_counts()
st.write(teOSS_project_before)

st.markdown("**A bar chart representing What are your expectations for the TeOSS Learners Training Program?**")
st.image("your_expectations.png")
your_expectations = df_1["what_are_your_expectations_for_the_TeOSS_Learners_Training_Program?"]
st.write(your_expectations)