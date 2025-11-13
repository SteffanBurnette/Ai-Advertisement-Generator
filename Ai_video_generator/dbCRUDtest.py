import asyncio
import pymongo
from pymongo import AsyncMongoClient
import os 
from dotenv import load_dotenv

load_dotenv("C:/Users/Steffan/Desktop/Ai_advertisement_generator/Ai-Advertisement-Generator/Ai_video_generator/.env")
URI = os.getenv("MONGO_CONNECTION_STRING")


async def main():
    try:
        uri = URI
        client = AsyncMongoClient(uri)

        database = client["test"]
        collection = database["col1"]

        # start example code here
        #Insert a single value
        #result = await collection.insert_one({ "name" : "jeff" })
        #print(result.acknowledged)

        #Insert multiple values at once
        '''
        document_list = [
            { "name" : "pika" },
            { "age" : "13" }
            ]

        result = await collection.insert_many(document_list)
        print(result.acknowledged)
        '''

        #Updating a value
        '''
        query_filter = { "age" : "13" }
        update_operation = { "$set" : 
             { "name" : "ginyu" }
                            }
        result = await collection.update_one(query_filter, update_operation)

        print(result.modified_count)
        '''
        #Removing one value
        '''
        query_filter = { "age" : "13" }
        replace_document = { "name" : "replaced" }

        result = await collection.replace_one(query_filter, replace_document)

        print(result.modified_count)
        '''
        #Deleting one value 
        '''
        query_filter = { "name" : "pika" }

        result = await collection.delete_one(query_filter)
        print(result.deleted_count)
        '''

        #Find one value 
        results = await collection.find_one({ "name" : "jeff" })
        print(results)

        #Count documents in a collection
        count = await collection.count_documents({})
        print(count)

        #Getting distinct values
        results = await collection.distinct("name")

        for document in results:
            print(document) 
        # end example code here

        await client.close()

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

asyncio.run(main())

""""

name
"Mercedes Tyler"
email
"mercedes_tyler@fakegmail.com"
movie_id
573a1390f29313caabcd4323
text
"Eius veritatis vero facilis quaerat fuga temporibus. Praesentium exped…"


"""