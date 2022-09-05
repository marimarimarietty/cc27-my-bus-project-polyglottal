release: python api.migrate_db migrate
web:  uvicorn api.main:app --reload --host=0.0.0.0 --port=${PORT:-5000}
