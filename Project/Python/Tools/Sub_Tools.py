from Tools.Base_Tools import BaseTools
class SubTools(BaseTools):
    @staticmethod  
    def AddToFile(path: str, context: str):
        with open(path, "a") as file:
            file.write(context)
            file.close()
        return None