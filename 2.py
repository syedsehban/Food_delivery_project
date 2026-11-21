import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("food_delivery.csv")
print(df.head(5))

print(df.columns)
print(df.info())

df=df.drop(columns=['Id','Delivery_person_ID','Restaurant_lotitude','Restaurant_longitude','Restaurant_latitude','Delivery_location_latitude','Delivery_location_longitude','Time_Order_picked'],errors='ignore')
df.columns=df.columns.str.capitalize()
df=df.rename(columns={"Time_orderd" : "Time_Ordered"})
print(df.head())


print(type(df["Delivery_person_age"][1]))
print(type(df["Delivery_person_ratings"][1]))
print(type(df["Time_Ordered"][0]))
print(df.duplicated().sum())

df['Delivery_person_age']=pd.to_numeric(df["Delivery_person_age"],errors='coerce')
df["Delivery_person_ratings"]=pd.to_numeric(df["Delivery_person_ratings"],errors='coerce')
print(df.isna().sum())


missing_percentage=df.isna().mean()*100
print(missing_percentage)
df=df.dropna()
print(df)

df['Order_date']=pd.to_datetime(df['Order_date'])
print(df['Order_date'])

data=df['Time_Ordered']
print(data)
df['Time_Ordered']=pd.to_datetime(df['Time_Ordered'],errors='coerce')
plot1=sns.scatterplot(x='Delivery_person_age',y='Delivery_person_ratings',data=df)
plt.show()
df=df.dropna(subset=['Road_traffic_density'])
plot2=sns.boxplot(x='Road_traffic_density',y='Delivery_person_ratings',data=df)
plt.title('Rating  distribution by traffic density')
plt.show()

plot3=pd.crosstab(df['Weatherconditions'],df['Vehicle_condition'])
sns.heatmap(plot3,annot=True,fmt='d',cmap='YlGnBu')
plt.title('Frequency:Weather vs. VehicleConditions')
plt.show()






