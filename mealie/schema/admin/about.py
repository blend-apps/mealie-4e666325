from mealie.schema._mealie import MealieModel


class AppStatistics(MealieModel):
    total_recipes: int
    total_users: int
    total_households: int
    total_groups: int
    uncategorized_recipes: int
    untagged_recipes: int


class AppInfo(MealieModel):
    production: bool
    version: str
    demo_status: bool
    allow_signup: bool
    allow_password_login: bool
    default_group_slug: str | None = None
    default_household_slug: str | None = None
    enable_oidc: bool
    oidc_redirect: bool
    oidc_provider_name: str
    token_time: int


class AppTheme(MealieModel):
    # Grayscale palette — light mode
    light_primary: str = "#212121"
    light_accent: str = "#424242"
    light_secondary: str = "#616161"
    light_success: str = "#4F4F4F"
    light_info: str = "#757575"
    light_warning: str = "#9E9E9E"
    light_error: str = "#000000"

    # Grayscale palette — dark mode
    dark_primary: str = "#FAFAFA"
    dark_accent: str = "#E0E0E0"
    dark_secondary: str = "#BDBDBD"
    dark_success: str = "#9E9E9E"
    dark_info: str = "#757575"
    dark_warning: str = "#BDBDBD"
    dark_error: str = "#FFFFFF"


class AppStartupInfo(MealieModel):
    is_first_login: bool
    """
    The applications best guess that a user hasn't logged in. Currently, it really
    on indicates that the 'changeme@example.com' user is still in the database. Once
    it is removed, this will always return False.
    """

    is_demo: bool


class AdminAboutInfo(AppInfo):
    versionLatest: str
    api_port: int
    api_docs: bool
    db_type: str
    db_url: str | None = None
    default_group: str
    default_household: str
    build_id: str
    recipe_scraper_version: str


class CheckAppConfig(MealieModel):
    email_ready: bool
    ldap_ready: bool
    oidc_ready: bool
    base_url_set: bool
    is_up_to_date: bool
