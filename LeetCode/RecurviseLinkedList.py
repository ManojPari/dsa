
def reverseLinkedList(head):
    if head == None and head["next"] == None:
         return head
    
    print(head)
    rest = reverseLinkedList(head["next"])
    head["next"]["next"] = head

    head["next"] = None

    return rest

head = {
     'data': 2,
     'next': {
          "data": 4,
          "next": {
               "data": 5,
               "next": {
                    "data": 8,
                    "next" : {
                         "data": -1,
                         "next": {
                              "data": 9,
                              "next": None
                         }
                    }
               }
          }
     }
}

res = reverseLinkedList(head)

print(res)