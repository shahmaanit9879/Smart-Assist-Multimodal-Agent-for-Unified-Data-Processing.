import faiss
import numpy as np
import json
from .embedder import Embedder

class RAGPipeline:
    def __init__(self, data_path="data/knowledge.json"):
        self.embedder = Embedder()

        with open(data_path, 'r') as f:
            self.docs = json.load(f)

        embeddings = [self.embedder.encode(d["text"]) for d in self.docs]
        self.index = self.build_index(embeddings)

    def build_index(self, embeddings):
        dim = len(embeddings[0])
        index = faiss.IndexFlatL2(dim)
        index.add(np.array(embeddings))
        return index

    def retrieve(self, query):
        q_emb = self.embedder.encode(query)
        dist, idx = self.index.search(np.array([q_emb]), k=3)
        return "\n".join([self.docs[i]["text"] for i in idx[0]])
