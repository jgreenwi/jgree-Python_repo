import boto3


dynamodb = boto3.client('dynamodb')

response = dynamodb.put_item(
    Item={
   'ID':{
          'S': 'hsv9krNOqy'  ,
        },
        'Theme Park': {
            'S': 'Universal Studios',
        },
        'Ride': {
            'S': 'Harry Potter',
        },
        'Rank': {
            'S': '1',
        },
    'ID':{
          'S': 'u2Kket8QKP'  ,
        },
        'Theme Park': {
            'S': 'Hollywood Studios',
        },
        'Ride': {
            'S': 'Tower of Terror',
        },
        'Rank': {
            'S': '2',
        },
    'ID':{
          'S': 'ouvGYwXPze'  ,
        },
        'Theme Park': {
            'S': 'Hollywood Studios',
        },
        'Ride': {
            'S': 'Galaxys Edge',
        },
        'Rank': {
            'S': '3',
        },
    'ID':{
          'S': 'FurxXXkfui'  ,
        },
        'Theme Park': {
            'S': 'Animal Kingdom',
        },
        'Ride': {
            'S': 'Flight of Passage',
        },
        'Rank': {
            'S': '4',
        },
    'ID':{
          'S': 'So1bPsGjst'  ,
        },
        'Theme Park': {
            'S': 'Universal Studios',
        },
        'Ride': {
            'S': 'Incredible Hulk',
        },
        'Rank': {
            'S': '5',
        },    
    'ID':{
          'S': 'uxnYSyg5tW'  ,
        },
        'Theme Park': {
            'S': 'Universal Studios',
        },
        'Ride': {
            'S': 'Amazing Spider-man',
        },
        'Rank': {
            'S': '6',
        },    
    'ID':{
          'S': 'rgqyz0cIDQ'  ,
        },
        'Theme Park': {
            'S': 'King Kong',
        },
        'Ride': {
            'S': '',
        },
        'Rank': {
            'S': '7',
        },    
    'ID':{
          'S': '6LzW5jI9it'  ,
        },
        'Theme Park': {
            'S': 'Magical Kingdom',
        },
        'Ride': {
            'S': 'Space Mountain',
        },
        'Rank': {
            'S': '8',
        },    
    'ID':{
          'S': 'VCy2lMlqgH'  ,
        },
        'Theme Park': {
            'S': 'Animal Kingdom',
        },
        'Ride': {
            'S': 'Legend of Forbidden Mountain',
        },
        'Rank': {
            'S': '9',
        },    
    'ID':{
          'S': 'o9Id85edOy'  ,
        },
        'Theme Park': {
            'S': 'Universal Studios',
        },
        'Ride': {
            'S': 'Revenge of the Mummy',
        },
        'Rank': {
            'S': '10',
        },    
    
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='DisneyAttractions',
)