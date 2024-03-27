# Path-&-Query-Parameters

## Path Parameters:

## What are path parameters in FastAPI?

Path parameters are bits of information included in the URL address. They let you grab changing values from the URL and use them in your code to adjust how your app responds to requests.

## How are path parameters defined in FastAPI route declarations?

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/users/{user_id}")
async def post_user(user_id: str):
    return {"user_id": user_id}
```

## Can path parameters have default values? If yes, how can they be set?

Path parameters cannot have default values. If you want to make a path parameter optional, you can use query parameters instead.

## Provide an example of a FastAPI route with path parameters.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return {"product_id": product_id}
```

# Query Parameters:

## What are query parameters in FastAPI?

Query parameters are additional function parameters that are not included in the path parameters.

## How are query parameters defined in FastAPI route declarations?

```python
from fastapi import FastAPI

app = FastAPI()

items_arr = [{"item_name": "Jail"}, {"item_name": "Link"}, {"item_name": "Gen"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return items_arr[skip : skip + limit]
```

## What is the difference between path parameters and query parameters?

The query is the set of key-value pairs that go after the ? in a URL, separated & characters.
Path parameters are used to define a specific endpoint.

## Can query parameters have default values? If yes, how can they be set?

Query parameters in FastAPI can have default values. To set default values for query parameters, you can specify them directly in the route declaration using default parameter values.

## Provide an example of a FastAPI route with query parameters.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{items_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

# Combining Path and Query Parameters:

Can a FastAPI route have both path parameters and query parameters? If yes, provide an example.

Yes, a FastAPI route can have both path parameters and query parameters.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, query: str | None = None):
    if query:
        return {"item_id": item_id, "q": query}
    return {"item_id": item_id}
```

## What is the order of precedence if a parameter is defined both in the path and as a query parameter?

If a parameter is defined both in the path and as a query parameter, the path parameter takes precedence over the query parameter. In other words, the value provided in the URL path will be used, and any value provided for the same parameter in the query string will be ignored.

# Data Types and Validations:

## How does FastAPI handle data types and validation for path and query parameters?

FastAPI handles data types and validation for path and query parameters by automatically converting incoming request data to the specified data types and validating it against the provided type annotations. If the incoming data doesn't match the specified data type, FastAPI will respond with an error message.

## What are some common data types that can be used for path and query parameters?

Float: float
Boolean: bool
Integer: int
String: str
List: list

## How can you enforce validation rules on path and query parameters in FastAPI?

Data Type Annotations: Annotate parameters with the appropriate data type. FastAPI will automatically convert and validate the incoming data against these annotations.
Default Values: You can provide default values for parameters, and FastAPI will use them if no value is provided in the request.

# Usage and Benefits:

In what scenarios would you use path parameters over query parameters, and vice versa?

### Path Parameter Scenario:

Endpoint: Path parameters serve as identifiers for specific endpoints within the API. Positioned within the URL path, they offer a transparent indication of the resource targeted for access.
SEO and Readability: Path parameters contribute to search engine optimization (SEO) and improve URL readability. Descriptive paths make URLs more user-friendly and easier to understand.

### Query Parameter Scenario:

Optional Parameters: Query parameters are ideal for passing optional information to API endpoints. They allow clients to specify additional details without cluttering the URL path.
Filtering and Sorting: Query parameters are commonly used for filtering, sorting, or modifying response data. They enable clients to customize the data they receive based on specific criteria.

## What are the benefits of using path and query parameters in API design?

Flexibility: Path and query parameters offer flexibility for clients to tailor API requests and responses to their needs, supporting diverse use cases.
Readability: Clear and structured path and query parameters enhance the readability and usability of APIs, making them more accessible to developers and users alike.

## Can you provide examples of real-world use cases where path and query parameters would be employed effectively?

### Path Parameters:

Accessing a user profile: /products/{product_id}

### Query Parameters:

Filtering products by category: /products?category=jewelry

# Error Handling:

# #How does FastAPI handle errors related to missing or invalid path/query parameters?

FastAPI automatically manages errors concerning absent or invalid path and query parameters, responding with suitable HTTP error codes.

For missing parameters:

- If a path parameter is not found, FastAPI responds with a 404 Not Found error.
- If a query parameter is not present, FastAPI responds with a 422 Unprocessable Entity error.

Regarding invalid parameters:

- If a path or query parameter doesn't meet validation criteria (e.g., incorrect data type), FastAPI returns a 422 Unprocessable Entity error.

## Can you customize error responses for cases where required parameters are missing or validation fails?

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()


async def path_param_exception_handler(request, exception):
    try:
        if exception.status_code == 404:
            return JSONResponse(content={"error": "Resource not found"}, status_code=404)
    except AttributeError:
        pass
    return exception
```
