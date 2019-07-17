import psycopg2


dbConnect = psycopg2.connect(
    host="peiky-core-certification.cog5jtvdbon3.us-east-2.rds.amazonaws.com",
    database= "peiky_cert",
    port= "5432",
    user="omar.perez",
    password= "omar.perez"
    )


cursor1 = dbConnect.cursor()

def division_zone_area():
    
    cursor1.execute(
        "select id,name,company_id, type from division where name like '%Zona 53%'"
        )   
    variable =  cursor1.fetchmany()

    for x in variable:
        print(f"zone_id {x[0]} zone_name {x[1]} company {x[2]} type {x[3]} ")
division_zone_area()

def user_password():
    update_password =  cursor1.execute(
        "update public.user set password = '$argon2i$v=19$m=65536,t=6,p=1$bQJfpYygrDnU4IuL2hPmMw$ce/hAj7zduyDotAGb3cjrV5/P5FjlVYLifNCYlHVRTc' where email like '%omar.perez@peiky.com%';")
    dbConnect.commit()
    dbConnect.close()
# user_password()


def user_session():
    
    cursor1.execute(
        "select s.user_id,s.application_id,s.version_id,s.status from session as s  where user_id in (select id from public.user where email like '%omar.perez@peiky.com%') and status = true" 
        )
    
    var_out_put = cursor1.fetchall() #trae todo los valores
    
    # update_status = cursor1.execute (
    # "update session set status = false where user_id in (select id from public.user where email like '%omar.perez@peiky.com%') "
    # )
    # dbConnect.commit()
    # dbConnect.close()
    
    for x in var_out_put:
        print(f" user_id {x[0]}  aplication_id {x[1]} version_id {x[2]} status {x[3]}")
# user_session()

def user_store():
    
    cursor1.execute(
        "select  us.user_id, us.store_id,us.status from user_store as us where user_id in (select id from public.user where  email like '%omar.perez@peiky.com%') order by us.store_id asc ;"
    )

    # update_store =cursor1.execute (
    #     "update user_store set status = false where user_id in  (select id from public.user where email like '%omar.perez@peiky.com%' and store_id = 5396);"
    #  )
    # dbConnect.commit()
    # dbConnect.close()

    var_store = cursor1.fetchall() #trae algun valor 
    
    for u in var_store:
        print(f"user_id {u[0]} store_id {u[1]} status {u[2]} ")
# user_store()

def user_company():
    # example subquery

    cursor1.execute(
        "select * from user_company as uc where user_id in (select id from  public.user where email like '%omar.perez@peiky.com%')order by uc.company_id asc;"
    )

    # update_company = cursor1.execute("update user_company set status = true where user_id in (select id from public.user where email like '%omar.perez@peiky.com%' and company_id in (5,6,7))")
    # dbConnect.commit()
    # dbConnect.close()

    variable = cursor1.fetchall()
    for x in variable:
        print(f" user_id {x[0]} company_id {x[1]} role_id {x[2]} division_id {x[3]} status {x[4]}")
# user_company()




def products_category():
    cursor1.execute(
        "select p.name,p.description,p.price,pc.id,pc.name, pc.company_id from product as p  join product_category as pc   on (p.product_category_id = pc.id) where p.name like '%ropa colección mayo34%' "
    )
    variable = cursor1.fetchmany()
    for x in variable:
        print(f"Product {x[0]} Description {x[1]} Price {x[2]} Category_id {x[3]} Category_name {x[4]} Company {x[5]}")
# products_category()
# dbConnect.close()


