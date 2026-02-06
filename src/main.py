from ask_sdk_core.skill_builder import SkillBuilder
from src.handlers.check_status import CheckStatusIntentHandler
from src.handlers.default import (
    HelpIntentHandler,
    CancelAndStopIntentHandler,
    ErrorHandler,
)

sb = SkillBuilder()

# Add the request handlers
sb.add_request_handler(CheckStatusIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelAndStopIntentHandler())

# Add the error handler
sb.add_exception_handler(ErrorHandler())

# Expose the skill builder object as a lambda handler
lambda_handler = sb.lambda_handler()