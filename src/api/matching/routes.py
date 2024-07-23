__all__ = ["router"]

from fastapi import APIRouter, Depends

from src.middleware.auth_guard import get_id
from src import repositories as reps
from src.utils import messages
import src.exceptions as exceptions
import src.schemas as schemas

router = APIRouter(
    prefix="/match",
    tags=["Matching"],
)


@router.get(
    "",
    responses={
        200: {"model": list[schemas.ProfileDTO]},
        401: {"model": messages.Unauthorized},
        404: {"model": messages.NotFound},
    },
)
async def get_match(id: str = Depends(get_id)):
    profiles = await reps.matching_repository.get(id)
    if len(profiles) <= 0:
        raise exceptions.EntityNotFoundException("matches")
    return profiles


@router.put(
    "/{secondary_id}",
    responses={
        200: {"model": schemas.MatchDTO},
        401: {"model": messages.Message},
    },
)
async def get_match(secondary_id: int, primary_id: int = Depends(get_id)):
    return await reps.matching_repository.match(primary_id, secondary_id)
