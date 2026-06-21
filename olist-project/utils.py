

def count_docs(db, collection, doc_name, operator, conditions):
    """
    Counts the specified values in a given collection, based on given conditions, and calculates the proportion of the entire collection that these documents represent.
    """
    doc_count = db[collection].count_documents({operator: [{doc_name: conditions[0]}, {doc_name: conditions[1]}]})
    proportion = doc_count / db[collection].count_documents({})
    return doc_count, proportion