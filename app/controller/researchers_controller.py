from app.persistance.repository import researcher_repo

def get_all_researchers():
    return researcher_repo.get_all_researchers()
