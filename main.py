from flask import Flask, render_template, request
from dotenv import load_dotenv
import meraki

load_dotenv()

app = Flask(__name__)

dashboard = meraki.DashboardAPI()


@app.route("/")
def orgs():
    orgs = dashboard.organizations.getOrganizations()
    return render_template("index.html", orgs=orgs)


@app.route("/networks", methods=["POST"])
def networks():
    org_id = request.form["org_id"]
    networks = dashboard.organizations.getOrganizationNetworks(org_id)
    return render_template("networks.html", networks=networks)


@app.route("/devices", methods=["POST"])
def devices():
    network_id = request.form["network_id"]
    devices = dashboard.networks.getNetworkDevices(network_id)
    return render_template("devices.html", devices=devices)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
