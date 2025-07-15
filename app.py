# モジュールのインポート
from dotenv import load_dotenv
from openai import OpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import streamlit as st
import os

# 環境変数のロード
load_dotenv()

# OpenAIのAPIキーを取得
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Streamlitの設定
st.title("家事のアドバイザー")
st.write("家事に関するアドバイスをするAIアプリケーションです。")
st.write("###### ジャンル（掃除または料理）を選択して、質問を入力してください。")

selected_item = st.radio("ジャンルを選択してください。", ["掃除", "料理"])

input_message = st.text_input(label=f"{selected_item}に関する質問を入力してください。")

text_count = len(input_message)

st.divider()

if st.button("実行"):
    if input_message:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"あなたは{selected_item}の専門家です。質問に対して初心者にも分かりやすく簡潔に答えてください。ジャンルが違う場合、判りませんと答えてください。",
                },
                {"role": "user", "content": f"{input_message}"},
            ],
            temperature=0.5,
        )
        st.write("###### 回答：", completion.choices[0].message.content)
    else:
        st.error("質問を入力してから「実行」ボタンを押してください。")
