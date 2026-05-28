from pymongo import MongoClient
import time

def main():
    print("Connecting to MongoDB...")
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test_db']
    collection = db['test_collection']

    print("Dropping collection if exists...")
    collection.drop()

    print("Inserting document...")
    doc = {"name": "VisTrails", "type": "Workflow", "score": 100}
    
    start_time = time.time()
    result = collection.insert_one(doc)
    
    print("Finding document...")
    found = collection.find_one({"_id": result.inserted_id})
    print(f"Found: {found}")

    print("Counting documents...")
    count = collection.count_documents({})
    print(f"Total documents: {count}")

    print("Aggregating documents...")
    pipeline = [{"$match": {"type": "Workflow"}}, {"$group": {"_id": "$type", "total": {"$sum": "$score"}}}]
    agg_result = list(collection.aggregate(pipeline))
    print(f"Aggregation result: {agg_result}")
    
    end_time = time.time()
    print(f"MongoDB operations completed in {end_time - start_time:.4f} seconds")

if __name__ == '__main__':
    main()
