import pandas as pd
col=["name","國文","數學", "英文",  "自然", "社會"]
data=[["小林",'75', '62', '85', '73', '60' ],["小黃", "91", '53' ,'56',  '63', '65'],["小陳",'71', '88', '51', '69', '87'],["小美",'69', '53', '87' ,'74', '70' ]]
df=pd.DataFrame(data,columns=col) #columns=列 科目才能上面
print(df) #輸出每一項

print("後二位的成績")
print(df.iloc[2:4,:])


sector = df.groupby("自然")
print("自然遞減排序")
print(df["自然"].sort_values(ascending=False))













