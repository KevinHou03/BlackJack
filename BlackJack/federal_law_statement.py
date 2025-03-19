import sys
import time
import pyfiglet

def verification():
    print("\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b*********** FBI Warning ***********\n")
    print(
        "Federal law provides severe civil and criminal penalties for the unauthorized participation or engagement in any form of gambling by any individual under the age of 21.\n")
    print(
        "A valid government-issued photo ID (e.g., passport, driver’s license, or state-issued identification card) is not only encouraged but MANDATORY to verify the participant's age and identity before engaging in any gambling activities.\n")
    print(
        "Failure to provide a valid form of identification or providing falsified documentation will result in immediate disqualification from participation, potential forfeiture of winnings, and may lead to legal prosecution under applicable federal and state laws.\n")
    print(
        "By proceeding, you affirm that you are of legal age to participate in gambling activities and that you fully understand and accept the risks and responsibilities involved.\n")
    print(
        "All activities are monitored and recorded for security and compliance purposes. Unauthorized access or fraudulent behavior will be reported to the appropriate authorities, including the Federal Bureau of Investigation (FBI) and other relevant law enforcement agencies.\n")
    print(
        "Proceed with caution. Violations of these terms may result in permanent suspension and legal consequences.\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b*************************************\n")

    id = input("Please enter your government-issued ID number for verification:\n")
    sys.stdout.write('\nID Authentication In Progress')
    sys.stdout.flush()
    for _ in range(10):
        time.sleep(0.3)
        print('.', end='')
    sys.stdout.write('\nID Verification In Progress')
    sys.stdout.flush()
    for _ in range(12):
        time.sleep(0.3)
        print('.', end='')
    time.sleep(1)
    print("\n\nIdentity verification completed successfully. You may now proceed to the game.\n\n")


