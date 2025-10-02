import sys, markdown

command = sys.argv[1]

def isMD(fileName):
    extention = fileName[-3:]
    if extention == '.md':
        return True
    else:
        return False
    
def isHTML(fileName):
    extention = fileName[-5:]
    if extention == '.html':
        return True
    else:
        return False

if command == 'markdown':
    inputFileName = sys.argv[2]
    if not isMD(inputFileName):
        print('wrong input file.')
        sys.exit()

    outputFileName = sys.argv[3]
    if not isHTML(outputFileName):
        print('wrong output file.')
        sys.exit()

    contentMD = ''
    contentHTML = ''

    with open(inputFileName, 'r') as fInput:
        contentMD = fInput.read()

    contentHTML = markdown.markdown(contentMD)

    with open(outputFileName, 'w') as fOutput:
        fOutput.write(contentHTML)
else:
    print('wrong command.')