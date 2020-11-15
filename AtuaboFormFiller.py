#! python3
import pyautogui, time

formData = [{'Name': 'Janet Salifn', 'Contact': '0544077323', 'Connection' : 'Native',
        'PeriodStayed' : 0, 'Gender': 'Female', 'PositionStatus' : 'No', 'Education': 2, 'EducationOther':'',
             'Age': 30, 'Live': 'Atuabo', 'LiveOther':'', 'Employment': 'Unemployed', 'Work': 'Farmer',
             'Salary': 0,
             'Married': 'No', 'Children': 'Yes', 'ChildEducationLevel':'Secondary', 'LiveAlone':'No',
             'PeopleLivingWith': 7,
             'FeaturePhones': 4, 'SmartPhones': 2, 'Network': 0, 'NetworkStrength': 0,
             'WeeklyCredit': 10, 'MonthlyCredit': 40, 'LikeTown': 'No', 'FamilyOutside': 'Yes',
             'Where': 'Tarkwa, Takoradi', 'Dislike': (0,1), 'Resources': (1, 5), 'ResourceInformation': 0,
             'AtuaboGasHelped': 0, 'ThreeThings': (4), 'ChallengesCTGG': (0), 'ChallengesOfAtuabo': (5),
             'MadeEffort': 'No', 'GetUpdated': 'No', 'HowWantUpdated': 0, 'HowWantUpdatedOther':'',
             'HowRatherUpdated': 0,
             'HowRatherUpdatedOther':'',
             'ComfortableWithIT': 'Yes', 'Token': 3, 'Fuel': 3, 'OtherFuelSource':'Yes',
             'KnowDeforestation': 'Yes',
             'EmployedMost': 'Male', 'AnotherSourceOfIncome': 'Yes', 'BusinessType': 'Factory',
             'WantHelp': 'Yes', 'KnowPeopleWhoNeedHelp': 'Yes'},
               ]

pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')
for person in formData:
            print('>>> 5-SECOND TO PAUSE TO LET USER PRESS CTRL-C <<<')
            time.sleep(5)
            print('Entering %s info...' % (person['Name']))
