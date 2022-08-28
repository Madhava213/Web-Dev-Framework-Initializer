allLibraries = {
    "Sass": {
        "command": "npm install sass --save",
        "defaultValue": False},
    "Framer Motion": {
        "command": "npm install framer-motion --save",
        "defaultValue": False},
    "React Icons": {
        "command": "npm install react-icons --save",
        "defaultValue": False},
    "Material UI": {
        "command": "npm install @material-ui/core --save",
        "defaultValue": False},
    "Victory": {
        "command": "npm install victory --save",
        "defaultValue": False},
    "React Reveal": {
        "command": "npm install react-reveal --save --force",
        "defaultValue": False},
    "React Spring": {
        "command": "yarn add react-spring --save",
        "defaultValue": False},
    "Express": {
        "command": "npm install express --save",
        "defaultValue": False},
    "Boron": {
        "command": "npm install boron --save",
        "defaultValue": False},
    "Anime JS": {
        "command": "npm install animejs --save",
        "defaultValue": False},
    "Cors": {
        "command": "npm install cors --save",
        "defaultValue": False},
    "Stripe": {
        "command": "npm install stripe --save",
        "defaultValue": False},
    "Nodemon": {
        "command": "npm install --save-dev nodemon",
        "defaultValue": False},
    "React Hook Form": {
        "command": "npm install react-hook-form --save",
        "defaultValue": False},
    "React Hook Form Error": {
        "command": "npm install @hookform/error-message --save",
        "defaultValue": False},
    "Nodemailer": {
        "command": "npm install nodemailer --save",
        "defaultValue": False},
    "Axios": {
        "command": "npm install axios --save",
        "defaultValue": False},
    "Google Recaptcha v2": {
        "command": "npm install --save react-google-recaptcha",
        "defaultValue": False},
    "Bodyparser": {
        "command": "npm install body-parser --save",
        "defaultValue": False},
    "Dotenv": {
        "command": "npm install Dotenv --save",
        "defaultValue": False},
    "React Spinner": {
        "command": "npm install --save react-spinners",
        "defaultValue": False},
    "React Intersection Observer": {
        "command": "npm install react-intersection-observer --save",
        "defaultValue": False},
    "Next On Netlify": {
        "command": "npm install --save next-on-netlify",
        "defaultValue": False},
    "Netlify CLI (install on global environment)": {
        "command": "npm install -g netlify-cli",
        "defaultValue": False},
    "Bootstrap": {
        "command": "npm install react-bootstrap bootstrap@4.6.0 --save",
        "defaultValue": False},
    "React Suite": {
        "command": "npm i rsuite --save",
        "defaultValue": False},
    "React Animated Burger Icon": {
        "command": "npm i -S react-animated-burgers styled-components --save --force",
        "defaultValue": False},
    "React Animated Burger Sidebar": {
        "command": "npm install react-burger-menu --save",
        "defaultValue": False},
    "Fauna DB": {
        "command": "npm install --save faunadb",
        "defaultValue": False},
    "Chakra UI": {
        "command": "npm i @chakra-ui/react @emotion/react@^11 @emotion/styled@^11 framer-motion@ --save",
        "defaultValue": False},
    "Semantic UI": {
        "command": "npm install semantic-ui-react semantic-ui-css --save",
        "defaultValue": False},
    "Evergreen UI": {
        "command": "npm install evergreen-ui --save",
        "defaultValue": False},
    "Grommet UI": {
        "command": "npm install grommet grommet-icons styled-components --save",
        "defaultValue": False},
    "Elemental UI": {
        "command": "npm install elemental --save",
        "defaultValue": False},
    "Rebass": {
        "command": "npm i rebass --save",
        "defaultValue": False},
    "Onsen UI": {
        "command": "npm install onsenui react-onsenui --save",
        "defaultValue": False},
    "Syntax Highlighter": {
        "command": "npm install react-syntax-highlighter --save",
        "defaultValue": False},
    "Copy to Clipboard": {
        "command": "npm install react-copy-to-clipboard --save",
        "defaultValue": False},
    "Drei": {
        "command": "npm install @react-three/drei --save",
        "defaultValue": False},
    "Redux JS": {
        "command": "npm install @reduxjs/toolkit --save",
        "defaultValue": False},
    "Redux JS Core": {
        "command": "npm install redux --save",
        "defaultValue": False},
    "Next Redux Wrapper": {
        "command": "npm install next-redux-wrapper --save",
        "defaultValue": False},
    "Date FNS": {
        "command": "npm install date-fns --save",
        "defaultValue": False},
    "Fast Sort": {
        "command": "npm install fast-sort --save",
        "defaultValue": False},
    "Sorted Array Operations": {
        "command": "npm install sorted-array-operations --save",
        "defaultValue": False},
    "Trie Search": {
        "command": "npm install trie-search --save",
        "defaultValue": False},
    "Moment": {
        "command": "npm install moment --save",
        "defaultValue": False},
    "React Quill JS": {
        "command": "npm install react-quilljs --save",
        "defaultValue": False},
    "Redis OM": {
        "command": "npm install redis-om --save",
        "defaultValue": False},
    "React Dropzone": {
        "command": "npm install react-dropzone --save",
        "defaultValue": False},
    "React Player": {
        "command": "npm install react-player --save",
        "defaultValue": False},
    "React Webcam": {
        "command": "npm install react-webcam --save",
        "defaultValue": False},
    "MUI X Date Pickers": {
        "command": "npm install @mui/x-date-pickers --save",
        "defaultValue": False},
    "FS": {
        "command": "npm install fs --save",
        "defaultValue": False},
    "React File Preview Latest": {
        "command": "npm install react-file-preview-latest --save",
        "defaultValue": False},
    "Next Bundle Analyzer(Dev)": {
        "command": "npm install @next/bundle-analyzer --save-dev",
        "defaultValue": False},
}

