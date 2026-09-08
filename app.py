from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# الصفحة الرئيسية (عرض الأدوات)
@app.route('/')
def home():
    return render_template('index.html')

# صفحة تفاصيل الأداة
@app.route('/item/<int:item_id>')
def item_details(item_id):
    return render_template('item-details.html', item_id=item_id)

# صفحة إضافة أداة جديدة
@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        # هنا سيتم استقبال البيانات من الفورم مثل اسم الأداة والتصنيف
        title = request.form.get('title')
        category = request.form.get('category')
        # بعد حفظ البيانات في قاعدة البيانات يتم التوجيه للرئيسية
        return redirect(url_for('home'))
    
    return render_template('add-item.html')

# صفحة الملف الشخصي
@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
