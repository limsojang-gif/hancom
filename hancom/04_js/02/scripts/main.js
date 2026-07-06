// 1. id 가 title인 제목을 찾아서 title 상자에 담는다. 
// . 은 ~의 라고 해석 
// 같은 id로 셋이 연결: HTML id="title"= const title → CSS #title → JS
// -> html의 id tilte 과 연결한다. = 이것은 문서 선택자 css 의 #title과 같은 부분이다.

const title = document.querySelector("#title");
// const  id 에서 가져올 부분   (html에서 가져올 부분)  . 은 ~의 
const btn = document.querySelector("#btn");


// byn id 가 이벤트가 발생한다면 ( 클릭 -> 타이틀의 텍스트 컨텐츠가 hello world 로 바뀐다)
btn.addEventListener("click",() => {
    title.textContent="Hello World!!"
});

// () =>  이것의 의미는 이것을 클릭하면 이것이된다 라고 해석됨  정해진 양식으로 ()안에 무엇을 따로 입력할 필요는 없다. 