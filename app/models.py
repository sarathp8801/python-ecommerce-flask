from .database import get_connection


class Product:
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        cursor.close()
        conn.close()

        return products


class User:
    @staticmethod
    def register(name, email, password):
        conn = get_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, password))

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def login(email, password):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = "SELECT * FROM users WHERE email=%s AND password=%s"
        cursor.execute(sql, (email, password))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        return user


class Order:
    @staticmethod
    def create(user_id, items):
        """
        items: list of product dicts, e.g.
        [{id: 1, name: 'Laptop', price: 799.99}, ...]
        """
        if not items:
            return None

        total = sum(float(p["price"]) for p in items)

        conn = get_connection()
        cursor = conn.cursor()

        # create order
        cursor.execute(
            "INSERT INTO orders (user_id, order_date, total) VALUES (%s, NOW(), %s)",
            (user_id, total),
        )
        order_id = cursor.lastrowid

        # each product quantity = 1 for now
        for p in items:
            cursor.execute(
                "INSERT INTO order_items (order_id, product_id, quantity, price) "
                "VALUES (%s, %s, %s, %s)",
                (order_id, p["id"], 1, p["price"]),
            )

        conn.commit()
        cursor.close()
        conn.close()

        return order_id
