# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.tree import DecisionTreeClassifier
# import joblib
# ## 경고창 무시
# import warnings
#
# warnings.filterwarnings(action='ignore')
#
#
# def pred_module():
#     # 데이터 불러오기
#     data = pd.read_csv('../mlData/쇼핑몰_최종2.xlsx')
#     data = data.dropna(axis=0)
#     data['네이버 태그 클릭량'] = data[['네이버 태그 클릭량']].apply(pd.to_numeric)
#     print('data를 찍어봅시다.>> ', data)
#     # 라벨 인코딩
#     le = LabelEncoder()
#     data['TAG'] = le.fit_transform(data['TAG'])
#     data['평일휴일'] = le.fit_transform(data['평일휴일'])
#     data['요일'] = le.fit_transform(data['요일'])
#     data['시간대'] = le.fit_transform(data['시간대'])
#     data['성별'] = le.fit_transform(data['성별'])
#     data['연령대'] = le.fit_transform(data['연령대'])
#
#     # train_test_split
#     X = pd.DataFrame(data, columns=['평일휴일', '요일', '시간대', '성별', '연령대', '건수합계', '네이버 태그 클릭량'])
#     y = pd.DataFrame(data['TAG'].values.reshape(-1, 1))
#     X_train, X_test, y_train, y_test = train_test_split(X,
#                                                         y,
#                                                         test_size=0.2,
#                                                         random_state=3
#                                                         )
#
#     # 의사결정나무
#     dt_clf = DecisionTreeClassifier(random_state=156)
#     dt_clf.fit(X_train, y_train)
#     return dt_clf
#
