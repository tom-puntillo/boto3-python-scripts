import argparse # ararse is a built in python package, we add it with an import statement
import boto3

#define the parser variable equal to argparse.ArgumentParser()

parser = argparse.ArgumentParser(description='Provides translation between one source language and another of the same set of languages.')

#Add each of the arguments using the parser.add_argument() method
parser.add_argument(
    '--text',
    dest='Text',
    type=str,
    help='The text to translate. The text string can be a maximum of 5,000 bytes long. Depending on your character set, this may be less than 5,000',
    required=True
    )
    
parser.add_argument(
    '--source-language-code',
    dest='SourceLanguageCode',
    type=str,
    help='The language code for the language of the source text. The language must be a language supported Amazon Translate',
    required=True
    )
    
parser.add_argument(
    '--target-language-code',
    dest='TargetLanguageCode',
    type=str,
    help='The language code requested for the language of the target text. The language must be a language supported by Amazon Translate',
    required=True
    )
    
# This will inspect the command line, convert each argument to the appropiate type and then invoke the appropriate action.
args = parser.parse_args()
    
def translate_text(**kwargs):
    translate = boto3.client('translate')
    response = translate.translate_text(**kwargs)
    print(response)

def main():
  # vars() is an inbuilt function which returns a dictionary object
  translate_text(**vars(args))
    
if __name__ == '__main__':
    main()