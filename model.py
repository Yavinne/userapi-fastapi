from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base
import redis

Base = declarative_base()
db_url = "sqlite:///./userapi.db"

# Tantative de connexion au serveur redis
# L'exécution doit poursuivre en cas d'inaccessibilité du serveur
try:
  redis_client = redis.Redis(host='redis', port=6379, db=0)
except:
  redis_client = None

engine = create_engine(db_url)
Base.metadata.create_all(bind=engine)

class User(Base):
  """
  Classe représentant un utilisateur
  Hérite de la classe `Base` de l'ORM SQLAlchemy

  Attributs:
    id (int): Identifiant unique de l'utilisateur (clé primaire).
    name (str): Nom de l'utilisateur.
    gender (str): Genre de l'utilisateur.
    avatar (str): URL ou chemin de l'image d'avatar de l'utilisateur.
    details (str): Détails supplémentaires sur l'utilisateur.
    
    Tous les attributs sont obligatoires
  """
  __tablename__ = 'Users'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  gender = Column(String)
  avatar = Column(String)
  details = Column(String)

  @staticmethod
  def create(name: str, gender: String, avatar: String, details: String):
    """
    Méthode pour créer un utilisateur

    Args:
      name (str): Nom de l'utilisateur.
      gender (str): Genre de l'utilisateur.
      avatar (str): URL ou chemin de l'image d'avatar de l'utilisateur.
      details (str): Détails supplémentaires sur l'utilisateur.

    Retour:
      User: L'objet utilisateur créé, ou un message d'erreur si la création a échoué.
    """
    user = User(id=None, name=name, gender=gender, avatar=avatar, details=details)
    session = Session(bind=engine)
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()
    if user.id:
      try:
        # Tentative de mise en cache des données de l'utilisateur
        redis_client.set(f"user{user.id}", user.__str__(), 3600)
      except:
        pass
      return user
    else:
      return f"Impossible de creer l'utilisateur {name}"

  @staticmethod
  def read(user_id: int):
    """
    Méthode pour lire un utilisateur

    Args:
      user_id (int): Identifiant unique de l'utilisateur à récupérer.

    Retour:
      User: L'objet utilisateur récupéré, ou un message d'erreur si l'utilisateur n'est pas trouvé.
    """
    try:
      # Tentative de lecture de l'utilisateur depuis le cache
      res = eval(redis_client.get(f"user{user_id}")) # La valeur stockée doit être évaluée comme un dictionnaire
      user = User(res['id'], res['name'], res['gender'], res['avatar'], res['details'])
      return user
    except:
      session = Session(bind=engine)
      user = session.query(User).filter_by(id=user_id).first()
      try:
        # Tentative de mise en cache des données lues
        redis_client.set(f"user{user.id}", user.__str__(), 3600)
      except:
        pass
      session.close()
      if not user:
        return f"Utilisateur avec l'id {user_id} non trouve"
      return user

  @staticmethod
  def update(user_id: int, new_data: dict):
    """
    Méthode pour mettre à jour un utilisateur existant

    Args:
      user_id (int): Identifiant unique de l'utilisateur à mettre à jour.
      new_data (dict): Dictionnaire contenant des paires clé-valeur représentant les nouvelles données utilisateur.
        - Les clés doivent être des attributs valides de la classe `User`.

    Retour:
      User: L'objet utilisateur mis à jour, ou un message d'erreur si la mise à jour a échoué.
    """
    session = Session(bind=engine)
    user = session.query(User).filter_by(id=user_id).first()
    if user:
      for key, value in new_data.items():
        if hasattr(user, key):
          setattr(user, key, value)
        else:
          return f"Erreur format de la requete: {key} n'est pas un attribut valide pour un utilisateur"
      session.commit()
      user = session.query(User).filter_by(id=user_id).first()
      session.close()
      # Tentative de mise à jour du cache avec les nouvelles données
      try:
        redis_client.set(f"user{user_id}", user.__str__(), 3600)
      except:
        pass

      return user
    else:
      return f"Utilisateur avec l'id {user_id} non trouve"

  @staticmethod
  def delete(user_id: int):
    """
    Méthode pour supprimer un utilisateur

    Args:
      user_id (int): Identifiant unique de l'utilisateur à supprimer.

    Retour:
      str: Message de confirmation si l'utilisateur a été supprimé, ou un message d'erreur s'il n'a pas été retrouvé.
    """
    session = Session(bind=engine)
    user = session.query(User).filter_by(id=user_id).first()
    if user:
      session.delete(user)
      session.commit()
      # Tentative de retrait du cache
      try:
        redis_client.delete(f"user{user_id}")
      except:
        pass
      
    else:
      return f"Utilisateur avec l'id {user_id} non trouve"
    session.close()
    return f"Utilisateur avec l'id {user_id} supprime"
  
  def __init__(self, id, name, gender, avatar, details):
    self.id = id
    self.name = name
    self.avatar = avatar
    self.gender = gender
    self.details = details
  
  def __str__(self):
    val = ""
    for key, value in self.__dict__.items():
      if not key.startswith("_"):
        val += f"'{key}':'{value}', "
    val = "{" + val[:-2] + "}" # retrait des deux derniers caractères ", " et ajout d'accolades
    return val

