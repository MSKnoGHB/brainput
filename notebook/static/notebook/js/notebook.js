const commandArea = document.getElementById('command-area')

if(commandArea){
  commandArea.addEventListener('click',(e)=>{
    const commandText = commandArea.innerText
    navigator.clipboard.writeText(commandText)
    const copyMessage = document.getElementById('copy-message')
    copyMessage.classList.add('show')
    setTimeout(()=>{
      copyMessage.classList.remove('show')
    }, 2000)
  });
}