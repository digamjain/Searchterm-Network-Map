import psycopg2
import csv
import streamlit as st

def get_csv(searchTerm):

    #Enter the database connection string in the ../.streamlit/secrets.toml file
    conn = psycopg2.connect(database = st.secrets["name_of_db"],user = st.secrets["username"] ,host = st.secrets["hostname"], port=st.secrets["port_number"] ,password = st.secrets["user_password"])
    cur = conn.cursor()

    #searchTerm = str(input("Enter the searchTerm: ")).lstrip(" ")
    ss = searchTerm

    lis_cname = []
    cur.execute("select column_name from information_schema.columns where table_name = 'cars_info'")
    temp = []
    for i in cur :
        temp.append(str(i).strip("('").strip("',)").upper())
    lis_cname.append(temp[:-1])


    lis_tag = []
    lis_tag.append(searchTerm)
    poplis = []
    weight =3
    f = open('networkmap/depth1.csv', mode='w', newline='')
    writer = csv.writer(f)
    for i in lis_cname:
        lis = list(i)
        lis.append('weight')
        writer.writerow(lis)

    while(len(lis_tag)!=0):

        searchTerm = lis_tag.pop()
        poplis.append(searchTerm)

        cur.execute(f" select * from cars_info where tag  ~* '{searchTerm}.*' ")
        data = cur.fetchall()


        for row in data:
            lis = list(row)
            lis.append(weight)
            writer.writerow(lis)



        cur.execute(f" select tag from cars_info where tag ~* '{searchTerm}.*' ")
        data2 = cur.fetchall()
        # print(data2)
        if weight ==3:
            weight = weight-1


        for x in data2:
            for y in x:
                for k in y.split(', '):
                    if k not in lis_tag and k not in poplis:
                        lis_tag.append(k)

    # print("Done")
    f.close()
    cur.close()
    conn.close()
    return(ss)
