Dont like Readme File? Check the Notion Document:
https://othmanyoutubetutorial.notion.site/Setting-up-Firebase-with-the-Swift-project-in-Xcode-d1740682ac48407fa2cf7bdeea9f4dd4 
---

- Go to firebase, create app with the [help of the link](https://firebase.google.com).
- Make sure your App-Identifier must be same with the Firebase App.
- After completing your app registration firebase will give you GoogleInfo.plist, add it in the root project folder.

- Go to the Firebase database and Create a new node with the following data

`"placeholder : Hello world"`

- Enter the project folder with the terminal and perform `pod install`
- Open the ARTextDemoApp.xcodeworkspace that got generated due to pod install
- Add the Firebase SDK locally after git cloning it [from the following link](https://github.com/firebase/firebase-ios-sdk.git)
- Wait for the Dependencies to be Indexed
- Open ViewController and create firebase DB Instance.
- Fetch  data with respect to the given node. In my case is "placeholder". How to read and write data in firebase [you can follow this link](https://firebase.google.com/docs/database/ios/read-and-write).

---
