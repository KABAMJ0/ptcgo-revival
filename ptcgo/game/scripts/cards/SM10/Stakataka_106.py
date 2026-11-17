from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8ac69d94-5497-5873-8f74-ef8c1f8a831a",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stakataka.Name",
    display_name="Stakataka",
    searchable_by=["Stakataka", "Basic", "Ultra Beast", "Stakataka"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=106,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=805,
    abilities=[
        Ability(
            title="Wall of Stone",
            game_text="If your opponent has 3 or fewer Prize cards remaining, this Pok\u00e9mon's maximum HP is 200.",
            effect=unimplemented,
        ),
        Attack(
            title="Top Down",
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=unimplemented,
        ),
    ],
)