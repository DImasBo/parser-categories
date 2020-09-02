import logging
logger_root = logging.getLogger(__name__)
c_handler = logging.StreamHandler()
c_handler.setFormatter(logging.Formatter("%(levelname)s: %(asctime)s | %(message)s"))
c_handler.setLevel(logging.DEBUG)
logger_root.addHandler(c_handler)

USER_AGENT_FILE = 'bin/user-agent.txt'
LUXEL_SITE = 'https://luxel.ua/'

LUXEL_CATEGORIES = [
	'https://luxel.ua/svetodiodnie--led--lampi/led_lampy',
	'https://luxel.ua/svetodiodnoe--led--fitoosveshhenie/led-fitolampi',
	'https://luxel.ua/svetodiodnoe--led--osveshhenie/led-t5',
	'https://luxel.ua/svetodiodnoe--led--osveshhenie/led-svetilniki-s-pultom-upravlenija',
	'https://luxel.ua/svetodiodnoe--led--osveshhenie/led_paneli',
	'https://luxel.ua/svetodiodnoe--led--osveshhenie/led-nastolnie-lampi'
]

LUXEL_RESULT_FILE = "result/result.csv"

LUXEL_CURRENCY_ID_DEFAULT = "UAH"
LUXEL_CATEGORY_ID_DEFAULT = "1"

LUXEL_FLOWS = 10
