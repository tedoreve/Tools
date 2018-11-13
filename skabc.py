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
from sklearn.base import BaseEstimator, TransformerMixin


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
    return housing, housing_labels

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
    imputer = Imputer(strategy="median")
    housing_num = housing.drop("ocean_proximity", axis=1)
    # imputer.fit(housing_num)
    # X = imputer.transform(housing_num)
    X = imputer.fit_transform(housing_num)
    housing_tr = pd.DataFrame(X, columns=housing_num.columns)
    # encoder = LabelEncoder()
    # housing_cat_encoded = encoder.fit_transform(housing["ocean_proximity"])
    # print(encoder.classes_)
    # encoder = OneHotEncoder()
    # housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1,1))
    encoder = LabelBinarizer()
    housing_cat_1hot = encoder.fit_transform(housing["ocean_proximity"])
    return housing_tr, housing_cat_1hot

#=================================自定义转换器===================================


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

#====================================主程序=====================================


if __name__ == "__main__":
    
    housing, housing_labels = get_housing_data()
    # vis_and_insights(housing)
    housing_tr ,housing_cat_1hot = prepare_housing_data(housing)
    
    rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6
    attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
    housing_extra_attribs = attr_adder.transform(housing.values)
#==============================================================================
