from dataclasses import dataclass

@dataclass
class Config:
    device: str = 'cpu'
    runtime: str = 'gloo'
