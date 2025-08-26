with get_openai_callback() as cb:
    question = {"question":"DetCo_Unsupervised Contrastive Learning for Object Detection 논문에 대해 설명해줄래?"}
    docs = db.similarity_search(question['question'])
    context = "\n".join([doc.page_content for doc in docs])
    
    answer = chain.stream({
    "question": question["question"],
    "context": context
})
    stream_response(answer)
    
    print(f"\n총 사용된 토큰수: \t\t{cb.total_tokens}")
    print(f"프롬프트에 사용된 토큰수: \t{cb.prompt_tokens}")
    print(f"답변에 사용된 토큰수: \t{cb.completion_tokens}")
    print(f"호출에 청구된 금액(USD): \t${cb.total_cost}")