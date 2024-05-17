from .. import model
from redis import ConnectionError as redis_exception

def test_create():
    try:
        user = model.User.create(name="John Doe", gender="M", avatar="https://example.com/avatar.jpg", details="RAS")
        assert 'id' in user.__dict__ and user.name == "John Doe" and user.gender == "M" and user.avatar == "https://example.com/avatar.jpg" and user.details == "RAS"
    except redis_exception:
        pass

def test_read():
    try:
        user = model.User.create(name="John Doe", gender="M", avatar="https://example.com/avatar.jpg", details="RAS")
        user_read = model.User.read(user.id)
        assert 'id' in user_read.__dict__ and user_read.name == "John Doe" and user_read.gender == "M" and user_read.avatar == "https://example.com/avatar.jpg" and user_read.details == "RAS"
    except redis_exception:
        pass

def test_badread():
    try:
        id = "bad_id"
        user_read = model.User.read(id)
        assert user_read == f"Utilisateur avec l'id {id} non trouve"
    except redis_exception:
        pass

def test_update():
    try:
        user = model.User.create(name="John Doe", gender="M", avatar="https://example.com/avatar.jpg", details="RAS")
        user = model.User.update(user.id, {'details': 'Some details'})
        assert user.details == "Some details"
    except redis_exception:
        pass

def test_badupdate():
    try:
        user = model.User.create(name="John Doe", gender="M", avatar="https://example.com/avatar.jpg", details="RAS")
        msg = model.User.update(user.id, {'bad_attribute': 'Some data'})
        assert msg == f"Erreur format de la requete: bad_attribute n'est pas un attribut valide pour un utilisateur"
    except redis_exception:
        pass

def test_delete():
    try:
        user = model.User.create(name="John Doe", gender="M", avatar="https://example.com/avatar.jpg", details="RAS")
        msg = model.User.delete(user.id)
        assert msg == f"Utilisateur avec l'id {user.id} supprime"
    except redis_exception:
        pass
