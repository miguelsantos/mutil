import sys

from plumbum import cli, local

from plumbum.cmd import networksetup

class Wlanadm(cli.Application):
    """Wi-Fi configuration manager"""
    PROGNAME = "wlanadm"
    VERSION = "0.0.1"
    verbosity = cli.Flag(["v", "verbose"], help = "Verbosity level",)

    def main(self, *args):
        if args:
            print("Unknown command %r" % (args[0]))
            return 1
        if not self.nested_command:
            print("No command given")
            return 1


@Wlanadm.subcommand("list")
class WlanadmList(cli.Application):
    """Lists all network interfaces"""

    wifi_only = cli.Flag("w", help = "Listis only Wi-Fi interfaces")
    net_only = cli.Flag("n", help = "Lists networks instead of interfaces (only available Wi-Fi networks)")

    def main(self):
        print(networksetup["-listallhardwareports"]())

@Wlanadm.subcommand("on")
class WlanadmOn(cli.Application):
    """Starts the selected network interface"""

    def main(self, ifname):
        pass

@Wlanadm.subcommand("off")
class WlanadmOff(cli.Application):
    """Stops the selected network interface"""

    def main(self, ifname):
        pass

@Wlanadm.subcommand("join")
class WlanadmJoin(cli.Application):
    """Joins the selected wifi network"""

    def main(self, netname):
        pass

if __name__=="__main__":
    Wlanadm.run()
