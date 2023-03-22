from pydantic import BaseModel

class info_(BaseModel):
    namee: str
    villege: str
    education: str
    course: str

if __name__ == "__main__":
    data = {
        "namee": "yogesh",
        "villege":"chakan",
        "education": "mechanical",
        "course": "python"
    }
    obj = info_(**data)   # serialization / data validation
    breakpoint()
