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
#TODO: ReadFile 
#nomes =['Tomas1207']
x= 986/1173
y= 1229/1265
x1 = 988/1171
y1 = 1228/1266
userinput = "desert"
counter = 0
total = len(nomes)
for nome in nomes:
    counter +=1
    printProgressBar(counter,total,prefix="Progress:",suffix='Complete', length=50)
    if userinput == "desert":
        image = Image.open('.\Image\Main2.jpg')
        if len(nome) > 10:
            font_type = ImageFont.truetype('.\LLLIBERT.TTF',24)
        else:
            font_type = ImageFont.truetype('.\LLLIBERT.TTF',26)

        im = ImageOps.mirror(image)
        draw = ImageDraw.Draw(im)
        text = draw.textsize(nome[::-1],font_type)
        draw.text(xy=(((1060+874)/2)-text[0]/2,((1267+1227)/2)-text[1]/2),text=nome,font=font_type)
        nome = nome.replace(" ","").lower()
        im.save("mirrorImagens/PT_DPM_Desert_"+ nome +"_vests.png")

        imagepos = Image.open("mirrorImagens/PT_DPM_Desert_"+ nome +"_vests.png")
        img = ImageOps.mirror(imagepos)
        
        img.save("FinalImagens/PT_DPM_Desert_"+ nome + "_vests.png")
        
        driveinfo = subprocess.Popen(f'powershell.exe ..\ImageToPAA\ImageToPAA.exe ..\\PTsimsColetes\\FinalImagens\\PT_DPM_Desert_{nome}_vests.png ..\Mod\\addons\\pt_items\\data\\DPM\\PT_DPM_Desert_{nome}_vests.paa',stdout=subprocess.DEVNULL)
    else:
        image = Image.open('.\Image\Main.jpg')
        if len(nome) > 10:
            font_type = ImageFont.truetype('.\LLLIBERT.TTF',24)
        else:
            font_type = ImageFont.truetype('.\LLLIBERT.TTF',26)

        im = ImageOps.mirror(image)
        draw = ImageDraw.Draw(im)
        text = draw.textsize(nome[::-1],font_type)
        draw.text(xy=(((1060+874)/2)-text[0]/2,((1267+1227)/2)-text[1]/2),text=nome,font=font_type)
        nome = nome.replace(" ","").lower()
        im.save("mirrorImagens/PT_DPM_"+ nome +"_vests.png")

        imagepos = Image.open("mirrorImagens/PT_DPM_"+ nome +"_vests.png")
        img = ImageOps.mirror(imagepos)
        
        img.save("FinalImagens/PT_DPM_"+ nome + "_vests.png")
        
        driveinfo = subprocess.Popen(f'powershell.exe ..\ImageToPAA\ImageToPAA.exe ..\\PTsimsColetes\\FinalImagens\\PT_DPM_{nome}_vests.png ..\Mod\\addons\\pt_items\\data\\DPM\\PT_DPM_{nome}_vests.paa',stdout=subprocess.DEVNULL)
        
    with open('..\\Mod\\addons\\pt_items\\config.cpp','r+')as config:
        lines = config.readlines()
        for line in lines:
            if userinput == "desert":
                if "PTc Desert "+nome+" Plate Carrier" in line:
                    break
            else:
                if "PTc "+nome+" Plate Carrier" in line:
                    break
        else:
            if userinput == "desert":
                template = """};\nclass DS_PT_Desert_"""+nome+"""_Plate_Carrier: V_PlateCarrier1_rgr {
            displayName = "PTc Desert """+nome+""" Plate Carrier ";
            picture = "\PT_items\data\DPM_Desert\Icon_PT_DPM_Desert_vests.paa";
            hiddenSelections[] = {
                "camo"
            };
            hiddenSelectionsTextures[] = {
                "\PT_items\data\DPM\PT_DPM_Desert_"""+nome+"""_vests.paa"
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
            else:
                template = """};\nclass DS_PT_"""+nome+"""_Plate_Carrier: V_PlateCarrier1_rgr {
            displayName = "PTc """+nome+""" Plate Carrier ";
            picture = "\PT_items\data\DPM\Icon_PT_DPM_vests.paa";
            hiddenSelections[] = {
                "camo"
            };
            hiddenSelectionsTextures[] = {
                "\PT_items\data\DPM\PT_DPM_"""+nome+"""_vests.paa"
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