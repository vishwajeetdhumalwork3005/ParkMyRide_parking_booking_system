// Enhanced UX & Validation for ParkMyRide
document.addEventListener('DOMContentLoaded', function(){
  
  // Signup form validation
  const signupForm = document.getElementById('signupForm')
  if(signupForm){
    signupForm.addEventListener('submit', function(e){
      const pwd = signupForm.querySelector('input[name=password]').value
      const conf = signupForm.querySelector('input[name=confirm_password]').value
      const email = signupForm.querySelector('input[name=email]').value
      
      // Validate email format
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      if(!emailRegex.test(email)){
        e.preventDefault()
        alert('Please enter a valid email address')
        return
      }
      
      // Validate password match
      if(pwd !== conf){
        e.preventDefault()
        alert('✗ Passwords do not match')
        return
      }
      
      // Validate password length
      if(pwd.length < 6){
        e.preventDefault()
        alert('✗ Password must be at least 6 characters long')
        return
      }
    })
  }
  
  // Add focus styles to form inputs
  const inputs = document.querySelectorAll('input, textarea, select')
  inputs.forEach(input => {
    input.addEventListener('focus', function(){
      this.style.boxShadow = '0 0 0 3px rgba(20, 184, 166, 0.1)'
    })
    input.addEventListener('blur', function(){
      this.style.boxShadow = 'none'
    })
  })
  
  // Enhanced booking confirmation
  const bookForm = document.querySelector('form[id="bookForm"]')
  if(bookForm){
    bookForm.addEventListener('submit', function(e){
      const startEl = this.querySelector('input[name=start_time]')
      const endEl = this.querySelector('input[name=end_time]')
      
      const sd = new Date(startEl.value)
      const ed = new Date(endEl.value)
      
      if(ed <= sd){
        e.preventDefault()
        alert('✗ End time must be after start time')
        return
      }
      
      if(!confirm('✓ Confirm this booking?')){
        e.preventDefault()
      }
    })
  }
  
  // Smooth scroll behavior
  document.querySelectorAll('a[href^=\"#\"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href')
      if(href !== '#'){
        e.preventDefault()
        const target = document.querySelector(href)
        if(target){
          target.scrollIntoView({behavior: 'smooth'})
        }
      }
    })
  })
  
  // Add loading state to forms
  document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(){
      const buttons = this.querySelectorAll('button[type=\"submit\"]')
      buttons.forEach(btn => {
        btn.disabled = true
        btn.textContent = btn.textContent + ' ⏳'
      })
    })
  })
  
  // Real-time form validation
  const emailInputs = document.querySelectorAll('input[type=\"email\"]')
  emailInputs.forEach(input => {
    input.addEventListener('blur', function(){
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      if(this.value && !emailRegex.test(this.value)){
        this.style.borderColor = 'var(--red)'
        this.title = 'Please enter a valid email'
      } else {
        this.style.borderColor = 'var(--gray-300)'
        this.title = ''
      }
    })
  })
  
  // Phone number formatting
  const phoneInputs = document.querySelectorAll('input[type=\"text\"][name=\"phone\"]')
  phoneInputs.forEach(input => {
    input.addEventListener('input', function(){
      let value = this.value.replace(/\D/g, '')
      if(value.length > 10) value = value.slice(0, 10)
      this.value = value
    })
  })
  
  // Add visual feedback for available/booked status
  const badges = document.querySelectorAll('.badge')
  badges.forEach(badge => {
    if(badge.classList.contains('available')){
      badge.setAttribute('aria-label', 'Parking spot is available')
    } else if(badge.classList.contains('busy')){
      badge.setAttribute('aria-label', 'Parking spot is booked')
    }
  })
  
})
