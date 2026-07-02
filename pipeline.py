from agents import build_search_agent, build_scrape_agent, writer_chain, critic_chain

def run_research_agent(topic:str) -> dict:

    state = {}

    #step-1: search agent working
    print("\n"+"="*50)
    print("step 1 - search agent is working ...")
    print("="*50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages" : [("user", f"Search for recent and reliable information on the topic: {topic}")],
    })

    state['searched_results'] = search_result['messages'][-1].content

    print("\n search result", state['searched_results'])

    #step-2: Scrape agent working
    print("\n"+"="*50)
    print("step 2 - scrape agent is working ...")
    print("="*50)

    scrape_agent = build_scrape_agent()
    scrape_result = scrape_agent.invoke({
        "messages": [("user",
        f"Based on the search result about '{topic}',"
        f"pick the most relevant url and scrape it for deeper content.\n\n"
        f"Search Result: \n{state['searched_results'][:800]}"
        )]
    })

    state['scraped_content'] = scrape_result['messages'][-1].content

    print("\n scraped content", state['scraped_content'],"\n")

    #step-3 Writer chain working

    print("\n"+"="*50)
    print("step 3 - writer chain is working ...")
    print("="*50)
    

    research_combined = (
       f"SEARCH RESULTS: \n {state['searched_results']} \n\n"
       f"SCRAPED CONTENT: \n {state['scraped_content']}"
    )

    state['Report']=writer_chain.invoke({
        'topic': topic,
        "research": research_combined
    })

    print("\n Final report", state['Report'],"\n")

    #step-4 Critic chain working

    print("\n"+"="*50)
    print("step 4 - critic chain is working ...")
    print("="*50)

    state['Feedback']=critic_chain.invoke({
        'report': state['Report']
    })

    print("\n critic report", state['Feedback'],"\n")

    return state

if __name__ == "__main__":
    topic = input("Enter a research topic : ")
    run_research_agent(topic)