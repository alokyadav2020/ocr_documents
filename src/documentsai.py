from google.api_core.client_options import ClientOptions
from google.cloud import documentai
from pathlib import Path



MIME_TYPE ='image/jpeg'

def ocr_doc(PROJECT_ID:str,LOCATION:str,PROCESSOR_ID:str,FILE_PATH:Path):

    try:
       
       if FILE_PATH is not None:
           #Instantiates a client
        docai_client = documentai.DocumentProcessorServiceClient(client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com"))

        # The full resource name of the processor, e.g.:
        # projects/project-id/locations/location/processor/processor-id
        # You must create new processors in the Cloud Console first
        RESOURCE_NAME = docai_client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)

        # Read the file into memory
        with open(FILE_PATH, "rb") as image:
            image_content = image.read()

        # Load Binary Data into Document AI RawDocument Object
        raw_document = documentai.RawDocument(content=image_content, mime_type=MIME_TYPE)

        # Configure the process request
        request = documentai.ProcessRequest(name=RESOURCE_NAME, raw_document=raw_document)

        # Use the Document AI client to process the sample form
        result = docai_client.process_document(request=request)

        document_object = result.document
        return document_object.text
        # print("Document processing complete.")
        # print(f"Text: {document_object.text}")
                
       
    except Exception as e:
       raise e
       

#