from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, count_prizes_remaining

card = PokemonCardDef(
    guid="7996ca4d-8b1d-5f0c-8014-51e13da19f4d",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name",
    display_name="Carbink",
    searchable_by=["Carbink", "Basic", "Carbink"],
    subtypes=["Basic"],
    collector_number=242,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=703,
    abilities=[
        Ability(
            title="Double Type",
            game_text="As long as this Pok\u00e9mon is in play, it is Fighting and Psychic type.",
            effect=unimplemented,
        ),
        Attack(
            title="Counter Jewel",
            game_text="If your opponent has 2 or fewer Prize cards remaining, this attack does 100 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            effect=bonus_if(lambda ctx: count_prizes_remaining("theirs")(ctx) <= 2, 100),
        ),
    ],
)