import os
import yaml
import argparse
import logging

def read_params(config_path):
    with open(config_path) as yaml_file:
        print("-----------------yaml_file-------------------")
        print(yaml_file)
        config = yaml.safe_load(yaml_file)
    return config

def main(config_path, datasource):
    config = read_params(config_path)
    print(config)


if __name__ =="__main__":

    args = argparse.ArgumentParser()
    config_path = os.path.join("config", "param.yaml")
    args.add_argument("--config", default=config_path)
    args.add_argument("--datasource", default=None)

    parsed_args = args.parse_args()
    print(parsed_args.config, parsed_args.datasource)
    main(config_path = parsed_args.config, datasource=parsed_args.datasource)

