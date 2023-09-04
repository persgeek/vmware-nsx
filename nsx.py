import base64
import requests

class Nsx:

    address = None
    username = None
    password = None

    MACHINE_URL = 'api/v1/fabric/virtual-machines'
    GROUP_URL = 'api/v1/infra/domains/default/groups'
    POLICY_URL = 'api/v1/infra/domains/default/security-policies'

    MEMBER_TYPE_VIRTUAL_MACHINE = 'VirtualMachine'

    RESOURCE_TYPE_EXTERNAL_ID = 'ExternalIDExpression'
    RESOURCE_TYPE_L4_PORT = 'L4PortSetServiceEntry'

    CATEGORY_APPLICATION = 'Application'

    ACTION_ALLOW = 'ALLOW'
    ACTION_DROP = 'DROP'

    DIRECTION_IN = 'IN'
    DIRECTION_OUT = 'OUT'

    PROTOCOL_TCP = 'TCP'
    PROTOCOL_UDP = 'UDP'

    VALUE_ANY = 'ANY'

    def __init__(self, address, username, password):

        self.address = address
        self.username = username
        self.password = password

    def append(self, *parts):

        output = ''

        for part in parts:

            output += str(part)

        return output

    def getUrl(self, *parts):

        url = self.append('https://', self.address)

        for part in parts:

            url = self.append(url, '/', part)

        return url

    def getSession(self):

        session = requests.Session()

        session.auth = (self.username, self.password)
        session.verify = False

        return session

    class Response:

        response = None

        def __init__(self, response):

            self.response = response

        def json(self):

            return self.response.json()

        def success(self):

            if self.response.status_code in [200, 201]:
                return True

            return False

    def getGroups(self):

        url = self.getUrl(self.GROUP_URL)

        response = self.getSession().get(url)

        return self.Response(response)

    def getGroup(self, name):

        url = self.getUrl(self.GROUP_URL, name)

        response = self.getSession().get(url)

        return self.Response(response)

    def createGroup(self, name, params=None):

        url = self.getUrl(self.GROUP_URL, name)

        response = self.getSession().put(url, json=params)

        return self.Response(response)

    def updateGroup(self, name, params=None):

        url = self.getUrl(self.GROUP_URL, name)

        response = self.getSession().patch(url, json=params)

        return self.Response(response)

    def getMachines(self):

        url = self.getUrl(self.MACHINE_URL)

        response = self.getSession().get(url)

        return self.Response(response)

    def getPolicies(self):

        url = self.getUrl(self.POLICY_URL)

        response = self.getSession().get(url)

        return self.Response(response)

    def getPolicy(self, name):

        url = self.getUrl(self.POLICY_URL, name)

        response = self.getSession().get(url)

        return self.Response(response)

    def createPolicy(self, name, params=None):

        url = self.getUrl(self.POLICY_URL, name)

        response = self.getSession().put(url, json=params)

        return self.Response(response)

    def updatePolicy(self, name, params=None):

        url = self.getUrl(self.POLICY_URL, name)

        response = self.getSession().patch(url, json=params)

        return self.Response(response)

    def destroyPolicy(self, name):

        url = self.getUrl(self.POLICY_URL, name)

        response = self.getSession().delete(url)

        return self.Response(response)
