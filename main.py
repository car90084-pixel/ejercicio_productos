import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI

from database import db
from vistas import router as vistas_router

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Al arrancar la aplicación se crea el pool de conexiones a PostgreSQL.
    await db.connect(os.environ["DATABASE_URL"])
    yield
    # Al apagar la aplicación, el pool se cierra para liberar las conexiones.
    await db.close()


app = FastAPI(lifespan=lifespan)

app.include_router(vistas_router)