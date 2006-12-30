<?php
/**
 * hebrew language file
 *
 * @license    GPL 2 (http://www.gnu.org/licenses/gpl.html)
 * @author     DoK <kamberd@yahoo.com>
 */

// for admin plugins, the menu prompt to be displayed in the admin menu
// if set here, the plugin doesn't need to override the getMenuText() method
$lang['menu']       = 'הגדרות תצורה';

$lang['error']      = 'ההגדרות לא עודכנו בגלל ערך לא תקף, נא לעיין בשינויים ולשלוח שנית.
                       <br />הערכים שאינם נכונים יסומנו בגבול אדום.';
$lang['updated']    = 'ההגדרות עודכנו בהצלחה.';
$lang['nochoice']   = '(אין אפשרויות זמינות נוספות)';
$lang['locked']     = 'קובץ ההגדרות אינו בר עידכון, אם הדבר אינו מכוון, <br />
                       יש לודא כי קובץ ההגדרות המקומי וההרשאות נכונים.';

/* --- Config Setting Headers --- */
$lang['_configuration_manager'] = 'מנהל תצורה'; //same as heading in intro.txt
$lang['_header_dokuwiki'] = 'הגדרות DokuWiki';
$lang['_header_plugin'] = 'הגדרות תוסף';
$lang['_header_template'] = 'הגדרות תבנית';
$lang['_header_undefined'] = 'הגדרות שונות';

/* --- Config Setting Groups --- */
$lang['_basic'] = 'הגדרות בסיסיות';
$lang['_display'] = 'הגדרות תצוגה';
$lang['_authentication'] = 'הגדרות הזדהות';
$lang['_anti_spam'] = 'הגדרות נגד דואר זבל';
$lang['_editing'] = 'הגדרות עריכה';
$lang['_links'] = 'הגדרות קישורים';
$lang['_media'] = 'הגדרות מדיה';
$lang['_advanced'] = 'הגדרות מתקדמות';
$lang['_network'] = 'הגדרות רשת';
// The settings group name for plugins and templates can be set with
// plugin_settings_name and template_settings_name respectively. If one
// of these lang properties is not set, the group name will be generated
// from the plugin or template name and the localized suffix.
$lang['_plugin_sufix'] = 'הגדרות תוסף';
$lang['_template_sufix'] = 'הגדרות תבנית';

/* --- Undefined Setting Messages --- */
$lang['_msg_setting_undefined'] = 'אין מידע-על להגדרה.';
$lang['_msg_setting_no_class'] = 'אין קבוצה להגדרה.';
$lang['_msg_setting_no_default'] = 'אין ערך ברירת מחדל.';

/* -------------------- Config Options --------------------------- */

$lang['fmode']       = 'מצב יצירת קובץ';
$lang['dmode']       = 'מצב יצירת ספריה';
$lang['lang']        = 'שפה';
$lang['basedir']     = 'ספרית בסיס';
$lang['baseurl']     = 'כתובת URL בסיסית';
$lang['savedir']     = 'ספריה לשמירת מידע';
$lang['start']       = 'שם דף הפתיחה';
$lang['title']       = 'כותרת הויקי';
$lang['template']    = 'תבנית';
$lang['fullpath']    = 'הצגת נתיב מלא לדפים בתחתית';
$lang['recent']      = 'שינויים אחרונים';
$lang['breadcrumbs'] = 'מספר עקבות להיסטוריה';
$lang['youarehere']  = 'עקבות היררכיות להיסטוריה';
$lang['typography']  = 'שימוש בחלופות טיפוגרפיות';
$lang['htmlok']      = 'אישור שיבוץ HTML';
$lang['phpok']       = 'אישור שיבוץ PHP';
$lang['dformat']     = 'תסדיר תאריך (נא לפנות לפונקציה <a href="http://www.php.net/date">date</a> של PHP)';
$lang['signature']   = 'חתימה';
$lang['toptoclevel'] = 'רמה עליונה בתוכן הענינים';
$lang['maxtoclevel'] = 'רמה מירבית בתוכן הענינים';
$lang['maxseclevel'] = 'רמה מירבית בעריכת קטעים';
$lang['camelcase']   = 'השתמש בראשיות גדולות לקישורים';
$lang['deaccent']    = 'נקה שמות דפים';
$lang['useheading']  = 'השתמש בכותרת הראשונה לשם הדף';
$lang['refcheck']    = 'בדוק שיוך מדיה';
$lang['refshow']     = 'מספר שיוכי המדיה שיוצגו';
$lang['allowdebug']  = 'אפשר דיבוג <b>יש לבטל אם אין צורך!</b>';

$lang['usewordblock']= 'חסימת דואר זבל לפי רשימת מילים';
$lang['indexdelay']  = 'השהיה בטרם הכנסה לאינדקס (שניות)';
$lang['relnofollow'] = 'השתמש ב- rel="nofollow" לקישורים חיצוניים';
$lang['mailguard']   = 'הגן על כתובות דוא"ל';

/* Authentication Options */
$lang['useacl']      = 'השתמש ברשימות בקרת גישה';
$lang['autopasswd']  = 'צור סיסמאות באופן אוטומטי';
$lang['authtype']    = 'מנוע הזדהות';
$lang['passcrypt']   = 'שיטת הצפנת סיסמאות';
$lang['defaultgroup']= 'קבוצת ברירת המחדל';
$lang['superuser']   = 'משתמש-על';
$lang['profileconfirm'] = 'אשר שינוי פרופילים עם סיסמה';
$lang['disableactions'] = 'בטל פעולות DokuWiki';
$lang['disableactions_check'] = 'בדיקה';
$lang['disableactions_subscription'] = 'הרשמה/הסרה מרשימה';
$lang['disableactions_wikicode'] = 'הצגת המקור/יצוא גולמי';
$lang['disableactions_other'] = 'פעולות אחרות (מופרדות בפסיק)';

