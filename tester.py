import subprocess
globals_scss = '@import url("https://fonts.googleapis.com/css2?family=Righteous&display=swap");\n@import url("https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,300;0,400;1,300;1,400&display=swap");\n@import url("https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@0,400;0,500;1,500;1,700&family=Eczar:wght@400;500;600&display=swap");\n@import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500&display=swap");\n@import url("https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&display=swap");\nhtml,\nbody {\n    padding: 0;\n    margin: 0;\n    font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen,\n        Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif;\n}\n\na {\n    color: inherit;\n    text-decoration: none;\n}\n\n* {\n    box-sizing: border-box;\n}\n'



fileData = 'import Layout from "../components/Layout";\nimport "../styles/globals.scss";\nimport Footer from "../components/Footer";\nimport { motion } from "framer-motion";\nfunction MyApp({ Component, pageProps, router }) {\n    return (\n        <motion.div\n            key={router.route}\n            initial={{ opacity: 0.7 }}\n            animate={{ opacity: 1 }}\n        >\n<Layout />\n            <Component {...pageProps} />\n            <Footer />\n        </motion.div>\n    );\n}\n\nexport default MyApp;\n'

data = fileData.split('\n')
i = data[0]
def charAdder(words):
    result = ''
    for i in words:
        if(i == ">" or i == "<"):
            result += "^" + i
        else:
            result += i
    return result
commander = "echo " + charAdder(i) + " > hello.txt"
subprocess.run(commander, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
for i in range(1,len(data)):
    if(data[i]!= ''):
        print(" Hey : " + data[i] )
        commander = "echo " + charAdder(data[i]) + " >> hello.txt"
        les = subprocess.run(commander, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        print(les.stdout)
    else:
        print("NOBODY")
        les = subprocess.run("echo. >> hello.txt", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)

