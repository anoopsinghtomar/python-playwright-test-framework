"""
Framework constants.

Centralized location for framework-wide constants to avoid magic numbers
and duplicated strings.
"""

# Timeouts (milliseconds)
DEFAULT_TIMEOUT = 30_000
SHORT_TIMEOUT = 5_000
LONG_TIMEOUT = 60_000

# Browsers
CHROMIUM = "chromium"
FIREFOX = "firefox"
WEBKIT = "webkit"

# Supported environments
DEV = "dev"
QA = "qa"
UAT = "uat"
PROD = "prod"

# Artifact directories
LOGS_DIR = "logs"
REPORTS_DIR = "reports"
SCREENSHOTS_DIR = "screenshots"
TRACES_DIR = "traces"

# Screenshot names
FAILURE_SCREENSHOT = "failure"

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = "automation.log"