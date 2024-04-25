import psycopg2
from psycopg2 import Error
from helper_functions import query_sql
import psycopg2

def getCoaches():
    return query_sql("SELECT Coach.ID, Coach.Name AS Coach_Name, Coach.Age, Coach.Years_of_Experience, Branch.location AS Branch_Name FROM Coach JOIN Branch ON Coach.Branch_ID = Branch.ID;")

def getCoachesbyYears(years):
    query = "SELECT ID, Name, Age, Years_of_Experience FROM Coach WHERE Years_of_Experience > %s ORDER BY Years_of_Experience DESC"
    print (query_sql(query, (years,)))
    return query_sql(query, (years,))

def getCoachPlans():
    query = """
            SELECT 
                sub.Coach_ID, 
                sub.Name AS Coach_Name, 
                sub.Plan_ID, 
                sub.Description AS Plan_Description, 
                sub.Member_Count
            FROM (
                SELECT 
                    c.ID AS Coach_ID, 
                    c.Name, 
                    p.ID AS Plan_ID, 
                    p.Description, 
                    COUNT(m.ID) AS Member_Count,
                    RANK() OVER (PARTITION BY c.ID ORDER BY COUNT(m.ID) DESC) AS rank
                FROM 
                    Coach c
                JOIN 
                    Plan p ON c.ID = p.Coach_ID
                LEFT JOIN 
                    Member m ON p.ID = m.Plan_ID
                GROUP BY 
                    c.ID, c.Name, p.ID, p.Description
            ) sub
            WHERE 
                sub.rank = 1;
            """
    return query_sql(query)

def getCoachInfo(ID):
    Plans = query_sql("SELECT COUNT(*) AS num_plans FROM Plan WHERE Coach_ID = %s;", (ID,))
    TotalPt = query_sql("SELECT COUNT(*) AS num_sessions FROM Reserve_PT WHERE Coach_ID = %s;", (ID,))
    Dep = query_sql("SELECT Dependents.Name, Dependents.Relationship FROM Dependents JOIN Coach ON Dependents.Coach_ID = Coach.ID WHERE Coach.ID = %s;", (ID,))
    Coach = query_sql("SELECT * FROM Coach WHERE ID = %s;", (ID,))
    
    # Handle potential None values
    Plans_count = Plans[0][0] if Plans else None
    TotalPt_count = TotalPt[0][0] if TotalPt else None
    Dep_info = Dep if Dep else None
    Coach_info = Coach[0][1:5] if Coach else (None, None, None, None)  # Assuming columns 1 to 4 contain relevant info
    
    return list(Coach_info) + [Plans_count, TotalPt_count, Dep_info]


print(getCoachInfo(201))