import psycopg2

def updata_sql(model,brand,category,type1)
    conn = psycopg2.connect(database="device", user="product", password="product", host="", port="5432")
    print "Opened database successfully"
    cur = conn.cursor()
    cur.execute("UPDATE product set category = '%s' , type = '%s' where model = '%s' and brand = '%s'"
               % (category,type1,model,brand))
    conn.commit()
    printf("Operation done successfully")
    
if __name__ == "__main__":
    updata_sql()
