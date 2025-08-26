# serve-my-own-LLM
study langchain and make my own local agent through exe and gradio

how to compose llms
 - study about prompts and how to load the llms from Ollama and OpenAI
 - Difference about persona, chat examples, prompt template
   - persona : llms persona = prefix
   - chat examples : examples
   - prompt template : example that how to model recognize the Q&A

how to made vectorDB
 - study about how to compose rag
 - this code based on pdf file and its loader
 - load file and split it by semantic chunk
 - save it as db

conversation
 - use stream and ask question to model

plans
 1.change every models that comes from Ollama(local based)
 2. use gradio to visualize this
 3. made db that contains multiple files or DB
 4. upgrade it to agent
 5. made tools that save the conversation in memory
