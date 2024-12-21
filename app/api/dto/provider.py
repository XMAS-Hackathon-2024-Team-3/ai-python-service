from pydantic import BaseModel


class ProviderDTO(BaseModel):
    id: int
    conversion: float
    avg_time: float
    commission: float
    limit_min: int
    limit_max: int

    class Config:
        frozen = True
