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
st.markdown("**A bar chart representing the Overall Training Experience**")
st.image("training_experience.png")
training_experience = df_2["7. How would you rate the overall training experience?"].value_counts()
st.write(training_experience)



st.markdown("**A wordcloud chart representing What Aspects Of The Training Did You Enjoy Most**")
st.image("training_you_enjoy_most.png")
training_you_enjoy_most = df_2["8. What aspects of the training did you enjoy most?"].value_counts()
st.write(training_you_enjoy_most)


st.markdown("**A bar chart representing Were The Training Objectives Clearly Communicated?**")
st.image("training_objectives.png")
training_objectives = df_2["9. Were the training objectives clearly communicated?"].value_counts()
st.write(training_objectives)


st.markdown("**A bar chart representing How Engaging Did You Find The Training Sessions?**")
st.image("engaging_training_sessions.png")
engaging_training_sessions = df_2["10. How engaging did you find the training sessions?"].value_counts()
st.write(engaging_training_sessions)


st.markdown("**A bar chart representing How Effective Were The Trainers In Delivering The Content?**")
st.image("effective_delivering_the_content.png")
effective_delivering_the_content = df_2["11. How effective were the trainers in delivering the content?"].value_counts()
st.write(effective_delivering_the_content)


st.markdown("**A bar chart representing How Would You Rate The Training Materials Provided?**")
st.image("training_materials_provided.png")
training_materials_provided = df_2["12. How would you rate the training materials provided?"].value_counts()
st.write(training_materials_provided)


st.markdown("**A wordcloud chart representing What New Skills Or Knowledge Did You Acquire From The Training**")
st.image("new_skills_or_knowledge.png")
new_skills_or_knowledge = df_2["13. What new skills or knowledge did you acquire from the training?"].value_counts()
st.write(new_skills_or_knowledge)


st.markdown("**A bar chart representing How Confident Do You Feel In Using Technology For Learning After The Training?**")
st.image("confident_using_technology_after_training.png")
confident_using_technology_after_training = df_2["14. How confident do you feel in using technology for learning after the training?"].value_counts()
st.write(confident_using_technology_after_training)



st.markdown("**A wordcloud chart representing What Challenges Did You Encounter While Using Technology During The Training**")
st.image("challenges_encounter.png")
challenges_encounter = df_2["15. What challenges did you encounter while using technology during the training?"].value_counts()
st.write(challenges_encounter)


st.markdown("**A wordcloud chart representing How Do You Plan To Apply What You Learned In Your Studies**")
st.image("learned_in_studies.png")
learned_in_studies = df_2["16. How do you plan to apply what you learned in your studies?"].value_counts()
st.write(learned_in_studies)


st.markdown("**A wordcloud chart representing What Topics Would You Like To See Covered In Future Training Sessions**")
st.image("topics_in_future_training_sessions.png")
topics_in_future_training_sessions = df_2["17. What topics would you like to see covered in future training sessions?"].value_counts()
st.write(topics_in_future_training_sessions)


st.markdown("**A wordcloud chart representing Do You Have Any Suggestions To Improve The Training Program**")
st.image("suggestions_to_improve.png")
suggestions_to_improve = df_2["18. Do you have any suggestions to improve the training program?"].value_counts()
st.write(suggestions_to_improve)


