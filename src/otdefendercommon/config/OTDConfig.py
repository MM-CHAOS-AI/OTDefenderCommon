from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class OTDConfig(BaseSettings):
    # Declare properties with explicit Python type hints
    OTDEF_VERSION:str = "0.0.0"
    RUN_MODE:str = "DEV"
    OTDEF_DB_FILE:str = "otdefdb_current.db"
    OTDEF_DB_DIR:str = "./otdb/"
    OTDEF_DB_BACKUP:str = "/home/user/Unix_Extra/OTDefender/DB_BACKUP/"
    TIMEOUT:float = 30.0
    DEBUG:bool = True
    DB_ECHO:bool = False

    # For sensor
    PCAP_WATCH_DIR:str = "./PAC_WATCH"
    PCAP_PROCESSED_DIR:str = "./PAC_PROCESSED"
    SENSOR_EVENT_TRIGGER_SEC:int = 10
    PCAP_MERGE_EVENT_TRIGGER_SEC:int = 3600
    PCAP_MERGE_DIR:str = "./PCAP_MERGED"

    #LOGGING 
    LOG_FILE_PATH:str = "./logs/OTSensorMain_App.log"
    LOG_MAX_SIZE:int = 100 * 1024 * 1024,  # 100 MB
    LOGGING_MODE:str = "INFO"
    LOG_BACKUP_COUNT:int = 5

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return f"sqlite:///{self.OTDEF_DB_DIR}/{self.OTDEF_DB_FILE}"

    # Tell Pydantic to read from the local .env file automatically
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Instantiated globally for easy project-wide importing
settings = OTDConfig()
