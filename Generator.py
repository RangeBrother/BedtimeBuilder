import secrets
import openai

openai.api_key = secrets.API_KEY
s_model = 'text-davinci-003'
def getStory(s_name, s_age, s_gender, s_theme):
    story = openai.Completion.create(
        max_tokens= 400,
        model=s_model,
        prompt= 'Write a short {theme} themed bedtime story for a {age} year old {gender} named {name}'.format(
            theme=s_theme, age =s_age, gender=s_gender, name=s_name)
    )
    return str(story['choices'][0]['text'])


