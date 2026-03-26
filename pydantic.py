from pydantic import BaseModel

class Benchmark(BaseModel):
    status: str
    fps: int

data = {"status": "benchmark executed", "fps": "120"}

b = Benchmark(**data)

print(b.fps)   # 120 (converted to int)