from slimmer import html_slimmer
import sys

base = open("bootstrap_form.html", "r")
html = base.read();
base.close()

uscf = open("email_templates/usc.html", "r")
usc = uscf.read();
uscf.close()


sivcf = open("email_templates/sivc.html", "r")
sivc = sivcf.read();
sivcf.close()


sivuf = open("email_templates/sivu.html", "r")
sivu = sivuf.read();
sivuf.close()


otherf = open("email_templates/other.html", "r")
other = otherf.read();
otherf.close()


html=html_slimmer( html.strip().replace('\n',' ').replace('\t',' ').replace('\r',' ')  )

html = html.replace("###USC-TEMPLATE###", usc);
html = html.replace("###SIVC-TEMPLATE###", sivc);
html = html.replace("###SIVU-TEMPLATE###", sivu);
html = html.replace("###OTHER-TEMPLATE###", other);
html = html.replace("###EMAIL###", "test@test.com");
html = html.replace("###EMAIL-SUBJECT###", "Afghanistan Email");

out = open("email.min.html","w")
out.write(html)
out.close()
