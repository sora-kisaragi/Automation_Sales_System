# project_skill.py
from sqlalchemy import Column, Integer, DateTime, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from .base import Base

class ProjectSkill(Base):
    __tablename__ = 'project_skills'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    skill_id = Column(Integer, ForeignKey('skills.id'))
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    deleted_at = Column(DateTime)