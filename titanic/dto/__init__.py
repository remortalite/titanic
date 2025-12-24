from sqlalchemy import create_engine

from titanic.dto.models import Base


engine = create_engine('sqlite:///sqlite.db')
Base.metadata.create_all(engine)
