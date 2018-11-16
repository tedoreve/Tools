import os
import tarfile
from six.moves import urllib
import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing.label import LabelBinarizerPipelineFriendly
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
#=================================下载数据======================================

def fetch_housing_data(housing_url, housing_path):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

#==================================装载数据=====================================

def load_housing_data(housing_path):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

#============================获得初步处理的数据===================================

def get_housing_data():
    DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
    HOUSING_PATH  = "datasets/housing"
    HOUSING_URL   = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"
    # fetch_housing_data(HOUSING_URL, HOUSING_PATH)
    data          = load_housing_data(HOUSING_PATH)
    # train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
    data["income_cat"] = np.ceil(data["median_income"] / 1.5)
    data["income_cat"].where(data["income_cat"] < 5, 5.0, inplace=True)
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(data, data["income_cat"]):
        strat_train_set = data.loc[train_index]
        strat_test_set  = data.loc[test_index]
    for sets in (strat_train_set, strat_test_set):
        sets.drop(["income_cat"], axis=1, inplace=True)
    # data['median_income'].hist(bins=5, figsize=(20,15))
    # plt.show()
    housing = strat_train_set.drop("median_house_value", axis=1)
    housing_labels = strat_train_set["median_house_value"].copy()
    return housing, housing_labels, strat_test_set

#==============================可视化及初步理解数据================================

def vis_and_insights(housing):
    housing.plot(kind='scatter',x='longitude',y='latitude',alpha=0.1,
                  s=housing['population']/100, label='population',
                  c=housing['median_house_value'],cmap=plt.get_cmap('jet'),
                  colorbar=True)
    plt.legend()
    corr_matrix = housing.corr()
    corr_matrix["median_house_value"].sort_values(ascending=False)
    attributes = ["median_house_value", "median_income", "total_rooms",
    "housing_median_age"]
    scatter_matrix(housing[attributes], figsize=(12, 8))
    housing.plot(kind="scatter", x="median_income", y="median_house_value",
                  alpha=0.1)    
    housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
    housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
    housing["population_per_household"]=housing["population"]/housing["households"]


#===================================准备数据====================================

def prepare_housing_data(housing):
    # housing.dropna(subset=["total_bedrooms"]) # option 1
    # housing.drop("total_bedrooms", axis=1) # option 2
    # median = housing["total_bedrooms"].median()
    # housing["total_bedrooms"].fillna(median) # option 3
    # imputer = Imputer(strategy="median")
    housing_num = housing.drop("ocean_proximity", axis=1)
    # imputer.fit(housing_num)
    # X = imputer.transform(housing_num)
    # X = imputer.fit_transform(housing_num)
    # housing_tr = pd.DataFrame(X, columns=housing_num.columns)
    # encoder = LabelEncoder()
    # housing_cat_encoded = encoder.fit_transform(housing["ocean_proximity"])
    # print(encoder.classes_)
    # encoder = OneHotEncoder()
    # housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1,1))
    encoder = LabelBinarizer()
    housing_cat_1hot = encoder.fit_transform(housing["ocean_proximity"])
    cat_one_hot_attribs = list(encoder.classes_)
    
    
    # attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
    # housing_extra_attribs = attr_adder.transform(housing.values)
    # num_pipeline = Pipeline([
    #         ('imputer', Imputer(strategy="median")),
    #         ('attribs_adder', CombinedAttributesAdder()),
    #         ('std_scaler', StandardScaler()),
    #         ])
    # housing_num_tr = num_pipeline.fit_transform(housing_num)
    
    num_attribs = list(housing_num)
    cat_attribs = ["ocean_proximity"]
    extra_attribs = ["rooms_per_hhold", "pop_per_hhold", "bedrooms_per_room"]
    attributes = num_attribs + extra_attribs + cat_one_hot_attribs
    num_pipeline = Pipeline([
            ('selector', DataFrameSelector(num_attribs)),
            ('imputer', Imputer(strategy="median")),
            ('attribs_adder', CombinedAttributesAdder()),
            ('std_scaler', StandardScaler()),
        ])
    cat_pipeline = Pipeline([
            ('selector', DataFrameSelector(cat_attribs)),
            ('label_binarizer', LabelBinarizerPipelineFriendly()),
        ])
    full_pipeline = FeatureUnion(transformer_list=[
            ("num_pipeline", num_pipeline),
            ("cat_pipeline", cat_pipeline),
        ])
    housing_prepared = full_pipeline.fit_transform(housing)
    return housing_prepared, attributes, full_pipeline


