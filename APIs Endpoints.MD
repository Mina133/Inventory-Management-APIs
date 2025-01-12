# Inventory Management API Endpoints

## Inventory Item Management Endpoints

### 1. List/Create Inventory Items
- **Path**: `/api/item/`
- **Method**: GET/POST
- **Description**: Retrieve or create inventory items.
- **Request Example (POST)**:
  ```json
  {
      "name": "Laptop",
      "description": "Gaming Laptop",
      "quantity": 10,
      "price": 1500.00,
      "category": 1,
      "supplier": 2,
      "store": 3,
      "low_stock_threshold": 5
  }
  ```
- **Response Example**:
  ```json
  {
      "id": 1,
      "name": "Laptop",
      "description": "Gaming Laptop",
      "quantity": 10,
      "price": 1500.00,
      "category": 1,
      "supplier": 2,
      "store": 3,
      "low_stock_threshold": 5,
      "date_added": "2025-01-08T12:34:56Z",
      "last_updated": "2025-01-08T12:34:56Z"
  }
  ```

## 2. Retrieve/Update/Delete Inventory Item
- **Path**: `/api/item/<id>/`
- **Method**: GET/PUT/DELETE
- **Description**: Retrieve, update, or delete a specific inventory item.
- **Request Example (PUT)**:
  ```json
  {
      "quantity": 15
  }
  ```
- **Response Example**:
  ```json
  {
      "id": 1,
      "name": "Laptop",
      "quantity": 15
  }
  ```

---

## Category Management Endpoints

### 1. List/Create Categories
- **Path**: `/api/category/`
- **Method**: GET/POST
- **Description**: Retrieve or create categories.
- **Request Example (POST)**:
  ```json
  {
      "name": "Electronics"
  }
  ```
- **Response Example**:
  ```json
  {
      "id": 1,
      "name": "Electronics"
  }
  ```

### 2. Retrieve/Update/Delete Category
- **Path**: `/api/category/<id>/`
- **Method**: GET/PUT/DELETE
- **Description**: Manage a specific category.

---

## Inventory Levels Endpoint

### 1. View Inventory Levels with Filters
- **Path**: `/api/item/levels/`
- **Method**: GET
- **Description**: View inventory levels with optional filters.
- **Query Parameters**:
  - `category` (string, optional)
  - `price_min` (float, optional)
  - `price_max` (float, optional)
  - `low_stock` (boolean, optional)
- **Response Example**:
  ```json
  [
      {
          "name": "Laptop",
          "quantity": 10,
          "price": 1500.00,
          "category__name": "Electronics"
      },
      {
          "name": "Phone",
          "quantity": 50,
          "price": 800.00,
          "category__name": "Electronics"
      }
  ]
  ```

---

## stores 

### 1. View Stores
- **Path**: `/api/store/`
- **Method**: GET
- **Description**: list the stores 
- **Response Example**:
  ```json
   [
      {
          "id": 1,
          "Name": "Store 1",
          "Location": "Luxor",
          "staff_members": [
              1
          ]
      }
  ]
  ```

---

## Inventory Report Endpoint

### 1. Generate Inventory Report
- **Path**: `/api/item/report/`
- **Method**: GET
- **Description**: Generate a report of total inventory value and low stock items.
- **Response Example**:
  ```json
  {
      "total_value": 25000.00,
      "low_stock_items": 3
  }
  ```


---


## User Management Endpoints

### 1. User CRUD
- **Path**: `/api/users/`
- **Method**: GET/POST/PUT/DELETE
- **Description**: Manage user accounts.
- **Request Examples**:
  - Create User (POST):
    ```json
    {
        "username": "user1",
        "email": "user1@example.com",
        "password": "securepassword"
    }
    ```
  - Update User (PUT):
    ```json
    {
        "username": "updated_user"
    }
    ```
- **Response Example**:
  ```json
  {
      "id": 1,
      "username": "updated_user",
      "email": "user1@example.com"
  }
  ```

---



