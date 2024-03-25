import urllib.request
print('Your Weather Report')
print()
print('Current observations are avialable for:')
print('- Chicago')
print('- Houston')
print('- Los Angeles')
print('- New York')
name = input('Enter the city you would like a weather report for: ')
while True:
    if name != "Chicago" and name != "Houston" and name != "Los Angeles" and name != "New York":
        name = input('No data available. Please try another city: ')
    else:
        print ('Accessing weather data...')
############## CHICAGO #################       
        if name == "Chicago":
            url = 'https://w1.weather.gov/xml/current_obs/display.php?stid=KMDW'
            try:
                response = urllib.request.urlopen(url)
                data = response.read().decode('utf-8')
                splitdata = data.split("\n")
            except:
                print('Something went wrong.')
            else:
                print('')
                print('The current weather has been accessed for Chicago')
                print('')         
            print('Information Available:')
            print('- location')
            print('- weather')
            print('- temperatura')
            print('- humidity')
            print('- wind')
            print('- observation')
            print('')
            need = input('What weather information would you like? ')
            while True:
                if need != "location" and need != "weather" and need != "temperature" and need != "humidity" and need != "wind" and need != "observation" and need != "done":
                    print("That data is not available")
                    print()
                    need = input("""What weather information would you like? Or, to end, enter "done".""")
                else:                  
                    if need == "location":
                        print('The location is ',splitdata[24][11:-11])
                        print()
                    elif need == "weather":
                        print('The weather in Chicago is', splitdata[30][10:-10])
                        print()
                    elif need == "temperature":
                        print('The temperature in Chicago is',splitdata[32][9:-9],'degrees F')
                        print()
                    elif need == "humidity":
                        print('The humidity in Chicago is', splitdata[34][20:-20] + "%")
                        print()
                    elif need == "wind":
                        print('The wind in Chicago is', splitdata[35][14:-14])
                        print()
                    elif need == "observation":
                        print('The observation in Chicago', splitdata[28][19:-19])
                        print()
                    elif need == "done":
                        print()
                        export = input('Would you like to export the weather report and generate a data visualization?(yes/no): ')
                        if export == "yes":
                            f = open('report.txt', 'w')
                            f.write('Weather for Chicago\n')
                            f.write('\n')
                            f.write('Location:'+splitdata[24][11:-11]+'\n')
                            f.write('Weather:'+splitdata[30][10:-10]+'\n')
                            f.write('Observation:'+splitdata[28][19:-19]+'\n')
                            f.write('Temperature:'+splitdata[32][9:-9]+' degrees F'+'\n')
                            f.write('Wind:'+splitdata[35][14:-14]+'\n')
                            f.write('Humidity:'+splitdata[34][20:-20]+'%'+'\n')
                            f.close()
                            print('The full weather report has been exported,')
                            print('generating your visualization...')
                            #import Turtle
                            break
                        elif export == "no":
                            break
                    need = input("""What weather information would you like? Or, to end, enter "done".""")
################ HOUSTON #################
        elif name == "Houston":
            url = 'https://w1.weather.gov/xml/current_obs/display.php?stid=KDKR'
            try:
                response = urllib.request.urlopen(url)
                data = response.read().decode('utf-8')
                splitdata = data.split("\n")
            except:
                print('Something went wrong.')
            else:
                print('')
                print('The current weather has been accessed for Los Angeles')
                print('')     
            print('Information Available:')
            print('- location')
            print('- weather')
            print('- temperatura')
            print('- humidity')
            print('- wind')
            print('- observation')
            print('')
            need = input('What weather information would you like? ')
            while True:
                if need != "location" and need != "weather" and need != "temperature" and need != "humidity" and need != "wind" and need != "observation" and need != 'done':
                    print("That data is not available")
                    print()
                    need = input("""What weather information would you like? Or, to end, enter "done".""")
                else:
                    if need == "location":
                        print('The location is',splitdata[24][11:-11])
                        print()
                    elif need == "weather":
                        print('The weather in Houston is', splitdata[30][10:-10])
                        print()
                    elif need == "temperature":
                        print('The temperature in Houston is',splitdata[32][9:-9],'degrees F')
                        print()
                    elif need == "humidity":
                        print('The humidity in Houston is', splitdata[34][20:-20] + "%")
                        print()
                    elif need == "wind":
                        print('The wind in Houston is', splitdata[35][14:-14])
                        print()
                    elif need == "observation":
                        print('The observation in Houston', splitdata[28][19:-19])
                        print()
                    elif need == "done":

                        export = input('Would you like to export the weather report and generate a data visualization?(yes/no): ')

                        if export == "yes":

                            f = open('report.txt', 'w')

                            f.write('Weather for Houston\n')
                            f.write('\n')
                            f.write('Location:'+splitdata[24][11:-11]+'\n')
                            f.write('Weather:'+splitdata[30][10:-10]+'\n')
                            f.write('Observation:'+splitdata[28][19:-19]+'\n')
                            f.write('Temperature:'+splitdata[32][9:-9]+' degrees F'+'\n')
                            f.write('Wind:'+splitdata[35][14:-14]+'\n')
                            f.write('Humidity:'+splitdata[34][20:-20]+'%'+'\n')
                            f.close()
                            print('The full weather report has been exported,')
                            print('generating your visualization...')
                            #import Turtle
                            break
                        elif export == "no":
                            break
                    need = input("""What weather information would you like? Or, to end, enter "done".""")
