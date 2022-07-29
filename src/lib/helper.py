def get_operation_state_message(CS):
    '''
    Converts 'CS' (operation state) to more readable 'operation_state_message'

    args:
        CS: Operation state from the VE.Direct protocol
    returns:
        operation_state_message: Human friendly operation state message
    '''

    codes = {
        '0': 'Off',
        '1': 'Low power',
        '2': 'Fault',
        '3': 'Bulk',
        '4': 'Absorbtion',
        '5': 'Float',
        '6': 'Storage',
        '7': 'Equalize',
        '9': 'Inverting',
        '11': 'Power supply',
        '245': 'Starting up',
        '246': 'Repeated absorbtion',
        '247': 'Auto equalize / Recondition',
        '248': 'BatterySafe',
        '252': 'External Control'
    }
    if CS in codes:
        result = codes[CS]
    else:
        result = f"Unrecognized 'CS' value: {CS}"
    return result

def get_product_name(PID):
    '''
    Converts 'PID' (Product ID) to more readable 'product_name'

    args:
        PID: Product ID from the VE.Direct protocol
    returns:
        product_name: Human friendly product name
    '''

    codes = {
        '0xA054': 'SmartSolar MPPT 75|10',
        '0xA055': 'SmartSolar MPPT 100|15',
        '0xA056': 'SmartSolar MPPT 150|20',
        '0xA057': 'SmartSolar MPPT 200|25',
        '0xA058': 'SmartSolar MPPT 250|30',
        '0xA059': 'SmartSolar MPPT 300|35'
        # TODO Add correct/all smartsolar product names
    }
    if PID in codes:
        result = codes[PID]
    else:
        result = f"Unrecognized 'PID' value: {PID}"
    return result

def get_error_message(ERR):
    '''
    Converts 'ERR' (Error code) to more readable 'error_message'

    args:
        ERR: Error code as returned by the VE.Direct protocol
    returns:  
        error_message: Human readable error message
    '''

    codes = {
        '0': 'No error',
        '2': 'Battery voltage too high',
        '17': 'Charger temperature too high',
        '18': 'Charger over current',
        '19': 'Charger current reversed',
        '20': 'Bulk time limit exceeded',
        '21': 'Current sensor issue. Sensor bias/sensor broken.'
    }

    if ERR in codes:
        result = codes[ERR]
    else:
        result = f"Unrecognized 'ERR' value: {ERR}"
    return result

def get_mppt_mode_message(MPPT):
    '''
    Converts 'MPPT' (MPPT mode) to more readable 'mppt_mode_message'

    args:
        MPPT: MPPT Mode ID as returned by the VE.Direct protocol
    returns:    
        mppt_mode_message: Human readable description
    '''

    codes = {
        '0': 'Off',
        '1': 'Voltage or current limited',
        '2': 'MPP Tracker active',
    }
    if MPPT in codes:
        result = codes[MPPT]
    else:
        result = f"Unrecognized `MPPT` value: {MPPT}"        
    return result

def get_off_reason_message(OR):
    '''
    Converts 'OR' (Off reason) to more readable 'off_reason_message'

    args:
        OR: Off reason code as returned by the VE.Direct protocol
    returns:
        off_reason_message: Human readable off reason message
    '''
    # TODO Add more error codes
    codes = {
        '0x00000000': 'Not off',
        '0x00000001': 'No input power',
        '0x00000002': 'Switched off (power switch)',
        '0x00000004': 'Switched off (device mode register)',
        '0x00000008': 'Remote input',
        '0x00000010': 'Protection active',
        '0x00000020': 'Paygo',
        '0x00000040': 'BMS',
        '0x00000080': 'Engine shutdown detection',
        '0x00000100': 'Analysing input voltage'
    }
    if OR in codes:
        result = codes[OR]
    else:
        result = f"Unrecognized off reason: {OR}"
    return result
