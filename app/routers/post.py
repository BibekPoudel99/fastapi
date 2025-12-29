from fastapi import Body, status, HTTPException, Depends, APIRouter
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import schemas, model, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
              limit: int = 15, skip: int = 0, search: Optional[str] = ""):
    # cur.execute("""SELECT * FROM posts""")
    # posts = cur.fetchall()
    results = db.query(model.Post, func.count(model.Vote.post_id).label("votes")).join(
        model.Vote, model.Vote.post_id == model.Post.id, isouter=True
    ).group_by(
        model.Post.id
    ).filter(
        model.Post.title.contains(search)).limit(limit).offset(skip).all() # it is a list
    
    # posts = [{"Post": post, "votes": vote} for post, vote in results]

    return results

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def createpost(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute("""INSERT INTO posts(title, content, published) VALUES(%s, %s, %s) RETURNING * """,
    #             (post.title, post.content, post.published))
    # new_post = cur.fetchone()
    # conn.commit()
    new_post = model.Post(owner_id =current_user.id,
        **post.dict()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    # post = cur.fetchone()
    # post = db.query(model.Post).filter(model.Post.id == id).first()

    post = db.query(model.Post, func.count(model.Vote.post_id).label("votes")).join(
        model.Vote, model.Vote.post_id == model.Post.id, isouter=True
    ).group_by(
        model.Post.id).filter(model.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} was not found!!")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message" : f"Post with id {id} was not found!!"}

    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested" \
    #     "action")
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    # deleted_post = cur.fetchone()
    delete_post_query = db.query(model.Post).filter(model.Post.id == id)

    deleted_post = delete_post_query.first()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} does not exist!")
    
    if deleted_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested" \
        "action")
    
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    # cur.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE id=%s returning *""",
    #             (post.title, post.content, post.published, str(id))) 
    query = db.query(model.Post).filter(model.Post.id == id)
    post = query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} does not exist!")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested" \
        "action")
    
    query.update(updated_post.dict(), synchronize_session=False) # we need to pass in a python dictionary 
    db.commit()

    return query.first()