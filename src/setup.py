from db import engine
import models

models.Base.metadata.drop_all(engine)
models.Base.metadata.create_all(engine)
