from fastapi import FastAPI

from . import database, models, schemas

models.Base.metadate_create_all(bind=database.engine)
app = FastAPI(name="بذل‌الخاطر")
