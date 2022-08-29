import streamlit as st
import subprocess


def frameworkSpecific(selection, Data, inputName):
    if(selection == "Node JS"):
        directory_result = subprocess.run("mkdir " + inputName, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        st.error(directory_result.stdout.decode())
        setup_result = subprocess.run(Data["command"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + inputName)
        st.error(setup_result.stdout.decode())
        return False
    elif(selection == "Clean Boilerplate Next JS"):
        st.write(Data["command"] + inputName)
        setup_result = subprocess.run(Data["command"] + inputName, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        st.error(setup_result.stdout.decode())
        st.write("./" + inputName)
        subprocess.run("mkdir components", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + inputName)
        subprocess.run("del favicon.ico", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + inputName + "/public")
        subprocess.run("del vercel.svg", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + inputName + "/public")
        subprocess.run("del globals.css", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + inputName + "/styles")
        subprocess.run("del Home.module.css", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + inputName + "/styles")
        return False
    return True

def createForm(Name, Data):
    with st.form(key='setup-form-framework'):
        # Input
        name = st.text_input(label=("Enter the name of your " +
                                    Name + " App (all lowercase) : "))

        # Checkboxes
        for item,val in Data["libraries"].items():
            val["checkbox"] = st.checkbox(item, value=val["defaultValue"])

        # Submit Button
        submit_button = st.form_submit_button(label='Submit')

        # After Submit
        if(submit_button):
            st.info('Running 🚀')
            if(Name == "Next JS" or Name == "Clean Boilerplate Next JS"):
                setup_result = subprocess.run("npm install --global create-next-app", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
                st.info(setup_result.stdout.decode())
            if(frameworkSpecific(Name, Data, name)):
                setup_result = subprocess.run(Data["command"] + name, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
                st.error(setup_result.stdout.decode())
            for item,val in Data["libraries"].items():
                if(val["checkbox"]):
                    lib_result = subprocess.run(
                        val["command"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + name)
                    st.success(item + " ⇓")
                    st.error(lib_result.stdout.decode())
            st.success("THE PROGRAM HAS RAN SUCCESSFULLY! 🎉")
