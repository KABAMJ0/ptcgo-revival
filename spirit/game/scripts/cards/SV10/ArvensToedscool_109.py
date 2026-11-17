from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="594eb601-40ef-5f42-aed0-5cb61c8ffa77",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensToedscool.Name",
    display_name="Arven's Toedscool",
    searchable_by=["Arven's Toedscool", "Basic", "ArvensToedscool"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=948,
    abilities=[
        Attack(
            title="Slight Intrusion",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)