<!DOCTYPE html>
<html>
    <head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8">
    <meta http-equiv="Cache-control" content="no-cache">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CuiBapVH_cPanel_Install_Success</title>
    <style type="text/css">
        body {
            font-family: Arial, Helvetica, sans-serif;
            font-size: 14px;
            line-height: 1.428571429;
            background-color: #ffffff;
            color: #2F3230;
            padding: 0;
            margin: 0;
        }
        section, footer {
            display: block;
            padding: 0;
            margin: 0;
        }
        .container {
            margin-left: auto;
            margin-right: auto;
            padding: 0 10px;
        }
        .sorry-text {
            font-size: 500%;
            color: #CCCCCC;
        }

        .additional-info {
            background-repeat: no-repeat;
            background-color: #293A4A;
            color: #FFFFFF;
        }
        .additional-info a {
            color: #FFFFFF;
        }
        .additional-info-items {
            padding: 20px 0;
            min-height: 350px;
        }
        .contact-info {
            margin-bottom: 20px;
            font-size: 16px;
        }
        .contact-info a {
            text-decoration: underline;
            color: #428BCA;
        }
        .contact-info a:hover,
        .contact-info a:focus,
        .contact-info a:active {
            color: #2A6496;
        }
        .reason-text {
            margin: 20px 0;
            font-size: 16px;
        }
        ul {
            display: inline-block;
            list-style: none outside none;
            margin: 0;
            padding: 0;
        }
        ul li {
            float: left;
            text-align: center;
        }
        .additional-info-items ul li {
            width: 100%;
        }
        .heading-text {
            font-weight: bold;
            display: block;
            text-align: left;
        }
        .description {
            text-align: left;

        }
        .info-image {
            padding: 10px;
        }

        footer {
            text-align: center;
            margin: 60px 0;
        }

        footer a {
            text-decoration: none;
        }

        .copyright {
            font-size: 10px;
            color: #3F4143;
        }

        @media (min-width: 768px) {
            .additional-info {
                background-image: none;
            }
            .additional-info-items {
                padding: 20px;
            }
            .container {
                width: 90%;
            }
            .additional-info-items ul li {
                width: 25%;
                padding: 20px;
            }
            .reason-text {
                font-size: 18px;
            }
            .contact-info {
                font-size: 18px;
            }
        }
        @media (min-width: 992px) {
            .additional-info {
                background-image: url('/img-sys/error-bg-left.png');
            }
            .container {
                width: 70%;
            }
            .sorry-text {
                font-size: 900%;
            }
        }
    </style>
    </head>
    <body>
        <div class="container">
            <span class="sorry-text">Oh!</span>

            <section class="contact-info">
                cPanel(CuiBapVH_VN) đã được cài đặt thành công:
                <a href="mailto:cuibapvh@gmail.com" target="_blank" rel="noopener noreferrer" title="Click this link to contact the host" id="dynamicProviderLink">
                    cuibapvh@gmail.com
                </a>
            </section>

            <p class="reason-text">Lí do bạn nhìn thấy thông báo này: </p>
        </div>
        <section class="additional-info">
            <div class="container">
                <div class="additional-info-items">
                    <ul>
                        <li>
                            <div class="info-image">
                                <img src="/img-sys/IP_changed.png"/>
                            </div>
                            <span class="heading-text">
                                Địa chỉ IP đã thay đổi.
                            </span>
                            <div class="description">
                                Địa chỉ IP của tên miền gần đây đã được thay đổi. Hãy kiểm tra cài đặt DNS để xác nhận rằng tên miền được cài đặt chính xác. Nó sẽ mất 8-24 giờ để thay đổi DNS có hiệu lực.
                                Phục hồi quyền truy cập tới trang web bằng cách <a href="https://go.cpanel.net/cleardnscache">theo dõi nhưng hướng dẫn</a> để xoá DNS cache.
                            </div>
                        </li>
                        <li>
                            <div class="info-image">
                                <img src="/img-sys/server_misconfigured.png"/>
                            </div>
                            <span class="heading-text">
                                Server bị lỗi trong quá trình cài đặt.
                            </span>
                            <div class="description">
                                 Bạn phải chắc chắn rằng nhà cung cấp dịch vụ hosting cung cấp chính xác địa chỉ IP cho cài đặt Apache và bản ghi DNS. Hãy khởi động lại Apache để thiết lập mới có hiệu lực.
                            </div>
                        </li>
                        <li>
                            <div class="info-image">
                                <img src="/img-sys/server_moved.png"/>
                            </div>
                            <span class="heading-text">
                                Trang web đã được di chuyển tới máy chủ khác.
                            </span>
                            <div class="description">
                                Đường dẫn của tên miền có thể đã được thay đổi hoặc nhà cung cấp dịch vụ hosting đã di chuyển tài khoản tới một máy chủ khác.
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </section>
        <footer>
            <div class="container">
                <a href="http://cpanel.com/?utm_source=cpanelwhm&utm_medium=cplogo&utm_content=logolink&utm_campaign=cpanelwhmreferral" target="cpanel" title="cPanel, L.L.C.">
                    <img src="/img-sys/powered_by_cpanel.svg" height="20" alt="cPanel, L.L.C." />
                    <div class="copyright">Bản quyền © 2019 cPanel, L.L.C.</div>
                </a>
            </div>
        </footer>
    </body>
</html>
