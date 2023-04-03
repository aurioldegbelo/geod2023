# Code adapted from https://github.com/AIAdvantage/chatgpt-api-youtube
# To see how to create a virtual environment, check https://python.land/virtual-environments/virtualenv 
# python -m venv my-envi, and the next steps, see https://stackoverflow.com/a/74825209
# For error of installation due to privileges, see https://stackoverflow.com/questions/66322049/could-not-install-packages-due-to-an-oserror-winerror-2-no-such-file-or-direc
# For gitignore, see https://github.com/github/gitignore/blob/main/Python.gitignore
# If VS Code shows issues about execution policies, you may need to change the execution policies settings in the powershell, see https://www.sharepointdiary.com/2014/03/fix-for-powershell-script-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system.html

import api_keys
import openai

openai.api_key = api_keys.my_open_ai_key

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                          messages=[{"role": "user", 
                                            "content": "Tell me something about Dresden"}])
print(completion.choices[0].message.content)

