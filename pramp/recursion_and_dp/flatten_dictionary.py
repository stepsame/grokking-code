"""
Flatten a Dictionary
Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it.
If a certain key is empty, it should be excluded from the output (see e in the example below).
input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }
output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }


"""

"""
Solution:
Recursion is a natural choice for this kind of problem.
We iterate over the keys in dict and distinguish between two cases: 
If the value mapped to a key is a primitive,
 we take that key and simply concatenate it to the flattened key we've created up to this point.
 We then map the resulting key to the value in the output dictionary.
If the value is a dictionary, 
 we again concatenate the keys, but instead of adding the resulting key and value to the output dictionary,
 we recurse on the value with the newly formed key.

Because it is useful to create the output dictionary outside of the recursive function, 
it makes sense to use a helper function in this problem.

Time Complexity:

Space Complexity:

"""


def flatten_dict(path, original_dict, flat_dict):
    for key, value in original_dict.items():
        if path and key:
            updated_path = f'{path}.{key}'
        elif path:
            updated_path = path
        else:
            updated_path = key
        if not isinstance(value, dict):
            flat_dict[updated_path] = value
        else:
            flatten_dict(updated_path, value, flat_dict)


def solution(original_dict):
    flat_dict = {}
    flatten_dict("", original_dict, flat_dict)
    print(flat_dict)
    return flat_dict


def main():
    assert solution({
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }) == {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }


if __name__ == '__main__':
    main()
