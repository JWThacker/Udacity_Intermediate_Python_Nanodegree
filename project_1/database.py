"""A database encapsulating collections of near-Earth objects and approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""
from models import CloseApproach
from models import NearEarthObject


class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """

    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of
        NEOs and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link
        themtogether - after it's done, the `.approaches` attribute of
        each NEO has a collection of that NEO's close approaches, and
        the `.neo` attribute of each close approach references the
        appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        neos = list(neos)
        self._neos = list(neos)
        self._approaches = list(approaches)
        self._neos_name_dict = {}
        self._neos_des_dict = {}
        for neo in self._neos:
            if neo.name:
                self._neos_name_dict[neo.name] = neo

        for neo in self._neos:
            if neo.designation not in self._neos_des_dict.keys():
                self._neos_des_dict[neo.designation] = neo

        neos.sort(key=self._sorting_criteria)
        for approach in self._approaches:
            location = self._binary_search(neos, approach._designation)
            if location >= 0:
                approach.neo = neos[location]
                neos[location].approaches.append(approach)

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary
        designation, or `None`.
        """
        try:
            to_return = self._neos_des_dict[designation]
            return to_return
        except KeyError as e:
            return None

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        try:
            to_return = self._neos_name_dict[name]
            return to_return
        except KeyError as e:
            return None

    def query(self, filters=()):
        """Query CloseApproaches to generate those that match certain filters.

        This generates a stream of `CloseApproach` objects
        that match all of the provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order,
        which isn't guaranteed to be sorted meaninfully, although
        is often sorted by time.

        :param filters: A collection of filters capturing user-specified
                        criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        potentialApproach = []
        ge = 0
        eq = 1
        le = 2
        filterKeys = list(filters.keys())
        dateKey = filterKeys[0]
        distanceKey = filterKeys[1]
        velocityKey = filterKeys[2]
        diameterKey = filterKeys[3]
        hazardousKey = filterKeys[4]
        for approach in self._approaches:
            potentialApproach.append(approach)
            # Are there any datetime filters?
            if not self.isFullOfNones(filters[dateKey]):
                # Does the query ask for a max and min value of date?
                if self.isDoubleBounded(filters[dateKey]):
                    if filters[dateKey][ge](approach) and \
                            filters[dateKey][le](approach):
                        pass
                    else:
                        potentialApproach.pop()
                # Does the query ask only for a min date?
                if self.isLowerBounded(filters[dateKey]):
                    if filters[dateKey][ge](approach):
                        pass
                    else:
                        potentialApproach.pop()
                # Does the query ask only for a max date?
                if self.isUpperBounded(filters[dateKey]):
                    if filters[dateKey][le](approach):
                        pass
                    else:
                        potentialApproach.pop()
                # Does the query ask only for a specific date?
                if self.isAskingForEquality(filters[dateKey]) or\
                        self.allNonNones(filters[dateKey]):
                    if filters[dateKey][eq](approach):
                        pass
                    else:
                        potentialApproach.pop()
            # If the approach object didn't fit the above specificiations,
            # end iteration and continue
            if self.isEmpty(potentialApproach):
                continue
            else:
                pass
            # Are there any distance filters?
            if not self.isFullOfNones(filters[distanceKey]):
                # If so, does the query ask for a max and min distance?
                if self.isDoubleBounded(filters[distanceKey]):
                    if filters[distanceKey][ge](approach) and\
                            filters[distanceKey][le](approach):
                        pass
                    else:
                        potentialApproach.pop()
                # Does the query ask for a min distance?
                if self.isUpperBounded(filters[distanceKey]):
                    if filters[distanceKey][le](approach):
                        pass
                    else:
                        potentialApproach.pop()
                # Does the query ask for a max distance?
                if self.isLowerBounded(filters[distanceKey]):
                    if filters[distanceKey][ge](approach):
                        pass
                    else:
                        potentialApproach.pop()
            # If the approach didn't fit the above specifications,
            # end iteration and continue
            if self.isEmpty(potentialApproach):
                continue
            else:
                pass
            # Are there any velocity filters?
            if not self.isFullOfNones(filters[velocityKey]):
                # If so, does the query as for a min and max velocity?
                if self.isDoubleBounded(filters[velocityKey]):
                    if filters[velocityKey][ge](approach) and\
                            filters[velocityKey][le](approach):
                        pass
                    else:
                        potentialApproach.pop()
                # Does the query ask for a max velocity?
                if self.isUpperBounded(filters[velocityKey]):
                    if filters[velocityKey][le](approach):
                        pass
                    else:
                        potentialApproach.pop()
                # Does the query ask for a min velocity?
                if self.isLowerBounded(filters[velocityKey]):
                    if filters[velocityKey][ge](approach):
                        pass
                    else:
                        potentialApproach.pop()
            # If the approach didn't fit the above specification,
            # end iteration and continue.
            if self.isEmpty(potentialApproach):
                continue
            else:
                pass
            # Are there and diameter filters?
            if not self.isFullOfNones(filters[diameterKey]):
                # If so, does the query ask for a max and min diameter?
                if self.isDoubleBounded(filters[diameterKey]):
                    if filters[diameterKey][ge](approach) and\
                            filters[diameterKey][le](approach):
                        pass
                    else:
                        potentialApproach.pop()
                # Does the query ask only for a max diameter?
                if self.isUpperBounded(filters[diameterKey]):
                    if filters[diameterKey][le](approach):
                        pass
                    else:
                        potentialApproach.pop()
                # Does the query ask only for a min diameter?
                if self.isLowerBounded(filters[diameterKey]):
                    if filters[diameterKey][ge](approach):
                        pass
                    else:
                        potentialApproach.pop()
            # If the approach didn't fit the above specifications,
            # end iteration and continue.
            if self.isEmpty(potentialApproach):
                continue
            else:
                pass
            # Are there any hazardous filters?
            if not self.isFullOfNones(filters[hazardousKey]):
                # If so, does the approach meet the requirements of the filter?
                if filters[hazardousKey][eq](approach):
                    pass
                else:
                    potentialApproach.pop()
            # If the approach didn't fit the above specification,
            # end iteration and continue.
            if self.isEmpty(potentialApproach):
                continue
            else:
                yield potentialApproach.pop()

    def _sorting_criteria(self, neo_cad):
        """Define a way to sort NearEarthObject/CloseApproach.

        :param neo_cad: an instance of a NearEarthObject/CloseApproach
        :return a String - the instances are to be sorted in
        lexographic order by their designation
        """
        if isinstance(neo_cad, CloseApproach):
            return neo_cad._designation
        else:
            return neo_cad.designation

    def _binary_search(self, list_in, target):
        """Perform binary search on NearEarthObjects/CloseApproach objects.

        This method performs binary search on a list of
        NearEarthObject/CloseApproach objects given
        a particular target designation.

        :param list_in: The list of instances of
                        NearEarthObjects/CloseApproaches
        :param target: The target designation (each NearEarthObject
                       has a unique designation).
        :return: The location (index) of the particular index in the list.
                 If the object is not found, return -1.
        """
        left = 0
        right = len(list_in) - 1
        while left <= right:
            middle = (left + right) // 2
            if list_in[middle].designation < target:
                left = middle + 1
            elif list_in[middle].designation > target:
                right = middle - 1
            else:
                return middle
        return -1

    def isLowerBounded(self, list_in):
        """Determine if a list of filters requests a single minimum value.

        :param list_in: The list of AttributeFilters
        :return: A boolean representing whether or not a
                 list of filters request a minimum value
        """
        if (list_in[0] is not None) and (list_in[2] is None):
            return True
        else:
            return False

    def isUpperBounded(self, list_in):
        """Determine if a list of filters requests a single maximum value.

        :param list_in: The list of AttributeFilters
        :return: A boolean representing whether or not a list
                 of filters requests a maximum value
        """
        if (list_in[0] is None) and (list_in[2] is not None):
            return True
        else:
            return False

    def isDoubleBounded(self, list_in):
        """Determine if a list of filters requests a maximum/minimum values.

        :param list_in: The list of AttributeFilters
        :return: A boolean representing whether or not a list
                 of filters requests a maximum and minimum value
        """
        if (list_in[0] is not None) and (list_in[1] is None) and\
                (list_in[2] is not None):
            return True
        else:
            return False

    def isAskingForEquality(self, list_in):
        """Determine if a list of filters requests one value.

        :param list_in: The list of AttributeFilters
        :return: A boolean representing whether or not
                 a list of filters requests a single value
        """
        if list_in[1] is not None:
            return True
        else:
            return False

    def isFullOfNones(self, list_in):
        """Determine if a list of AttributeFilters is full of None values.

        :param list_in: The list of AttributeFilters
        :return: A boolean representing whether or not
                 the list is empty (full of Nones)
        """
        return all(element is None for element in list_in)

    def allNonNones(self, list_in):
        """Determine if a list of AttributeFilters contains any None values.

        This method determines if all the elements of list_in are instances
        of subclasses of AttributeFilter.

        :param list_in: The list of AttributeFilters
        :return: A boolean representing whether or not if the list
        is full of instances of AttributeFilters
        """
        return all(element is not None for element in list_in)

    def isEmpty(self, list_in):
        """Determine if a list/stack is empty or not.

        :param list_in: The list with a single approach in it
        :return: A boolean representing whether or not the stack is empty
        """
        return len(list_in) < 1
