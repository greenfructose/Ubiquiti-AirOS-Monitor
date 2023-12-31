from django.db import models


class Basetable(models.Model):
    basetable_id = models.AutoField(primary_key=True)
    portfw = models.BooleanField()


class Interfaces(models.Model):
    interfaces_id = models.AutoField(primary_key=True)
    hwaddr = models.CharField(max_length=100)
    ifname = models.CharField(max_length=100)
    enabled = models.BooleanField()
    mtu = models.IntegerField()
    basetable_id = models.ForeignKey(Basetable, on_delete=models.CASCADE)


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    cable_len = models.IntegerField()
    tx_packets = models.IntegerField()
    rx_dropped = models.CharField(max_length=100)
    duplex = models.BooleanField()
    speed = models.IntegerField()
    rx_errors = models.CharField(max_length=100)
    rx_packets = models.IntegerField()
    tx_errors = models.CharField(max_length=100)
    snr = models.CharField(max_length=100)
    tx_dropped = models.CharField(max_length=100)
    rx_bytes = models.CharField(max_length=100)
    ipaddr = models.CharField(max_length=100)
    plugged = models.BooleanField()
    tx_bytes = models.CharField(max_length=100)
    interfaces_id = models.OneToOneField(Interfaces, on_delete=models.CASCADE)


class Firewall(models.Model):
    firewall_id = models.AutoField(primary_key=True)
    iptables = models.BooleanField()
    ip6tables = models.BooleanField()
    ebtables = models.BooleanField()
    eb6tables = models.BooleanField()
    basetable_id = models.OneToOneField(Basetable, on_delete=models.CASCADE)


class Host(models.Model):
    host_id = models.AutoField(primary_key=True)
    fwversion = models.CharField(max_length=100)
    device_id = models.CharField(max_length=100)
    cpuload = models.CharField(max_length=100)
    netrole = models.CharField(max_length=100)
    totalram = models.IntegerField()
    devmodel = models.CharField(max_length=100)
    power_time = models.IntegerField()
    uptime = models.IntegerField()
    freeram = models.IntegerField()
    hostname = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    loadavg = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    timestamp = models.IntegerField()
    basetable_id = models.OneToOneField(Basetable, on_delete=models.CASCADE)


class Wireless(models.Model):
    wireless_id = models.AutoField(primary_key=True)
    antenna_gain = models.IntegerField()
    distance = models.IntegerField()
    rx_nss = models.CharField(max_length=100)
    apmac = models.CharField(max_length=100)
    aprepeater = models.BooleanField()
    noisef = models.IntegerField()
    frequency = models.IntegerField()
    nol_state = models.CharField(max_length=100)
    compat_11n = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)
    security = models.CharField(max_length=100)
    ieeemode = models.CharField(max_length=100)
    rx_idx = models.CharField(max_length=100)
    nol_timeout = models.CharField(max_length=100)
    band = models.CharField(max_length=100)
    cac_timeout = models.CharField(max_length=100)
    rx_chainmask = models.CharField(max_length=100)
    essid = models.CharField(max_length=100)
    count = models.CharField(max_length=100)
    tx_nss = models.CharField(max_length=100)
    cac_state = models.CharField(max_length=100)
    chanbw = models.IntegerField()
    dfs = models.CharField(max_length=100)
    rstatus = models.CharField(max_length=100)
    hide_essid = models.CharField(max_length=100)
    txpower = models.IntegerField()
    center1_freq = models.IntegerField()
    tx_idx = models.CharField(max_length=100)
    tx_chainmask = models.CharField(max_length=100)
    sta_disconnected = models.CharField(max_length=100)
    basetable_id = models.OneToOneField(Basetable, on_delete=models.CASCADE)


class Polling(models.Model):
    polling_id = models.AutoField(primary_key=True)
    gps_sync = models.BooleanField()
    cb_capacity = models.IntegerField()
    fixed_frame = models.BooleanField()
    flex_mode = models.CharField(max_length=100)
    tx_use = models.IntegerField()
    use = models.IntegerField()
    ul_capacity = models.IntegerField()
    atpc_status = models.CharField(max_length=100)
    dl_capacity = models.IntegerField()
    ff_cap_rep = models.BooleanField()
    rx_use = models.CharField(max_length=100)
    wireless_id = models.OneToOneField(Wireless, on_delete=models.CASCADE)


class Throughput(models.Model):
    throughput_id = models.AutoField(primary_key=True)
    tx = models.IntegerField()
    rx = models.IntegerField()
    wireless_id = models.OneToOneField(Wireless, on_delete=models.CASCADE)


