import os
from enum import Enum

from dotenv import load_dotenv


load_dotenv()
API_URL = os.getenv("API_URL")


class Url(Enum):
    DAYS = 1
    GROUPS = 2
    LECTURERS = 3
    LESSONS = 4
    SLOTS = 5
    SPECIALTIES = 6
    VENUES = 7
    SCHEDULE = 8

urls = {
    Url.DAYS:       f"{API_URL}/api/v1/lookup/days",
    Url.GROUPS:     f"{API_URL}/api/v1/lookup/groups",
    Url.LECTURERS:  f"{API_URL}/api/v1/lookup/lecturers",
    Url.LESSONS:    f"{API_URL}/api/v1/lookup/lessons",
    Url.SLOTS:      f"{API_URL}/api/v1/lookup/slots",
    Url.SPECIALTIES:f"{API_URL}/api/v1/lookup/specialties",
    Url.VENUES:     f"{API_URL}/api/v1/lookup/venues",
    Url.SCHEDULE:   f"{API_URL}/api/v1/schedule",
}