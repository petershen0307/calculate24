calculate24
===========

輸入4個數字，會找出運算結果為24的所有運算式

輸入格式
--------

支援雙位數
```python
list(map(postfix_to_infix, calculate24([10, 2, 3, 4]))
```

不支援雙位數
```python
list(map(postfix_to_infix, calculate24('1234'))
```