# BACKEND Programming using FAST API

### DAY 7 [22-01-2025]

## Query Paramters and String Validation
- You can limit query (string) given to 50 character using Annotated (typing module) and Query (fastapi)
### In this example below we are validating a bought query to be between 0 to 500 and default value being 50
```python
# Here Product is the Base Pydantic Model carrying Product Arguments
@app.put("/products/{product_id}")
def update_product(product_id:int,product:Product, bought:Annotated[int,Query(ge=0,le=500)]=50):
    # function stuff
# here ge=greater than equal to, le=less than equal to
```
### And in the below we are validating a string query 'q' to have less than 50 characters
```python
@app.put("/items/{item_no}")
def update(item_no:int,q:Annotated[str|None,Query(max_length=50)]=None):
    #function stuff

q:str|None=None 👎
q:Annotated[str|None, Query(....)]=None 🔥
```
### There were two methods to add query validation (New Method Better Practice)
```python

q:Annotated[str|None,Query(max_length=50)]=None # NEW
q:str|None=Query(default=None,max_length=50) # OLD

bought:Annotated[int,Query(ge=0,le=500)]=50 # NEW
bought:int|None=Query(default=50,ge=0,le=500) # OLD

``` 

### Some more query validation that we can use with string instances
```python
Annotated[str|None,Query(min_length=3, max_length=50)]=None  #min_length
Annotated[str|None,Query(pattern="^fixedpattern$")]=None  # using regex with pattern=
# ^ and $ are start and end of the regex expression
pattern="^[A-Z][a-zA-Z]*(-[A-Z][a-zA-Z]*)+$"
# Above pattern means, starting with capital letter followed by 0 or more characters (can be upper or lower) followed by ('-' Hyphen and then again first format like string) '+' means repeat the string inside () so as many hyphen separated city as possible 
```

![alt text](image.png)

### Two ways of saying a Query parameter is required
```python
bought: Annotated[int, Query(ge=20,le=500)]=... # not recommended as no proper swagger documentation
bought: Annotated[int, Query(ge=20,le=500)]
# BOTH CONVEY THE SAME THING
```

### Passing list as Query Parameters
```python
@app.get("item/")
def read_items(q:Annotated[list[str],Query()]=None):
    query_items = {'q':q}
    return query_items
# items/?q=foo&q=bar => ['foo', 'bar']

def read_items(q:list[str]=None) # ❌ will try try to fetch info from request body not url so using Query is necessary

```

- You can use *title*, *description* and *alias* inside Query()
```python
color_variant: Annotated[list[str],Query(default=..., title="Color Variant",description="Give a color variant"), alias="color-variant"],
# alias will make you use <url>/item/?color-variant=red&color-variant=blue
```