##            pyautogui.click(867,133)
            pyautogui.write(['\t'])
            pyautogui.write(person['Name'] + '\t')
            pyautogui.write(person['Contact'] + '\t')
            if person['Connection'] == 'Native':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            elif person['Connection'] == 'Settler':
                pyautogui.press('space')
                pyautogui.write(['down', '\t', '\t'])
            elif person['Connection'] == 'New comer':
                pyautogui.press('space')
                pyautogui.write(['down', 'down', '\t', '\t'])
            elif person['Connection'] == 'Visitor':
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', '\t', '\t'])
            if person['PeriodStayed'] == 0:
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            elif person['PeriodStayed'] == 1:
                pyautogui.press('space')
                pyautogui.write(['down', '\t', '\t', '\t'])
            elif person['PeriodStayed'] == 2:
                pyautogui.press('space')
                pyautogui.write(['down', 'down', '\t', '\t', '\t'])
            elif person['PeriodStayed'] == 3:
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', '\t', '\t', '\t'])
            if person['Gender'] == 'Female':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            elif person['Gender'] == 'Male':
                pyautogui.press('space')
                pyautogui.write(['down', '\t', '\t'])
            if person['PositionStatus'] == 'No':
                pyautogui.write(['down', '\t', '\t', '\t', '\t', '\t'])
            elif person['PositionStatus'] == 'Yes':
                pyautogui.press('space')
                print('Some more code here')
            if person['Education'] == 0:
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            elif person['Education'] == 1:
                pyautogui.press('space')
                pyautogui.write(['down', '\t', '\t', '\t'])
            elif person['Education'] == 2:
                pyautogui.press('space')
                pyautogui.write(['down', 'down', '\t', '\t', '\t'])
            elif person['Education'] == 3:
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', '\t', '\t', '\t'])
            elif person['Education'] == 4:
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', 'down', '\t', '\t', '\t'])
            elif person['Education'] == 5:
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', 'down', 'down', '\t', '\t', '\t'])
            elif person['Education'] == 6:
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', 'down', 'down', 'down'])
                pyautogui.write(person['EducationOther'] + '\t' + '\t')
            if person['Age'] <= 19:
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            elif person['Age'] <= 25:
                pyautogui.press('space')
                pyautogui.write(['down', '\t', '\t', '\t'])
            elif person['Age'] <= 35:
                pyautogui.press('space')
                pyautogui.write(['down', 'down', '\t', '\t', '\t'])
            elif person['Age'] <= 45:
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', '\t', '\t', '\t'])
            elif person['Age'] <= 55:
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', 'down', '\t', '\t', '\t'])
            elif person['Age'] <= 65:
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', 'down', 'down', '\t', '\t', '\t'])
            if person['Live'] == 'Sanzule':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            elif person['Live'] == 'Ekwe':
                pyautogui.press('space')
                pyautogui.write(['down', '\t', '\t', '\t'])
            elif person['Live'] == 'Ngalekpole':
                pyautogui.press('space')
                pyautogui.write(['down', 'down', '\t', '\t', '\t'])
            elif person['Live'] == 'Ngalekyi':
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', '\t', '\t', '\t'])
            elif person['Live'] == 'Baku':
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', 'down', '\t', '\t', '\t'])
            elif person['Live'] == 'Anokyi':
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', 'down', 'down', '\t', '\t', '\t'])
            elif person['Live'] == 'Atuabo':
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', 'down', 'down', 'down', '\t', '\t', '\t'])
            elif person['Live'] == 'Asem Nda':
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', 'down', 'down', 'down', 'down', '\t', '\t', '\t'])
            else:
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', 'down', 'down', 'down', 'down', '\t', '\t', '\t'])
                pyautogui.write(person['LiveOther'] + '\t' + '\t')
            if person['Employment'] == 'Unemployed':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            elif person['Employment'] == 'Employed':
                pyautogui.press('space')
                pyautogui.write(['down', 'down', '\t', '\t'])
                pyautogui.write(person['Work'] + '\t')
            elif person['Employment'] == 'Part-time':
                pyautogui.press('space')
                pyautogui.write(['down', '\t', '\t'])
                pyautogui.write(person['Work'] + '\t')
            if person['Salary'] == 0:
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            elif person['Salary'] == 1:
                pyautogui.press('space')
                pyautogui.write(['down', '\t', '\t', '\t'])
            elif person['Salary'] == 2:
                pyautogui.press('space')
                pyautogui.write(['down', 'down', '\t', '\t', '\t'])
            elif person['Salary'] == 3:
                pyautogui.press('space')
                pyautogui.write(['down', 'down', 'down', '\t', '\t', '\t'])
            if person['Married'] == 'No':
                pyautogui.press('space')
                pyautogui.write(['down', '\t', '\t'])
            elif person['Married'] == 'Yes':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'], 0.5)
            if person['Children'] == 'No':
                pyautogui.press('space')
                pyautogui.write([ 'down', '\t', '\t', '\t', '\t', '\t', '\t', '\t', '\t', '\t', '\t'])
            elif person['Children'] == 'Yes':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
                if person['ChildEducationLevel'] == 'Nursery':
                    pyautogui.press('space')
                    pyautogui.write(['\t', '\t', '\t', '\t', '\t', '\t', '\t', '\t'])
                elif person['ChildEducationLevel'] == 'Primary':
                    pyautogui.write(['\t'])
                    pyautogui.press('space')
                    pyautogui.write(['\t', '\t', '\t', '\t', '\t', '\t', '\t'])
                elif person['ChildEducationLevel'] == 'Secondary':
                    pyautogui.write(['\t', '\t', '\t'])
                    pyautogui.press('space')
                    pyautogui.write(['\t', '\t', '\t', '\t', '\t'])
                elif person['ChildEducationLevel'] == 'Tertiary':
                    pyautogui.write(['\t', '\t', '\t', '\t'])
                    pyautogui.press('space')
                    pyautogui.write(['\t', '\t', '\t', '\t'])
            if person['LiveAlone'] == 'No':
                pyautogui.write(['down', '\t', '\t'])
                pyautogui.write(str(person['PeopleLivingWith']) + '\t')
                pyautogui.write(str(person['FeaturePhones']) + '\t')
                pyautogui.write(str(person['SmartPhones']) + '\t')
            elif person['LiveAlone'] == 'Yes':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            if person['Network'] == 0:
                 pyautogui.press('space')
                 pyautogui.write(['\t', '\t', '\t', '\t'])
            elif person['Network'] == 1:
                pyautogui.write(['\t'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])     
            elif person['Network'] == 2:
                pyautogui.write(['\t', '\t'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            elif person['Network'] == 3:
                pyautogui.write(['\t', '\t', '\t'])
                pyautogui.press('space')
                pyautogui.write(['\t'])
            if person['NetworkStrength'] == 0:
                 pyautogui.press('space')
                 pyautogui.write(['\t', '\t'])
                 pyautogui.write(str(person['WeeklyCredit']) + '\t')
                 pyautogui.write(str(person['MonthlyCredit']) + '\t')
            elif person['NetworkStrength'] == 1:
                 pyautogui.write(['down', '\t', '\t'])
                 pyautogui.write(str(person['WeeklyCredit']) + '\t')
                 pyautogui.write(str(person['MonthlyCredit']) + '\t')
            elif person['NetworkStrength'] == 2:
                pyautogui.write(['down', 'down', '\t', '\t'])
                pyautogui.write(str(person['WeeklyCredit']) + '\t')
                pyautogui.write(str(person['MonthlyCredit']) + '\t')
            if person['LikeTown'] == 'No':
                pyautogui.write(['down', '\t', '\t'])
            elif person['LikeTown'] == 'Yes':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            if person['FamilyOutside'] == 'No':
                pyautogui.write(['down', '\t', '\t', '\t'])
            elif person['FamilyOutside'] == 'Yes':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
                pyautogui.write(person['Where'] + '\t')
            if person['Dislike'] == (0,1):
                pyautogui.press('space')
                pyautogui.write(['\t'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            elif person['Dislike'] == (0):
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            elif person['Dislike'] == (1):
                pyautogui.write(['\t'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            elif person['Dislike'] == (2):
                pyautogui.write(['\t', '\t'])
                pyautogui.press('space')
                pyautogui.write(['\t'])
            if person['Resources'] == (1,5):
                pyautogui.write(['\t'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t', '\t'])
                pyautogui.press('space')
                pyautogui.write(['\t'])
            elif person['Resources'] == (1):
                pyautogui.write(['\t'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t', '\t', '\t'])
            if person['ResourceInformation'] == 0:
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            elif person['ResourceInformation'] == 1:
                pyautogui.write(['down'])
                pyautogui.write(['\t', '\t'])
            elif person['ResourceInformation'] == 2:
                pyautogui.write(['down', 'down'])
                pyautogui.write(['\t', '\t'])
            if person['AtuaboGasHelped'] == 0:
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            elif person['AtuaboGasHelped'] == 1:
                pyautogui.write(['down'])
                pyautogui.write(['\t', '\t'])
            elif person['AtuaboGasHelped'] == 2:
                pyautogui.write(['down', 'down'])
                pyautogui.write(['\t', '\t'])
            elif person['AtuaboGasHelped'] == 3:
                pyautogui.write(['down', 'down', 'down'])
                pyautogui.write(['\t', '\t'])
            if person['ThreeThings'] == (4):
                pyautogui.write(['\t', '\t', '\t', '\t'])
                pyautogui.press('space')
                pyautogui.write(['\t'])
            elif person['ThreeThings'] == (2):
                pyautogui.write(['\t', '\t'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            if person['ChallengesCTGG'] == (0):
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t', '\t', '\t'])
            elif person['ChallengesCTGG'] == (0,1):
                pyautogui.press('space')
                pyautogui.write(['\t'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t', '\t'])
            elif person['ChallengesCTGG'] == (0,2):
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            if person['ChallengesOfAtuabo'] == (5):
                pyautogui.write(['\t', '\t', '\t', '\t', '\t'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t', '\t', '\t', '\t', '\t'])
            if person['MadeEffort'] == 'No':
                pyautogui.write(['down', '\t', '\t', '\t', '\t', '\t'])
            if person['GetUpdated'] == 'No':
                pyautogui.write(['down', '\t', '\t'])
            if person['HowWantUpdated'] == 0:
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            elif person['HowWantUpdated'] == 1:
                pyautogui.write(['down'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            elif person['HowWantUpdated'] == 2:
                pyautogui.write(['down', 'down'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            else:
                pyautogui.write(['down', 'down', 'down'])
                pyautogui.write(person['HowWantUpdatedOther'])
                pyautogui.write(['\t', '\t'])
            if person['HowRatherUpdated'] == 0:
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            elif person['HowRatherUpdated'] == 1:
                pyautogui.write(['down'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            elif person['HowRatherUpdated'] == 2:
                pyautogui.write(['down', 'down'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            elif person['HowRatherUpdated'] == 3:
                pyautogui.write(['down', 'down', 'down'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            elif person['HowRatherUpdated'] == 4:
                pyautogui.write(['down', 'down', 'down', 'down'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t', '\t'])
            else:
                pyautogui.write(['down', 'down', 'down', 'down', 'down'])
                pyautogui.write(person['HowRatherUpdatedOther'])
                pyautogui.write(['\t', '\t'])
            if person['ComfortableWithIT'] == 'Yes':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            elif person['ComfortableWithIT'] == 'No':
                pyautogui.write(['down'])
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            if person['Token'] == 1:
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            elif person['Token'] == 2:
                pyautogui.write(['down'])
                pyautogui.write(['\t', '\t'])
            elif person['Token'] == 3:
                pyautogui.write(['down', 'down'])
                pyautogui.write(['\t', '\t'])
            elif person['Token'] == 4:
                pyautogui.write(['down', 'down', 'down'])
                pyautogui.write(['\t', '\t'])
            elif person['Token'] == 5:
                pyautogui.write(['down', 'down', 'down', 'down'])
                pyautogui.write(['\t', '\t'])
            elif person['Token'] == 10:
                pyautogui.write(['down', 'down', 'down', 'down', 'down'])
                pyautogui.write(['\t', '\t'])
            if person['Fuel'] == 3:
                pyautogui.write(['\t', '\t', '\t'])
                pyautogui.press('space')
                pyautogui.write(['\t'])
            if person['OtherFuelSource'] == 'Yes':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            else:
                pyautogui.write(['down'])
                pyautogui.write(['\t', '\t'])
            if person['KnowDeforestation'] == 'Yes':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            else:
                pyautogui.write(['down'])
                pyautogui.write(['\t', '\t'])
            if person['EmployedMost'] == 'Male':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            elif person['EmployedMost'] == 'Female':
                pyautogui.write(['down'])
                pyautogui.write(['\t', '\t'])
            if person['AnotherSourceOfIncome'] == 'Yes':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            else:
                pyautogui.write(['down'])
                pyautogui.write(['\t', '\t'])
            if person['BusinessType'] == 'Factory':
                pyautogui.write(['down'])
                pyautogui.write(['\t', '\t'])
            if person['WantHelp'] == 'Yes':
                pyautogui.press('space')
                pyautogui.write(['\t', '\t'])
            if person['KnowPeopleWhoNeedHelp'] == 'Yes':
                pyautogui.press('space')
            else:
                pyautogui.write(['down'])
            
                                
                            
            
            
                
                
            
            
            
                
                
                
                
##            pyautogui.write(person['comments'] + '\t')
##            time.sleep(0.5)
##            pyautogui.press('enter')
##            print('Submitted form.')
##            time.sleep(5)
##            pyautogui.write(['\t', 'enter'])
            
            
        
        
        
