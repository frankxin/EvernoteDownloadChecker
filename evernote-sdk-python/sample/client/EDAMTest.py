#
# A simple Evernote API demo script that lists all notebooks in the user's
# account and creates a simple test note in the default notebook.
#
# Before running this sample, you must fill in your Evernote developer token.
#
# To run (Unix):
#   export PYTHONPATH=../../lib; python EDAMTest.py
#

import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
import re
import smtplib

from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter
from email.mime.text import MIMEText

# Real applications authenticate with Evernote using OAuth, but for the
# purpose of exploring the API, you can get a developer token that allows
# you to access your own Evernote account. To get a developer token, visit
# https://sandbox.evernote.com/api/DeveloperToken.action
auth_token = "S=s1:U=8fda7:E=1547f073cf6:C=14d27560f48:P=1cd:A=en-devtoken:V=2:H=b86b0b05e46ced7583b24db5792e990e"

if auth_token == "your developer token":
    print "Please fill in your developer token"
    print "To get a developer token, visit " \
        "https://sandbox.evernote.com/api/DeveloperToken.action"
    exit(1)

# Initial development is performed on our sandbox server. To use the production
# service, change sandbox=False and replace your
# developer token above with a token from
# https://www.evernote.com/api/DeveloperToken.action
client = EvernoteClient(token=auth_token, sandbox=True)

user_store = client.get_user_store()

version_ok = user_store.checkVersion(
    "Evernote EDAMTest (Python)",
    UserStoreConstants.EDAM_VERSION_MAJOR,
    UserStoreConstants.EDAM_VERSION_MINOR
)
print "Is my Evernote API version up to date? ", str(version_ok)
print ""
if not version_ok:
    exit(1)

note_store = client.get_note_store()
noteFilter = NoteFilter(words="EDAMTest");
noteFind = note_store.findNotes(noteFilter,0,25);
print len(noteFind.notes)
note = note_store.getNote(noteFind.notes[0].guid , True , True , True , False);
print note.content
m = re.match(r'^[\s\S]+<div>windows\s*:\s*([\S\s]+?)</div>[\s\S]+$',note.content)
print m.group(0)
print '\n'
print m.group(1)

f = open('./downloads.php','r') 
phpFile = f.read()
downloadsMatch = re.match(r'^[\s\S]+"EvernoteMac"\s+=>\s+"(\S+)"[\s\S]+$',phpFile)
print downloadsMatch.group(1)  


# List all of the notebooks in the user's account
notebooks = note_store.listNotebooks()
print "Found ", len(notebooks), " notebooks:"
for notebook in notebooks:
    print "  * ", notebook.name

# print
# print "Creating a new note in the default notebook"
# print

# To create a new note, simply create a new Note object and fill in
# attributes such as the note's title.
# note = Types.Note()
# note.title = "Test note from EDAMTest.py"

# To include an attachment such as an image in a note, first create a Resource
# for the attachment. At a minimum, the Resource contains the binary attachment
# data, an MD5 hash of the binary data, and the attachment MIME type.
# It can also include attributes such as filename and location.
# image = open('enlogo.png', 'rb').read()
# md5 = hashlib.md5()
# md5.update(image)
# hash = md5.digest()

# data = Types.Data()
# data.size = len(image)
# data.bodyHash = hash
# data.body = image

# resource = Types.Resource()
# resource.mime = 'image/png'
# resource.data = data

# # Now, add the new Resource to the note's list of resources
# note.resources = [resource]

# # To display the Resource as part of the note's content, include an <en-media>
# # tag in the note's ENML content. The en-media tag identifies the corresponding
# # Resource using the MD5 hash.
# hash_hex = binascii.hexlify(hash)

# # The content of an Evernote note is represented using Evernote Markup Language
# # (ENML). The full ENML specification can be found in the Evernote API Overview
# # at http://dev.evernote.com/documentation/cloud/chapters/ENML.php
# note.content = '<?xml version="1.0" encoding="UTF-8"?>'
# note.content += '<!DOCTYPE en-note SYSTEM ' \
#     '"http://xml.evernote.com/pub/enml2.dtd">'
# note.content += '<en-note>Here is the Evernote logo:<br/>'
# note.content += '<en-media type="image/png" hash="' + hash_hex + '"/>'
# note.content += '</en-note>'

# # Finally, send the new note to Evernote using the createNote method
# # The new Note object that is returned will contain server-generated
# # attributes such as the new note's unique GUID.
# created_note = note_store.createNote(note)

# print "Successfully created a new note with GUID: ", created_note.guid



# Send email method.
msg = MIMEText('this have a change on MAC','plain','utf-8')
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.set_debuglevel(1)
server.login('fzhang2@evernote.com','')
server.sendmail('fzhang2@evernote.com','frankxin93@gmail.com',msg.as_string())
print 'an email send \n'
