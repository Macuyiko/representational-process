import gensim
import loadRandomWalks
import time


def learn(folderName, walksName, vectorsize=16, ignore_gateways=False, epochs=10):
    documents = loadRandomWalks.get_doc(folderName, walksName, ignore_gateways)
    print('Data Loading finished. ')
    print(documents[0])
    model = gensim.models.Doc2Vec(documents, dm=0, alpha=0.025, size=vectorsize, window=2, min_alpha=0.001, min_count=1)
    model.train(documents,len(documents), epochs=epochs)
    model.save('output/'+folderName+walksName+'M2VVS'+ str(vectorsize)+'.model')
    model.save_word2vec_format('output/'+folderName+ walksName+'M2VVS'+ str(vectorsize)+'.word2vec')
