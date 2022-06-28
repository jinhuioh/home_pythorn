# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.tree import DecisionTreeClassifier
# import joblib
# ## 경고창 무시
# import warnings
# warnings.filterwarnings(action='ignore')
# from ai.mlPickle import pred_module
#
# tag_predict = joblib.load('tag_predict.pkl')
#
# def pred_tag(data):
#     # 예측 결과 출력
#     result = tag_predict.predict_proba([data])
#     if result[0][0] == 1:
#         print('생활/사무용품')
#     elif result[0][1] == 1:
#         print('식료품')
#     elif result[0][2] == 1:
#         print('애완용품')
#     elif result[0][3] == 1:
#         print('인테리어')
#     elif result[0][4] == 1:
#         print('취미용품')
#     elif result[0][5] == 1:
#         print('패션')
#     elif result[0][6] == 1:
#         print('화장품')