# Pest-Chatbot
Contains the files used to make the chatbot, multiple different ways of generating a knowledge graph + embeddings, then also slightly different ways to communicate with the chatbot.  
When running w/ Exllamav2: 
pros: fully local, no rate/token limits. 
cons: requires 15gb of gpu ~ limited by hardware, slower than the api. 
*Please note that due to my computer limitations the Exllama notebooks were ran on kaggle using the 2x T4 gpu option

When running w/ HuggingFace api: pros: fast compared to exllamav2, 
can easily use different models, allows the user to surpass hardware limitations. 
cons: rate/token limits, not fully local.  

When running w/ ollama: 
pros: fully local, easy to setup.
cons: limited by hardware.
