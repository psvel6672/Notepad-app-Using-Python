class Author:

    def __init__(self, toolName):
        self.Tool = toolName

        self.author = """
------------------------------------------
Author    :: PS Thamizhan
Tool Name :: """+str(self.Tool)+"""
Reach Me  :: psthamizhan02@gmail.com
------------------------------------------
"""
    def echoAuthor(self):
        print(self.author)
