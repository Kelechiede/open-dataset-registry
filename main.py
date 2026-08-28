from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas
import auth

# Create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Open Dataset Registry API",
    description="A public catalogue of datasets — browse, search and filter by domain and tags",
    version="1.0.0"
)

# ── Dependency ────────────────────────────────────────
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ── ROOT ──────────────────────────────────────────────
@app.get("/")
def root():
    return {
        "message": "Welcome to the Open Dataset Registry API",
        "developer": "Kelechukwu Innocent Ede",
        "endpoints": ["/datasets", "/datasets/search", "/docs"]
    }


# ── AUTH ROUTES ───────────────────────────────────────
@app.post("/auth/register")
def register(admin: schemas.AdminRegister, db: Session = Depends(get_db)):
    existing = db.query(models.Admin).filter(
        models.Admin.username == admin.username
    ).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )
    new_admin = models.Admin(
        username=admin.username,
        email=admin.email,
        password=auth.hash_password(admin.password)
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return {
        "message": f"Admin account created for {admin.username}",
        "username": admin.username,
        "email": admin.email
    }


@app.post("/auth/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    admin = db.query(models.Admin).filter(
        models.Admin.username == form_data.username
    ).first()
    if not admin or not auth.verify_password(
        form_data.password, admin.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = auth.create_access_token(
        data={"sub": admin.username}
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": admin.username,
        "message": "Login successful"
    }


# ── DATASET ROUTES ────────────────────────────────────
@app.get("/datasets")
def get_datasets(db: Session = Depends(get_db)):
    datasets = db.query(models.Dataset).all()
    return [
        {
            "id": d.id,
            "name": d.name,
            "source": d.source,
            "format": d.format,
            "size": d.size,
            "domain": d.domain,
            "description": d.description,
            "tags": d.tags.split(",") if d.tags else [],
            "url": d.url
        }
        for d in datasets
    ]


@app.get("/datasets/search")
def search_datasets(
    domain: str = None,
    format: str = None,
    tag: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Dataset)
    if domain:
        query = query.filter(
            models.Dataset.domain.ilike(f"%{domain}%")
        )
    if format:
        query = query.filter(
            models.Dataset.format.ilike(f"%{format}%")
        )
    datasets = query.all()
    results = [
        {
            "id": d.id,
            "name": d.name,
            "source": d.source,
            "format": d.format,
            "size": d.size,
            "domain": d.domain,
            "description": d.description,
            "tags": d.tags.split(",") if d.tags else [],
            "url": d.url
        }
        for d in datasets
    ]
    if tag:
        results = [
            r for r in results
            if tag.lower() in [t.strip().lower() for t in r["tags"]]
        ]
    return {
        "query": {"domain": domain, "format": format, "tag": tag},
        "count": len(results),
        "results": results
    }


@app.get("/datasets/{dataset_id}")
def get_dataset(dataset_id: int, db: Session = Depends(get_db)):
    dataset = db.query(models.Dataset).filter(
        models.Dataset.id == dataset_id
    ).first()
    if not dataset:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found"
        )
    return {
        "id": dataset.id,
        "name": dataset.name,
        "source": dataset.source,
        "format": dataset.format,
        "size": dataset.size,
        "domain": dataset.domain,
        "description": dataset.description,
        "tags": dataset.tags.split(",") if dataset.tags else [],
        "url": dataset.url
    }


@app.post("/datasets")
def create_dataset(
    dataset: schemas.DatasetCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.verify_token)
):
    new_dataset = models.Dataset(
        name=dataset.name,
        source=dataset.source,
        format=dataset.format,
        size=dataset.size,
        domain=dataset.domain,
        description=dataset.description,
        tags=dataset.tags,
        url=dataset.url
    )
    db.add(new_dataset)
    db.commit()
    db.refresh(new_dataset)
    return new_dataset


@app.put("/datasets/{dataset_id}")
def update_dataset(
    dataset_id: int,
    updates: schemas.DatasetUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.verify_token)
):
    dataset = db.query(models.Dataset).filter(
        models.Dataset.id == dataset_id
    ).first()
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    if updates.name is not None:
        dataset.name = updates.name
    if updates.source is not None:
        dataset.source = updates.source
    if updates.format is not None:
        dataset.format = updates.format
    if updates.size is not None:
        dataset.size = updates.size
    if updates.domain is not None:
        dataset.domain = updates.domain
    if updates.description is not None:
        dataset.description = updates.description
    if updates.tags is not None:
        dataset.tags = updates.tags
    if updates.url is not None:
        dataset.url = updates.url
    db.commit()
    db.refresh(dataset)
    return dataset


@app.delete("/datasets/{dataset_id}")
def delete_dataset(
    dataset_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.verify_token)
):
    dataset = db.query(models.Dataset).filter(
        models.Dataset.id == dataset_id
    ).first()
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    db.delete(dataset)
    db.commit()
    return {"message": f"Dataset '{dataset.name}' deleted successfully"}