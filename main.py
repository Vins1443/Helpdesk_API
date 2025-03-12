from fastapi import FastAPI, HTTPException
from models import Ticket
import crud

app = FastAPI()

@app.post("/tickets/")
def create_ticket(ticket: Ticket):
    ticket_id = crud.create_ticket(ticket.title, ticket.description, ticket.status)
    return {"id": ticket_id, **ticket.dict()}

@app.get("/tickets/")
def get_tickets():
    return crud.get_all_tickets()

@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    ticket = crud.get_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"id": ticket[0], "title": ticket[1], "description": ticket[2], "status": ticket[3]}

@app.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, ticket: Ticket):
    rows_updated = crud.update_ticket(ticket_id, ticket.title, ticket.description, ticket.status)
    if rows_updated == 0:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"id": ticket_id, **ticket.dict()}

@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    rows_deleted = crud.delete_ticket(ticket_id)
    if rows_deleted == 0:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"message": "Ticket deleted successfully"}

