from unittest.mock import Mock

mock = Mock()

import json

teste = json.dumps({'a': 1})
json = mock

#Como pode ser visto no print abaixo a dependência json não possui a função "dumps", porém ainda assim foi possível "disfarçar"
print(dir(json))