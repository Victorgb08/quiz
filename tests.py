import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_add_multiple_choices():
    question = Question(title='q1')
    question.add_choice('Choice 1', False)
    question.add_choice('Choice 2', True)
    assert len(question.choices) == 2
    assert question.choices[0].text == 'Choice 1'
    assert question.choices[1].text == 'Choice 2'


def test_remove_choice_by_id():
    question = Question(title='q1')
    choice = question.add_choice('Choice 1', False)
    question.remove_choice_by_id(choice.id)
    assert len(question.choices) == 0


def test_remove_all_choices():
    question = Question(title='q1')
    question.add_choice('Choice 1', False)
    question.add_choice('Choice 2', True)
    question.remove_all_choices()
    assert len(question.choices) == 0


def test_set_correct_choices():
    question = Question(title='q1')
    choice1 = question.add_choice('Choice 1', False)
    choice2 = question.add_choice('Choice 2', False)
    question.set_correct_choices([choice2.id])
    assert not choice1.is_correct
    assert choice2.is_correct


def test_select_correct_choices():
    question = Question(title='q1', max_selections=2)
    choice1 = question.add_choice('Choice 1', True)
    choice2 = question.add_choice('Choice 2', False)
    selected = question.select_choices([choice1.id, choice2.id])
    assert selected == [choice1.id]


def test_select_choices_exceeding_max_selections():
    question = Question(title='q1', max_selections=1)
    choice1 = question.add_choice('Choice 1', True)
    choice2 = question.add_choice('Choice 2', False)
    with pytest.raises(Exception):
        question.select_choices([choice1.id, choice2.id])


def test_add_choice_with_empty_text():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.add_choice('', False)


def test_add_choice_with_long_text():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.add_choice('a' * 101, False)


def test_generate_unique_choice_ids():
    question = Question(title='q1')
    choice1 = question.add_choice('Choice 1', False)
    choice2 = question.add_choice('Choice 2', False)
    assert choice1.id != choice2.id


def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question(title='q1', points=0)
    with pytest.raises(Exception):
        Question(title='q1', points=101)