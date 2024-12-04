Functions:

ML.GENERATE_TEXT: It is leveraging vertex AI node hour (cost, token limit, Queries per minute (QPM) limit) if you use remote models from Vertex AI.
ML.TRANSLATE: Related to Cloud Translation API. you can perform the following tasks:

TRANSLATE_TEXT
DETECT_LANGUAGE

ML.UNDERSTAND_TEXT: Related to Cloud Natural Language API. you can perform the following tasks:

ANALYZE_ENTITIES
ANALYZE_ENTITY_SENTIMENT
ANALYZE_SENTIMENT
ANALYZE_SYNTAX
CLASSIFY_TEXT



For example, to perform a question answering task, you could provide a prompt similar to CONCAT("What are the key concepts in the following article?: ", article_text). You can also provide context as part of the prompt. For example, CONCAT("context: Only output 'yes' or 'no' to the following question: ", question). If your data requires additional context, using ML.GENERATE_TEXT with a Vertex AI model is a better choice, as those models allow you to provide context as part of the prompt you submit. Keep in mind that providing additional context as input increases **token count** and **cost**. 

# Bigquery ML vs Vertex AI

ML.TRANSLATE output includes information about the input language, and ML.UNDERSTAND_TEXT output includes information about the magnitude of the sentiment for sentiment analysis tasks. Generating this metadata is possible with the Vertex AI models, but this requires significant prompt engineering, and isn't likely to provide the same granularity.
