API ENDPOINTS DOCUMENTATION
==============================
Generated on: 2025-04-03 18:31:52

ENDPOINTS:

• GET /
  Summary: Read Root

• GET /getSingleProduct/{item_id}
  Summary: Getone
  Parameters:
  - item_id (path): string (required)

• GET /getAll
  Summary: Getall

• GET /addNew
  Summary: Read Root

• GET /deleteOne
  Summary: Read Root

• GET /startsWith/{letter}
  Summary: Read Root
  Parameters:
  - letter (path): string (required)

• GET /paginate/{start_id}/{end_id}
  Summary: Paginate Products
  Parameters:
  - start_id (path): string (required)
  - end_id (path): string (required)

• GET /convert/{item_id}
  Summary: Read Root
  Parameters:
  - item_id (path): string (required)

• GET /items/{item_id}
  Summary: Read Item
  Parameters:
  - item_id (path): integer (required)
  - q (query):  


API DOCUMENTATION:
==============================
For interactive API documentation, visit:
1. Swagger UI: http://127.0.0.1:8000/docs
2. ReDoc: http://127.0.0.1:8000/redoc

For the OpenAPI schema: http://127.0.0.1:8000/openapi.json