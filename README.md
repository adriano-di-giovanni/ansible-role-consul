# Ansible Role: Consul

[![Build Status](https://travis-ci.org/adriano-di-giovanni/ansible-role-consul.svg?branch=master)](https://travis-ci.org/adriano-di-giovanni/ansible-role-consul)

Ansible role for [Consul](https://www.consul.io/):

* basic, opinionated install
* optional [RPC encryption with TLS](https://www.consul.io/docs/agent/encryption.html)
* optional [Web UI](https://www.consul.io/intro/getting-started/ui.html) install

## Requirements

None.

## Role Variables

The following variables apply to all nodes in a Consul cluster.

<table>
  <thead>
    <tr>
      <th>variable</th>
      <th>required</th>
      <th>default</th>
      <th>choices</th>
      <th>comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>consul_datacenter</td>
      <td>yes</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>
        <p>The datacenter in which the agent is running.</p>
        <p>See <a href="https://www.consul.io/docs/agent/options.html#datacenter">documentation</a> for more details.</p>
      </td>
    </tr>
    <tr>
      <td>consul_start_join</td>
      <td>yes</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>
        <p>An array of strings specifying addresses of nodes to join upon startup.</p>
        <p>See <a href="https://www.consul.io/docs/agent/options.html#start_join">documentation</a> for more details.</p>
      </td>
    </tr>
    <tr>
      <td>consul_tls</td>
      <td>no</td>
      <td>no</td>
      <td>
        <ul>
          <li>yes</li>
          <li>no</li>
        </ul>
      </td>
      <td>
        <p>This flag indicates if RPC encryption with TLS should enabled.</p>
        <p>See <a href="https://www.consul.io/docs/agent/encryption.html">documentation</a> for more details.</p>
        <p>When <code>consul_tls: yes</code>, the variables <code>consul_tls_ca_file_content</code>, <code>consul_tls_cert_file_content</code> and <code>consul_tls_key_file_content</code> should also be set.</p>
      </td>
    </tr>
    <tr>
      <td>consul_tls_ca_file_content</td>
      <td>no</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>If <code>consul_tls: yes</code>, this variable should contain the CA certificate file contents. You can use <a href="https://galaxy.ansible.com/adriano-di-giovanni/consul-tls/">adriano-di-giovanni.consul-tls</a> role to generate all the certificates.</td>
    </tr>
    <tr>
      <td>consul_tls_cert_file_content</td>
      <td>no</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>If <code>consul_tls: yes</code>, this variable should contain the server certificate file contents. You can use <a href="https://galaxy.ansible.com/adriano-di-giovanni/consul-tls/">adriano-di-giovanni.consul-tls</a> role to generate all the certificates.</td>
    </tr>
    <tr>
      <td>consul_tls_key_file_content</td>
      <td>no</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>If <code>consul_tls: yes</code>, this variable should contain the server key file contents. You can use <a href="https://galaxy.ansible.com/adriano-di-giovanni/consul-tls/">adriano-di-giovanni.consul-tls</a> role to generate all the certificates.</td>
    </tr>
    <tr>
      <td>consul_version</td>
      <td>no</td>
      <td>0.7.0</td>
      <td>&nbsp;</td>
      <td>Version of Consul to install</td>
    </tr>
  </tbody>
</table>

The following variables apply to certain nodes of a Consul cluster:

<table>
  <thead>
    <tr>
      <th>variable</th>
      <th>required</th>
      <th>default</th>
      <th>choices</th>
      <th>comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>consul_bootstrap</td>
      <td>no</td>
      <td>no</td>
      <td>
        <ul>
          <li>yes</li>
          <li>no</li>
        </ul>
      </td>
      <td>
        <p>This flag is used to control if a server is in bootstrap mode. It is important that no more than one server per datacenter be running in this mode.</p>
        <p>See <a href="https://www.consul.io/docs/agent/options.html#bootstrap">documentation</a> for more details.</p>
      </td>
    </tr>
    <tr>
      <td>consul_server</td>
      <td>no</td>
      <td>no</td>
      <td>
        <ul>
          <li>yes</li>
          <li>no</li>
        </ul>
      </td>
      <td>
        <p>This flag is used to control if an agent is in server or client mode.</p>
        <p>See <a href="https://www.consul.io/docs/agent/options.html#server">documentation</a> for more details.</p>
      </td>
    </tr>
    <tr>
      <td>consul_ui</td>
      <td>no</td>
      <td>no</td>
      <td>
        <ul>
          <li>yes</li>
          <li>no</li>
        </ul>
      </td>
      <td>
        <p>This flag indicates if built-in Web UI should be enabled.</p>
        <p>See <a href="https://www.consul.io/docs/agent/options.html#ui">documentation</a> for more details.</p>
      </td>
    </tr>
  </tbody>
</table>

## Dependencies

None

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - role: adriano-di-giovanni.consul
      consul_datacenter: dc2
      consul_start_join:
        - 192.168.0.2
        - 192.168.0.3
        - 192.168.0.4
      consul_tls: true
      consul_tls_ca_file_content: |
        -----BEGIN CERTIFICATE-----
        MIIEETCCAvmgAwIBAgIJAKg3dFuagpONMA0GCSqGSIb3DQEBCwUAMGIxCzAJBgNV
        BAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRYwFAYDVQQHEw1TYW4gRnJhbmNp
        c2NvMRIwEAYDVQQKEwlIYXNoaUNvcnAxEjAQBgNVBAMTCUhhc2hpQ29ycDAgFw0x
        NjEwMjAxNjMzMzZaGA8yMTE1MDkyNzE2MzMzNlowYjELMAkGA1UEBhMCVVMxEzAR
        BgNVBAgTCkNhbGlmb3JuaWExFjAUBgNVBAcTDVNhbiBGcmFuY2lzY28xEjAQBgNV
        BAoTCUhhc2hpQ29ycDESMBAGA1UEAxMJSGFzaGlDb3JwMIIBIjANBgkqhkiG9w0B
        AQEFAAOCAQ8AMIIBCgKCAQEAzRjPWtIk1THi7Qa57xcCVYc0QM0I9ihG3Zsk994D
        vaaFya6wYqUHsx2QkzlqAz6iVIGShRKqoav2YdMMCqKTtQ1zVLYJRDFSJZPce8I2
        ZmkpjnWydnlEgWhZBOkYqxR3HP5ILt0zhhl6FFsLtSI+x6plt+y6OGEFPmC9aGAz
        a5pDZoZUuzQK8dPML2CvQITRVKisltSA+0F4TWPA12poOmkqmfWqri2D6xQcoqPf
        xOPb/IWy+alzColU9yKCnIskp3Ll9sBh1jE9fXel2VW/46DWtgG05wAjwv/u1D/D
        ata6zxOhKgQtfloha4CWYzSUAGty7j7u5b8ZAzNU30WtCwIDAQABo4HHMIHEMB0G
        A1UdDgQWBBTm2zqJWizfofkkCgIbz8P49cu1mjCBlAYDVR0jBIGMMIGJgBTm2zqJ
        WizfofkkCgIbz8P49cu1mqFmpGQwYjELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNh
        bGlmb3JuaWExFjAUBgNVBAcTDVNhbiBGcmFuY2lzY28xEjAQBgNVBAoTCUhhc2hp
        Q29ycDESMBAGA1UEAxMJSGFzaGlDb3JwggkAqDd0W5qCk40wDAYDVR0TBAUwAwEB
        /zANBgkqhkiG9w0BAQsFAAOCAQEAbxjyu6RFS0KcpMmOOJj615EbV8DsgPhFmKin
        gmq4fDPwVaFs0P1n4VFpujNdCm1LhbAKy2+K6z9oGNwG576l0do7ZaUwdEL7a9Ll
        97CR9MrElxW2C3gI/b6jAJp94zrawh0yZx5zjIWi/IE3rEc66pM87Hk3SrMR4vx0
        LcyHihZyGmsGUgOsqqmztCvw3nlrVOj8SHs9N437ZgfxsoWGsiiURDLobciDOkMn
        JiCHmmmWgrArJKa+3B6Dnv2a0zMEH4IKxgbg3zrjyHMjBNCcnxiO8ionr36HVitv
        CWWkh5FHA3nmsGn3lTnHMngv1tXqHg3hXx1O3H5IWAiZU6zWww==
        -----END CERTIFICATE-----

      consul_tls_cert_file_content: |
        -----BEGIN CERTIFICATE-----
        MIIDbjCCAlagAwIBAgICEAAwDQYJKoZIhvcNAQELBQAwYjELMAkGA1UEBhMCVVMx
        EzARBgNVBAgTCkNhbGlmb3JuaWExFjAUBgNVBAcTDVNhbiBGcmFuY2lzY28xEjAQ
        BgNVBAoTCUhhc2hpQ29ycDESMBAGA1UEAxMJSGFzaGlDb3JwMB4XDTE2MTAyMDE2
        MzMzN1oXDTI2MTAxODE2MzMzN1owFzEVMBMGA1UEAxQMKi5kYzIuY29uc3VsMIIB
        IjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzTTpzdxJ2dGAnv1L1hxyGybD
        Wx5d06ExYldDjkP0QhkJoenseef59rRKwpa4R9igHOit596NTmsdzHDBe62p5Hiv
        Z4c2KjUgV///yI/RkRx///hqyK1OkoXtQClr/TqLkVNyDy+nB6l8TNpQgtzKom9o
        jkBPxZJhTiEFtOR1jNrghoF6JpIiLml/eXrJaL6LNicdBRuQEAyHbpwi5UFlDthR
        HOo2ipZSrSFGXY5Xs3w9vuxLbE+rRPxPrYrnNfQDNjOgNGh1Qj4A8SFyWBWJGYLl
        bFriJ299+x9OQOLUSlLY7JsIrOvcN42/EnsOXC91gYedQUrFzM9JnNM4c8uP0wID
        AQABo3kwdzAJBgNVHRMEAjAAMB0GA1UdDgQWBBSpdBZ8IHd/9zK4ib10URJAIk/c
        szAfBgNVHSMEGDAWgBTm2zqJWizfofkkCgIbz8P49cu1mjALBgNVHQ8EBAMCBaAw
        HQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMA0GCSqGSIb3DQEBCwUAA4IB
        AQBHApfRJI6FmYiBKRer2E2bruULXcy5hvT4s5B4Yk8GVfrSbtdiKq0QKNHAz3jZ
        Vy2sZWwxk6o6+LF7f1HEzwdwZWGIzliiCnyQj0PQQl+Aqo4ElAVactO6IzMGqhXP
        Gx9fihmD+kYEA3rqtc4JixeNJvQPgGPDtiH8z9R1POAbgHjuNfo31ZvQaYfHHodT
        +ovurep+UyD2+xsqNGSX59yq8DccIZLN6cWS95f/kkCPcUpdjCuY06kRapp4Auw9
        +S4QnW3hTMm8ia4vqgQgmU1UiwpT25sQcW4dHN4U7LK0ZW7sgqWtqMN9fJIzzYx1
        B53IRQ0AvWfJSgUMiaIUWGIc
        -----END CERTIFICATE-----

      consul_tls_key_file_content: |
        -----BEGIN RSA PRIVATE KEY-----
        MIIEpAIBAAKCAQEAzTTpzdxJ2dGAnv1L1hxyGybDWx5d06ExYldDjkP0QhkJoens
        eef59rRKwpa4R9igHOit596NTmsdzHDBe62p5HivZ4c2KjUgV///yI/RkRx///hq
        yK1OkoXtQClr/TqLkVNyDy+nB6l8TNpQgtzKom9ojkBPxZJhTiEFtOR1jNrghoF6
        JpIiLml/eXrJaL6LNicdBRuQEAyHbpwi5UFlDthRHOo2ipZSrSFGXY5Xs3w9vuxL
        bE+rRPxPrYrnNfQDNjOgNGh1Qj4A8SFyWBWJGYLlbFriJ299+x9OQOLUSlLY7JsI
        rOvcN42/EnsOXC91gYedQUrFzM9JnNM4c8uP0wIDAQABAoIBAEV9YqNssrGJSYYN
        fo3eCiH5qXQEv383+dI0fNMDXga4FdP3tDXAAZyyhxKIGZVy3R2NCb8YVT+19FxT
        3qF0OLD+0V88oXH/lZlXPpX7Zds/DHVw+TBFx/LEWYg9vqz9E2A+IsTTvTtSAJ7B
        2zvFavVAxuZNDvZ30G21rwoHx2rP482YYDG2vRTUD1hbbc65QUIJLWLS8cuUsMtm
        INzJ394jep642iKYBheByw2R5BBmnOgdBTss/4Mh6J3BWlxxl5Qg42wpRSGzgP6F
        JV2Jlb895RsIh4uHiNq304dGiDSLJb9RmWmzHLGFiQB7EPdwdCCsMvTgdC7no/md
        Uq7hbAECgYEA/24MXxg71cNZZuM/cOwDlmXNOHFMiedF/URsm09ANqNZRfaiCn0J
        2v3B6AQIyynHLwSVSQ4+mP9VlscvdTYp6pa2A1+K0b8DSFxbDquTw2ad6KwVvsi5
        nneLo+Q+RLZ6ldJYxYTf6exKaS7MtvjpOU8ax2GAj0Zg34EY0yKzvdMCgYEAzaoq
        6fYXSMQ9WLS+tM0qEDHsD8nBPnHhPUI/uNSe3Akb2vzmWwHoawB0Xh1jtYHpx/9V
        IvasoHEHuXIkB22X3y5cIZbVS6BiCVDGBYQTpImFnz9wH4FHyd7/KKu6LBX4DLhs
        0ZPk+eNrucK8XOs5Fw1hxwoA/ij/m+oK7k5bpgECgYBx2YBEJo4M8nx3wpR1ZY0X
        zRpSrRVbZi0o/QWXmBRcBiT1bT++gwsQhAiYvKuaum1ghJ9xp5q5IR3qDbAWg2Td
        ff10tXIvmP8Ckr+3YzyCXMvHeGRc3CT3//rKuyISCG/NNauBpn8TSdHE3io65+k0
        NREPi2L8+XaWSHljKlWJJwKBgQC3MhIBz2SUO8FNZ8rL8Ei8nkthEN0ii3wP/hgW
        wsYyx6ZZXZavkDaAQapmPxWXE36z2Lv0ZfgE/kncJVD0kOmMMpZ8kQez0swg8iNB
        vJFmqd0tqettFNJmfk2Y48b1CCio5AqCcJOxB6Polw8EUb7Lyu7CxiV2P/zX3BUa
        iw/WAQKBgQD29pZNjSOFGW7A8dKH2Yya/VkxeAmn4/1TP/LvTwu/syYr0sZxLftK
        dbqjV/4kdybK2yc2QssONKuPttjV+YSJaSZvjgKfhhqD81weuZT3SdRqwgYBnzeZ
        3iTxsZB1N64pbX8b9b2xu1emLqI3rSLMATMPoUptHoB9hNGkBFSY+w==
        -----END RSA PRIVATE KEY-----
```

The `example/` folder contains project files to provision a local development Consul cluster using Vagrant and VirtualBox.

## License

MIT

## Author Information

Adriano Di Giovanni
