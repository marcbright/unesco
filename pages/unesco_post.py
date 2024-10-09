import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st


logo_path = "pages/gi_logo.png"

# Display the logo
st.logo(logo_path, size="large", link = "https://gi-kace.gov.gh/")

df_2 = pd.read_excel("UNESCOs_Technology_Enabled_Open_School_Project_TeOSS_Learners_Training_Program_Post-Training_Assessment_.xlsx")
df_drop = df_2.drop(["4. Grade/Class", "5. Region of School", "6. How would you rate the overall training experience?",
             "7. What aspects of the training did you enjoy most?", "8. Were the training objectives clearly communicated?", "9. How engaging did you find the training sessions?",
             "10. How effective were the trainers in delivering the content?", "11. How would you rate the training materials provided?", "12. What new skills or knowledge did you acquire from the training?", 
             "13. How confident do you feel in using technology for learning after the training?", "14. What challenges did you encounter while using technology during the training?",
             "15. How do you plan to apply what you learned in your studies?", "16. What topics would you like to see covered in future training sessions?",
             "17. Do you have any suggestions to improve the training program?", "18. Any additional comments or feedback?", "_id", "_uuid", "_submission_time", "_validation_status", 
             "_notes", "_status", "_submitted_by", "__version__", "_tags", "_index"], axis = 1, inplace=True)




st.markdown("### POST-ASSESMENT DATA")
st.dataframe(df_2.head(), width=2000)



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
