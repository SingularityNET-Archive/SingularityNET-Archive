---
DOC: 1
Title: QADAO Open Source AI Workflow
Status: Active
Category: Standards
Authors:
    - Stephen
    - Andre
    - Vani
Discussions:
    - https://github.com/SingularityNET-Archive/SingularityNET-Archive/pulls
Created: 
License: CC-BY-4.0
---

# QADAO Open Source AI Workflow (RAG)

This is a draft of a possible approach to an AI workflow for QADAO (e.g. Research, Development, Testing and Implementation etc).

Most of this draft is sourced from the Langchain website - https://www.langchain.com/
Using this as a starting point to draft our own approach.

## Why RAG ?

A RAG workflow refines generalist AI models with local domain knowledge. This allows for clear ownership of data, more timely updates and local community safeguarding.

# Methods
## Retrieval

### Contextualize your LLM App

Retrieval Augmented Generation (RAG) with LangChain connects your company data to the power of LLMs.

https://python.langchain.com/docs/modules/data_connection/

How retrieval augments generative models is the key here. 

(see https://youtu.be/T-D1OfcDW1M)

The aim is to constrain data structures into contexts or prompts that generate relevant responses.

Examples of augmentation include :

- specfiying to provide sources for what is retrieved. This provides a means to sanity check the response at the Evaluation stage (eg unit tests). 

- timeliness of the response (time / date contexts etc).

- As a means of quality assurance. A way to include admissions of ignorance in generative responses and avoid hallucinations. 

## Agents

Go autonomous  with LangChain Agents

Turn your LLMs into reasoning engines that take action, responsibly.

https://python.langchain.com/docs/modules/agents/

## Evaluation

Harden your application with LangSmith evaluation

Don’t ship on “vibes” alone. Define a test suite to capture 
qualitative and quantitative performance metrics.

https://docs.smith.langchain.com/evaluation


## Sources


