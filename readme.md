# E-Commerce Website Backend

### This is the backend for an eCommerce website built with Django Rest Framework (DRF). It provides APIs for managing accounts, products, categories, reviews, payments, orders, carts, and notifications.

## Features

## User Authentication:

### User registration, login, and profile management.

### Role-based access control (admin, customer).

## Product Management:

### Add, update, delete, and view products.

### Categorize products using categories.

### Add reviews and ratings.

## Cart and Order Management:

### Add items to the cart, update quantities, and remove items.

#### Place orders and track their statuses.

## Payment Integration:

### Process payments using external payment gateways.

### Generate payment receipts.

## Notifications:

### Real-time notifications for order updates.

### Email notifications for account-related activities.

## Admin Dashboard:

### Manage users, products, categories, and orders.

## Tech Stack

### Backend: Django, Django Rest Framework (DRF)

### Database: Sqlite3 Database

### Authentication: JWT (JSON Web Tokens)

## API Documentation: Swagger (drf-yasg)

## Getting Started

### Follow these steps to set up and run the project locally:

1. Clone the Repository
   bash
   Copy code
   git clone https://github.com/<your-github-username>/<repo-name>.git
   cd <repo-name>
2. Create a Virtual Environment
   bash
   Copy code
   python3 -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
3. Install Dependencies
   bash
   Copy code
   pip install -r requirements.txt
4. Set Up Environment Variables
   Create a .env file in the project root and add the following variables:

plaintext
Copy code
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
JWT_SECRET=your_jwt_secret
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password 5. Apply Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate 6. Create a Superuser
bash
Copy code
python manage.py createsuperuser 7. Run the Development Server
bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000 to access the API.

API Endpoints
Authentication
POST /api/auth/register/: Register a new user.
POST /api/auth/login/: Authenticate a user and retrieve a token.
Products
GET /api/products/: List all products.
POST /api/products/: Add a new product (admin only).
GET /api/products/<id>/: Retrieve a product by ID.
PUT /api/products/<id>/: Update a product (admin only).
DELETE /api/products/<id>/: Delete a product (admin only).
Categories
GET /api/categories/: List all categories.
POST /api/categories/: Add a new category (admin only).
Cart
GET /api/cart/: View the cart.
POST /api/cart/add/: Add an item to the cart.
PUT /api/cart/update/<id>/: Update the quantity of an item.
DELETE /api/cart/remove/<id>/: Remove an item from the cart.
Orders
GET /api/orders/: List all orders (admin) or user-specific orders.
POST /api/orders/: Place a new order.
GET /api/orders/<id>/: View order details.
Payments
POST /api/payments/: Process a payment.
Notifications
GET /api/notifications/: View all notifications.
Testing
Run the test suite to ensure everything is working correctly:

bash
Copy code
python manage.py test

<!-- Deployment
Using Docker
Build and run the containers: -->

<!-- bash
Copy code
docker-compose up --build
The application will be available at http://localhost:8000. -->

## Environment Variables

### Ensure all sensitive data is stored in environment variables for production.

## Contact

### For questions or support, reach out at:

### Email: oguanyiacynthia@gmail.com

### GitHub: Cyndie040
