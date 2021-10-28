from speech_recognition import Recognizer, Microphone
from .parser import bot_parser

def reccord_audio():
    """Records audio from the microphone and returns the audio data"""
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occurred, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    recognizer = Recognizer()
    microphone = Microphone()
    if not isinstance(recognizer, Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=3)
        recognizer.dynamic_energy_threshold = True  
        audio = recognizer.listen(source, phrase_time_limit=5)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly

    try:
        response["transcription"] = recognizer.recognize_google(
            audio, 
            language="fr-FR"
            )
    except Exception as ex:

        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "Desolé, je n'ai pas compris; {0}".format(ex)
        response["transcription"] = "En attente de votre réponse"
        return response
        
    except Recognizer.RequestError as e:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "Recognition error; {0}".format(e)
        response["transcription"] = "Desolé, je n'ai pas pu me connecter au serveur...essayez encore"


    response = bot_parser(response["transcription"].lower())


    return response
