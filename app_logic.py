import mysql.connector


def get_info(search_query):
    """Connects to the ensembl database
     and retrieves data with a mySQL query

    :param search_query: A string with the seargh query
        used to filter the results
    :return result: A list with all the retrieved data from
        the ensemble database
    """
    result = list()
    conn = mysql.connector.connect(host='ensembldb.ensembl.org',
                                   user='anonymous',
                                   db='homo_sapiens_core_95_38')
    cursor = conn.cursor()
    cursor.execute("select description from gene where description is not null"
                   " and length(description) > 2 and description like '%"
                   + search_query + "%'order by description")
    for row in cursor:
        result.append(row[0])
    conn.close()
    return result
