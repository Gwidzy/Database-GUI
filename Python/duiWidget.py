import rumps
import subprocess
import os

class DUI(rumps.App):
    
    def __init__(self):
        super(DUI, self).__init__("DUI", icon="images/database-storage.png") # <a href="https://www.flaticon.com/free-icons/database" title="database icons">Database icons created by phatplus - Flaticon</a>

        # main menu items
        self.menu = [
            rumps.MenuItem("Create Queries"),
            rumps.MenuItem("Update Queries"),
            rumps.MenuItem("Select Queries"),
            rumps.MenuItem("Options")
        ]

        # add submenu items under "Run Scripts"
        self.menu["Create Queries"].add(rumps.MenuItem("Create Table", callback=self.run_crtTbl))
        self.menu["Create Queries"].add(rumps.MenuItem("Populate Table", callback=self.run_popTbl))
        self.menu["Update Queries"].add(rumps.MenuItem("Rename Table", callback=self.run_rnmTbl))
        self.menu["Update Queries"].add(rumps.MenuItem("Rename Column", callback=self.run_rnmCol))
        self.menu["Update Queries"].add(rumps.MenuItem("Add Column", callback=self.run_addCol))
        self.menu["Select Queries"].add(rumps.MenuItem("Get values", callback=self.run_slctSql))

        self.menu["Options"].add(rumps.MenuItem("About", callback=self.run_abt))

    def run_crtTbl(self, sender):
        self.run_tool_script("createTable.py")

    def run_popTbl(self, sender):
        self.run_tool_script("populateTable.py")
        
    def run_rnmTbl(self, sender):
        self.run_tool_script("renameTable.py")

    def run_rnmCol(self, sender):
        self.run_tool_script("renameColumn.py")

    def run_addCol(self, sender):
        self.run_tool_script("addColumn.py")

    def run_slctSql(self, sender):
        self.run_tool_script("selectSQL.py")

    def run_abt(self, sender):
        self.run_tool_script("about.py")

    def run_quit(self, sender):
        self.run_tool_script("quit.py")

    def run_tool_script(self, script_name):
        script_path = os.path.join(os.path.dirname(__file__), '', script_name)
        subprocess.Popen(["/usr/local/bin/python3.13", script_path])

if __name__ == "__main__":
    DUI().run()
