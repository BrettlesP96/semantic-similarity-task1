import spacy

nlp = spacy.load('en_core_web_md')

def semantic_similarity(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return doc1.similarity(doc2)

text1 = "cat"
text2 = "monkey"
text3 = "banana"

similarity12 = semantic_similarity(text1, text2)
similarity13 = semantic_similarity(text1, text3)
similarity23 = semantic_similarity(text2, text3)

print(f"Similarity between {text1} and {text2}: {similarity12:.4f}")
print(f"Similarity between {text1} and {text3}: {similarity13:.4f}")
print(f"Similarity between {text2} and {text3}: {similarity23:.4f}")