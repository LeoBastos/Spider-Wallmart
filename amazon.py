import scrapy
import json


"""
Criar função para ver quantidades de itens retornados e qtd paginas (paginator)
para fazer o range
"""

class AmazonSpider(scrapy.Spider):
    name = 'Amazon'

    custom_settings = {
        'USER_AGENT': '',
        'ACCEPT_LANGUAGE': 'en-US, en;q=0.5',
        'AUTOTHROTTLE_ENABLED': True,
        'ROBOTSTXT_OBEY': False,
        'FEED_EXPORT_ENCODING': 'utf-8',
        #'AUTOTHROTTLE_START_DELAY': 10
    }

    def start_requests(self):
        for page in range(1, 22):
            yield scrapy.Request(f'https://www.amazon.com/-/pt/s?k=notebook+acer&page={page}&ref=sr_pg_{page}')

    def parse(self, response, **kwargs):

        for i in response.xpath('//div[@class="puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v3vtwxgppca0z12v18v51zrqona s-latency-cf-section s-card-border"]'):
            title = i.xpath('.//span[@class="a-size-medium a-color-base a-text-normal"]//text()').get()
            rating = i.xpath('.//span[@class="a-icon-alt"]//text()').get(),
            review = i.xpath('.//span[@class="a-size-base s-underline-text"]//text()').get(),
            price = i.xpath('.//span[@class="a-offscreen"]//text()').get(),
            url = i.xpath('.//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]').get()

            yield {
                'title': title,
                'rating': rating,
                'review': review,
                'price': price,
                'url': url
            }

        for item in response.css('html.a-ws.a-js.a-audio.a-video.a-canvas.a-svg.a-drag-drop.a-geolocation.a-history.a-webworker.a-autofocus.a-input-placeholder.a-textarea-placeholder.a-local-storage.a-gradients.a-transform3d.a-touch-scrolling.a-text-shadow.a-text-stroke.a-box-shadow.a-border-radius.a-border-image.a-opacity.a-transform.a-transition.a-ember body.a-m-us.a-aui_72554-c.a-aui_a11y_sr_678508-c.a-aui_accordion_a11y_role_354025-t1.a-aui_killswitch_csa_logger_372963-c.a-aui_pci_risk_banner_210084-c.a-aui_preload_261698-c.a-aui_rel_noreferrer_noopener_309527-c.a-aui_template_weblab_cache_333406-c.a-aui_tnr_v2_180836-c.a-meter-animate div#a-page div#search div.s-desktop-width-max.s-desktop-content.s-wide-grid-style-t1.s-opposite-dir.s-wide-grid-style.sg-row div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 div.sg-col-inner span.rush-component.s-latency-cf-section div.s-main-slot.s-result-list.s-search-results.sg-row div.sg-col-20-of-24.s-result-item.s-asin.sg-col-0-of-12.sg-col-16-of-20.AdHolder.sg-col.s-widget-spacing-small.sg-col-12-of-16 div.sg-col-inner div.s-widget-container.s-spacing-small.s-widget-container-height-small.celwidget.slot=MAIN.template=SEARCH_RESULTS.widgetId=search-results_1 div.rush-component div.rush-component.s-featured-result-item div.puis-card-container.s-card-container.s-overflow-hidden.aok-relative.puis-include-content-margin.puis.puis-v3vtwxgppca0z12v18v51zrqona.s-latency-cf-section.puis-card-border div.a-section div.puisg-row div.puisg-col.puisg-col-4-of-12.puisg-col-8-of-16.puisg-col-12-of-20.puisg-col-12-of-24.puis-list-col-right div.puisg-col-inner div.a-section.a-spacing-small.a-spacing-top-small div.a-section.a-spacing-none.puis-padding-right-small.s-title-instructions-style h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2 a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal'):
            print(item)
