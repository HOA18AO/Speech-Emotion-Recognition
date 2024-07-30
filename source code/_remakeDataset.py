import os
import librosa
import shutil

# create '_train/'
for folder in os.listdir('TESS/'):
    if '.' in os.path.basename(folder): # not a folder
        continue
    destination = folder.split('_')[-1].lower()
    print(destination)
    for file in os.listdir('TESS/' + folder):
        #print(file)
        if file.endswith('.wav'):
            filePath = os.path.join('TESS/' + folder + '/' + file)
            destinationPath = os.path.join('_train/' + destination)
            if not os.path.exists(destinationPath + '/' + filePath):
                shutil.copy(filePath, destinationPath)

# create '_test'
# this is gonna skip some files that are 'repetition'
for folder in os.listdir('RAVDESS/'):
    # print('here')
    if '.' in os.path.basename(folder): # not a folder
        continue # skip
    for f in os.listdir('RAVDESS/' + folder + '/'):
        # print(1)
        if f.endswith('.wav'):
            box = f.split('.')[0].split('-')
            print(box)
            # box[0] == '03', box[1] == '01'
            definition = {
                'emotion' : '', # box[2]
                'intensity' : '', # box[3]
                'statement' : '', # box[4]
                'speaker' : box[6], # box[6]
            }
            if box[2] == '01' or box[2] == '02':
                definition['emotion'] = 'neutral'
            elif box[2] == '03':
                definition['emotion'] = 'happy'
            elif box[2] == '04':
                definition['emotion'] = 'sad'
            elif box[2] == '05':
                definition['emotion'] = 'angry'
            elif box[2] == '06':
                definition['emotion'] = 'fear'
            elif box[2] == '07':
                definition['emotion'] = 'disgust'
            elif box[2] == '08':
                definition['emotion'] = 'surprise'
            else:
                definition['emotion'] = '?emotion'
            
            if box[3] == '01':
                definition['intensity'] = 'normal'
            elif box[3] == '02':
                definition['intensity'] = 'strong'
            else:
                definition['intensity'] = '?intensity'
            
            if box[4] == '01':
                definition['statement'] = 'kids'
            elif box[4] == '02':
                definition['statement'] = 'dogs'
            else:
                definition['statement'] = '?statement'
            
            # Generate the new file name
            fileName = f"{definition['emotion']}_{definition['intensity']}_{definition['statement']}_{definition['speaker']}.wav"
            print(fileName)
            # Define current file path and destination path
            current_file_path = os.path.join('RAVDESS/' + folder + '/' + f)
            destination_folder = os.path.join('_test', definition['emotion'])
            if not os.path.exists(destination + '/' + fileName):
                shutil.copy(current_file_path, destination_folder + '/' + fileName)
            # move
            #if not os.path.exists(destinationPath + file):