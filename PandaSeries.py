import pandas as pd
import numpy as np

s=pd.Series([1,2,3,4],index=['A','B','C',"D"],dtype=float)
print(s)

data=np.array(['c','s','h','a','r','p','c','o','r','n','e','r'])
s=pd.Series(data)
print(s[:4])
print(s[5:])
print(s[1:6])
print(s[6])

d={'Day':420,'Day2':421}
s=pd.Series(d)
print(s)

#Label based Indexing
data=np.array(['c','s','h','a','r','p','c','o','r','n','e','r','c'])
ser=pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])
print(ser[17])

df=pd.read_csv('../Python Sample Dataset/horse.csv',nrows=10)
print(df.columns)
ser=pd.Series(df['surgery'])
data=ser.head(10)

#   Adding 2 series
ser1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
ser2 = pd.Series([1, 2, 3], index=['a', 'b', 'e'])
df_sum=ser1.add(ser2)
print("Add:",df_sum)
s_prod=ser1.sum(axis=0)
print("Sum:",s_prod)

ser1['f']=25
ser3=pd.concat((ser1,ser2))
print(ser3)

# Basic arithmetics 
s_sub = ser1.sub(ser2)
print("Sub:\n", s_sub)

s_mul = ser1.mul(ser2)
print("\nMul:\n", s_mul)

s_div = ser1.div(ser2)
print("\nDiv:\n", s_div)

s_pow = ser1.pow(ser2)
print("\nPow:\n", s_pow)

s_mean = ser1.mean()
print("\nMean:", s_mean)

s_prod = ser1.prod()
print("Product:", s_prod)

s_abs = ser1.abs()
print("\nAbs:\n", s_abs)

s_count = ser1.count()
print("\nCount:", s_count)

s_size = ser1.size
print("Size:", s_size)

print("\nIs Unique:", ser1.is_unique)



data = {
    'Country': ['India', 'USA', 'UK'],
    'Capital': ['New Delhi', 'Washington DC', 'London'],
    'Population': [1400, 331, 67]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)

Df=df['Country']
print(Df)
print()

def pandas_df():
    data = {
    'Country': ['India', 'USA', 'UK'],
    'Capital': ['New Delhi', 'Washington DC', 'London'],
    'Population': [1400, 331, 67]
    }

    df = pd.DataFrame(data)
    
    # Column selection
    Df = df[['Country', 'Capital']]
    print(Df)

    # Row selection
    data1 = Df.loc[0]   # returns the first row
    print(data1)

    data1 = Df.loc[0:1]  # returns the first 2 rows (inclusive)
    print(data1)

    data1 = Df.loc[1:2]  # returns rows 1 and 2
    print(data1)


    data = {
        'Name': ['C', 'Sharp', 'Corner'],
        'Age': [20, 21, 22],
        'Address': ['Delhi', 'Kanpur', 'Tamil Nadu']
    }
    df = pd.DataFrame(data)

    # Checking null values
    print(df.isnull())

    data1 = {
        'Name': [np.nan, 'Sharp', 'Corner'],
        'Age': [20, np.nan, 22],
        'Address': [np.nan, 'Kanpur', 'Tamil Nadu']
    }
    df1 = pd.DataFrame(data)

    # Checking null values
    print(df1.isnull())
    print('fill',df1.fillna(0))

    # Creating another dictionary
    f = {
        "Array_1": [49.50, 70],
        "Array_2": [65.1, 49.50]
    }
    data=pd.DataFrame(f)
    print(data.replace(49.50,60))

    for i,j in df.items():
        print(i,j)
        print

def interpolation():
    
    df = pd.DataFrame({
        'A': [1, np.nan, np.nan, 4, np.nan, 6, np.nan, 8]
    })

    print("Original DataFrame:\n", df)

    linear = df.interpolate(method='linear')
    print("\nLinear:\n", linear)

    nearest = df.interpolate(method='nearest')
    print("\nNearest:\n", nearest)

    quadratic = df.interpolate(method='quadratic')
    print("\nQuadratic:\n", quadratic)

    cubic = df.interpolate(method='cubic')
    print("\nCubic:\n", cubic)

    forward = df.interpolate(method='linear', limit_direction='forward',inplace=False)
    print("\nForward:\n", forward)

    backward = df.interpolate(method='linear', limit_direction='backward',inplace=False)
    print("\nBackward:\n", backward)


#############################################################################
#pandas_df()
interpolation()