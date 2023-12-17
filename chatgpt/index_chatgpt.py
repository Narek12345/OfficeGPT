from llama_index import (
	Document,
	LLMPredictor,
	PromptHelper,
	StorageContext,
	GPTVectorStoreIndex,
	load_index_from_storage,
)

from langchain.llms import OpenAI

import os


def index_chatgpt_file(file, user):
	# Получаем chatgpt токен.
	chatgpt_token = user.profile.chatgpt_token

	try:
		contents = file.file.read()
		with open(file.filename, 'wb') as f:
			f.write(contents)
	except Exception:
		return {"message": "There was an error uploading the file"}
	finally:
		file.file.close()
		os.remove(file.filename)

	text = contents.decode()

	llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name='text-davinci-003', max_tokens=300))
	prompt_helper = PromptHelper(4096, 300, 0.2, chunk_size_limit=600)

	documents = [Document(text=text)]

	index = GPTVectorStoreIndex.from_documents(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

	index.storage_context.persist()

	return "200 OK"