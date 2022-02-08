Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="onion"
>>> a=s[0]
>>> s=s[1:]
>>> s
'nion'
>>> snew=s.replace(a,'$')
>>> snew=a+snew
>>> snew
'oni$n'
>>> 
