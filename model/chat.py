#!/usr/bin/python3

from __future__ import annotations
from typing import List
from activity import Activity


class Chat:

    def __init__(self, activities: List[Activity]):
        self.activities = activities

    '''
        Gives us an iterator for traversing
        over an instance of Chat object 
    '''

    def __iter__(self):
        return iter(self.activities)

    '''
        Returns position, at which we need to insert
        a new Activity ( for this chat ), so that
        ascendingly sorted order is kept.
        
        Position is found using binary search mechanism.
    '''

    def __getPushPosition__(self, idx: int, low: int, high: int):
        if low > high:
            return 0
        elif low == high:
            return low if self.activities[low].index > idx else (low + 1)
        else:
            mid = (low + high) // 2
            return self.__getPushPosition__(idx, low, mid) \
                if self.activities[mid].index > idx \
                else self.__getPushPosition__(idx, mid + 1, high)

    '''
        Pushes an instance of Activity subclass ( either Event or Message )
        into collection of all activities happened in chat
        in proper position, so that sorted order is kept
        ( ascending in terms of index of Activity )
    '''

    def push(self, item: Activity):
        self.activities.insert(self.__getPushPosition__(
            item.index, 0, len(self.activities) - 1), item)

    '''
        Denotes whether this activity is an Event
        or not

        If not an event, then it's a Message, sent by
        some chat participant
    '''

    def isEvent(self, idx: int) -> bool:
        try:
            self.getItem(idx).user
            return False
        except Exception:
            return True

    '''
        As all entries made into chat holder are organized in
        sorted fashion in terms of their index number,
        we can reduce search time by doing it using binary search.

        That's what is done here.
    '''

    def __getItem__(self, idx: int, low: int, high: int) -> int:
        if low > high:
            return -1
        elif low == high:
            return low if self.activities[low].index == idx else -1
        else:
            mid = (low + high) // 2
            return self.__getItem__(idx, low, mid) \
                if self.activities[mid].index >= idx \
                else self.__getItem__(idx, mid + 1, high)

    '''
        Finds an activity ( may be event or message ),
        happened in group by its corresponding index value 
        ( well this index is generated by telegram desktop 
        application, while exporting chat, which is to be examined )
    '''

    def getItem(self, idx: int) -> Activity:
        tmp = self.__getItem__(idx, 0, len(self.activities) - 1)
        return self.activities[tmp] if tmp == -1 else None


if __name__ == '__main__':
    print('[!]This module is expected to be used as a backend handler')
    exit(0)
