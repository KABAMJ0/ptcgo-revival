from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="34ec0c72-e492-5d78-a3cd-f7ab5cb10041",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=490,
    abilities=[
        Ability(
            title="Wave Veil",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)