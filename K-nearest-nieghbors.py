import math
import numpy as np
import sklearn.datasets as sk
# cancer = sk.load_breast_cancer()
# feat = cancer.feature_names
# print(len(feat), " Features")
# print(len(cancer.data), " Instances")
# print(cancer.target_names)
# print(cancer.DESCR)


# boston = sk.load_boston()
# features = boston.feature_names
# print(len(features), " Features")
# print(len(boston.data), " Instances")
# print("Task: \n ____________________________________", boston.DESCR)

def convert_to_list(data):
    if type(data) == dict:
        convtrainingset = []
        for item in enumerate(data.items()):
            it = list(item)
            convtrainingset.append(it)
    if type(data) == tuple:
        if len(data) > 2:
            convtrainingset = []
            s, st = 0, 2
            for item in data:
                convtrainingset.append(list(data[s:st]))
                s += 2
                st += 2
                if len(data) == s:
                    break
    else: 
        convtrainingset = data
    return convtrainingset


def most_frequent(List):
    return max(set(List), key = List.count)


def distance_formula(feature1, feature2):
    distance = 0.0
    distance += ((feature1[1] - feature2[1])**2) + ((feature1[0] - feature2[0])**2)
    return math.sqrt(abs(distance))


def classify(list_of_neighbors, target_series):
    classes = []
    for key in list_of_neighbors:
        row_num = list_of_neighbors[key]
        class_num = target_series[row_num]
        classes.append(class_num)

    return classes


def k_nearest_neighbors(trainingset, targetset, data_point, nearest_neighbors):
    if type(trainingset) != list:
        trainingset = convert_to_list(trainingset)
    
    dict_of_dist = {}     
    n = 0                
    for point in trainingset:
        dist = distance_formula(point[:2], data_point[:2])
        dict_of_dist[dist] = n
        n += 1
    dict_of_dist = dict(sorted(dict_of_dist.items()))   #Working
    temp = [[key, value] for key, value in dict_of_dist.items()]
    neighbors = {value[0]:value[1] for key, value in enumerate(temp[:nearest_neighbors])}

    class_name = most_frequent(classify(neighbors, targetset))

    return f"class is {class_name}"

sample_class1 = [5, 3.2]
sample_class2 = [5.4, 3]
sample_class3 = [6.7, 3.3]

iris = sk.load_iris()

df = iris.data
t_df = iris.target
df = df.tolist()


print(k_nearest_neighbors(df, t_df, sample_class3, 3))
print(k_nearest_neighbors(df, t_df, sample_class2, 3))
print(k_nearest_neighbors(df, t_df, sample_class1, 3))