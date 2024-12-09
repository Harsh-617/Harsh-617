import streamlit as st
import pandas as pd

df = pd.read_csv("site_data.csv")

st.session_state.page = "Home"

# Sidebar menu to navigate between pages
page = st.sidebar.radio("Select a page", ["Home", "Contact"], index=0 if st.session_state.page == "Home" else 1)

st.session_state.page = page

if st.session_state.page == "Home":
    #st.title("Harsh Kudu")
    st.markdown("<div style='font-size:64px; text-align: center;'> <strong>Harsh Kudu</strong> </div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    with st.container():
        # Define two columns with different widths
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(r"C:\Users\LENOVO-PC\PycharmProjects\website1\images\image.png", width=180)

        with col2:
            # Use HTML to control text size and style
            st.markdown("""
                <div style="font-size:18px;">
                    <strong>About me:</strong><br>
                    Hi, my name is Harsh Kudu, and I am a 17-year-old student currently pursuing a Bachelor's (Hons) in Computer Science at Asia Pacific University, Malaysia.
                    My passion for technology has always driven me to explore and learn about the tech field, which is why I chose Computer Science as my path.
                    I have experience in Python programming and a basic understanding of HTML, CSS, and C++. I am eager to enhance my skills further and contribute to exciting projects in the tech world.
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <head><link href="https://fonts.googleapis.com/css2?family=Acme&display=swap" rel="stylesheet"></head>
    <style>.a { font-size:40px; font-family: 'Acme', sans-serif; border: 2px solid #52FF86; border-radius: 36px; padding: 10px 100px 10px 100px; color: white; background-color: #604EFF; display: inline-block; margin: 0 auto;}.center-container{text-align:center}
    </style>
    <div class="center-container">
        <div class="a">   My Projects   </div>
    </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br><br><br>", unsafe_allow_html=True)

    with st.container():
        st.title("1. To-Do App:")
        col1, col2 = st.columns([1,2])
        with col1:
            st.markdown("<br>", unsafe_allow_html=True)
            st.image(r'C:\Users\LENOVO-PC\PycharmProjects\website1\images\15.png',width=240)

            st.markdown("""
                <div style="text-align: center; padding-left: 50px;">
                    <button style="background-color: #604EFF; color: white; border: 2px solid #52FF86; border-radius: 36px; padding: 10px 20px;">
                        <a href="https://github.com/Harsh-617" target="_blank" style="text-decoration: none; color: white;">Button</a>
                    </button>
                </div>
                """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div style="font-size:18px;">
                <ul style="list-style-type: circle;">
                <strong>Description:</strong><br>
                A productivity-boosting ToDo app made using Python. It allows users to store, delete, edit daily tasks, and view timestamps.<br>                Versions:<br>
                <li>Command Line: Runs on terminal/command line.</li>
                <li>Desktop: Built with PySimpleGUI, runs on desktop.</li>
                <li>Web App: Deployed on the cloud using Streamlit.</li>
                This app helps manage daily tasks efficiently, enhancing productivity.
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<br><br><br><br>", unsafe_allow_html=True)

    with st.container():
        st.title("2. File Management System:")

        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
                <div style="font-size:18px;">
                <ul style="list-style-type: circle;">
                <strong>Description:</strong><br>
                A command-line file management system made using Python, utilizing modules like os, shutil and logging.<br> Features:<br>
                <li>Create/Delete: Easily create and delete files and directories.</li>
                <li>Segregation: Automatically segregates files by extension into specific directories, creating directories if they don’t exist.</li>
                <li>Unique Naming: Checks for existing file/directory names and generates unique names to avoid conflicts.</li>
                This system significantly saves time by organizing files efficiently.
                </div>
                """, unsafe_allow_html=True)

        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            st.image(r'C:\Users\LENOVO-PC\PycharmProjects\website1\images\18.png',width=240)
            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown("""
                <div style="text-align: center; padding-left: 50px;">
                    <button style="background-color: #604EFF; color: white; border: 2px solid #52FF86; border-radius: 36px; padding: 10px 20px;">
                        <a href="https://github.com/Harsh-617" target="_blank" style="text-decoration: none; color: white;">Button</a>
                    </button>
                </div>
                """, unsafe_allow_html=True)

#The target="_blank" attribute in an HTML <a> (anchor) tag tells the browser to open the linked document in a new tab or window

    st.markdown("<br><br><br><br>", unsafe_allow_html=True)

    with st.container():
        st.title("3. Diary App:")

        col1, col2 = st.columns([1,2])
        with col1:
            st.markdown("<br>", unsafe_allow_html=True)
            st.image(r'C:\Users\LENOVO-PC\PycharmProjects\website1\images\11.png',width=230)
            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown("""
                <div style="text-align: center; padding-left: 50px;">
                    <button style="background-color: #604EFF; color: white; border: 2px solid #52FF86; border-radius: 36px; padding: 10px 20px;">
                        <a href="https://github.com/Harsh-617" target="_blank" style="text-decoration: none; color: white;">Button</a>
                    </button>
                </div>
                """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div style="font-size:18px;">
                <ul style="list-style-type: circle;">
                <strong>Description:</strong><br>
                A Python-based command-line personal diary application designed to help users create and manage their diary entries directly from the terminal.<br> Features:<br>
                <li>Adding Entries</li>
                <li>Viewing Entries</li>
                <li>Viewing Entry Content</li>
                <li>Searching Entries</li>
                <li>Deleting Entries</li>
                Data Storage: Diary entries are stored in text files, ensuring that your data is easily accessible and manageable. The table columns for diary entries include:<br>
                <li>Title: A brief title or subject for the diary entry, providing a quick overview of what the entry is about.</li>
                <li>Content: The main content of the diary entry, containing your thoughts, reflections, or any information you want to record.</li>
                This diary app is a practical tool for anyone looking to maintain a personal diary, offering a straightforward way to document and manage your daily experiences
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<br><br><br><br>", unsafe_allow_html=True)

    with st.container():
        st.title("4. YouTube Video Downloader:")

        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
                <div style="font-size:18px;">
                <ul style="list-style-type: circle;">
                <strong>Description:</strong><br>
                A command-line YouTube video downloader made using the yt_dlp library.<br> Features:<br>
                <li>Input Link: Provide the video link to download.</li>
                <li>Customizable Options: Customize download options to suit your needs.</li>
                This tool efficiently downloads videos from YouTube, offering flexibility and ease of use.
                </div>
                """, unsafe_allow_html=True)

        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            st.image(r'C:\Users\LENOVO-PC\PycharmProjects\website1\images\7.png',width=235)
            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown("""
                <div style="text-align: center; padding-left: 50px;">
                    <button style="background-color: #604EFF; color: white; border: 2px solid #52FF86; border-radius: 36px; padding: 10px 20px;">
                        <a href="https://github.com/Harsh-617" target="_blank" style="text-decoration: none; color: white;">Button</a>
                    </button>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<br><br>", unsafe_allow_html=True)

    with st.container():
        st.markdown("""
        <head><link href="https://fonts.googleapis.com/css2?family=Acme&display=swap" rel="stylesheet"></head>
        <style>.a { font-size:40px; font-family: 'Acme', sans-serif; border: 2px solid #52FF86; border-radius: 36px; padding: 1px 150px 1px 150px; color: white; background-color: #604EFF; display: inline-block; margin: 0 auto;}.center-container{text-align:center}
        </style>
        <div class="center-container">
            <div class="a">   My Projects   </div>
        </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><br><br>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1,1,1])

        card_style = """
        <style>
            .card { font-size: 20px; font-family: 'Acme', sans-serif;
                    border: 2px solid #52FF86; border-radius: 15px;
                    padding: 15px; color: black; background-color: #d3d3d3;
                    text-align: center, margin-bottom: 20px;
                    height: 250px; display: flex; flex-direction: column; justify-content: center;
                    position: relative; text-decoration: none }
            .card:hover { box-shadow: 0px 4px 8px rgba(0,0,0,0.2)}
            .card h3, .card p {margin: 0; position relative; z-index: 1}
            .card a {position:absolute; top:0; left:0; right:0; bottom:0; z-index:0}
        </style>"""

# The z-index property in CSS controls the stacking order of elements that overlap
# z-index: 1 will be on top of the other boxes.
# z-index: 0 will be in the middle.
# z-index: -1 will be at the bottom.

#The box-shadow: 0px 4px 8px rgba(0,0,0,0.2); property in CSS adds a shadow effect to an element, making it look like it’s lifted off the page.
#0px (Horizontal Offset): This sets the horizontal distance of the shadow. A value of 0px means the shadow is directly under the element, with no horizontal shift.
#4px (Vertical Offset): This sets the vertical distance of the shadow. A value of 4px means the shadow is shifted 4 pixels down from the element
#8px (Blur Radius): This determines how blurry the shadow is. A value of 8px creates a moderately blurred shadow. The higher the number, the more blurred the shadow will be
#rgba(0,0,0,0.2) (Color): This sets the color of the shadow. rgba(0,0,0,0.2) means the shadow is black (rgb(0,0,0)) with 20% opacity (0.2), making it semi-transparent.


        st.markdown(card_style, unsafe_allow_html=True)

        def project_card(project_name, description, link):
            return f"""
            <div class='card'>
                <a href='{link}' target='_blank'></a>
                <h3>{project_name}</h3>
                <p>{description}</p>
            </div>
            """

# df.iloc[0]: This is using pandas to select the first row of the DataFrame df. .iloc[0] is the method used to access the first row based on its index.
#['Project Name'], ['Description'], ['Link']: These are accessing specific columns in the DataFrame for the first row.

        with col1:
            st.markdown(project_card(df.iloc[0]['Project Name'], df.iloc[0]['Description'], df.iloc[0]['Link']),unsafe_allow_html=True)

        with col2:
            st.markdown(project_card(df.iloc[1]['Project Name'], df.iloc[1]['Description'], df.iloc[1]['Link']),unsafe_allow_html=True)

        with col3:
            st.markdown(project_card(df.iloc[2]['Project Name'], df.iloc[2]['Description'], df.iloc[2]['Link']),unsafe_allow_html=True)

            st.markdown(" ")
            st.markdown(" ")

        col1, col2, col3 = st.columns([1,1,1])

        with col1:
            st.markdown(project_card(df.iloc[3]['Project Name'], df.iloc[3]['Description'], df.iloc[3]['Link']),unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <style>.c { font-size:40px; font-family: 'Acme',sans-serif ; border: 2px solid #52FF86; border-radius: 36px; padding: 150px 100px 150px 100px; color: black; background-color: grey; display: inline-block; margin: 0 auto;}.center-container{text-align:center}
            </style>
            <div class="center-container">
                <div class="c"> </div>
            </div>
                """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <style>.c { font-size:40px; font-family: 'Acme',sans-serif ; border: 2px solid #52FF86; border-radius: 36px; padding: 150px 100px 150px 100px; color: black; background-color: grey; display: inline-block; margin: 0 auto;}.center-container{text-align:center}
            </style>
            <div class="center-container">
                <div class="c"> </div>
            </div>
                """, unsafe_allow_html=True)

        st.markdown("<br><br><br><br>", unsafe_allow_html=True)

        import streamlit.components.v1 as components

        components.html("""
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            <style>
            .H {
                border: 1px;
                padding: 1px;
                background-color: #1AE83C;
                text-align: center;
            }
            .small-text {
                font-size: 24px;
            }
            
/* display: flex; property in CSS is used to create a flex container, which enables a flexible box layout model  */

  /*  Once you have a flex container, you can use various properties to control the layout of the flex items: */
  /*  flex-direction: Defines the direction of the flex items (row, column, etc.). */
  /*  justify-content: Aligns the flex items along the main axis (left, right, center, space-between, etc.). */
  /*  align-items: Aligns the flex items along the cross axis (top, bottom, center, stretch, etc.). */
  /*  flex-wrap: Controls whether the flex items should wrap onto multiple lines.      */     
            
            .columns {
                display: flex;
                justify-content: center;
                color:black
            }
            
/* flex-grow: 0;: This means the flex item will not grow to fill available space in the flex container. */
/* flex-shrink: 0;: This means the flex item will not shrink if there is not enough space in the flex container. */
/* flex-basis: auto;: This sets the initial size of the flex item based on its content or any width/height properties set on it   */         
            
            .column {
                flex: 0 0 auto; /* flex-grow , flex-shrink , flex-basis */
                padding: 10px;
                margin: 0 5px; text-align:center
            }
            .fs i {
              font-size:36px;
              color:black
            }
            </style>
            <div class="H">
                <h1>This is all about me.</h1>
                <p class="small-text">Thank you</p>
                <div class="columns">
                    <div class="column"> <div class="fs"> <a href="https://github.com/Harsh-617" target="_blank"> <i class="fab fa-github" aria-hidden="true"></i> </a> </div></div>
                    <div class="column"> <div class="fs"> <a href="https://www.linkedin.com/in/yourusername" target="_blank"> <i class="fas fa-envelope" aria-hidden="true"></i> </a> </div></div>
                    <div class="column"> <div class="fs"> <a href="mailto:harshkudu67@gmail.com"> <i class="fab fa-linkedin" aria-hidden="true"></i> </a> </div></div>
                </div>
                <div>2024 | Harsh Kudu</div>
            </div>
            """, height=400)


elif st.session_state.page == "Contact":

    col1, col2 = st.columns([3, 4])

    with col1:
        st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            .heading {
                font-size: 32px;
                font-family: 'Poppins', sans-serif;
                color: #A91079;
                line-height: 1.4;
            }
        </style>
        <div class="heading">Let's discuss<br>something cool<br>together</div>
        """, unsafe_allow_html=True)

        st.markdown(" ")
#The rel attribute specifies the relationship between the HTML document and the linked resource. stylesheet indicates that the linked resource is a CSS file
        st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <style>
            .outer-border {
                border: 3px solid #A91079;
                border-radius: 20px;
                padding: 10px;
                background-color: #E846AF;
                width: 280px;
            }
            .inner-border {
                border: 2px solid #A91079;
                border-radius: 28px;
                padding: 10px;
                background-color: #ffffff;
                margin-bottom: 15px;
                text-align: center;
                color: #A91079;
                font-family: 'Poppins', sans-serif;
                width: 257px;
                margin: 0 auto;
            }
            .inner-border:last-child {
                margin-bottom: 0;
            }
            .icon {
                margin-right: 10px;
            }
        </style>
        <div class="outer-border">
            <div class="inner-border">
                <i class="fa-solid fa-envelope icon"></i>harshkudu67@gmail.com
            </div><br>
            <div class="inner-border">
                <i class="fa-solid fa-phone icon"></i>+91 9309564620
            </div><br>
            <div class="inner-border">
                <i class="fa-solid fa-location-dot icon"></i>Mumbai, India
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(" ")
        st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <style>
            .form-container {
                border: 3px solid #A91079;
                padding: 20px;
                background-color: #E846AF;
                border-radius: 36px;
                color: white;
                font-family: 'Poppins', sans-serif;
                width: 300px; height: 400px;  
                position: relative;
            }
            .form-item {
                margin-bottom: 30px;
                font-weight: 600;
                font-size: 16px;
            }
            .send-button {
                border: 2px solid #A91079;
                border-radius: 28px;
                padding: 10px;
                background-color: #ffffff;
                color: #A91079;
                font-weight: 600;
                text-align: center;
                cursor: pointer;
                margin-top: 20px;
            }
            .icon-container {
                position: absolute;
                bottom: 10px;
                left: 50%;
                transform: translateX(-50%); /* moves an element horizontally by 50% of its own width to the left */
                display: flex;
                gap: 20px;
            }
            .icon-container i {
                font-size: 28px;
                color: white;
                cursor: pointer;
            }
        </style>
        <div class="form-container">
            <div class="form-item">Your Name:</div>
            <div class="form-item">Your Email:</div>
            <div class="form-item">Your Message:</div>
            <div class="send-button">Send Message</div>
            <div class="icon-container">
                <a href="https://github.com/Harsh-617" target="_blank">
                    <i class="fab fa-github"></i>
                </a>
                <a href="https://www.linkedin.com/in/yourusername" target="_blank">
                    <i class="fab fa-linkedin"></i>
                </a>
                <a href="harshkudu67@gmail.com">
                    <i class="fa-solid fa-envelope"></i>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)