nodeJSLibraries = {
    "Express": allLibraries["Express"],
    "Nodemon": allLibraries["Nodemon"],
    "Cors": allLibraries["Cors"],
    "Bodyparser": allLibraries["Bodyparser"],
    "Dotenv": allLibraries["Dotenv"],
    "Axios": allLibraries["Axios"],
}

reactJSLibraries = nextJSLibraries = cleanNextJSLibraries = {
    "Sass": allLibraries["Sass"],
    "Framer Motion": allLibraries["Framer Motion"],
    "React Icons": allLibraries["React Icons"],
    "Material UI": allLibraries["Material UI"],
    "Victory": allLibraries["Victory"],
    "React Reveal": allLibraries["React Reveal"],
    "React Spring": allLibraries["React Spring"],
    "React Spinner": allLibraries["React Spinner"],
    "Boron": allLibraries["Boron"],
    "Anime JS": allLibraries["Anime JS"],
    "Stripe": allLibraries["Stripe"],
    "Express": allLibraries["Express"],
    "Nodemon": allLibraries["Nodemon"],
    "Cors": allLibraries["Cors"],
    "Bodyparser": allLibraries["Bodyparser"],
    "Dotenv": allLibraries["Dotenv"],
    "Axios": allLibraries["Axios"],
    "React Hook Form": allLibraries["React Hook Form"],
    "React Hook Form Error": allLibraries["React Hook Form Error"],
    "Nodemailer": allLibraries["Nodemailer"],
    "Google Recaptcha v2": allLibraries["Google Recaptcha v2"],
    "React Intersection Observer": allLibraries["React Intersection Observer"],
    "Next On Netlify": allLibraries["Next On Netlify"],
    "Netlify CLI (install on global environment)": allLibraries["Netlify CLI (install on global environment)"],
    "Bootstrap": allLibraries["Bootstrap"],
    "React Suite": allLibraries["React Suite"],
    "React Animated Burger Icon": allLibraries["React Animated Burger Icon"],
    "React Animated Burger Sidebar": allLibraries["React Animated Burger Sidebar"],
    "Fauna DB": allLibraries["Fauna DB"],
    "Chakra UI": allLibraries["Chakra UI"],
    "Semantic UI": allLibraries["Semantic UI"],
    "Evergreen UI": allLibraries["Evergreen UI"],
    "Grommet UI": allLibraries["Grommet UI"],
    "Elemental UI": allLibraries["Elemental UI"],
    "Rebass": allLibraries["Rebass"],
    "Onsen UI": allLibraries["Onsen UI"],
    "Syntax Highlighter": allLibraries["Syntax Highlighter"],
    "Copy to Clipboard": allLibraries["Copy to Clipboard"],
    "Redux JS": allLibraries["Redux JS"],
    "Redux JS Core": allLibraries["Redux JS Core"],
    "Next Redux Wrapper": allLibraries["Next Redux Wrapper"],
    "Date FNS": allLibraries["Date FNS"],
    "Fast Sort": allLibraries["Fast Sort"],
    "Sorted Array Operations": allLibraries["Sorted Array Operations"],
    "Trie Search": allLibraries["Trie Search"],
    "Moment": allLibraries["Moment"],
    "React Quill JS": allLibraries["React Quill JS"],
    "Redis OM": allLibraries["Redis OM"],
    "React Dropzone": allLibraries["React Dropzone"],
    "React Player": allLibraries["React Player"],
    "React Webcam": allLibraries["React Webcam"],
    "MUI X Date Pickers": allLibraries["MUI X Date Pickers"],
    "FS": allLibraries["FS"],
    "React File Preview Latest": allLibraries["React File Preview Latest"],
    "Next Bundle Analyzer(Dev)": allLibraries["Next Bundle Analyzer(Dev)"],
}


threeJSLibraries = {
    "Drei": allLibraries["Drei"],
    "Sass": allLibraries["Sass"],
    "React Spring": allLibraries["React Spring"],
}
