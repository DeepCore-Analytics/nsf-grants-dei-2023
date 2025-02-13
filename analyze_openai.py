import sys
import os
import time

import requests
import traceback
from tenacity import retry, stop_after_attempt, wait_fixed


import pandas as pd

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def call_openai(prompt, temperature=0.0):

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    payload = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": prompt}],
        #"response_format": {"type": "json_object"},
        "temperature": temperature,
        "max_tokens": 4096,
    }

    res = requests.post(url, headers=headers, json=payload).json()
    kind = res["choices"][0]["message"]["content"]

    return kind

def main():

    df = pd.read_csv("output.csv")

    if os.path.exists("output_done.csv"):
        df_done = pd.read_csv("output_done.csv")

        done_ids = df_done["award_id"].tolist()
        outlist = df_done.to_dict(orient="records")
    else:
        done_ids = []
        outlist = []

    nn = len(df)
    for i, row in df.iterrows():

        print(f"{i+1}/{nn}")

        title = row["award_title"]
        abstract = row["abstract"]
        award_id = row["award_id"]

        if award_id in done_ids:
            continue

        prompt = f"""
        You are a social scientist specializing in the study of woke culture and
        diversity, equity, and inclusiion (DEI) initiatives.

        Below is the title and abstract of an NSF grant. Determine if the grant is
        focused primarily on DEI related topics or focused primarily on a scientific topic.
        Respond with "DEI" or "scientific".

        Title: {title}

        Abstract: {abstract}
        """

        try:
            kind = call_openai(prompt)
            time.sleep(1)

        except:
            traceback.print_exc()
            print(row)
            sys.exit()

        xd = dict(row)
        xd["kind"] = kind
        outlist.append(xd)

        if i % 10 == 0:
            print(f"Processed {i} rows")
            df_out = pd.DataFrame(outlist)
            df_out.to_csv("output_done.csv", index=False)


if __name__ == "__main__":

    main()