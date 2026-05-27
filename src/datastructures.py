"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
       self.last_name = last_name
       self._members = []

    # This method generates a unique incremental ID
    def _generateId(self):
        return randint(0,9999)

    def add_member(self, member):
        if "id" not in member:
            member.update(
                id = self._generateId
            )
        self._members.append(member)
        pass

    def delete_member(self, id):
        for member in self._members:
            if member ["id"] == id:
                self._members.remove(member)
                return "true"
        return False

    def get_member(self, id):
        for member in self._members:
            if member ["id"] == id:
                return member
        return None      
        

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members