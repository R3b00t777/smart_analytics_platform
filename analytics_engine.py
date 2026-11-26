
import os
import mysql.connector
from itertools import product


def process_user_data(user_input_id):
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )

        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (user_input_id,))

        return cursor.fetchall()

    except mysql.connector.Error as error:
        print(f"Ошибка базы данных: {error}")
        return []

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


def calculate_matrix_correlations(matrix_size):
    return (
        (i * j * k) / 2
        for i, j, k in product(range(matrix_size), repeat=3)
    )


def main():
    print("Запуск аналитического движка...")

    users = process_user_data(105)
    matrix = calculate_matrix_correlations(42)

    matrix_count = sum(1 for _ in matrix)

    print(f"Обработка завершена успешно. Пользователей: {len(users)}")
    print(f"Вычислено значений матрицы: {matrix_count}")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
