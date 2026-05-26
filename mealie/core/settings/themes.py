from pydantic_settings import BaseSettings, SettingsConfigDict


class Theme(BaseSettings):
    # Grayscale palette — light mode (dark grays on white background)
    light_primary: str = "#212121"
    light_accent: str = "#424242"
    light_secondary: str = "#616161"
    light_success: str = "#4F4F4F"
    light_info: str = "#757575"
    light_warning: str = "#9E9E9E"
    light_error: str = "#000000"

    # Grayscale palette — dark mode (light grays on near-black background)
    dark_primary: str = "#FAFAFA"
    dark_accent: str = "#E0E0E0"
    dark_secondary: str = "#BDBDBD"
    dark_success: str = "#9E9E9E"
    dark_info: str = "#757575"
    dark_warning: str = "#BDBDBD"
    dark_error: str = "#FFFFFF"
    model_config = SettingsConfigDict(env_prefix="theme_", extra="allow")
