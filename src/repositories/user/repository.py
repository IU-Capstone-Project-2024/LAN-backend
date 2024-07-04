__all__ = ["user_repository"]


from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories import profile_repository
from src.schemas.userinfo import UpdateUserInfo, UserInfo
from src.storage.sql.models import User
from src.storage.sql.storage import AbstractSQLAlchemyStorage
from src.exceptions import NoUserException, NoProfileException


class SqlUserRepository:
    storage: AbstractSQLAlchemyStorage

    def update_storage(self, storage: AbstractSQLAlchemyStorage) -> Self:
        self.storage = storage
        return self

    def _create_session(self) -> AsyncSession:
        return self.storage.create_session()

    async def get(self, id: int) -> UserInfo | None:
        async with self._create_session() as session:
            # Get user
            user = await session.get(User, id)
            if not user:
                raise NoUserException()
            # Get profile
            profile = await profile_repository.get(user.profile_id)
            if not profile:
                raise NoProfileException()
            # Merge everything into a UserInfo object
            return UserInfo(
                first_name=user.first_name,
                last_name=user.last_name,
                username=user.username,
                photo_url=user.photo_url,
                about=profile.about,
                date_of_birth=profile.date_of_birth,
                sex=profile.sex,
                religion=profile.religion,
                hobby=profile.hobby,
                soc_media=profile.soc_media,
                metrics=profile.metrics,
            )

    async def update(self, id: int, update: UpdateUserInfo) -> UserInfo | None:
        async with self._create_session() as session:

            # Get user
            user = await session.get(User, id)
            if not user:
                raise NoUserException()

            # Get profile
            profile = await profile_repository.get(user.profile_id)
            if not profile:
                raise NoProfileException()

            # Update
            user.first_name = update.first_name or user.first_name
            user.last_name = update.last_name or user.last_name
            user.username = update.username or user.username
            user.photo_url = update.photo_url or user.photo_url

            profile.date_of_birth = update.date_of_birth or profile.date_of_birth
            profile.sex = update.sex or profile.sex
            profile.religion = update.religion or profile.religion
            profile.hobby = update.hobby or profile.hobby
            profile.soc_media = update.soc_media or profile.soc_media
            profile.metrics = update.metrics or profile.metrics

            session.add(user)
            await profile_repository.update(id, profile, session)

            await session.commit()

            return UserInfo(
                first_name=user.first_name,
                last_name=user.last_name,
                username=user.username,
                photo_url=user.photo_url,
                about=profile.about,
                date_of_birth=profile.date_of_birth,
                sex=profile.sex,
                religion=profile.religion,
                hobby=profile.hobby,
                soc_media=profile.soc_media,
                metrics=profile.metrics,
            )


user_repository: SqlUserRepository = SqlUserRepository()
