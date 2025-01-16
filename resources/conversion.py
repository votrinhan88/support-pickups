from copy import deepcopy

def convert_ammo_config_py2xml(input:dict) -> dict:
    out = {}
    for k, v in input.items():
        assert k in ['Name', 'AmmoMax', 'AmmoMax50', 'AmmoMax100']
        
        if k in ['AmmoMax', 'AmmoMax50', 'AmmoMax100']:
            out[k] = {'@value': str(v)}
        else:
            out[k] = v
    return out


def convert_weapon_config_py2xml(input:dict) -> dict:
    out = {}
    for k, v in input.items():
        assert k in ['FireType', 'AmmoInfo', 'Speed']
        
        if k == 'AmmoInfo':
            out[k] = {'@ref': v}
        elif k == 'Speed':
            out[k] = {'@value': str(v)}
        else:
            out[k] = v
    return out


def convert_pickup_item(input:dict) -> dict:
    DELETE_TOKEN = '!DELETE'
    output = deepcopy(input)
    if output['Name'].startswith('PICKUP_WEAPON_') or output['Name'].startswith('PICKUP_VEHICLE_WEAPON_'):
        for i_r, r in enumerate(output['Rewards']['Item']):
            if r.startswith('REWARD_WEAPON_') or r.startswith('REWARD_AMMO_'):
                output['Rewards']['Item'][i_r] = DELETE_TOKEN
        while DELETE_TOKEN in output['Rewards']['Item']:
            output['Rewards']['Item'].remove(DELETE_TOKEN)
    return output