class Sta(models.Model):
    sta_id = models.AutoField(primary_key=True)
    ul_capacity_expect = models.IntegerField()
    dl_linkscore = models.IntegerField()
    tx_ratedata = models.CharField(max_length=100)
    distance = models.IntegerField()
    rx_nss = models.CharField(max_length=100)
    chainrssi = models.CharField(max_length=100)
    mac = models.CharField(max_length=100)
    dl_rate_expect = models.CharField(max_length=100)
    dl_avg_linkscore = models.IntegerField()
    rx_idx = models.CharField(max_length=100)
    ul_avg_linkscore = models.IntegerField()
    tx_sretries = models.CharField(max_length=100)
    signal = models.IntegerField()
    ul_rate_expect = models.CharField(max_length=100)
    noisefloor = models.IntegerField()
    ul_linkscore = models.IntegerField()
    tx_lretries = models.CharField(max_length=100)
    dl_capacity_expect = models.IntegerField()
    tx_packets = models.CharField(max_length=100)
    rssi = models.IntegerField()
    lastip = models.CharField(max_length=100)
    last_disc = models.CharField(max_length=100)
    tx_latency = models.CharField(max_length=100)
    tx_nss = models.CharField(max_length=100)
    cb_capacity_expect = models.IntegerField()
    uptime = models.IntegerField()
    ul_signal_expect = models.IntegerField()
    dl_signal_expect = models.IntegerField()
    tx_idx = models.CharField(max_length=100)
    wireless_id = models.ForeignKey(Wireless, on_delete=models.CASCADE)


class Remote(models.Model):
    remote_id = models.AutoField(primary_key=True)
    antenna_gain = models.IntegerField()
    oob = models.BooleanField()
    tx_ratedata = models.CharField(max_length=100)
    distance = models.IntegerField()
    cpuload = models.CharField(max_length=100)
    chainrssi = models.CharField(max_length=100)
    airview = models.CharField(max_length=100)
    cable_loss = models.CharField(max_length=100)
    netrole = models.CharField(max_length=100)
    totalram = models.IntegerField()
    platform = models.CharField(max_length=100)
    power_time = models.IntegerField()
    compat_11n = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)
    sys_id = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100)
    temperature = models.IntegerField()
    rx_bytes = models.CharField(max_length=100)
    ipaddr = models.CharField(max_length=100)
    signal = models.IntegerField()
    noisefloor = models.IntegerField()
    tx_bytes = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    rx_chainmask = models.CharField(max_length=100)
    rssi = models.IntegerField()
    device_id = models.CharField(max_length=100)
    tx_power = models.IntegerField()
    rx_throughput = models.IntegerField()
    version = models.CharField(max_length=100)
    uptime = models.IntegerField()
    freeram = models.IntegerField()
    tx_throughput = models.IntegerField()
    time = models.CharField(max_length=100)
    sta_id = models.OneToOneField(Sta, on_delete=models.CASCADE)


class Unms(models.Model):
    unms_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100)
    basetable_id = models.OneToOneField(Basetable, on_delete=models.CASCADE)
    remote_id = models.OneToOneField(Remote, on_delete=models.CASCADE)


class Ethlist(models.Model):
    ethlist_id = models.AutoField(primary_key=True)
    cable_len = models.IntegerField()
    ifname = models.CharField(max_length=100)
    snr = models.CharField(max_length=100)
    duplex = models.BooleanField()
    enabled = models.BooleanField()
    plugged = models.BooleanField()
    speed = models.IntegerField()
    remote_id = models.ForeignKey(Remote, on_delete=models.CASCADE)


class Gps(models.Model):
    gps_id = models.AutoField(primary_key=True)
    dop = models.CharField(max_length=100)
    fix = models.CharField(max_length=100)
    alt = models.CharField(max_length=100)
    sats = models.IntegerField()
    time_synced = models.CharField(max_length=100)
    dim = models.CharField(max_length=100)
    lon = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    remote_id = models.OneToOneField(Remote, on_delete=models.CASCADE)


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    link = models.IntegerField()
    time = models.IntegerField()
    wireless_id = models.OneToOneField(Wireless, on_delete=models.CASCADE)
    remote_id = models.OneToOneField(Remote, on_delete=models.CASCADE)


class Stats(models.Model):
    stats_id = models.AutoField(primary_key=True)
    tx_packets = models.IntegerField()
    tx_pps = models.CharField(max_length=100)
    rx_bytes = models.CharField(max_length=100)
    rx_pps = models.IntegerField()
    tx_bytes = models.CharField(max_length=100)
    rx_packets = models.IntegerField()
    sta_id = models.OneToOneField(Sta, on_delete=models.CASCADE)


class Airmax(models.Model):
    airmax_id = models.AutoField(primary_key=True)
    beam = models.CharField(max_length=100)
    cb_capacity = models.IntegerField()
    desired_priority = models.CharField(max_length=100)
    ul_capacity = models.IntegerField()
    atpc_status = models.CharField(max_length=100)
    dl_capacity = models.IntegerField()
    actual_priority = models.CharField(max_length=100)
    sta_id = models.OneToOneField(Sta, on_delete=models.CASCADE)


class Tx(models.Model):
    tx_id = models.AutoField(primary_key=True)
    cinr = models.IntegerField()
    evm = models.CharField(max_length=100)
    usage = models.IntegerField()
    airmax_id = models.OneToOneField(Airmax, on_delete=models.CASCADE)


class Rx(models.Model):
    rx_id = models.AutoField(primary_key=True)
    cinr = models.IntegerField()
    evm = models.CharField(max_length=100)
    usage = models.CharField(max_length=100)
    airmax_id = models.OneToOneField(Airmax, on_delete=models.CASCADE)


class Services(models.Model):
    services_id = models.AutoField(primary_key=True)
    pppoe = models.BooleanField()
    airview = models.CharField(max_length=100)
    dhcpd = models.BooleanField()
    dhcpc = models.BooleanField()
    dhcp6d_stateful = models.BooleanField()
    basetable_id = models.OneToOneField(Basetable, on_delete=models.CASCADE)
