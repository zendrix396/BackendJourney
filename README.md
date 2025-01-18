# BACKEND Programming using FAST API

### DAY 3 [18-01-2025]

### Query Parameters
- Parameters that comes after "?" in the url
- can be of 2 types: required and optional (with default or null value)
#### Required parameter declaration
```python
@app.get("/item/{item_no}/")
def func(item_no:str,required_field:int):
    return {"item":item_no,"required*":required_field}
```
#### Optional parameters declaration
```python
@app.get("/item/{item_no}/")
def func(item_no:str,optional_1:int=10,optional_2:bool=false,optional_3:str|None=None): #default value being 10,false and Null respectively, Avoid using just str=None instead str|None=None "Industry Practice"
    return {"item":item_no,"optional 1":optional_1,"optional 2":optional_2,"optional_3":optional_3}
```
