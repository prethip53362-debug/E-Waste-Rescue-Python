from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
from kivy.utils import get_color_from_hex
import re
import webbrowser

GREEN = "#188053"
DARK = "#133227"
PALE = "#EBF7EF"
BG = "#F7FAF7"
MUTED = "#67786D"
WHITE = "#FFFFFF"

KV = r"""
#:import dp kivy.metrics.dp

<PrimaryButton@Button>:
    size_hint_y: None
    height: dp(50)
    background_normal: ''
    background_down: ''
    background_color: (0.09, 0.50, 0.32, 1)
    color: 1, 1, 1, 1
    bold: True
    font_size: '15sp'

<InfoCard@BoxLayout>:
    orientation: 'vertical'
    size_hint_y: None
    height: self.minimum_height
    padding: dp(16)
    spacing: dp(7)
    canvas.before:
        Color:
            rgba: (0.92, 0.97, 0.94, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(16)]
    Label:
        text: root.title_text
        size_hint_y: None
        height: self.texture_size[1] + dp(4)
        text_size: self.width, None
        halign: 'left'
        valign: 'middle'
        color: (0.075, 0.196, 0.153, 1)
        bold: True
        font_size: '17sp'
    Label:
        text: root.body_text
        size_hint_y: None
        height: self.texture_size[1] + dp(4)
        text_size: self.width, None
        halign: 'left'
        valign: 'top'
        color: (0.40, 0.47, 0.43, 1)
        font_size: '14sp'

<HomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: (0.97, 0.98, 0.97, 1)
            Rectangle:
                pos: self.pos
                size: self.size
        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: dp(18), dp(18), dp(18), dp(28)
                spacing: dp(16)
                BoxLayout:
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(12)
                    Label:
                        text: '♻'
                        size_hint_x: None
                        width: dp(55)
                        font_size: '38sp'
                        color: (0.09, 0.50, 0.32, 1)
                    BoxLayout:
                        orientation: 'vertical'
                        Label:
                            text: 'E-WASTE'
                            bold: True
                            font_size: '22sp'
                            color: (0.075, 0.196, 0.153, 1)
                            halign: 'left'
                            valign: 'bottom'
                            text_size: self.size
                        Label:
                            text: 'RESCUE  •  SMART RECYCLING'
                            bold: True
                            font_size: '10sp'
                            color: (0.09, 0.50, 0.32, 1)
                            halign: 'left'
                            valign: 'top'
                            text_size: self.size
                    Label:
                        text: 'ECO\\nHERO'
                        size_hint_x: None
                        width: dp(62)
                        font_size: '11sp'
                        bold: True
                        color: (0.09, 0.50, 0.32, 1)
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)
                    spacing: dp(13)
                    canvas.before:
                        Color:
                            rgba: (0.03, 0.22, 0.16, 1)
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [dp(22)]
                    Label:
                        text: '🌿  MAKE EVERY DEVICE COUNT'
                        size_hint_y: None
                        height: dp(24)
                        font_size: '12sp'
                        bold: True
                        color: (0.65, 0.92, 0.75, 1)
                        halign: 'left'
                        text_size: self.size
                    Label:
                        text: 'Give old tech.\\nA new purpose.'
                        size_hint_y: None
                        height: dp(92)
                        font_size: '31sp'
                        bold: True
                        color: (1, 1, 1, 1)
                        halign: 'left'
                        text_size: self.width, None
                    Label:
                        text: 'Your unused electronics can have a second life. Choose smarter ways to repair, reuse and recycle responsibly.'
                        size_hint_y: None
                        height: dp(70)
                        font_size: '14sp'
                        color: (0.87, 0.94, 0.89, 1)
                        halign: 'left'
                        valign: 'top'
                        text_size: self.width, None
                    PrimaryButton:
                        text: 'Explore E-Waste  →'
                        on_release: app.go('categories')
                    Label:
                        text: 'REPAIR  •  REUSE  •  RECYCLE'
                        size_hint_y: None
                        height: dp(20)
                        font_size: '11sp'
                        bold: True
                        color: (0.72, 0.87, 0.76, 1)
                Label:
                    text: 'Your Eco Dashboard'
                    size_hint_y: None
                    height: dp(32)
                    font_size: '22sp'
                    bold: True
                    color: (0.075, 0.196, 0.153, 1)
                    halign: 'left'
                    text_size: self.size
                Label:
                    text: 'Small actions. Meaningful change.'
                    size_hint_y: None
                    height: dp(22)
                    font_size: '13sp'
                    color: (0.40, 0.47, 0.43, 1)
                    halign: 'left'
                    text_size: self.size
                GridLayout:
                    cols: 2
                    size_hint_y: None
                    height: dp(100)
                    spacing: dp(12)
                    InfoCard:
                        title_text: '♻  06'
                        body_text: 'Device categories'
                    InfoCard:
                        title_text: '🌍  01'
                        body_text: 'Planet to protect'
                Label:
                    text: 'What would you like to do?'
                    size_hint_y: None
                    height: dp(32)
                    font_size: '20sp'
                    bold: True
                    color: (0.075, 0.196, 0.153, 1)
                    halign: 'left'
                    text_size: self.size
                PrimaryButton:
                    text: '📊  Impact Dashboard'
                    on_release: app.go('dashboard')
                PrimaryButton:
                    text: '📱  Identify E-Waste'
                    on_release: app.go('categories')
                PrimaryButton:
                    text: '♻️  Recycling Guide'
                    on_release: app.go('guide')
                PrimaryButton:
                    text: '📍  Recycling Centres'
                    on_release: app.go('centres')
                PrimaryButton:
                    text: '🚚  Request Pickup'
                    on_release: app.go('pickup')
                Label:
                    text: 'Small Actions. Big Impact.\\nGive your old electronics a greener future.'
                    size_hint_y: None
                    height: dp(60)
                    halign: 'center'
                    color: (0.09, 0.50, 0.32, 1)
                    font_size: '14sp'

<ContentScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(18)
        spacing: dp(12)
        canvas.before:
            Color:
                rgba: (0.97, 0.98, 0.97, 1)
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: root.page_title
            size_hint_y: None
            height: dp(42)
            font_size: '25sp'
            bold: True
            color: (0.075, 0.196, 0.153, 1)
            halign: 'left'
            text_size: self.size
        Label:
            text: root.page_subtitle
            size_hint_y: None
            height: dp(42)
            font_size: '14sp'
            color: (0.40, 0.47, 0.43, 1)
            halign: 'left'
            valign: 'top'
            text_size: self.size
        ScrollView:
            do_scroll_x: False
            GridLayout:
                id: cards
                cols: 1
                spacing: dp(12)
                size_hint_y: None
                height: self.minimum_height
        PrimaryButton:
            text: '← Back to Home'
            on_release: app.go('home')

<PickupScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(18)
        spacing: dp(10)
        canvas.before:
            Color:
                rgba: (0.97, 0.98, 0.97, 1)
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'Request Pickup'
            size_hint_y: None
            height: dp(42)
            font_size: '25sp'
            bold: True
            color: (0.075, 0.196, 0.153, 1)
            halign: 'left'
            text_size: self.size
        Label:
            text: 'Prepare a sample collection request.'
            size_hint_y: None
            height: dp(28)
            font_size: '14sp'
            color: (0.40, 0.47, 0.43, 1)
            halign: 'left'
            text_size: self.size
        ScrollView:
            do_scroll_x: False
            GridLayout:
                cols: 1
                spacing: dp(8)
                size_hint_y: None
                height: self.minimum_height
                Label:
                    text: 'Your Name'
                    size_hint_y: None
                    height: dp(24)
                    halign: 'left'
                    text_size: self.size
                    color: (0.075, 0.196, 0.153, 1)
                TextInput:
                    id: name_input
                    hint_text: 'Enter your name'
                    multiline: False
                    size_hint_y: None
                    height: dp(48)
                Label:
                    text: 'Phone Number'
                    size_hint_y: None
                    height: dp(24)
                    halign: 'left'
                    text_size: self.size
                    color: (0.075, 0.196, 0.153, 1)
                TextInput:
                    id: phone_input
                    hint_text: 'Enter 10-digit phone number'
                    input_filter: 'int'
                    multiline: False
                    size_hint_y: None
                    height: dp(48)
                Label:
                    text: 'Device Type'
                    size_hint_y: None
                    height: dp(24)
                    halign: 'left'
                    text_size: self.size
                    color: (0.075, 0.196, 0.153, 1)
                Spinner:
                    id: device_input
                    text: 'Select a device'
                    values: ['Mobile Phone', 'Laptop / Computer', 'TV / Monitor', 'Battery', 'Chargers / Cables', 'Other Electronics']
                    size_hint_y: None
                    height: dp(48)
                Label:
                    text: 'Pickup Area / City'
                    size_hint_y: None
                    height: dp(24)
                    halign: 'left'
                    text_size: self.size
                    color: (0.075, 0.196, 0.153, 1)
                TextInput:
                    id: area_input
                    hint_text: 'Enter your area or city'
                    multiline: False
                    size_hint_y: None
                    height: dp(48)
                Label:
                    text: 'Additional Details'
                    size_hint_y: None
                    height: dp(24)
                    halign: 'left'
                    text_size: self.size
                    color: (0.075, 0.196, 0.153, 1)
                TextInput:
                    id: details_input
                    hint_text: 'Quantity or other details (optional)'
                    size_hint_y: None
                    height: dp(90)
            bar_width: dp(4)
        PrimaryButton:
            text: 'Submit Pickup Request'
            on_release: app.submit_pickup()
        PrimaryButton:
            text: '← Back to Home'
            on_release: app.go('home')
"""

