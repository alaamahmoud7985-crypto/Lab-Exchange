# Lab-Exchange
# Salefny Shokran (سلفني شكراً)
#### Video Demo: <URL HERE>
#### Description:

**Salefny Shokran** (Arabic for *"Lend Me, Thank You"*) is a web-based community platform designed specifically for engineering students to share, borrow, buy, and exchange study tools and lab equipment (such as T-squares, multimeters, drawing sets, and calculators).

The application is built to solve a very common problem among engineering students: purchasing expensive tools that are only needed for a single semester or laboratory experiment.

### Features
- **Dynamic Homepage & Search:** Users can browse all available engineering items or filter them dynamically using keywords, engineering departments (e.g., General Engineering, Architecture, Civil, Electrical/Computers, Mechanical), or listing types (Free Borrowing, Paid Borrowing, Selling, Exchanging).
- **Add New Item:** A dedicated form allowing students to submit new items to the marketplace with details including title, category, listing type, price, and description.
- **Dynamic Profile Management:** A simple profile page where students can manage their personal identity (Name, Department, University Email) without needing a complex multi-user database setup.
- **Item Deletion:** Students can remove their own items directly from their profile page with real-time database updating.
- **Item Details:** A specialized view to display complete information about a specific tool.

---

### Tech Stack & Architecture
- **Backend:** Python 3, Flask framework.
- **Database:** SQLite (`project.db`) using CS50's SQL module.
- **Frontend:** HTML5, CSS3, JavaScript, Jinja2 templating, Bootstrap 5 (RTL configuration for Arabic support).

---

### File Structure & Functionality

#### `app.py`
The primary Python script driving the Flask backend. It contains the application route handlers and database queries:
- `/`: Renders `index.html` with dynamic search and filtering queries using SQL `LIKE` and parameterized conditions.
- `/add-item`: Processes `POST` requests to insert new engineering equipment into the `items` table in SQLite.
- `/profile`: Handles displaying user information and fetching the current student's listed tools.
- `/delete-item/<int:item_id>`: Handles deletion requests to execute `DELETE` queries in the database and redirect back to the profile.
- `/item/<int:item_id>`: Fetches a single item's detailed information by its primary key (`id`).

#### `project.db`
The SQLite database containing the core table `items`, which stores:
- `id` (INTEGER, Primary Key)
- `title` (TEXT)
- `category` (TEXT)
- `listing_type` (TEXT)
- `price` (TEXT)
- `description` (TEXT)

#### `templates/`
- **`index.html`**: The main landing page featuring the search bar, category filters, and a dynamic Jinja2 grid loop rendering all items stored in the database.
- **`add-item.html`**: Form interface for inputting tool details.
- **`profile.html`**: User profile displaying student details, live-update fields, and an item management list with interactive delete confirmation prompts.
- **`item-details.html`**: View template displaying extended information for an individual item.

#### `static/`
- **`style.css`**: Custom styling rules extending Bootstrap 5 RTL to achieve an engineering-themed marketplace interface.

---

### How to Run the Application
1. Clone the repository and navigate to the project directory:
   ```bash
   cd project
   
