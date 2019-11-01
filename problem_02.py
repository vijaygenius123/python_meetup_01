"""
Author: Vijayaraghavan Sundararaman
Date : 01/Nov/2019
"""

"""
 
 .______   .______        ______   .______    __       _______ .___  ___. 
 |   _  \  |   _  \      /  __  \  |   _  \  |  |     |   ____||   \/   | 
 |  |_)  | |  |_)  |    |  |  |  | |  |_)  | |  |     |  |__   |  \  /  | 
 |   ___/  |      /     |  |  |  | |   _  <  |  |     |   __|  |  |\/|  | 
 |  |      |  |\  \----.|  `--'  | |  |_)  | |  `----.|  |____ |  |  |  | 
 | _|      | _| `._____| \______/  |______/  |_______||_______||__|  |__| 

    From the API https://randomuser.me/api?results=10 
        1. Calculate Average Age 
        2. Ratio Of Male Vs Female 
                                                                    
 
"""

"""
 
      ___       __        _______   ______   .______       __  .___________. __    __  .___  ___. 
     /   \     |  |      /  _____| /  __  \  |   _  \     |  | |           ||  |  |  | |   \/   | 
    /  ^  \    |  |     |  |  __  |  |  |  | |  |_)  |    |  | `---|  |----`|  |__|  | |  \  /  | 
   /  /_\  \   |  |     |  | |_ | |  |  |  | |      /     |  |     |  |     |   __   | |  |\/|  | 
  /  _____  \  |  `----.|  |__| | |  `--'  | |  |\  \----.|  |     |  |     |  |  |  | |  |  |  | 
 /__/     \__\ |_______| \______|  \______/  | _| `._____||__|     |__|     |__|  |__| |__|  |__| 
                                                                                                  
    
    1. Get The Data From API
    2. Convert It To JSON
    3. Extract The Results
    4. Iterate Over Each Person And Push Age & Sex Into A Two Different Arrays
"""
from json import loads
from requests import get

BASE_URL = "https://randomuser.me/api?results="
num_of_results = 10
url = BASE_URL + str(num_of_results)


def get_average(data):
    """Returns the average of the list

    Args: 
        data: list of numbers for which we need average
    
    Returns:
        average: average of the data. sum of data / num of data points 

    """
    return sum(data) / len(data)


def get_ratio(data):
    """Returns the average of the list

    Args: 
        data: list containing the different items
    
    Returns:
        ratio: dictonary of number of times a item is appearing in the list

    """
    unique = set((data))
    count = {}
    for item in unique:
        count[item]  = 0
    for item in data:
        count[item] += 1/len(data)
    return count


if __name__ == '__main__':
    response = get(url)
    if response.status_code == 200:
        json_response = loads(response.text)
        results = json_response.get('results', [])
        ages = []
        sexs = []
        for result in results:
            sexs.append(result.get('gender'))
            ages.append(result.get('dob').get('age'))
        print(get_average(ages))
        print(get_ratio(sexs))
        
    else:
        print("There Seems To Be An Issue In The Network / URL")

