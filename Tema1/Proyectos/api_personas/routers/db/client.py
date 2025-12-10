from pymongo import MongoClient

router = APIRouter(prefix="/moviles", tags=["moviles"])

db_client = MongoClient()