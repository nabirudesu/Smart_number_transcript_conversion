import { useFormik } from 'formik';
import { useState } from 'react';
import React from 'react';
import * as Yup from 'yup';
import AudioRecorder from './AudioRecorder';

const CalculateForm = () => {
  const [dinarWords, setDinarWords] = useState('')
  const [isVoice, setIsvoice] = useState(true)
  const formSchema = Yup.object().shape({
    number: Yup.number().when('currency', {
      is: (value) => value === 'Dinar',
      then: (schema) => schema.min(0, 'يجب ان تكون القيمة اعلى من الصفر').max(9999999, "المبلغ تعدى المسموح به").required("الرجاء إدخال المبلغ المراد تحويله"),
      otherwise: (schema) => schema.min(100, 'يجب ان تكون القيمة اعلى من المئة سنتيم').max(999999999, "المبلغ تعدى المسموح به").required("الرجاء إدخال المبلغ المراد تحويله")
    }),
    currency: Yup.string()
  });
  const formik = useFormik({
    initialValues: {
      number: undefined,
      currency: "Dinar"
    },
    validationSchema: formSchema,
    onSubmit: async (values) => {
      let NumberSubmitted = 0
      let currencySubmitted = ""
      // here we return the dinarTextValue
      NumberSubmitted = values.number
      currencySubmitted = values.currency
      const response = await fetch('http://127.0.0.1:5000/number_to_words', {
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify({
          'number': NumberSubmitted,
          'currency': currencySubmitted,
        }),
        headers: { 'content-type': 'application/json; charset=UTF-8' },
      }).then((response) => response.json()).then((data) => data.transcription)
      setDinarWords(response)
      console.log(response)
    }
  });

  const Result = () => (
    <div className='w-full'>
      <h1 dir='rtl' className='text-xl text-green-300 mb-2'>
        النتيجة
      </h1>
      <div className='bg-gray-200 text-slate-900 color-slate-900 py-2 rounded-md'>
        <p dir='rtl' className='text-xl h-20 p-1.5'>
          {/* display the value rended from the backend dinar_number_to_arabic_words */}
          {dinarWords}
        </p>
      </div>
    </div>
  );
  return (
    <section className='bg-opacity-60 lg:w-3/5 w-4/5 bg-black p-8 rounded-xl'>
      <div className='align- mb-12'>
        <h1 dir='rtl' className='text-4xl text-white text-center font-bold'>
          تحويل المبالغ المالية إلى كتابة
        </h1>
      </div>
      <div className="flex justify-center gap-10 flex-col">
        <div className="flex flex-row justify-center gap-10 sm:gap-28 md:gap-58 bg-opacity-60 -m-8 bg-black p-8">
          <button type="button" onClick={() => setIsvoice(false)} className="flex items-center  text-2xl font-bold leading-6 text-white" aria-expanded="false">
            إدخال المبلغ بالصوت
          </button>
          <button type="button" onClick={() => setIsvoice(true)} className="flex items-center  text-2xl font-bold leading-6 text-white" aria-expanded="false">
            إدخال المبلغ بالارقام
          </button>
        </div>
        <div className='flex justify-center gap-10 flex-col'>
          <div className='flex flex-col gap-10 w-full'>
            {isVoice
              ? <form className='flex flex-col gap-2 justify-center' onSubmit={formik.handleSubmit}>
                <div className='flex flex-col gap-4'>
                  <div className='flex flex-row-reverse	w-full gap-4'>
                    <div className='flex flex-col w-full gap-2'>
                      <label dir='rtl' htmlFor='number' className='text-xl '>
                        القيمة بالارقام
                      </label>
                      <input
                        dir='rtl'
                        id='number'
                        type='number'
                        className='bg-gray-200 text-slate-900 color-slate-900 h-10 w-full px-4 py-2 rounded-md outline-none'
                        placeholder='أدخل الرقم'
                        onChange={formik.handleChange}
                        value={formik.values.number}
                        onBlur={formik.handleBlur} />
                    </div>
                    <div className='flex flex-col w-full gap-2'>
                      <label dir='rtl' htmlFor='number' className='text-xl '>
                        العملة المستعملة
                      </label>
                      <select
                        dir='rtl'
                        id='Currency'
                        name='currency'
                        type='number'
                        className='bg-gray-200 text-slate-900 w-full color-slate-900 h-10 px-4 py-2 rounded-md outline-none'
                        value={formik.values.currency}
                        onChange={formik.handleChange}
                      >
                        <option value="Dinar">الدينار الجزائري</option>
                        <option value="Centime">السنتيم</option>
                      </select>
                    </div>
                  </div>
                  {formik.errors.number && (
                    <p dir='rtl' className='text-red-500 text-sm'>
                      {formik.errors.number}
                    </p>
                  )}
                  <button dir='rtl' type="submit" className='bg-blue-500 text-white px-2 py-1 h-10 rounded-md hover:bg-blue-400 transition-colors'>
                    تحويل
                  </button>
                </div>
                <div className='flex w-full'>
                  <Result />
                </div>
              </form>
              : <AudioRecorder />}
          </div>
        </div>
      </div>
    </section>
  );
};

export default CalculateForm;
