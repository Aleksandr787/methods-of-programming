import pytest
import os
import tempfile
from laba_number_3.database.database import Database, EmployeeTable, DepartmentTable


@pytest.fixture
def temp_employee_file():
    """ Создаем временный файл для таблицы рабочих """
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    yield temp_file.name
    os.remove(temp_file.name)

@pytest.fixture
def temp_department_file():
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    yield temp_file.name
    os.remove(temp_file.name)

#Пример, как используются фикстуры
@pytest.fixture
def database(temp_employee_file, temp_department_file):
    """ Данная фикстура задает БД и определяет таблицы. """
    db = Database()

    # Используем временные файлы для тестирования файлового ввода-вывода в EmployeeTable и DepartmentTable
    employee_table = EmployeeTable()
    employee_table.FILE_PATH = temp_employee_file
    department_table = DepartmentTable()
    department_table.FILE_PATH = temp_department_file

    db.register_table("employees", employee_table)
    db.register_table("departments", department_table)

    return db

def test_insert_employee(database):
    # Добавляем сотрудников с department_id
    database.insert("employees", "1 Alice 30 70000 10")
    database.insert("employees", "2 Bob 28 60000 20")
    database.insert("employees", "3 Carol 25 50000 10")

    employee_data = database.select("employees", 1, 3)
    assert len(employee_data) == 3
    assert employee_data[0] == {'id': '1', 'name': 'Alice', 'age': '30', 'salary': '70000', 'department_id': '10'}
    assert employee_data[1] == {'id': '2', 'name': 'Bob', 'age': '28', 'salary': '60000', 'department_id': '20'}
    assert employee_data[2] == {'id': '3', 'name': 'Carol', 'age': '25', 'salary': '50000', 'department_id': '10'}

def test_unique_employee(database):
    database.insert("employees", "1 Alice 30 70000 10")
    with pytest.raises(ValueError):
        database.insert("employees", "1 Alice 30 70000 10")  # Дублирующий id+department_id
    database.insert("employees", "1 Alice 30 70000 11")  # Разный department_id — ок

def test_insert_department(database):
    database.insert("departments", "10 IT")
    database.insert("departments", "20 HR")
    database.insert("departments", "30 IT")
    departments = database.select("departments", "IT")
    assert len(departments) == 2
    assert departments[0]['department_name'] == 'IT'
    assert departments[1]['department_name'] == 'IT'

def test_unique_department(database):
    database.insert("departments", "10 IT")
    with pytest.raises(ValueError):
        database.insert("departments", "10 HR")  # Дублирующий id
    database.insert("departments", "11 HR")  # Разный id — ок

def test_join_employees_departments(database):
    database.insert("departments", "10 IT")
    database.insert("departments", "20 HR")
    database.insert("employees", "1 Alice 30 70000 10")
    database.insert("employees", "2 Bob 28 60000 20")
    database.insert("employees", "3 Carol 25 50000 10")
    joined = database.join("employees", "departments")
    assert len(joined) == 3
    # Проверяем, что у Alice и Carol department_name == IT, у Bob == HR
    names = {row['name']: row['department_department_name'] for row in joined}
    assert names['Alice'] == 'IT'
    assert names['Carol'] == 'IT'
    assert names['Bob'] == 'HR'

def test_csv_files_deleted(temp_employee_file, temp_department_file):
    # Проверяем, что после удаления файлов они действительно удалены
    assert not os.path.exists(temp_employee_file)
    assert not os.path.exists(temp_department_file)