#==================================建模========================================
    
def mod_line(housing_prepared, housing_labels):
    
    line_reg = LinearRegression()
    line_reg.fit(housing_prepared, housing_labels)
    # some_data = housing.iloc[:10000]
    # some_labels = housing_labels.iloc[:10000]
    # some_data_prepared = prepare_housing_data(some_data)
    # some_data_predictions = lin_reg.predict(some_data_prepared)
    # print("Predictions:\t", some_data_predictions)
    # print("Labels:\t\t", list(some_labels))    
    housing_predictions = line_reg.predict(housing_prepared)
    line_mse = mean_squared_error(housing_labels, housing_predictions)
    line_rmse = np.sqrt(line_mse)
    return line_reg, line_rmse

def mod_tree(housing_prepared, housing_labels):
    tree_reg = DecisionTreeRegressor()
    tree_reg.fit(housing_prepared, housing_labels)
    housing_predictions = tree_reg.predict(housing_prepared)
    tree_mse = mean_squared_error(housing_labels, housing_predictions)
    tree_rmse = np.sqrt(tree_mse)
    return tree_reg, tree_rmse

def mod_forest(housing_prepared, housing_labels):
    forest_reg = RandomForestRegressor()
    forest_reg.fit(housing_prepared, housing_labels)
    housing_predictions = forest_reg.predict(housing_prepared)
    forest_mse = mean_squared_error(housing_labels, housing_predictions)
    forest_rmse = np.sqrt(forest_mse)
    return forest_reg, forest_rmse

def mod_test(housing_prepared, housing_labels, mod):
    if mod == 'line':
        reg, rmse = mod_line(housing_prepared, housing_labels)
    elif mod == 'tree':
        reg, rmse = mod_tree(housing_prepared, housing_labels)
    else:
        reg, rmse = mod_forest(housing_prepared, housing_labels)
    
    scores = cross_val_score(reg, housing_prepared, housing_labels,
                             scoring="neg_mean_squared_error", cv=10)
    scores_rmse = np.sqrt(abs(scores))
    disp_scores(scores_rmse)
    return reg, rmse

def mod_tune(housing_prepared, housing_labels, mod, attributes):
    reg, rmse = mod_test(housing_prepared, housing_labels, mod)
    param_grid = [
        {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
        {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
    ]
    grid_search = GridSearchCV(reg, param_grid, cv=5,
                               scoring='neg_mean_squared_error')
    grid_search.fit(housing_prepared, housing_labels)
    # print(grid_search.best_params_)
    # print(grid_search.best_estimator_)
    # cvres = grid_search.cv_results_
    # for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    #     print(np.sqrt(-mean_score), params)
    feature_importances = grid_search.best_estimator_.feature_importances_
    print(sorted(zip(feature_importances, attributes), reverse=True))
    return grid_search.best_estimator_
#=================================自定义转换器===================================

rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6
    
class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self # nothing else to do
    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,
                         bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]
 
class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values

#===================================小工具们=====================================

def disp_scores(scores):
    print("===================")
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())
    print("===================")

#====================================主程序=====================================

if __name__ == "__main__":
    
    housing, housing_labels, strat_test_set = get_housing_data()
    # vis_and_insights(housing)
    housing_prepared, attributes, full_pipeline = prepare_housing_data(housing)
    final_model = mod_tune(housing_prepared, housing_labels, 'forest', attributes)
    X_test = strat_test_set.drop('median_house_value', axis=1)
    y_test = strat_test_set['median_house_value'].copy()
    
    X_test_prepared = full_pipeline.transform(X_test)
    final_predictions = final_model.predict(X_test_prepared)
    final_mse = mean_squared_error(y_test, final_predictions)
    final_rmse = np.sqrt(final_mse)

#==============================================================================
