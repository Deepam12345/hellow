from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY_HERE")

def summarize_report(text):

    prompt = f"""

You are an experienced medical AI.

Summarize the report in simple language.

Report:

{text}

"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    return response.choices[0].message.content