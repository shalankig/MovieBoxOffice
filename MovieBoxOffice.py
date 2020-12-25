import os
import sys


class BoxOffice:
    def __init__(self, w, n):
        self.w = w
        self.n = n
        self.queues = [[] for i in range(w)]
        self.open = [False for i in range(w)]
        self.open[0] = True

        '''
        'starts' and 'ends' can be used as front and rear respectively for literal queue implementation
        However, List is a Python’s built-in data structure that can be used as a queue. 
        Instead of enqueue() and dequeue(), append() and pop() functions are used directly
        '''
        # self.starts = [0 for i in range(w)]
        # self.ends = [0 for i in range(w)]

    '''
    This function returns True if the box office window is open and
    False if it is yet to be opened (closed).
    '''
    def isOpen(self, windowId):
        if windowId <= len(self.queues):
            return self.open[windowId - 1]
        else:
            return "Window ID outside supplied range, Please Recheck input file"

    '''
    This function returns the queue (number of people waiting) in front of the window. 
    Will return empty queue if window is closed
    '''
    def getWindow(self, windowId):
        if windowId <= len(self.queues):
            return self.queues[windowId - 1]
        else:
            return "Window ID outside supplied range, Please Recheck input file"

    '''
    This function is called to add a new person to one of the open window queues. 
    It returns windowId of the window where the person should go to and 
    1 if all the queues are full
    '''
    def addPerson(self, personId):
        min_window_size = self.n
        for open_window_index, open_window in enumerate(self.open):
            if open_window:
                open_window_length = len(self.queues[open_window_index])
                if open_window_length < min_window_size:
                    min_window_size = open_window_length
                    current_window = open_window_index
                else:
                    pass

        if min_window_size == self.n:
            for window in range(len(self.queues)):
                if len(self.queues[window]) < self.n:
                    self.queues[window].append(personId)
                    self.open[window] = True
                    return window + 1
            else:
                return -1

        else:
            self.queues[current_window].append(personId)
            self.open[current_window] = True
            return current_window + 1

    '''
    This function is called to issue a ticket at every open box office
    window with a queue of at least one person.
    '''
    def giveTicket(self):
        tickets_given = 0
        for j in self.queues:
            if len(j) > 0:
                j.pop(0)
                tickets_given += 1
        return tickets_given


def main():
    filePath = 'inputPS19.txt'

    # Check if input file exists
    if not os.path.isfile(filePath):
        print("File Path {} does not exist. Exiting....".format(filePath))
        sys.exit()

    # Read the input file
    with open(filePath, 'r+') as input_file:
        # Create the output file
        with open('outputPS19.txt', 'w') as output_file:
            x = []
            for line in input_file:
                boxOffice = line.split(':')
                if len(boxOffice) == 3 and boxOffice[0] == 'ticketSystem':
                    # create an instance of the box office class
                    BoxOfficeInstance = BoxOffice(int(boxOffice[1]), int(boxOffice[2]))
                    x.append(boxOffice[1])
                    x.append(boxOffice[2])

                elif len(boxOffice) == 2:
                    boxOffice[-1] = boxOffice[-1].strip()

                    if boxOffice[0] == 'isOpen':
                        is_open = BoxOfficeInstance.isOpen(int(boxOffice[1]))
                        # Writing the result in output file
                        output_file.write(boxOffice[0] + boxOffice[1] + ' >> ' + str(is_open) + '\n')
                    elif boxOffice[0] == 'getWindow':
                        get_window = BoxOfficeInstance.getWindow(int(boxOffice[1]))
                        # Writing the result in output file
                        output_file.write(boxOffice[0] + boxOffice[1] + ' >> ' + str(get_window) + '\n')
                    elif boxOffice[0] == 'addPerson':
                        add_person = BoxOfficeInstance.addPerson(int(boxOffice[1]))
                        # Writing the result in output file
                        if add_person == -1:
                            output_file.write(boxOffice[0] + boxOffice[1] + ' >> ' + 'All Queues are full' + '\n')
                        else:
                            output_file.write(boxOffice[0] + boxOffice[1] + ' >> ' + str(add_person) + '\n')
                    elif boxOffice[0] == 'giveTicket':
                        give_ticket = BoxOfficeInstance.giveTicket()
                        # Writing the result in output file
                        output_file.write(boxOffice[0] + boxOffice[1] + ' >> ' + str(give_ticket) + '\n')


# Calling the main function
if __name__ == '__main__':
    main()


