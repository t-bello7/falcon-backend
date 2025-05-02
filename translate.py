import pandas as pd
import requests

import groq
import pandas
import time

GROQ_API_KEY='from env variable'

sys_prompt = '''
You are a professional African language translator.
Translate user input to the requested target language accurately.
Only return the translated text without extra explanation.
'''

groq_client = groq.Groq(api_key=GROQ_API_KEY)

def translate_text(text, source_lang='Hausa', target_lang='English'):
    time.sleep(2)  # To avoid rate limits
    user_prompt = f"Translate this from {source_lang} to {target_lang}:\n{text}"

    response = groq_client.chat.completions.create(
        model='llama3-70b-8192',
        messages=[
            {'role': 'system', 'content': sys_prompt},
            {'role': 'user', 'content': user_prompt}
        ],
        temperature=0.1,
        top_p=0.9,
        seed=79
    )

    output = response.choices[0].message.content.strip()
    return output

print(translate_text("Mo fe ra oja.", source_lang="Hausa", target_lang="English"))
# Output: I want to send goods to Niger.
