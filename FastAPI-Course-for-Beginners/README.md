# FastAPI Course for Beginners

## Installation and Creating your First API

**Terminal PowerShell:**

- Install FastAPI > `python -m pip install fastapi`
- Install webserver > `pip install uvicorn`
- Make `myapi.py` file

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"name": "First Data"}
```

> Endpoints:
> 
> GET: Get an information
> POST: Create something new
> PUT: Update
> Delete: Delete something

- Run app > `python myapi.py`
- Run our FastAPI project for our server > `uvicorn myapi:app --reload`
- Basic documentation for all the API's you have on your app > `http://127.0.0.1:8000/docs`

![](https://hackmd.io/_uploads/ryRAgTGs2.png)

- We don't need to use `Postman` or any external service to test API, you can just come here.

![](https://hackmd.io/_uploads/H18I-TMsh.png)
![](https://hackmd.io/_uploads/Bk1sbTGi3.png)
![](https://hackmd.io/_uploads/HyYaWpzo2.png)
![](https://hackmd.io/_uploads/ryW1zTzsh.png)

## Path Parameters

Name parameter is used to return a data relating to an input in the part or in the endpoint. So we can do it that using either a part or a query. So we have two input parameters, which are path parameter and a query parameter.

```python
from fastapi import FastAPI

students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}

app = FastAPI()

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]
```

> Refresh the website `http://127.0.0.1:8000/docs` you don't have to run again the `uvicorn`

![](https://hackmd.io/_uploads/rkfN2azs3.png)
![](https://hackmd.io/_uploads/rJBwhTGi3.png)

- Run `http://127.0.0.1:8000/get-student/1`

![](https://hackmd.io/_uploads/HyJ32pMjh.png)

```python
from fastapi import FastAPI, Path


students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}

app = FastAPI()

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description='The ID of the student you want to view')):
    return students[student_id]
```

> Path: What we really want to collect.

![](https://hackmd.io/_uploads/SyG-eAfin.png)

:red_circle::red_circle: **IMPORTANT** :red_circle::red_circle:
> gt: greater than
> lt: less than
> ge: greater than or equal to
> le: less than or equal to

```python
from fastapi import FastAPI, Path

students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}

app = FastAPI()

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description='The ID of the student you want to view', gt=0, lt=3)):
    return students[student_id]
```

![](https://hackmd.io/_uploads/ByfEz0Gin.png)
![](https://hackmd.io/_uploads/Hy3LGAGin.png)

## Query Parameters

The query is used to pass a value into a URL that is quite similar to the path parameter.

Example: `google.com/results?search=Python`

```python
from fastapi import FastAPI, Path
from typing import Optional

students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}

app = FastAPI()

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description='The ID of the student you want to view', gt=0, lt=3)):
    return students[student_id]

@app.get("/get-by-name")
def get_student(name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"Data": "Not found"}
```

![](https://hackmd.io/_uploads/H1WXoWVs3.png)
![](https://hackmd.io/_uploads/HJiSiZ4j3.png)

- If you want not required:

![](https://hackmd.io/_uploads/B1hanb4ih.png)

- You have to do this:

![](https://hackmd.io/_uploads/H12C3bVi2.png)

- The best practice is to use the `Optional[str] = None`

![](https://hackmd.io/_uploads/rJsZ1G4ih.png)

- You can't do this because this is a required value and you have an Optional value:

![](https://hackmd.io/_uploads/HJtggG4j3.png)

- Put an `*` and we can now write it if we have a default parameter or optional or whatever required is goint to work since we have this now.

![](https://hackmd.io/_uploads/B19olGNo3.png)


### Difference between Path and Query parameter:

Path parameters and query parameters are both used to pass data to an API endpoint, but they differ in how they are included in the URL and how they are used in the backend.

1. Path Parameters:
   - Syntax: Path parameters are defined within the URL path itself, denoted by curly braces `{}`.
   - Example: `/users/{user_id}`
   - Usage: Path parameters are used to identify and retrieve a specific resource or entity. They are commonly used in RESTful APIs to represent unique identifiers for resources. For example, in the above URL, `{user_id}` is a path parameter that can be used to retrieve information about a specific user.
   - How to define in FastAPI: In FastAPI, you can define path parameters using the `Path` function. Example: `def get_user(user_id: int = Path(...))`.

2. Query Parameters:
   - Syntax: Query parameters are added to the end of the URL after a question mark `?` and are in the format `key=value`. Multiple query parameters are separated by ampersands `&`.
   - Example: `/users?name=john&age=25`
   - Usage: Query parameters are used to filter, sort, or provide additional data to an API endpoint. They are not part of the resource's path but are used to modify the behavior of the request. For example, in the above URL, `name=john` and `age=25` are query parameters that can be used to filter users with the name "john" and age 25.
   - How to define in FastAPI: In FastAPI, you can define query parameters by directly specifying them in the function parameters. Example: `def get_users(name: str = None, age: int = None)`.

In summary, path parameters are used to identify a specific resource or entity within the URL path, while query parameters are used to modify the behavior or filter the results of an API request. Both path and query parameters are useful for passing data to API endpoints, and the choice between them depends on the use case and the design of the API.

## Combining Path and Query Parameters

```python
from fastapi import FastAPI, Path
from typing import Optional

students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}

app = FastAPI()

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description='The ID of the student you want to view', gt=0, lt=3)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"Data": "Not found"}
```

![](https://hackmd.io/_uploads/Hk_6wfEi2.png)
![](https://hackmd.io/_uploads/SJKmuG4j3.png)

## Request Body and The Post Method

- Create an Student, you should later save it into a database because if you refresh the page you lose it.

```python
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

students = {1: {"name": "john", "age": 17, "year": "year 12"}}


class Student(BaseModel):
    name: str
    age: int
    year: str


app = FastAPI()


# GET Method
@app.get("/")
def index():
    return {"name": "First Data"}


# Path Parameter
@app.get("/get-student/{student_id}")
def get_student(
    student_id: int = Path(
        ..., description="The ID of the student you want to view", gt=0, lt=3
    )
):
    return students[student_id]


# Query Parameter
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


# POST Method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student

    return students[student_id]
```

![](https://hackmd.io/_uploads/BJxxsGNs3.png)
![](https://hackmd.io/_uploads/S12WsfVoh.png)

## Put Method

```python
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

students = {1: {"name": "john", "age": 17, "year": "year 12"}}


class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

app = FastAPI()


# GET Method
@app.get("/")
def index():
    return {"name": "First Data"}


# Path Parameter
@app.get("/get-student/{student_id}")
def get_student(
    student_id: int = Path(
        ..., description="The ID of the student you want to view", gt=0, lt=3
    )
):
    return students[student_id]


# Query Parameter
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


# POST Method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student

    return students[student_id]

# PUT Method
@app.put("/update-student/{student-id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age
    
    if student.year != None:
        students[student_id].year = student.year
        
    
    return students[students_id]
```

- First make a POST

![](https://hackmd.io/_uploads/BJLm-SNj2.png)

- Then a PUT

![](https://hackmd.io/_uploads/rJ-SbSVih.png)

## DELETE Method

```python
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

students = {1: {"name": "john", "age": 17, "year": "year 12"}}


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


app = FastAPI()


# GET Method
@app.get("/")
def index():
    return {"name": "First Data"}


# Path Parameter
@app.get("/get-student/{student_id}")
def get_student(
    student_id: int = Path(
        ..., description="The ID of the student you want to view", gt=0, lt=3
    )
):
    return students[student_id]


# Query Parameter
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


# POST Method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student

    return students[student_id]


# PUT Method
@app.put("/update-student/{student-id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]


# DELETE Method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    del students[student_id]
    
    return {"Message": "Student deleted successfully"}
```

- First make a POST
- Then DELETE

![](https://hackmd.io/_uploads/Hk3pfr4j2.png)