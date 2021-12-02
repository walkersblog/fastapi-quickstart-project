import fastapi
import scripts.example1
import scripts.example2
import scripts.example3
from pydantic import BaseModel

router = fastapi.APIRouter()


# Example 1 - Add two integers
class Example1Values(BaseModel):
    integer1: int = 10
    integer2: int = 10


@router.post('/api/example1/')
def script(values: Example1Values):
    result = scripts.example1.add_values(values.integer1, values.integer2)
    return {
        'result': result
    }


# Example 2 - Concatenate three strings
class Example2Values(BaseModel):
    string1: str = "HELLO"
    string2: str = "WORLD"
    string3: str = "Today"


@router.post('/api/example2/')
def script(values: Example2Values):
    result = scripts.example2.concat_strings(values.string1, values.string2, values.string3)
    return {
        'result': result
    }


# Example 3 - Use memory and sleep
class Example3Values(BaseModel):
    gigabytes: int = 5
    minutes: int = 1


@router.post('/api/example3/')
def script(values: Example3Values):
    result = scripts.example3.consume_memory(values.gigabytes, values.minutes)
    return {
        'result': result
    }
