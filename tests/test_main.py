from typer.testing import CliRunner

from sav_to_excel.main import app

runner = CliRunner()


def test_transformation():
    command_name = "transform_sav_to_excel"
    args = [command_name, "accidents.sav", "accidents.xlsx"]

    result = runner.invoke(app, args)


