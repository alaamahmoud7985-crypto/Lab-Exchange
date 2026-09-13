# Salafni Shokran (سلفني شكراً)
#### Video Demo: [https://youtu.be/OhoDFXx229s?si=Po6GpCFz8KEA9QC1]
#### Description:

**Salafni Shokran** (Borrow Me, Thank You) is a web application built as the final project for CS50. The project was collaboratively designed and developed by **Nourhan Ahmed** and **Alaa Mahmoud** from Egypt.

### Project Overview
Engineering students often require expensive drawing tools, calculators, and specialized equipment for specific semesters. **Salafni Shokran** provides a centralized, dedicated platform for engineering students to exchange, sell, or donate their tools easily within their academic community.

### Key Features
* **Browse & Filter Items:** Students can view all listed engineering tools on the homepage and filter them by category or listing type (Sale, Exchange, Donation).
* **Search Functionality:** Dynamic search bar allowing users to find specific equipment by title or description keywords.
* **Add New Items:** A dedicated form for users to list tools, specifying title, category, price, condition, and detailed description.
* **Item Details & Contact:** Detailed view for each item displaying description, condition, and an integrated **WhatsApp direct link** to quickly contact the item owner.
* **User Profile & Management:** A profile dashboard showing user details and listed tools, with options to delete listings once sold or exchanged.

### File Architecture
* `app.py`: The core Flask application handling request routing, database queries, and dynamic rendering.
* `project.db`: The SQLite database containing relational tables for `users`, `items`, `requests`, and `reviews`.
* `schema.sql`: Contains the database structure and SQL table creation queries.
* `templates/`: Directory housing HTML views (`index.html`, `add-item.html`, `item-details.html`, `profile.html`).
* `static/`: Contains `style.css` for application styling and layout responsiveness.

### Authors
* **Norhan Ahmed**
* **Alaa Mahmoud**
*
