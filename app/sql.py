# class Cl(BaseModel):
#     title:str
#     content:str
#     msg:int=1
#     msg1:Optional[int]=None

# my_posts=[{"title":"title 1","id":1},{"tile":"title 2","id":2},{"title":"title 3","id":3}]

# @app.get("/")
# def login():
#     return {"message":"Hii.."}

# @app.post("/posts")
# def mypost(new_post:Cl):
#     print(new_post)
#     return {"Data":new_post}

# # To add id as a randomvalue , pydantic model into dict
# @app.post('/posts')
# def mypost(post:Cl):
#     post_dict=post.dict()
#     post_dict['id']=randrange(0,10)
#     my_posts.append(post_dict)
#     return{"data":my_posts}

# # To get the latest one

# @app.get('/posts/latest')
# def get_latest():
#     post=my_posts[len(my_posts)-1]
#     print(post)
#     return{"details":post}

# # To get purticular details:

# def find_post(id):
#     for p in my_posts:
#         if p['id']==id:
#             return p
        
# @app.get("/posts/{id}")
# def get_post(id:int):   
#     post=find_post(id)
#     if not post:
#         Response.status_code=404 # To get the 404 error
#         return{"Details": f"The {id} is not posted"}    
#     return{"id":post}

# @app.get("/posts1/{id}")
# def get_post(id:int):   
#     post=find_post(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the {id} not exists")
      
# #To delete the value
# def find_index(id):
#     for i,p in enumerate(my_posts):
#         if p['id']==id:
#             return i
        
        
# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete(id: int):
#     index=find_index(id)
#     if not index:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"There no id {id}")
#     my_posts.pop(index)
#     return
# #update the purticular post
# @app.put("/posts/{id}")
# def update(id:int,post:Cl):
#     index=find_index(id)
#     if not index:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"There no id {id}")
#     post_dict=post.dict()
#     post_dict["id"]=id
#     my_posts[index]=post_dict
#     return{"msg":my_posts}

# # Connecting database
 
# try:
#     con=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='postgres',cursor_factory=RealDictCursor)
#     print("Databse is connected successfully..")
#     cursor=con.cursor()
# except Exception as error:
#     print("Can not connect the database")
#     print("Error :",error)
#     time.sleep(3)

# @app.get("/get")
# def msg():
#     cursor.execute("""SELECT *  FROM product WHERE p_id=6""")
#     post=cursor.fetchone()
#     if not post:
#         return{"msg:":f"There is no data "}
#     print(post)
#     return{"data":post}

# #To post the value in database

# class Post(BaseModel):
#     p_name:str
#     quantity:int
#     p_id:int

# @app.post("/post")
# def post(post:Post):
#     cursor.execute("""INSERT INTO product(p_name,quantity,p_id) VALUES(%s,%s,%s) RETURNING *""",(post.p_name,post.quantity,post.p_id))
#     new_post=cursor.fetchone()
#     con.commit()
#     return{"data":new_post}

# # To fetch the purticular record

# def find(id):
#     for p in post:
#         if p['p_id']==id:
#             return p
# @app.get("/post/{id}")
# def get_one(id):
#     cursor.execute(f"""SELECT * FROM product WHERE p_id= {id} """)
#     one=cursor.fetchone()
#     if not one:
#         raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
#     return{"details:":one}

# # To Delete a record

# @app.delete("/post/{id}")
# def delete_record(id):
#     cursor.execute(f"""DELETE FROM product WHERE p_id={id} RETURNING *""")
#     deleted_record=cursor.fetchone()
#     con.commit() 
#     if deleted_record==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The id={id} does not exist")
    
#     return{"data":deleted_record}

# # to Update the record

# @app.put("/post/{id}")
# def update(post:Post,id):
#     cursor.execute("""UPDATE product SET p_name=%s,quantity=%s,p_id=%s WHERE p_id=%s Returning *""",(post.p_name,post.quantity,id,id))
#     updated_recored=cursor.fetchone()
#     con.commit()
#     if not updated_recored:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Not found id={id}")
#     return{"details:":updated_recored}
 
# # @app.post("/posts")
# # def mypost(a: dict=Body(...)):
# #     print(a)
# #     return{"data":f"title {a['title']} msg {a['msg']}"}   

# @app.get("/sqlalchemy")
# def test_post(db:Session=Depends(get_db)):
#     new_post=db.query(model.register).all()
    # return{"status":new_post.id}


      # hashed_pwd=pwd_context.hash(post.password)
    # post.password=hashed_pwd
    # new_post=model.encrypt(**post.dict())
    # db.add(new_post)
    # db.commit()
    # db.refresh(new_post)
    # return {"data":new_post}