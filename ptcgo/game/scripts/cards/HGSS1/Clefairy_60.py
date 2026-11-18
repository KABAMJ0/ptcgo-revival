from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b768a5e3-d2ea-544a-bb43-62e49e1ee223",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    display_name="Clefairy",
    searchable_by=["Clefairy", "Basic", "Clefairy"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="HGSS1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=35,
    abilities=[
        Attack(
            title="Minimize",
            game_text="During your opponent's next turn, any damage done to Clefairy by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Slap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)