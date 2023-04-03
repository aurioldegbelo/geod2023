# code adapted from 
import openai
import my_api_keys


completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                          messages=[{"role": "user", 
                                            "content": "Tell me something about Dresden"}])
print(completion.choices[0].message.content)



#print ("The API key is", my_api_keys.example_key)