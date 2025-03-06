Evaluation Question set for Ai Agent Prompt

About Us:

There are thousands of ai tools and companies out there for many different task…There are also many different crypto coin exchanges out there in the world. In our organization what we are trying to do is that combining ai tools and crypto coin and exchanges data we are trying to make a visualize platform for them with their details… Back before our product people need to visit multiple sites to see how a crypto coin is working or growing about that crypto coin…. So by using our platform people can do that in a single platform same as well for ai tools ai is growing we are making people aware of ai tools all a complete platform for ai and crypto data with analysis…


Here is the database collections we are using:
['CryptoDetails', 'YCombinator', 'TheresAnAIForThat', 'Crypto', 'FutureTools']}

AI Section are the:
TheresAnAIForThat, Ycombinator, Futuretools, Producthunt

Crypto Section are the:
Crypto, CryptoDetails


Here is the context:

We are trying to build a chat system agent where user can came and chat with our agent and our agent will response using our database…. Here is the plan we decided for our agent:


Approach 1: PURE LLM call(NO EMBEDDING OR VECTOR SEARCH) not a rag agent… just a execution agent + llm

•⁠ ⁠In this approach we don’t need any embedding model to make vectors for our collection and questions or inputs…
•⁠ ⁠A vector search can be perform or regular model call to the question to route that question if its about crypto or ai or anything else… We can have different execution agent for each category
•⁠ ⁠By giving info to model about our schema with a top level description about each nested element(Specific to model so can get better results) with a few shot example of how the schema can be in our database
•⁠ ⁠Generate a db query regarding that question and perform that query in our database and get the response and pass it to model again get a beautiful descriptive results…(Ex: Latest price of bitcoin is 100k usd on march 2 2025)
•⁠ ⁠We can deploy a small model of our own for this task so we don’t need to use any gpt overprice model…

Appraoch 2 : What we implemented on recent code(26 feb) can call it rag approach:

•⁠ ⁠Finds relevant collections via vector search(Need a embedding model can be openai or open source)
•⁠ ⁠Generates aggregation pipeline using GPT-4o
•⁠ ⁠Executes query against MongoDB
•⁠ ⁠Produces natural language response using GPT-4
•⁠ ⁠Finds relevant collections via vector search
•⁠ ⁠Generates aggregation pipeline using GPT-4o
•⁠ ⁠Executes query against MongoDB
•⁠ ⁠Produces natural language response using LLM



We could have both approach in our system combined could name it a hybrid system…

Task:

So your task is after analyzing the context above you have to to create few (10-100) evaluation test data(Questions that will be used to test our system) (1. Factual 2. Multihop - require multiple db call over multiple collections/tables) (with ground truth - known data) to then see.. which approach does better.