import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('./app/depression.csv')

  # ¿Las personas con abuso de sustancias son más propensas a ser depresivas? R/: NO
  
  Yes = list(filter(lambda item: item['History of Substance Abuse'] == 'Yes', data)) 
  No = list(filter(lambda item: item['History of Substance Abuse'] == 'No', data)) 

  Labels = ['Yes', 'No']
  Values = [len(Yes), len(No)]

  charts.generate_pie_chart(Labels, Values)
  
'''
  # comportamiento de edades de población depresiva R/: la mayor población con depresión es entre los 50 y 64 años

  Jovenes = list(filter(lambda item: int(item['Age']) <= 29, data))
  Adultos = list(filter(lambda item: int(item['Age']) <= 49, data))
  AdultoMayor = list(filter(lambda item: int(item['Age']) <= 64, data))
  Anciano = list(filter(lambda item: int(item['Age']) >= 65, data))
  
  Labels = ['Jovenes', 'Adultos', 'AdultoMayor', 'Anciano']
  Values = Values = [len(Jovenes), len(Adultos), len(AdultoMayor), len(Anciano)]
  charts.generate_bar_chart(Labels, Values)
  

  # ¿Las personas que consumen alcohol son más propensas a ser depresivas? R/: Sí, las personas que consumen alcohol son más propensas a ser depresivas.
  
  Low = list(filter(lambda item: item['Alcohol Consumption'] == 'Low', data)) 
  Moderate = list(filter(lambda item: item['Alcohol Consumption'] == 'Moderate', data))
  High = list(filter(lambda item: item['Alcohol Consumption'] == 'High', data))
  
  Labels = ['Low', 'Moderate', 'High']
  Values = [len(Low), len(Moderate), len(High)]

  charts.generate_pie_chart(Labels, Values)

 
# ¿Las personas con historial familiar de depresion son más propensas a ser depresivas? R/: NO

  Yes = list(filter(lambda item: item['Family History of Depression'] == 'Yes', data)) 
  No = list(filter(lambda item: item['Family History of Depression'] == 'No', data)) 

  Labels = ['Yes', 'No']
  Values = [len(Yes), len(No)]

  charts.generate_pie_chart(Labels, Values)
  
'''




if __name__ == '__main__':
  run()
  
 
  



