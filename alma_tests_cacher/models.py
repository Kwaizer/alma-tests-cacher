from typing import List, Optional, Union

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

from alma_tests_cacher.constants import (
    DEFAULT_BS_API_URL,
    DEFAULT_LOGGING_LEVEL,
    DEFAULT_REQUESTS_LIMIT,
    DEFAULT_SLEEP_TIMEOUT,
)


class PackageTestRepository(BaseModel):
    int_id: Optional[int] = Field(None, alias='id')
    bson_id: Optional[str] = Field(None, alias='_id')
    package_name: str
    folder_name: str
    url: str

    @property
    def id(self):
        return self.int_id or self.bson_id


class TestRepository(BaseModel):
    __test__ = False
    id: Union[int, str]
    name: str
    url: str
    tests_dir: str
    tests_prefix: Optional[str] = ""
    packages: List[PackageTestRepository]
    common_test_dir_name: str = ""


class Config(BaseSettings):
    requests_limit: int = DEFAULT_REQUESTS_LIMIT
    sleep_timeout: int = DEFAULT_SLEEP_TIMEOUT
    bs_api_url: str = DEFAULT_BS_API_URL
    logging_level: str = DEFAULT_LOGGING_LEVEL
    bs_jwt_token: str = ""
    cacher_sentry_environment: str = "dev"
    cacher_sentry_dsn: str = ""
    cacher_sentry_traces_sample_rate: float = 0.2
    gerrit_username: str = ""
