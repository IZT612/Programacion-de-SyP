from pymongo import MongoClient

router = APIRouter(prefix="/usersdb", tags=["usersdb"])

db_client = MongoClient()