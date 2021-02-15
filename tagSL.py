# A copy of the apache license is included below to prevent
# the LICENSE file from needing to be distributed alongside
# this file as a standalone file.
'''
Copyright 2021 approachcircle

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
import os, time, traceback
try:

    class SessionLockedException(Exception):
        pass
    
    class display:
        def sessionState(self): # get the session state
            os.system("if exist SESSION.LOCK (echo the session is currently locked) else (echo the session is currently unlocked)")

    class do:
        def lockSession(self):
            os.system("echo > SESSION.LOCK")
            print("session locked")

        def unlockSession(self):
            os.system("del SESSION.Lock")
            print("session unlocked")

        def sessionExists(self):
            raise SessionLockedException("session has already been locked. possibly by another instance?")

    do = do()
    display = display()

except SessionLockedException:
    traceback.print_exc()
    print()
    print("press enter.")
    input()