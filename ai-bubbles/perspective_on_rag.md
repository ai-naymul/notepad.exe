My Perspective on ai agent

Approach 1: PURE LLM call(NO EMBEDDING OR VECTOR SEARCH) not a rag agent… just a execution agent + llm

- In this approach we don’t need any embedding model to make vectors for our collection and questions or inputs…
- A vector search can be perform or regular model call to the question to route that question if its about crypto or ai or anything else… We can have different execution agent for each category
- By giving info to model about our schema with a top level description about each nested element(Specific to model so can get better results) with a few shot example of how the schema can be in our database
- Generate a db query regarding that question and perform that query in our database and get the response and pass it to model again get a beautiful descriptive results…(Ex: Latest price of bitcoin is 100k usd on march 2 2025)
- We can deploy a small model of our own for this task so we don’t need to use any gpt overprice model…

Appraoch 2 : What we implemented on recent code(26 feb) can call it rag approach:

* Finds relevant collections via vector search(Need a embedding model can be openai or open source)
* Generates aggregation pipeline using GPT-4o
* Executes query against MongoDB
* Produces natural language response using GPT-4
* Finds relevant collections via vector search
* Generates aggregation pipeline using GPT-4o
* Executes query against MongoDB
* Produces natural language response using LLM

Potential issue with rag agen:
- We are defining database schema on our own so when making vector similarity search it is not more reliable than then the approach 1. For example, we stored all the coinmarketcap things inside the cmc class if you perform cmc the its not that similar like coinmarket or relevant but if we say model that cmc stands for coinmarketcap it can give more accurate mongoldb query for us.
- In approach one we are using pure llm call so no worries about embedding model



Are we gonna deploy our own small model or use any llm provider service? I think deploying our own a small model that can only give us the mongodb query is more price effective than using close source model….

Or gemini due to its low cost…..


