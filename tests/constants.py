"""
Copyright 2022 Rob Weber

This file is part of omni-epd

omni-epd is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
import os.path

GOOD_EPD_NAME = "omni_epd.mock"  # this should always be a valid EPD
BAD_EPD_NAME = "omni_epd.bad"  # this is not a valid EPD

BAD_CONFIG_FILE = 'bad_conf.ini'  # name of invalid configuration file
ALL_IMAGE_OPTIONS = "all_options.ini"  # ini file that attempt to run all base options

# Testing Images
GALAXY_IMAGE = os.path.join(os.getcwd(), "examples", "PIA03519_small.jpg")
