import requests
import pytest

host = 'https://pokemonbattle.me:9104'
def test_status_code():
      answer = requests.get(f'{host}/trainers')
      assert answer.status_code == 200

@pytest.mark.parametrize('key, value', [('trainer_name', 'Max'), 
                                         ('city', 'Moscow')])

def test_part_of_answer(key, value):
      answer_body = requests.get(f'{host}/trainers', 
                                 params = {'trainer_id' : 4617})                       
      assert answer_body.json()[key] == value
