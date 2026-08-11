"""
FastAPI REST API Starter Code

This starter code provides a foundation for building a REST API with FastAPI.
Complete the tasks in README.md to build and extend this API.
"""

from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI application
app = FastAPI()

# TODO: Define your Item model here using Pydantic
# Example structure:
# class Item(BaseModel):
#     id: int
#     name: str
#     price: float


# TODO: Task 1 - Create a welcome endpoint at GET /
@app.get("/")
def read_root():
    """
    Welcome endpoint that returns a greeting message.
    """
    # TODO: Return a welcome message as JSON
    pass


# TODO: Task 1 - Create an endpoint that accepts a path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Get an item by ID.
    """
    # TODO: Return the item_id in a JSON response
    pass


# TODO: Task 2 & 3 - Implement CRUD operations
# Create endpoints for:
# - GET /items (list all items with pagination)
# - GET /items/{item_id} (get a single item)
# - POST /items (create a new item)
# - PUT /items/{item_id} (update an item)
# - DELETE /items/{item_id} (delete an item)
# - GET /items/search?q=query (search items by name)


if __name__ == "__main__":
    import uvicorn
    # Run the server with: python app.py
    # Or directly with: uvicorn app:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
