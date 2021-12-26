from app.persistance.models import Researchers

def get_all_researchers():
    return Researchers.all()
