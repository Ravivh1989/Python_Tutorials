import pprint

import svn.local

r = svn.local.LocalClient('/tmp/test_repo.co')
info = r.info()
pprint.pprint(info)