# Ammos conversion dict has 3 tags: add, update, delete + metadata
AMMOS_CONVERSION = {
    'AMMO_PISTOL': {
        'update': {'Name': 'AMMO_9MM', 'AmmoMax': 60, 'AmmoMax50': 90, 'AmmoMax100': 120},
    },
    'AMMO_SMG': {
        'add': [
            {'Name': 'AMMO_38S', 'AmmoMax': 60, 'AmmoMax50': 90, 'AmmoMax100': 120},
            {'Name': 'AMMO_40C', 'AmmoMax': 60, 'AmmoMax50': 90, 'AmmoMax100': 120},
            {'Name': 'AMMO_45C', 'AmmoMax': 60, 'AmmoMax50': 90, 'AmmoMax100': 120},
            {'Name': 'AMMO_50C', 'AmmoMax': 60, 'AmmoMax50': 90, 'AmmoMax100': 120},
        ],
        'delete': True,
    },
    'AMMO_RIFLE': {
        'update': {'Name': 'AMMO_556', 'AmmoMax': 90, 'AmmoMax50': 135, 'AmmoMax100': 180},
    },
    'AMMO_MG': {
        'update': {'Name': 'AMMO_762', 'AmmoMax': 90, 'AmmoMax50': 135, 'AmmoMax100': 180},
    },
    'AMMO_SNIPER': {
        'update': {'Name': 'AMMO_50BMG', 'AmmoMax': 30, 'AmmoMax50': 45, 'AmmoMax100': 60},
    },
    # AMMO_MINIGUN is also used for some vehicle weapons, so it's updated into a
    # new ammo type for WEAPON_MINIGUN 
    'AMMO_MINIGUN': {
        'add': [{'Name': 'AMMO_762MNG', 'AmmoMax': 300, 'AmmoMax50': 450, 'AmmoMax100': 600}],
    },
    'AMMO_SHOTGUN': {
        'add': [
            {'Name': 'AMMO_12G', 'AmmoMax': 40, 'AmmoMax50': 60, 'AmmoMax100': 80},
            {'Name': 'AMMO_20G', 'AmmoMax': 50, 'AmmoMax50': 75, 'AmmoMax100': 100},
            {'Name': 'AMMO_18MM', 'AmmoMax': 20, 'AmmoMax50': 30, 'AmmoMax100': 40},
        ],
        'delete': True,
    },
    'AMMO_STUNGUN': {},
    'AMMO_SNIPER_REMOTE': {},
    'AMMO_FIREEXTINGUISHER': {},
    'AMMO_PETROLCAN': {},
    'AMMO_GRENADELAUNCHER': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_GRENADELAUNCHER_SMOKE': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_RPG': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_STINGER': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_GRENADE': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_BALL': {},
    'AMMO_STICKYBOMB': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_SMOKEGRENADE': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_BZGAS': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_FLARE': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_MOLOTOV': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_TANK': {},
    'AMMO_SPACE_ROCKET': {},
    'AMMO_PLANE_ROCKET': {},
    'AMMO_PLAYER_LASER': {},
    'AMMO_ENEMY_LASER': {},
    'AMMO_BIRD_CRAP': {},
    'AMMO_MG_ARMORPIERCING': {},
    'AMMO_MG_FMJ': {},
    'AMMO_MG_INCENDIARY': {},
    'AMMO_MG_TRACER': {},
    'AMMO_PISTOL_FMJ': {},
    'AMMO_PISTOL_HOLLOWPOINT': {},
    'AMMO_PISTOL_INCENDIARY': {},
    'AMMO_PISTOL_TRACER': {},
    'AMMO_RIFLE_ARMORPIERCING': {},
    'AMMO_RIFLE_FMJ': {},
    'AMMO_RIFLE_INCENDIARY': {},
    'AMMO_RIFLE_TRACER': {},
    'AMMO_SMG_FMJ': {},
    'AMMO_SMG_HOLLOWPOINT': {},
    'AMMO_SMG_INCENDIARY': {},
    'AMMO_SMG_TRACER': {},
    'AMMO_SNIPER_ARMORPIERCING': {},
    'AMMO_SNIPER_EXPLOSIVE': {},
    'AMMO_SNIPER_FMJ': {},
    'AMMO_SNIPER_INCENDIARY': {},
    'AMMO_SNIPER_TRACER': {},
    'AMMO_SHOTGUN_ARMORPIERCING': {},
    'AMMO_SHOTGUN_EXPLOSIVE': {},
    'AMMO_SHOTGUN_HOLLOWPOINT': {},
    'AMMO_SHOTGUN_INCENDIARY': {},
    'AMMO_FIREWORK': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_RAILGUN': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_FLAREGUN': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_HOMINGLAUNCHER': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_PROXMINE': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_SNOWBALL': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_PIPEBOMB': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_RAYPISTOL': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_HAZARDCAN': {},
    'AMMO_TRANQUILIZER': {},
    'AMMO_FERTILIZERCAN': {},
    'AMMO_EMPLAUNCHER': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_ACIDPACKAGE': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_RAILGUNXM3': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
    'AMMO_SNOWLAUNCHER': {'update': {'AmmoMax': 4, 'AmmoMax50': 6, 'AmmoMax100': 8},},
}

