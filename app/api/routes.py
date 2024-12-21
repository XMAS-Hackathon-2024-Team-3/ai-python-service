from time import perf_counter
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel, TypeAdapter
from .dto.provider import ProviderDTO
from ..ai.model import predict_priority

router = APIRouter()


class FilteredResponseDTO(BaseModel):
    filteredData: List[ProviderDTO]
    executionTime: float


@router.post("/ai_filtered_data",  response_model=FilteredResponseDTO)
async def ai_filtered_data(providers: list[ProviderDTO]):
    # Фильтрация данных с помощью нейронной сети
    json_data = [provider.model_dump() for provider in providers]

    start_time = perf_counter()
    filtered_providers = predict_priority(json_data)
    end_time = perf_counter()

    execution_time = (end_time - start_time) * 1000

    filtered_providers_list = TypeAdapter(
        List[ProviderDTO]).validate_python(filtered_providers)

    return FilteredResponseDTO(
        filteredData=filtered_providers_list,
        executionTime=execution_time
    )
