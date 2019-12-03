import pickle

def loadPickle(filename):
    filename = 'Models/' + filename + pickle_ext
    file = open(filename, 'rb')
    model = pickle.load(file)
    file.close()
    return model

def savePickle(model, filename):
    filename = 'Models/' + filename + pickle_ext
    file = open(filename, 'wb+')
    pickle.dump(model, file)
    file.close()

pickle_ext = '.p'
article_training_data_loc = 'Data/articles-training-byarticle-20181122.xml'
article_ground_truth_data_loc = 'Data/ground-truth-training-byarticle-20181122.xml'
# TODO: Add Name below
publisher_training_data_loc = 'Data/addName.xml'
publisher_ground_truth_data_loc = 'Data/addName.xml'
training_data_schema = 'Data/article.xsd'
ground_truth_schema = 'Data/ground-truth.xsd'
train_text_tsv = 'Data/train.text.tsv'
