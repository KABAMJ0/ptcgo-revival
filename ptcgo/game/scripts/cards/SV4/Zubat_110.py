from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="90305c28-cb00-556f-a45a-15b4ebbf3832",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    display_name="Zubat",
    searchable_by=["Zubat", "Basic", "Zubat"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=41,
    abilities=[
        Attack(
            title="Supersonic",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)