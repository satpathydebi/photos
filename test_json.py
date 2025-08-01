import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Define the synthetic data structure based on the provided variables
data = {
    'AGE (V1)': np.random.choice([1, 2, 3, 4, 5], size=1600),
    'GENDER (V2)': np.random.choice([1, 2, 3], size=1600),
    'GRADE (V3)': np.random.choice([1, 2], size=1600),
    'POCKET MONEY (V4)': np.random.choice([1, 2, 3, 4, 5, 6, 7, 8], size=1600),
    'EVER TRIED SMOKING CIGARETTE (V5)': np.random.choice([1, 2], size=1600),
    'AGE YOU FIRST CIGARETTE (V6)': np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], size=1600),
    'PAST 30 DAYS, HOW MANY DAYS YOU SMOKE CIGARETTES (V7)': np.random.choice([1, 2, 3, 4, 5, 6, 7], size=1600),
    'PAST 30 DAYS, HOW MANY CIG YOU SMOKE PER DAY (V8)': np.random.choice([1, 2, 3, 4, 5, 6, 7], size=1600),
    'PAST 30 DAYS, HOW DID YOU GET THEM? CIG (V9)': np.random.choice([1, 2, 3, 4, 5, 6, 7], size=1600),
    'PAST 30 DAYS, DID ANYONE REFUSE TO SELL CIG DUE TO AGE? (V10)': np.random.choice([1, 2, 3], size=1600),
    'PAST 30 DAYS, HOW DID YOU BUY THEM? CIG (V11)': np.random.choice([1, 2, 3, 4, 5], size=1600),
    'HOW MUCH YOU THINK A PACK OF CIGARETTE COST? (V12)': np.random.choice([1, 2, 3, 4, 5, 6, 7], size=1600),
    'EVER TRIED SMOKING BIDI (V13)': np.random.choice([1, 2], size=1600),
    'AGE YOU FIRST BIDI (V14)': np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], size=1600),
    'PAST 30 DAYS, HOW MANY DAYS YOU SMOKE BIDI (V15)': np.random.choice([1, 2, 3, 4, 5, 6, 7], size=1600),
    'PAST 30 DAYS, HOW MANY BIDI YOU SMOKE PER DAY (V16)': np.random.choice([1, 2, 3, 4, 5, 6, 7], size=1600),
    'PAST 30 DAYS, HOW DID YOU GET THEM? BIDI (V17)': np.random.choice([1, 2, 3, 4, 5, 6, 7], size=1600),
    'PAST 30 DAYS, DID ANYONE REFUSE TO SELL BIDI DUE TO AGE? (V18)': np.random.choice([1, 2, 3], size=1600),
    'PAST 30 DAYS, HOW DID YOU BUY THEM? BIDI (V19)': np.random.choice([1, 2, 3, 4, 5], size=1600),
    'HOW MUCH YOU THINK A PACK OF BIDI COST? (V20)': np.random.choice([1, 2, 3, 4, 5, 6], size=1600),
    'EVER TRIED WITH ANY FORM OF SMOKED TOBACCO PRODUCTS (V21)': np.random.choice([1, 2], size=1600),
    'PAST 30 DAYS, DID YOU USE ANY FORM OF SMOKED TOBACCO PRODUCTS (V22)': np.random.choice([1, 2], size=1600),
    'BEFORE TODAY HAVE YOU HEARD OF E-CIG ANY SUCH LIKE DEVICES? (V23)': np.random.choice([1, 2], size=1600),
    'EVER EXPERIMENTED/USED E-CIG OR ANY SUCH? (V24)': np.random.choice([1, 2], size=1600),
    'DO YOU USUALLY SMOKE TOBACCO FIRST THING IN THE MORNING OR FEEL LIKE SMOKING TOBACCO FIRST THING IN THE MORNING? (V25)': np.random.choice([1, 2, 3], size=1600),
    'HOW SOON AFTER YOU SMOKED TOBACCO DO YOU START TO FEEL A STRONG DESIRE TO SMOKE AGAIN THAT IS HARD TO IGNORE? (V26)': np.random.choice([1, 2, 3, 4, 5, 6, 7, 8], size=1600),
    'WHERE DO YOU USUALLY SMOKE? (V27)': np.random.choice([1, 2, 3, 4, 5, 6, 7, 8], size=1600),
    'DO YOU WANT TO STOP SMOKING NOW? (V28)': np.random.choice([1, 2, 3, 4], size=1600),
    'DURING THE PAST 12 MONTHS, DID YOU EVER TRY TO STOP SMOKING? (V29)': np.random.choice([1, 2, 3, 4], size=1600),
    'DO YOU THINK YOU WOULD BE ABLE TO STOP SMOKING IF YOU WANTED TO? (V30)': np.random.choice([1, 2, 3, 4], size=1600),
    'HAVE YOU EVER RECEIVED HELP OR ADVICE TO HELP YOU STOP SMOKING? (V31)': np.random.choice([1, 2, 3, 4, 5, 6], size=1600),
    'HOW LONG AGO DID YOU STOP SMOKING? (V32)': np.random.choice([1, 2, 3, 4, 5, 6, 7], size=1600),
    'WHAT WAS THE REASON YOU DECIDED TO STOP SMOKING? (V33)': np.random.choice([1, 2, 3, 4, 5, 6, 7], size=1600),
    'HAVE YOU HEARD ABOUT TOBACCO QUITLINE? (V34)': np.random.choice([1, 2], size=1600),
    'HAVE YOU EVER CALLED THE TOBACCO QUITLINE? (V35)': np.random.choice([1, 2], size=1600),
    'DURING THE PAST 7 DAYS, ON HOW MANY DAYS HAS ANYONE SMOKED INSIDE YOUR HOME, IN YOUR PRESENCE? (V36)': np.random.choice([1, 2, 3, 4, 5, 6], size=1600),
    'DURING THE PAST 7 DAYS, ON HOW MANY DAYS HAS ANYONE SMOKED IN YOUR PRESENCE, INSIDE ANY ENCLOSED PUBLIC PLACE? (V37)': np.random.choice([1, 2, 3, 4, 5], size=1600),
    'DURING THE PAST 7 DAYS, ON HOW MANY DAYS HAS ANYONE SMOKED IN YOUR PRESENCE, AT ANY OUTDOOR PUBLIC PLACE? (V38)': np.random.choice([1, 2, 3, 4, 5], size=1600),
    'DURING THE PAST 30 DAYS, DID YOU SEE ANYONE SMOKE INSIDE THE SCHOOL BUILDING OR OUTSIDE ON SCHOOL PROPERTY? (V39)': np.random.choice([1, 2], size=1600),
    'DO YOU THINK THE SMOKE FROM OTHER PEOPLE’S TOBACCO SMOKING IS HARMFUL TO YOU? (V40)': np.random.choice([1, 2, 3, 4], size=1600),
    'DO YOU SUPPORT THE BAN ON SMOKING INSIDE ENCLOSED PUBLIC PLACES? (V41)': np.random.choice([1, 2], size=1600),
    'DO YOU SUPPORT THE BAN ON SMOKING AT OUTDOOR PUBLIC PLACES? (V42)': np.random.choice([1, 2], size=1600),
    'HAVE YOU EVER TRIED OR EXPERIMENTED WITH TOBACCO LEAF (V43I)': np.random.choice([1, 2], size=1600),
    'HAVE YOU EVER TRIED OR EXPERIMENTED WITH BETEL QUID WITH TOBACCO /PAAN (V43II)': np.random.choice([1, 2], size=1600),
     'HAVE YOU EVER TRIED OR EXPERIMENTED WITH SADA/ SURTI, KHAINI OR TOBACCO LIME MIXTURE (V43III)': np.random.choice([1, 2], size=1600),
    'HAVE YOU EVER TRIED OR EXPERIMENTED WITH GUTKHA (V43IV)': np.random.choice([1, 2], size=1600),
    'HAVE YOU EVER TRIED OR EXPERIMENTED WITH PAAN MASALA TOGETHER WITH TOBACCO (V43V)': np.random.choice([1, 2], size=1600),
    'HAVE YOU EVER TRIED OR EXPERIMENTED WITH MAWA (MIXTURE OF SUPARI, ZARDA, LIME, ETC.) (V43VI)': np.random.choice([1, 2], size=1600),
    'HAVE YOU EVER TRIED OR EXPERIMENTED WITH GUL (V43VII)': np.random.choice([1, 2], size=1600),
    'HAVE YOU EVER TRIED OR EXPERIMENTED WITH GUDAKHU (V43VIII)': np.random.choice([1, 2], size=1600),
    'HAVE YOU EVER TRIED OR EXPERIMENTED WITH SNUFF (V43XI)': np.random.choice([1, 2], size=1600),
    'HAVE YOU EVER TRIED OR EXPERIMENTED WITH OTHERS (V43X)': np.random.choice([1, 2], size=1600),
    'HOW OLD WERE YOU WHEN YOU FIRST TRIED SMOKELESS TOBACCO? (V44)': np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], size=1600),
    'DURING THE PAST 30 DAYS, DID YOU USE ANY FORM OF SMOKELESS TOBACCO PRODUCTS? (V45)': np.random.choice([1, 2], size=1600),
    'DURING THE PAST 30 DAYS, ON HOW MANY DAYS DID YOU USE SMOKELESS TOBACCO? (V46)': np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], size=1600),
    'THE LAST TIME YOU USED SMOKELESS TOBACCO DURING THE PAST 30 DAYS, HOW DID YOU GET THEM? (V47)': np.random.choice([1, 2, 3, 4, 5, 6, 7], size=1600),
    'DURING THE PAST 30 DAYS, DID ANYONE REFUSE TO SELL YOU SMOKELESS TOBACCO BECAUSE OF YOUR AGE? (V48)': np.random.choice([1, 2, 3], size=1600),
    'THE LAST TIME YOU BOUGHT SMOKELESS TOBACCO DURING THE PAST 30 DAYS, HOW DID YOU BUY THEM? (V49)': np.random.choice([1, 2, 3, 4], size=1600),
    'ON AVERAGE, HOW MUCH DO YOU THINK A SINGLE USE POUCH OF SMOKELESS TOBACCO COSTS? (V50)': np.random.choice([1, 2, 3, 4, 5, 6], size=1600),
})

# This will print the dictionary to verify the structure
print(data)
