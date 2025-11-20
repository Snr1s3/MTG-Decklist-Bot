from pymongo import MongoClient
from ..config import DB_USER, DB_PSSWD, DB_URL
class MongoCRUD:

    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PSSWD}@{DB_URL}")
            cls._instance.db = cls._instance.client["testbottelegram1"]
            cls._instance.collection = cls._instance.db["decklists"]
        return cls._instance

    def create(self,deck_name: str, deck: list[str]):
        partner= False
        commanders= []
        if partner:
            commanders = deck[:2]
            deck = deck[2:]
        else:
            commanders = [deck[0]]
            deck = deck[1:]
        data={
            "deck_name":deck_name,
            "deck_list":{
                "commander":commanders,
                "deck":deck
            }
        }
        result = self._instance.collection.insert_one(data)
        return result.inserted_id
    
    def get_all_decks(self):
        def extract_commander(card_str):
            parts = card_str.split('1 ', 1)
            if len(parts) < 2:
                return card_str
            return parts[1].split('(', 1)[0].strip()
        decks = []
        for doc in self.collection.find({}, {"deck_name": 1, "deck_list.commander": 1, "_id": 0}):
            commanders_raw = doc.get("deck_list", {}).get("commander", [])
            commanders = [extract_commander(c) for c in commanders_raw]
            decks.append({
                "deck_name": doc.get("deck_name", ""),
                "commander": commanders
            })
        return decks