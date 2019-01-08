#!/usr/bin/env python

# Copyright 2019 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import logging
import os
import requests
import sys
import traceback

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


# widget status api-endpoint configuration
api_config = {"GCP_REGION" : os.getenv('GCP_REGION'), 
              "PROJECT_ID" : os.getenv('DEVSHELL_PROJECT_ID'),
              "PUBLISH_FUNCTION" : "publish_widget" }


WIDGET_PUBLISH_URL = "https://{GCP_REGION}-{PROJECT_ID}.cloudfunctions.net/function-{PUBLISH_FUNCTION}".format(**api_config)
  

def submit_widgets(widget_count=1):
    """Function to create a widget_count of widget processing requests
    Args:
         widget_count (int): The number of widgets to publish
    """

    try: 

        widget_submit_time = datetime.datetime.utcnow().isoformat()
        for i in range(widget_count) :
            widget_content = \
                "Widget {} submitted for processing at {}".format(str(i+1), widget_submit_time)
            r = requests.post(url=WIDGET_PUBLISH_URL, 
                              data={"widget_content" :  widget_content})

            logging.info(r.text)

    except :
        exc_type, exc_value, exc_traceback = sys.exc_info()
        
        logging.error(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))

if __name__ == "__main__":

    widget_count = 1
    if len(sys.argv) == 2 :
        widget_count = int(sys.argv[1])

    submit_widgets(widget_count)
