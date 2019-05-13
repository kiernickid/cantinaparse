import json
import sys

def break_list(selector, l, answer, subview_count) :
    for element in l : 
        if isinstance(element, dict) :
            print("-" * subview_count)
            subview_count += 1
            master_parse(selector, element, answer, subview_count)

def master_parse(selector, data, answer, subview_count) :
    curr_keys = data.keys() 
    for key in curr_keys :
        if isinstance(data[key], list) and key == selector: 
            print(" " * subview_count + str(data[key]))
            answer += data[key]
        elif isinstance(data[key], list) : 
            break_list(selector, data[key], answer, subview_count)
        elif isinstance(data[key], dict) : 
            master_parse(selector, data[key], answer, subview_count)
        elif key == selector : 
            print(" " * subview_count + str(data[key]))
            answer.append(data[key])
    return answer
        


def parse_classNames(selector, data, answer) :
     
    print("ANSWER: " + str(answer))
    if selector == "classNames" : 
        print(data)
        print("----------------------")
        if "subviews" in data.keys() :
            if 'classNames' in data.keys() :
                answer += data['classNames']
            for x in data['subviews'] :
                parse_classNames("classNames", x, answer)
            else : 
                return list(set(answer))

def parse_classIdentifier(selector, data, answer) :
    print("ANSWER: " + str(answer))
    if selector == "identifier" : 
        print(data)
        print("----------------------")
        if "subviews" in data.keys() :
            if 'control' in data.keys() :
                if 'identifier' in data['control'].keys():
                    answer.append(data['control']['identifier'])
            for x in data['subviews'] :
                parse_classIdentifier("identifier", x, answer)
            else : 
                return list(set(answer))
    


if __name__ == '__main__':

    file_name = sys.argv[1]
    if file_name[-5:] != ".json" :
        raise ValueError("Did not input a valid json file")
    with open(file_name) as inputfile:  
        data = json.load(inputfile)
    
    userinput = ""
    while userinput != "exit" :
        userinput = input("What is your selection ")
        if userinput == "classNames" or userinput == "identifier" or userinput == "class" : 
            answer = master_parse(userinput, data, [], 0)
            print("Full List of {}".format(userinput))
            print(str(answer))
        else : 
            print("ERROR: please enter classNames, identifier, or class")
    
    exit()
    
    
    