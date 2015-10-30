import sys

from plumbum import cli, local

from plumbum.cmd import networksetup

class Wlanadm(cli.Application):
    """
    Wi-Fi configuration manager
    """
    PROGNAME = "wlanadm"
    VERSION = "0.0.1"

    verbosity = cli.Flag(["v", "verbose"], help = "Verbosity level")

    #Listing group
    #lists_group = "Listing switches"

    @cli.switch("l")
    def list(self):
        """
        Lists all network interfaces
        """

        print(networksetup("-listallhardwareports"))

    def _format_wifi_only(self, hpl, idx):
        #return ("%s\n%s\n%s\n" % hpl[idx], hpl[idx+1], hpl[idx+2])
        return "{0}\n{1}\n{2}\n".format(hpl[idx], hpl[idx+1], hpl[idx+2])

    @cli.switch("w", excludes = ["n"])
    def wifi_only(self):
        """
        Lists only WiFi interfaces
        """

        hardports = networksetup("-listallhardwareports").splitlines()
        for index, line in enumerate(hardports):
            for j in line.split():
                if "Wi-Fi" in j:
                    print(self._format_wifi_only(hardports, index))
        # @NOTE: This **needs** to be beautified

    @cli.switch("n", requires = ["l"], excludes = ["w"])
    def netw_only(self):
        """
        Lists networks instead of interfaces (only Wi-Fi networks)
        """

        print("netw")
        # @TODO: Implement the actual function, based on airport utility

    def main(self, *args):
        if args:
            print("Unknown command %r" % (args[0]))
            return 1
        if not self.nested_command:
            print("\nHARDWARE Interfaces\n===================")
            self.list()


@Wlanadm.subcommand("on")
class WlanadmOn(cli.Application):
    """
    Starts the selected network interface
    """

    def main(self, ifname):
        pass

@Wlanadm.subcommand("off")
class WlanadmOff(cli.Application):
    """
    Stops the selected network interface
    """

    def main(self, ifname):
        pass

@Wlanadm.subcommand("join")
class WlanadmJoin(cli.Application):
    """
    Joins the selected wifi network
    """

    def main(self, netname):
        pass

if __name__=="__main__":
    Wlanadm.run()
