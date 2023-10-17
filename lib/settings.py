from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass(frozen=True)
class Settings:
    n_jobs: int
    seed: int

def get_settings(path: str) -> Settings:
    with open(path) as f:
        return Settings.from_json(f.read())