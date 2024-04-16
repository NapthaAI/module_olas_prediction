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

    question = "Will there be an initial public offering on either the Shanghai Stock Exchange or the Shenzhen Stock Exchange before 1 January 2016?"

    inputs = InputSchema(
        question = question,
    )

    run_tool(inputs)