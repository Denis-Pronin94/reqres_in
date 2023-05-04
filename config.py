from dynaconf import LazySettings

settings = LazySettings(
    SETTINGS_FILE_FOR_DYNACONF='settings.yaml;settings.local.yaml',

)
settings.configure()

URL = settings['URL']
