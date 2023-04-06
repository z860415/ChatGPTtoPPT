import openai
import os
from dotenv import load_dotenv

load_dotenv()

def generate_notes(title:str):
    request_string = f'''
    請幫我把「{title}」主題課程，以好的方面闡述，整理成4000字三級結構簡報，以 Markdown 標記語法原始程式碼方便複製使用
    '''
    openai.api_key = os.getenv('GPT_TOKEN')

    messages = []
    msg = request_string
    messages.append({"role":"user","content":msg})   # 添加 user 回應
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=2000,
        temperature=0.5,
        messages=messages
    )
    # ai_msg = response.choices[0].message.content.replace('\n','')
    ai_msg = response.choices[0].message.content
    messages.append({"role":"assistant","content":ai_msg})   # 添加 ChatGPT 回應
    # print(f'ai > {ai_msg}')
    with open('./output.txt', 'w', encoding='utf-8') as file:
        file.write(ai_msg)
