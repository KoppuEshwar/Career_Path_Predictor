import streamlit as st
import pickle

st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Luckiest+Guy&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

model = pickle.load(open('C:/xampp/htdocs/Project_Me/Career_Path_Predictor_Mini_Project_Sem_4/Models/rf_classifier.sav','rb'))
st.title("Career Path Predictor !")

st.header("Enter Your Answer with 'Yes' or 'No'")

display = ('No','Yes')

options = list(range(len(display)))
 
skills = ('poor','medium','excellent')

skill_options = list(range(len(skills)))

st1=st.form(key="form1")

ques1 = st1.number_input("Enter your GPA",value=0)

ques2=st1.selectbox("Did you do webdev during college time ?",options,format_func=lambda x: display[x])

ques3=st1.selectbox("Are you good at Data analysis ?",options,format_func=lambda x: display[x])

ques4=st1.selectbox("How would you Rate your Reading and Writing Skills",skill_options,format_func=lambda x: skills[x])

ques5=st1.selectbox("Are you a tech person ?",options,format_func=lambda x: display[x])

ques6=st1.selectbox("Were you in a non tech society ?",options,format_func=lambda x: display[x])

ques7=st1.selectbox("Are you good at coding ?",options,format_func=lambda x: display[x])

ques8=st1.selectbox("Have you developed mobile apps ?",options,format_func=lambda x: display[x])

ques9=st1.selectbox("Are you good at communication ?",options,format_func=lambda x: display[x])

ques10=st1.selectbox("Do you have specialization in security",options,format_func=lambda x: display[x])

ques11=st1.selectbox("Have you ever handled large databases ?",options,format_func=lambda x: display[x])

ques12=st1.selectbox("Do you have knowlege of statistics and data science?",options,format_func=lambda x: display[x])

ques13=st1.selectbox("Are you proficient in English ?",options,format_func=lambda x: display[x])

ques14=st1.selectbox("Have you ever managed some event?",options,format_func=lambda x: display[x])

ques15=st1.selectbox("Do you write technical blogs ?",options,format_func=lambda x: display[x])

ques16=st1.selectbox("Are you into marketing ?",options,format_func=lambda x: display[x])

ques17=st1.selectbox("Are you a ML expert ?",options,format_func=lambda x: display[x])

ques18=st1.selectbox("Do you have a lot of connections ?",options,format_func=lambda x: display[x])

ques19=st1.selectbox("Have you ever built live project ?",options,format_func=lambda x: display[x])

if st1.form_submit_button(label = "SUBMIT"):
    features = [[ques1,ques2,ques3,ques4,ques5,ques6,ques7,ques8,ques9,ques10,
    ques11,ques12,ques13,ques14,ques15,ques16,ques17,ques18,ques19]]
    print(features)
    prediction = model.predict(features)
    print(prediction)
    lc = [str(i) for i in prediction]
    ans = str("".join(lc))
    # st.success(ans)
    st.markdown(f"""
    <h1>{ans}</h1>
""", unsafe_allow_html=True)
    temp =  ans
    def display():
        if(temp == "Content Writer"):
            st.subheader('''What is content writing? 
            Image result for content writing
            Content writing is the process of writing, editing, and publishing content in a digital format. That content can include blog posts, video or podcast scripts, ebooks or whitepapers, press releases.
            Try improving these skills to ace : ) 
            Adaptability to different writing styles. ...
            Strong research skills. ...
            Creating original and creative content. ...
            Good understanding of SEO. ...
            Organization skills. ...
            Communication skills. ''')