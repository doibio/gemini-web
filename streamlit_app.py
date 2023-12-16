import streamlit as st
import requests
import json

get_url = 'http://localhost:5000/users/12345/conversations/67890/messages'

response = requests.get(get_url)

if response.status_code == 200:
    data = json.loads(response.text)
    for message in data:
        st.markdown(message.get("text", "No text available"))
else:
    st.write(f'Failed to retrieve data: Status code {response.status_code}')

with st.form(key='message_form'):
    user_message = st.text_input('Enter your message')
    submit_button = st.form_submit_button('Send Message')

    if submit_button and user_message:
        post_url = 'http://localhost:5000/users/12345/conversations/67890/messages'
        
        post_data = {"text": user_message}

        post_response = requests.post(post_url, json=post_data)
