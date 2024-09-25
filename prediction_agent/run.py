from litellm import completion
from prediction_agent.schemas import InputSchema
from prediction_agent.utils import get_logger
import re
from typing import Any, Dict, Optional, Tuple

logger = get_logger(__name__)

def extract_json_string(text):
    # This regex looks for triple backticks, captures everything in between until it finds another set of triple backticks.
    pattern = r"(\{[^}]*\})"
    matches = re.findall(pattern, text)
    return matches[0].replace("json", "")

def run(inputs: InputSchema, cfg) -> Tuple[str, Optional[str], Optional[Dict[str, Any]], Any]:
    """Run the task"""

    prediction_prompt = cfg["inputs"]["prediction_prompt"].format(prompt=inputs.prompt)
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
