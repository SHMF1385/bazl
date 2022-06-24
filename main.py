from datetime import timedelta
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import config, crud, database, models, schemas, utils

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI(name="بذل‌الخاطر")

@app.post('/signup')
def signup(form_data: schemas.Signup, db: Session = Depends(database.get_db)):
    if not utils.is_email(form_data.email):
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="رایانامهٔ وارد شده معتبر نیست",
            headers={"WWW-Authenticate": "Bearer"},
        )
    check_email = db.query(models.User).filter(models.User.email == form_data.email).first()
    if check_email:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="این رایانامه قبلا توسط شخص دیگری استفاده شده",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # TODO: Send Confirmation email
    new_user = crud.create_user(schemas.Signup(email=form_data.email, nickname=form_data.nickname, password=form_data.password), db)
    return {'email': new_user.email, 'nickname': new_user.nickname}

@app.post('/token', response_model=schemas.TokenData)
def login_for_acccess_token(form_data: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    user = crud.authenticate_user(email=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={'sub': user.email},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token}
