-- models/cleaned_data.sql

with raw_data as (
    select
        channel_title,
        channel_username,
        id,
        message,
        date,
        media_path
    from {{ ref('raw_scraped_data') }}
),

cleaned_data as (
    select
        channel_title,
        channel_username,
        id,
        lower(message) as message,  -- Convert message text to lowercase
        date,
        media_path
    from raw_data
    where message is not null  -- Filter out rows with null messages
)

select * from cleaned_data
