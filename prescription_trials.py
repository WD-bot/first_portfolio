from prescription_data import *

trial_patients = ["Denis", "Edward", "Hugo", "Georg", "Kenn"] #someone whos is not getting warfarin
#trial_patients = ["Denis", "Edward", "Hugo", "Georg]

def switch_warfarin_to_edoxaban(trial_patients, patients):
    """
    Replaces Warfarin with Edoxaban in the prescriptions of trial patients.

    param:
    patients (dict): Dictionary of patients and their prescriptions.

    return:
    None (modifies the patients dictionary in-place)
    """
    for patient in patients:
        if patient in patients:  # Check if patient exists in dictionary
            prescription = patients[patient]
            if warfarin in prescription:
                prescription.remove(warfarin)
                prescription.add(edoxaban)
                print(f"{patient} switched from Warfarin to Edoxaban.")
            # else:
            #     print(f"⚠️ {patient} is not prescribed Warfarin. Removing from trial.") #if it was a trial
        else:
            print(f"❌ {patient} not found in patient list.")

# Example usage:
trial_patients = ["Denis", "Edward", "Lars", "Georg", "Isabella"]
switch_warfarin_to_edoxaban(trial_patients, patients)



# Interactions should also give a Warning
# Function to check patients' prescriptions
def check_medication(patients, adverse_interactions, anticoagulants):
    """
    Checks for adverse interactions and gives OBS for anticoagulants

    :param patients:
    patients (dict): Dictionary of patients and their prescriptions.
    :param adverse_interactions: list of some adverse interactions
    :param anticoagulants: list of the used anticoagulants
    :return: None
    """
    for patient, prescriptions in patients.items():
        # Check for contraindikations/adverse interactions
        for interaction in adverse_interactions:
            if interaction.issubset(prescriptions):  # If patient has the full interaction set
                print(f"⚠️WARNING: {patient} has a contraindication: {', '.join([drug[0] for drug in interaction])}")

        # Check for anticoagulating medication for possible double medication errors
        if any(med in prescriptions for med in anticoagulants):
            print(f"BE AWARE: {patient} is taking anticoagulant medication!")

# Run function
check_medication(patients, adverse_interactions, anticoagulants)
