from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1b582673-dc78-54d3-9895-52cc33aa6788",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WailordEX.Name",
    display_name="Wailord-EX",
    searchable_by=["Wailord-EX", "Basic", "EX", "WailordEX"],
    subtypes=["Basic", "EX"],
    collector_number=38,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=250,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=321,
    abilities=[
        Ability(
            title="Water Veil",
            game_text="Whenever you attach an Energy card from your hand to this Pok\u00e9mon, remove all Special Conditions from it.",
            effect=unimplemented,
        ),
        Attack(
            title="High Breaching",
            game_text="This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 5},
            damage=120,
            effect=unimplemented,
        ),
    ],
)