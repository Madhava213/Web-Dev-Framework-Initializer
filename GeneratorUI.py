import streamlit as st
import subprocess

###### Installing Standard Libraries  #####
def library_install(name,sass,framer,react_icons,materialUI,victory, react_reveal, react_spring, express, boron, animejs, cors, stripe, nodemon, react_hook_form, react_hook_error, nodemailer, axios, recaptcha, bodyparser, dotenv  ):
    if(sass):
        setup_result = subprocess.run("npm install sass --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(framer):
        setup_result = subprocess.run("npm install framer-motion --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(react_icons):
        setup_result = subprocess.run("npm install react-icons --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(materialUI):
        setup_result = subprocess.run("npm install @material-ui/core --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode()) 
    if(victory):
        setup_result = subprocess.run("npm install victory --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(react_reveal):
        setup_result = subprocess.run("npm install react-reveal --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(react_spring):
            setup_result = subprocess.run("yarn add react-spring --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
            st.error(setup_result.stdout.decode())
    if(express):
        setup_result = subprocess.run("npm install express --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(boron):
        setup_result = subprocess.run("npm install boron --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(animejs):
        setup_result = subprocess.run("npm install animejs --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(cors):
        setup_result = subprocess.run("npm install cors --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(stripe):
        setup_result = subprocess.run("npm install stripe --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(nodemon):
        setup_result = subprocess.run("npm install --save-dev nodemon", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(react_hook_form):
        setup_result = subprocess.run("npm install react-hook-form --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(react_hook_error):
        setup_result = subprocess.run("npm install @hookform/error-message --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(nodemailer):
        setup_result = subprocess.run("npm install nodemailer --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(axios):
        setup_result = subprocess.run("npm install axios --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(recaptcha):
        setup_result = subprocess.run("npm install --save react-google-recaptcha", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(bodyparser):
        setup_result = subprocess.run("npm install body-parser --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
    if(dotenv):
        setup_result = subprocess.run("npm install dotenv --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
        
###### Getting Input and Setup Project  #####
sass = framer  = react_icons = materialUI = victory = drei = react_spring = react_reveal = express = boron = animejs = False
cors = stripe  = nodemon = False
react_hook_form = react_hook_error = nodemailer = axios = recaptcha = bodyparser = dotenv = False
st.write("""
    # Framework Setup🔥
    """
)
framework = st.radio("Choose a Framework",('React JS', 'Next JS', 'Node JS', 'Three JS (React-Three-Fiber)'))

def project_creator(frameName,checkName):
    with st.form(key='setup-form-framework'):
        name = st.text_input(label="Enter the name of your " + checkName + " App (all lowercase) : ")
        sass = st.checkbox("Sass", value=False)
        framer = st.checkbox("Framer Motion", value=False)
        react_icons = st.checkbox("React Icons", value=False)
        materialUI = st.checkbox("Material UI", value=False)
        victory = st.checkbox("Victory", value=False)
        react_reveal = st.checkbox("React Reveal", value=False)
        react_spring = st.checkbox("React Spring", value=False)
        express = st.checkbox("Express", value=False)
        boron = st.checkbox("Boron", value=False)
        animejs = st.checkbox("Anime JS", value=False)
        cors = st.checkbox("Cors", value=False)
        stripe = st.checkbox("Stripe", value=False)
        nodemon = st.checkbox("Nodemon", value=False)
        react_hook_form = st.checkbox("React Hook Form", value=False)
        react_hook_error = st.checkbox("React Hook Form Error", value=False)
        nodemailer = st.checkbox("Nodemailer", value=False)
        axios = st.checkbox("Axios", value=False)
        recaptcha = st.checkbox("Google Recaptcha v2", value=False)
        submit_button = st.form_submit_button(label='Submit')
    if(submit_button):
        if(frameName == "next"):
            setup_result = subprocess.run("npm install --global create-next-app", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        setup_command = "npx create-" + frameName + "-app " + name
        setup_result = subprocess.run(setup_command, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        st.error(setup_result.stdout.decode())
        library_install(name,sass,framer,react_icons,materialUI,victory,react_reveal, react_spring, express, boron, animejs, cors, stripe, nodemon, react_hook_form, react_hook_error, nodemailer, axios, recaptcha,bodyparser, dotenv    )
        
if(framework == "React JS"):
    project_creator("react",framework)
elif(framework == "Next JS"):
    project_creator("next",framework)
elif(framework == "Node JS"):
    with st.form(key='setup-form-node'):
        express = st.checkbox("Express", value=False)
        nodemon = st.checkbox("Nodemon", value=False)
        cors = st.checkbox("Cors", value=False)
        bodyparser = st.checkbox("Bodyparser", value=False)
        dotenv = st.checkbox("Dotenv", value=False)
        axios = st.checkbox("Axios", value=False)
        submit_button = st.form_submit_button(label='Create Node JS project')
    if(submit_button):
        if(express):
            setup_result = subprocess.run("npm install express --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
            st.error(setup_result.stdout.decode())
        if(nodemon):
            setup_result = subprocess.run("npm install --save-dev nodemon", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
            st.error(setup_result.stdout.decode())
        if(cors):
            setup_result = subprocess.run("npm install cors --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
            st.error(setup_result.stdout.decode())
        if(axios):
            setup_result = subprocess.run("npm install axios --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
            st.error(setup_result.stdout.decode())
        if(bodyparser):
            setup_result = subprocess.run("npm install body-parser --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
            st.error(setup_result.stdout.decode())
        if(dotenv):
            setup_result = subprocess.run("npm install dotenv --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
            st.error(setup_result.stdout.decode())
        setup_result = subprocess.run("mkdir node_server", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        setup_result = subprocess.run("npm init -y ", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./node_server")
        st.error(setup_result.stdout.decode())
elif(framework == "Three JS (React-Three-Fiber)"):
    with st.form(key='setup-form-three'):
        name = st.text_input(label="Enter the name of your Three JS App (all lowercase) : ")
        drei = st.checkbox("Drei", value=False)
        sass = st.checkbox("Sass", value=False)
        react_spring = st.checkbox("React Spring", value=False)
        submit_button = st.form_submit_button(label='Submit')
    if(submit_button):
        setup_command = "npx create-react-app " + name
        setup_result = subprocess.run(setup_command, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        st.error(setup_result.stdout.decode())
        setup_result = subprocess.run("npm install three --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
        setup_result = subprocess.run("npm install three @react-three/fiber --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
        st.error(setup_result.stdout.decode())
        if(sass):
            setup_result = subprocess.run("npm install sass --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
            st.error(setup_result.stdout.decode())
        if(drei):
            setup_result = subprocess.run("npm install @react-three/drei --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
            st.error(setup_result.stdout.decode())
        if(react_spring):
            setup_result = subprocess.run("yarn add react-spring --save", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
            st.error(setup_result.stdout.decode())
            