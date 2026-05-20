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

//カテゴリ選択絞り込み

const mainCategorySelect = document.getElementById('main-category-select')

if(mainCategorySelect){
  mainCategorySelect.addEventListener('change',(e)=>{
    const mainCategoryId = e.target.value

    if(mainCategoryId=='brank'){
      fetch(`/api/select_reset/?main_category_id=${mainCategoryId}`)
    }else{
      fetch(`/api/sub_categories/?main_category_id=${mainCategoryId}`)
      
    };
    
    .then(response => response.json())

    .then(data =>{
      const mainCategorySelect = document.getElementById('main-category-select')
      console.log(mainCategoryId)      
      //if(mainCategoryId == 'blank'){
        subCategorySelect.innerHTML = '<option value="blank">カテゴリを選択</option>'
      //} else {
        //subCategorySelect.innerHTML = ''
      //}
      data.forEach(sub_category => {
        const option = document.createElement('option')
        option.value = sub_category.id
        option.text = sub_category.name
        subCategorySelect.appendChild(option)
      })
    }) 
  })
};

const subCategorySelect = document.getElementById('sub-category-select')
if(subCategorySelect){
  subCategorySelect.addEventListener('change',(e)=>{
    const subCategoryId = e.target.value
    //console.log(subCategoryId)

    fetch(`/api/main_categories/?sub_category_id=${subCategoryId}`)
    .then(response => response.json())

    .then(data =>{
      
      mainCategorySelect.innerHTML = '<option value="blank">カテゴリを選択</option>'
      data.forEach(main_category => {
        const option = document.createElement('option')
        option.value = main_category.id
        option.text = main_category.name
        mainCategorySelect.appendChild(option)
      })
      if(data.length > 0 && subCategoryId != "blank") {
          mainCategorySelect.value = data[0].id
      }

    }) 
  })
};
