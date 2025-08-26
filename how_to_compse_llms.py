from langchain_openai import ChatOpenAI # 외부 자원 사용 - 사용량에 의한 결제
from langchain_community.llms import Ollama # 내 자원 사용 - local 자원에 모델 올려서 사용
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache

llm = ChatOpenAI(
    temperature = 0,
    openai_api_key="You can get your own api keys"
)

set_llm_cache(InMemoryCache())

examples = [{"question" : "당신은 어떤 AI인가요", "answer":"저는 언어 기반의 AI입니다."},
           {"question" : "당신은 무얼 할 수 있나요", "answer":"agent 형태로 구현된다면 tool을 사용할 수 있습니다"},
           {"question" : "당신을 설명하세요", "answer":"저는 다량의 언어 데이터로 학습된 인공지능 모델입니다"}]

example_prompt = PromptTemplate.from_template(
    "Question:\n{question}\nAnswer:\n{answer}"
)

persona = """
당신은 '추론의 달인'이라는 별명을 가진 AI입니다. 
모든 질문에 대해 중간 질문을 나누어 단계적으로 사고하며, 
논리적으로 판단하고, 마지막에 결론을 명확하게 말합니다.
다음은 그런 방식으로 답한 예시들입니다.
"""

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix = persona,
    suffix="Question:\n{question}\nAnswer:",
    input_variables=["question"],
)

# llm = Ollama(model="llama3")
# chain = LLMChain(llm = llm, prompt = prompt)

chain = prompt | llm | StrOutputParser()
question = {"question":"당신도 인간처럼 생각할 수 있나요"}

answer = chain.stream(question)
stream_response(answer)