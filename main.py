import pinecone
from google import genai
import os
from pinecone import ServerlessSpec
from docs1 import text

# add your api key in the env
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
PINECONE_API = os.getenv('PINECONE_API')

# Initialize the gemini
client = genai.Client(api_key=GEMINI_API_KEY)

# Embed the content into vector
response = client.models.embed_content(
    model="text-embedding-004",
    contents=text
)

vector = response.embeddings[0].values

# initialize the pinecone
pi = pinecone.Pinecone(api_key=PINECONE_API)

# add to vector cloud database. This create index if not created already
index_name = "gemini-embedding"
if index_name not in [i["name"] for i in pi.list_indexes()]:
    pi.create_index(name=index_name, dimension=len(vector), spec=ServerlessSpec(
    cloud="aws",
    region="us-east-1",
  ))

index = pi.Index(index_name)

# Insert the content into the index
index.upsert(vectors=[
    {"id": "doc-1", "values": vector, "metadata": {"text": text}}
])

# Users query
query = input("Ask anything about the Food Cuisine: ")


while query != "end":

    # Embed the query into the vector
     q_embed = client.models.embed_content(
         model = 'text-embedding-004',
         contents = query
     )

     query_vector = q_embed.embeddings[0].values

    # Search the vector query in the index
     search = index.query(
         vector = query_vector,
         top_k = 3,
         include_metadata=True
     )

    # Get the content
     content_text = [m.metadata['text'] for m in search.matches]
     content = '\n'.join(content_text)

     prompt = f"""Use the following context to answer the question:

        Context:
        {content}
        
        Question:
        {query}
        
        Answer in a helpful, concise way."""

    # Use the content to get the answer
     answer = client.models.generate_content(
         model="gemini-1.5-flash",
         contents=prompt
     )

     print("Gemini answer:", answer.text, '\n')

    # Type 'end' to end the query
     query = input("Enter your query (enter 'end' to end): ")