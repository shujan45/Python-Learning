import sqlite3

conn=sqlite3.connect("database\college.sqlite3")
cur=conn.cursor()

cur.execute("""create table if not exists students(
    id integer primary key autoincrement,
    name text not null,
    age integer not null,
    address text not null
)
""")
conn.commit()


# def insert(name, age, address):
#     cur.execute("""
#                 insert into students (name,age,address) values (?,?,?)
#                 """,(name,age,address))
#     conn.commit()

# # insert("Rita",19,"koteshwar")




# def select():
#     cur.execute("""
#         select * from students
#     """)
#     rows=cur.fetchall()
#     # rows=cur.fetchone()
#     # rows=cur.fetchmany()
#     print(rows)
# select()



def delete():
    cur.execute("""
        delete from students where id in (3,5,6)
    """)
    conn.commit()
del1=delete()



# def update(name,id):
#     cur.execute("""
#         update students set name=? where id=?
#     """,(name,id))
#     conn.commit()
# update('sabina',7)

# another method
def update ():
    cur.execute("""
        update students set name='shyam' where id=7
    """)
    conn.commit()
up1=update()