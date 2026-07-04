from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
import os
Window.size = (500, 400)
Window.clearcolor = (0.12, 0.12, 0.14, 1)


class ImageGalleryApp(App):

    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=15, spacing=6)
        buttons_layout = BoxLayout(orientation="horizontal",size_hint=(None, None),width=250,height=50,spacing=10)
        buttons_wrapper = AnchorLayout(anchor_x="center",anchor_y="center",size_hint_y=None,height=50)
        self.gallery_title = Label(text = "Image Gallery",font_size = "22sp",size_hint_y = None, height = 35,
                                    color=(1,1,1,1), bold= True)
        self.image_list = self.load_images()
        self.current_index = 0

        if self.image_list:
            first_image = self.image_list[self.current_index]
        else:
            first_image = ""
        
        self.image_widget = Image(source= first_image, fit_mode="contain", size_hint_y=1)
        
        if self.image_list:
            counter_text = f"Image {self.current_index + 1} / {len(self.image_list)}"
        else:
            counter_text = ""
        self.counter_label = Label(text=counter_text,font_size="16sp",size_hint_y=None,height=30,
                                    color=(1, 1, 1, 1))
        self.next_button = Button(text="Next", font_size="20sp", size_hint_y=None, height=50,size_hint_x=None,width=120,
                                  background_normal="",background_color=(0.15, 0.45, 0.85, 1),color=(1, 1, 1, 1),bold=True)
        self.prev_button = Button(text="Previous", font_size="20sp", size_hint_y=None, height=50,size_hint_x=None,width=120,
                                  background_normal="",background_color=(0.15, 0.45, 0.85, 1),color=(1, 1, 1, 1),bold=True)

        if not self.image_list:
            self.next_button.disabled = True
            self.gallery_title.text = "No images found"
            self.prev_button.disabled = True
        
        self.next_button.bind(on_press= self.show_next_image)
        self.prev_button.bind(on_press= self.show_previous_image)

        main_layout.add_widget(self.gallery_title)
        main_layout.add_widget(self.image_widget)
        main_layout.add_widget(self.counter_label)
        buttons_layout.add_widget(self.prev_button)
        buttons_layout.add_widget(self.next_button)
        buttons_wrapper.add_widget(buttons_layout)
        main_layout.add_widget(buttons_wrapper)

        return main_layout
    
    def show_next_image(self, instance):

        if not self.image_list:
            return
        self.current_index += 1
        if self.current_index == len(self.image_list):
            self.current_index = 0
        self.image_widget.source = self.image_list[self.current_index]
        self.counter_label.text = f"Image {self.current_index + 1} / {len(self.image_list)}"

    def show_previous_image(self, instance):
        if not self.image_list:
            return
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.image_list) - 1
        self.image_widget.source = self.image_list[self.current_index]
        self.counter_label.text = f"Image {self.current_index + 1} / {len(self.image_list)}"

    def load_images(self):
        image_paths = []
        image_folder = "images"
        if not os.path.exists(image_folder):
            return []
        files = sorted(os.listdir(image_folder))
        for filename in files:
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                full_path = os.path.join(image_folder, filename)
                image_paths.append(full_path)
        
        return image_paths
            




if __name__ == "__main__":
    ImageGalleryApp().run()
