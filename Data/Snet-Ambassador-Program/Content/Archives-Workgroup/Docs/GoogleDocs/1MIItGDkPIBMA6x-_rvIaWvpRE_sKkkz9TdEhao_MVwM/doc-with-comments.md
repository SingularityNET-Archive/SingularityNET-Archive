# AI Ethics Strategy for sNET Archives 

> [Comments]
> Context - AI
> * Martin Soki35: My approach ensures that AI systems support rather than replace human decision-making, aligning with contemporary ethical standards. Additionally, I address AI risks such as hallucinations, bias, and security issues, with mitigations through explainability, cultural awareness, and education. This proactive stance will foster trustworthy and accountable AI systems, contributing to ethical, fair, and beneficial outcomes for all stakeholders.
>   - Vanessa Cardui: Hi Martin - we already have your first point, under the heading "Human-centredness".

Would you like to add your other points to the section below on "risk and mitigation", maybe?
>   - Martin Soki35: Hallucinations
   Risk: AI can give wrong information.
   Mitigation: Always provide sources for answers.

Bias
   Risk: AI can be biased.
   Mitigation: Regularly check for bias and be mindful of different cultures.

Consent
   Risk: Issues with copyright and correct credit.
   Mitigation: Ensure sources are properly credited and licensed.

Security
   Risk: Data misuse and manipulation.
   Mitigation: Educate users on secure practices and protect data.
>



# Overview

## Consent 

> [Comments]
> Context - Consent
> * Vanessa Cardui: Is there also something here about AI transparency: i.e. that Archives users should be made aware of when AI is being used e.g  as part of a search tool they are using, or to tag or catalogue material they are looking at? It's not exactly "consent" if there is not an alternative - but maybe there will be? (Resolved by Vanessa Cardui)
>   - Vanessa Cardui: I'd also like to include something on what I would call clarity or honesty or non-deceptiveness - we will not use AI that pretends to be human or to have emotions, or that tries to deceive humans into believing they are ineracting with a human or human-like entity, or arrogates  human functions to itself.

I dunno what people think about this - but it's one of the things I loathe about ChatGPT - it's always pretending to be human. If I ran the world, lol, AI chat bots would be banned even from saying "I feel", and they would definitely be banned from saying "I understand your feelings" or "I will strive to improve ". It's deceptive, and it gives people a mistaken impression of what AI tools actually are.
>   - Colleen Pridemore: I concur completely
>



Respect for Beings, Sentient and non Sentient persons

Open Source and Creative Commons licensing

GDPR



## Beneficial

Do no harm

Benefits all of humanity, not just segments or groups





## Justice



Considerations of equity and equality

Considerations of need and effort

Recognising individual effort and contribution

Recognising merit 

> [Comments]
> Context - Recognising merit
> * Vanessa Cardui: who defines "merit"? and how is the definition shared?

Is there maybe something here about skill or expertise?
>   - Colleen Pridemore: merit still needs clarification.  skills and expertise need to be evaluated to be included within the definition, "merit". Does merit imply the weight or impact their input has had on the project?
>



## Human-centredness?

AI systems should be designed to augment and support human decision-making, not replace it. The SingularityNET Archives will promote human-AI collaboration ,  and will ensure that humans re main in the Loop for guidance and have final say tain  control over AI systems and their outputs when necessary. .  

> [Comments]
> Context - outputs
> * Colleen Pridemore: ...until such a time where consciousness begins to emerge in the AI then we will have to switch to "Guiding" AI.
>





# AI Risks



## 1. Hallucinations (lies   lol)  

> [Comments]
> Context - Hallucinations
> * Colleen Pridemore: I heard MeTTa is working on LLM Hallucinations?
>

Factual errors presented as semantic truths



LLMs do not understand meaning they only return semantic indices (still can be lies  lol)



### Mitigation



Explainability - link to the Why of the response and provide sources (is this also transparency?)

## 2. Bias



Bias in how sources are structured, retrieved, augmented and generated (presented).



### Mitigation



Culture awareness and auditing



Broad prompts may reproduce bias in a sample

Be aware that your question may reflect your culture

Audit responses to see how your data reflects your culture



## 3. Consent

Attribution and copyright issues 

> [Comments]
> Context - Attribution and copyright issues
> * Vanessa Cardui: I think "consent" might cover more than just attribution and copyright.

Is there something here about consent to AI being used at all in a service? Like, a "right to refuse"? Should people be able to say, for example, "I don't want to be assessed by AI for a bank loan" or "I don't want my doctor to use AI to diagnose me" or "I want access to a non-AI search tool on this website" or whatever? Obvs could be hugely impractical - but do/should people have that right? or maybe, should they have it in some contexts?
This prolly connects with the idea of transparency - **knowing** when AI is being used and when it's not - but it occurs to me that transparency is a bit toothless if poeple cannot also object/refuse.
>



### Mitigation



Auditing - check provenance of sources

Accountability Accountivity - check ownership and l i cen s c ing



## 4. Security



Abuse of data - manipulation of private information



Jailbreaking

Prompt injection - malicious prompt manipulation



### Mitigation



Education



Does data augmentation empower the user ?







# Culture



What is your culture ?



What is the intent of your use of AI ?



Your Ethos ?



Is it a consent based process ?



# Governance



Roles and responsibilities of people working with AI

Education about benevolent AI lifecycles

AI risk management and mitigation

How to ensure trust and accountability  ? I think all human-ai-interaction should be recorded, thus keeping it Decentralized



We need to consider the scope of the SNet Archive. A broadly based large generative model is often called a Foundation model. But our intent may be to start with narrowly based data sources that are simply augmented with generative tools. In short we may want to start with just being able to ask the Archive simple questions. But even this step will reveal bias and culture. We need to observe what questions get asked and ask why. Only then can we meaningfully audit the results. 

> [Comments]
> Context - We need to observe what questions get asked and ask why.
> * Vanessa Cardui: Relates to Colleen's point above, about recording all human-AI interactions.

Feels like a 2-step process - record them, then classify them somehow to understand what TYPES of questions they are. Maybe classify by what (and how many) sources an AI needs to use in order to answer them? Some questions, it will just need to look at 1 line in 1 meeting summary, in isolation; other questions, it'll need to combine sources. Quite a different approach for the AI - and interesting if it's needing to look at (for example) 3 different summaries by 3 different people with 3 different sets of biases...
>
> Context - But our intent may be to start with narrowly
> * Colleen Pridemore: I am just curious here.  Why so narrow?  Just because of the situation and the archives growing larger with a fast growing community; hence more data?
>   - Vanessa Cardui: Clarity and relevance, really. Constraining (e.g. via a RAG retrieval process) the sources that your AI can draw on (for example, in our case, constraining it to the Archives corpus itself, plus maybe linked docs) seems likely to give more accurate and relevant answers, and fewer hallucinations and fabrications. But that's a hypothesis, which we would need to test - hence the whole RAG retrieval work  :-)
>   - Colleen Pridemore: I see, yes in using RAG, that makes complete sense. Thanks for the explanation!
>







# Sources



## IBM AI Ethics





https://www.ibm.com/impact/ai-ethics

https://www.ibm.com/topics/ai-ethics



## AI Fairness 360

This extensible open source toolkit can help you examine, report, and mitigate discrimination and bias in machine learning models throughout the AI application lifecycle. We invite you to use and improve it.

https://aif360.res.ibm.com/

## Oxford Institute for Ethics in AI

https://www.oxford-aiethics.ox.ac.uk/



