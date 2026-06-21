

def count_docs(db, collection, doc_name):
    """
    Counts the missing values in a given collection and calculates the proportion of the entire collection that these documents represent.
    """
    doc_count = db[collection].count_documents({"$or": [{doc_name: {"$in": [None, ""]}}, {doc_name: {"$exists": False}}]})
    proportion = doc_count / db[collection].count_documents({})
    return doc_count, proportion