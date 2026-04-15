import pytest

from youtube_metrics.readers import FileReader


@pytest.fixture
def csv_header():
    return "title,ctr,retention_rate,views,likes,avg_watch_time\n"


@pytest.fixture
def csv_valid_row1():
    return "Я бросил IT и стал фермером,18.2,35,45200,1240,4.2\n"


@pytest.fixture
def csv_valid_row2():
    return "Как я спал по 4 часа и ничего не понял,22.5,28,128700,3150,3.1\n"


@pytest.fixture
def csv_invalid_row():
    return "Я переписал всё на Go и пожалел,22.5z,28,128700,3150,3.1\n"


def test_read_single_csv_file(tmp_path, csv_header, csv_valid_row1):
    file = tmp_path / "file.csv"
    
    file.write_text(csv_header + csv_valid_row1, encoding="utf-8")

    result = FileReader.read_csv_files([file])

    assert result[0]["title"] == "Я бросил IT и стал фермером"
    assert result[0]["ctr"] == 18.2
    assert result[0]["retention_rate"] == 35
    assert result[0]["views"] == 45200
    assert result[0]["likes"] == 1240
    assert result[0]["avg_watch_time"] == 4.2


def test_read_multiple_csv_files(tmp_path, csv_header, csv_valid_row1, csv_valid_row2):
    file1 = tmp_path / "file1.csv"
    file2 = tmp_path / "file2.csv"

    file1.write_text(csv_header + csv_valid_row1, encoding="utf-8")
    file2.write_text(csv_header + csv_valid_row2, encoding="utf-8")

    result = FileReader.read_csv_files([file1, file2])

    assert result[0]["title"] == "Я бросил IT и стал фермером"
    assert result[0]["ctr"] == 18.2
    assert result[0]["retention_rate"] == 35
    assert result[0]["views"] == 45200
    assert result[0]["likes"] == 1240
    assert result[0]["avg_watch_time"] == 4.2

    assert result[1]["title"] == "Как я спал по 4 часа и ничего не понял"
    assert result[1]["ctr"] == 22.5
    assert result[1]["retention_rate"] == 28
    assert result[1]["views"] == 128700
    assert result[1]["likes"] == 3150
    assert result[1]["avg_watch_time"] == 3.1


def test_read_csv_files_raises_file_not_found():
    with pytest.raises(FileNotFoundError):
        FileReader.read_csv_files(["not_found.csv"])


def test_read_csv_files_raises_file_value_error(tmp_path, csv_header, csv_invalid_row):
    with pytest.raises(ValueError):
        file = tmp_path / "file.csv"
        
        file.write_text(csv_header + csv_invalid_row, encoding="utf-8")

        FileReader.read_csv_files([file])
