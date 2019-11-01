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

    Write A Program To Find The Word For nth Occurrence
    Example :
        find_occurrence("STRING","SUB_STRING",3)                                                         
"""

"""
 
      ___       __        _______   ______   .______       __  .___________. __    __  .___  ___. 
     /   \     |  |      /  _____| /  __  \  |   _  \     |  | |           ||  |  |  | |   \/   | 
    /  ^  \    |  |     |  |  __  |  |  |  | |  |_)  |    |  | `---|  |----`|  |__|  | |  \  /  | 
   /  /_\  \   |  |     |  | |_ | |  |  |  | |      /     |  |     |  |     |   __   | |  |\/|  | 
  /  _____  \  |  `----.|  |__| | |  `--'  | |  |\  \----.|  |     |  |     |  |  |  | |  |  |  | 
 /__/     \__\ |_______| \______|  \______/  | _| `._____||__|     |__|     |__|  |__| |__|  |__| 
                                                                                                  
    
    1. Create A Loop Of N Counts    
    2. Check If SubString Exits In String And Get Index
         Yes -> Increment Count, And Last Found Index By 1 
                Check If Occurence = Count , Break Since Occurrence Is Found
         No  -> Break Loop And Show nth Occurence Does Not Exist If Count > 0 Else Show String Does Not Exist
"""


test_string = """ 
Lorem ipsum dolor sit amet, quis fringilla ultricies eu wisi, suspendisse quam leo sit, luctus velit sed ipsum dignissim, mauris quis ut sollicitudin ipsum. Placerat ac eleifend pulvinar laoreet sit, et urna diam vulputate, volutpat ut, faucibus blandit quis commodo dolores, id nulla. Lorem vehicula egestas neque sit aliquam, arcu condimentum facilisis massa euismod. Volutpat mi nec habitant nibh dolor, in congue laoreet curabitur dui, lacinia etiam, placerat odio. Mauris tincidunt augue velit dolor enim lectus, pellentesque eget maecenas arcu risus metus, proin soluta, etiam corporis velit in imperdiet, eu rutrum scelerisque fringilla duis phasellus eleifend. Odio ut ipsum, ornare vel, semper diam nisl porttitor vitae turpis quis.
Amet elementum lacinia donec quisque ornare porta, lorem blandit morbi dicta duis justo augue, arcu felis rutrum commodo nam. Quas dolor congue leo est ullamcorper. Ac imperdiet, odio pede, mauris proin scelerisque elit at. Pharetra conubia, magnis sit ipsum, erat ut sed, vitae consectetuer mauris wisi ac donec, dapibus congue. At cras amet nam. Vestibulum nibh dolor, laoreet mauris,lacus pede, eros vestibulum.
"""
sub_string = 'velit'


class NotFound(Exception):
   """Base class for other exceptions"""
   pass


def return_index_if_exists(string, sub_string, start_index):
    """Given a string and substring, returns if the sting exists or not

    Args:
        string: string in which the substring needs to be found
        sub_string: the sub string which needs to be found in the string

    Returns:
        index : the index in string where the substring is found
        
    Raises:
        NotFound : if the sub string does not exist
    """
    index = string.find(sub_string, start_index)
    if index == -1:
        raise NotFound
    else:
        return index


    

def find_occurrence(string, sub_string, occurrence):
    """Given a string, substring and count , returns the index of the nth occurrence of the substring
    
    Args:
        string: string in which the substring needs to be found
        sub_string: the sub string which needs to be found in the string
        occurrence : the nth occurrence that we need to find
    
    Returns:
        index : index of the nth Occurrence

    """
    last_index = 0
    count = 0
    if occurrence>0:
        for i in range(0,occurrence):
            try:
                last_index = return_index_if_exists(string, sub_string, last_index)
                last_index += 1
                count += 1
                if(count ==occurrence):
                    print("Index Of {0}th Occurrence {1}".format(occurrence,last_index-1))
                    break
            except NotFound:
                if(count == 0):
                    print("The {0} Does Not Exist At All".format(sub_string))
                else:
                    print("The Last Occurence Of {0} is {1}".format(sub_string, count))
                break
    else:
        print("Please give an occurrence more than or equal to 1")


if __name__ == '__main__':
    find_occurrence(test_string,sub_string, 4)


