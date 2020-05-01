from DoublyLinkedList import DoublyLinkedList
import random

class HashTableNode:
    def __init__(self, searchKey=None, newItem=None):
        self.searchKey = searchKey
        self.newItem = newItem

class HashTable:
    def __init__(self, probe, size):
        assert probe == "linearProbe" or probe == "quadraticProbe" or probe == "chaining"
        assert size > 0
        self.probe = probe
        self.size = size
        self.table = [None] * self.size

    def hash(self, searchKey):                                          #Hash methode (a mod x), check of de zoeksleutel een string of int is.
        if isinstance(searchKey, str):
            searchKey = int(''.join([str(ord(char)) for char in (searchKey)]))
        hash = searchKey % self.size
        return hash

    def linearProbe(self, searchKey):
        index = self.hash(searchKey)
        while self.table[index] is not None:                             #Blijf deze loop runnen tot we een lege plek vinden in de tabel.
            if index >= self.size - 1:
                index = 0                                                #Zet check op 1 om op index 0 verder te zoeken.
            else:
                index += 1
        return index

    def quadraticProb(self, searchKey):
        index = constant = self.hash(searchKey)
        iteration = 0
        g = 0
        while self.table[index] is not None:                            #Blijf deze loop runnen tot we een lege plek vinden in de tabel.
                iteration += 1
                index = constant + iteration ** 2
                if index > self.size - 1:                               #Blijf doorgaan tot we alle indexes hebben gehad.
                        g += 1
                        constant = g - 1
                        iteration = 0
                        index = constant + iteration ** 2
        return index

    def tableInsert(self, searchKey, newItem):
        if self.probe == "chaining":
            node = HashTableNode(searchKey, newItem)
            position = self.table[self.hash(searchKey)]
            if position is None:                                        #De positie in de tabel is leeg. Maak een nieuwe dubbel gelinkte lijst aan.
                position = DoublyLinkedList()
                position.insertNode(node.searchKey, node.newItem)       #Insert de node in deze nieuwe lijst.
                self.table[self.hash(node.searchKey)] = position
                return True
            else:
                if position.searchList(node.searchKey) is False:
                    position.insertNode(node.searchKey, node.newItem)
                    self.table[self.hash(node.searchKey)] = position
                    return True
                elif searchKey == position.searchList(node.searchKey)[0][0]:
                    return False
        elif self.tableLength() == self.size:                           #De tabel is vol dus return False.
            return False
        elif self.probe == "linearProbe":                               #Gebruik linearprobe om items te inserten
            if self.linearProbe(searchKey) is False:
                return False
            else:
                self.table[self.linearProbe(searchKey)] = searchKey, newItem
                return True
        elif self.probe == "quadraticProbe":                            #Gebruik quadraticprobe om items te inserten
            if self.quadraticProb(searchKey) is False:
                return False
            else:
                self.table[self.quadraticProb(searchKey)] = searchKey, newItem
                return True

    def isEmpty(self):
        if self.tableLength() is 0:
            return True
        else:
            return False

    def tableRetrieve(self, searchKey):                                 #Zoek een item en begin bij de gehashte searchKey.
        if self.probe == "chaining":
            position = self.table[self.hash(searchKey)]
            if position is not None:
                result = position.searchList(searchKey)                 #Roep de zoekfunctie van de dubbel gelinkte lijst.
                if result is None or result is False:
                    return False
                return result[0][1]
            return False
        else:
            if self.searcher(searchKey) is False:                       #Gebruik de search functie om een item te zoeken.
                return False
            return self.searcher(searchKey)[0][1]                       #De zoek functie geeft: Key,Item,index. We willen alleen het item.

    def tableLength(self):                                              #Return de lengte van de tabel.
        total = index = 0
        while index != self.size:                                       #Check voor een item op elke index.
            position = self.table[index]
            if position is not None and position is not "Deleted":
                if self.probe == "chaining":                            #De gelinkte lijst heeft buckets. Als de probe method chaining is dan moeten we de items per bucket op elke index optellen.
                    result = position.getList()
                    total = total + len(result)
                else:
                    total += 1                                          #Totaal aantal items + 1.
            index += 1
        return total

    def tableDelete(self, searchKey):                                   #Zoek een item dmv linearprobe of quadratic.
        position = self.table[self.hash(searchKey)]
        if self.probe == "chaining":
            if position is not None:
                return position.deleteNode(searchKey)
            return False
        else:
            if self.searcher(searchKey) is False:
                return False
            else:
                self.table[self.searcher(searchKey)[1]] = "Deleted"     #self.searcher(searchKey)[1] geeft de index van het item.
                return True

    def clear(self):                                                    #Verwijder alle item uit de tabel.
        self.table = [None] * self.size

    def searcher(self, searchKey):                                      #Zoek een item en begin bij de gehashte searchKey.
        index = constant = self.hash(searchKey)
        iteration = g = check = 0
        if self.hash(searchKey) >= self.size:
            return False
        elif self.probe == "chaining":
            position = self.table[self.hash(searchKey)]
            if position is not None:
                result = position.searchList(searchKey)
                if result is None or result is False:
                    return False
                return result[0][1]
            return False
        elif self.probe == "linearProbe":                                 #Afhankelijk van de probe methode gebruik de juist probe om te zoeken.
            while self.table[index] is not None:                          #Blijf linprobe runnen tot we none tegenkomen en het item met de KEY niet in de tabel kan zitten.
                if self.table[index][0] == searchKey:
                    return self.table[index], index
                elif check == 1 and index >= self.hash(searchKey):        #Stop als we de hele tabel hebben doorzocht.
                    return False
                elif index >= self.size - 1:
                    index = 0
                    check = 1
                else:
                    index += 1
            return False
        elif self.probe == "quadraticProbe":
            while self.table[index] is not None:                           #Blijf quadraticProbe runnen tot we none tegenkomen en de table dus leeg is.
                if self.table[index][0] == searchKey:
                    return self.table[index], index
                elif g >= self.size:
                    return False
                else:
                    iteration += 1
                    index = constant + iteration ** 2
                    if index > self.size - 1:
                        g += 1
                        constant = g - 1
                        iteration = 0
                        index = constant + iteration ** 2
            return False