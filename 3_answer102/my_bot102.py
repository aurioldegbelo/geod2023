# Code adapted from https://github.com/AIAdvantage/chatgpt-api-youtube
# To see how to create a virtual environment, check https://python.land/virtual-environments/virtualenv 
# python -m venv my-envi, and the next steps, see https://stackoverflow.com/a/74825209
# For error of installation due to privileges, see https://stackoverflow.com/questions/66322049/could-not-install-packages-due-to-an-oserror-winerror-2-no-such-file-or-direc
# For gitignore, see https://github.com/github/gitignore/blob/main/Python.gitignore
# If VS Code shows issues about execution policies, you may need to change the execution policies settings in the powershell, see https://www.sharepointdiary.com/2014/03/fix-for-powershell-script-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system.html


# The code for this bot is taken from https://www.haihai.ai/chatgpt-api/
# Credits also to https://www.youtube.com/watch?v=pGOyw_M1mNE for the nice intro video to chatbot building
import my_api_keys
import openai # open ai documentation at https://platform.openai.com/docs/introduction/overview

openai.api_key = my_api_keys.my_open_ai_key

messages = []
system_msg = input("What type of chatbot would you like to create? ")
messages.append({"role": "system", "content": system_msg})

print("Say hello to your new assistant!")
while input != "quit()": 
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")