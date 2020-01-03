

class GetCookie:

    cookiesObj = {}

    def getCookie(self, cookies):
        for a in cookies.split(';'):
            if a:
                name, value = a.strip().split('=', 1)
                self.cookiesObj[name] = value
        print('处理完毕后的cookie为')
        print(self.cookiesObj)