To see the index
http://127.0.0.1:8000/restaurant/

To see the menu
GET /restaurant/menu/

To add new menu item, do a post request with item title, price and inventory (Note: no authentication required)
POST /restaurant/menu/

To see a specific menu item ny pk
GET /restaurant/menu/<int:pk>

To update a specific menu item by pk(Note: no authentication required)
PATCH /restaurant/menu/<int:pk>

To delete a specific menu item by pk (Note: no authentication required)
DELETE /restaurant/menu/<int:pk>

To register a new user, do a POST request with username and password
POST /auth/users/

To obtain a token, do a POST request with valid username and password
POST /api-token-auth/ 
POST /auth/token/login/

To Logout
POST /auth/token/logout/

authentication needed in Booking
To view all reservations
GET /booking/tables/ 

To view single reservation by pk
GET /booking/tables/<int:pk>/

To update a single reservation
PATCH /booking/tables/2/
