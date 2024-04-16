# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2023-2024 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module implements a Mech tool for binary predictions."""

from litellm import completion
from olas_prediction.schemas import InputSchema
from olas_prediction.utils import get_logger
import os
import re
from typing import Any, Dict, Optional, Tuple
import yaml 

logger = get_logger(__name__)

def extract_json_string(text):
    # This regex looks for triple backticks, captures everything in between until it finds another set of triple backticks.
    pattern = r"(\{[^}]*\})"
    matches = re.findall(pattern, text)
    return matches[0].replace("json", "")

def run(inputs: InputSchema, cfg) -> Tuple[str, Optional[str], Optional[Dict[str, Any]], Any]:
    """Run the task"""

    prediction_prompt = cfg["inputs"]["prediction_prompt"].format(question=inputs.question)
    messages = [
        {"role": "system", "content": cfg["inputs"]["system_message"]},
        {"role": "user", "content": prediction_prompt},
    ]
    response = completion(
        model=cfg["models"]["ollama"]["model"],
        messages=messages,
        temperature=cfg["models"]["ollama"]["temperature"],
        max_tokens=cfg["models"]["ollama"]["max_tokens"],
        api_base=cfg["models"]["ollama"]["api_base"],
    )
    extracted_block = extract_json_string(response.choices[0].message["content"])
    return extracted_block, prediction_prompt