class HomeScreen(Screen):
    pass

class ContentScreen(Screen):
    page_title = StringProperty("")
    page_subtitle = StringProperty("")

class PickupScreen(Screen):
    pass

class EWasteRescueApp(App):
    def build(self):
        self.title = "E-Waste Rescue"
        self.store = JsonStore("pickup_requests.json")
        Builder.load_string(KV)
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ContentScreen(name="content"))
        sm.add_widget(PickupScreen(name="pickup"))
        return sm

    def go(self, page):
        if page == "home":
            self.root.current = "home"
            return
        if page == "pickup":
            self.root.current = "pickup"
            return

        screen = self.root.get_screen("content")
        screen.ids.cards.clear_widgets()
        pages = {
            "categories": ("Identify E-Waste", "Choose the right way to handle each item.", [
                ("📱 Mobile Phones", "Back up your data and erase personal information. Consider repair, reuse or authorised recycling."),
                ("💻 Laptops & Computers", "Protect your files before repair, reuse or authorised recycling."),
                ("🔌 Chargers & Cables", "Keep electronic accessories out of general rubbish. Use a suitable collection point."),
                ("🔋 Batteries", "Do not puncture, crush or burn batteries. Keep damaged batteries away from heat."),
                ("🎧 Earphones & Accessories", "Check for repair or reuse before recycling through suitable collection channels."),
                ("🖥️ TVs & Monitors", "Handle screens carefully. Do not break or burn them. Use an authorised collection point."),
            ]),
            "guide": ("Recycling Guide", "Simple steps towards responsible recycling.", [
                ("01 Repair or Reuse", "Check whether your device can be repaired, donated or safely reused."),
                ("02 Protect Your Data", "Back up important files and erase personal information before handing over a device."),
                ("03 Handle Batteries Carefully", "Never burn or puncture batteries. Follow appropriate battery collection guidance."),
                ("04 Choose Authorised Recyclers", "Use authorised collection centres or recyclers."),
            ]),
            "centres": ("Recycling Centres", "Verify details and authorisation before visiting.", [
                ("🔎 Verify Before Visiting", "Use the official CPCB E-Waste EPR Portal or TNPCB resources to check current recycler registration, accepted devices and address. Demo listings can become outdated."),
                ("Official Information", "Open the CPCB E-Waste EPR Portal using the button below."),
            ]),
            "dashboard": ("Impact Dashboard", "A snapshot of our sustainability mission.", [
                ("♻ TOTAL DEVICES: 128", "Illustrative demo statistics only; these are not live collection totals."),
                ("📱 Phones: 76", "Illustrative demo statistic."),
                ("💻 Other devices: 52", "Illustrative demo statistic."),
                ("🌍 Our Mission", "Promote repair, reuse and authorised recycling to reduce electronic waste."),
                ("💚 Make a Difference", "Protect personal data and choose authorised e-waste collection channels."),
            ]),
        }
        title, subtitle, cards = pages[page]
        screen.page_title = title
        screen.page_subtitle = subtitle
        for heading, body in cards:
            card = Factory.InfoCard(title_text=heading, body_text=body)
            screen.ids.cards.add_widget(card)
        if page == "centres":
            from kivy.uix.button import Button
            btn = Button(text="Official Recycler Information", size_hint_y=None, height=50,
                         background_normal="", background_color=get_color_from_hex(GREEN),
                         color=(1,1,1,1), bold=True)
            btn.bind(on_release=lambda *_: webbrowser.open("https://eprewaste.cpcb.gov.in/"))
            screen.ids.cards.add_widget(btn)
        self.root.current = "content"

    def submit_pickup(self):
        screen = self.root.get_screen("pickup")
        name = screen.ids.name_input.text.strip()
        phone = screen.ids.phone_input.text.strip()
        device = screen.ids.device_input.text
        area = screen.ids.area_input.text.strip()
        details = screen.ids.details_input.text.strip()

        if not name or not phone or not area or device == "Select a device":
            self.message("Missing details", "Please fill in name, phone, device and area.")
            return
        if not re.fullmatch(r"[0-9]{10}", phone):
            self.message("Invalid phone number", "Enter a valid 10-digit phone number.")
            return

        record = {
            "name": name, "phone": phone, "device": device,
            "area": area, "details": details
        }
        self.store.put("latest_request", **record)
        self.message("Pickup Request Saved ♻️",
                     f"Thank you, {name}! Your details are saved on this device. "
                     "The request has not been sent to a collection team; an online service connection is required.")
        screen.ids.name_input.text = ""
        screen.ids.phone_input.text = ""
        screen.ids.device_input.text = "Select a device"
        screen.ids.area_input.text = ""
        screen.ids.details_input.text = ""

    def message(self, title, body):
        layout = BoxLayout(orientation="vertical", padding=14, spacing=10)
        layout.add_widget(Label(text=body, halign="center", valign="middle"))
        from kivy.uix.button import Button
        close = Button(text="OK", size_hint_y=None, height=44,
                       background_normal="", background_color=get_color_from_hex(GREEN))
        layout.add_widget(close)
        popup = Popup(title=title, content=layout, size_hint=(0.88, 0.42), auto_dismiss=False)
        close.bind(on_release=popup.dismiss)
        popup.open()

if __name__ == "__main__":
    EWasteRescueApp().run()
