__author__ = 'HP'
import itertools

### 1. The problem talks about how the Amazon parrots were delivering the ordered items at the wron places to the wrong people. The state space here would be
###   all the combinations possible for the 5 different people ordering 5 different items at five different places,wherein each combination has one person ordering one particular item at one address , the sum of which was 14400.
### The successor function for identifying the next possible steps would be by applying the information we have about the list of people who have received the items that they did not order.
###For example : The person who ordered the Candelabraum received a Banister. So we can compare that with the list of ordered items and build a list where the person who ordered the Candelabraum receives the Banister.
###Now on comparison with the combinations of the  list of people who have ordered items that we generated,we can eliminate choices where the person has  received a Banister but have also ordered a Banister.
### We follow this methodology to identify and remove wrong deductions thereby getting the final original list.

####3. We made a design decision of keeping a list of lists and where the MasterCombinations list would hold the list of each combination of people,items and people. We faced a challenge
#### in implementing the function for removal of wrong combinations as we were removing the items while iterating which resulted in wrong indexing and gave us the wrong combinations. This was
### rectified by adding the condition for removal after iterating over all the items in the combination and then removing false combinations.


count = 0
ct1=0
ct=0
MasterCombinations = []
people = ['Irene', 'Frank', 'George', 'Heather', 'Jerry']
items = ['Candelabraum', 'Banister', 'Doorknob', 'Elephant', 'Amplifier']
places = ['Kirkwood Street', 'Lake Avenue', 'Orange Drive', 'North Avenue', 'Maxwell Street']
for a in itertools.permutations(places):
    for b in itertools.permutations(items):
        count+=1
        alist = (a, b, people)
        MasterCombinations.append(alist)
#print 'Total Combinations '+str(count)
removeList=[]
for combi in MasterCombinations:
    ct1+=1
    received=['','','','','']
    valFlag = 'Y'
    for i in range(0,5):
        if(combi[1][i]=='Candelabraum'):
            if (received[i] == '') or (received[i] == 'Banister'):
                received[i] = 'Banister'
            else:
                valFlag = 'N'
                break
        if(combi[1][i]=='Banister'):
            if (received[i] == '') or (received[i] == combi[1][(combi[2].index('Irene'))]):
                received[i] = combi[1][(combi[2].index('Irene'))]
            else:
                valFlag = 'N'
                break
        if(combi[2][i]=='Frank'):
            if (received[i] == '') or (received[i] == 'Doorknob'):
                received[i] = 'Doorknob'
            else:
                valFlag = 'N'
                break
        if(combi[0][i]=='Kirkwood Street'):
            if (received[i] == '') or (received[i] == combi[1][(combi[2].index('George'))]):
                received[i] = combi[1][(combi[2].index('George'))]
            else:
                valFlag = 'N'
                break
        if(combi[0][i]=='Lake Avenue'):
            if (received[i] == '') or (received[i] == combi[1][(combi[0].index('Kirkwood Street'))]):
                received[i] = combi[1][(combi[0].index('Kirkwood Street'))]
            else:
                valFlag = 'N'
                break
        if(combi[2][i]=='Heather'):
            if (received[i] == '') or (received[i] == combi[1][(combi[0].index('Orange Drive'))]):
                received[i] = combi[1][(combi[0].index('Orange Drive'))]
            else:
                valFlag = 'N'
                break
        if(combi[2][i]=='Jerry'):
            if (received[i] == '') or (received[i] == combi[1][(combi[2].index('Heather'))]):
                received[i] = combi[1][(combi[2].index('Heather'))]
            else:
                valFlag = 'N'
                break
        if(combi[0][i]=='North Avenue'):
            if (received[i] == '') or (received[i] == 'Elephant'):
                received[i] = 'Elephant'
            else:
                valFlag = 'N'
                break
        if(combi[1][i]=='Elephant'):
            if (received[i] == '') or (received[i] == combi[1][(combi[0].index('Maxwell Street'))]):
                received[i] = combi[1][(combi[0].index('Maxwell Street'))]
            else:
                valFlag = 'N'
                break
        if(combi[0][i]=='Maxwell Street'):
            if (received[i] == '') or (received[i] == 'Amplifier'):
                received[i] = 'Amplifier'
            else:
                valFlag = 'N'
                break
    if (received[0]==combi[1][0]) or (received[0] == '') or (received[1]==combi[1][1]) or (received[1] == '') or (received[2]==combi[1][2]) or (received[2] == '') or (received[3]==combi[1][3]) or (received[3] == '') or (received[4]==combi[1][4]) or (received[4] == '') or (valFlag == 'N'):
        #MasterCombinations.remove(combi)
        removeList.append(combi)

for cntr in removeList:
    MasterCombinations.remove(cntr)

print "The items ordered by each person at their respective addresses were as follows"

for i in MasterCombinations:
  #  ct+=1
    for j in range(0,5):
        print i[2][j] +" ordered " + i[1][j] + " at "+ i[0][j]
    print "\n\n"
#print ct





