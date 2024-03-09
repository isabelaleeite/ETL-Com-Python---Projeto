import pandas as pd 
import os
import glob

# caminho para ler os arquivos

folder_path = 'src\\data\\raw'

# listas todos os arquivos de excel

excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

if not excel_files:
    print('Nenhum arquivo de excel encontrado.')
else:

    # dataframe = tabela na memória para guardar os conteúdos dos arquivos
    dfs = []

    for excel_files in excel_files:
     
      try: 
            # leio o arquivo de excel
          df_temp = pd.read_excel(excel_files)

           # pegar o nome do arquivo
          file_name = os.path.basename(excel_files)

          df_temp['filename'] = file_name

          
          # criar coluna chamada location
          
          if 'brasil' in file_name.lower():
            df_temp['location'] = 'br'
          elif 'france' in file_name.lower(): 
            df_temp['location'] = 'fr'
          elif 'italian' in file_name.lower(): 
            df_temp['location'] = 'it'

        #criar uma nova coluna chamada campaign

          df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')

        # guarda dados tratados dentr e um dataframe comum

          dfs.append(df_temp)

      except Exception as e:
        print(f"Erro ao ler o arquivo {excel_files}: {e}")

    if dfs:
     #concatena todas as tabelas salvas no dfs em uma unica tabela

     result = pd.concat(dfs, ignore_index=True)

    #caminho de saída

     output_file = os.path.join('src', 'data', 'ready', 'clean.xlsx')

    # configurou o motor da escrita
     writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    # leva os dados do resultado a serem escritos no motor do excel configurado

     result.to_excel(writer, index=False)

    # salva o arquivo de excel
     writer._save()

    else:
      print('Nenhum arquivo de excel encontrado.')