# GPTg
## General Purpose Transgender 

An LLM-powered chatbot aiming to provide useful and accurate information to transgender individuals about gender, transitioning, psychological coping, geographical political realities, and gender affirming care.  

## Current Architecture

Uses Langchain and FAISS to set up the knowledge database and a question answering chatbot.  Information sources are automatically scraped from the internet and a collection of documents and loaded into the vector database for retrieval. The chatbot is made available via FastAPI within a docker container.

# Project Roadmap

## Components
* Langchain Chatbot
* FastAPI for communicating with bot
* SQL chats database
* Web app 
* Vector database for knowledge base
* Curated collection of quality information sources
* Web-scraper
* ETL pipeline to load scraped text into vector database
* User feedback system
* Containerization, cloud deployment, and monitoring

## Chatbot Features
* Prompt engineering to optimize to provide useful information to trans users
* Chat history memory with windowing and summarization
* Vector-database integration so that the bot can recall and use relevant expert knowledge from external sources
* * Medical literature
* * Information about gender
* * Wikipedia
* * Curated political news sources
* * Travel advisories
* * Scientific papers
* * Crisis support materials
* Citing the sources for the information used from the vector database
