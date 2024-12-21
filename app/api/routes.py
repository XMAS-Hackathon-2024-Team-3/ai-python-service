from fastapi import APIRouter
from pydantic import BaseModel
from .dto.provider import ProviderDTO
from .responses import FilteredDataResponse

router = APIRouter()


class FilteredDataResponse(BaseModel):
    filteredData: list[ProviderDTO]


def filter_with_neural_network(providers: list[ProviderDTO]) -> list[ProviderDTO]:
    return providers


@router.post("/ai_filtered_data", response_model=FilteredDataResponse)
async def ai_filtered_data(providers: list[ProviderDTO]):
    # Фильтрация данных с помощью нейронной сети
    filtered_data = filter_with_neural_network(providers)

    return {"filteredData": filtered_data}
