#!/usr/bin/env python

import json
import os
from olas_prediction.run import run
from olas_prediction.schemas import InputSchema
import yaml

def run_tool(cfg):
    response = run(cfg)

    result = json.loads(response[0])
    prompt_response = response[1]

    print("Final Prompt: ", prompt_response)
    print("Result: ", result)


if __name__ == "__main__":

    with open("olas_prediction/component.yaml", 'r') as cfg_file:
        cfg = yaml.safe_load(cfg_file)

    question = "Will there be an initial public offering on either the Shanghai Stock Exchange or the Shenzhen Stock Exchange before 1 January 2016?"

    cfg = InputSchema(
        question = question,
        prediction_prompt = cfg["inputs"]["prediction_prompt"],
        system_message = cfg["inputs"]["system_message"],
        model_provider = cfg["models"]["default_model_provider"],
        model = cfg["models"]["ollama"]["model"],
        max_tokens = cfg["models"]["ollama"]["max_tokens"],
        temperature = cfg["models"]["ollama"]["temperature"],
    )

    run_tool(cfg)