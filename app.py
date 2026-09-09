from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 1. الصفحة الرئيسية (عرض الأدوات)
@app.route('/')
def home():
    return render_template('index.html')

# 2. صفحة إضافة أداة جديدة
@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        # استقبال البيانات من الفورم
        title = request.form.get('title')
        category = request.form.get('category')
        listing_type = request.form.get('listing_type')
        price = request.form.get('price')
        description = request.form.get('description')

        # بعد حفظ البيانات يتم التوجيه للرئيسية
        return redirect(url_for('home'))

    return render_template('add-item.html')

# 3. صفحة الملف الشخصي (حسابي)
@app.route('/profile')
def profile():
    return render_template('profile.html')

# 4. صفحة تفاصيل أداة محددة
@app.route('/item/<int:item_id>')
def item_details(item_id):
    return render_template('item-details.html', item_id=item_id)

if __name__ == '__main__':
    app.run(debug=True)
