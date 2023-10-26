import boto3
translate_client = boto3.client('translate')
def lambda_handler(event, context): 
    # event['Details']['Parameters']['exampleParameterKey1'];
    print(event)
    review_text = event['Details']['Parameters']['text']
    targetLanaugageCode = event['Details']['Parameters']['targetLanguageCode']
    resp = {}
    
    if targetLanaugageCode == "en": 
        resp['TranslatedText'] = review_text
        return resp
        
    translate_response = translate_client.translate_text(
        Text=review_text,
        SourceLanguageCode='auto',
        TargetLanguageCode=targetLanaugageCode
    )
    print(translate_response)    
    return translate_response