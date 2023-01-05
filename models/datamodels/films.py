from models.basemodel import Base
from typing import Optional, List, Union
from pydantic import validator, BaseModel
from datetime import datetime, date


class FilmResponse(BaseModel):
    film_id: str
    title: str
    episode_id: Optional[str]
    opening_crawl: str
    director: str
    producer: str
    release_date: Union[str, date, datetime]
    edited: str
    created: str

    @validator("release_date")
    def check_release_date(cls, release_date):
        if isinstance(release_date, datetime) or isinstance(release_date, date):
            return release_date.strftime("%d-%m-%y")

    @validator("edited")
    def check_edited(cls, edited):
        if isinstance(edited, datetime) or isinstance(edited, date):
            return edited.strftime("%d-%m-%y")

    @validator("created")
    def check_created(cls, created):
        if isinstance(created, datetime) or isinstance(created, date):
            return created.strftime("%d-%m-%y")

    @validator("episode_id")
    def check_episode_id(cls, episode_id):
        if episode_id is None:
            return ""


class PatchFilm_(BaseModel):
    film_id: int
    title: Optional[str]
    episode_id: Optional[str]
    opening_crawl: Optional[str]
    director: Optional[str]
    producer: Optional[str]
    release_date: Union[str, datetime] = "25-05-77"
    created: Union[str, datetime] = "25-05-77"
    edited: Union[str, datetime] = "25-05-77"
    url: Optional[str]


class Film_(Base):
    film_id: int
    title: str
    episode_id: str
    opening_crawl: str
    director: str
    producer: str
    release_date: Union[str, datetime]

    characters: Optional[List[str]]
    planets: Optional[List[str]]
    starships: Optional[List[str]]
    vehicles: Optional[List[str]]
    species: Optional[List[str]]

    @validator("release_date")
    def check_release_date(cls, release_date):
        if isinstance(release_date, str):
            return datetime.strptime(release_date, "%d-%m-%y")
        return release_date
