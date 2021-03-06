from data import Data
# import vis
from model import Model
from time import time

if __name__ == '__main__':
    # create data class, which import the 2015-2016 crime data in Chicago
    crimes = Data()
    # randomly sample 0.2 data to save computational time
    crimes.random_sample(0.2)
    # preprocessing function in Data class includes:
    # change data index,
    # encode some features to label,
    # create new feature
    # and split data to train and test.
    crimes.preprocessing()

    # create a model class with grid search parameters by accuracy
    # Optimal parameters are assigned
    # run_all function fits the model then evaluates the performance in test data
    start = time()
    param_logit_grid = {'logit_grid':
                            {'penalty': ['l1', 'l2'],
                             'C': [10 ** i for i in range(-3, 1, 1)]}}
    logit = Model(crimes, 'logit', param_logit_grid)
    logit.grid_search_all('accuracy', 3)
    logit.run_all('accuracy', 3)
    end = time()
    print 'Time used for logistic regression: {} min.'.format((end - start) / 60)

    # Similar grid search is made for xgboost model. Best parameters are chosen as follows.
    start = time()
    param_xgb = {'xgb': {'learning_rate': 0.1,
                         'n_estimators': 650,
                         'gamma': 1,
                         'max_depth': 4,
                         'subsample': 1}}
    xgb = Model(crimes, 'xgb', param_xgb)
    xgb.run_all()
    end = time()
    print 'Time used for XGboost: {} min.'.format((end - start) / 60)
