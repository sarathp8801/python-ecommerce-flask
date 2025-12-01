from flask import Blueprint, render_template, request, redirect, session
from .models import Product, User, Order

main = Blueprint('main', __name__)


# --------- HOME ----------
@main.route('/')
def index():
    products = Product.get_all()
    return render_template("index.html", products=products)


# --------- LOGIN ----------
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.login(
            request.form['email'],
            request.form['password']
        )

        if user:
            session['user'] = user['id']
            session['user_name'] = user['name']

            if 'cart' not in session:
                session['cart'] = []

            return redirect('/')

    return render_template('login.html')


# --------- LOGOUT ----------
@main.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('user_name', None)
    session.pop('cart', None)
    return redirect('/')


# --------- REGISTER ----------
@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        User.register(
            request.form['name'],
            request.form['email'],
            request.form['password']
        )
        return redirect('/login')

    return render_template('register.html')


# --------- ADD TO CART ----------
@main.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form['product_id']

    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart

    return redirect('/cart')


# --------- REMOVE FROM CART ----------
@main.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    index = int(request.form['index'])

    cart = session.get('cart', [])

    if 0 <= index < len(cart):
        cart.pop(index)

    session['cart'] = cart

    return redirect('/cart')


# --------- VIEW CART ----------
@main.route('/cart')
def cart():
    cart_ids = session.get('cart', [])

    items = []
    total = 0.0

    all_products = Product.get_all()

    for item_id in cart_ids:
        for product in all_products:
            if str(product['id']) == str(item_id):
                items.append(product)
                total += float(product['price'])

    return render_template("cart.html", items=items, total=total)


# --------- CHECKOUT ----------
@main.route('/checkout', methods=['POST'])
def checkout():
    if 'user' not in session:
        return redirect('/login')

    cart_ids = session.get('cart', [])

    if not cart_ids:
        return redirect('/cart')

    items = []
    all_products = Product.get_all()

    for item_id in cart_ids:
        for product in all_products:
            if str(product['id']) == str(item_id):
                items.append(product)

    order_id = Order.create(session['user'], items)

    session['cart'] = []

    user_name = session.get('user_name')

    return render_template("order_success.html", order_id=order_id, user_name=user_name)