############### LOS ANGELES ###############
        elif name == "Los Angeles":
            url = 'https://w1.weather.gov/xml/current_obs/display.php?stid=KLAX'
            try:
                response = urllib.request.urlopen(url)
                data = response.read().decode('utf-8')
                splitdata = data.split("\n")
            except:
                print('Something went wrong.')
            else:
                print('')
                print('The current weather has been accessed for Los Angeles')
                print('')
            print('Information Available:')
            print('- location')
            print('- weather')
            print('- temperatura')
            print('- humidity')
            print('- wind')
            print('- observation')
            print('')

            need = input('What weather information would you like? ')

            while True:

                if need != "location" and need != "weather" and need != "temperature" and need != "humidity" and need != "wind" and need != "observation" and need != "done":
                    print("That data is not available")
                    print()

                    need = input("""What weather information would you like? Or, to end, enter "done".""")

                else:

                    if need == "location":

                        print('The location is',splitdata[24][11:-11])
                        print()

                    elif need == "weather":

                        print('The weather in Los Angeles is', splitdata[30][10:-10])
                        print()

                    elif need == "temperature":
                        
                        print('The temperature in Los Angeles is',splitdata[32][9:-9],'degrees F')
                        print()

                    elif need == "humidity":

                        print('The humidity in Los Angeles is', splitdata[34][20:-20] + "%")
                        print()

                    elif need == "wind":

                        print('The wind in Los Angeles is', splitdata[35][14:-14])
                        print()

                    elif need == "observation":

                        print('The observation in Los Angeles is', splitdata[28][19:-19])

                    elif need == "done":

                        export = input('Would you like to export the weather report and generate a data visualization?(yes/no): ')

                        if export == 'yes':

                            f = open('report.txt', 'w')

                            f.write('Weather for Los Angeles\n')
                            f.write('\n')
                            f.write('Location:'+splitdata[24][11:-11]+'\n')
                            f.write('Weather:'+splitdata[30][10:-10]+'\n')
                            f.write('Observation:'+splitdata[28][19:-19]+'\n')
                            f.write('Temperature:'+splitdata[32][9:-9]+' degrees F'+'\n')
                            f.write('Wind:'+splitdata[35][14:-14]+'\n')
                            f.write('Humidity:'+splitdata[34][20:-20]+'%'+'\n')

                            f.close()

                            print('The full weather report has been exported,')
                            print('generating your visualization...')

                            #import Turtle

                            

                            break

                        elif export == "no":

                            break
                    need = input("""What weather information would you like? Or, to end, enter "done".""")

                
########### NEW YORK ##########
        elif name == "New York":
            url = 'https://w1.weather.gov/xml/current_obs/KLGA.xml'
            try:
                response = urllib.request.urlopen(url)
                data = response.read().decode('utf-8')
                splitdata = data.split("\n")
            except:       
                print('Something went wrong.')
            else:
                print('')
                print('The current weather has been accessed for New York')
                print('')
            print('Information Available:')
            print('- location')
            print('- weather')
            print('- temperatura')
            print('- humidity')
            print('- wind')
            print('- observation')
            print('')

            need = input('What weather information would you like? ')

            while True:

                if need != "location" and need != "weather" and need != "temperature" and need != "humidity" and need != "wind" and need != "observation" and need != "done":
                    print("That data is not available")
                    print()

                    need = input("""What weather information would you like? Or, to end, enter "done".""")

                else:

                    if need == "location":

                        print('The location is',splitdata[15][11:-11])
                        print()

                    elif need == "weather":

                        print('The weather in New York is', splitdata[21][10:-10])
                        print()

                    elif need == "temperature":
                        
                        print('The temperature in New York is',splitdata[23][9:-9],'degrees F')
                        print()

                    elif need == "humidity":

                        print('The humidity in New York is', splitdata[25][20:-20] + "%")
                        print()

                    elif need == "wind":

                        print('The wind in New York is', splitdata[26][14:-14])
                        print()

                    elif need == "observation":

                        print('The observation in New York', splitdata[19][19:-19])
                        print()
                    elif need == "done":
                        export = input('Would you like to export the weather report and generate a data visualization?(yes/no): ')
                        if export == 'yes':
                            f = open('report.txt', 'w')
                            f.write('Weather for New York\n')
                            f.write('\n')
                            f.write('Location:'+splitdata[15][11:-11]+'\n')
                            f.write('Weather:'+splitdata[21][10:-10]+'\n')
                            f.write('Observation:'+splitdata[19][19:-19]+'\n')
                            f.write('Temperature:'+splitdata[23][9:-9]+' degrees F'+'\n')
                            f.write('Wind:'+splitdata[26][14:-14]+'\n')
                            f.write('Humidity:'+splitdata[25][20:-20]+'%'+'\n')
                            f.close()
                            print('The full weather report has been exported,')
                            print('generating your visualization...')
                            #import Turtle
                            break
                        elif export == "no":
                            break
                    need = input("""What weather information would you like? Or, to end, enter "done".""")
        else:
            name = input("No data available. Please try another city: ")
        break
    


    


