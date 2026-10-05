from storage import ScoreBoard
def test_a_new_scoreboard_is_empty(tmp_path)->None:
    board= ScoreBoard(str(tmp_path/"leaderboared.json"))
    assert board.is_empty()
