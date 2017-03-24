import urllib.request
import json
import dml
import prov.model
import datetime
import uuid
import requests

class linearRegressionObesityTime(dml.Algorithm):
        contributor = 'asafer_asambors_maxzm_vivyee'
        reads = ['asager_asambors_maxzm_vivyee.obesity_time']
        writes = ['asager_asambors_maxzm_vivyee.obesity_time_linear_reagression_data']

        @staticmethod
        def execute(trial=False):
                startTime = datetime.datetime.now()

                #set up the connection
                client = dml.pymongo.MongoClient()
                repo = client.repo
                repo.authenticate('asafer_asambors_maxzm_vivyee','asafer_asambors_maxzm_vivyee')


                #loads
                obesity_time = repo['asafer_asambors_maxzm_vivyee.obesity_time'].find()

                obesity_time_tuples = [[a['time'],a['data_value']] for a in obesity_time]

                X = [:,0] # x will be the time it takes to get to a healthy location
                Y = [:,1] # y is going to be the obesity percent

                # we are going to run a linear regression that predicts the current level of obesity given how long it takes to get somewhere healthy

                meanX = sum(X)*1.0/len(X)
                meanY = sum(Y)*1.0/len(Y)

                varX = sum([(v-meanX)**2 for v in X])
                varY = sum([(v-meanY)**2 for v in Y])

                minYHatCov = sum([(X[i]-meanX)*(Y[i]-meanY) for i in range(len(Y))])

                B1 = minYHatCov/varX
                B0 = meanY-B1*meanX

                return {"start":startTime, "end":endtime}

        @staticmethod
        def provenance(doc = prov.model.ProvDocument(), startTime = None, endTime = None):
                #TODO write this :/

