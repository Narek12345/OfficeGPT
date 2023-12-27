import requests

URL = 'https://officegpt-api.onrender.com'


def upload_file_for_training(file, chatgpt_token):
	url = URL + '/upload_file_for_training'
	params = {'OPENAI_API_KEY': chatgpt_token}
	file = {'file': file}
	requests.post(url=url, params=params, files=file)


def make_request_in_chatgpt(text):
	url = URL + '/make_request_in_chatgpt/?text=' + text
	resp = requests.post(url=url)

	data = resp.json()
	return data['response']
