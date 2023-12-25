# project.py
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    company_name = Column(String(255))
    person_in_charge = Column(String(255))
    project_name = Column(String(255))
    project_content = Column(Text)
    work_location = Column(String(255))
    period = Column(String(255))
    number_of_people = Column(String(255))
    price_requirements = Column(String(255))
    settlement = Column(String(255))
    interview = Column(String(255))
    summary = Column(Text)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime)