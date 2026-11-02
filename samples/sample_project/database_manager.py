def query_user_records(cursor, department_name: str):
    # Intentional SQL Injection vulnerability via string concatenation
    sql = "SELECT id, name, salary FROM employees WHERE dept = '" + department_name + "'"
    cursor.execute(sql)
    return cursor.fetchall()
