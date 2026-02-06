from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from src.core.api import get_status

class CheckStatusIntentHandler(AbstractRequestHandler):
    """Handler for the CheckStatusIntent."""

    def can_handle(self, handler_input: HandlerInput) -> bool:
        """
        Checks if the handler can handle the incoming request.
        """
        return handler_input.request_envelope.request.intent.name == "CheckStatusIntent"

    def handle(self, handler_input: HandlerInput) -> Response:
        """
        Handles the CheckStatusIntent.
        """
        status_data = get_status()

        if status_data:
            speech_text = "Aqui está o status das linhas: "
            for line in status_data["lines"]:
                speech_text += f"A linha {line['name']} está com status de {line['status']}. "
            speech_text += f"Última atualização foi em {status_data['updatedAt']}."
        else:
            speech_text = "Não consegui encontrar o status das linhas no momento."

        return handler_input.response_builder.speak(speech_text).set_should_end_session(True).response
