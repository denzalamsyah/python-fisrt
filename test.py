# from fastapi import FastAPI
# import blog

# app = FastAPI()

# blog.models.Base.metadata.create_all(blog.database.engine)

# app.include_router(blog.routers.blog.router) # menghubungkan dengan router blog
# app.include_router(blog.routers.user.router) # menghubungkan dengan router user
# app.include_router(blog.routers.authentication.router)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)