import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
# Importing
import Libraries

frameworks = {
    'Node JS': {
        "command": "npm init -y ",
        "libraries": Libraries.nodeJSLibraries
    },
    'React JS': {
        "command": "npx create-react-app ",
        "libraries": Libraries.reactJSLibraries
    },
    'Next JS': {
        "command": "npm install --global create-next-app ",
        "libraries": Libraries.nextJSLibraries
    },
    'Clean Boilerplate Next JS': {
        "command": "npm install --global create-next-app ",
        "libraries": Libraries.cleanNextJSLibraries
    },
    'Three JS (React-Three-Fiber)': {
        "command": "npx create-react-app ",
        "libraries": Libraries.threeJSLibraries
    }
}
