import qrcode

features=qrcode.QRCode(version=1,box_size=40,border=3)

features.add_data("https://www.myntra.com/?utm_source=dms_google&utm_medium=searchbrand_cpc&utm_campaign=dms_google_searchbrand_cpc_Search_Brand_Myntra_Brand_India_BM_TROAS_SOK_New&gclid=CjwKCAjwjOunBhB4EiwA94JWsHqBSMPOJTlo9664G7Rpdtp05LxQv7PqmYJDIVUiTtpvUH3xy0aFbBoCaBUQAvD_BwE")

features.make(fit=True)
generate_image=features.make_image(fill_color="black",back_color="white")
generate_image.save('image.png')