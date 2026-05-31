//コマンドワンクリックコピー機能
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

//カテゴリ選択のデータリストをリセット
function listReset(){
  const mainCategorySelect = document.getElementById('main-category-select')
  fetch(`/api/list_reset/?category_type=${"main"}`)
  .then(response => response.json())
  .then(data =>{
    console.log(data)
    mainCategorySelect.innerHTML = '<option value="">カテゴリを選択</option>'
    data.forEach(mainCategory => {
      const option = document.createElement('option')
      option.value = mainCategory.id
      option.text = mainCategory.name
      mainCategorySelect.appendChild(option)
    })
  })
  const subCategorySelect = document.getElementById('sub-category-select')
  fetch(`/api/list_reset/?category_type=${"sub"}`)
  .then(response => response.json())
  .then(data =>{
    console.log(data)
    subCategorySelect.innerHTML = '<option value="">カテゴリを選択</option>'
    data.forEach(subCategory => {
      const option = document.createElement('option')
      option.value = subCategory.id
      option.text = subCategory.name
      subCategorySelect.appendChild(option)
    })
  })
}

//カテゴリ選択のフィルタリング
const mainCategorySelect = document.getElementById('main-category-select')
const subCategorySelect = document.getElementById('sub-category-select')

mainCategorySelect.addEventListener('change',(e)=>{
  const mainCategoryId = e.target.value
  
  if(mainCategoryId == ''){
    listReset()
    return
  };
  
  fetch(`/api/filtering_main/?main_category_id=${mainCategoryId}`)
  .then(response => response.json())
  .then(data =>{
    console.log(data)
    console.log(Array.isArray(data))
    subCategorySelect.innerHTML = '<option value="">カテゴリを選択</option>'
    data.forEach(subCategory => {
      const option = document.createElement('option')
      option.value = subCategory.id
      option.text = subCategory.name
      subCategorySelect.appendChild(option)
      if(mainCategoryId != '') {
        subCategorySelect.value = data[0].id
      }
    })
  })
});

subCategorySelect.addEventListener('change',(e)=>{
  const subCategoryId = e.target.value

  if(subCategoryId == ''){
    listReset()
    return
  };

  fetch(`/api/filtering_sub/?sub_category_id=${subCategoryId}`)
  .then(response => response.json())
  .then(data =>{
    mainCategorySelect.innerHTML = '<option value="">カテゴリを選択</option>'
    console.log(data)
    console.log(Array.isArray(data))
    data.forEach(mainCategory => {
      const option = document.createElement('option')
      option.value = mainCategory.id
      option.text = mainCategory.name
      mainCategorySelect.appendChild(option)
      if(subCategoryId != '') {
        mainCategorySelect.value = data[0].id
      }
    })
  })
});
      
