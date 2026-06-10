import numpy as np
from sentence_transformers import SentenceTransformer


def cosine_sim(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


model = SentenceTransformer("all-MiniLM-L6-v2")

referencia = "dor torácica intensa"
comparar = [
    "angina pectoris",
    "fibrilação atrial com flutter",
    "como tratar diabetes tipo 2",
    "prescrição de varfarina",
]

emb_ref = model.encode(referencia)

print(f"\nReferência: '{referencia}'\n")
for frase in comparar:
    emb = model.encode(frase)
    sim = cosine_sim(emb_ref, emb)
    barra = "█" * int(sim * 20)
    print(f"  {sim:.2f}  {barra:<20}  {frase}")
print()
