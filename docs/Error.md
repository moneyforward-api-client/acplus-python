# Error

エラー
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | エラー種別:   * &#x60;validation_failed&#x60;: リクエストボディやパラメータのバリデーションエラー   * &#x60;operation_not_completed&#x60;: 処理待ちや処理中のリクエストに対し、ファイルダウンロードや削除を要求した   * &#x60;invalid_credential&#x60;: 認証・認可情報が不正   * &#x60;permission_denied&#x60;: APIを実行する権限がない   * &#x60;request_not_found&#x60;: 指定された作成要求IDが存在しない   * &#x60;data_creation_failed&#x60;: 作成要求を受けたが、その後の処理でデータやファイル生成に失敗した   * &#x60;unsupported_media_type&#x60;: APIでサポートされていないリクエスト形式。Content-Type が不正な場合など。   * &#x60;internal_error&#x60;: 内部エラー  | [default to 'internal_error']
**title** | **str** | エラー概要 | 
**detail** | **str** | エラーの詳細な説明 | 
**errors** | [**list[ErrorDetail]**](ErrorDetail.md) | エラー詳細のリスト | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


