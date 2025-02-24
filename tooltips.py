tooltips = {
    "api_key": "Enter your API Key here. If using the official OpenAI API, obtain it from https://platform.openai.com/account/api-keys.",
    "base_url": "The API endpoint of the model. For the official OpenAI API: https://api.openai.com/v1. For Ollama local deployment, it might be similar to http://localhost:11434/v1. No need to fill this for Gemini model.",
    "interface_format": "Specify the LLM interface compatibility format, such as DeepSeek, OpenAI, Ollama, ML Studio, Gemini, etc.\n\nNote:"+
                       "OpenAI compatibility refers to any interface that can be requested via this standard, not limited to api.openai.com\n"+
                       "For example, the Ollama interface format is also compatible with OpenAI, so it can be used without modification\n"+
                       "The ML Studio interface format is also consistent with the OpenAI interface format.",
    "model_name": "The name of the model to be used, such as deepseek-reasoner, gpt-4o, etc. If using Ollama or similar, enter the name of the local model you have downloaded.",
    "temperature": "The randomness of the generated text. Higher values are more divergent, while lower values are more precise.",
    "max_tokens": "The maximum number of tokens to generate in a single request. Range: 1~100000. Enter an appropriate value based on the model context and requirements.\n"+
                 "Here are the maximum values for some common models:\n"+
                 "o1: 100,000\n"+
                 "o1-mini: 65,536\n"+
                 "gpt-4o: 16384\n"+
                 "gpt-4o-mini: 16384\n"+
                 "deepseek-reasoner: 8192\n"+
                 "deepseek-chat: 4096\n",
    "embedding_api_key": "The API Key required to call the Embedding model.",
    "embedding_interface_format": "The interface format of the Embedding model, such as OpenAI or Ollama.",
    "embedding_url": "The API endpoint of the Embedding model.",
    "embedding_model_name": "The name of the Embedding model, such as text-embedding-ada-002.",
    "embedding_retrieval_k": "The number of top-K results to return when performing vector retrieval.",
    "topic": "A brief description of the overall theme or main story background of the novel.",
    "genre": "The genre of the novel, such as fantasy, urban, science fiction, etc.",
    "num_chapters": "The total number of chapters expected in the novel.",
    "word_number": "The target word count for each chapter.",
    "filepath": "The root directory path where generated files will be stored. All txt files, vector libraries, etc., should be placed in this directory.",
    "chapter_num": "The current chapter number being processed, used for draft or finalization operations.",
    "user_guidance": "Additional instructions or writing guidance provided for this chapter.",
    "characters_involved": "A list of characters who need to be prominently featured or have an impact on the plot in this chapter.",
    "key_items": "Important props, clues, or items that appear in this chapter.",
    "scene_location": "The main location or scene description for this chapter.",
    "time_constraint": "The time pressure or deadline setting involved in the plot of this chapter."
}
