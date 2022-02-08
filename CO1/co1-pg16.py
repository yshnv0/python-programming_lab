Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="hello world"
>>> s1=s.split()
>>> s1
['hello', 'world']
>>> a=s[0]
>>> a
'h'
>>> a=s1[0]
>>> a
'hello'
>>> b=s1[1]
>>> b
'world'
>>> p=a[0]
>>> p
'h'
>>> q=b[0]
>>> q
'w'
>>> m=a[1:]
>>> m
'ello'
>>> n=b[1:]
>>> n
'orld'
>>> snew=m+q+p+n
>>> snew
'ellowhorld'
>>> snew=q+m+p+n
>>> snew
'wellohorld'
>>> 
