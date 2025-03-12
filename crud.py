from database import get_db_connection

def create_ticket(title, description, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tickets (title, description, status) VALUES (?, ?, ?)", 
                   (title, description, status))
    conn.commit()
    ticket_id = cursor.lastrowid
    conn.close()
    return ticket_id

def get_all_tickets():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()
    conn.close()
    return [{"id": t[0], "title": t[1], "description": t[2], "status": t[3]} for t in tickets]

def get_ticket(ticket_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,))
    ticket = cursor.fetchone()
    conn.close()
    return ticket

def update_ticket(ticket_id, title, description, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tickets SET title = ?, description = ?, status = ? WHERE id = ?", 
                   (title, description, status, ticket_id))
    conn.commit()
    rows_updated = cursor.rowcount
    conn.close()
    return rows_updated

def delete_ticket(ticket_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
    conn.commit()
    rows_deleted = cursor.rowcount
    conn.close()
    return rows_deleted
