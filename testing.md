# 🧶 The Crochet Files

## 🧪 Testing

The website is fully responsive and has been tested on multiple device sizes.

---

### 🖥️ Desktop View

✅ The layout scales correctly  
✅ Navigation works as expected  
✅ All buttons and forms are accessible  

#### 📸 Screenshots

 Landing Page  
  ![image](docs/landing-page.png)

 Navigation Bar  
  ![image](docs/navbar.png)

 Add New Project  
  ![image](docs/add-page.png)

 Edit Project  
  ![image](docs/edit-page.png)

 View Project Page  
  ![image](docs/project-page.png)

 No Comments State  
  ![image](docs/no-comment.png)

---

### 📱 Mobile View

✅ Navigation collapses correctly  
✅ Forms are readable and scrollable  
✅ Cards and buttons scale appropriately  

#### 📸 Screenshots

 Home View  
  ![image](docs/mobile-home-view.png)

 Navigation Menu  
  ![image](docs/mob-nav.png)

 Add New Project  
  ![image](docs/mob-new-pat.png)

 Edit Project  
  ![image](docs/mob-edit.png)

 View Project  
  ![image](docs/mob-view.png)

 Comment Section  
  ![image](docs/mob-com.png)

## 🧪 Manual Test Cases

The following features were manually tested across desktop and mobile devices:

| Feature                   | Test Case Description                                  | Status   |
|---------------------------|--------------------------------------------------------|----------|
| 🔐 User Registration      | Sign up with valid and invalid credentials             | ✅ Pass   |
| 🔓 User Login/Logout      | Login/logout flow works as expected                    | ✅ Pass   |
| ➕ Add Project             | Form validates input and displays project on submit    | ✅ Pass   |
| ✏️ Edit Project           | Changes are saved and reflected on the detail page     | ✅ Pass   |
| ❌ Delete Project         | Project is removed and no longer accessible            | ✅ Pass   |
| 💬 Comment on Project     | Adds comment and displays it beneath project           | ✅ Pass   |
| ❤️ Like Project           | Like counter updates and toggles properly              | ✅ Pass   |
| 📱 Mobile Responsiveness  | Pages adapt correctly to smaller screen sizes          | ✅ Pass   |
| 🧭 Navbar Functionality   | All links and dropdowns navigate correctly             | ✅ Pass   |

## Debug Off

The project uses an option called DEBUG to help keep the site safe when it is live. This is disabled in production so that sensitive data is not displayed if an issue occurs. When DEBUG is turned off, additional security options are enabled, such as mandating HTTPS and protecting cookies. These help to keep user data protected. When working locally on your PC (DEBUG enabled), these options are disabled to make testing and development easier.

![image](docs/debug-two.png) ![image](docs/debug-one.png)

