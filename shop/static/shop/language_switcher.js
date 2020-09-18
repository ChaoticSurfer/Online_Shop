// $(document).ready(function () {
//     // Initialization
//     $.sls.init({
//         defaultLang: "geo",
//         path: "shop/static/shop/languages/",
//         persistent: true,
//         clean: true,
//         attributes: ["title", "data-my-custom-attribute"],
//         observe: document
//     });
//
//     // Event hook example
//     $(document).on("jquery-sls-language-switched", function(event){
//         // Make select element reflect current language if language loaded from persistence
//         if ( $('#lang-switcher').val != $.sls.getLang() ) {
//             $('#lang-switcher').val($.sls.getLang());
//         }
//         console.log( "Language switched: " + event.message );
//     });
//
// });
//
// function selectLanguage(select) {
//     $.sls.setLang(select.value);
// }