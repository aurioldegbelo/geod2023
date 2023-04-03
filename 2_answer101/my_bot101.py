# Code adapted from https://github.com/AIAdvantage/chatgpt-api-youtube
# To see how to create a virtual environment, check https://python.land/virtual-environments/virtualenv 
# python -m venv my-envi, and the next steps, see https://stackoverflow.com/a/74825209
# For error of installation due to privileges, see https://stackoverflow.com/questions/66322049/could-not-install-packages-due-to-an-oserror-winerror-2-no-such-file-or-direc
# For ginignore 
import my_api_keys
import openai

openai.api_key = my_api_keys.my_open_ai_key

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                          messages=[{"role": "user", 
                                            "content": "Tell me something about Dresden"}])
print(completion.choices[0].message.content)

