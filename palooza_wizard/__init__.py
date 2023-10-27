import palooza_wizard.utils.files as files
import palooza_wizard.constants as constants

for folder in constants.FOLDERS:
    files.create_folder_if_not_exists(folder)