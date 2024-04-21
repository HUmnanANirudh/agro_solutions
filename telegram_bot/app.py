from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler,filters

msp_data = {
    'Paddy': {
        'Common': {
            '2022-2023': 2040,
            '2023-2024': 2183,
            'Increase': 143
        },
        'Grade A': {
            '2022-2023': 2060,
            '2023-2024': 2203,
            'Increase': 143
        }
    },
    'Jowar': {
        'Hybrid': {
            '2022-2023': 2970,
            '2023-2024': 3180,
            'Increase': 210
        },
        'Maldandi': {
            '2022-2023': 2990,
            '2023-2024': 3225,
            'Increase': 235
        }
    },
    'Bajra': {
        '': {
            '2022-2023': 2350,
            '2023-2024': 2500,
            'Increase': 150
        }
    },
    'Maize': {
        '': {
            '2022-2023': 1962,
            '2023-2024': 2090,
            'Increase': 128
        }
    },
    'Ragi': {
        '': {
            '2022-2023': 3578,
            '2023-2024': 3846,
            'Increase': 268
        }
    },
    'Arhar (Tur)': {
        '': {
            '2022-2023': 6600,
            '2023-2024': 7000,
            'Increase': 400
        }
    },
    'Moong': {
        '': {
            '2022-2023': 7755,
            '2023-2024': 8558,
            'Increase': 803
        }
    },
    'Urad': {
        '': {
            '2022-2023': 6600,
            '2023-2024': 6950,
            'Increase': 350
        }
    },
    'Cotton': {
        'Medium Staple': {
            '2022-2023': 6080,
            '2023-2024': 6620,
            'Increase': 540
        },
        'Long Staple': {
            '2022-2023': 6380,
            '2023-2024': 7020,
            'Increase': 640
        }
    },
    'Groundnut in shell': {
        '': {
            '2022-2023': 5850,
            '2023-2024': 6377,
            'Increase': 527
        }
    },
    'Sunflower seed': {
        '': {
            '2022-2023': 6400,
            '2023-2024': 6760,
            'Increase': 360
        }
    },
    'Soyabeen': {
        'Yellow': {
            '2022-2023': 4300,
            '2023-2024': 4600,
            'Increase': 300
        }
    },
    'Sesamum': {
        '': {
            '2022-2023': 7830,
            '2023-2024': 8635,
            'Increase': 805
        }
    },
    'Nigerseed': {
        '': {
            '2022-2023': 7287,
            '2023-2024': 7734,
            'Increase': 447
        }
    },
    'Wheat': {
        '': {
            '2024-2025': 2125,
            '2024-2025': 2275,
            'Increase': 150
        }
    },
    'Barley': {
        '': {
            '2024-2025': 1735,
            '2024-2025': 1850,
            'Increase': 115
        }
    },
    'Gram': {
        '': {
            '2024-2025': 5335,
            '2024-2025': 5440,
            'Increase': 105
        }
    },
    'Masur (Lentil)': {
        '': {
            '2024-2025': 6000,
            '2024-2025': 6425,
            'Increase': 425
        }
    },
    'Rapeseed & Mustard': {
        '': {
            '2024-2025': 5450,
            '2024-2025': 5650,
            'Increase': 200
        }
    },
    'Safflower': {
        '': {
            '2024-2025': 5650,
            '2024-2025': 5800,
            'Increase': 150
        }
    },
    'Toria': {
        '': {
            '2024-2025': 5050,
            '2024-2025': 5450,
            'Increase': 400
        }
    },
    'Copra': {
        'Milling': {
            '2024-2025': 10860,
            '2024-2025': 11160,
            'Increase': 300
        },
        'Ball': {
            '2024-2025': 11750,
            '2024-2025': 12000,
            'Increase': 250
        }
    },
    'De-husked coconut': {
        '': {
            '2023-2024': 2860,
            '2023-2024': 2930,
            'Increase': 70
        }
    },
    'Raw Jute': {
        'TDN-3 equivalent to earlier TD-5 grade': {
            '2024-2025': 5050,
            '2024-2025': 5335,
            'Increase': 285
        }
    },
    'Sugarcane': {
        '$': {
            '2024-2025': 340,
            '2024-2025': 0,  
            'Increase': 0    
        }
    }
}


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome! Please select your preferred language:\n\n1. English\n2. Hindi')

async def select_language(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()
    if 'english' in text:
        context.user_data['language'] = 'english'
        await update.message.reply_text('You have selected English.')
        await update.message.reply_text('What do you want to do?\n\n1. Get updates on MSP prices,/msp\n2. Secure a contract (Visit our website at [YOUR_WEBSITE_URL])\n3. Manage agricultural waste (Visit our website at [YOUR_WEBSITE_URL])')
    elif 'hindi' in text:
        context.user_data['language'] = 'hindi'
        await update.message.reply_text('आपने हिंदी का चयन किया है।')
        await update.message.reply_text('आप क्या करना चाहते हैं?\n\n1. MSP की कीमतों पर अपडेट प्राप्त करें, /msp\n2. एक संविदा सुरक्षित करें(हमारी वेबसाइट पर जाएं [YOUR_WEBSITE_URL])\n3. कृषि अपशिष्ट प्रबंधित करें (हमारी वेबसाइट पर जाएं [YOUR_WEBSITE_URL])')

def display_msp(msp_data):
    msp_response = ""
    for commodity, varieties in msp_data.items():
        msp_response += f"{commodity}\n"
        for variety, details in varieties.items():
            msp_response += f"- {variety}:\n"
            for year, price in details.items():
                if year != "Increase":
                    msp_response += f"  {year}: {price} Rs per quintal\n"
                else:
                    msp_response += f"  Increase over previous year: {price} Rs per quintal\n"
            msp_response += "\n"
    return msp_response

async def msp_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    language = context.user_data.get('language', 'english')
    msp_text = display_msp(msp_data)  
    await update.message.reply_text(msp_text, parse_mode='Markdown')

def error(update, context):
    print(f'Update {update} caused error {context.error}')

app = (
    ApplicationBuilder().token('token').build()
)

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start_command))
app.add_handler(MessageHandler(filters.Regex(r'(1|english|2|hindi)'), select_language))
app.add_handler(CommandHandler('msp', msp_command))
app.add_error_handler(error)

app.run_polling()
