import json
from fastapi import APIRouter
from pydantic import BaseModel
from .dto.provider import ProviderDTO
from .responses import FilteredDataResponse
from ..ai.model import predict_priority

router = APIRouter()


class FilteredDataResponse(BaseModel):
    filteredData: list[ProviderDTO]


@router.post("/ai_filtered_data")
async def ai_filtered_data(providers: list[ProviderDTO]):
    # Фильтрация данных с помощью нейронной сети
    json_data = [provider.model_dump() for provider in providers]

    filtered_providers = json.loads(predict_priority(json_data))

    return {"filteredData": filtered_providers}
