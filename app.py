<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .item {
            display: flex;
            justify-content: center;
            align-items: center;
            border: 1px solid #181818;
            font-size: 1.2rem;
            font-weight: bold;
        }

        .color1 {
            background-color: #78FF96;
        }

        .color2 {
            background-color: #6E95FB;
        }


        .container {
            padding: 5px;
            display: grid;
            grid-template-columns: 150px 150px;
            grid-auto-rows: 150px 150px 150px;
            grid-gap: 15px;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }

        .item1 {
            grid-column: 1 / 3;
            grid-row: 1 / 3;
            border-radius: 20px;
            border: none;
            box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);

        }

        .item2 {

            border-radius: 20px;
            grid-row: 3 / 5;
            border: none;

            box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);

        }

        .item3 {
            border-radius: 20px;
            border: none;

            box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);

        }

        .item4 {
            border-radius: 20px;
            border: none;

            box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);

        }

        .hi {
            background-color: #0099ff;
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translate(-50%, -50%);
        }

        .memo-container {
            position: absolute;
            top: 110%;
            left: 50%;
            transform: translate(-50%, -50%);
        }

        .memoinput {
            width: 200px;
            height: 20px;
            border-radius: 10px;
            background-color: #6E95FB;
            border: none;
            margin-right: 10px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);

        }

        .memo {
            width: 300px;
            height: 300px;
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);

        }

        .memo div {
            padding: 20px;
        }

        #myCanvas {
            position: absolute;
            top: 150%;
            left: 50%;
            transform: translate(-50%, -50%);
        }

        .writememo {
            margin: auto;
            margin-bottom: 10px;
            display: flex;
        }

        .alertimg {
            height: 50px;
            width: 50px;
        }

        .lookalertbtn {
            width: 50px;
            height: 50px;
            border: none;
            border-radius: 10px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
            
        }

        .deletebtn {
            background-color: none;
        }

        .memobtn {
            border: none;
            color: white;
            border-radius: 10px;
            box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);

        }
        .dday{
            color: white;
            font-size: 12px;
        }
        .container div{
            color: white;
        }
        .pepercent{
            margin-left: 10px;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="item item1 color2">
            <div class="lunch">
                <div style="position: relative; left: 35%; top: 0;">점심메뉴</div>

            </div>
        </div>
        <div class="item item2 color1">
            <div class="currentschedule">
                시간표

            </div>
        </div>
        <div class="item item3 color2">
            <div class="pepercent"></div>
        </div>
        <div class="item item4 color1">
            <div>
                <div class="testdday dday"></div>
                <div class="vacationdday dday"></div> 
                <div class="competitiondday dday"></div>
            </div>
        </div>


    </div>


    <div class="memo-container ">
        <div class="writememo">
            <input type="text" class="memoinput">
            <button class="memobtn color2">메모</button>
        </div>
        <div class="memo color1">
            <div>
                안녕
                <button class="deletebtn">x</button>
            </div>
        </div>
    </div>





    <button class="lookalertbtn color2">알림</button>



    <script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
    <canvas id="myCanvas" width="370" height="250" style="border:1px solid #000;"></canvas>

    <script>
        const memoInput = document.querySelector('.memoinput')
        const addmemobtn = document.querySelector('.memobtn')
        const container = document.querySelector('.memo')
        const currentalertbtn = document.querySelector('.lookalertbtn')



        swal('알림', '{{currentalert}}', 'info');

        currentalertbtn.addEventListener('click', () => {
            swal('알림', '{{currentalert}}', 'info');
        })
        function plusmemolocalstorage(writememo) {
            let array
            if (JSON.parse(localStorage.getItem('memo')) == null) {
                array = []
            }
            else {
                array = JSON.parse(localStorage.getItem('memo'))
            }
            array.push(writememo)
            localStorage.setItem('memo', JSON.stringify(array));
        }
        function deletememo(event) {
            const memo = event.target.parentElement
            memo.remove()
            let arr = JSON.parse(localStorage.getItem('memo'))
            for (var i = 0; i < arr.length; i++) {
                if (arr[i] == memo.innerText.replace('delete', '')) {
                    arr.splice(i, 1);
                    i--;
                }
            }
            localStorage.setItem('memo', JSON.stringify(arr))
        }
        addmemobtn.addEventListener('click', () => {
            const memo = document.createElement('div')
            memo.innerText = memoInput.value
            const deletebtn = document.createElement('button')
            deletebtn.classList = 'deletebtn'
            deletebtn.innerText = 'delete'
            memo.appendChild(deletebtn)
            container.appendChild(memo)
            deletebtn.addEventListener('click', deletememo)
            plusmemolocalstorage(memoInput.value)
        })

        console
        function extractNumbersFromString(inputString) {
            // 입력 문자열에서 숫자만 추출
            var numbers = inputString.match(/\d+/g);
            if (numbers) {
                // 숫자 배열을 문자열로 변환하여 반환
                return numbers.join('');
            } else {
                return "문자열에서 숫자를 찾을 수 없습니다.";
            }
        }
        var currentDate = new Date();

        // 년, 월, 일을 가져와서 필요한 형식에 맞게 조정
        var year = currentDate.getFullYear();
        var month = (currentDate.getMonth() + 1).toString().padStart(2, '0'); // 월은 0부터 시작하므로 1을 더하고, 두 자리 숫자로 만들기 위해 padStart 사용
        var day = currentDate.getDate().toString().padStart(2, '0'); // 두 자리 숫자로 만들기 위해 padStart 사용
        var dayIndex = currentDate.getDay();

        // 날짜 문자열 조합
        var formattedDate = year + month + day;
        formattedDate = '20240307'
        // 결과 출력
        var weekdays = ["일", "월", "화", "수", "목", "금", "토"];

        const schedule = {
            '월': ['체육', '과학', '역사', '수학', '기가', '국어'],
            '화': ['스포츠', '영어', '국어', '기가', '체육', '사회', '동아리'],
            '수': ['수학', '영어', '미술', '국어', '사회', '음악'],
            '목': ['체육', '수학', '국어', '역사', '과학', '영어,', '기가'],
            '금': ['사회', '미술', '과학', '영어', '기가', '역사']
        }
        const timeschedule = []
        const approximatetimeschedule = [['0900', '1000'], ['1000', '1100'], ['1100', '1200'], ['1200', '1300'], ['1300', '1400'], ['1400', '1500'], ['1500', '1600']]
        const currentSchedule = schedule[weekdays[dayIndex]]
        const currentschedulediv = document.querySelector('.currentschedule')

        currentSchedule.forEach((r) => {
            let Div = document.createElement('div')
            Div.innerText = r
            currentschedulediv.appendChild(Div)
        })


        let writename
        let name
        const lunchdate = formattedDate
        $.ajax({
            url: `https://open.neis.go.kr/hub/mealServiceDietInfo?KEY=f6e86c64f5744a28a326715cb9045d9b&Type=xml&pIndex=1&pSize=10&ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7751012&MLSV_YMD=${lunchdate}`, //데이터를 주고받을 파일 주소 입력,
            data: 'xml',
            async: false,
            success: function (result) {
                // console.log(result)
                let name = result.querySelector("DDISH_NM")
                name = name.textContent
                writename = name

            },
            error: function () {
                console.log("error")
            }
        })

        name = writename
        let lunchnamelist = []
        for (i in writename) {
            name = name.replace('<br/>', '\n')

        }
        let Div = document.createElement('div')
        Div.innerText = name
        document.querySelector('.lunch').appendChild(Div)

        console.log(name)
        // console.log(writename)


        const date = formattedDate
        const time = '0800'
        const Location = { 'x': '62', 'y': '120' }
        var Url = `http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst?serviceKey=pnQ5v4XETtnvKlJ%2BqsVcx8ufZ4p47dIaU0VE53H4ql3yZ0vpeuDWpQo9myqZ8DrHeFM%2FtSzPq0ZG0maI5YGmsA%3D%3D&numOfRows=60&pageNo=1&base_date=${date}&base_time=${time}&nx=${Location['x']}&ny=${Location['y']}&dataType=JSON`
        var rain = {}
        var result = {}
        $.ajax({
            url: Url,
            data: 'json',
            async: false,
            success: function (result) {
                result['response']['body']['items']['item'].forEach((res) => {
                    if (res['category'] == 'RN1') {
                        rain[res["fcstTime"]] = res["fcstValue"]
                    }
                })
            },
            error: function () {
                console.log("error")
            }
        })



        const pepercent = document.querySelector('.pepercent')
        function rainpercentpe(starttime, endtime, weatherdata) {
            var arroundrainpercent = 0 //주변시간 강수 여부
            var ifrain = 0
            for (k in weatherdata) {

                if (parseInt(starttime) - parseInt(k) <= 0 && parseInt(endtime) - parseInt(k) > 0) {
                    if (weatherdata[k] != '강수없음') {
                        ifrain = parseInt(extractNumbersFromString(weatherdata[k]))
                    }
                }
                else {
                    if (weatherdata[k] != '강수없음' && parseInt(extractNumbersFromString(weatherdata[k])) > 2) {
                        arroundrainpercent += 1 //강수있으면 +1

                    }

                }

            }
            if (arroundrainpercent == 0 && !ifrain) {//주변 강수량이 없고 그 시간 강수량이 없으면
                console.log('주변 강수량이 없고 그 시간 강수량이 없습니다 -체육 할 확률이 매우 높습니다')
                pepercent.innerText = ' -체육 할 확률이 매우 높습니다'
            }
            else if (arroundrainpercent == 0 && ifrain) {//주변 강수량은 없지만 그 시간 강수량이 있으면
                if (ifrain < 2) {
                    console.log('체육 시간 주변에 강수량이 없고 체육시간에는 아주 조금의 비가 예상됩니다 -체육할 확률이 높습니다')
                    pepercent.innerText = ' -체육할 확률이 높습니다'
                }
                else if (ifrain < 6) {
                    console.log('체육 시간 주변에 강수량이 없고 체육시간에는 조금의 비가 예상됩니다 -운이좋으면 체육할 수 있습니다')
                    pepercent.innerText = ' -운이좋으면 체육할 수 있습니다'
                }
                else if (ifrain < 10) {
                    console.log('체육 시간 주변에 강수량이 없고 체육시간에는 비가 예상됩니다 - 체육하기 힘들수 있습니다')
                    pepercent.innerText = ' - 체육하기 힘들수 있습니다'
                }
                else {
                    console.log('주변강수량은 없지만 체육 시간에는 비가 많이 내립니다 -체육은 힘들 수 있습니다')
                    pepercent.innerText = ' -체육은 힘들 수 있습니다'
                }
            }

            else if (arroundrainpercent > 0 && !ifrain) {//주변 강수량은 있지만 그 시간 강수량이 없으면
                console.log('체육시간 주변에는 비가 내리지만 체육시간에는 비가 안 내립니다 -운이 좋으면 체육 할 수 있습니다')
                pepercent.innerText = ' -운이 좋으면 체육 할 수 있습니다'
            }

            else if (arroundrainpercent > 0 && ifrain) {//주변 강수량이 있고 그 시간 강수량이  있으면
                if (ifrain < 2) {
                    console.log('체육 시간 주변에 강수량이 있고 체육시간에는 아주 조금의 비가 예상됩니다 -체육 못할 확률이 있습니다')
                    pepercent.innerText = ' -체육 못할 확률이 있습니다'
                }
                else if (ifrain < 6) {
                    console.log('체육 시간 주변에 강수량이 있고 체육시간에는 조금의 비가 예상됩니다 -체육 못할 수 있습니다')
                    pepercent.innerText = ' -체육 못할 수 있습니다'
                }
                else if (ifrain < 10) {
                    console.log('체육 시간 주변에 강수량이 있고 체육시간에는 비가 예상됩니다 -체육을 못할 확률이 높습니다')
                    pepercent.innerText = ' -체육을 못할 확률이 높습니다'
                }
                else {
                    console.log('주변강수량은 있고 체육 시간에는 비가 많이 내립니다 -체육을 못할 확률이 매우 높습니다')
                    pepercent.innerText = ' -체육을 못할 확률이 매우 높습니다'
                }
            }

        }
        for (var i = 0; i < currentSchedule.length; i++) {
            if (currentSchedule[i] == '체육') {
                rainpercentpe(approximatetimeschedule[currentSchedule.indexOf('체육')][0], approximatetimeschedule[currentSchedule.indexOf('체육')][1], rain)
            }

        }


        function calculateClosestFutureDday(dates, names) {
            // 현재 날짜 객체 생성
            var currentDate = new Date();

            // 미래 날짜만을 저장할 배열
            var futureDates = [];
            var filterednames = []
            // 현재 이후의 날짜만을 futureDates 배열에 저장
            dates.forEach(function (date) {
                if (date.getTime() > currentDate.getTime()) {
                    futureDates.push(date);
                    filterednames.push(names[dates.indexOf(date)])
                }
            });

            // 가장 가까운 미래 날짜 찾기
            var closestDate = futureDates[0];
            var closestDiff = Math.abs(futureDates[0].getTime() - currentDate.getTime());
            var closestName = filterednames[0]; // 가장 가까운 날짜의 이름

            for (var i = 1; i < futureDates.length; i++) {
                var diff = Math.abs(futureDates[i].getTime() - currentDate.getTime());
                if (diff < closestDiff) {
                    closestDiff = diff;
                    closestDate = futureDates[i];
                    closestName = names[i];
                }
            }

            // 가장 가까운 날짜의 디데이 계산
            var timeDiff = closestDate.getTime() - currentDate.getTime();
            var daysDiff = Math.ceil(timeDiff / (1000 * 3600 * 24));

            return { name: closestName, dday: daysDiff };
        }
        function gettestdday() {
            var dateA = new Date("2024-04-29");
            var dateB = new Date("2024-07-01");
            var dateC = new Date("2024-09-30");
            var dateD = new Date("2024-12-11");

            var names = ['1학기 중간', '1학기 기말', '2학기 중간', '2학기 기말']
            var dates = [dateA, dateB, dateC, dateD];

            var closestInfo = calculateClosestFutureDday(dates, names);

            if (closestInfo.dday !== Infinity) {
                console.log(closestInfo.name + " D-" + closestInfo.dday);
            }
            return closestInfo.name + " D-" + closestInfo.dday
        }
        function getvacationdday() {
            var dateA = new Date("2024-07-19");
            var dateB = new Date("2024-08-16");
            var dateC = new Date("2024-09-30");
            var dateD = new Date("2025-01-08");

            var names = ['여름방학식', '개학식', '겨울방학식', '개학']
            var dates = [dateA, dateB, dateC, dateD];

            var closestInfo = calculateClosestFutureDday(dates, names);

            if (closestInfo.dday !== Infinity) {
                console.log(closestInfo.name + " D-" + closestInfo.dday);
            }
            return closestInfo.name + " D-" + closestInfo.dday
        }
        function getcompetitiondday() {
            var dateA = new Date("2024-10-18");
            var currentDate = new Date();

            var timeDiff = dateA.getTime() - currentDate.getTime();
            var daysDiff = Math.ceil(timeDiff / (1000 * 3600 * 24));

            if (daysDiff !== Infinity) {
                console.log('체육대회,신릉제' + " D-" + daysDiff);
            }
            return '체육대회,신릉제' + " D-" + daysDiff
        }
        document.querySelector('.testdday').innerText = gettestdday()
        document.querySelector('.vacationdday').innerText = getvacationdday()
        document.querySelector('.competitiondday').innerText = getcompetitiondday()

        let partner_seat = []
        $.ajax({
            type: 'POST',
            async: false,
            url: 'http://127.0.0.1:5000/seats/',//데이터를 주고받을 파일 주소 입력,
            data: {
                use: 'show'
            },//보내는 데이터,
            dataType: 'json',
            success: function (result) {
                partner_seat = result
            },
            error: function () {
                //에러가 났을 경우 실행시킬 코드
            }
        })
        var canvas = document.getElementById("myCanvas");
        var ctx = canvas.getContext("2d");

        // 글자 스타일 설정
        ctx.font = "10px bold";
        ctx.fillStyle = "black";

        // 글자 쓰기
        ctx.fillText("1분단", 20, 50);
        ctx.fillText("2분단", 110, 50);
        ctx.fillText("3분단", 200, 50);
        ctx.fillText("4분단", 310, 50);


        var x = 10
        var y = 70
        for (var i = 0; i < 16; i++) {

            var partner1 = partner_seat[i][0]
            var partner2 = partner_seat[i][1]



            if (i == 4) {
                x = 100
                y = 70
            }
            if (i == 8) {
                x = 190
                y = 70
            }
            if(i == 12){
                x = 300
                y = 70
            }
            ctx.fillText(partner1, x, y);
            ctx.fillText(partner2, x + 35, y);
            y += 20

        }

    </script>
</body>

</html>
