USE auto_convert_project_information;

-- プロジェクト情報テーブル
CREATE TABLE projects (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '主キー',
    company_name VARCHAR(255) COMMENT '企業名',
    person_in_charge VARCHAR(255) COMMENT '担当者',
    project_name VARCHAR(255) COMMENT '案件名',
    project_content TEXT COMMENT '案件内容',
    work_location VARCHAR(255) COMMENT '勤務地',
    period VARCHAR(255) COMMENT '期間',
    number_of_people VARCHAR(255) COMMENT '募集人数',
    price_requirements VARCHAR(255) COMMENT '単価要件',
    settlement VARCHAR(255) COMMENT '精算',
    interview VARCHAR(255) COMMENT '面談',
    summary TEXT COMMENT '要約',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時',
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日時',
    deleted_at DATETIME COMMENT '削除日時'
) COMMENT='プロジェクト情報';

-- スキル情報テーブル
CREATE TABLE skills (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '主キー',
    skill VARCHAR(255) COMMENT 'スキル',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時',
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日時',
    deleted_at DATETIME COMMENT '削除日時'
) COMMENT='スキル情報';

-- 企業情報テーブル
CREATE TABLE companies (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '主キー',
    company_name VARCHAR(255) COMMENT '企業名',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時',
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日時',
    deleted_at DATETIME COMMENT '削除日時'
) COMMENT='案件提供 企業情報';

-- 担当者情報テーブル
CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '主キー',
    company_id INT COMMENT '企業ID',
    contact_name VARCHAR(255) COMMENT '担当者名',
    email VARCHAR(255) NOT NULL COMMENT 'メールアドレス',
    phone_number VARCHAR(255) COMMENT '電話番号',
    FOREIGN KEY (company_id) REFERENCES companies(id),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時',
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日時',
    deleted_at DATETIME COMMENT '削除日時'
) COMMENT='担当者情報';

-- スキル情報と必須スキル情報の中間テーブル
CREATE TABLE project_skills (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '主キー',
    project_id INT COMMENT 'プロジェクトID',
    skill_id INT COMMENT 'スキルID',
    type VARCHAR(255) COMMENT '必須かどうかを表す種別',
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (skill_id) REFERENCES skills(id),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時',
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日時',
    deleted_at DATETIME COMMENT '削除日時'
) COMMENT='スキル情報の中間テーブル';