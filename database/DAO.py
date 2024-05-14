from database.DB_connect import DBConnect
from model.paese import Paese

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_all_vertici(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT c1.StateAbb, c1.CCode, c1.StateNme
                    FROM contiguity AS ct
                    JOIN country c1 ON ct.state1no = c1.CCode
                    WHERE ct.year <= %s
                    ORDER BY c1.StateNme
                    """

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(
                Paese(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_archi(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT ct.state1no, ct.state2no
                            FROM contiguity AS ct
                            WHERE ct.year <= %s
                            AND ct.conttype = 1"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(
                (row['state1no'], row['state2no']))

        print(result)

        cursor.close()
        conn.close()
        return result





