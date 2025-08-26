from langchain_openai import ChatOpenAI # 외부 자원 사용 - 사용량에 의한 결제
from langchain_community.llms import Ollama # 내 자원 사용 - local 자원에 모델 올려서 사용
from langchain.chains import LLMChain # chain 생성 
from langchain.prompts import PromptTemplate # prompt template
from langchain_core.prompts.few_shot import FewShotPromptTemplate # fewshot template persona, chat e.g, prompt
from langchain.cache import InMemoryCache # 캐시 - 응답을 저장해서 같은 질문이 들어올 때 사용량 X
from langchain.globals import set_llm_cache # 캐시 - 응답을 저장해서 같은 질문이 들어올 때 사용량 X
from langchain.callbacks import get_openai_callback # 토큰 수 및 추징요금 추적


llm = ChatOpenAI(
    temperature = 0,
    openai_api_key="your own api keys"
)

set_llm_cache(InMemoryCache())

examples = [{"question" : "당신은 어떤 AI인가요", "answer":"저는 언어 기반의 AI입니다."},
           {"question" : "당신은 무얼 할 수 있나요", "answer":"agent 형태로 구현된다면 tool을 사용할 수 있습니다"},
           {"question" : "당신을 설명하세요", "answer":"저는 다량의 언어 데이터로 학습된 인공지능 모델입니다"}]

example_prompt = PromptTemplate.from_template(
    "Question:\n{question}\nAnswer:\n{answer}"
)

persona = """
당신은 한국인 ML,DL 교수 AI입니다.
모든 질문에 대해 단계적으로 사고하며 정확한 연산과, 과정 그로 일어날 효과들에대해 
논리적으로 판단하고, 마지막에 결론을 명확하게 말합니다.
"""

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix = persona,
    suffix="Question:\n{question}\nContext:\n{context}\nAnswer:",
    input_variables=["question","context"],
)

db = Chroma(
    persist_directory="./my_paper_vectordb",
    embedding_function=embedding
)
# llm = Ollama(model="llama3")
# chain = LLMChain(llm = llm, prompt = prompt)

chain = prompt | llm | StrOutputParser()