/* Advanced Options */
$lang['updatecheck'] = 'בדיקת עידכוני אבטחה והתראות? על DokuWiki להתקשר אל splitbrain.org לצורך כך.';
$lang['userewrite']  = 'השתמש בכתובות URL יפות';
$lang['useslash']    = 'השתמש בלוכסן להרדת מרחבי שמות בכתובות';
$lang['usedraft']    = 'שמור טיוטות באופן אוטומטי בעת עריכה';
$lang['sepchar']     = 'מפריד בין מילות שם-דף';
$lang['canonical']   = 'השתמש בכתובות URL מלאות';
$lang['autoplural']  = 'בדוק לצורת רבים בקישורים';
$lang['compression'] = 'אופן דחיסת קבצים ב-attic';
$lang['cachetime']   = 'גיל מירבי לזכרון מטמון (שניות)';
$lang['locktime']    = 'גיל מירבי לקבצי נעילה (שניות)';
$lang['fetchsize']   = 'גודל הקובץ המירבי (bytes) ש-fetch.php יכול להוריד מבחוץ';
$lang['notify']      = 'שלח התראות על שינויים לכתובת דוא"ל זו';
$lang['registernotify'] = 'שלח מידע על משתמשים רשומים חדשים לכתובת דוא"ל זו';
$lang['mailfrom']    = 'כתובת הדוא"ל לשימוש בדברי דוא"ל אוטומטיים';
$lang['gzip_output'] = 'השתמש בקידוד תוכן של gzip עבור xhtml';
$lang['gdlib']       = 'גרסת ספרית ה-GD';
$lang['im_convert']  = 'נתיב לכלי ה-convert של ImageMagick';
$lang['jpg_quality'] = 'איכות הדחיסה של JPG (0-100)';
$lang['spellchecker']= 'השתמש בבודק איות';
$lang['subscribers'] = 'התר תמיכה ברישום לדפים';
$lang['compress']    = 'פלט קומפקטי של CSS ו-javascript';
$lang['hidepages']   = 'הסתר דפים תואמים (ביטויים רגולריים)';
$lang['send404']     = 'שלח "HTTP 404/Page Not Found" עבור דפים שאינם קיימים';
$lang['sitemap']     = 'צור מפת אתר של Google (ימים)';

$lang['rss_type']    = 'סוג פלט XML';
$lang['rss_linkto']  = 'פלט ה-XML מקשר אל';
$lang['rss_update']  = 'פלט ה-XML מתעדכן כל (שניות)';
$lang['recent_days'] = 'כמה שינויים אחרונים לשמור (ימים)';

/* Target options */
$lang['target____wiki']      = 'חלון יעד לקישורים פנימיים';
$lang['target____interwiki'] = 'חלון יעד לקישורים בין מערכות ויקי';
$lang['target____extern']    = 'חלון יעד לקישורים חיצוניים';
$lang['target____media']     = 'חלון יעד לקישור למדיה';
$lang['target____windows']   = 'חלון יעד לתיקיות משותפות';

/* Proxy Options */
$lang['proxy____host'] = 'שם השרת המתווך';
$lang['proxy____port'] = 'שער השרת המתווך';
$lang['proxy____user'] = 'שם המשתמש בשרת המתווך';
$lang['proxy____pass'] = 'סיסמת ההשרת המתווך';
$lang['proxy____ssl']  = 'השתמש ב-ssl כדי להתחבר לשרת המתווך';

/* Safemode Hack */
$lang['safemodehack'] = 'אפשר שימוש בפתרון ל-safemode';
$lang['ftp____host'] = 'שרת FTP עבור פתרון ה-safemode';
$lang['ftp____port'] = 'שער ה-FTP עבור פתרון ה-safemode';
$lang['ftp____user'] = 'שם המשתמש ב-FTPעבור פתרון ה-safemode';
$lang['ftp____pass'] = 'סיסמת ה-FTP לפתרון ה-safemode';
$lang['ftp____root'] = 'ספרית השורש ב-FTP עבור פתרון ה-safemode';

/* userewrite options */
$lang['userewrite_o_0'] = 'ללא';
$lang['userewrite_o_1'] = '.htaccess';
$lang['userewrite_o_2'] = 'פנימי של DokuWiki';

/* deaccent options */
$lang['deaccent_o_0'] = 'כבוי';
$lang['deaccent_o_1'] = 'הסר ניבים';
$lang['deaccent_o_2'] = 'הסב ללטינית';

/* gdlib options */
$lang['gdlib_o_0'] = 'ספרית ה-GD אינה זמינה';
$lang['gdlib_o_1'] = 'גרסה 1.x';
$lang['gdlib_o_2'] = 'זיהוי אוטומטי';

/* rss_type options */
$lang['rss_type_o_rss']  = 'RSS 0.91';
$lang['rss_type_o_rss1'] = 'RSS 1.0';
$lang['rss_type_o_rss2'] = 'RSS 2.0';
$lang['rss_type_o_atom'] = 'Atom 0.3';

/* rss_linkto options */
$lang['rss_linkto_o_diff']    = 'תצוגת הבדלים';
$lang['rss_linkto_o_page']    = 'הדף שהשתנה';
$lang['rss_linkto_o_rev']     = 'גרסאות קודמות';
$lang['rss_linkto_o_current'] = 'הדף הנוכחי';

/* compression options */
$lang['compression_o_0']   = 'ללא';
$lang['compression_o_gz']  = 'gzip';
$lang['compression_o_bz2'] = 'bz2';

