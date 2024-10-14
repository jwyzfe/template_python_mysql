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
        sql = "SELECT * FROM QUESTION"
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            print(row)  # 각 행 출력
            print(f"pk_id: {row['QPK_A']}, column1: {row['QUESTION']}, column2: {row['ANSWER']}")
            
            
        sql2 = "SELECT * FROM OPTION_TABLE"
        cursor.execute(sql2)
        data2 = cursor.fetchall()
        for row in data2:
            print(row)  # 각 행 출력
            print(f"pk_id: {row['OPK_B']}, column1: {row['OFK_A']}, column2: {row['OPTIONS']}")

    

finally:
    conn.close()
    
    
    