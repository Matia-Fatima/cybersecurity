import pywifi
from pywifi import const
import time

def get_wifi_interface():
    wifi = pywifi.PyWiFi()
    interfaces = wifi.interfaces()

    if len(interfaces) == 0:
        print(" No Wi-Fi adapter found!")
        return None

    print("\nAvailable Interfaces:")
    for idx, iface in enumerate(interfaces):
        print(f"{idx} → {iface.name()}")

    # Use first interface automatically
    iface = interfaces[0]
    print(f"\nUsing interface: {iface.name()}\n")
    return iface

def scan_wifi():
    iface = get_wifi_interface()
    if iface is None:
        return

    print(" Scanning Wi-Fi networks... Please wait 5 seconds.\n")
    iface.scan()
    time.sleep(5)   # increased scan time

    networks = iface.scan_results()

    if len(networks) == 0:
        print("No Wi-Fi networks found! Make sure Wi-Fi is ON.")
        return

    print(f"{'SSID':30} {'Signal':10} {'Security'}")
    print("-" * 60)

    for net in networks:
        ssid = net.ssid if net.ssid else "Hidden Network"
        signal = net.signal

        # Detect security type
        if net.akm:
            if const.AKM_TYPE_WPA2 in net.akm:
                security = "WPA2"
            elif const.AKM_TYPE_WPA in net.akm:
                security = "WPA"
            else:
                security = str(net.akm[0])
        else:
            security = "Open"

        print(f"{ssid:30} {signal:<10} {security}")

if __name__ == "__main__":
    scan_wifi()
