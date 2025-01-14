from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)
    cards = db.relationship("Card", backref="board")

    def to_dict(self):
        board = {
            "id" : self.board_id,
            "title" : self.title,
            "owner" : self.owner
        }

        return board

    @classmethod
    def from_dict(cls, request_body):
        board = Board(
            title=request_body["title"],
            owner=request_body["owner"]
        )

        return board
