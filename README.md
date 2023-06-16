# utnamTTE (Text To Expression)

[![PyPi version](https://img.shields.io/badge/PyPi-0.0.2-000000?style=for-the-badge&logo=&logoColor=ffdd54)](https://pypi.org/projects/utnamtte/)
This is a convertor that takes normal mathematical text expressions as String inputs (eg. "2+ln2√π) and return the expression as it would be written in python (2+(math.log(2))*(math.sqrt(math.pi))

**Installation**


    pip install utnamtte

## Ways to import

Method 1

```python
import utnamtte
print(utnamtte.tte("2+ln2"))
```


Method 2

```python
from utnamtte import tte
print(tte("2+ln2"))
```


Method 3

```python
from utnamtte import tte as xy
print(xy("2+ln2"))
```

## Symbols
```python
You can use π or pi (case insensitive) or math.pi
You can use e (case insensitive) or math.e
You can use { or ( and } or )
You can use × or * and ÷ or /

```
## Auto-complete brackets
```python
#utnamtte auto-completes incomplete brackets
a = tte("2*7/(3+1")
print(a)
print(eval(a))

```
```python
Output: 2*7/(3+1)
        3.5
```

## Division
```python
a = tte("7/3π")
print(a)
print(eval(a))
```
```python
Output: 7/(3)*math.pi
        7.330...
```

## Square root

```python
print(tte("2√π11+3"))
```
```python
Output: 2*(math.sqrt(math.pi))*11+3
```
```python
# you can also use sqrt and √ under √ without brackets
print(tte("2√√sqrtπ11+3"))
```
```python
Output: 2*(math.sqrt(math.sqrt(math.sqrt(math.pi))))*11+3
```

## Mod or Absoulute
```python
print(tte("2|3-6|7+3"))
```
```python
Output: 2*(abs(3-6))*7+3
```

## Log
```python
print(tte("4ln11e"))
```
```python
Output: 4*(math.log(11))*math.e
```
```python
# you can also use log and ln of ln without brackets
print(tte("4lnlnlog1331π+3"))
```
```python
Output: 4*(math.log(math.log(math.log(1331))))*math.pi+3
```
```python
# use log to the desired base as follow
print(tte(f"log({number}, {base})"))
```

## Antilog
```python
print(tte(f"antilog({base}, {power})"))
```



Application of this library
**MATEX** is an application to input text mathematical expression and convert into python readable mathematical expression and output the result.
Also it can convert such mathematical expressions into **_Python_** and **_Java_** expressions.

This application was built using **Python** and **kivymd 0.104.2**.

🔗 Download the apk file from [here](https://drive.google.com/drive/folders/13NEsclz1rMhXaleFpfHcjPhmgV5ac7Gf)

▶️  [App tutorial here](https://youtu.be/_vezBiyNTOA)
