class Lexicon(object):
            def scan(self, userinput):
                #First split up input into a list of words.
                words = userinput.split()
                output = []
                #Next go through the list, for each word give it a label
                #form a list of words for each label
                for item in words:
                    result = self.label(item) #return a nice tuple
                    output.append(result)
                #return a list of all of these labeled words
                return output

            def label(self, item):
                #label the item and package it up in a tuple
                if item in ['north', 'south', 'east']:
                    return ('direction', item)
                    #test if its a verb
                elif item in ['go', 'kill', 'eat']:
                    return ('verb', item)
                    #test if its a stop
                elif item in ['the', 'in', 'of']:
                    return ('stop', item)
                    #test if its a noun
                elif item in ['bear', 'princess']:
                    return ('noun', item)
                    #test if its a number
                else:
                    try:
                        number = int(item)
                        return('number', number)
                    except ValueError:
                        return ('error', item)


lexicon = Lexicon()
