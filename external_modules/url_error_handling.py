class Url_Error_Handling(Exception):    # ok
    def __init__(self,message:str) -> None:
        super().__init__(message)
        self.__message=message
    def __str__(self) -> str:
        return f"{self.__message}"


if __name__=="__main__":
    x=Url_Error_Handling('bad connection')
    print(x)