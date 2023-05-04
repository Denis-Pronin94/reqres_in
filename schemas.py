from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, HttpUrl
from pydantic.color import Color


class ListData(BaseModel):
    """Schema list data."""

    id: int
    email: str
    first_name: str
    last_name: str
    avatar: HttpUrl


class Support(BaseModel):
    """Schema support."""

    url: HttpUrl
    text: str


class ListDataResource(BaseModel):
    """Schema list data resource."""

    id: int
    name: str
    year: int
    color: Color
    pantone_value: str


class ListUserSchema(BaseModel):
    """Schema List user."""

    page: int
    per_page: int
    total: int
    total_pages: int
    data: Optional[List[ListData]]
    support: Support


class SingleUserSchema(BaseModel):
    """Schema single user."""

    data: ListData
    support: Support


class ListResourceSchema(BaseModel):
    """Schema single user."""

    page: int
    per_page: int
    total: int
    total_pages: int
    data: Optional[List[ListDataResource]]
    support: Support


class SingleResourceSchema(BaseModel):
    """Schema single resource."""

    data: ListDataResource
    support: Support


class CreateSchema(BaseModel):
    """Schema create."""

    name: str
    job: str
    id: int
    createdAt: datetime


class UpdateSchema(BaseModel):
    """Schema update."""

    name: str
    job: str
    updatedAt: datetime


class RegisterSuccessfulSchema(BaseModel):
    """Schema register."""

    id: int
    token: str


class RegisterUnsuccessfulSchema(BaseModel):
    """Schema unregister."""

    error: str


class LoginSuccessfulSchema(BaseModel):
    """Schema register."""

    token: str


class LoginUnsuccessfulSchema(BaseModel):
    """Schema register."""

    error: str
