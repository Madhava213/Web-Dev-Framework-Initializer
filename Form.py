import streamlit as st
import subprocess


def frameworkSpecific(selection, Data, inputName):
    if(selection == "Node JS"):
        directory_result = subprocess.run("mkdir " + inputName, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        st.error(directory_result.stdout.decode())
        setup_result = subprocess.run(Data["command"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, cwd="./" + inputName)
        st.error(setup_result.stdout.decode())
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
