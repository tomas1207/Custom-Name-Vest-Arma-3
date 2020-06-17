from PIL import Image, ImageDraw,ImageFont,ImageOps
import subprocess
import sys
from subprocess import DEVNULL
import os
# Print iterations progress
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


nomes = ['Tomas1207','Mr Rato','Andre','TheBigOne','Stone Ricci','Rui_Sludge','Mata Pombos','Kaos','Crisostomo','MiTraPT','MacgyverPT','Dog','Costa','SrWer','MaG','NicoFuzu','Krespin','Rodriguez','Batman','Ranger','Birta','Telmo','Red']
types = ['Desert','DPM']
#nomes = ['Pedro7161']
#x= 986/1173
#y= 1229/1265
#x1 = 988/1171
#y1 = 1228/1266
userinput = ""

total = len(nomes)

def namecontrol(name):
    if len(name) > 10:
        font_type = ImageFont.truetype('.\LLLIBERT.TTF',24)
    else:
        font_type = ImageFont.truetype('.\LLLIBERT.TTF',26)
    return font_type

def mirroImg(image):
    return ImageOps.mirror(image)
 
def seralizenome(nome):
    return nome.replace(" ","").lower()
def textdrawonimg(mirro,nome,tipo,font_type):
    draw = ImageDraw.Draw(mirro)
    text = draw.textsize(nome[::-1],font_type)
    draw.text(xy=(((1060+874)/2)-text[0]/2,((1267+1227)/2)-text[1]/2),text=nome,font=font_type)
    nome = seralizenome(nome)
    mirro.save("mirrorImagens/PT_DPM_"+tipo+"_"+ nome +"_vests.png")

def opentypeimg(tipo):
    return Image.open(f'.\Image\{tipo}.jpg')

def unmirroandreadytopack(tipo,nome):
    nome = seralizenome(nome)
    imagepos = Image.open("mirrorImagens/PT_DPM_"+tipo+"_"+ nome +"_vests.png")
    img = mirroImg(imagepos)
    img.save("FinalImagens/PT_DPM_"+tipo+"_"+ nome + "_vests.png")

def imgageCretator(tipo):
    counter = 0
    for nome in nomes:
        counter +=1
        printProgressBar(counter,total,prefix="Progress:",suffix='Complete', length=50)
        textdrawonimg(mirroImg(opentypeimg(tipo)),nome,tipo,namecontrol(nome))
        unmirroandreadytopack(tipo,nome)
        nome = seralizenome(nome)
        driveinfo = subprocess.Popen(f'powershell.exe ..\ImageToPAA\ImageToPAA.exe ..\\PTsimsColetes\\FinalImagens\\PT_DPM_{tipo}_{nome}_vests.png ..\\Mod\\addons\\pt_items\\data\\DPM\\PT_DPM_{tipo}_{nome}_vests.paa',stdout=subprocess.DEVNULL)
        writeconfig(nome,tipo)
        

def writeconfig(nome,tipo):
    nome = seralizenome(nome)
    with open('..\\Mod\\addons\\pt_items\\config.cpp','r+')as config:
        lines = config.readlines()
        for line in lines:
                if f"PTc {tipo} {nome} Plate Carrier" in line:
                    break
           
        else:
            
            template = """};\nclass DS_PT_"""+tipo+"""_"""+nome+"""_Plate_Carrier: V_PlateCarrier1_rgr {
            displayName = "PTc """+tipo+""" """+nome+""" Plate Carrier ";
            picture = "\PT_items\data\DPM\Icon_PT_DPM_"""+tipo+"""_vests.paa";
            hiddenSelections[] = {
                "camo"
            };
            hiddenSelectionsTextures[] = {
                "\PT_items\data\DPM\PT_DPM_"""+tipo+"""_"""+nome+"""_vests.paa"
            };
            class ItemInfo: vestitem {
                uniformModel = "\A3\Characters_F\BLUFOR\equip_b_vest02.p3d";
                containerclass = "Supply120";
                mass = 50;
                hiddenSelections[] = {
                    "camo"
                };
                class HitpointsProtectionInfo {
                    class Neck {
                        hitpointName = "HitNeck";
                        armor = 8;
                        passThrough = 0.5;
                    };
                    class Arms {
                        hitpointName = "HitArms";
                        armor = 8;
                        passThrough = 0.5;
                    };
                    class Chest {
                        hitpointName = "HitChest";
                        armor = 24;
                        passThrough = 0.1;
                    };
                    class Diaphragm {
                        hitpointName = "HitDiaphragm";
                        armor = 24;
                        passThrough = 0.1;
                    };
                    class Abdomen {
                        hitpointName = "HitAbdomen";
                        armor = 24;
                        passThrough = 0.1;
                    };
                    class Body {
                        hitpointName = "HitBody";
                        passThrough = 0.1;
                    };
                };
            };
        };"""

            del lines[-1]
            lines[-1] = template
            #config.write(test)  
            with open('..\\Mod\\addons\\pt_items\\config.cpp','w+') as cenas:
                for line in lines:
                    cenas.write(line)
                cenas.write('\n};')
for tipo in types:
    imgageCretator(tipo)