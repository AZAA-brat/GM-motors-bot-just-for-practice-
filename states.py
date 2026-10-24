from aiogram.fsm.state import StatesGroup, State


class Review(StatesGroup):
    rating = State()
    message = State()

class Maintenance(StatesGroup):
    car = State()
    problem = State()

class TestDrive(StatesGroup):
    name = State()
    phone = State()
    car = State()
    office = State()
    email = State()

class Purchase(StatesGroup):
    name = State()
    phone = State()
    car = State()
    configuration = State()
    email = State()

class Admin(StatesGroup):
    new_car = State()
    update_car = State()
    update_configuration = State()
