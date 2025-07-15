// Fungsi untuk memuat file bahasa
function loadLanguageFile(language) {
	console.log(`Loading language file for ${language}`);
  return fetch(`/static/${language}.json`)
    .then(response => response.json())
    .then(data => data)
    .catch(error => console.error('Error loading language file:', error));
}

// Fungsi untuk mengganti bahasa
function changeLanguage(language) {
	console.log(`Changing language to ${language}`);
  loadLanguageFile(language)
    .then(data => {
      document.getElementById('introText').innerText = data.intro;
      document.getElementById('welcomeText').innerText = data.welcome;
      document.getElementById('aboutText').innerText = data.about;
      document.getElementById('serv_titleText').innerText = data.serv_title;
      document.getElementById('serv_sub_titleText').innerText = data.serv_sub_title;
      document.getElementById('serv_sub_title_descText').innerText = data.serv_sub_title_desc;
      document.getElementById('serv_title_dataText').innerText = data.serv_title_data;
      document.getElementById('serv_datast_descText').innerText = data.serv_datast_desc;
      document.getElementById('serv_datand_descText').innerText = data.serv_datand_desc;
      document.getElementById('serv_title_webText').innerText = data.serv_title_web;
      document.getElementById('serv_webst_descText').innerText = data.serv_webst_desc;
      document.getElementById('serv_webnd_descText').innerText = data.serv_webnd_desc;
      document.getElementById('serv_title_mobileText').innerText = data.serv_title_mobile;
      document.getElementById('serv_mobilest_descText').innerText = data.serv_mobilest_desc;
      document.getElementById('serv_mobilend_descText').innerText = data.serv_mobilend_desc;
      document.getElementById('serv_title_apiText').innerText = data.serv_title_api;
      document.getElementById('serv_apist_descText').innerText = data.serv_apist_desc;
      document.getElementById('serv_apind_descText').innerText = data.serv_apind_desc;
      document.getElementById('serv_title_erpText').innerText = data.serv_title_erp;
      document.getElementById('serv_erpst_descText').innerText = data.serv_erpst_desc;
      document.getElementById('serv_erpnd_descText').innerText = data.serv_erpnd_desc;
      document.getElementById('serv_title_crmText').innerText = data.serv_title_crm;
      document.getElementById('serv_crmst_descText').innerText = data.serv_crmst_desc;
      document.getElementById('serv_crmnd_descText').innerText = data.serv_crmnd_desc;
      document.getElementById('serv_title_acaText').innerText = data.serv_title_aca;
      document.getElementById('serv_acast_descText').innerText = data.serv_acast_desc;
      document.getElementById('serv_acand_descText').innerText = data.serv_acand_desc;
      document.getElementById('serv_title_mlText').innerText = data.serv_title_ml;
      document.getElementById('serv_mlst_descText').innerText = data.serv_mlst_desc;
      document.getElementById('serv_mlnd_descText').innerText = data.serv_mlnd_desc;
      document.getElementById('testimonial_titleText').innerText = data.testimonial_title;
      document.getElementById('testimonial_descText').innerText = data.testimonial_desc;
      document.getElementById('testimonial_stText').innerText = data.testimonial_st;
      document.getElementById('testimonial_ndText').innerText = data.testimonial_nd;
      document.getElementById('testimonial_rdText').innerText = data.testimonial_rd;
      document.getElementById('testimonial_thText').innerText = data.testimonial_th;
      document.getElementById('faq_descText').innerText = data.faq_desc;
      document.getElementById('q_1Text').innerText = data.q_1;
      document.getElementById('q_2Text').innerText = data.q_2;
      document.getElementById('q_3Text').innerText = data.q_3;
      document.getElementById('q_4Text').innerText = data.q_4;
      document.getElementById('q_5Text').innerText = data.q_5;
      document.getElementById('q_6Text').innerText = data.q_6;
      document.getElementById('q_7Text').innerText = data.q_7;
      document.getElementById('q_8Text').innerText = data.q_8;
      document.getElementById('q_9Text').innerText = data.q_9;
      document.getElementById('q_10Text').innerText = data.q_10;
      document.getElementById('q_11Text').innerText = data.q_11;
      document.getElementById('q_12Text').innerText = data.q_12;
      document.getElementById('q_13Text').innerText = data.q_13;
      document.getElementById('q_14Text').innerText = data.q_14;
      document.getElementById('q_15Text').innerText = data.q_15;
      document.getElementById('a_1Text').innerText = data.a_1;
      document.getElementById('a_2Text').innerText = data.a_2;
      document.getElementById('a_3Text').innerText = data.a_3;
      document.getElementById('a_4Text').innerText = data.a_4;
      document.getElementById('a_5Text').innerText = data.a_5;
      document.getElementById('a_6Text').innerText = data.a_6;
      document.getElementById('a_7Text').innerText = data.a_7;
      document.getElementById('a_8Text').innerText = data.a_8;
      document.getElementById('a_9Text').innerText = data.a_9;
      document.getElementById('a_10Text').innerText = data.a_10;
      document.getElementById('a_11Text').innerText = data.a_11;
      document.getElementById('a_12Text').innerText = data.a_12;
      document.getElementById('a_13_aText').innerText = data.a_13_a;
      document.getElementById('a_13_bText').innerText = data.a_13_b;
      document.getElementById('a_13_cText').innerText = data.a_13_c;
      document.getElementById('a_13_dText').innerText = data.a_13_d;
      document.getElementById('a_13_eText').innerText = data.a_13_e;
      document.getElementById('a_14Text').innerText = data.a_14;
      document.getElementById('a_15Text').innerText = data.a_15;
      document.getElementById('started_titleText').innerText = data.started_title;
      document.getElementById('started_descText').innerText = data.started_desc;
      document.getElementById('started_cta_titleText').innerText = data.started_cta_title;
      document.getElementById('started_cta_desc_stText').innerText = data.started_cta_desc_st;
      document.getElementById('started_cta_desc_ndText').innerText = data.started_cta_desc_nd;
      document.getElementById('started_cta_qText').innerText = data.started_cta_q;
      document.getElementById('started_list_stText').innerText = data.started_list_st;
      document.getElementById('started_list_ndText').innerText = data.started_list_nd;
      document.getElementById('started_list_rdText').innerText = data.started_list_rd;
      document.getElementById('mail_titleText').innerText = data.mail_title;
      document.getElementById('mail_submitText').innerText = data.mail_submit;
			document.getElementsByClassName('red_attentionText')[0].innerText = data.red_attention;
      document.getElementsByClassName('red_attentionAPIsText')[0].innerText = data.red_attention_APIs;

      var redAttentionElements = document.getElementsByClassName('red_attentionText');

			for (var i = 0; i < redAttentionElements.length; i++) {
			  redAttentionElements[i].innerText = data.red_attention;
			}

      var redAttentionAPIsElements = document.getElementsByClassName('red_attentionAPIsText');

			for (var i = 0; i < redAttentionAPIsElements.length; i++) {
			  redAttentionAPIsElements[i].innerText = data.red_attention_APIs;
			}
    });
}

document.getElementById('changeToEnglish').addEventListener('click', function() {
  changeLanguage('en');
});

document.getElementById('changeToBahasa').addEventListener('click', function() {
  changeLanguage('id');
});

document.addEventListener('DOMContentLoaded', function() {
  changeLanguage('en');
});