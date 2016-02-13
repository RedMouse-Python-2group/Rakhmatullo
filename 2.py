# -*- coding: utf-8 -*-
# Laba 2.1
st = raw_input("Enter str:  ")
st = st.split(' ')
n = ''
for i in st:
    if len(i) > len(n):
        n=i
print('The longest word is: ', n)
