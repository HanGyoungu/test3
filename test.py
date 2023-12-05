import streamlit as st  
import numpy as np  
import math as m
import cv2
import matplotlib.pyplot as plt
import os 
import sys 
import random 
import pandas as pd
os.system('cls')


col1, col2 = st.columns([1,2])
with col1:
    st.image('cat.jpg', width=300)
with col2:
    '놓치면 후회할 인재(고먐미, 시급 츄르3개)'
    '전화번호(📞):010-xxxx-xxxx'
    '이메일(💌): strustar@konyang.ac.kr'
    '주소(🏠): 충남 논산시 대학로 121'

col= st.columns(4)
with col[0]:
    st.link_button("Google(🌐)", "https://google.com")
with col[1]:
    st.link_button("Naver(✅)", "https://naver.com")
with col[2]:
    st.link_button("Daum(💚)", "https://Daum.net")
with col[3]:
    st.link_button("Facebook(ⓕ)", "https://facebook.com")

''
''
'## :orange[자기 소개]'
'#### 저는 시골에서 2남1녀의 :red[가난한 집]에서 태어나...'



sys.exit()
fig, ax = plt.subplots()

x = []
y = []
for i in range(-10, 11, 1): 
    x.append(i)
    y.append(3*i**3 - 5*i**2 + 3*i - 7)

col1,col2,col3 = st.columns(3)

with col1:
    cc = st.radio('선의 색을 선택하시오.', ['red', 'green', 'blue', 'orange', 'm','c'])
with col2:
    ma =  st.radio('마커의 형태를 선택하시오.', ['x','^', 'o', 's','p','h','*'])
with col3:
    ls =  st.radio('선의 형태를 선택하시오.', [':', '--', '-', '-.'])
plt.plot(x,y, color = cc, marker = ma, linestyle = ls)

# plt.plot(x,y, ':cx')
st.pyplot(fig)











































# fig, ax = plt.subplots()

# a = 2
# b = -5
# c = 3
# d = -7

# x = []
# y = []
# for i in range(-100,101,50):
#     x.append(i)
#     y.append(a*i**3 + b*i**2 + c*i + d)
# col1, col2, col3 = st.columns(3)
# with col1:
#     color = st.radio('색을 선택하시오', ('red', 'green', 'blue'))
# with col2:
#     linestyle = st.radio('선의 스타일을 선택하시오.', ('-', '-.', ':'))
# with col3:
#     marker = st.radio('마커의 스타일을 선택하시오.', ('s', '^', 'o'))

# plt.plot(x,y, color = color, marker = marker, linestyle = linestyle)

# st.pyplot(fig)














sys.exit()
st.write('Hello, *World!* :sunglasses:')

'# Hello, *World!* **tt** ***cc***  :red[red] :green[green] :blue[blue]💮💤'
'## Hello, *World!* **tt** ***cc***  :red[red] :green[green] :blue[blue]💮💤'
'### Hello, *World!* **tt** ***cc***  :red[red] :green[green] :blue[blue]💮💤'
'#### Hello, *World!* **tt** ***cc***  :red[red] :green[green] :blue[blue]💮💤'
'##### Hello, *World!* **tt** ***cc***  :red[red] :green[green] :blue[blue]💮💤'
'###### Hello, *World!* **tt** ***cc***  :red[red] :green[green] :blue[blue]💮💤'

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)




# li = [1,2,3,4]
# n = np.array(li)
# p = pd.Series(li, index=['a','b','c','d'])
# li
# n  
# p



list1 = list([['한빛','남자','20','180'], ['한결','남자','21','177'], ['김한결','중성','51','167'], ['한라','여자','20','160']])
n = np.array(list1)
col_names = ['이름', '성별', '나이', '키']
df = pd.DataFrame(list1, columns=col_names, index=['1행','2행','3행','4행'])


genre = st.radio("선택하시오.", ["오름차순", "내림차순", "기타", "요약"], horizontal=True, index=2 )  

number = st.number_input('Insert a number', value=20, step=1)
df.iloc[3,2] = number

if '오름' in genre:
    st.dataframe(df.sort_values(by=['키']))
if '내림' in genre:
    st.dataframe(df.sort_values(by=['키'], ascending=False))
if '기타' in genre:
    st.dataframe(df)
if '요약' in genre:
    st.dataframe(df.describe())



# li = [1,2,3,4]
# li

# for i in range(4):
#     li[i] = li[i] + 3
# li

# li = np.array([1,2,3,4])
# li
# li_sort = np.sort(li)[::-1]
# li_sort
































# t = turtle.Turtle()
# t.shape('turtle')



# os.system('cls')

# a = np.array([1,10,-5,2])
# print(np.abs(a))
# print(np.sqrt(a))
# print(a**0.5)
# print(np.square(a))
# print(a**2)















# a= np.arange(8)
# a
# a.shape = (4,2)
# a
# b = a.flatten()
# b
# b.resize((4,2))
# b
# c = np.resize(b,(2,4))
# c





# list = [10,10,10,10,10],  [10,10,10,10,10], [10,10,10,10,10], [10,10,10,10,10]
# n = np.array(list)
# n


# n = np.eye(10)
# n




# n = 100
# for i in range(1, n+1):
#     if i%7 == 3:
#         i

# n=3
# arr = np.full((n,n),'나머지')


# for i in range(n):
#     for j in range(n):
#         # arr[i,j] = '나머지'
#         if i == j or  i+j==n-1:
#             arr[i,j] = '대각선'
#         # if i+j==n-1:
#             # arr[i,j] = '대각선'
# arr



# n = np.full((4,5),10)
# n

# n2 = []
# n2.append(10)
# n2
# n2 = np.append(n2, 15)
# n2

# arr = np.array([1,2,3])
# s = arr.sum()
# s
# s1 = np.sum(arr)
# s1

# arr.







































# list1 = [[1,2,3,4], [3,5,7,9]]
# a = np.array(list1)
# a



# n = np.full((10,5),7)

# n = np.eye(5)
# n

# def user_eye(n):
#     arr = np.zeros((n,n))
#     for i in range(n):
#         for j in range(n):
#             if i == n-j+1:
#                 arr[i,j] = 1
#     return arr

# arr = user_eye(10)
# arr





















































