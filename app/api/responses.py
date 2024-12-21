from pydantic import BaseModel
from .dto.provider import ProviderDTO


class FilteredDataResponse(BaseModel):
    filteredData: list[ProviderDTO]
