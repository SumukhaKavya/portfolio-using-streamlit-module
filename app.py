import streamlit as st
st.set_page_config(page_title='My Portfolio', page_icon=':mortar_board:',layout='wide')
col1,col2=st.columns(2, gap="medium")
with col1:
    st.subheader("Hi, I am Sumukha Kavya :wave:")
    st.markdown('''
            <div style="display:flex; flex-direction: row;">
            <a href="https://www.linkedin.com/in/sumukha-kavya-477939243" style="padding-right: 10px;">
            <img src="https://img.icons8.com/color/48/000000/linkedin.png"/>
            </a>
            <a href="https://github.com/SumukhaKavya" style="padding-right: 10px;">
            <img src="https://img.icons8.com/color/48/000000/github.png"/>
            </a>
            <a href="mailto:daliparthysumukhakavya@gmail.com">
            <img src="https://img.icons8.com/color/48/000000/email.png"/>
            </a>
            </div>
            ''', unsafe_allow_html=True)
    st.image('capture.PNG')
    st.write('''Highly adaptive individual with problem solving skills, analytical skills, logical skills, teamwork, communication skills and keenly interested in
contributing to functional and technical design, as well as coding and testing software applications to meet business requirements.
''')
with col2:
    if 'active_tab' not in st.session_state:
         st.session_state.active_tab = 'About me'
    tabs=(["About me","My Skills","Education","Projects","Certifications"])
    active_tab = tabs.index(st.session_state.active_tab) if 'active_tab' in st.session_state else 0
    selected_tab = st.sidebar.radio('Select a tab', tabs, index=active_tab)
    if selected_tab=="About me":
        with st.container():
            st.header('About me')
            st.write(''' I am currently pursuing B.tech. in Computer Science and Engineering at Sastra University,Thanjavur.
            I like exploring and learning new technologies. Right now iam learning different technologies like Python, Mysql,Tableau, Html,CSS,Javascript,ReactJs.
            I have started doing projects based on these technologies.
            You can find my projects, skills, education details and certificates by clicking on below buttons.
            ''')
            button1=st.button('My Projects')
            if button1:
                st.session_state.active_tab = 'Projects'
            button2=st.button('Education Details')
            if button2:
                st.session_state.active_tab = 'Education'
            button3=st.button('Skills')
            if button3:
                st.session_state.active_tab = 'My Skills'
            button4=st.button('Certificates')
            if button4:
                st.session_state.active_tab = 'Certifications'


    if selected_tab=="Projects":
        with st.container():
            st.header('My Projects')
            st.subheader('Project 1:')
            st.subheader('Webscraping and data analysis of OYO Hotels in major Indian cities.')
            st.write('''Webscraping and extracting the data using beautiful soup and requests in python.The data set is constructed from the
                      data extracted about 6 different cities and data cleaning is done and further the data is analysed to get the insights
                      about the ratings,pricing and customer satisfaction on the oyo hotels.''')
            st.write("github link:")
            st.markdown('''
                            <a href="https://github.com/SumukhaKavya/Webscraping-and-data-analysis-of-oyo-hotels" style="padding-right: 10px;">
                            <img src="https://img.icons8.com/color/48/000000/github.png"/>
                            </a>''',unsafe_allow_html=True)
            st.subheader('Project 2:')
            st.subheader('Zomato Delivery Data Analysis Project')
            st.write('''Utilized Tableau to perform data analysis on Zomato delivery data answered several key questions by interpreting the data
                        and presenting the findings in a Tableau dashboard . Created a visually appealing and user-friendly dashboard that allows
                        for easy exploration of the data and demonstrated proficiency in data analysis and visualization using Tableau, as
                        well as familiarity with the Zomato delivery data and the restaurant industry.''')
            st.write("github link:")
            st.markdown('''
                            <a href="https://github.com/SumukhaKavya/Tableau-Dashboard" style="padding-right: 10px;">
                            <img src="https://img.icons8.com/color/48/000000/github.png"/>
                            </a>''',unsafe_allow_html=True)
            st.subheader('Project 3:')
            st.subheader('Frontend Application using React')
            st.write('''This is a Front End Application that uses the Unsplash API to retrieve images and display them to the user based on their search query. The application is built using React and utilizes routes, context, and hooks.''')
            st.write("github link:")
            st.markdown('''
                            <a href="https://github.com/SumukhaKavya/React-App" style="padding-right: 10px;">
                            <img src="https://img.icons8.com/color/48/000000/github.png"/>
                            </a>''',unsafe_allow_html=True)
            st.subheader('Project 4:')
            st.subheader('License Plate Detection')
            st.write('''License plate detection system to detect and recongnize the
                       license plates of cars using YOLOV3 algorithm.''')
            st.subheader('Project 5:')
            st.subheader('Multi-Keyword Secure Search')
            st.write('''A multi-keyword search system where in users can search and
                        retreive the files containing the requested keywords.''')
            
    if selected_tab=="My Skills":
        with st.container():
            st.header("Skills Progress")
            st.write("Here are my skills and their progress")
            skills = {'Python': 85, 'Java': 80, 'SQL': 90, 'HTML/CSS': 80, 'Javascript':80,'ReactJs':70}
            for skill, progress in skills.items():
              st.write(skill)
              st.progress(progress/100)

    if selected_tab=="Education":
        with st.container():
            st.header('Education Details:')
            choice=st.radio(
                "which Qualification would you like to see",
                ('SSC','Intermediate','Graduation')
            )
            if choice=='SSC':
                st.write("School: Raghunatha Model High School")
                st.write("Year of Passing: 2016")
                st.write("GPA: 9.8")
                
            if choice=='Intermediate':
                st.write("Name of college: Narayana Junior College")
                st.write("Year of Passing: 2018")
                st.write("percentage: 98.3%")

            if choice=='Graduation':
                st.write("Name of University: Sastra University")
                st.write("Year of Passing: 2023")
                st.write("CGPA: 7.8")      
    if selected_tab=="Certifications":
        with st.container():
            st.subheader("Certificates") 
            st.write("Udemy : Python Programming")   
            st.write("NPTEL: Introduction to Industry 4.0 and Industrial Internet of Things, Online Privacy")
            st.write("NPTEL: Development of Soft skills and Personality")
            st.write("Innomatics Research Labs: Exploratory Data Analysis Using Python Libraries")
            
            
