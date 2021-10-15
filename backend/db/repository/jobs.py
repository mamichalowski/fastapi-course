from sqlalchemy.orm import Session
from sqlalchemy.sql.operators import exists

from schemas.jobs import JobCreate
from db.models.jobs import Job

def create_new_job(job: JobCreate, db : Session,owner_id):
    job = Job(**job.dict(),owner_id = owner_id)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

def retreive_job(id:int,db:Session):
    job = db.query(Job).filter(Job.id==id).first()
    return job

def list_jobs(db:Session):
   # jobs = db.query(Job).filter(Job.is_active == True)
   jobs = db.query(Job).offset(0).limit(100).all()
   return jobs

def update_job_by_id(id:int,job:JobCreate,db:Session,owner_id:int):
    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job.first():
        return 0
    job.__dict__.update(owner_id=owner_id)
    existing_job.update(job.__dict__)
    db.commit()
    return 1





