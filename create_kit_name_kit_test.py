import sender_stand_request
import data

# Функция для изменения значения в параметре name в теле запроса
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Функция для позитивной проверки
def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_kits(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == get_kit_body(name)["name"]

# Функция негативной проверки
def negative_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_kits(kit_body)

    assert kit_response.status_code == 400

# Функция негативной проверки с пустым запросом
def negative_assert_empty(kit_body):
        kit_response = sender_stand_request.post_kits(kit_body)

        assert kit_response.status_code == 400

# 1) Допустимое количество символов (1)
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert('а')

# 2) Допустимое количество символов (511)
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')

# 3) Количество символов меньше допустимого (0)
def test_create_kit_0_letter_in_name_get_success_response():
    negative_assert('')

# 4) Количество символов больше допустимого (512)
def test_create_kit_512_letter_in_name_get_success_response():
    negative_assert('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')

# 5) Разрешены английские буквы
def test_create_kit_ENG_letter_in_name_get_success_response():
    positive_assert('QWErty')

# 6) Разрешены русские буквы
def test_create_kit_RUS_letter_in_name_get_success_response():
    positive_assert('Мария')

# 7) Разрешены спецсимволы
def test_create_kit_spec_char_in_name_get_success_response():
    positive_assert('№%@')

# 8) Разрешены пробелы
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert('Человек и КО ')

# 9) Разрешены цифры
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert('123')

# 10) Параметр не передан в запросе
def test_create_kit_no_parameter_in_name_get_success_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_empty(kit_body)

# 11) Передан другой тип параметра (число)
def test_create_kit_int_in_name_get_success_response():
    negative_assert(123)