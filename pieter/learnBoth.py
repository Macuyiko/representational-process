import Act2Vec, Trace2Vec, Log2Vec, Model2Vec

folderName="PLG2"
walksName="Structural"
Model2Vec.learn(folderName, walksName, 16, ignore_gateways=False, epochs=20)

#folderName="generated_1000"
#Log2Vec.learn(folderName, 16, docid_only=True, merge_traces=False)