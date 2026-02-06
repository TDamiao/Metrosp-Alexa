from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for the HelpIntent."""

    def can_handle(self, handler_input: HandlerInput) -> bool:
        """
        Checks if the handler can handle the incoming request.
        """
        return (
            handler_input.request_envelope.request.type == "IntentRequest"
            and handler_input.request_envelope.request.intent.name == "AMAZON.HelpIntent"
        )

    def handle(self, handler_input: HandlerInput) -> Response:
        """
        Handles the HelpIntent.
        """
        speech_text = "Você pode me perguntar sobre o status das linhas de transporte. Como posso ajudar?"
        return handler_input.response_builder.speak(speech_text).ask(speech_text).response


class CancelAndStopIntentHandler(AbstractRequestHandler):
    """Handler for the Cancel and Stop intents."""

    def can_handle(self, handler_input: HandlerInput) -> bool:
        """
        Checks if the handler can handle the incoming request.
        """
        return (
            handler_input.request_envelope.request.intent.name
            in ["AMAZON.CancelIntent", "AMAZON.StopIntent"]
        )

    def handle(self, handler_input: HandlerInput) -> Response:
        """
        Handles the Cancel and Stop intents.
        """
        speech_text = "Até logo!"
        return handler_input.response_builder.speak(speech_text).response


class ErrorHandler(AbstractRequestHandler):
    """Handler for errors."""

    def can_handle(self, handler_input: HandlerInput, exception: Exception) -> bool:
        """
        Checks if the handler can handle the incoming request.
        """
        return True

    def handle(self, handler_input: HandlerInput, exception: Exception) -> Response:
        """
        Handles errors.
        """
        print(exception)
        speech_text = "Desculpe, houve um erro. Tente novamente."
        return handler_input.response_builder.speak(speech_text).response
