import pytest
import subprocess 
import rps
import sys 

def test_rock_is_valid_play():
    assert rps.is_valid_play("rock") is True

def test_paper_is_valid_play():
    assert rps.is_valid_play("paper") is True

def test_scissors_is_valid_play():
    assert rps.is_valid_play("scissors") is True

def test_invalid_play():
    assert rps.is_valid_play("kdjfla") is False

def test_empty_play():
    assert rps.is_valid_play("") is False
    

def test_random_play_is_valid():
    for _ in range(100):
        play = rps.random_play()
        assert rps.is_valid_play(play)

def test_random_play_is_fairish():
    """ This should work in most universes! """ 
    plays = [ rps.random_play() for _ in range(1000)  ]
    assert plays.count('rock') > 100
    assert plays.count('paper') > 100
    assert plays.count('scissors') > 100 


def test_paper_beats_rock():
    assert rps.determine_game_result('paper', 'rock') == 'human'
    assert rps.determine_game_result('rock', 'paper') == 'computer'

def test_rock_beats_scissors():
    assert rps.determine_game_result('rock', 'scissors') == 'human'
    assert rps.determine_game_result('scissors', 'rock') == 'computer'

def test_scissor_beats_paper():
    assert rps.determine_game_result('scissors', 'paper') == 'human'
    assert rps.determine_game_result('paper', 'scissors') == 'computer'

@pytest.mark.parametrize('play', ['paper', 'rock', 'scissors'])    
def test_tie(play):
    assert rps.determine_game_result(play, play) == 'tie'




def input_fake(fake):
    def input_fake_(prompt):
        print(prompt)
        return fake
    return input_fake_
    

#@pytest.fixture%
#def faked_input_rock(monkeypatch):
#    monkeypatch.setattr()


#def test_whole_game(capsys, monkeypatch):
    # monkeypatch.setattr('builtins.input', input_fake_rock)

@pytest.mark.parametrize('play', ['rock', 'paper', 'scissors'])    
def test_whole_game(capsys, play):
    rps.main(input=input_fake(play))
    captured = capsys.readouterr()
    assert 'rock, paper, or scissors?' in captured.out 
    assert ('computer wins' in captured.out) or ('human wins' in captured.out) or ('It\'s a tie!' in captured.out)

    
def test_game_asks_again_if_wrong_input():
    cp = subprocess.run([sys.executable, 'rps.py'],
                        input='asdf\nrock',
                        encoding='utf-8',
                        stdout=subprocess.PIPE)
    assert cp.stdout.count('rock, paper, or scissors?') == 2


def fake_random_play(play):
    def fake_random_play_():
        return play
    return fake_random_play_ 

@pytest.mark.parametrize('play', ['rock', 'paper', 'scissors'])
def test_whole_game_tie(capsys, monkeypatch, play):
    monkeypatch.setattr('rps.random_play', fake_random_play(play))
    
    rps.main(input=input_fake(play))
    captured = capsys.readouterr()
    assert 'It\'s a tie!' in captured.out 

games = [('paper', 'scissors', 'computer'),
         ('paper', 'rock', 'human'),
         ('rock', 'scissors', 'human'),
         ('rock', 'paper', 'computer'),
         ('scissors', 'paper', 'human'),
         ('scissors', 'rock', 'computer')]

@pytest.mark.parametrize('game', games)
def test_whole_game_wins(capsys, monkeypatch, game):
    monkeypatch.setattr('rps.random_play', fake_random_play(game[1]))

    rps.main(input=input_fake(game[0]))
    captured = capsys.readouterr()
    assert game[2] in captured.out

    
