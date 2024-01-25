#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    module_name = dir(hidden_4)

    for i in range(len(module_name)):
        if module_name[i][:2] != '__':
            print(module_name[i])
