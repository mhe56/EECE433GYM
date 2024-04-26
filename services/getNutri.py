import psycopg2
from psycopg2 import Error
from helper_functions import query_sql
import psycopg2



def getNutri():
    return query_sql("SELECT Nutritionist.ID, Nutritionist.Name AS Nutritionist_Name, Nutritionist.Branch_ID, Branch.location AS Branch_Name FROM Nutritionist JOIN Branch ON Nutritionist.Branch_ID = Branch.ID;")

def getNutriPlans():
    query = """
            SELECT 
                sub.Nutritionist_ID, 
                sub.Name AS Nutritionist_Name, 
                sub.Plan_ID, 
                sub.Description AS Plan_Description, 
                sub.Member_Count
            FROM (
                SELECT 
                    n.ID AS Nutritionist_ID, 
                    n.Name, 
                    p.ID AS Plan_ID, 
                    p.Description, 
                    COUNT(m.ID) AS Member_Count,
                    RANK() OVER (PARTITION BY n.ID ORDER BY COUNT(m.ID) DESC) AS rank
                FROM 
                    Nutritionist n
                JOIN 
                    Plan p ON n.ID = p.Nutritionist_ID
                LEFT JOIN 
                    Member m ON p.ID = m.Plan_ID
                GROUP BY 
                    n.ID, n.Name, p.ID, p.Description
            ) sub
            WHERE 
                sub.rank = 1;
            """
    return query_sql(query)


def getNutritionistInfo(ID):
    Plans = query_sql(f"SELECT COUNT(*) AS num_plans FROM Plan WHERE Nutritionist_ID = {ID};")
    MemberAppts = query_sql(f"SELECT COUNT(*) AS num_appointments FROM Reserve_Appointment WHERE Nutritionist_ID = {ID};")
    MembersServed = query_sql(f"SELECT COUNT(DISTINCT Member_ID) AS num_members FROM Reserve_Appointment WHERE Nutritionist_ID = {ID};")
    Nutr = query_sql(f"SELECT ID, name, Branch_ID FROM Nutritionist WHERE ID = {ID};")
    
    # Handle potential None values
    Plans_count = Plans[0][0] if Plans else None
    MemberAppts_count = MemberAppts[0][0] if MemberAppts else None
    MembersServed_count = MembersServed[0][0] if MembersServed else None
    Nutr_info = Nutr[0] if Nutr else (None, None, None)  # Assuming columns 1 to 3 contain relevant info
    
    return list(Nutr_info) + [Plans_count, MemberAppts_count, MembersServed_count]

def insert_nutri(id,nm,bid):
    query = f"INSERT INTO nutritionist (ID, Name, Branch_ID) VALUES ({id}, '{nm}', {bid});"
    x = query_sql(query, insert=True)
    print(x)
    return x