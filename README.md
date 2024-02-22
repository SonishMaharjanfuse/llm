# Word Embedding

Word Embedding is the porcess of converting text to numbers. As the text is incompactible with ML and DL the text must be converted to numbers. 

example: "I am familier with word embedding"

["I", "am", "familier", "with", "word", "embedding"]

[0, 1, 2, 3, 4, 5]

## Types of Word Embedding

There are different types of embedding broadly classifed into:
- Frequency-based Embedding
- Prediction-based Embedding

### Frequency-based Embedding

It is also generally of three types:

- Count Vector
- TF-IDF Vector
- Co-Occurance Vector

#### Count Vector

D1: Ram is a boy. He has a boy named sam.
D2: Sita husband name is Ram. She also has a boy.

    Ram Sita    boy named   sam wife    husband
D1: 1   0       2   1       1   0       0
D2: 1   1       1   0       0   0       1

#### TG-IDF Vector

Consider the below sample table which gives the count of terms(tokens/words) in two documents.

![Alt text](image.png)

Now, let us define a few terms related to TF-IDF.

TF = (Number of times term t appears in a document)/(Number of terms in the document)

So, TF(This,Document1) = 1/8

TF(This, Document2)=1/5

It denotes the contribution of the word to the document i.e words relevant to the document should be frequent. eg: A document about Messi should contain the word ‘Messi’ in large number.

IDF = log(N/n), where, N is the number of documents and n is the number of documents a term t has appeared in.

where N is the number of documents and n is the number of documents a term t has appeared in.

So, IDF(This) = log(2/2) = 0.

So, how do we explain the reasoning behind IDF? Ideally, if a word has appeared in all the document, then probably that word is not relevant to a particular document. But if it has appeared in a subset of documents then probably the word is of some relevance to the documents it is present in.

Let us compute IDF for the word ‘Messi’.

IDF(Messi) = log(2/1) = 0.301.

Now, let us compare the TF-IDF for a common word ‘This’ and a word ‘Messi’ which seems to be of relevance to Document 1.

TF-IDF(This,Document1) = (1/8) * (0) = 0

TF-IDF(This, Document2) = (1/5) * (0) = 0

TF-IDF(Messi, Document1) = (4/8)*0.301 = 0.15

As, you can see for Document1 , TF-IDF method heavily penalises the word ‘This’ but assigns greater weight to ‘Messi’. So, this may be understood as ‘Messi’ is an important word for Document1 from the context of the entire corpus.


