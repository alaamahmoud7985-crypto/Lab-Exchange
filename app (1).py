from cs50 import SQL
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
db = SQL("sqlite:///project.db")

# 1. الصفحة الرئيسية (البحث والتصفية)
@app.route('/')
def home():
    q = request.args.get('q', '').strip()
    category = request.args.get('category', '')
    listing_type = request.args.get('listing_type', '')

    query = "SELECT * FROM items WHERE 1=1"
    params = []

    if q:
        query += " AND (title LIKE ? OR description LIKE ?)"
        params.append(f"%{q}%")
        params.append(f"%{q}%")

    if category and category != "all":
        query += " AND category = ?"
        params.append(category)

    if listing_type and listing_type != "all":
        query += " AND listing_type = ?"
        params.append(listing_type)

    query += " ORDER BY id DESC"

    items = db.execute(query, *params)
    return render_template('index.html', items=items)


# 2. إضافة أداة
@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        title = request.form.get('title')
        category = request.form.get('category')
        listing_type = request.form.get('listing_type')
        price = request.form.get('price')
        description = request.form.get('description')

        if not price or not price.strip():
            price = "مجاناً"

        db.execute(
            "INSERT INTO items (title, category, listing_type, price, description) VALUES (?, ?, ?, ?, ?)",
            title, category, listing_type, price, description
        )

        return redirect(url_for('home'))

    return render_template('add-item.html')


# 3. صفحة الحساب الشخصي
@app.route('/profile')
def profile():
    user_name = request.args.get('user_name', 'آلاء')
    user_email = request.args.get('user_email', 'student@eng.edu.eg')
    user_dept = request.args.get('user_dept', 'هندسة حاسبات / كهرباء')

    items = db.execute("SELECT * FROM items ORDER BY id DESC")
    return render_template('profile.html', items=items, user_name=user_name, user_email=user_email, user_dept=user_dept)


# 4. دالة الحذف (تنفذ أمر الحذف وتنعش الصفحة)
@app.route('/delete-item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    db.execute("DELETE FROM items WHERE id = ?", item_id)
    return redirect(url_for('profile'))


# 5. تفاصيل الأداة
@app.route('/item/<int:item_id>')
def item_details(item_id):
    items = db.execute("SELECT * FROM items WHERE id = ?", item_id)
    if items:
        return render_template('item-details.html', item=items[0])
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
