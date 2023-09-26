# aa-as-is

img2imgで入力画像をそのまま出力画像にするだけの[Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)（以下sdwebui）用のextensionです。

sdwebui v1.6.0で動作を確認しています。

## インストール

sdwebuiの通常のextensionと同じ方法でインストールすることができます。

1. sdwebuiの「Extensions」タブを開く。
2. 「Install from URL」タブを開く。
3. 「URL for extension's git repository」欄に `https://github.com/fai-9/aa-as-is` と入力する。
4. 「Install」ボタンを押す。
5. `Installed into /Users/fai-9/local-sd/stable-diffusion-webui/extensions/aa-as-is. Use Installed tab to restart.` というメッセージが表示されたら「Reload UI」を押してUIをリロードするか、sdwebuiを再起動する。

## 使い方

img2imgタブに「As Is」というアコーディオンが追加されるので、「Enable」にチェックを入れてください。

## 応用

### !After Detailerと組み合わせる

[!After Detailer](https://github.com/Bing-su/adetailer)（以下ADetailer）は生成画像に含まれる人や人の顔を自動検出して補正するためのextensionです。

ADetailerは一度画像を生成しないと適用できないため、生成画像を加工してから顔を補正したい時にはinpaintで顔の部分をマスクして画像を生成して適用するなど一手間が必要になります。また、そのようにした場合は顔が元々のものと変わってしまうなど、望ましくない副作用が生じることもあります。aa-as-isを使うことで、そのような問題を解消することができます。

ADetailerと組み合わせて画像を直接補正する方法は以下の通りです。

1. 「img2img」タブを開く。
2. 「Generation」の「img2img」タブに元画像をアップロードする。
3. 「Sampling steps」を1にする。（1でなくとも動作しますが、高速化のために1に設定すると良いでしょう）
4. 「As Is」アコーディオンを開いて「Enable」にチェックを入れる。
5. 「ADetailer」アコーディオンを開いて「Enable」にチェックを入れる。
6. ADetailerの各種設定を行う。
    - 「Inpainting」タブの「Use separate steps」についてはチェックを入れて「ADetailer steps」を適切に設定して下さい。（そうしないとstepsが1になってしまいます）
7. 「Genrate」を押して画像を生成する。

