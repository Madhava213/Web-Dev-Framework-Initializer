from tkinter import Frame
import streamlit as st
import subprocess
import Form
from Data import Frameworks

st.write("""# Framework Setup🔥""")

# List Frameworks
frameworkList = Frameworks.frameworks.keys()
framework = st.radio("Choose a Framework", tuple(frameworkList))

# Create Libraries Form
Form.createForm(framework, Frameworks.frameworks[framework])
