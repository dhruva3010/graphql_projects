from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from ariadne import QueryType, make_executable_schema, gql, MutationType, load_schema_from_path
from graphql import graphql_sync
from database.database import SessionLocal, create_tables, run_migrations
from models.models import TestModel
from resolvers import query, mutation
import uvicorn

app = FastAPI()

schema = make_executable_schema(load_schema_from_path("schema.graphqls"), query, mutation)

@app.post("/graphql")
async def graphql(request: Request):
    data = await request.json()
    print(data)
    query = data.get('query')  # Extract the GraphQL query from the data
    variables = data.get('variables')
    result, _ = graphql_sync(
        schema,
        query,
        context_value=request,
        variable_values=variables,
    )
    status_code = 200 if result else 400

    if not result:
        response_data = {
            'errors': [str(error) for error in result]
        }
        return JSONResponse(response_data, status_code=status_code)
    return JSONResponse(result, status_code=status_code)

if __name__ == "__main__":
    create_tables()
    run_migrations()
    uvicorn.run(app, host="0.0.0.0", port=8000)
