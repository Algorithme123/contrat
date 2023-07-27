# controllers/default.py
import os

# List all clients
def liste_clients():
    clients = db().select(db.Client.ALL)
    return dict(clients=clients)

# Create a new client
def create_client():
    form = SQLFORM(db.Client)
    if form.process().accepted:
        session.flash = 'Client créé'
        redirect(URL('default', 'liste_clients'))
    return dict(form=form)

# Update a client
def edit_client():
    client = db.Client(request.args(0)) or redirect(URL('default', 'liste_clients'))
    form = SQLFORM(db.Client, client)
    if form.process().accepted:
        redirect(URL('default', 'liste_clients'))
    return dict(form=form)

# Delete a client
def delete_client():
    client_id = request.vars.id
    client = db.Client(client_id)
    if not client:
        raise HTTP(404, "Le client n'existe pas")
    db(db.Client.id == client_id).delete()
    session.flash = 'Client supprimé'
    redirect(URL('default', 'liste_clients'))
