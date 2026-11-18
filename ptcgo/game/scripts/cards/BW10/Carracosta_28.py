from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_for_bonus
from ptcgo.game.card_effects.trainers import all_of, named, is_item_card

card = PokemonCardDef(
    guid="b2aaabac-5980-5492-9f79-9da2927e9180",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carracosta.Name",
    display_name="Carracosta",
    searchable_by=["Carracosta", "Stage 1", "Carracosta"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name",
    family_id=564,
    abilities=[
        Attack(
            title="Fossil Clutch",
            game_text="You may discard an Item card that has Fossil in its name from your hand. If you do, this attack does 50 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=discard_for_bonus(predicate=all_of(is_item_card, named("fossil")), max_count=1, flat=50),
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)