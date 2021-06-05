import streamlit as st
import subprocess

###### Installing Standard Libraries  #####
def library_install(name,sass,framer,react_icons,materialUI,victory):
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
        
###### Getting Input and Setup Project  #####
sass = False
framer = False
react_icons = False
materialUI = False
victory = False
drei = False
react_spring = False
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
        submit_button = st.form_submit_button(label='Submit')
    if(submit_button):
        setup_command = "npx create-" + frameName + "-app " + name
        setup_result = subprocess.run(setup_command, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        st.error(setup_result.stdout.decode())
        library_install(name,sass,framer,react_icons,materialUI,victory)
        
if(framework == "React JS"):
    project_creator("react",framework)
elif(framework == "Next JS"):
    project_creator("next",framework)
elif(framework == "Node JS"):
    with st.form(key='setup-form-node'):
        submit_button = st.form_submit_button(label='Create Node JS project')
    if(submit_button):
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
            