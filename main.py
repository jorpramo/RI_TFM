import mongodb
__author__ = 'jpradas'
reader = MongoDBCorpusReader(db='test',collection='DOCS', field='nombre')
reader.text()
reader.__len__()