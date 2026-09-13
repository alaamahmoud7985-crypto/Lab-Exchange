from cs50 import SQL
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
db = SQL("sqlite:///project.db")

# 1. الصفحة الرئيسية (تصفح الأدوات المتاحة والبحث)
@app.route('/')
def home():
    q = request.args.get('q', '').strip()
    category = request.args.get('category', '')

    query = "SELECT items.*, users.username FROM items JOIN users ON items.user_id = users.id WHERE items.status = 'available'"
    params = []

    if q:
        query += " AND (items.title LIKE ? OR items.description LIKE ?)"
        params.append(f"%{q}%")
        params.append(f"%{q}%")

    if category and category != "all":
        query += " AND items.category = ?"
        params.append(category)

    query += " ORDER BY items.id DESC"

    items = db.execute(query, *params)
    return render_template('index.html', items=items)


# 2. إضافة أداة جديدة
@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        title = request.form.get('title')
        category = request.form.get('category')
        description = request.form.get('description')

        # استخدام user_id = 1 مؤقتاً لحين إضافة نظام تسجيل الدخول (Sessions)
        user_id = 1

        db.execute(
            "INSERT INTO items (user_id, title, category, description) VALUES (?, ?, ?, ?)",
            user_id, title, category, description
        )

        return redirect(url_for('home'))

    return render_template('add-item.html')


# 3. صفحة الملف الشخصي (عرض أدوات المستخدم وطلباته)
@app.route('/profile')
def profile():
    user_id = 1  # مستخدم افتراضي حالياً

    user = db.execute("SELECT * FROM users WHERE id = ?", user_id)
    my_items = db.execute("SELECT * FROM items WHERE user_id = ? ORDER BY id DESC", user_id)

    # جلب الطلبات المقدمة على أدوات هذا المستخدم
    my_requests = db.execute("""
        SELECT requests.id AS request_id, items.title, users.username AS requester_name, requests.status
        FROM requests
        JOIN items ON requests.item_id = items.id
        JOIN users ON requests.requester_id = users.id
        WHERE items.user_id = ?
    """, user_id)

    return render_template('profile.html', user=user[0] if user else None, items=my_items, requests=my_requests)


# 4. تفاصيل أداة + إمكانية طلبها
@app.route('/item/<int:item_id>')
def item_details(item_id):
    items = db.execute("""
        SELECT items.*, users.username, users.phone, users.department
        FROM items
        JOIN users ON items.user_id = users.id
        WHERE items.id = ?
    """, item_id)

    if items:
        return render_template('item-details.html', item=items[0])
    return redirect(url_for('home'))


# 5. إرسال طلب استعارة/تبادل لأداة
@app.route('/request-item/<int:item_id>', methods=['POST'])
def request_item(item_id):
    requester_id = 1  # المستخدم الحالي

    db.execute(
        "INSERT INTO requests (item_id, requester_id) VALUES (?, ?)",
        item_id, requester_id
    )
    return redirect(url_for('profile'))


# 6. حذف أداة
@app.route('/delete-item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    db.execute("DELETE FROM items WHERE id = ?", item_id)
    return redirect(url_for('profile'))


if __name__ == '__main__':
    app.run(debug=True)
