import sys
import os
import json
import cohere  
from cohere.responses.classify import Example
from dotenv import load_dotenv

def getInputs():
    inputs = []

    try:
        with open('reviews.json', 'r', encoding="utf8") as f:
            data = json.load(f)

            for review in data['reviews']:
                inputs.append( [ review['content'], review['rating'] ] )
    
    except ( FileNotFoundError, PermissionError ):
        print("File " + sys.argv[1] + " has bad permissions or does not exist!")
        print("Exiting program...")
        sys.exit(1)

    finally:
        f.close()                       # Closing file
        
    return inputs

def main():
    load_dotenv()

    inputs = getInputs()

    co = cohere.Client( os.getenv( 'COHERE_API_KEY' ) )

    examples = []
    for i in range(0, len( inputs ) - 5 ):
        examples.append( Example( inputs[i][0], str( inputs[i][1] ) ) )

    # We assume we have enough reviews such that the last 5 can be used as verifiers (not used as input into the cohere model)
    toPredict = []
    for i in range( len( inputs ) - 5, len( inputs ) ):
        toPredict.append( inputs[i][0] )

    response = co.classify(  
        model='large',  
        inputs=toPredict,  
        examples=examples)

    # Create a list of actual and predicted ratings and determine how many we are able to predict based off of previous reviews
    actualRatings = []
    for i in range( len( inputs ) - 5, len( inputs ) ):
        actualRatings.append( inputs[i][1] )

    predictedRatings = []
    for item in response.classifications:
        predictedRatings.append( int( item.predictions[0] ) )

    correctPredictions = 0
    for r in range( 0, len( actualRatings ) ):
        if actualRatings[r] == predictedRatings[r]:
            correctPredictions += 1

    print( "Based on the previous reviews, we are able to guess with " + str( ( correctPredictions / len( actualRatings ) ) * 100 ) + "% accuracy what you would rate other books based on the review content!" )

main()