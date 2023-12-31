def convertPydanticToJson(results):
    column_names = results.keys()
    
    final_result = [
        dict(zip(column_names, result))
        for result in results
    ]

    return final_result