# Conversion dict has 1 tags: update + update
WEAPONS_CONVERSION = {
    # Melee
    'WEAPON_UNARMED':       {'metadata': {'name': 'Unarmed',                'Group': 'Melee'}},
    'WEAPON_ANIMAL':        {'metadata': {'name': 'Animal',                 'Group': 'Melee'}},
    'WEAPON_COUGAR':        {'metadata': {'name': 'Cougar',                 'Group': 'Melee'}},
    'WEAPON_KNIFE':         {'metadata': {'name': 'Knife',                  'Group': 'Melee'}},
    'WEAPON_NIGHTSTICK':    {'metadata': {'name': 'Nightstick',             'Group': 'Melee'}},
    'WEAPON_HAMMER':        {'metadata': {'name': 'Hammer',                 'Group': 'Melee'}},
    'WEAPON_BAT':           {'metadata': {'name': 'Baseball Bat',           'Group': 'Melee'}},
    'WEAPON_GOLFCLUB':      {'metadata': {'name': 'Golf Club',              'Group': 'Melee'}},
    'WEAPON_CROWBAR':       {'metadata': {'name': 'Crowbar',                'Group': 'Melee'}},
    'WEAPON_HATCHET':       {'metadata': {'name': 'Hatchet',                'Group': 'Melee'}},
    'WEAPON_MACHETE':       {'metadata': {'name': 'Machete',                'Group': 'Melee'}},
    'WEAPON_FLASHLIGHT':    {'metadata': {'name': 'Flashlight',             'Group': 'Melee'}},
    'WEAPON_SWITCHBLADE':   {'metadata': {'name': 'Switchblade',            'Group': 'Melee'}},
    'WEAPON_STUNROD':       {'metadata': {'name': 'The Shocker',            'Group': 'Melee'}},
    'WEAPON_WRENCH':        {'metadata': {'name': 'Wrench',                 'Group': 'Melee'}},
    'WEAPON_POOLCUE':       {'metadata': {'name': 'Pool Cue',               'Group': 'Melee'}},
    'WEAPON_DAGGER':        {'metadata': {'name': 'Antique Cavalry Dagger', 'Group': 'Melee'}},
    'WEAPON_HANDCUFFS':     {'metadata': {'name': 'Handcuffs',              'Group': 'Melee'}},
    'WEAPON_GARBAGEBAG':    {'metadata': {'name': 'Garbage Bag',            'Group': 'Melee'}},
    'WEAPON_KNUCKLE':       {'metadata': {'name': 'Knuckle Dusters',        'Group': 'Melee'}},
    'WEAPON_BATTLEAXE':     {'metadata': {'name': 'Battle Axe',             'Group': 'Melee'}},
    'WEAPON_STONE_HATCHET': {'metadata': {'name': 'Stone Hatchet',          'Group': 'Melee'}},
    'WEAPON_CANDYCANE':     {'metadata': {'name': 'Candy Cane',             'Group': 'Melee'}},
    'WEAPON_BOTTLE':        {'metadata': {'name': 'Bottle',                 'Group': 'Melee'}},
    
    # Handgun
    'WEAPON_PISTOL': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_9MM', 'Speed': 390},
        'metadata': {'name': 'Pistol', 'Group': 'Handgun', 'counterpart': 'Taurus PT92AF'},
    },
    'WEAPON_COMBATPISTOL': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_9MM', 'Speed': 355},
        'metadata': {'name': 'Combat Pistol', 'Group': 'Handgun', 'counterpart': 'H&K P2000'},
    },
    'WEAPON_APPISTOL': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 640},
        'metadata': {'name': 'AP Pistol', 'Group': 'Handgun', 'counterpart': 'Colt SCAMP'},
    },
    'WEAPON_PISTOL50': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_50C', 'Speed': 470},
        'metadata': {'name': 'Pistol .50', 'Group': 'Handgun', 'counterpart': 'Desert Eagle'},
    },
    'WEAPON_STUNGUN': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_STUNGUN', 'Speed': 70},
        'metadata': {'name': 'Stun Gun', 'Group': 'Handgun', 'counterpart': 'TASER 7 (+ M26 Taser)'},
    },
    'WEAPON_SNSPISTOL': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_40C', 'Speed': 300},
        'metadata': {'name': 'SNS Pistol', 'Group': 'Handgun', 'counterpart': 'H&K P7M10'},
    },
    'WEAPON_HEAVYPISTOL': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_45C', 'Speed': 253},
        'metadata': {'name': 'Heavy Pistol', 'Group': 'Handgun', 'counterpart': 'Enterprise Widebody 1911'},
    },
    'WEAPON_VINTAGEPISTOL': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_9MM', 'Speed': 320},
        'metadata': {'name': 'Vintage Pistol', 'Group': 'Handgun', 'counterpart': 'FN Model 1922'},
    },
    'WEAPON_FLAREGUN': {
        'update': {'AmmoInfo': 'AMMO_FLAREGUN', 'Speed': 88},
        'metadata': {'name': 'Flare Gun', 'Group': 'Handgun', 'counterpart': 'Orion Brand Flare Gun'},
    },
    'WEAPON_MARKSMANPISTOL': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_38S', 'Speed': 250},
        'metadata': {'name': 'Marksman Pistol', 'Group': 'Handgun', 'counterpart': 'Thompson/Center Contender G2'},
    },
    'WEAPON_REVOLVER': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_45C', 'Speed': 450},
        'metadata': {'name': 'Heavy Revolver', 'Group': 'Handgun', 'counterpart': 'Taurus Raging Bull'},
    },
    'WEAPON_PISTOL_MK2': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_9MM', 'Speed': 381},
        'metadata': {'name': 'Pistol Mk II', 'Group': 'Handgun', 'counterpart': 'Beretta 92'},
    },
    'WEAPON_DOUBLEACTION': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_38S', 'Speed': 230},
        'metadata': {'name': 'Double Action Revolver', 'Group': 'Handgun', 'counterpart': 'Colt M1892'},
    },
    'WEAPON_REVOLVER_MK2': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_38S', 'Speed': 300},
        'metadata': {'name': 'Heavy Revolver Mk II', 'Group': 'Handgun', 'counterpart': 'Chiappa Rhino'},
    },
    'WEAPON_SNSPISTOL_MK2': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_38S', 'Speed': 230},
        'metadata': {'name': 'SNS Pistol Mk II', 'Group': 'Handgun', 'counterpart': 'AMT Backup'},
    },
    'WEAPON_CERAMICPISTOL': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_9MM', 'Speed': 351},
        'metadata': {'name': 'Ceramic Pistol', 'Group': 'Handgun', 'counterpart': 'H&K PSP'},
    },
    'WEAPON_NAVYREVOLVER': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_45C', 'Speed': 450},
        'metadata': {'name': 'Navy Revolver', 'Group': 'Handgun', 'counterpart': 'Taurus Raging Bull'},
    },
    'WEAPON_GADGETPISTOL': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_9MM', 'Speed': 375},
        'metadata': {'name': 'Perico Pistol', 'Group': 'Handgun', 'counterpart': 'P08 Luger'},
    },
    'WEAPON_PISTOLXM3': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_9MM', 'Speed': 351},
        'metadata': {'name': 'WM 29 Pistol', 'Group': 'Handgun', 'counterpart': 'H&K P7M13'},
    },
    'WEAPON_RAYPISTOL': {
        'update': {'AmmoInfo': 'AMMO_RAYPISTOL'},
        'metadata': {'name': 'Up-n-Atomizer', 'Group': 'Handgun', 'counterpart': 'H&K P7M13'},
    },
    'WEAPON_TRANQUILIZER': {
        'update': {'FireType': 'DELAYED_HIT', 'Speed': 60},
        'metadata': {'name': 'Tranquilizer', 'Group': 'Handgun'},
    },
    'WEAPON_STUNGUN_MP': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_STUNGUN', 'Speed': 70},
        'metadata': {'name': 'Stun Gun MP', 'Group': 'Handgun', 'counterpart': 'TASER 7 (+ M26 Taser)'},
    },
    'WEAPON_HACKINGDEVICE': {
        'update': {},
        'metadata': {'name': 'Hacking Device', 'Group': 'Handgun', 'counterpart': 'TASER 7 (+ M26 Taser)'},
    },

    # Submachine
    'WEAPON_MICROSMG': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_9MM', 'Speed': 350},
        'metadata': {'name': 'Micro SMG', 'Group': 'Submachine', 'counterpart': 'Mini Uzi'},
    },
    'WEAPON_SMG': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_9MM', 'Speed': 400},
        'metadata': {'name': 'SMG', 'Group': 'Submachine', 'counterpart': 'MP5A3'},
    },
    'WEAPON_ASSAULTSMG': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 900},
        'metadata': {'name': 'Assault SMG', 'Group': 'Submachine', 'counterpart': 'Magpul PDR'},
    },
    'WEAPON_COMBATPDW': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_9MM', 'Speed': 390},
        'metadata': {'name': 'Combat PDW', 'Group': 'Submachine', 'counterpart': 'SIG Sauer MPX'},
    },
    'WEAPON_MACHINEPISTOL': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_9MM', 'Speed': 360},
        'metadata': {'name': 'Machine Pistol', 'Group': 'Submachine', 'counterpart': 'TEC-9'},
    },
    'WEAPON_MINISMG': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_9MM', 'Speed': 320},
        'metadata': {'name': 'Mini SMG', 'Group': 'Submachine', 'counterpart': 'Škorpion Vz. 82'},
    },
    'WEAPON_SMG_MK2': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_9MM', 'Speed': 390},
        'metadata': {'name': 'SMG Mk II', 'Group': 'Submachine', 'counterpart': 'SIG Sauer MPX'},
    },
    'WEAPON_TECPISTOL': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_9MM', 'Speed': 400},
        'metadata': {'name': 'Tactical SMG', 'Group': 'Submachine', 'counterpart': 'Steyr TMP'},
    },

    # Assault Rifle
    'WEAPON_ASSAULTRIFLE': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_762', 'Speed': 735},
        'metadata': {'name': 'Assault Rifle', 'Group': 'Rifle', 'counterpart': 'Norinco Type 56-2'},
    },
    'WEAPON_CARBINERIFLE': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 1006},
        'metadata': {'name': 'Carbine Rifle', 'Group': 'Rifle', 'counterpart': 'AR-15'},
    },
    'WEAPON_ADVANCEDRIFLE': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 890},
        'metadata': {'name': 'Advanced Rifle', 'Group': 'Rifle', 'counterpart': 'CTAR-21'},
    },
    
    'WEAPON_SPECIALCARBINE': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 722},
        'metadata': {'name': 'Special Carbine', 'Group': 'Rifle', 'counterpart': 'H&K G36C'},
    },
    'WEAPON_BULLPUPRIFLE': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 930},
        'metadata': {'name': 'Bullpup Rifle', 'Group': 'Rifle', 'counterpart': 'QBZ-95-1'},
    },
    'WEAPON_COMPACTRIFLE': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_762', 'Speed': 735},
        'metadata': {'name': 'Compact Rifle', 'Group': 'Rifle', 'counterpart': 'Norinco Type 56'},
    },
    'WEAPON_ASSAULTRIFLE_MK2': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_762', 'Speed': 715},
        'metadata': {'name': 'Assault Rifle Mk II', 'Group': 'Rifle', 'counterpart': 'AK-15'},
    },
    'WEAPON_CARBINERIFLE_MK2': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 1006},
        'metadata': {'name': 'Carbine Rifle Mk II', 'Group': 'Rifle', 'counterpart': 'AR-15'},
    },
    'WEAPON_BULLPUPRIFLE_MK2': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 925},
        'metadata': {'name': 'Bullpup Rifle Mk II', 'Group': 'Rifle', 'counterpart': 'FAMAS G2 (+ Kel-Tec RFB)'},
    },
    'WEAPON_SPECIALCARBINE_MK2': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 850},
        'metadata': {'name': 'Special Carbine Mk II', 'Group': 'Rifle', 'counterpart': 'H&K G36K'},
    },
    'WEAPON_MILITARYRIFLE': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 970},
        'metadata': {'name': 'Military Rifle', 'Group': 'Rifle', 'counterpart': 'Steyr AUG A3'},
    },
    'WEAPON_HEAVYRIFLE': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 870},
        'metadata': {'name': 'Heavy Rifle', 'Group': 'Rifle', 'counterpart': 'FN SCAR-L'},
    },
    'WEAPON_TACTICALRIFLE': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 960},
        'metadata': {'name': 'Service Carbine', 'Group': 'Rifle', 'counterpart': 'M16A4'},
    },
    'WEAPON_BATTLERIFLE': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_762', 'Speed': 840},
        'metadata': {'name': 'Battle Rifle', 'Group': 'Rifle', 'counterpart': 'FN FAL'},
    },
    'WEAPON_STRICKLER': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 970},
        'metadata': {'name': 'El Strickler', 'Group': 'Rifle', 'counterpart': 'Steyr AUG A3'},
    },

    # Machine Gun
    'WEAPON_MG': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_762', 'Speed': 825},
        'metadata': {'name': 'MG', 'Group': 'Machine Gun', 'counterpart': 'PKM'},
    },
    'WEAPON_COMBATMG': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_762', 'Speed': 900},
        'metadata': {'name': 'Combat MG', 'Group': 'Machine Gun', 'counterpart': 'Mk 48'},
    },
    
    'WEAPON_GUSENBERG': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_45C', 'Speed': 285},
        'metadata': {'name': 'Gusenberg Sweeper', 'Group': 'Machine Gun', 'counterpart': 'M1928A1 Thompson'},
    },
    'WEAPON_COMBATMG_MK2': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_762', 'Speed': 875},
        'metadata': {'name': 'Combat MG Mk II', 'Group': 'Machine Gun', 'counterpart': 'Mark 48/M60E4'},
    },
    'WEAPON_RAYCARBINE': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_762'},
        'metadata': {'name': 'Unholy Hellbringer', 'Group': 'Machine Gun'},
    },

    # Shotgun
    'WEAPON_PUMPSHOTGUN': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_12G', 'Speed': 378},
        'metadata': {'name': 'Pump Shotgun', 'Group': 'Shotgun', 'counterpart': 'Mossberg 590'},
    },
    'WEAPON_SAWNOFFSHOTGUN': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_12G', 'Speed': 403},
        'metadata': {'name': 'Sawed-Off Shotgun', 'Group': 'Shotgun', 'counterpart': 'Mossberg 500'},
    },
    'WEAPON_ASSAULTSHOTGUN': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_12G', 'Speed': 388},
        'metadata': {'name': 'Assault Shotgun', 'Group': 'Shotgun', 'counterpart': 'UTAS UTS-15', },
    },
    'WEAPON_BULLPUPSHOTGUN': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_12G', 'Speed': 404},
        'metadata': {'name': 'Bullpup Shotgun', 'Group': 'Shotgun', 'counterpart': 'Kel-Tec KSG'},
    },
    'WEAPON_MUSKET': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_18MM', 'Speed': 475},
        'metadata': {'name': 'Musket', 'Group': 'Shotgun', 'counterpart': 'Brown Bess'},
    },
    'WEAPON_HEAVYSHOTGUN': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_20G', 'Speed': 366},
        'metadata': {'name': 'Heavy Shotgun', 'Group': 'Shotgun', 'counterpart': 'Saiga 12K'},
    },
    'WEAPON_DBSHOTGUN': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_12G', 'Speed': 475},
        'metadata': {'name': 'Double Barrel Shotgun', 'Group': 'Shotgun', 'counterpart': 'Zabala Double Barrel Shotgun'},
    },
    'WEAPON_AUTOSHOTGUN': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_12G', 'Speed': 475},
        'metadata': {'name': 'Sweeper Shotgun', 'Group': 'Shotgun', 'counterpart': 'Armsel Striker'},
    },
    'WEAPON_PUMPSHOTGUN_MK2': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_12G', 'Speed': 337},
        'metadata': {'name': 'Pump Shotgun Mk II', 'Group': 'Shotgun', 'counterpart': 'Remington Model 870'},
    },
    'WEAPON_COMBATSHOTGUN': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_12G', 'Speed': 475},
        'metadata': {'name': 'Combat Shotgun', 'Group': 'Shotgun', 'counterpart': 'Franchi SPAS-12'},
    },

    # Sniper Rifle
    'WEAPON_SNIPERRIFLE': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_762', 'Speed': 850},
        'metadata': {'name': 'Sniper Rifle', 'Group': 'Sniper Rifle', 'counterpart': 'AW-F'},
    },
    'WEAPON_HEAVYSNIPER': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_50BMG', 'Speed': 853},
        'metadata': {'name': 'Heavy Sniper', 'Group': 'Sniper Rifle', 'counterpart': 'Barrett M107'},
    },
    'WEAPON_REMOTESNIPER': {},

    'WEAPON_MARKSMANRIFLE': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 990},
        'metadata': {'name': 'Marksman Rifle', 'Group': 'Sniper Rifle', 'counterpart': 'Ruger Mini-14'},
    },
    'WEAPON_HEAVYSNIPER_MK2': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_50BMG', 'Speed': 879},
        'metadata': {'name': 'Heavy Sniper Mk II', 'Group': 'Sniper Rifle', 'counterpart': 'Serbu BFG-50A'},
    },
    'WEAPON_MARKSMANRIFLE_MK2': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_762', 'Speed': 762},
        'metadata': {'name': 'Marksman Rifle Mk II', 'Group': 'Sniper Rifle', 'counterpart': 'Springfield M1A Loaded'},
    },
    'WEAPON_PRECISIONRIFLE': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_556', 'Speed': 792},
        'metadata': {'name': 'Precision Rifle', 'Group': 'Sniper Rifle', 'counterpart': 'Remington 700 PCR Enhanced'},
    },

    # Heavy Weapon
    'WEAPON_GRENADELAUNCHER': {
        'update': {'Speed': 75},
        'metadata': {'name': 'Grenade Launcher', 'Group': 'Heavy Weapon', 'counterpart': 'Milkor MGL'},
    },
    'WEAPON_GRENADELAUNCHER_SMOKE': {},
    'WEAPON_RPG': {
        'update': {'Speed': 300},
        'metadata': {'name': 'RPG', 'Group': 'Heavy Weapon', 'counterpart': 'RPG-7'},
    },
    'WEAPON_PASSENGER_ROCKET': {},
    'WEAPON_AIRSTRIKE_ROCKET': {},
    'WEAPON_STINGER': {},
    'WEAPON_MINIGUN': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_762MNG', 'Speed': 850},
        'metadata': {'name': 'Minigun', 'Group': 'Heavy Weapon', 'counterpart': 'M134'},
    },    
    'WEAPON_FIREWORK': {
        'update': {'Speed': 110},
        'metadata': {'name': 'Firework Launcher', 'Group': 'Heavy Weapon', 'counterpart': 'Panzerschreck'},
    },
    'WEAPON_RAILGUN': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_RAILGUN', 'Speed': 2500},
        'metadata': {'name': 'Railgun', 'Group': 'Heavy Weapon'},
    },
    'WEAPON_HOMINGLAUNCHER': {
        'update': {'AmmoInfo': 'AMMO_HOMINGLAUNCHER', 'Speed': 430},
        'metadata': {'name': 'Homing Launcher', 'Group': 'Heavy Weapon', 'counterpart': 'SA-7 Grail'},
    },
    'WEAPON_RAYMINIGUN': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_762MNG', 'Speed': 850},
        'metadata': {'name': 'Widowmaker', 'Group': 'Heavy Weapon'},
    },
    'WEAPON_EMPLAUNCHER': {
        'update': {'AmmoInfo': 'AMMO_EMPLAUNCHER', 'Speed': 76},
        'metadata': {'name': 'Compact EMP Launcher', 'Group': 'Heavy Weapon', 'counterpart': 'M320'},
    },
    'WEAPON_RAILGUNXM3': {
        'update': {'FireType': 'DELAYED_HIT', 'AmmoInfo': 'AMMO_RAILGUNXM3', 'Speed': 2500},
        'metadata': {'name': 'Coil Railgun', 'Group': 'Heavy Weapon'},
    },
    'WEAPON_SNOWLAUNCHER': {
        'update': {'AmmoInfo': 'AMMO_SNOWLAUNCHER', 'Speed': 76},
        'metadata': {'name': 'Snowball Launcher', 'Group': 'Heavy Weapon', 'counterpart': 'M79 Grenade launcher'},
    },
    'WEAPON_COMPACTLAUNCHER': {
        'update': {'Speed': 76},
        'metadata': {'name': 'Compact Grenade Launcher', 'Group': 'Heavy Weapon', 'counterpart': 'M79 Grenade launcher'},
    },
    
    # Throwable
    'WEAPON_GRENADE':      {'metadata': {'name': 'Grenade',          'Group': 'Throwable'}},
    'WEAPON_STICKYBOMB':   {'metadata': {'name': 'Sticky Bomb',      'Group': 'Throwable'}},
    'WEAPON_SMOKEGRENADE': {'metadata': {'name': 'Tear Gas',         'Group': 'Throwable'}},
    'WEAPON_BZGAS':        {'metadata': {'name': 'BZ Gas',           'Group': 'Throwable'}},
    'WEAPON_MOLOTOV':      {'metadata': {'name': 'Molotov Cocktail', 'Group': 'Throwable'}},
    'WEAPON_BALL':         {'metadata': {'name': 'Baseball',         'Group': 'Throwable'}},
    'WEAPON_FLARE':        {'metadata': {'name': 'Flare',            'Group': 'Throwable'}},
    'WEAPON_BALL':         {'metadata': {'name': 'Flare',            'Group': 'Throwable'}},
    'WEAPON_FLARE':        {'metadata': {'name': 'Flare',            'Group': 'Throwable'}},
    'WEAPON_PROXMINE':     {'metadata': {'name': 'Flare',            'Group': 'Throwable'}},
    'WEAPON_SNOWBALL':     {'metadata': {'name': 'Flare',            'Group': 'Throwable'}},
    'WEAPON_PIPEBOMB':     {'metadata': {'name': 'Flare',            'Group': 'Throwable'}},
    'WEAPON_ACIDPACKAGE':  {'metadata': {'name': 'Flare',            'Group': 'Throwable'}},

    # Miscellaneous
    'WEAPON_FIREEXTINGUISHER': {'metadata': {'name': 'Fire Extinguisher', 'Group': 'Miscellaneous'}},
    'WEAPON_PETROLCAN':        {'metadata': {'name': 'Jerry Can',         'Group': 'Miscellaneous'}},
    'WEAPON_DIGISCANNER':      {'metadata': {'name': 'Digiscanner',       'Group': 'Miscellaneous'}},
    'GADGET_NIGHTVISION':      {'metadata': {'name': 'Nightvision',       'Group': 'Miscellaneous'}},
    'GADGET_PARACHUTE':        {'metadata': {'name': 'Parachute',         'Group': 'Miscellaneous'}},
    'OBJECT':                  {'metadata': {'name': 'Object',            'Group': 'Miscellaneous'}},
    'WEAPON_BRIEFCASE':        {'metadata': {'name': 'Briefcase',         'Group': 'Miscellaneous'}},
    'WEAPON_BRIEFCASE_02':     {'metadata': {'name': 'Briefcase',         'Group': 'Miscellaneous'}},
    'WEAPON_HAZARDCAN':        {'metadata': {'name': 'Jerry Can',         'Group': 'Miscellaneous'}},
    'WEAPON_FERTILIZERCAN':    {'metadata': {'name': 'Fertilizer Can',    'Group': 'Miscellaneous'}},
    'WEAPON_METALDETECTOR':    {'metadata': {'name': 'Metal Detector',    'Group': 'Miscellaneous'}},
}
