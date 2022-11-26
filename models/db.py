from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

import config

engine = create_async_engine(
    url=config.DB_URL_ASYNC,
    echo=config.DB_ECHO
)

Session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncSession:
    async with Session.begin() as session:
        yield session
        await session.close()

