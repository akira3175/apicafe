import django
from django.conf import settings

# Cấu hình Django trước khi truy cập settings
django.setup()

# Bây giờ bạn có thể truy cập vào settings
from django.db import connection
print(connection.settings_dict)

def show_tables():
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for table in tables:
            print(table)

# Gọi hàm để xem danh sách các bảng trong cơ sở dữ liệu
show_tables()
