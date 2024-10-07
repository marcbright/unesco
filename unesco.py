import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st


logo_path = "gi_logo.png"

# Display the logo
st.logo(logo_path, size="large", link = "https://gi-kace.gov.gh/")


st.markdown("## UNESCO Baseline and Post assesment")
df_1 = pd.read_excel('Book1.xlsx', engine='openpyxl')
df_2 = pd.read_excel("UNESCOs_Technology_Enabled_Open_School_Project_TeOSS_Learners_Training_Program_Post-Training_Assessment_.xlsx")
df_drop = df_2.drop(["4. Grade/Class", "5. Region of School", "6. How would you rate the overall training experience?",
             "7. What aspects of the training did you enjoy most?", "8. Were the training objectives clearly communicated?", "9. How engaging did you find the training sessions?",
             "10. How effective were the trainers in delivering the content?", "11. How would you rate the training materials provided?", "12. What new skills or knowledge did you acquire from the training?", 
             "13. How confident do you feel in using technology for learning after the training?", "14. What challenges did you encounter while using technology during the training?",
             "15. How do you plan to apply what you learned in your studies?", "16. What topics would you like to see covered in future training sessions?",
             "17. Do you have any suggestions to improve the training program?", "18. Any additional comments or feedback?", "_id", "_uuid", "_submission_time", "_validation_status", 
             "_notes", "_status", "_submitted_by", "__version__", "_tags", "_index"], axis = 1, inplace=True)

st.markdown("### PRE-ASSESMENT DATA")
st.dataframe(df_1.head(), width=2000)


st.markdown("### POST-ASSESMENT DATA")
st.dataframe(df_2.head(), width=2000)

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

#POST ASSESMENT
#overall_experience
st.markdown("### BELOW ARE THE CHARTS FOR THE POST ASSESMENT")
st.markdown("**A bar chart representing the overall training experience**")
st.image("overall_experience.png")


#Overall
st.markdown("**A wordcloud chart showing the most frequent word typed for the overall training experience**")
st.image("aspect_training.png")

#OBJs
st.markdown("**A bar chart representing if training objectives clearly communicated**")
st.image("train_objs.png")

#Engagement
st.markdown("**A pie chart representing how engaging the training sessions**")
st.image("engagement.png")


#Effective Delivery
st.markdown("**A pie chart representing effective in deliverying of content**")
st.image("effective_deli.png")

#Training materials
st.markdown("**A bar chart representing the training materials provided**")
st.image("training_materials.png")


#New skills
st.markdown("**A wordcloud chart representing new skills or knowledge acquired from training**")
st.image("new_skills.png")


#Confident 
st.markdown("**A pie chart representing how confident using technology for learnig after the training**")
st.image("confi_using_tech.png")


#Topics 
st.markdown("**A pie chart representing topics likely to see covered in future training sessions**")
st.image("topics.png")
