import pymysql

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='python_mysql_mysql',  # 컨테이너 이름 또는 IP
    user='cocolabhub',
    password='cocolabhub',
    db='python_mysql',  # 데이터베이스 이름
    charset='utf8mb4', 
    cursorclass=pymysql.cursors.DictCursor  # DictCursor로 설정    
)

try:
    with conn.cursor() as cursor:
        # Read
        sql = "SELECT * FROM TableName"
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            print(row)  # 각 행 출력
            print(f"pk_id: {row['pk_id']}, column1: {row['column1']}, column2: {row['column2']}")

    

finally:
    conn.close()