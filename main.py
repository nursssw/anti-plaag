def jaccard_similarity(x,y):
  intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
  union_cardinality = len(set.union(*[set(x), set(y)]))
  return intersection_cardinality/float(union_cardinality)

sentences = ["Hello, everybody! This is the content of the first file!",
"Hello everybody! This is the content of the third file"]
sentences = [sent.lower().split(" ") for sent in sentences]
jaccard_similarity(sentences[0], sentences[1])
print(sentences)
