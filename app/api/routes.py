from typing import List
from fastapi import APIRouter
from pydantic import BaseModel, TypeAdapter
from .dto.provider import ProviderDTO
from ..ai.model import predict_priority

router = APIRouter()


class FilteredDataResponse(BaseModel):
    filteredData: list[ProviderDTO]


@router.post("/ai_filtered_data")
async def ai_filtered_data(providers: list[ProviderDTO]):
    # Фильтрация данных с помощью нейронной сети
    json_data = [provider.model_dump() for provider in providers]

    filtered_providers = predict_priority(json_data)
    filtered_providers_list = TypeAdapter(
        List[ProviderDTO]).validate_python(filtered_providers)

    return {"filteredData": filtered_providers_list}
