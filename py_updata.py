import psycopg2


def updata_sql(model, brand, category, type1):
    cur = conn.cursor()
    cur.execute("UPDATE product set category='%s',type='%s' remark='dzh' where model='%s' and brand='%s'"
                % (category, type1, model, brand))
    print(category)


if __name__ == "__main__":
    # coding:utf-8
    import csv

    # path = ''文件地址
    path = 'F:\物联网\CWE\productcsv.csv'
    # 连接数据库
    conn = psycopg2.connect(database="device_info", user="product", password="product", host="10.10.13.112",
                            port="5432")
    print("Opened database successfully")
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        #逐行读取数据
        for row in reader:
            updata_sql(row[0], row[5], row[2], row[3])
    conn.commit()
    print("Operation done successfully")
