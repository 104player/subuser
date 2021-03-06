#!/usr/bin/env python
# This file should be compatible with both Python 2 and 3.
# If it is not, please file a bug report.

"""
High level operations used for interacting with the subuser registry.
"""

#external imports
#import ...
#internal imports
import subuserlib.verify
import subuserlib.subprocessExtras as subprocessExtras

def showLog(user):
  user.getRegistry().getGitRepository().run(["log"])

def checkoutNoCommit(user,commit):
  subprocessExtras.call(["rm","-rf","*"],cwd=user.getConfig()["registry-dir"])
  user.getRegistry().getGitRepository().run(["checkout",commit,"."])
  user.reloadRegistry()

def rollback(user,commit):
  checkoutNoCommit(user,commit)
  user.getRegistry().logChange("Rolling back to commit: "+commit)
  subuserlib.verify.verify(user)
  user.getRegistry().commit()
