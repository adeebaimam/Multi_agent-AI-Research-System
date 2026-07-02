from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from tools import web_search, scrape_url
import os
from dotenv import load_dotenv

load_dotenv()

#model setup
llm = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0
)

#1st agent
def build_search_agent():
    return create_agent(
        model = llm,
        tools = [web_search],
        system_prompt="""
        You are a search agent.

Always use the web_search tool.

Your final response MUST be the exact output returned by the tool.

Do not summarize.
Do not analyze.
Do not rewrite.
Do not omit any URLs.
Return all Titles, URLs, and Snippets exactly as received.
"""
    )


#2nd agent
def build_scrape_agent():
    return create_agent(
        model = llm,
        tools = [scrape_url]
    )

#writer chain(will use runnables)
writer_prompt = ChatPromptTemplate.from_messages([
    'system', "You are expert research writer. You will be given a topic and you will write a clear, detailed and insightful reports.",
    'human', """Write a detailed research report on the topic below.
    
    Topic: {topic}
    
    Research Gathered: {research}
    
    Structure the report as
    -Introduction
    -Key Findings (minimum 3 well-explained points)
    -Conclusion
    -Sources (if any, list all URLS found in research)
    
    Be detailed, factual and professional."""
])

writer_chain = writer_prompt | llm | StrOutputParser()

#critic_chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

    Report:
    {report}

    Respond in this exact format:

    Score: X/10

    Strengths:
    - ...
    - ...

    Areas to Improve:
    - ...
    - ...

    One line verdict:
    ..."""),
    ])

critic_chain = critic_prompt | llm | StrOutputParser()
