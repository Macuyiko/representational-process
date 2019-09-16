import gensim
import loadXES
import time

def learn(folderName, vectorsize=16, epochs=10, docid_only=False, merge_traces=False):
    documents = loadXES.get_doc_multiple_XES_tagged(folderName, docid_only=docid_only, merge_traces=merge_traces)
    print('Data Loading finished')
    print(documents[0])
    model = gensim.models.Doc2Vec(documents, dm=0, alpha=0.15, vector_size=vectorsize, window=1, min_alpha=0.001, min_count=0,
        max_vocab_size=None, dbow_words=1, hs=0, negative=0, sample=0, dm_concat=1, dm_mean=0)
    model.train(documents, len(documents), epochs=epochs)
    model.save('output/'+folderName+'L2VVS'+str(vectorsize) +'.model')
    model.save_word2vec_format('output/'+folderName+ 'L2VVS'+str(vectorsize) + '.word2vec')
