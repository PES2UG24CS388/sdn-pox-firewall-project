from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()
mac_to_port = {}

blocked_src = "00:00:00:00:00:01"
blocked_dst = "00:00:00:00:00:03"


def _handle_ConnectionUp(event):
    log.info("Switch connected")


def _handle_PacketIn(event):
    packet = event.parsed
    src = str(packet.src)
    dst = str(packet.dst)
    in_port = event.port

    mac_to_port[src] = in_port

    # 🚫 Block h1 -> h3
    if src == blocked_src and dst == blocked_dst:
        log.info("Blocked traffic from %s to %s", src, dst)
        return

    # If destination known, install flow rule
    if dst in mac_to_port:
        out_port = mac_to_port[dst]

        msg = of.ofp_flow_mod()
        msg.match.dl_dst = packet.dst
        msg.actions.append(of.ofp_action_output(port=out_port))
        event.connection.send(msg)

        log.info("Installed flow %s -> port %s", dst, out_port)

    else:
        # flood unknown
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)


def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
